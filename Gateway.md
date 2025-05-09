# Gateway

To connect your local OPC UA server to the umati.app the initiative provides a software gateway.
This gateway subscribes via OPC UA (Client/Server; TCP Binary) to your server and publishes the information to an MQTT broker.

~~This [gateway](https://github.com/umati/Dashboard-OPCUA-Client) is provided as an open source version based on [open62541](https://open62541.org) and currently uses a _custom_ JSON encoding for the payload. It is planned to migrate to OPC UA part 14 JSON encoding and defined topic tree, as soon as v1.05.03 is published.~~

A new version of the [gateway](https://github.com/umati/umatiGateway) is provided as an open source version based on [OPC UA .NET Standard Stack](https://github.com/OPCFoundation/UA-.NETStandard) and currently uses a _custom_ JSON encoding for the payload. The umati core team currently migrate the encoding to OPC UA part 14 UA JSON encoding and a defined topic tree.

## Architecture

### High level

OPC UA server --- Gateway --- MQTT Broker --- umati.app

### With protocols

- OPC UA server --- OPC UA TCP binary ---> Gateway
- Gateway --- MQTT over Websockets ---> MQTT Broker
- MQTT broker --- MQTT over Websockets ---> device viewing umati.app

## Configuration and connection

The detailed configuration of the client and how to deploy and run it is described in the [source repository](https://github.com/umati/umatiGateway/blob/develop/docs/user/usage.md).

### The gateway is provided as

- Standalone binary x86 (32bit) Linux/Windows
- Standalone binary x86_64 (64bit) Linux/Windows
- Standalone binary x86 (32bit) Linux .deb package for ubuntu 22.04 and 24.04
- Standalone binary x86_64 (64bit) Linux .deb package for ubuntu 22.04 and 24.04
- container image x86_64/arm64

The binaries can be downloaded [here](https://github.com/umati/umatiGateway/releases)

To obtain credentials to connect to the umati.app MQTT broker please follow [Server documentation](Server.md#connecting-an-opc-ua-server-to-umatiapp).
