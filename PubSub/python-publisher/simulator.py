# SPDX-License-Identifier: MIT

"""
UMATI ShowcaseMachineTool Simulator

Publishes OPC UA Pub/Sub messages over MQTT to simulate a machine tool.
Uses the Pydantic classes from showcasemachine_classes.py as the data model.

Steps:
  1. Publishes all metadata messages from data/ (one-time, retained)
  2. Fills the machine model with realistic initial values
  3. Runs a simulation loop that mutates values and publishes data messages
"""

import paho.mqtt.client as mqtt
import json
import time
import random
import glob
import math
import uuid
import os
from dotenv import load_dotenv
import showcasemachine_classes as smc

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "fe02umati.isw.uni-stuttgart.de")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
PUBLISH_INTERVAL = float(os.getenv("SIM_INTERVAL", 2.0))  # seconds between updates
# Seconds between (re-)publishing metadata messages. Set to 0 to publish only once at startup.
METADATA_INTERVAL = float(os.getenv("METADATA_INTERVAL", 60.0))
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
MACHINE_NAME = os.getenv("MACHINE_NAME", "SvenShowcaseMachineTool")
MACHINE_LOCATION = os.getenv(
    "MACHINE_LOCATION", "VIRTUAL 2 1/N 48.1351 E 11.5820"
)
# The base topic prefix — must match what the collector subscribes to
TOPIC_PREFIX = os.getenv("TOPIC_PREFIX", "opcua/umati/v3/json")
COMPANY_ID = os.getenv("COMPANY_ID", "vdw")
PUBLISHER_ID = os.getenv("PUBLISHER_ID", "simulator-001")


# ─────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────

def to_pascal_case(snake_str):
    """Convert snake_case to PascalCase. e.g. 'signal_color' -> 'SignalColor'."""
    return "".join(word.capitalize() for word in snake_str.split("_"))


def model_to_pascal_payload(model):
    """Dump a Pydantic model to a dict with PascalCase keys (flat, no nesting).
    
    Only includes scalar fields (skips sub-models) and non-None values.
    This mirrors how OPC UA data messages carry only the leaf values
    for a given topic, not the full tree.
    """
    payload = {}
    for field_name, field_info in model.model_fields.items():
        value = getattr(model, field_name)
        if value is None:
            continue
        # Skip sub-model fields — those are published on their own topic
        if isinstance(value, smc.BaseModel):
            continue
        # Skip list fields (like active_errors)
        if isinstance(value, list):
            continue
        # Convert key to PascalCase, except virtualId stays as-is
        if field_name == "virtual_id":
            payload["virtualId"] = value
        else:
            payload[to_pascal_case(field_name)] = value
    return payload


def build_data_message(payload_dict):
    """Wrap a payload dict in the OPC UA Part 14 JSON data message envelope."""
    return {
        "MessageId": str(uuid.uuid4()),
        "MessageType": "ua-data",
        "PublisherId": PUBLISHER_ID,
        "Messages": [
            {
                "Payload": payload_dict
            }
        ]
    }


# Mapping from Pydantic attribute path → MQTT topic path
# This handles the cases where snake_case doesn't round-trip cleanly
# (e.g. channel_1 → "Channel 1", light_0 → "Light 0")
TOPIC_MAP = {
    "":                                                          "ShowcaseMachineTool",
    "identification":                                            "ShowcaseMachineTool/Identification",
    "production":                                                "ShowcaseMachineTool/Production",
    "production/active_program":                                 "ShowcaseMachineTool/Production/ActiveProgram",
    "production/active_program/state":                           "ShowcaseMachineTool/Production/ActiveProgram/State",
    "monitoring":                                                "ShowcaseMachineTool/Monitoring",
    "monitoring/machine_tool":                                   "ShowcaseMachineTool/Monitoring/MachineTool",
    "monitoring/stacklight":                                     "ShowcaseMachineTool/Monitoring/Stacklight",
    "monitoring/stacklight/light_0":                             "ShowcaseMachineTool/Monitoring/Stacklight/Light 0",
    "monitoring/stacklight/light_1":                             "ShowcaseMachineTool/Monitoring/Stacklight/Light 1",
    "monitoring/stacklight/light_2":                             "ShowcaseMachineTool/Monitoring/Stacklight/Light 2",
    "monitoring/channel_1":                                      "ShowcaseMachineTool/Monitoring/Channel 1",
    "monitoring/spindle":                                        "ShowcaseMachineTool/Monitoring/Spindle",
    "notification":                                              "ShowcaseMachineTool/Notification",
    "equipment":                                                 "ShowcaseMachineTool/Equipment",
    "equipment/tools":                                           "ShowcaseMachineTool/Equipment/Tools",
    "equipment/tools/tool1":                                     "ShowcaseMachineTool/Equipment/Tools/Tool1",
}

