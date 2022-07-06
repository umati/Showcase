# Full Exemplary PubSub Dataset

This folder contains a full PubSub dataset including topics and messages for data and metadata messages for the [ShowcaseMachineTool of the umati SampleServer](https://github.com/umati/Sample-Server/blob/develop/MachineTools/ShowcaseMachineTool.cpp).

The data topic structure is mapped to files as follows
`opcua/umati/v3/json/data/verbose/server-cpp-dev/ShowcaseMachineTool/Identification` &rarr; `data_opcua_umati_v3_json_data_verbose_server-cpp-dev_ShowcaseMachineTool_Identification`.

The metadata topic structure is mapped to files as follows
`opcua/umati/v3/json/metadata/verbose/server-cpp-dev/ShowcaseMachineTool/Identification` &rarr; `metadata_opcua_umati_v3_json_metadata_verbose_server-cpp-dev_ShowcaseMachineTool_Identification.json`.

In this case we had the OPCUA-MQTT-Gateway [umatiGateway](https://github.com/umati/umatiGateway) configured with:
- clientId=verbose/server-cpp-dev in the `umatiGatewayConfig.xml`, which means
- COMPANY_ID=verbose
- PUBLISHER_ID=server-cpp-dev


Each file contains a `json` structured as follows:
```jsonc
{   
    // The topic, under which the message in "payload" is published
    "topic": "opcua/umati/v3/json/data/verbose/server-cpp-dev/ShowcaseMachineTool/Identification",
    // The message published under the topic
    "payload": { /* ... */ }
```

If one wanted to reproduce the message/topic tree, he simply would load all jsons `metadata_*` and `data_*`, iterate through them and send out messages containing the message in `payload` over the topic `topic` over mqtt. The filename itself does not need to be parsed in this case.
