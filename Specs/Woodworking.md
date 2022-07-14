# umati showcase information model for Wood Working machines

In the following the umati showcase describes the additional information on top of the [OPC 40550 UA for Woodworking](https://) companion specification.

Please refer to the provided xml-Nodesets or UaModeler-project for exemplary implementation.

The following describes the umati showcase information model for Wood Working.

For participants that are familiar with the information model, we have included comments and descriptions about changes between the release candidate information model and the showcase information model.

All participants not familiar with the release candidate information model do not need to review these changes in detail but rather follow the described model and refer to the provided xml Nodeset files and UA modeler project.

## NodeSets for the showcase

[Release Candidate NodeSet](https://github.com/umati/Sample-Server/tree/main/model/Woodworking)

[Protoyping NodeSet](https://github.com/umati/Woodworking/tree/main/Model) **Remark:** You have to be umati partner and added to the access list. (Contact: [info@umati.org](mailto:info@umati.org))

## General information valid for the umati showcase demonstration

| **DISCLAIMER** | For all applications the OPC UA server is to be configured without predefined NodeIDs for the instances. Clients will need to browse Instances or translate BrowsePaths find the NodeID for accessing the address space and available instances. |
| --- | --- |

### Identification data

The identification for machine tools are inherited from the Machinery companion specification.
To fill the demo dashboard machine page with the most content the variables marked with a **strong mandatory** should be provided if you like to look the machine identification nicely.

#### [**MachineIdentificationType Definition**](https://reference.opcfoundation.org/Machinery/docs/8.6/)

| **Attribute** | **Value** |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| BrowseName | MachineIdentificationType |
| IsAbstract | False |
| Description | Contains information about the identification and nameplate of a machine |
|     |     |     |     |     |     |
| **References** | **NodeClass** | **BrowseName** | **DataType** | **TypeDefinition** | **Other** |
| Subtype of the 2:FunctionalGroupType defined in OPC 10000-100, i.e. inheriting the InstanceDeclarations of that Node. |
| 0:HasProperty | Variable | 0:DefaultInstanceBrowseName | 0:QualifiedName | 0:PropertyType |     |
| 0:HasInterface | ObjectType | IMachineVendorNameplateType |
| 0:HasInterface | ObjectType | IMachineTagNameplateType |
| Applied from IMachineVendorNameplateType |     |     |     |     |     |
| 0:HasProperty | Variable | 2:ProductInstanceUri | 0:String | 0:PropertyType | M, RO |
| 0:HasProperty | Variable | 2:Manufacturer | 0:LocalizedText | 0:PropertyType | M, RO |
| 0:HasProperty | Variable | 2:ManufacturerUri | 0:String | 0:PropertyType | O, RO |
| 0:HasProperty | Variable | **2:Model** | 0:LocalizedText | 0:PropertyType | **M**, RO |
| 0:HasProperty | Variable | **2:ProductCode** | 0:String | 0:PropertyType | **M**, RO |
| 0:HasProperty | Variable | 2:HardwareRevision | 0:String | 0:PropertyType | O, RO |
| 0:HasProperty | Variable | **2:SoftwareRevision** | 0:String | 0:PropertyType | **M**, RO |
| 0:HasProperty | Variable | 2:DeviceClass | 0:String | 0:PropertyType | **M**, RO |
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

#### FAIR Shortnames

Fair shortnames are defined [here.](Fairs.md)

### Adaption of the provided information models for your purpose

- The provided NodeSet contains the address space with the ObjectTypes, VariableTypes and DataTypes of the Woodworking companion specificaion and **must not** be changed.
- Change the URI of the instance namespace (optional, but recommended)

  `http://www.<MANUFACTURERDOMAIN>/example`

- The rules for creating a URI can be found online. Please follow [this link](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier). In the case of a URL as a URI, it is not necessary that the site actually exists, it only identifies the machine uniquely. In order to simplify debugging it is recommended to choose a URI which allows an identification of the machine also for third persons, e.g. by including the company name.

- The machine will get a unique NamespaceURI after being integrated to the datahub by addition of a suffix to ensure unique namespaces.

## Value mapping between OPC UA companion specification and umati.app Woodworking

### Wood Working - Overview

![Overview](../img/Woodworking/WWM-Overview.png "WW Overview")

### Active Program Statusbar

For the status overview in the dashboard, the _State_ of the _RecipeInRun_ is stored and plotted over time. The status bar **does NOT relate to the stacklight** status!

Each status is assigned to a color, the color scheme is here (subject to change):

| State | Color |
| --- | --- |
| STANDBY | &#9898; Gray |
| WORKING | &#128994; Green |
| READY | &#128992; Yellow |
| ERROR | &#128308; Red |
| Any other (unspecified) state | &#9899; Black |

A gap is left for periods of time in which no data was recorded (e.g. machine offline). An exemplary timeline is shown above.

### Wood Working - Identification

![Identification](../img/Woodworking/WWM-Identification.png "MT Identification")

### Wood Working - Active Program

![ActiveProgram](../img/Woodworking/WWM-ActiveProgram.png "MT ActiveProgram")

### Wood Working - Monitoring Stationary

![MonitoringStationary](../img/Woodworking/WWM-MonitoringStationary.png "MT Monitoring")

### Wood Working - Monitoring Throughfeed

![MonitoringThroughfeed](../img/Woodworking/WWM-MonitoringThroughfeed.png "MT Monitoring")

### Device Classes

Based on the _DeviceClass_ the image for the individual machine page is selected.

This is the current mapping:

#### Throughfeed

- ProfilingMachine
- EdgebandingMachine
- BoringMachine
- SandingMachine
- HandlingMachine

#### Stationary

- MachiningCenter
- Press
- SawingMachine