# Use a distinct machine name in the MQTT topics without changing the generated Python model class name.
TOPIC_MAP = {
    attr_path: topic.replace("ShowcaseMachineTool", MACHINE_NAME)
    for attr_path, topic in TOPIC_MAP.items()
}


def replace_machine_ids(model):
    """Replace the default machine name in virtual IDs throughout the model."""
    for field_name in model.model_fields:
        value = getattr(model, field_name)
        if isinstance(value, smc.BaseModel):
            replace_machine_ids(value)
        elif isinstance(value, str):
            setattr(
                model,
                field_name,
                value.replace("17:ShowcaseMachineTool", f"17:{MACHINE_NAME}"),
            )


def replace_strings_in_payload(value):
    """Update virtual IDs in metadata while leaving namespace names intact."""
    if isinstance(value, dict):
        return {key: replace_strings_in_payload(item) for key, item in value.items()}
    if isinstance(value, list):
        return [replace_strings_in_payload(item) for item in value]
    if isinstance(value, str):
        return value.replace("17:ShowcaseMachineTool", f"17:{MACHINE_NAME}")
    return value


def publish_data(client, attr_path, model):
    """Publish a data message for the given model at the given attribute path."""
    topic_suffix = TOPIC_MAP.get(attr_path)
    if topic_suffix is None:
        return
    topic = f"{TOPIC_PREFIX}/data/{COMPANY_ID}/{PUBLISHER_ID}/{topic_suffix}"
    payload = model_to_pascal_payload(model)
    if not payload:
        return
    message = build_data_message(payload)
    client.publish(topic, json.dumps(message))


# ─────────────────────────────────────────────────────────
# Phase 1: Publish Metadata (from existing JSON files)
# ─────────────────────────────────────────────────────────

def publish_all_metadata(client):
    """Read all metadata JSON files from data/ and publish them as retained messages."""
    metadata_files = glob.glob("data/metadata_*.json")
    count = 0
    for filepath in sorted(metadata_files):
        with open(filepath, "r") as f:
            data = json.load(f)
        topic = data["topic"]
        topic = topic.replace("ShowcaseMachineTool", MACHINE_NAME)
        topic = topic.replace("vdw", COMPANY_ID)
        topic = topic.replace("server-cpp-dev", PUBLISHER_ID)
        topic = topic.replace("opcua/umati/v3/json", TOPIC_PREFIX)
        print(f"Publing to {topic}")
        payload = data["payload"]
        payload = replace_strings_in_payload(payload)
        client.publish(topic, json.dumps(payload), retain=True)
        count += 1
    print(f"[Simulator] Published {count} metadata messages (retained)")


# ─────────────────────────────────────────────────────────
# Phase 2: Initialize Machine with Realistic Values
# ─────────────────────────────────────────────────────────

