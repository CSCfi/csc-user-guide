# CSD

The Cambridge Structural Database is a collection of small-molecule
organic and organometallic crystal structures determined by X-ray and
neutron diffraction techniques.

## License
CSC provides a national license
which allows unlimited installations for **academic usage** at universities
and non-profit research institutes, as well as,
access to WebCSD from institutional IP address ranges. Currently, the
following universities have access to CSD: Aalto, Helsinki, Oulu,
Eastern-Finland, Jyväskylä, Turku, Åbo Akademi, Lappeenranta University
of Technology, Finnish Defence Forces University. If you want your
university or research institute added, fill in the 
[License agreement](../img/CSDLicenseAgreementTemplateNAC.pdf) 
and [contact us via Service Desk](../support/contact.md)

Using the CSD components requires adhering [to these conditions](../img/CSDLicenseAgreementTemplateNAC.pdf).

## Available

- Puhti: 2021
- Download and install locally

## Usage

The **Cambridge Structural Database System** has two major components:

-   The Cambridge Structural *Database* ([CSD])
-   *Software* for search, retrieval, display and analysis of CSD
    contents: ConQuest, VISTA, PreQuest, Superstar, Mercury, GOLD, and
    CSD-CrossMiner.

Software to access and analyse CSD entries:

-   [ConQuest] search and retrieval software
-   [Mercury] graphical display, analysis and visualisation of data
-   [Hermes] Main graphical interface to analysis tools
-   [PreQuest] In-house database creation tools
-   [IsoStar] A Knowledge Base of Intermolecular Interactions (not
    available on Puhti, please install locally, or use from CCDC)
-   [Mogul] A Knowledge Base of Molecular Geometry
-   [SuperStar]
    Predicting Protein-Ligand interactions using experimental
    knowledge-base data
-   [WebCSD] browser access to the CSD database
-   [CrossMiner] interactive versatile pharmacophore query tool (not available on Puhti)
-   [DASH] Solving crystal structures from powder diffraction data
    interactively (only for Windows)

There are three ways to access the CSD System:

-   Local installation (Windows or Linux, takes up a lot of disk space)
-   Using the CSD System via the [Puhti web interface](../computing/webinterface/index.md)
-   WebCSD (limited functionality), point your browser to [CCDC webserver](http://webcsd.ccdc.cam.ac.uk/)

### Using CSD as a local installation

The installation media can be downloaded from the CCDC website, but
needs the site number and confirmation code of your university. After
installation you need to activate the product. To obtain the required
codes, contact either [CSC Service Desk](../support/contact.md)
or the local CSD administrator at your university. This is the
recommended way for power users. The full installation requires ~18 GB of disk space.

### Using CSD on Puhti

[Open the Puhti web interface](https://puhti.csc.fi/) using a web browser and login using your CSC user account.

1. From there, [launch a Desktop](../computing/webinterface/desktop.md#launching).
2. Open a `Host Terminal` and  move to a suitable working directory.
3. Load the CSD module with `module load ccdc/2021`.

Now you have access to the programs ConQuest, Hermes, Mercury and Mogul. Run them by typing `cq`, `hermes`, `mercury`, or `mogul` in the terminal, respectively. Note that the GUI performance can be somewhat slow as the Puhti web interface does not yet provide accelerated graphics.

[GOLD](gold.md) has its own entry in Docs CSC.

### Using WebCSD directly with a browser

The [WebCSD service](https://www.ccdc.cam.ac.uk/structures) 
provides most of the search capabilities directly via a browser from
the computers within the licensed university's IP range. Access does not need
further authentication. If there are problems, [contact CSC
Service Desk](../support/contact.md).

## References

New software for searching the Cambridge Structural Database and
visualising crystal structures  
I. J. Bruno, J. C. Cole, P. R. Edgington, M. Kessler, C. F. Macrae, P.
McCabe, J. Pearson and R. Taylor, *Acta Crystallogr.*, **B58**, 389-397,
2002

Program specific references can be found in each of the
[online Documentation and Resources](https://www.ccdc.cam.ac.uk/support-and-resources/ccdcresources/)

## More information


FAQs and useful tutorials can be found at [the CSD website](https://www.ccdc.cam.ac.uk/support-and-resources) and e.g. in the [FAQ](https://www.ccdc.cam.ac.uk/support-and-resources/Support/search?c=Product+Reference).

  [CSD]: http://www.ccdc.cam.ac.uk/products/csd_system
  [License agreement]: https://research.csc.fi/documents/48467/73370/CCDC+License+Agreement+Template.pdf/bea49ea1-a6ee-4e7e-94d3-9b7ef8e3a361
  [ConQuest]: http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/ConQuest.aspx
  [Mercury]: https://www.ccdc.cam.ac.uk/solutions/csd-system/components/mercury/
  [Hermes]: https://www.ccdc.cam.ac.uk/support-and-resources/ccdcresources/Hermes_User_Guide.pdf
  [PreQuest]: http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/PreQuest.aspx
  [IsoStar]: http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/IsoStar.aspx
  [Mogul]: http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/Mogul.aspx
  [SuperStar]: http://www.ccdc.cam.ac.uk/Solutions/LifeSciences/Pages/SuperStar.aspx
  [WebCSD]: http://www.ccdc.cam.ac.uk/Solutions/CSDSystem/Pages/WebCSD.aspx
  [SolidFormModule]: http://www.ccdc.cam.ac.uk/Solutions/CSDSolidFormSuite/Pages/SolidFormModule.aspx
  [CrossMiner]: https://www.ccdc.cam.ac.uk/solutions/csd-discovery/components/CSD-CrossMiner/
  [DASH]: http://www.ccdc.cam.ac.uk/Solutions/PowderDiffraction/Pages/DASH.aspx

