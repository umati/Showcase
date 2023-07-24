# Gateway

To connect your local OPC UA server to the umati.app the initiative provides a software gateway.
This gateway subscribes via OPC UA (Client/Server; TCP Binary) to your server and publishes the information to and MQTT broker.

This [gateway](https://github.com/umati/Dashboard-OPCUA-Client) is provided as an open source version based on [open62541](https://open62541.org) and currently uses a _custom_ JSON encoding for the payload. It is planned to migrate to OPC UA part 14 JSON encoding and defined topic tree, as soon as v1.05.03 is published.

## Architecture

### High level

OPC UA server --- Gateway --- MQTT Broker --- umati.app

### With protocols

- OPC UA server --- OPC UA TCP binary ---> Gateway

- Gateway --- MQTT over Websockets ---> MQTT Broker
- MQTT broker --- MQTT over Websockets ---> device viewing umati.app

## Configuration and connection

The detailed configuration of the client and how to deploy and run it is described in the [source repository](https://github.com/umati/Dashboard-OPCUA-Client/blob/development/doc/usage_for_dashboard.md).

### The gateway is provided as

- Standalone binary x86 (32bit) Linux/Windows
- Standalone binary x86_64 (64bit) Linux/Windows
- Standalone binary x86 (32bit) Linux .deb package for ubuntu 20.04 and 22.04
- Standalone binary x86_64 (64bit) Linux .deb package for ubuntu 20.04 and 22.04
- container image x86_64

The binaries can be downloaded [here](https://github.com/umati/Dashboard-OPCUA-Client/releases)

A configuration file example as well as documentation is available [here](https://github.com/umati/Dashboard-OPCUA-Client/blob/development/doc/Configuration.md).

To obtain credentials to connect to the umati.app MQTT broker please follow [Server documentation](Server.md#connecting-an-opc-ua-server-to-umatiapp).