def create_initial_machine():
    """Create a ShowcaseMachineTool with realistic initial state."""
    m = smc.ShowcaseMachineTool(
        virtual_id="17:ShowcaseMachineTool",
        identification=smc.Identification(
            serial_number="SIM-2026-001",
            product_instance_uri=f"https://simulator.umati.app/{MACHINE_NAME}",
            manufacturer="UMATI Simulator",
            year_of_construction=2026,
            product_code="SIM-MT-001",
            software_revision="v1.0.0-sim",
            device_class="Machining centre (other)",
            location=MACHINE_LOCATION,
            model="SimulatedMachineTool",
            virtual_id="17:ShowcaseMachineTool.2:Identification",
        ),
        production=smc.Production(
            virtual_id="17:ShowcaseMachineTool.5:Production",
            active_program=smc.ActiveProgram(
                number_in_list=0,
                name="SimProgram_001.nc",
                virtual_id="17:ShowcaseMachineTool.5:Production.5:ActiveProgram",
                state=smc.State(
                    current_state="Running",
                    virtual_id="17:ShowcaseMachineTool.5:Production.5:ActiveProgram.5:State",
                ),
            ),
        ),
        monitoring=smc.Monitoring(
            virtual_id="17:ShowcaseMachineTool.5:Monitoring",
            machine_tool=smc.MachineTool(
                operation_mode=1,
                power_on_duration=3600,
                virtual_id="17:ShowcaseMachineTool.5:Monitoring.5:MachineTool",
            ),
            stacklight=smc.Stacklight(
                stacklight_mode=1,
                node_version="1",
                virtual_id="17:ShowcaseMachineTool.5:Monitoring.5:Stacklight",
                light_0=smc.StacklightElement(
                    number_in_list=0, is_part_of_base=True,
                    signal_on=True, signal_mode=0, signal_color=3,  # Green
                    virtual_id="17:ShowcaseMachineTool.5:Monitoring.5:Stacklight.5:Light 0",
                ),
                light_1=smc.StacklightElement(
                    number_in_list=1, is_part_of_base=True,
                    signal_on=False, signal_mode=0, signal_color=4,  # Yellow
                    virtual_id="17:ShowcaseMachineTool.5:Monitoring.5:Stacklight.5:Light 1",
                ),
                light_2=smc.StacklightElement(
                    number_in_list=2, is_part_of_base=True,
                    signal_on=False, signal_mode=0, signal_color=1,  # Red
                    virtual_id="17:ShowcaseMachineTool.5:Monitoring.5:Stacklight.5:Light 2",
                ),
            ),
            channel_1=smc.Channel1(
                channel_state=0,  # Active
                feed_override=100.0,
                channel_mode=0,  # Automatic
                name="Channel 1",
                virtual_id="17:ShowcaseMachineTool.5:Monitoring.17:Channel 1",
            ),
            spindle=smc.Spindle(
                is_rotating=True,
                override=100.0,
                is_used_as_axis=False,
                name="Spindle",
                virtual_id="17:ShowcaseMachineTool.5:Monitoring.17:Spindle",
            ),
        ),
        notification=smc.Notification(
            virtual_id="17:ShowcaseMachineTool.5:Notification",
        ),
        equipment=smc.Equipment(
            virtual_id="17:ShowcaseMachineTool.5:Equipment",
            tools=smc.Tools(
                node_version="1",
                virtual_id="17:ShowcaseMachineTool.5:Equipment.5:Tools",
                tool1=smc.Tool1(
                    locked=False,
                    control_identifier_interpretation=0,
                    control_identifier1=1,
                    name="Tool 1",
                    virtual_id="17:ShowcaseMachineTool.5:Equipment.5:Tools.17:Tool1",
                ),
            ),
        ),
    )
    replace_machine_ids(m)
    return m


# ─────────────────────────────────────────────────────────
# Phase 3: Simulation Loop — Mutate & Publish
# ─────────────────────────────────────────────────────────

