# umati Dashboard (The "umati app")

The umati dashboard at [https://umati.app](https://umati.app) is available as a neutral sample application to demonstrate OPC UA companion specification standardization.

- This dashboard shows all error free machine servers according to the defined [companion specifications](Specs.md).
- It lists [software solutions](Specs/Software.md) from umati partners, who provide a web accessible demonstration instance.

Machine data are available in a MQTT broker to provide live to the umati.app

Currently the companion specifications listed at [Specs](Specs.md) are implemented.
Integrations of future additional companion specification implementations based on the [OPC 40001-1 UA for Machinery](https://www.vdma.org/viewer/-/v2article/render/2737109) are in progress.

## Location of Fair, Machine and Software icons on the dashboard

### Fair pin

![Fair](img/map_pin_fair.svg)

Fair location and icon is set by fair organiser.

### Machine pin

![Machine](img/map_pin_machine_magenta.svg)

The machine instance _Location_ property (according to OPC 40001-1) shall be set to the following definition:

- Add GPS coordinates `<N/S> <Latitude|##.#########> <EW> <Longitude|###.#########>`, e.g. `N 51.257315 E 6.740885` to get a machine icon on the world map
- Add fair information `<fairshortname> <hall> <booth>`, e.g, “METAV 1 A22” to be associated to a fair
- **NOTE:** Machines can be referenced to more than one fair by providing a list of fair locations, deliminated by slash e.g. `METAV <XXX> <XXX>/EMO 12 D17/N 51.257315 E 6.740885`

### FAIR Shortnames

Fair shortnames are defined [here](Specs/Fairs.md).

### Software

![Software](img/map_pin_software_cyan.svg)

The software location will be manual set as discribed [here](Specs/Software.md).

## Dashboard Features

The dashboard provides information to solve a few use cases which are common in the companion specifications.

- Identifiy machines from different manufactures
- Provide an status overview of the machines
- Provide tool/measurment data
- Provide monitoring information

For the usage on fairs, the above location information provide the additional use case:

- Identify machines on a fair

These use cases can be access through the Overview, Machines and Software tabs, as well as the filter functionality.
