# Organizational and technical requirements for umati showcase participants

## umati showcase demonstration participants

Please register with [info@umati.org](mailto:info@umati.org) if you intend to participate at the umati showcase demonstration to ensure you receive all necessary information.

Parties involved in the showcase will offer different umati technology. We distinguish three solution types:

- **Component manufacturers (C)** supply umati partner components or industrial controls with [OPC UA Server](SERVER.html)s according to the umati showcase specification.
- **Machine tool manufacturers (M)** equip machine tools with the umati interface ([OPC UA Server](SERVER.html)) according to the umati showcase specification.
- **Application providers (A)** display and analyze provided data available over the umati interface according to the umati showcase specification.

Participants can provide more than one umati partner solution type.

## Memorandum of understanding

Regulations concerning offered services, obligations of the participants and brand usage are collected in a **memorandum of understanding** (MoU) which participants of the umati showcase will need to sign ahead of the umati showcase demonstration. Please refer to **MoU document** for further information. (Please request a copy by mailing to [info@umati.org](mailto:info@umati.org))

Every participant is permitted to advertise his or her involvement in the umati project through the free, time-limited **&quot;umati partner&quot;** logo, e.g. in the web or in prints etc. This permission ends one year after publication of the first umati OPC UA Companion Specification (OPC 40001-1 UA for Machinery). A product-assigned label will follow.

### Services offered by umati iniative include

