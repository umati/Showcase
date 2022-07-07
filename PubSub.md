# PublishSubcribe (MQTT Transport and UA JSON encoding)

This page describe how to connect to the umati.app Dashboard by using PubSub instead of the server/client connection described in other parts of the Specification.

> PubSub allows the distribution of data and events from an OPC UA information source to interested observers inside a device network as well as in IT and analytics cloud systems.

* Detailed Specification of PubSub can be found at: [OPC 10000-14](https://reference.opcfoundation.org/Core/docs/Part14/) Part 14: PubSub
* The JSON mapping is describe in [Part14/7.2.3](https://reference.opcfoundation.org/Core/docs/Part14/7.2.3/)

## Setup

The publisher could be implemented together with the OPC UA Server application on the same instance.
Additionally Gateways such as UA-Publisher or Azure OPC Publisher can be used to subscribe to the OPC UA Server and publish the information.

OPC UA Server/Publisher -- MQTT/JSON --> MQTT Broker

OPC UA Server --TCO binary --> Gateway -- MQTT/JSON --> MQTT Broker

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

* `<machine_id>` url encoding of e.g.: `prefix=<prefix>;nsu=<ns_uri of machine node>;<index of machine node>`, e.g. `prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002`

The topics follow the browse paths.

### Data-Topic

```html
<prefix>/json/data/<machine_id>/_WriterGroup
```

### Metadata-Topics (Examples)

```html
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Identification_Writer

<prefix>/json/metadata/<machine_id>/_WriterGroup/.Equipment.Tools.Tool1_Writer
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Equipment.Tools_Writer

<prefix>/json/metadata/<machine_id>/_WriterGroup/.Monitoring.MachineTool_Writer
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Monitoring.Channel 1_Writer
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Monitoring.Spindle_Writer
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Monitoring.Stacklight_Writer
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Monitoring.Stacklight.Light 0_Writer
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Monitoring.Stacklight.Light 1_Writer
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Monitoring.Stacklight.Light 2_Writer

<prefix>/json/metadata/<machine_id>/_WriterGroup/.Production.ActiveProgram_Writer
<prefix>/json/metadata/<machine_id>/_WriterGroup/.Production.ActiveProgram.State_Writer
```

## Examples

### Data Topic

Topic: `isw/json/data/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-data",
    "Messages": [
        {
            "DataSetWriterId": 53,
            "DataSetWriterName": ".Production.ActiveProgram_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920589240,
                "MinorVersion": 3920587330
            },
            "Timestamp": "2022-07-07T16:10:29.805737Z",
            "Payload": {
                "Name": {
                    "Type": 12,
                    "Body": "Basic Program"
                },
                "NumberInList": {
                    "Type": 5,
                    "Body": 0
                }
            }
        },
        {
            "DataSetWriterId": 52,
            "DataSetWriterName": ".Production.ActiveProgram.State_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920588010,
                "MinorVersion": 3920587890
            },
            "Timestamp": "2022-07-07T16:10:29.805765Z",
            "Payload": {
                "CurrentState": {
                    "Type": 21,
                    "Body": {
                        "Locale": "en",
                        "Text": "Running"
                    }
                }
            }
        },
        {
            "DataSetWriterId": 51,
            "DataSetWriterName": ".Monitoring.Stacklight_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920577050,
                "MinorVersion": 3920576210
            },
            "Timestamp": "2022-07-07T16:10:29.805787Z",
            "Payload": {
                "StacklightMode": {
                    "Type": 6,
                    "Body": 0
                },
                "NodeVersion": {
                    "Type": 12,
                    "Body": ""
                }
            }
        },
        {
            "DataSetWriterId": 50,
            "DataSetWriterName": ".Monitoring.Stacklight.Light 2_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920585300,
                "MinorVersion": 3920583640
            },
            "Timestamp": "2022-07-07T16:10:29.805821Z",
            "Payload": {
                "SignalColor": {
                    "Type": 6,
                    "Body": 2
                },
                "StacklightMode": {
                    "Type": 6,
                    "Body": 0
                },
                "IsPartOfBase": {
                    "Type": 1,
                    "Body": false
                },
                "SignalOn": {
                    "Type": 1,
                    "Body": true
                },
                "NumberInList": {
                    "Type": 5,
                    "Body": 2
                }
            }
        },
        {
            "DataSetWriterId": 49,
            "DataSetWriterName": ".Monitoring.Stacklight.Light 1_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920582860,
                "MinorVersion": 3920580630
            },
            "Timestamp": "2022-07-07T16:10:29.805888Z",
            "Payload": {
                "SignalColor": {
                    "Type": 6,
                    "Body": 4
                },
                "StacklightMode": {
                    "Type": 6,
                    "Body": 0
                },
                "IsPartOfBase": {
                    "Type": 1,
                    "Body": false
                },
                "SignalOn": {
                    "Type": 1,
                    "Body": false
                },
                "NumberInList": {
                    "Type": 5,
                    "Body": 1
                }
            }
        },
        {
            "DataSetWriterId": 48,
            "DataSetWriterName": ".Monitoring.Stacklight.Light 0_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920579490,
                "MinorVersion": 3920577350
            },
            "Timestamp": "2022-07-07T16:10:29.805949Z",
            "Payload": {
                "SignalColor": {
                    "Type": 6,
                    "Body": 1
                },
                "StacklightMode": {
                    "Type": 6,
                    "Body": 0
                },
                "IsPartOfBase": {
                    "Type": 1,
                    "Body": false
                },
                "SignalOn": {
                    "Type": 1,
                    "Body": true
                },
                "NumberInList": {
                    "Type": 5,
                    "Body": 0
                }
            }
        },
        {
            "DataSetWriterId": 47,
            "DataSetWriterName": ".Monitoring.Spindle_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920574090,
                "MinorVersion": 3920573210
            },
            "Timestamp": "2022-07-07T16:10:29.80601Z",
            "Payload": {
                "IsRotating": {
                    "Type": 1,
                    "Body": true
                },
                "IsUsedAsAxis": {
                    "Type": 1,
                    "Body": false
                },
                "Override": {
                    "Type": 11,
                    "Body": 103
                },
                "Name": {
                    "Type": 12,
                    "Body": "Spindle"
                }
            }
        },
        {
            "DataSetWriterId": 46,
            "DataSetWriterName": ".Monitoring.Channel 1_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920571210,
                "MinorVersion": 3920570240
            },
            "Timestamp": "2022-07-07T16:10:29.806042Z",
            "Payload": {
                "ChannelState": {
                    "Type": 6,
                    "Body": 1
                },
                "FeedOverride": {
                    "Type": 11,
                    "Body": 16.35999999940395355224609375
                },
                "ChannelMode": {
                    "Type": 6,
                    "Body": 0
                },
                "Name": {
                    "Type": 12,
                    "Body": "Channel 1"
                }
            }
        },
        {
            "DataSetWriterId": 45,
            "DataSetWriterName": ".Monitoring.MachineTool_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920569310,
                "MinorVersion": 3920568700
            },
            "Timestamp": "2022-07-07T16:10:29.806094Z",
            "Payload": {
                "OperationMode": {
                    "Type": 6,
                    "Body": 1
                },
                "PowerOnDuration": {
                    "Type": 7,
                    "Body": 0
                }
            }
        },
        {
            "DataSetWriterId": 23,
            "DataSetWriterName": ".Equipment.Tools_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920565170,
                "MinorVersion": 3920565000
            },
            "Timestamp": "2022-07-07T16:10:29.806124Z",
            "Payload": {
                "NodeVersion": {
                    "Type": 12,
                    "Body": null
                }
            }
        },
        {
            "DataSetWriterId": 22,
            "DataSetWriterName": ".Equipment.Tools.Tool1_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920566820,
                "MinorVersion": 3920565440
            },
            "Timestamp": "2022-07-07T16:10:29.806135Z",
            "Payload": {
                "ControlIdentifier1": {
                    "Type": 7,
                    "Body": 12
                },
                "ControlIdentifierInterpretation": {
                    "Type": 6,
                    "Body": 0
                },
                "Locked": {
                    "Type": 1,
                    "Body": false
                },
                "Name": {
                    "Type": 12,
                    "Body": "Tool1"
                }
            }
        },
        {
            "DataSetWriterId": 44,
            "DataSetWriterName": ".Identification_Writer",
            "SequenceNumber": 3,
            "MetaDataVersion": {
                "MajorVersion": 3920563480,
                "MinorVersion": 3920560150
            },
            "Timestamp": "2022-07-07T16:10:29.806175Z",
            "Payload": {
                "YearOfConstruction": {
                    "Type": 5,
                    "Body": 2021
                },
                "MonthOfConstruction": {
                    "Type": 3,
                    "Body": 11
                },
                "Manufacturer": {
                    "Type": 21,
                    "Body": {
                        "Locale": "",
                        "Text": "umati Showcase"
                    }
                },
                "ProductInstanceUri": {
                    "Type": 12,
                    "Body": "https://showcase.umati.org/Specs/Machinetools.html"
                },
                "SerialNumber": {
                    "Type": 12,
                    "Body": "2021-15360620311222485159"
                },
                "Model": {
                    "Type": 21,
                    "Body": {
                        "Locale": "",
                        "Text": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002"
                    }
                },
                "ProductCode": {
                    "Type": 12,
                    "Body": "2653837gg1548"
                },
                "SoftwareRevision": {
                    "Type": 12,
                    "Body": "v1.02.1"
                },
                "DeviceClass": {
                    "Type": 12,
                    "Body": "Machining centre (other)"
                },
                "Location": {
                    "Type": 12,
                    "Body": "CIMT E8 B014/VIRTUAL 0 0/N 49.871215 E 8.654204"
                },
                "ComponentName": {
                    "Type": 21,
                    "Body": {
                        "Locale": "",
                        "Text": "umati Showcase Component"
                    }
                }
            }
        }
    ]
}
```

### Metadata Topics

Topic: `isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Identification_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 44,
    "DataSetWriterName": ".Identification_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Identification",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=11"
        },
        "Fields": [
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
                "DataSetFieldId": "76E35778-47BC-098F-0DA0-4A147C279209",
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
                "DataSetFieldId": "4898AED0-D893-9809-4BC4-5CA5B15BB5CB",
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
                "DataSetFieldId": "22D78A78-07FC-CDE9-89B8-7B778E188148",
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
                "DataSetFieldId": "20E22A33-5AF0-8A44-5965-667614E1FE6F",
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
                "DataSetFieldId": "624FE9E4-4C1F-0A3A-3743-7407F68F7857",
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
                "DataSetFieldId": "87021A33-8413-F03F-AE6A-C6CC8E98D9AD",
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
                "DataSetFieldId": "20F4A41C-5FF7-7321-7FC7-1C01F3FFCF9C",
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
                "DataSetFieldId": "918C3834-0B1F-DD67-2622-A2EABBEB5E45",
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
                "DataSetFieldId": "11116866-0CCF-863A-9C69-6626AC3A8388",
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
                "DataSetFieldId": "7B86AA05-D66A-90CA-D06D-D67DB80B9089",
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
                "DataSetFieldId": "0FA09BFF-AA6E-345D-6C66-C61C4FC49C49",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920563480,
            "MinorVersion": 3920560150
        }
    }
}
```

### Topic

`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Equipment.Tools.Tool1_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 22,
    "DataSetWriterName": ".Equipment.Tools.Tool1_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Equipment.Tools.Tool1",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=50"
        },
        "Fields": [
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
                "DataSetFieldId": "8BF5D4F7-A852-8D50-D50D-6056788708E0",
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
                "DataSetFieldId": "A4F9AA8D-9C31-FE94-26A2-6A8615A17A77",
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
                "DataSetFieldId": "1C0DE6B1-F4AD-DCE4-9D69-5615C2AC5A05",
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
                "DataSetFieldId": "3583F550-2658-6708-6196-E93E1281A85A",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920566820,
            "MinorVersion": 3920565440
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Equipment.Tools_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 45,
    "DataSetWriterName": ".Monitoring.MachineTool_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Monitoring.MachineTool",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=26"
        },
        "Fields": [
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
                "DataSetFieldId": "1564B7F8-E549-0C5C-CBCC-ECAECC7CF79F",
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
                "DataSetFieldId": "061C1A48-34D1-786E-77D7-9D9970E75EB5",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920569310,
            "MinorVersion": 3920568700
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Monitoring.Channel 1_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 46,
    "DataSetWriterName": ".Monitoring.Channel 1_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Monitoring.Channel 1",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=16"
        },
        "Fields": [
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
                "DataSetFieldId": "534B0891-E249-25F1-51B5-8B680BD0CD8C",
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
                "DataSetFieldId": "4457A379-B2F3-2AFC-EFFE-8F98AC2A2262",
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
                                    "High": 100
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
                "DataSetFieldId": "AAC3BD75-1A70-567F-F8AF-EAFE7F4764E6",
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
                "DataSetFieldId": "1D7A9D9C-DE72-8ECF-E00E-609639C3DC7D",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920571210,
            "MinorVersion": 3920570240
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Monitoring.Spindle_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 47,
    "DataSetWriterName": ".Monitoring.Spindle_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Monitoring.Spindle",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=22"
        },
        "Fields": [
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
                "DataSetFieldId": "2C7A784A-1A3B-D5FC-8B48-344385589599",
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
                "DataSetFieldId": "BE09124E-6C85-4D5F-ABEA-5EE5B7BBAB0A",
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
                "DataSetFieldId": "821867B2-DD61-C0AF-7457-C5FCB3DB3D33",
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
                "DataSetFieldId": "ABF9F23D-6E76-ADF2-07F0-BF4B5BA51AB1",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920574090,
            "MinorVersion": 3920573210
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Monitoring.Stacklight.Light 0_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 48,
    "DataSetWriterName": ".Monitoring.Stacklight.Light 0_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Monitoring.Stacklight.Light 0",
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
                "DataSetFieldId": "5A2F1248-10E8-3318-5D95-6926C41CD18D",
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
                "DataSetFieldId": "2A2CB495-0EF8-5B98-ABBA-6B06E83E5345",
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
                "DataSetFieldId": "ADC52DDC-7D47-3376-B44B-949950556596",
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
                "DataSetFieldId": "175ABD9B-4CD5-7BAD-2BF2-7F77E56E86C8",
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
                "DataSetFieldId": "09E07496-BFB0-3FE4-7B47-A41AEB0E4014",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920579490,
            "MinorVersion": 3920577350
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Monitoring.Stacklight.Light 1_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 49,
    "DataSetWriterName": ".Monitoring.Stacklight.Light 1_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Monitoring.Stacklight.Light 1",
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
                "DataSetFieldId": "0C723215-7752-F231-6546-44E450E53E63",
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
                "DataSetFieldId": "22DF3E94-9166-02DF-E37E-F7CFE44EC4FC",
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
                "DataSetFieldId": "A4137327-B3F8-7D7A-7977-5725C43C33C3",
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
                "DataSetFieldId": "6BA74528-3C50-DFAF-FB0F-107166967987",
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
                "DataSetFieldId": "D5A11AAE-C94E-B4F9-B2CB-3CD3D41D51D5",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920582860,
            "MinorVersion": 3920580630
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Monitoring.Stacklight.Light 2_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 50,
    "DataSetWriterName": ".Monitoring.Stacklight.Light 2_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Monitoring.Stacklight.Light 2",
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
                "DataSetFieldId": "92A35434-F8DA-405C-0400-40548658A5DA",
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
                "DataSetFieldId": "590EC972-A5A6-5406-D50D-A0DA62064014",
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
                "DataSetFieldId": "812C0E2A-81A5-DCBB-8208-5055CD7C37E3",
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
                "DataSetFieldId": "C443E79E-0EF5-0FF7-9939-43C4F2AF5A65",
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
                "DataSetFieldId": "CFBB0365-51EE-7165-A08A-F83F0A005025",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920585300,
            "MinorVersion": 3920583640
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Monitoring.Stacklight_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 51,
    "DataSetWriterName": ".Monitoring.Stacklight_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Monitoring.Stacklight",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/IA/;i=1002"
        },
        "Fields": [
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
                "DataSetFieldId": "7807F6AA-CD82-1FF6-14E1-1E113A03F08F",
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
                "DataSetFieldId": "4FC81002-5D7A-058B-7707-B06B3763C63C",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920577050,
            "MinorVersion": 3920576210
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Production.ActiveProgram.State_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 52,
    "DataSetWriterName": ".Production.ActiveProgram.State_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Production.ActiveProgram.State",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=24"
        },
        "Fields": [
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
                "DataSetFieldId": "107A8B7F-2C61-3217-8EA8-8AE85A151171",
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
            "MajorVersion": 3920588010,
            "MinorVersion": 3920587890
        }
    }
}
```

Topic:
`isw/json/metadata/prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002/_WriterGroup/.Production.ActiveProgram_Writer`

Json:

```json
{
    "MessageId": null,
    "MessageType": "ua-metadata",
    "PublisherId": "prefix%3Disw%3Bnsu%3Dhttp%3A_2F_2Fisw.com_2Fiotconnect_2F%3Bi%3D5002",
    "DataSetWriterId": 53,
    "DataSetWriterName": ".Production.ActiveProgram_Writer",
    "MetaData": {
        "Namespaces": [],
        "StructureDataTypes": [],
        "EnumDataTypes": [],
        "SimpleDataTypes": [],
        "Name": ".Production.ActiveProgram",
        "Description": {
            "Locale": "en",
            "Text": "nsu=http://opcfoundation.org/UA/MachineTool/;i=32"
        },
        "Fields": [
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
                "DataSetFieldId": "4A28D008-4B67-8B97-47A4-EA9E2B5205E0",
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
                "DataSetFieldId": "FEAB0F10-64AC-F99D-5735-933989B86B56",
                "Properties": []
            }
        ],
        "DataSetClassId": "00000000-0000-0000-0000-000000000000",
        "ConfigurationVersion": {
            "MajorVersion": 3920589240,
            "MinorVersion": 3920587330
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
