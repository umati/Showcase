# UA-CloudPublisher

The usage of the UA-Cloudpublisher is described [here](https://github.com/umati/UA-CloudPublisher).

For demonstration purpose we provide a sample [publishednodes.json](publishednodes.json) to show how to confiure for machine tool instance.

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
    "MessageId": "914",
    "MessageType": "ua-data",
    "PublisherId": "UACloudPublisher",
    "Messages": [
        {
            "DataSetWriterId": 3383,
            "Timestamp": "2022-07-11T10:48:02.9933409Z",
            "Payload": {
                "FeedOverride": {
                    "Type": 11,
                    "Body": 90
                }
            }
        }
    ]
}
```

## Metadata Example

``` json
{
    "MessageId": "782",
    "MessageType": "ua-metadata",
    "PublisherId": "UACloudPublisher",
    "DataSetWriterId": 23389,
    "MetaData": {
        "Name": "urn:SampleServer;nsu=http://example.com/ShowcaseMachineTool/;i=55188",
        "Fields": [
            {
                "Name": "CurrentState",
                "FieldFlags": 0,
                "BuiltInType": 21,
                "DataType": {
                    "Id": 24
                },
                "ValueRank": -1,
                "MaxStringLength": 0,
                "DataSetFieldId": "f282a68f-7815-47f4-8f39-96ce3ea0d658"
            }
        ],
        "ConfigurationVersion": {
            "MajorVersion": 1,
            "MinorVersion": 1
        }
    }
}

```