- Listing all participants on the [http://umati.org](http://umati.org) website, prints, presentations etc. where practicable in scope and extent.
- Providing a corporate design to be used by all participants for free.
- Advertisement flyers, press conference, social media campaign with mentioning of all participants.

### Obligations of all participants include

- The “partner” is responsible to actively support the dissemination of umati amongst his customers, suppliers and market competitors.
- The “partner” shall participate in demonstration scenarios by connecting a product (obsolete
if the partner is an end user of machinery or software)
- The “partner” is obliged to ensure the visibility of umati in his communication, which includes
placing a reference to umati in his internet presence and to link to [http://umati.org](http://www.umati.org)
- The “partner” should become actively involved in the development of related OPC UA standards (providing feedback on documents circulated to the partners; participation in tests, plug fests, hackathons and the like).
- The “partner” shall support communication of umati, e.g. by providing statements or visuals, and permits the use of the “partner’s” logo for all public relations activities relating to umati.
- The “partner” must actively announce their participation in the umati showcase demonstration ahead of the trade show, e.g. in press conferences, newsletters, advertisement, etc.
- The “partner” must advertise umati at its booth in a visible way (roll-ups, banners, stickers on machines with QR code, display of informational material).
- The “partner” must educate booth personnel to inform visitors about umati. At any point in time at least one expert (umati proficient) must be available at the booth.
- For networking events of other marketing events, the “partner” offers at least one employee for participation.

#### Obligations of participants (M) connecting machinery

- Participant (M) must connect one or more machines that offer reliant data during the exhibition times. The machines do not need to be present on the METAV fair ground.
- Participant (M) agrees to full data openness, i.e. the data delivered during exhibition times may be used by any other umati showcase participant without restrictions.
- Participant (M) consents that all data delivered during exhibition times are archived by VDW and can be used in anonymized form for future demonstrations or tests.

#### Obligations of participants (C) supplying components

- Participants (C) without connected machines must verifiably offer support to other participants (M) for the connectivity via the umati interface.

Obligations of participants (A) showing applications

Participants (A) need to be aware, show sensitivity, and communicate that the umati showcase demonstration is demonstration only, i.e., data flowing in which can be used for analysis is not real production data and cannot be used to deduct any considerations regarding the performance of any connected equipment.

Please refer to the MoU for further details. In case of doubt/discrepancies to the preceding list the regulations as denoted in the MoU shall apply. A separate MoU is available for associations or other organizations that want to support umati. Please contact us at [info@umati.org](mailto:info@umati.org) for details.

## Marketing package for umati showcase participants

All participants received a marketing package which will be updated as the trade fairs approach. It currently contains the following items and can be found at: [https://vdw.de/umati-partner](https://vdw.de/umati-partner):

- **umati partner logo:** The umati Partner logo should be used in your marketing and press materials online as well as offline.

- **umati sticker for the connected machines:** [TODO: is currently prepared – not yet available] Each machine should be outfitted with a umati sticker. If you are connecting a machine that is not located on the fair ground, please find a suitable place for this sticker on your booth to enable visitors to access the dashboard side of your machine with this code. A picture of the sticker is shown below (diameter 200mm).

- **press release from VDW** : informs about the showcase and the registered parties. Please use it also for your own communication as a template. Further press releases are going to follow.
- **umati showcase folder** : [TODO:is currently prepared – not yet available] we will prepare a umati folder like the EMO version, but with more content and listing every partner and the booth information.
- **umati dashboard:** We provide a umati dashboard via a weblink to visualize all machines connected to the showcase. You are free to use this dashboard at your own booth. The dashboard access is described in chapter 4.
- **umati representative preparation/briefing:** We provide extensive documentation for your umati representatives (called umati Ambassadors), such that your employees can answer the most common questions concerning umati. For other booth personnel we provide a shortened version of this document.

### Necessary interaction by the participants are

- If you publish information or are mentioning umati partnership in other places, please **keep us informed by either sending a copy or a URL** for online material.

- For the fair with a central **umati booth**, there will be a logo wall with all umati partners. Please **provide a logo to us**.
- For picturing your machine on the umati dashboard, please **send us a picture of the specific machine** to [info@umati.org](mailto:info@umati.org) (Image will be compressed to 1100x800 if it&#39;s larger) together with the Namespace URI of the machine in the datahub. If you do not provide a picture, we will instead display a dummy machine icon.

## Documentation, timeline and notes on implementation details for umati showcase

### Provided documents and files

We have provided reference documents for the umati showcase information model as follows:

- Specification of [OPC UA server](SERVER.html) and parameter set for umati demonstrators, offers an extensive description of the umati showcase demonstrator story, organizational and technical requirements for all participants, specification of the umati showcase [OPC UA Server](SERVER.html) as well as documentation, timeline and notes for the umati showcase [OPC UA Server](SERVER.html) and client implementations
- [Memorandum of understanding](TODO:LINK) regulates the use of the brand, services offered by VDW and obligations of the participant in context to the umati showcase demonstrations, if you have registered as a umati partner already, there is no need to sign the MoU again.
- **Nodeset files**, describes the types specified in the umati showcase information model
- **Example instance**, depicts an instance view of the umati showcase information model
- **UaModeler-project**, combines the afore-mentioned XML-Nodesets in a common SDK tool environment to view the information model and adapt the instances easily to your machine tool (license required for XML export).
- for marketing materials and the umati ambassador/booth personnel documentation see [https://vdw.de/umati-partner](https://vdw.de/umati-partner) for current versions and details.

### Timeline for ramp-up

Infrastructures and tools are still under development. In the following you find expected release dates for prototypes and final implementations/design freezes. These **may change without notice** , please refer to the most recent version of this document for current dates.

| **Item** | **Supplier** | **Prototype available for all umati showcase participants** | **Design Freeze for umati showcase** |
| --- | --- | --- | --- |
| **Information Model Outline** | umati Initiative | 21.07.2020 |
| **Parameter Specification** | umati Initiative | 21.07.2020 | 31.08.2020 |
| **Server Functionality Specification** | umati Initiative | 21.07.2020 |
| **Dashboard** | umati | available |
| **Testserver** | umati | available |
| **Datahub update** | T-Systems | 23.08.2020 | 31.08.2020 |
| **OpenVPN configuration** | T-Systems | available |
| **Authentication at the datahub ([OPC UA Server](SERVER.html))** | T-Systems | available |

Deadlines for umati showcase participants:

| **Date** | **Activity** |
| --- | --- |
| **ongoing** | Sign and return MoU |
| **ongoing** | Mention your umati partnership during your METAV communication |
| **31.08.2020** | Provide machine image for umati dashboard |
| **6 weeks before a fair date** | Clarify the sticker placement with your marketing/booth responsible person |
| **10.09.2020** | Integration of an OPC UA-Server in the datahub. The integration is not possible during the fair. |
