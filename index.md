# General Information

- This document provides **all information** to get connected to the umati showcase demonstrator scenario.
- Participants who connect to the showcase, need to do so **on their own**, or with the help of their controls or software supplier. The umati project group **cannot** supply individual support on how to get [OPC UA Servers](Server.md) installed, online and deliver data. If questions arise regarding the information provided in **this documentation** or the connection to the datahub for the umati showcase demonstrator, please open an issue [here](https://github.com/umati/Showcase).

- An FAQ is provided [here](FAQ.md) and will be updated as needed.

## What is umati - the universal machine technology interface

To learn more please visit [https://umati.org](https://umati.org)

---

## Structure of the specification

- [OPC UA Server](Server.md)
- [OPC UA Client](Client.md)
- [Dashboard](Dashboard.md)
- [Implemented Specifications](Specs.md)
  - [MachineTool](Specs/MachineTool.md)
  - [PlasticsRubber](Specs/PlasticsRubber.md)
  - [Software Solutions](Specs/Software.md)
  - [WoodWorking](Specs/Woodworking.md)
  - [Geometrical Measuring Systems](Specs/GeometricalMeasuringSystems.md)
- Upcoming Specifications
  - [Robotics](Specs/WIP.md)
  - [MachineVision](Specs/WIP.md)
  - [Scales](Specs/WIP.md)
- [Organizational Information](Organization.md)
  - [Fairs](Specs/Fairs.md)
- [FAQ](FAQ.md)

### Versioning

This documentation is versioned, as some content details will be delivered later in time. Please refer to the latest version at [https://showcase.umati.org](https://showcase.umati.org) to receive the latest draft. If any errors or inconsistencies strike your attention, please contact us via [info@umati.org](mailto:info@umati.org) so that we can include the improvement in the next version:

| **Version** | **Date published** | **Note on changes** |
| --- | --- | --- |
| v0.01.0 | 08.07.2020 | First draft|
| v1.00.0 | 21.07.2020 | First release |
| v1.01.0 | 11.08.2020 | Update on Machine Tools and Fairs |
| v1.02.0 | 28.08.2020 | Update on Machine Tools and Fairs |
| v1.02.1 | 02.10.2020 | Update on Machine Tools |
| v1.02.2 | 23.11.2020 | Update License and activate CLA |
| v1.02.3 | 18.02.2021 | Update on Machine Tools and Software Solutions |
| v1.03.0 | 21.05.2021 | Complete update to latest developments |
| v1.04.0 | 03.09.2021 | Addition of Woodworking companion specification |
| v1.04.1 | 08.02.2022 | Updates to Machine Tools, Woodworking |
| v1.05.0 | 03.03.2022 | Integrates Geomentrical Measuring Systems |
| v1.06.0 | 13.07.2020 | Integrates PlasticsRubber specifications |

### Changelog

| Doc | Area | Description | Commit |
| --- | --- | --- | --- |
| [Dashboard](Dashboard.md) | Dashboard | Extend the datahub section | [122940e](https://github.com/umati/Showcase/commit/122940ebdd091251cbe5a028c3ffe719b5b6ec63) |
| [License](LICENSE) | License | Update of Repo License| [1e4f3d9](https://github.com/umati/Showcase/commit/1e4f3d934e4e4420554d0509fff11ba4f853e2f3)|
| [MachineTool](Specs/MachineTool.md) | Mapping of information | Pictures of app with mapping added | [f59f93d](https://github.com/umati/Showcase/commit/f59f93dc4eda4bdf4bf00efc53f8560bc6108b35) |
| [MachineTool](Specs/MachineTool.md) | Fair Specification | SoftwareRevision mandatory | [117ce4b](https://github.com/umati/Showcase/pull/16/commits/117ce4bde7a57574de1240e76d2d3aa1160bd517) |
| [MachineTool](Specs/MachineTool.md) | NodeSets for Machine Tools | Clarification on prototyping nodeset for showcase | [a2c4926](https://github.com/umati/Showcase/commit/a2c49264ca66caf6813de1ad8a5706d83ec3aa46) [7628b8a](https://github.com/umati/Showcase/commit/7628b8af38c41da2e01dac70f3d8f8be44f8949c) |
| [Fairs](Specs/Fairs.md) | Shortnames | Update of the fair shortnames | [084e061](https://github.com/umati/Showcase/commit/084e0611be0bf4618e17c07260dd24d397e31ce0) [7a63e15](https://github.com/umati/Showcase/pull/16/commits/7a63e15d3e0fe691630e07814ad9e82dfe2f92b0) |
| [Software](Specs/Software.md) | Software Solutions | Dashboard will show software solutions | [231ffc1](https://github.com/umati/Showcase/commit/231ffc1089b60020570286e095011defcee29b3b) [3b193a3](https://github.com/umati/Showcase/commit/3b193a34d1e64d3e93153023345073ae70e97423) |
| [MachineTool](Specs/MachineTool.md) | Description | Clarification of nodesets and requirements | [c61c73f](https://github.com/umati/Showcase/commit/c61c73fa74b17dce58fd7c938f9992746dbf688d) [e9313fb](https://github.com/umati/Showcase/commit/e9313fb65cd264aee6c256a43e3fd758b737c449) |
| [MachineTool](Specs/MachineTool.md) | Mapping | Updated pictures and mapping | [938a064](https://github.com/umati/Showcase/commit/938a0645771e879ca7cb5ab79be7706b0d4267d4)
| [Server](Server.md) | Fairconnect | Updated fairconnect and connection possibilities | [4f46e04](https://github.com/umati/Showcase/commit/4f46e04431582ccbd1c6714cbd018255e1d09262) |
| [Woodworking](Specs/Woodworking.md) | Specfication | Added specification for Woodworking companion specification | [7642c16](https://github.com/umati/Showcase/commit/7642c16db5f13a44fa8862483a8af8cd43fb43ec) |
| [Organizational Information](Organization.md) | Timeline | Removed the obsolete timeline for a 2020 showcase | [2416d15](https://github.com/umati/Showcase/commit/2416d1569cc43267d86530a934dcab267833d7fb) |
| [MachineTool](Specs/MachineTool.md) | Links | Updates broken links | [5e1af5c](https://github.com/umati/Showcase/commit/5e1af5ce1649addc68d87b87dd1323806a9194e3)  |
| [Woodworking](Specs/Woodworking.md) | Links | Updates broken links | [5e1af5c](https://github.com/umati/Showcase/commit/5e1af5ce1649addc68d87b87dd1323806a9194e3)  |
| [Geometrical Measuring Systems](Specs/GeometricalMeasuringSystems.md) | GMS | Adds specification page | [49c11bc](https://github.com/umati/Showcase/commit/49c11bc70113b8ceb4ea718e8cef5e27dd9ec5ff) |
| [PlasticsRubber](Specs/PlasticRubber.md) | PlasticsRubber | Adds specifications 40077, 40079 RC, 40082-1, 40082-2, 40082-3, 40084-2, 40084-11, PRGeneric | [5c95751](https://github.com/umati/Showcase/commit/5c95751e6a9220ed2fdda5f030d841a8b22e944b) |

## Demonstrator story umati showcase

### The umati vision

Connectivity with umati - universal machine technology interface - is simple, secure and future-oriented. Any machine with an umati interface can be easily connected with applications. No matter whether you are end user, system integrator or machine builder: with the umati interface you will be able to easily connect to machines of all manufacturers and controls. umati is an initiative by the umati community and is an association of companies from the mechanical and plant engineering industry that jointly and comprehensively bring a common interface concept based on OPC UA to the market for the entire mechanical and plant engineering sector. Currently it is sponsored and hosted by the German Machine Tool Builders' Association [(VDW)](https://vdw.de) and the mechanical engineering industry association [(VDMA)](https://vdma.org).

## umati showcase

This showcase demonstrates how **umati partners** connect components, machines and applications via a connectivity showcase. This showcase targets decision-makers in the machinery industry with a uniform marketing strategy and demonstrations showing the depth of the umati interface: from umati component suppliers over umati machine builders to umati partner applications that cumulate the data in dashboards, ERP, MES and cloud systems.

Trade fair guests will get information about umati at the virtual showcase and will be offered a hands-on experience via a white-label dashboard. The dashboard offers data of each individual machine connected through umati. The dashboard is easily accessible through any web browser with individual QR codes offering weblinks at each machine. It further offers responsive design for mobile end users.

Marketing for umati will be visible at the virtual showcase. Central umati marketing events will offer general information, depict specific use cases, offer Q&amp;A sessions and deliver experience reports over the duration of the trade fair. Marketing statements for umati showcase are coordinated centrally and distributed to all showcase participants. Please refer to chapter 3 for further details.

Ramp-up for all umati showcase demonstrations will be available in advance of the virtual showcase with an offered exemplary umati showcase test server.
