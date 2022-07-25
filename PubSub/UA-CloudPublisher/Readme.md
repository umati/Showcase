# UA-CloudPublisher

The usage of the UA-Cloudpublisher is described [here](https://github.com/umati/UA-CloudPublisher).

For demonstration purpose we provide a sample [publishednodes.json](publishednodes.json) to show how to configure a machine tool instance.

## publishednodes.json configuration example

``` json
[
  {
    "EndpointUrl": "opc.tcp://opcua.umati.app:4843/UA", // replace according your endpoint
    "OpcNodes": [
      {
        "Id": "nsu=http://example.com/ShowcaseMachineTool/;i=55245", // replace with your concrete ExpandedNodeId
        "OpcSamplingInterval": 500,
        "OpcPublishingInterval": 1000,
        "HeartbeatInterval": 0,
        "SkipFirst": false
      },
      ...

          ],
    "OpcEvents": [],
    "OpcAuthenticationMode": "Anonymous" // configuration see UA-CloudPublisher
  }
]
```

## Data Example

``` json
{
    "MessageId": "32050",
    "MessageType": "ua-data",
    "PublisherId": "UACloudPublisher",
    "Messages": [
        {
            "DataSetWriterId": 45938,
            "Timestamp": "2022-07-11T13:03:42.977107Z",
            "Payload": {
                "FeedOverride": {
                    "Type": 11,
                    "Body": 120
                }
            }
        }
    ]
}
```

## Metadata Example

``` json
{
  "MessageId": "32986",
  "MessageType": "ua-metadata",
  "PublisherId": "UACloudPublisher",
  "DataSetWriterId": 45938,
  "MetaData": {
    "Name": "urn:SampleServer;nsu=http://example.com/ShowcaseMachineTool/;i=55229",
    "Fields": [
      {
        "Name": "FeedOverride",
        "FieldFlags": 0,
        "BuiltInType": 11,
        "DataType": {
          "Id": 24
        },
        "ValueRank": -1,
        "MaxStringLength": 0,
        "DataSetFieldId": "5486271c-89f0-4607-aceb-e4c7741ea605"
      }
    ],
    "ConfigurationVersion": {
      "MajorVersion": 1,
      "MinorVersion": 1
    }
  }
}
```