def simulate_tick(machine, tick):
    """Mutate machine values to simulate a running machine.
    
    Returns a list of (attr_path, model) tuples for topics that changed.
    """
    changed = []
    m = machine.monitoring

    # Spindle override oscillates between 85-115% with some noise
    m.spindle.override = round(50 + 15 * math.sin(tick * 0.1) + random.uniform(-2, 2), 1)
    m.spindle.is_rotating = True
    changed.append(("monitoring/spindle", m.spindle))

    # Feed override drifts around 100%
    m.channel_1.feed_override = round(50 + 10 * math.cos(tick * 0.08) + random.uniform(-1, 1), 1)
    changed.append(("monitoring/channel_1", m.channel_1))

    # Power on duration increments every tick
    m.machine_tool.power_on_duration += int(PUBLISH_INTERVAL)
    changed.append(("monitoring/machine_tool", m.machine_tool))

    # Stacklight: green on while running, occasionally flash yellow
    m.stacklight.light_0.signal_on = True    # Green always on
    m.stacklight.light_1.signal_on = random.random() < 0.1  # Yellow 10% chance
    m.stacklight.light_2.signal_on = False   # Red off
    changed.append(("monitoring/stacklight/light_0", m.stacklight.light_0))
    changed.append(("monitoring/stacklight/light_1", m.stacklight.light_1))
    changed.append(("monitoring/stacklight/light_2", m.stacklight.light_2))

    # Program state: mostly running, occasionally changes
    if random.random() < 0.05:
        machine.production.active_program.state.current_state = random.choice(
            ["Running", "Interrupted", "Ended"]
        )
        changed.append(("production/active_program/state", machine.production.active_program.state))

    return changed


# ─────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[Simulator] Connected to MQTT broker at {MQTT_HOST}:{MQTT_PORT}")
    else:
        print(f"[Simulator] Connection failed with code {rc}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, transport="websockets")
    client.on_connect = on_connect
    client.ws_set_options(path="/ws")
    client.tls_set()
    if MQTT_USER and MQTT_PASSWORD:
        client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

    print(f"[Simulator] Connecting to {MQTT_HOST}:{MQTT_PORT}...")
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()

    # Wait for connection
    time.sleep(1)

    # Phase 1: Publish all metadata
    publish_all_metadata(client)

    # Phase 2: Create machine with initial values
    machine = create_initial_machine()

    # Publish initial state for ALL topics once
    print("[Simulator] Publishing initial state for all topics...")
    for attr_path, topic_suffix in TOPIC_MAP.items():
        # Navigate to the sub-model at this attr_path
        target = machine
        if attr_path:
            for part in attr_path.split("/"):
                target = getattr(target, part, None)
                if target is None:
                    break
        if target and isinstance(target, smc.BaseModel):
            publish_data(client, attr_path, target)

    print(f"[Simulator] Starting simulation loop (interval={PUBLISH_INTERVAL}s)")
    if METADATA_INTERVAL > 0:
        print(f"[Simulator] Re-publishing metadata every {METADATA_INTERVAL}s")
    else:
        print("[Simulator] Metadata is published once at startup only")
    print("[Simulator] Press Ctrl+C to stop\n")

    # Phase 3: Simulation loop
    tick = 0
    last_metadata_publish = time.time()
    try:
        while True:
            changed = simulate_tick(machine, tick)
            for attr_path, model in changed:
                publish_data(client, attr_path, model)

            # Periodically re-publish metadata messages
            if METADATA_INTERVAL > 0 and (time.time() - last_metadata_publish) >= METADATA_INTERVAL:
                publish_all_metadata(client)
                last_metadata_publish = time.time()

            # Print a status line
            sp = machine.monitoring.spindle
            ch = machine.monitoring.channel_1
            st = machine.production.active_program.state
            print(
                f"  tick={tick:04d}  "
                f"Spindle={sp.override:5.1f}%  "
                f"Feed={ch.feed_override:5.1f}%  "
                f"State={st.current_state:<12s}  "
                f"PowerOn={machine.monitoring.machine_tool.power_on_duration}s"
            )

            tick += 1
            time.sleep(PUBLISH_INTERVAL)

    except KeyboardInterrupt:
        print("\n[Simulator] Stopped.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
