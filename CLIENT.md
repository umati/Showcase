# OPC UA Client Requirements

## Connecting an OPC UA client to the datahub

### Aggregated umati showcase OPC UA server

The OPC UA endpoint of the datahub is public accessible by its DNS name. Each client needs to authenticate itself by username/password. The authentication details will be provided to everyone who has sign the MoU and wants to participate in the showcase. (See also chapter 13)

The datahub server will have the data of all connected machines in its address space.
See [Aggregating multiple umati OPC UA servers](Server.html "#Aggregating multiple umati OPC UA servers") for details on the information model.

The datahub OPC UA Server is available at `opc.tcp://datahub.umati.app:12686/umati`.

The following username and password is required to access the OPC UA Server:

**User**: umati-user

**Password**: Please request at [info@umati.org](mailto:info@umati.org) and [g.goerisch@vdw.de](mailto:g.goerisch@vdw.de)

## OPC UA client functionalities

As described in [OPC UA Server](SERVER.html), the client needs to support an encrypted connection, which is authenticated by username and password. The required profiles according to OPC UA Specification Part 7 are listed below:

- Standard UA Client 2017 Profile this includes:
  - Security Policy Required (encrypted connection required)
  - Security User Name Password Client
- Session Client Renew NodeIDs (namespace table might change over time, URI is necessary to detect the required namespace index)

## Getting started: OPC UA client for umati showcase

This specification focuses on the points that are specific to the umati showcase, general functionalities of OPC UA clients are not covered.

- A test server is available for the development of OPC UA clients. This does not correspond to a real machine behavior, but provides changing values in the parameters for functionality testing.

- The start node of the Machines folder in the address space is described in chapter 9 of the [OPC 40001-1 UA for Machinery](https://opcua.vdma.org/catalog-detail/-/catalog/3803). There is no guarantee that the namespace index of a machine will remain the same permanently (e.g. if the datahub is restarted or the connection between the machine and the datahub is interrupted). Therefore, the URI should be used to identify the correct namespace.
- The other nodes can be identified by Browse/ TranslateBrowsePathsToNodeIds.
 The client must be able to ignore certain/unavailable objects because some instances are optional (e.g. spindles or lamps).
- To get data continuously, use subscriptions and monitored items instead of repetitive read requests.
- **Close your session,** if you do not need it anymore. Refrain from using multiple sessions, as this might reduce the performance of the OPC UA Server. For most cases a single session is sufficient for the application.

### umati showcase test server

A test server is provided for basic testing and is supplied by VDW.

The test server provides the complete data model and changes its values. There is no real machine tool simulation behind the [OPC UA Server](SERVER.html). The values do not necessarily have a logical connection to each other. For example, the channel can be deactivated while the job is still being processed. The server is available at `opc.tcp://opcua.umati.app:4840` ; authentication is not required.
