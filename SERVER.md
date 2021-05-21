# OPC UA Server Requirements

## Connecting an OPC UA server to the data hub via VPN

### Datahub and the fairconnect-configuration

For this showcase we have a datahub provided off premise. This acts as an OPC UA aggregation server. The OPC UA servers (M) will connect via an OpenVPN tunnel to an VPN endpoint (one per participant; multiple are possible in case of multiple machines But preaggregation of machines to a single OPC UA Server at the participant is also possible, [see below for details](SERVER.md#openvpn-configuration).). An OPC UA client will connect to the OPC UA server(s) of that participant through the VPN tunnel. The application providers (A) will connect to the datahub OPC UA server endpoint, as an [OPC UA Client](CLIENT.md).
To connect to this datahub (M) need an OPC UA server and OpenVPN client to access one dedicated endpoint per partner.
In order to ease the onboarding process onto the datahub, we provide the [fairconnect application](https://fairconnect.umati.app) and a specified process for connecting OPC UA servers to the showcase:

#### Process summary for connecting an OPC UA server to the data hub via VPN

1. Fill in and sign the MoU as participant and indicate which/how many machines or you want to connect.
2. Install the [OpenVPN client](https://openvpn.net/community-downloads/) 
3. Wait to receive an email with a link to register your machine on the datahub.
4. Click the link and set a password for the machine account
5. Login into [fairconnect](https://fairconnect.umati.app) with the set password from step 4.

![Fairconnect screen](img/Fairconnect.png "Fairconnect screen")

6. Download your individual OpenVPN client configuration
7. Import the provided configuration and start the VPN connection on the OpenVPN client.
8. Insert the TCP port of the OPC UA Server
9. Set the authentication method and credentials: [Anonymous](http://opcfoundation.org/UA-Profile/Security/UserToken/Anonymous), [User/Password](http://opcfoundation.org/UA-Profile/Security/UserToken/Server/UserNamePassword), [X509 client](http://opcfoundation.org/UA-Profile/Security/UserToken/Server/X509Certificate) are possible.
10. Check whether the connection has been set up correctly.
11. Select the NS(Namespace)-URIs of your instance to be imported (If you have an aggregating server with more than one machine, please select all relevant namespaces).
12. Start the integration and wait for it to complete. This will take a couple of minutes, if errors occur you will get an output. Please adjust your server/connectivity accordingly. When all checks are passed, the machine is added to the datahub.
13. Check if the machine appears in the datahub (meaning the OPC UA server that clients can connect to, please refer to the following chapter for connection details) and all values are correct.
14. There is a delay between adding machines to the datahub (the aggregated OPC UA server) until they are added to the dashboard (the browser-based umati.app) as this takes a couple of minutes to propagate to the system.
15. Send an email to [info@umati.org](mailto:info@umati.org) with an image of the machine (PNG / 1000x800 pixel or larger) and the Namespace URI of the machine in the datahub. This image will be used for the dashboard at [https://umati.app](https://umati.app/) . If you do not provide a picture, we will instead display a dummy machine icon.

### OpenVPN client

Each OPC UA server that should be connected to the datahub requires its own OpenVPN client (e.g. when there are two machine tools with an OPC UA server each, each one will require its own VPN client. When both OPC UA servers are aggregated to one OPC UA server, one VPN client for the aggregated server is sufficient, see following scenario graphs). The OpenVPN client can be downloaded here: [https://openvpn.net/community-downloads/](https://openvpn.net/community-downloads/). The OpenVPN client will make the computer accessible to the OPC UA client running on the data hub. Each participant will connect to their own VPN server endpoint.

![VPN schema](img/VPN.png "VPN schema")

#### OpenVPN configuration

Each participant will initially receive as many machine accounts (OpenVPN certs) as requested in the MoU. Each configuration can be used for one VPN client instance.
See the picture above for possible scenarios of multiple OPC UA servers/multiple machines of one participant.
These configurations can be downloaded per machine at <https://fairconnect.umati.app> by all registered participants (M) who have indicated to connect machines with an OPC UA server.

The VPN-connection requires an unrestricted outbound connection to **vpn.umati.app** using **TCP port 443**.

#### OPC UA server/client connection

The OPC UA client runs on the datahub and is connected to the systems that runs the OpenVPN client. The OPC UA client connects to a specified port on this computer to establish a connection to the OPC UA server. The default port is 4840. You can set this port on the [fairconnect configuration page (**8**)](https://fairconnect.umati.app).

The default OPC UA connection settings are (encryption is done by the VPN):

| Type | Setting |
| --- | :---: |
| Security Mode | None |
| Algorithm | None |
| User Authentication | Anonymous |

The client connection will be established to higher security profiles, if they are available in the server.
Futhermore as of now the authentication to a OPC UA server is also available using either
- [User/Password](http://opcfoundation.org/UA-Profile/Security/UserToken/Server/UserNamePassword) enter credentials at **(9)**. 
or
- [X509 client certificate](http://opcfoundation.org/UA-Profile/Security/UserToken/Server/X509Certificate) select check box and download/install X509 client cert at **(9a)**.


## OPC UA server functionalities

The functional requirements for the OPC UA server provided for the umati showcase demonstration are as follows.

Provide at least the OPC 40001-1 UA for Machinery namespance and a instance namespace of your machine.

The minimal required profiles according to the OPC UA Specification Part 7 are listed below:

- Micro Embedded Device 2017 Server Profile this includes:
  - 2 Sessions
  - Attribute Read
  - Ua Binary Encoding
  - Core 2017 Server Facet
    - Authentication by username and password
    - TCP Binary
- Enhanced DataChange Subscription 2017 Server Facet (500 Monitored Items) (Model might contain more than 100 nodes)
- Data Access Server Facet
  - With mandatory &quot;Data Access AnalogItems&quot; as OverrideItemType is a subtype of AnalogItemType

## Getting started: OPC UA server for umati showcase

This manual focuses on the special features that are relevant when creating an umati OPC UA server for this fair demonstration. The general points about the OPC UA servers are not discussed in detail, e.g. how the data is linked with the OPC UA address space.

In this chapter the necessary adaptations of the OPC UA information model, some important points about the running OPC UA server and the connection to the datahub will be described in short.

### OPC UA server

- Load at least the Machinery types (as defined by OPC 40001-1 UA for Machinery) and the adapted instances in two separate namespaces into the OPC UA server.
- Ensure that all variables have valid values, if a variable could not be provided by the machine tool, set a neutral value. (e.g. if no override is available, set the value to 1).

### OPC UA Server connecting to the datahub

1. Please ensure corresponding umati-relevant namespace is added to the server.

2. `Machines` folder have to point to base Machinery namespace, <http://opcfoundation.org/UA/Machinery/>
This is where the datahub OPC UA client looks for showcase-relevant instances.

3. Only the following namespaces are accepted as well as understood by the datahub.

   - <http://opcfoundation.org/UA/>
   - <http://opcfoundation.org/UA/DI/>
   - <http://opcfoundation.org/UA/IA/>
   - <http://opcfoundation.org/UA/Machinery/>
   - <http://opcfoundation.org/UA/MachineTool/>
   - `your custom namespace(s) for you instance(s)`

   Your custom instance namespace **must not** contain references to any other namespace (e.g. instantiation a different companion specification in this namespace is not allowed).

4. If the computer, where the OpenVPN Client runs is accessible, try connecting to your OPC UA Server via the Open VPN IP-address (begins with 10.80.0.). If no OPC UA Client is available on this computer, basic connection test can also be done by using telnet, by `telnet 10.80.0.XX 4840` .
5. When the OPC UA Server and the VPN-Connection is established, visit [https://fairconnect.umati.app](https://fairconnect.umati.app/) to check your connection and integrate the machine to the datahub.

## Aggregating multiple umati OPC UA servers

The aggregation should be equivalent to an aggregation that implement the [Device Information Model Specification](https://reference.opcfoundation.org/v104/DI/v102/docs/5.9/).

We define a well-known entry point (Machines, nsu=<http://opcfoundation.org/UA/Machinery>;i=1001), which contains all Machinery-Instances (normally one, but there might be several).

one machine tool:

![Address space](img/Addressspace_sample.png "Addressspace sample")

These two address spaces should be merged so that in the aggregated server there is only one Machinetools-Folder and each Machine is under this node with the same NodeId-Identifiers und NodeId-URI (the NodeId-Index will be different) as in the original OPC UA server.

The required namespaces for Machinery and Machine Tools (see 4. above) is only loaded once in the aggregated server.

![Address space](img/Addressspace_aggregated.png "Adress space aggregated")
