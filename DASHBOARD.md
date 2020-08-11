# umati Dashboard

The umati dashboard at [https://umati.app](https://umati.app) is available as a neutral sample application.
This dashboard shows all error free machine servers according to the defined standards.

It is connected as a client application to the datahub OPC UA endpoint.

Currently only the integration of the [OPC 40501-1 UA for MachineTools](https://opcua.vdma.org/catalog-detail/-/catalog/3914) is developed. Details about the information modell implentation requrirements are shown [here](Specs/MACHINETOOLS.html).

Integrations of future additional companion specification implementations based on the [OPC 40001-1 UA for Machinery](https://opcua.vdma.org/catalog-detail/-/catalog/3803) are foreseen.

## Datahub

### Datahub connection

For this showcase we will have a datahub provided off premise. This will act as an OPC UA aggregation server. The machine server (M) will connect via an OpenVPN tunnel to an VPN endpoint (one per partner). An OPC UA client will connect to the [OPC UA Server(s)](SERVER.md) of that partner through the VPN tunnel. The application providers (A) will connect to an [OPC UA Server](SERVER.md).

To connect to this datahub (M) need an [OPC UA Server](SERVER.md) and OpenVPN client to access one dedicated endpoint per partner. (A) will connect via OPC UA directly to the datahub.
