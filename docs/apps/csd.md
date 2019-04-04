CSD
---

The **Cambridge Structural Database System** has two major components:

*   The Cambridge Structural _Database_ [CSD](http://www.ccdc.cam.ac.uk/products/csd_system)
*   _Software_ for search, retrieval, display and analysis of CSD contents: ConQuest, VISTA, PreQuest, Superstar, Mercury GOLD and CSD-CrossMiner.

The Cambridge Structural Database is a collection of small-molecule organic and organometallic crystal structures determined by X-ray and neutron diffraction techniques. The present database consists of more than 900 000 entries.

Software to access and analyse CSD entries:

*   [ConQuest](http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/ConQuest.aspx) search and retrieval software
*   [Mercury](http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/Mercury.aspx) graphical display and visualisation of data
*   [PreQuest](http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/PreQuest.aspx) In-house database creation tools
*   [IsoStar](http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/IsoStar.aspx) A Knowledge Base of Intermolecular Interactions (not available on Taito, install locally, or use from CCDC)
*   [Mogul](http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/Mogul.aspx) A Knowledge Base of Molecular Geometry
*   [SuperStar](http://www.ccdc.cam.ac.uk/Solutions/LifeSciences/Pages/SuperStar.aspx) Predicting Protein-Ligand interactions using experimental knowledge-base data
*   [WebCSD](http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/WebCSD.aspx) browser access to the CSD database
*   [SolidFormModule](http://www.ccdc.cam.ac.uk/Solutions/CSDSolidFormSuite/Pages/SolidFormModule.aspx) knowledge-based tools for molecular materials design
*   [CrossMiner](https://www.ccdc.cam.ac.uk/solutions/csd-discovery/components/CSD-CrossMiner/) interactive versatile pharmacophore query tool
*   [DASH](http://www.ccdc.cam.ac.uk/Solutions/PowderDiffraction/Pages/DASH.aspx) Solving crystal structures from powder diffraction data interactively (only for Windows)

### License agreement

Since 2015 CSC has obtained a national license which allows unlimited installations for academic usage, as well as, access to WebCSD from institutional IP address range. Currently, the following universities have access to CSD: Aalto, Helsinki, Oulu, Eastern-Finland, Jyväskylä, Turku, Åbo Akademi, Lappeenranta University of Technology, Finnish Defence Forces University. If you want your university added, fill in the [License agreement](https://research.csc.fi/documents/48467/73370/CCDC+License+Agreement+Template.pdf/bea49ea1-a6ee-4e7e-94d3-9b7ef8e3a361) below and contact Atte via CSC [Service Desk](https://research.csc.fi/support)

Using the CSD components requires adhering [to these conditions](https://research.csc.fi/documents/48467/73370/CCDC+License+Agreement+Template.pdf/bea49ea1-a6ee-4e7e-94d3-9b7ef8e3a361). If your university is not listed above, fill in this document, sign, scan and email to servicedesk at CSC.

### Available

Version 2019 is available on Taito. It is also possible to install the software locally, see above for licensing.

[What's new in 2019](https://downloads.ccdc.cam.ac.uk/documentation/CSDS/2019/Whats_New.pdf)

* * *

### Usage

There are three ways to access the CSD System:

*   Using CSD System on Taito-shell
*   Local installation (Windows or Linux)
*   WebCSD (limited functionality), point your browser in here: [http://webcsd.ccdc.cam.ac.uk/](http://webcsd.ccdc.cam.ac.uk/)

The installation media can be downloaded from the CCDC website, but needs the site number and confirmation code of your university. After installation you need to activate the product. To obtain the required codes, contact either CSC Service Desk or the local CSD administrator at your university. It is also possible to batch activate products, ask for details.

Additionally the WebCSD service can be used directly via a browser from the computers within the university's IP range. Access does not need further authentication. If there are problems, contact CSC's servicedesk at csc.fi. WebCSD can also be accessed with an individual username password pair from any location in Finland.

CSC is a Nationally Affiliated Center for the CSD System. Those university departments who are not yet members and want to have a local installation please contact Atte Sillanpää via Service Desk. Please note that the size of the databases and programs is more than 6 GB (upto 12 GB).

Note also that to use the programs listed above from CSC's taito-shell an X-terminal is needed. In linux this is built-in, but in windows, you will need some extra tweaking. We suggest using the Remote desktop service (NoMachine) which is particularly useful for CSD as it will make the interactive GUI usage fluent also for Linux users. Read more about [NoMachine at CSC](/-/nomachine). The old solution was to use an X-windows emulator, such as [Xming](http://sourceforge.net/projects/xming), but the Remote Desktop is simply better.

**Using CSD on Taito-shell:**

Cambridge Structural Database and programs related to it are available both by the _module_ command.

By typing the command

`module load ccdc`

you have access to programs ConQuest, PreQuest, IsoStar, Vista, Superstar, and Mercury.

For example, to access ConQuest, you need to type

```cq```

or to start Mercury, type

```mercury```

* * *

### References

New software for searching the Cambridge Structural Database and visualising crystal structures  
I. J. Bruno, J. C. Cole, P. R. Edgington, M. Kessler, C. F. Macrae, P. McCabe, J. Pearson and R. Taylor, _Acta Crystallogr._, **B58**, 389-397, 2002

Program specific references can be found here: [http://www.ccdc.cam.ac.uk/support/product\_references/](http://www.ccdc.cam.ac.uk/support/product_references/)

Here's a [link to Gromacs page](gromacs.md#ankkuri) anchor that works
