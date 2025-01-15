# umati showcase information model for Laser Systems

In the following the umati showcase describes the additional information on top of the [OPC 40501-1 UA for Laser](https://reference.opcfoundation.org/LaserSystems/v100/docs/) companion specification.

## NodeSets

[Normative NodeSet hosted by the OPC Foundation](https://github.com/OPCFoundation/UA-Nodeset/tree/latest/LaserSystems)



## General information valid for the umati showcase demonstration

| **DISCLAIMER** | For all applications the OPC UA server is to be configured without predefined NodeIds for the instances. Clients need to utilize the Services [Browse](https://reference.opcfoundation.org/Core/docs/Part4/5.8.2/) and [TranslateBrowsePathsToNodeIds](https://reference.opcfoundation.org/Core/docs/Part4/5.8.4/) to access nodes of interest. |

### Identification data

The identification for Laser Systems are inherited from the Machinery companion specification.
To fill the demo dashboard machine page with the most content the variables marked with a **strong mandatory** should be provided if you like to look the machine identification nicely.

#### [**MachineIdentificationType Definition**](https://reference.opcfoundation.org/Machinery/docs/8.6/)

| **Attribute** | **Value** |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| BrowseName | MachineIdentificationType | | | | |
| IsAbstract | False | | | | |
| Description | Contains information about the identification and nameplate of a machine | | | | |
|     |     |     |     |     |     |
| **References** | **NodeClass** | **BrowseName** | **DataType** | **TypeDefinition** | **Other** |
| Subtype of the 2:FunctionalGroupType defined in OPC 10000-100, i.e. inheriting the InstanceDeclarations of that Node. | | | | | |
| 0:HasProperty | Variable | 0:DefaultInstanceBrowseName | 0:QualifiedName | 0:PropertyType |     |
| 0:HasInterface | ObjectType | IMachineVendorNameplateType | | | |
| 0:HasInterface | ObjectType | IMachineTagNameplateType | | | |
| Applied from IMachineVendorNameplateType |     |     |     |     |     |
| 0:HasProperty | Variable | 2:ProductInstanceUri | 0:String | 0:PropertyType | M, RO |
| 0:HasProperty | Variable | 2:Manufacturer | 0:LocalizedText | 0:PropertyType | M, RO |
| 0:HasProperty | Variable | 2:ManufacturerUri | 0:String | 0:PropertyType | O, RO |
| 0:HasProperty | Variable | **2:Model** | 0:LocalizedText | 0:PropertyType | **M**, RO |
| 0:HasProperty | Variable | **2:ProductCode** | 0:String | 0:PropertyType | **M**, RO |
| 0:HasProperty | Variable | 2:HardwareRevision | 0:String | 0:PropertyType | O, RO |
| 0:HasProperty | Variable | **2:SoftwareRevision** | 0:String | 0:PropertyType | **M**, RO |
| 0:HasProperty | Variable | 2:DeviceClass | 0:String | 0:PropertyType | O, RO |
| 0:HasProperty | Variable | 2:SerialNumber | 0:String | 0:PropertyType | M, RO |
| 0:HasProperty | Variable | **YearOfConstruction** | UInt16 | 0:PropertyType | **M**, RO |
| 0:HasProperty | Variable | MonthOfConstruction | Byte | 0:PropertyType | O, RO |
| 0:HasProperty | Variable | InitialOperationDate | DateTime | 0:PropertyType | O, RO |
| Applied from IMachineTagNameplateType |     |     |     |     |     |
| 0:HasProperty | Variable | 2:AssetId | 0:String | 0:PropertyType | O, RW |
| 0:HasProperty | Variable | 2:ComponentName | 0:LocalizedText | 0:PropertyType | O, RW |
| 0:HasProperty | Variable | **Location** | 0:String | 0:PropertyType | **M**, RW |

#### Special requirements for correct location of the machine icon on the dashboard

The instance _Location_ property is evaluated according to the special requirements detailed [here](../Dashboard.md#location-of-fair-machine-and-software-icons-on-the-dashboard) to place a map icon for the machine.

### Adaption of the provided information models for your purpose

- The provided NodeSet contains the address space with the ObjectTypes, VariableTypes and DataTypes of the Laser Systems companion specification and **must not** be changed.
- Change the URI of the instance namespace (optional, but recommended)

  `http://www.<MANUFACTURERDOMAIN>/example`

- The rules for creating a URI can be found online. Please follow [this link](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier). 
In the case of a URL as a URI, it is not necessary that the site actually exists, it only identifies the machine uniquely. 
In order to simplify debugging it is recommended to choose a URI which allows an identification of the machine also for third persons, e.g. by including the company name.

- The machine will get a unique identifier like clientId%3Dvdw%7Csmplsrv1%3Bnsu%3Dhttp%3A_2F_2Fwww.wenzel-group.com_2FWenzel_20LH_2087_2F%3Bi%3D66382 <clientId><mqttusername><NamespaceUri><EntryNodeId> in the MQTT tree and in the Dashboard url.

## Value mapping between OPC UA companion specification and umati.app MachineTool page

### Laser System - Overview

![Overview](../img/Laser/Overview.png "Laser System Overview")

### Active Program Statusbar

For the status overview in the dashboard, the _StateNumber_ of the _4:Monitoring_.LasterSystemStatus.LaserSystemState_StateMachineType.CurrentState.Number_ is stored and plotted over time. The status bar **does NOT relate to the stacklight** status!

Each status is assigned to a color, the color scheme is here (subject to change):

| State |Number | Color |
| --- | --- | --- |
| Off |0| &#EAEAEA; Grey |
| EnergySaving |1| &#EAEAEA; Grey |
| Idle |2| &#EAEAEA; Grey |
| SetUp |3|&#EAEAEA; Grey |
| LaserReady |4|&#EAEAEA; Grey |
| Maintenance | 5 | &#EAEAEA; Grey|
| Error | 6 | &#EAEAEA; Grey|
| LaserOn | 7 | &#00b20e; Green|
| Any other (unspecified) state | | &#9899; Black |

A gap is left for periods of time in which no data was recorded (e.g. machine offline). An exemplary timeline is shown above.

### Laser Systems - Identification

![Identification](../img/MachineTool/MT-Identification.png "Identification")

### Laser Systems- Production

![Production](../img/Laser/Production.png "Production")

### Laser Systems - Monitoring

![Monitoring](../img/Laser/Monitoring.png "Monitoring")
