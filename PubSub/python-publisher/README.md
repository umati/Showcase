# UA4MT Publisher — OPC UA PubSub over MQTT (without a Server)

This project implements a lightweight **OPC UA PubSub JSON publisher** for
machine tools following the [UA4MT](https://opcfoundation.org/developer-tools/documents/view/199)
(OPC 40501-1) companion specification. It publishes to the
[umati](https://umati.org/) dashboard and any other OPC UA PubSub-enabled
application.

The key idea: **no OPC UA server or SDK is required**. The publisher constructs
OPC UA Part 14 JSON messages using only generic Python libraries (`paho-mqtt`,
`json`, `pydantic`) and publishes them directly over MQTT.

```text
Companion Spec NodeSet  +  Instance NodeSet
                │                  │
                └──────┬───────────┘
                       ▼
          Pydantic data model (Python)
                       │
                       ▼
            OPC UA Part 14 JSON envelopes
              (ua-metadata + ua-data)
                       │
                       ▼
                 MQTT (paho-mqtt)
                       │
                       ▼
            umati.app / PubSub subscribers
```

## Components

### `simulator.py` — The Publisher

The main component. It runs in three phases:

1. **Publish metadata** - reads `data/metadata_*.json` files and publishes them
   as **retained** MQTT messages on `…/metadata/…` topics. This tells
   subscribers what fields exist and what data types they have.
2. **Initialize machine** - creates a nested `ShowcaseMachineTool` Pydantic
   object with realistic initial values (spindle speed, feed override, machine
   state, stack lights, location, …) and publishes the initial state for every
   topic.
3. **Simulation loop** - mutates values each tick and publishes only the
   changed topics as `ua-data` messages. Optionally re-publishes metadata at a
   configurable interval.

Field names are converted from Python `snake_case` to OPC UA PascalCase
(e.g. `feed_override` → `FeedOverride`), except `virtual_id` which maps to
`virtualId` (an umati gateway convention).

### `showcasemachine_classes.py` — The Data Model

Pydantic classes that mirror the OPC UA object hierarchy from the instance
NodeSet. Each class represents one node in the address space; scalar variables
are fields, child objects are sub-models. This file is the Python equivalent
of the instance NodeSet.


### `data/` — Metadata and Sample Data Files

Contains two sets of JSON files captured from a reference OPC UA server:

| File pattern | Used by | Purpose |
|---|---|---|
| `metadata_*.json` | `simulator.py` | **Actively loaded and published** as retained MQTT messages (Phase 1) |
| `data_*.json` | - | Reference samples showing what data messages look like; not loaded by any component |

Each file stores the MQTT topic and the JSON payload together:

```json
{
    "topic": "opcua/umati/v3/json/metadata/vdw/server-cpp-dev/ShowcaseMachineTool/Monitoring/Spindle",
    "payload": { "MessageType": "ua-metadata", "MetaData": { "Fields": [...] }, ... }
}
```

## MQTT Topic Layout

Topics follow the standard umati convention:

```text
{TOPIC_PREFIX}/{message_type}/{COMPANY_ID}/{PUBLISHER_ID}/{machine_browse_path}
```

For example with the default configuration:

```text
opcua/umati/v3/json/metadata/vdw/simulator-001/SvenShowcaseMachineTool/Monitoring/Spindle
opcua/umati/v3/json/data/vdw/simulator-001/SvenShowcaseMachineTool/Monitoring/Spindle
```

The machine name can be changed via `MACHINE_NAME` in `.env` without renaming
the Python class.

## Message Structure

### `ua-metadata` (published once, retained)

Describes the fields and data types for a topic so subscribers can decode the
payload:

```json
{
    "MessageId": "47f11ef2-...",
    "MessageType": "ua-metadata",
    "PublisherId": "simulator-001",
    "DataSetWriterId": 207,
    "MetaData": {
        "Namespaces": ["http://opcfoundation.org/UA/", "..."],
        "Name": "ns=17;i=59047",
        "Fields": [
            { "Name": "IsRotating", "BuiltInType": 1, "DataType": { "Id": 1 } },
            { "Name": "Override",   "BuiltInType": 11, "DataType": { "Id": 11 } }
        ]
    }
}
```

### `ua-data` (published continuously)

Carries the current machine values:

```json
{
    "MessageId": "2eac7007-...",
    "MessageType": "ua-data",
    "PublisherId": "simulator-001",
    "Messages": [{
        "Payload": {
            "IsRotating": true,
            "Override": 103.2,
            "Name": "Spindle",
            "virtualId": "17:SvenShowcaseMachineTool.5:Monitoring.17:Spindle"
        }
    }]
}
```

Each topic's payload contains **only the scalar variables for that node** —
child objects are published on their own sub-topics.

## Configuration

Copy `.env.example` to `.env` and fill in your values:

```env
# MQTT Broker
MQTT_HOST=fe02umati.isw.uni-stuttgart.de
MQTT_PORT=443
MQTT_USER=your-username
MQTT_PASSWORD=your-password

# Machine identity
MACHINE_NAME=SvenShowcaseMachineTool
MACHINE_LOCATION=VIRTUAL 2 1/N 48.1351 E 11.5820

# Simulator settings
SIM_INTERVAL=2
METADATA_INTERVAL=60

# Topic layout
TOPIC_PREFIX=opcua/umati/v3/json
COMPANY_ID=vdw
PUBLISHER_ID=simulator-001
```

## Running

Requires Python ≥ 3.8.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the publisher:

```bash
python simulator.py
```

The simulator publishes changing values every `SIM_INTERVAL` seconds.
