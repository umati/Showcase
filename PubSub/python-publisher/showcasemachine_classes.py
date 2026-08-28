# SPDX-License-Identifier: MIT
from pydantic import BaseModel, Field
from typing import Optional, Any


# ---------------------------------------------------------
# Level 4+: Deep Leaf / Detail Nodes
# ---------------------------------------------------------

class CurrentState(BaseModel):
    """Production/ActiveProgram/State/CurrentState
    Fields: Number, Id, virtualId
    Note: This is a leaf sub-topic. The parent State class has
    current_state as a scalar (str). This sub-topic's data flows
    through the data_store fallback in collector.py.
    """
    number: Optional[int] = None
    id: Optional[str] = None
    virtual_id: Optional[str] = None


class State(BaseModel):
    """Production/ActiveProgram/State
    Fields: CurrentState, virtualId
    """
    current_state: Optional[str] = None
    virtual_id: Optional[str] = None


class ActiveProgram(BaseModel):
    """Production/ActiveProgram
    Fields: NumberInList, Name, virtualId
    """
    number_in_list: Optional[int] = None
    name: Optional[str] = None
    state: Optional[State] = Field(default_factory=State)
    virtual_id: Optional[str] = None


class StacklightElement(BaseModel):
    """Monitoring/Stacklight/Light 0, Light 1, Light 2
    Fields: NumberInList, IsPartOfBase, SignalOn, SignalMode, SignalColor, virtualId
    """
    number_in_list: Optional[int] = None
    is_part_of_base: Optional[bool] = None
    signal_on: Optional[bool] = None
    signal_mode: Optional[int] = None
    signal_color: Optional[int] = None
    virtual_id: Optional[str] = None


class Stacklight(BaseModel):
    """Monitoring/Stacklight
    Fields: StacklightMode, NodeVersion, virtualId
    Children: Light 0, Light 1, Light 2
    """
    stacklight_mode: Optional[int] = None
    node_version: Optional[str] = None
    light_0: Optional[StacklightElement] = Field(default_factory=StacklightElement)
    light_1: Optional[StacklightElement] = Field(default_factory=StacklightElement)
    light_2: Optional[StacklightElement] = Field(default_factory=StacklightElement)
    virtual_id: Optional[str] = None


class MachineTool(BaseModel):
    """Monitoring/MachineTool
    Fields: OperationMode, PowerOnDuration, virtualId
    """
    operation_mode: Optional[int] = None
    power_on_duration: Optional[int] = None
    virtual_id: Optional[str] = None


class Spindle(BaseModel):
    """Monitoring/Spindle
    Fields: IsRotating, Override, IsUsedAsAxis, Name, virtualId
    Note: Override is also a leaf sub-topic with its own fields
    (EngineeringUnits, EURange, virtualId). That sub-topic's data
    flows through the data_store fallback.
    """
    is_rotating: Optional[bool] = None
    override: Optional[float] = None
    is_used_as_axis: Optional[bool] = None
    name: Optional[str] = None
    virtual_id: Optional[str] = None


class Channel1(BaseModel):
    """Monitoring/Channel 1
    Fields: ChannelState, FeedOverride, ChannelMode, Name, virtualId
    Note: FeedOverride is also a leaf sub-topic with its own fields
    (EURange, EngineeringUnits, virtualId). That sub-topic's data
    flows through the data_store fallback.
    """
    channel_state: Optional[int] = None
    feed_override: Optional[float] = None
    channel_mode: Optional[int] = None
    name: Optional[str] = None
    virtual_id: Optional[str] = None


class Tool1(BaseModel):
    """Equipment/Tools/Tool1
    Fields: Locked, ControlIdentifierInterpretation, ControlIdentifier1, Name, virtualId
    Note: Locked is also a leaf sub-topic with its own fields
    (ReasonForLocking, virtualId). That sub-topic's data flows
    through the data_store fallback.
    """
    locked: Optional[bool] = None
    control_identifier_interpretation: Optional[int] = None
    control_identifier1: Optional[int] = None
    name: Optional[str] = None
    virtual_id: Optional[str] = None


class Tools(BaseModel):
    """Equipment/Tools
    Fields: NodeVersion, virtualId
    """
    node_version: Optional[str] = None
    tool1: Optional[Tool1] = Field(default_factory=Tool1)
    virtual_id: Optional[str] = None


# ---------------------------------------------------------
# Level 3: Main Component Branches
# ---------------------------------------------------------

class Production(BaseModel):
    """Fields: virtualId"""
    active_program: Optional[ActiveProgram] = Field(default_factory=ActiveProgram)
    virtual_id: Optional[str] = None


class Monitoring(BaseModel):
    """Fields: virtualId"""
    machine_tool: Optional[MachineTool] = Field(default_factory=MachineTool)
    stacklight: Optional[Stacklight] = Field(default_factory=Stacklight)
    channel_1: Optional[Channel1] = Field(default_factory=Channel1)
    spindle: Optional[Spindle] = Field(default_factory=Spindle)
    virtual_id: Optional[str] = None


class Equipment(BaseModel):
    """Fields: virtualId"""
    tools: Optional[Tools] = Field(default_factory=Tools)
    virtual_id: Optional[str] = None


class Notification(BaseModel):
    """Fields: virtualId"""
    active_errors: Optional[list] = Field(default_factory=list)
    virtual_id: Optional[str] = None


class Identification(BaseModel):
    """Fields: SerialNumber, ProductInstanceUri, Manufacturer,
    YearOfConstruction, ProductCode, SoftwareRevision,
    DeviceClass, Location, Model, virtualId
    """
    device_class: Optional[str] = None
    location: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    product_code: Optional[str] = None
    product_instance_uri: Optional[str] = None
    serial_number: Optional[str] = None
    software_revision: Optional[str] = None
    year_of_construction: Optional[int] = None
    virtual_id: Optional[str] = None


# ---------------------------------------------------------
# Level 2: The Root Machine Tool Node
# ---------------------------------------------------------

class ShowcaseMachineTool(BaseModel):
    """Fields: virtualId"""
    production: Optional[Production] = Field(default_factory=Production)
    monitoring: Optional[Monitoring] = Field(default_factory=Monitoring)
    notification: Optional[Notification] = Field(default_factory=Notification)
    equipment: Optional[Equipment] = Field(default_factory=Equipment)
    identification: Optional[Identification] = Field(default_factory=Identification)
    virtual_id: Optional[str] = None