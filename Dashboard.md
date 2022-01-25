# umati Dashboard (The "umati app")

The umati dashboard at [https://umati.app](https://umati.app) is available as a neutral sample application to demonstrate OPC UA companion specification standardization. 

- This dashboard shows all error free machine servers according to the defined [standards](Specs.md).
- It lists [software solutions](Specs/Software.md) from umati partners, who provide a web accessible demonstration instance.

It is connected as an OPC UA client application to the datahub OPC UA endpoint.

Currently the integration of [OPC 40001-1 UA for Machinery](https://reference.opcfoundation.org/Machinery/docs/) [OPC 40501-1 UA for MachineTool](https://reference.opcfoundation.org/MachineTool/docs/) is developed.

Integrations of future additional companion specification implementations based on the [OPC 40001-1 UA for Machinery](https://opcua.vdma.org/catalog-detail/-/catalog/3803) are in progress.

## Location of Fair, Machine and Software icons on the dashboard

### Fairs

![Fair](img/map_pin_fair.svg)

Location is set by fair organiser.

### Machines

![Machine](img/map_pin_machine_magenta.svg)

The machine instance _Location_ property (according to OPC 40001-1) shall be provided in the format `<fair> <hall> <booth>`, e.g, “METAV 1 A22” or format `<N/S> <Latitude|##.#########> <EW> <Longitude|###.#########>`, e.g. `N 51.257315 E 6.740885` for GPS coordinates.

**The machine only gets a map icon, if it provides at least the GPS location** 

Machines can be referenced to more than one fair by providing a list of fair locations, deliminated by slash e.g. `METAV <XXX> <XXX>/EMO 12 D17/N 51.257315 E 6.740885`

#### FAIR Shortnames

Fair shortnames are defined [here.](Fairs.md)

### Software

![Software](img/map_pin_software_cyan.svg)

The software location will be manual set for now, based on the same principle like machines.


## Datahub

### Datahub connection

For this showcase we will have a datahub provided off premise. This will act as an OPC UA aggregation server. The machine server (M) will connect via an OpenVPN tunnel to an VPN endpoint. An OPC UA client will connect to the [OPC UA Server(s)](Server.md) of that partner through the VPN tunnel. This client will browses for all instances of the supported specifications and will read all values and events of these instances. These values and events are forwarded to an aggregating OPC UA server, which will provide a copy of the instances with values. The application providers (A) will connect to the aggregating [OPC UA Server](Server.md) of this datahub. This ensures a constant load on the unterlying OPC UA servers of the machines, no matter how many applications read the OPC UA data in the aggregating OPC UA server.

To connect to this datahub (M) need an [OPC UA Server](Server.md) and OpenVPN client to access one dedicated endpoint per partner. (A) will connect via OPC UA directly to the datahub.
