# PublishSubcribe (MQTT Transport and UA JSON encoding)

This page describe how to connect to the umati.app Dashboard by using PubSub instead of the server/client connection described in other parts of the Specification.

> PubSub allows the distribution of data and events from an OPC UA information source to interested observers inside a device network as well as in IT and analytics cloud systems.

* Detailed Specification of PubSub can be found at: [OPC 10000-14](https://reference.opcfoundation.org/Core/docs/Part14/) Part 14: PubSub
* The JSON mapping is describe in [Part14/7.2.3](https://reference.opcfoundation.org/Core/docs/Part14/7.2.3/)

## Setup

To connect with PubSub to the umati.app, the publisher could be implemented together with the OPC UA Server application on the same instance.
Additionally Gateways such as [UA-CloudPublisher](https://github.com/umati/UA-CloudPublisher) provided by Erich Barnstedt (@barnstee) or [OPC Pulisher (Microsoft Azure IoT)](https://github.com/Azure/Industrial-IoT#opc-publisher---standalone) can be used to subscribe to the OPC UA Server and publish the information.

`OPC UA Server/Publisher` -- MQTT/JSON --> `MQTT Broker`

`OPC UA Server` -- TCP binary --> `Gateway` -- MQTT/JSON --> `MQTT Broker`

## MQTT Broker

For the showcase two brokers are used:

`dev.umati.app`

``` json
    "Prefix": "<companyname>", // see Topic Structure for details
    "BrokerUrl": "opc.mqtt://dev.umati.app:443",
    "PublisherId": "<Applicationname>", // see Topic Structure for details
    "Username": "",
    "Password": "",

```

`umati.app`

``` json
    "Prefix": "<companyname>",
    "BrokerUrl": "opc.mqtt://umati.app:443",
    "PublisherId": "<Applicationname>",
    "Username": "",
    "Password": ""
```

## Topic Structure

* `<prefix>`: Free to choose, e.g company name, e.g, `isw`

* `<machine_id>` url encoding of e.g.: `prefix=<prefix>;nsu=<ns_uri of machine node>;<node id of machine node>`, e.g. 
`prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234`

The topics follow the browse paths.

### Data-Topic

```html
<prefix>/json/data/<machine_id>/_WriterGroup
```

### Metadata-Topics (Examples)

```html
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FDI_2F;name=Identification

<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Tool1
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=MachineTool
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Channel 1
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Spindle
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 0
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 1
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 2
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight

<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=State
<prefix>/json/metadata/<machine_id>/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram
```

## Examples

### Data Topic

`isw/json/data/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup`

```json
{
    "MessageId": null,
    "MessageType": "ua-data",
    "Messages": [
        {
            "DataSetWriterId": 9,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388877790,
                "MinorVersion": 388875340
            },
            "Timestamp": "2022-07-15T15:34:20.850936Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 32,
                        "Namespace": "http://opcfoundation.org/UA/MachineTool/"
                    }
                },
                "Name": {
                    "Body": "Basic Program"
                },
                "NumberInList": {
                    "Body": 0
                }
            }
        },
        {
            "DataSetWriterId": 8,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=State",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388876230,
                "MinorVersion": 388876050
            },
            "Timestamp": "2022-07-15T15:34:20.850992Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 24,
                        "Namespace": "http://opcfoundation.org/UA/MachineTool/"
                    }
                },
                "CurrentState": {
                    "Body": "Running"
                }
            }
        },
        {
            "DataSetWriterId": 7,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388865050,
                "MinorVersion": 388864420
            },
            "Timestamp": "2022-07-15T15:34:20.851015Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 1002,
                        "Namespace": "http://opcfoundation.org/UA/IA/"
                    }
                },
                "StacklightMode": {
                    "Body": 0
                },
                "NodeVersion": {
                    "Body": ""
                }
            }
        },
        {
            "DataSetWriterId": 6,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 2",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388872940,
                "MinorVersion": 388871100
            },
            "Timestamp": "2022-07-15T15:34:20.851047Z",
            "Payload": {
                "SignalColor": {
                    "Body": 2
                },
                "StacklightMode": {
                    "Body": 0
                },
                "IsPartOfBase": {
                    "Body": false
                },
                "SignalOn": {
                    "Body": true
                },
                "NumberInList": {
                    "Body": 2
                }
            }
        },
        {
            "DataSetWriterId": 5,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 1",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388870180,
                "MinorVersion": 388868310
            },
            "Timestamp": "2022-07-15T15:34:20.851108Z",
            "Payload": {
                "SignalColor": {
                    "Body": 4
                },
                "StacklightMode": {
                    "Body": 0
                },
                "IsPartOfBase": {
                    "Body": false
                },
                "SignalOn": {
                    "Body": true
                },
                "NumberInList": {
                    "Body": 1
                }
            }
        },
        {
            "DataSetWriterId": 4,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 0",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388867340,
                "MinorVersion": 388865450
            },
            "Timestamp": "2022-07-15T15:34:20.851161Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 1006,
                        "Namespace": "http://opcfoundation.org/UA/IA/"
                    }
                },
                "SignalColor": {
                    "Body": 1
                },
                "StacklightMode": {
                    "Body": 0
                },
                "IsPartOfBase": {
                    "Body": false
                },
                "SignalOn": {
                    "Body": true
                },
                "NumberInList": {
                    "Body": 0
                }
            }
        },
        {
            "DataSetWriterId": 3,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Spindle",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388862930,
                "MinorVersion": 388862090
            },
            "Timestamp": "2022-07-15T15:34:20.851214Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 22,
                        "Namespace": "http://opcfoundation.org/UA/MachineTool/"
                    }
                },
                "IsRotating": {
                    "Body": true
                },
                "IsUsedAsAxis": {
                    "Body": false
                },
                "Override": {
                    "Body": 103
                },
                "Name": {
                    "Body": "Spindle"
                }
            }
        },
        {
            "DataSetWriterId": 2,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Channel 1",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388860440,
                "MinorVersion": 388859470
            },
            "Timestamp": "2022-07-15T15:34:20.851239Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 16,
                        "Namespace": "http://opcfoundation.org/UA/MachineTool/"
                    }
                },
                "ChannelState": {
                    "Body": 1
                },
                "FeedOverride": {
                    "Body": 41.4300000001676380634307861328125
                },
                "ChannelMode": {
                    "Body": 0
                },
                "Name": {
                    "Body": "Channel 1"
                }
            }
        },
        {
            "DataSetWriterId": 1,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=MachineTool",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388858450,
                "MinorVersion": 388857720
            },
            "Timestamp": "2022-07-15T15:34:20.851283Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 26,
                        "Namespace": "http://opcfoundation.org/UA/MachineTool/"
                    }
                },
                "OperationMode": {
                    "Body": 1
                },
                "PowerOnDuration": {
                    "Body": 0
                }
            }
        },
        {
            "DataSetWriterId": 1,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388853500,
                "MinorVersion": 388853310
            },
            "Timestamp": "2022-07-15T15:34:20.851306Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 44,
                        "Namespace": "http://opcfoundation.org/UA/MachineTool/"
                    }
                },
                "NodeVersion": {
                    "Body": null
                }
            }
        },
        {
            "DataSetWriterId": 0,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Tool1",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388855620,
                "MinorVersion": 388853860
            },
            "Timestamp": "2022-07-15T15:34:20.851311Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 50,
                        "Namespace": "http://opcfoundation.org/UA/MachineTool/"
                    }
                },
                "ControlIdentifier1": {
                    "Body": 12
                },
                "ControlIdentifierInterpretation": {
                    "Body": 0
                },
                "Locked": {
                    "Body": false
                },
                "Name": {
                    "Body": "Tool1"
                }
            }
        },
        {
            "DataSetWriterId": 0,
            "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FDI_2F;name=Identification",
            "SequenceNumber": 24,
            "MetaDataVersion": {
                "MajorVersion": 388851690,
                "MinorVersion": 388847890
            },
            "Timestamp": "2022-07-15T15:34:20.851346Z",
            "Payload": {
                "TypeDefinition": {
                    "Body": {
                        "Id": 11,
                        "Namespace": "http://opcfoundation.org/UA/MachineTool/"
                    }
                },
                "YearOfConstruction": {
                    "Body": 2021
                },
                "MonthOfConstruction": {
                    "Body": 11
                },
                "Manufacturer": {
                    "Body": "umati Showcase"
                },
                "ProductInstanceUri": {
                    "Body": "https://showcase.umati.org/Specs/Machinetools.html"
                },
                "SerialNumber": {
                    "Body": "2021-15360620311222485159"
                },
                "Model": {
                    "Body": "ShowcaseMachineTool"
                },
                "ProductCode": {
                    "Body": "2653837gg1548"
                },
                "SoftwareRevision": {
                    "Body": "v1.02.1"
                },
                "DeviceClass": {
                    "Body": "Machining centre (other)"
                },
                "Location": {
                    "Body": "CIMT E8 B014/VIRTUAL 0 0/N 49.871215 E 8.654204"
                },
                "ComponentName": {
                    "Body": "umati Showcase Component"
                }
            }
        }
    ]
}
```

### Metadata Topics
```json
isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FDI_2F;name=Identification

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 0,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FDI_2F;name=Identification",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FDI_2F;name=Identification",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=11"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "19AF8453-36B8-1C2C-F8AF-EACEE9DE9DF9",
                "Properties": []
            },
            {
                "Name": "YearOfConstruction",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 4,
                "DataType": {
                    "Id": 5
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "31ADB51B-7D7E-D3C2-0BF0-CF6C58357387",
                "Properties": []
            },
            {
                "Name": "MonthOfConstruction",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 2,
                "DataType": {
                    "Id": 3
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "D7AA4248-E66F-8B2C-8D98-2962EEDE8D58",
                "Properties": []
            },
            {
                "Name": "Manufacturer",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 20,
                "DataType": {
                    "Id": 21
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "772218BF-8DC3-DDB0-0400-8008A51A4104",
                "Properties": []
            },
            {
                "Name": "ProductInstanceUri",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "36914B8E-69BB-9CD9-F7EF-CE0CEC3E6386",
                "Properties": []
            },
            {
                "Name": "SerialNumber",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "5DEDA318-14DF-D288-9F59-A5DAA32AD21D",
                "Properties": []
            },
            {
                "Name": "Model",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 20,
                "DataType": {
                    "Id": 21
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "19EF6AF1-AC68-DD0B-ADEA-CE6CD66D7667",
                "Properties": []
            },
            {
                "Name": "ProductCode",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "769FD65B-3522-FFC2-0DE0-AEBA2D526506",
                "Properties": []
            },
            {
                "Name": "SoftwareRevision",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "51FBA6C0-0095-8554-60E6-BEDB289259F5",
                "Properties": []
            },
            {
                "Name": "DeviceClass",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "2BA94D84-F95E-6C57-D78D-286264D69DE9",
                "Properties": []
            },
            {
                "Name": "Location",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "6FA63C23-4AF4-68F4-2172-D70D3B63F69F",
                "Properties": []
            },
            {
                "Name": "ComponentName",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 20,
                "DataType": {
                    "Id": 21
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "E924D793-A52A-25EE-9959-C53C7D672632",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388851690,
            "MinorVersion": 388847890
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Tool1

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 0,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Tool1",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Tool1",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=50"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "1B2CA533-7843-EF0F-5EB5-DB4DBBAB3A23",
                "Properties": []
            },
            {
                "Name": "ControlIdentifier1",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 6,
                "DataType": {
                    "Id": 7
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "629B03B6-A3BE-4247-2842-04C03793F94F",
                "Properties": []
            },
            {
                "Name": "ControlIdentifierInterpretation",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 26,
                "DataType": {
                    "Id": 69,
                    "Namespace": 5
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "90802AC3-7831-AE80-1CF1-6F16C55C05A0",
                "Properties": []
            },
            {
                "Name": "Locked",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "35DE50E3-B396-75B2-A1FA-BF7B6C1611E1",
                "Properties": [
                    {
                        "Key": {
                            "Name": "ReasonForLocking",
                            "Uri": 5
                        },
                        "Value": {
                            "Type": 6,
                            "Body": 5
                        }
                    }
                ]
            },
            {
                "Name": "Name",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "06D2B035-E5B2-585D-2CE2-2E3233831831",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388855620,
            "MinorVersion": 388853860
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 1,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Equipment.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Tools",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=44"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "CBACCF7F-6D0F-5DA8-4514-F11F9C795705",
                "Properties": []
            },
            {
                "Name": "NodeVersion",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "060B3DB1-EB89-7DB1-FD5F-75D7E25E7547",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388853500,
            "MinorVersion": 388853310
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=MachineTool

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 1,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=MachineTool",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=MachineTool",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=26"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "15A8D595-A92E-C051-1321-D22DD7FD4F44",
                "Properties": []
            },
            {
                "Name": "OperationMode",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 26,
                "DataType": {
                    "Id": 65,
                    "Namespace": 5
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "9CA023F6-BB01-0252-3DA3-3AE329C2BCBB",
                "Properties": []
            },
            {
                "Name": "PowerOnDuration",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 6,
                "DataType": {
                    "Id": 7
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "82649134-46F7-ED64-6CF6-BF3B20527597",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388858450,
            "MinorVersion": 388857720
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Channel 1

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 2,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Channel 1",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Channel 1",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=16"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "24D157AB-5927-95D8-CFAC-EA4E1E519519",
                "Properties": []
            },
            {
                "Name": "ChannelState",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 26,
                "DataType": {
                    "Id": 64,
                    "Namespace": 5
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "4A417944-340F-0103-ECAE-1A91D9FDAFBA",
                "Properties": []
            },
            {
                "Name": "FeedOverride",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 10,
                "DataType": {
                    "Id": 11
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "2B71750D-BAE9-6BAF-AB2A-E26E6ED64DD4",
                "Properties": [
                    {
                        "Key": {
                            "Name": "EURange"
                        },
                        "Value": {
                            "Type": 22,
                            "Body": {
                                "TypeId": {
                                    "Id": 884
                                },
                                "Body": {
                                    "Low": 0,
                                    "High": 110
                                }
                            }
                        }
                    },
                    {
                        "Key": {
                            "Name": "EngineeringUnits"
                        },
                        "Value": {
                            "Type": 22,
                            "Body": {
                                "TypeId": {
                                    "Id": 887
                                },
                                "Body": {
                                    "NamespaceUri": "",
                                    "UnitId": 0,
                                    "DisplayName": {
                                        "Locale": "",
                                        "Text": "%"
                                    },
                                    "Description": {
                                        "Locale": "",
                                        "Text": ""
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            {
                "Name": "ChannelMode",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 26,
                "DataType": {
                    "Id": 67,
                    "Namespace": 5
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "7E4E1715-5B00-27E0-E7CE-4C543D43C47C",
                "Properties": []
            },
            {
                "Name": "Name",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "5210C40F-F262-00BE-2042-74D751F5EF0E",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388860440,
            "MinorVersion": 388859470
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Spindle

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 3,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Spindle",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Spindle",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=22"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "C566192A-A7DA-5B3D-5AA5-7AC7A69A0970",
                "Properties": []
            },
            {
                "Name": "IsRotating",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "0D93A83B-F2BB-EE62-2892-09307CD79D29",
                "Properties": []
            },
            {
                "Name": "IsUsedAsAxis",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "07666488-712F-35AD-8888-E84EAABA1BE1",
                "Properties": []
            },
            {
                "Name": "Override",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 10,
                "DataType": {
                    "Id": 11
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "CC1C6F8E-7608-5E3A-A7FA-0F4085283243",
                "Properties": [
                    {
                        "Key": {
                            "Name": "EngineeringUnits"
                        },
                        "Value": {
                            "Type": 22,
                            "Body": {
                                "TypeId": {
                                    "Id": 887
                                },
                                "Body": {
                                    "NamespaceUri": "",
                                    "UnitId": 0,
                                    "DisplayName": {
                                        "Locale": "",
                                        "Text": "%"
                                    },
                                    "Description": {
                                        "Locale": "",
                                        "Text": ""
                                    }
                                }
                            }
                        }
                    },
                    {
                        "Key": {
                            "Name": "EURange"
                        },
                        "Value": {
                            "Type": 22,
                            "Body": {
                                "TypeId": {
                                    "Id": 884
                                },
                                "Body": {
                                    "Low": 0,
                                    "High": 125
                                }
                            }
                        }
                    }
                ]
            },
            {
                "Name": "Name",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "2256326A-6CD2-3D12-76A7-AAEA0150D5CD",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388862930,
            "MinorVersion": 388862090
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 0

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 4,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 0",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 0",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/IA/;i=1006"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "FCA26FD1-3A03-DBCB-1041-D41D9119C15C",
                "Properties": []
            },
            {
                "Name": "SignalColor",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 5,
                "DataType": {
                    "Id": 3004,
                    "Namespace": 3
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "3AAC5F3A-682A-4199-DDBD-9B697C07F02F",
                "Properties": []
            },
            {
                "Name": "StacklightMode",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 5,
                "DataType": {
                    "Id": 3005,
                    "Namespace": 3
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "12A8ECB5-99EB-5A93-FBAF-4AD4C5CCFC3F",
                "Properties": []
            },
            {
                "Name": "IsPartOfBase",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "0CF608E2-D27C-1222-E72E-C22CD4FDFFEF",
                "Properties": []
            },
            {
                "Name": "SignalOn",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "79F78A65-FE88-3995-8218-2132B63BC31C",
                "Properties": []
            },
            {
                "Name": "NumberInList",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 4,
                "DataType": {
                    "Id": 28
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "2C40D65C-BFAF-DFBF-DC3D-D3DD58D5DD5D",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388867340,
            "MinorVersion": 388865450
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 1

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 5,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 1",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 1",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/IA/;i=1006"
        },
        "Fields": [
            {
                "Name": "SignalColor",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 5,
                "DataType": {
                    "Id": 3004,
                    "Namespace": 3
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "083082C1-8B51-0D98-DB4D-04B0D3AD6A36",
                "Properties": []
            },
            {
                "Name": "StacklightMode",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 5,
                "DataType": {
                    "Id": 3005,
                    "Namespace": 3
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "3C181295-208C-15FA-3323-0260BA0B5025",
                "Properties": []
            },
            {
                "Name": "IsPartOfBase",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "254E866C-176F-9C5D-6516-A19A96E93ED3",
                "Properties": []
            },
            {
                "Name": "SignalOn",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "D5A7F6B0-3967-2C77-DF5D-45C435835865",
                "Properties": []
            },
            {
                "Name": "NumberInList",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 4,
                "DataType": {
                    "Id": 28
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "6DAF9166-08F9-C7E5-6F76-C71CA84A8418",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388870180,
            "MinorVersion": 388868310
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 2
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 6,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 2",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight.nsu=http:_2F_2Fexample.com_2FShowcaseMachineTool_2F;name=Light 2",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/IA/;i=1006"
        },
        "Fields": [
            {
                "Name": "SignalColor",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 5,
                "DataType": {
                    "Id": 3004,
                    "Namespace": 3
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "D96807B3-696E-0ADC-9DF9-5FD509302342",
                "Properties": []
            },
            {
                "Name": "StacklightMode",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 5,
                "DataType": {
                    "Id": 3005,
                    "Namespace": 3
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "6F0DC22C-E189-2B00-5115-814894298298",
                "Properties": []
            },
            {
                "Name": "IsPartOfBase",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "8F534544-0814-DCB9-7E17-D13D254284C8",
                "Properties": []
            },
            {
                "Name": "SignalOn",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 0,
                "DataType": {
                    "Id": 1
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "993736B0-3C5D-EBD8-F16F-36D3D5DD6DA6",
                "Properties": []
            },
            {
                "Name": "NumberInList",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 4,
                "DataType": {
                    "Id": 28
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "2EB65D4E-6650-CC72-CF2C-32134FE43E63",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388872940,
            "MinorVersion": 388871100
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 7,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Monitoring.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Stacklight",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/IA/;i=1002"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "8A1E01F7-3227-285C-7317-81C808808828",
                "Properties": []
            },
            {
                "Name": "StacklightMode",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 5,
                "DataType": {
                    "Id": 3002,
                    "Namespace": 3
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "D71B4BCC-5209-8419-5E05-9039AC4A54E5",
                "Properties": []
            },
            {
                "Name": "NodeVersion",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "12F17944-7FE8-BDE2-6036-C39C2FF28F08",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388865050,
            "MinorVersion": 388864420
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=State

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 8,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=State",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=State",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=24"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "992AA8A9-D8BF-51DF-A83A-63269EB94B04",
                "Properties": []
            },
            {
                "Name": "CurrentState",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 20,
                "DataType": {
                    "Id": 21
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "E7103213-4822-6BD3-F22F-12711A518598",
                "Properties": [
                    {
                        "Key": {
                            "Name": "Number"
                        },
                        "Value": {
                            "Type": 7,
                            "Body": 1
                        }
                    },
                    {
                        "Key": {
                            "Name": "Id"
                        },
                        "Value": {
                            "Type": 17,
                            "Body": {
                                "Id": 138,
                                "Namespace": 5
                            }
                        }
                    }
                ]
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388876230,
            "MinorVersion": 388876050
        }
    }
}

isw/json/metadata/prefix=isw;nsu=de.uni-stuttgart.isw.sampleserver;i=1234/_WriterGroup/.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram

{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "ShowcaseMachineTool",
    "DataSetWriterId": 9,
    "DataSetWriterName": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram",
    "MetaData": {
        "Namespaces": [
            "http://opcfoundation.org/UA/",
            "urn:open62541.server.application",
            "http://opcfoundation.org/UA/DI/",
            "http://opcfoundation.org/UA/IA/",
            "http://opcfoundation.org/UA/Machinery/",
            "http://opcfoundation.org/UA/MachineTool/",
            "http://opcfoundation.org/UA/Woodworking/",
            "http://example.com/ShowcaseMachineTool/"
        ],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=Production.nsu=http:_2F_2Fopcfoundation.org_2FUA_2FMachineTool_2F;name=ActiveProgram",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=32"
        },
        "Fields": [
            {
                "Name": "TypeDefinition",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 16,
                "DataType": {
                    "Id": 17
                },
                "ValueRank": -1,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "80E504D3-BE2A-B42D-6CE6-EEEEB4DB3DE3",
                "Properties": []
            },
            {
                "Name": "Name",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 11,
                "DataType": {
                    "Id": 12
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "1A68444B-E28C-CA20-9B99-E99E4C84C87C",
                "Properties": []
            },
            {
                "Name": "NumberInList",
                "Description": {
                    "Locale": "",
                    "Text": ""
                },
                "FieldFlags": 0,
                "BuiltInType": 4,
                "DataType": {
                    "Id": 5
                },
                "ValueRank": -2,
                "ArrayDimensions": [],
                "MaxStringLength": 0,
                "DataSetFieldId": "F43D67F4-5BF0-57FC-B44B-3443F97F47A4",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 388877790,
            "MinorVersion": 388875340
        }
    }
}
```
## Example Datasets

* MachineTool Examples:
  * [ShowcaseMachineTool Data](PubSub/ShowcaseMachineTool-data.json)
  * [ShowcaseMachineTool MetaData](PubSub/ShowcaseMachineTool-metadata.json)
  * [MRMachineTool Data](PubSub/MRMachineTool-data.json)
  * [MRMachineTool MetaData](PubSub/MRMachineTool-metadata.json)
* Woodworking Examples:
  * [FullWoodworking Data](PubSub/FullWoodworking-data.json)
  * [FullWoodworking MetaData](PubSub/FullWoodworking-metadata.json)
