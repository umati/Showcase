# Python Publisher

The usage of the Python Publisher is described in the [UA-for-MachineTools Python publisher documentation](https://github.com/umati/UA-for-MachineTools/tree/main/samples/python-publisher).

For demonstration purposes, we provide the samples below to show what a complete message published by the simulator looks like.

## Data Example
Topic:
```text
opcua/umati/v3/json/data/verbose/server-cpp-dev/ShowcaseMachineTool/Monitoring/Spindle
```
Message:
```json
{
  "MessageId": "89a98bf4-95be-4cb1-9bb7-1ebb578f792d",
  "MessageType": "ua-data",
  "PublisherId": "1",
  "Messages": [
      {
          "Payload": {
              "IsRotating": {
                  "UaType": 1,
                  "Value": true
              },
              "Override": {
                  "UaType": 11,
                  "Value": 103
              },
              "IsUsedAsAxis": {
                  "UaType": 1,
                  "Value": false
              },
              "Name": {
                  "UaType": 12,
                  "Value": "Spindle"
              },
              "virtualId": {
                  "UaType": 12,
                  "Value": "17:ShowcaseMachineTool.5:Monitoring.17:Spindle"
              }
          }
      }
  ]
}
```

## Metadata Example

Topic:
```text
opcua/umati/v3/json/metadata/verbose/server-cpp-dev/ShowcaseMachineTool/Monitoring/Spindle`
```
Message:
```json
{
  "MessageId": "c17fbfb5-f1cb-448a-8d58-148b16c904d5",
  "MessageType": "ua-metadata",
  "PublisherId": "1",
  "DataSetWriterId": 15,
  "MetaData": {
      "Namespaces": [
          "http://opcfoundation.org/UA/",
          "urn:UmatiSampleServer",
          "http://opcfoundation.org/UA/DI/",
          "http://opcfoundation.org/UA/Machinery/",
          "http://opcfoundation.org/UA/IA/",
          "http://opcfoundation.org/UA/MachineTool/",
          "http://opcfoundation.org/UA/Woodworking/",
          "http://opcfoundation.org/UA/Machinery/Result/",
          "http://opcfoundation.org/UA/GMS/",
          "http://opcfoundation.org/UA/Dictionary/IRDI",
          "http://opcfoundation.org/UA/PADIM/",
          "http://opcfoundation.org/UA/Machinery/ProcessValues/",
          "http://opcfoundation.org/UA/AdditiveManufacturing/NodeSet2/",
          "http://example.com/FullMachineTool/",
          "http://example.com/FullMachineToolDynamic/",
          "http://example.com/BasicMachineTool/",
          "http://example.com/MRMachineTool/",
          "http://example.com/ShowcaseMachineTool/",
          "http://example.com/CNShowcaseMachineTool/",
          "http://example.com/BasicWoodworking/",
          "http://example.com/FullWoodworking/",
          "http://www.isw.uni-stuttgart.de/BasicGMS/",
          "https://www.hexagonmi.com/Hexagon PMM Gold/",
          "https://www.hexagonmi.com/Hexagon GLOBAL S/",
          "http://www.ogpgmbh.de/SmartScope CNC 500/",
          "http://www.wenzel-group.com/Wenzel LH 87/",
          "http://www.3yourmind.com/BasicAMMachine/",
          "http://www.3yourmind.com/ShowcaseAMMachine/"
      ],
      "Name": "ns=17;i=59047",
      "Fields": [
          {
              "Name": "IsRotating",
              "FieldFlags": 0,
              "BuiltInType": 1,
              "DataType": {
                  "Id": 1
              },
              "ValueRank": -2,
              "MaxStringLength": 0,
              "DataSetFieldId": "d9dccc6a-a291-479e-aaec-f5be7cd71e81"
          },
          {
              "Name": "Override",
              "FieldFlags": 0,
              "BuiltInType": 11,
              "DataType": {
                  "Id": 11
              },
              "ValueRank": -2,
              "MaxStringLength": 0,
              "DataSetFieldId": "71b3e07a-dbc7-4ddb-ab9d-c77e1ac6bf19"
          },
          {
              "Name": "IsUsedAsAxis",
              "FieldFlags": 0,
              "BuiltInType": 1,
              "DataType": {
                  "Id": 1
              },
              "ValueRank": -2,
              "MaxStringLength": 0,
              "DataSetFieldId": "aaa0a86c-e4cc-4d9e-b372-0f7f4e5a281a"
          },
          {
              "Name": "Name",
              "FieldFlags": 0,
              "BuiltInType": 12,
              "DataType": {
                  "Id": 12
              },
              "ValueRank": -2,
              "MaxStringLength": 0,
              "DataSetFieldId": "bdd16ab5-e37e-4042-a6d1-2c60fb1adf1c"
          },
          {
              "Name": "virtualId",
              "Description": {
                  "Text": "VirtualId used by the Gateway"
              },
              "FieldFlags": 0,
              "BuiltInType": 12,
              "DataType": {
                  "Id": 12
              },
              "ValueRank": -1,
              "MaxStringLength": 0,
              "DataSetFieldId": "382be11a-755a-4386-b946-0f2b4328d67e",
              "Properties": [
                  {
                      "Key": {
                          "Name": "relations"
                      },
                      "Value": {
                          "Type": 24,
                          "Body": [
                              {
                                  "Type": 22,
                                  "Body": {
                                      "TypeId": {
                                          "Id": 518
                                      },
                                      "Body": {
                                          "ReferenceTypeId": {
                                              "Id": 46
                                          },
                                          "IsForward": true,
                                          "NodeId": {
                                              "Id": 59049,
                                              "Namespace": 17
                                          },
                                          "BrowseName": {
                                              "Name": "Name",
                                              "Uri": 5
                                          },
                                          "DisplayName": {
                                              "Text": "Name"
                                          },
                                          "NodeClass": 2,
                                          "TypeDefinition": {
                                              "Id": 68
                                          }
                                      }
                                  }
                              },
                              {
                                  "Type": 22,
                                  "Body": {
                                      "TypeId": {
                                          "Id": 518
                                      },
                                      "Body": {
                                          "ReferenceTypeId": {
                                              "Id": 47
                                          },
                                          "IsForward": true,
                                          "NodeId": {
                                              "Id": 59048,
                                              "Namespace": 17
                                          },
                                          "BrowseName": {
                                              "Name": "IsRotating",
                                              "Uri": 5
                                          },
                                          "DisplayName": {
                                              "Text": "IsRotating"
                                          },
                                          "NodeClass": 2,
                                          "TypeDefinition": {
                                              "Id": 63
                                          }
                                      }
                                  }
                              },
                              {
                                  "Type": 22,
                                  "Body": {
                                      "TypeId": {
                                          "Id": 518
                                      },
                                      "Body": {
                                          "ReferenceTypeId": {
                                              "Id": 47
                                          },
                                          "IsForward": true,
                                          "NodeId": {
                                              "Id": 59050,
                                              "Namespace": 17
                                          },
                                          "BrowseName": {
                                              "Name": "Override",
                                              "Uri": 5
                                          },
                                          "DisplayName": {
                                              "Text": "Override"
                                          },
                                          "NodeClass": 2,
                                          "TypeDefinition": {
                                              "Id": 17570
                                          }
                                      }
                                  }
                              },
                              {
                                  "Type": 22,
                                  "Body": {
                                      "TypeId": {
                                          "Id": 518
                                      },
                                      "Body": {
                                          "ReferenceTypeId": {
                                              "Id": 47
                                          },
                                          "IsForward": true,
                                          "NodeId": {
                                              "Id": 59053,
                                              "Namespace": 17
                                          },
                                          "BrowseName": {
                                              "Name": "IsUsedAsAxis",
                                              "Uri": 5
                                          },
                                          "DisplayName": {
                                              "Text": "IsUsedAsAxis"
                                          },
                                          "NodeClass": 2,
                                          "TypeDefinition": {
                                              "Id": 63
                                          }
                                      }
                                  }
                              },
                              {
                                  "Type": 22,
                                  "Body": {
                                      "TypeId": {
                                          "Id": 518
                                      },
                                      "Body": {
                                          "ReferenceTypeId": {
                                              "Id": 47
                                          },
                                          "IsForward": false,
                                          "NodeId": {
                                              "Id": 59004,
                                              "Namespace": 17
                                          },
                                          "BrowseName": {
                                              "Name": "Monitoring",
                                              "Uri": 5
                                          },
                                          "DisplayName": {
                                              "Text": "Monitoring"
                                          },
                                          "NodeClass": 1,
                                          "TypeDefinition": {
                                              "Id": 14,
                                              "Namespace": 5
                                          }
                                      }
                                  }
                              },
                              {
                                  "Type": 22,
                                  "Body": {
                                      "TypeId": {
                                          "Id": 518
                                      },
                                      "Body": {
                                          "ReferenceTypeId": {
                                              "Id": 40
                                          },
                                          "IsForward": true,
                                          "NodeId": {
                                              "Id": 22,
                                              "Namespace": 5
                                          },
                                          "BrowseName": {
                                              "Name": "SpindleMonitoringType",
                                              "Uri": 5
                                          },
                                          "DisplayName": {
                                              "Text": "SpindleMonitoringType"
                                          },
                                          "NodeClass": 8
                                      }
                                  }
                              }
                          ]
                      }
                  }
              ]
          }
      ],
      "ConfigurationVersion": {
          "MajorVersion": 1,
          "MinorVersion": 0
      }
  }
}
```
