---
tags:
  - Academic
catalog:
  name: CSD
  description: Cambridge Structural Database and software for searching and analysing crystal structures
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - Roihu
---

# CSD

The Cambridge Structural Database is a collection of small-molecule
organic and organometallic crystal structures determined by X-ray and
neutron diffraction techniques.

## Available

-   Roihu-CPU: CSD, Version 2026.1
-   Download and install locally

Run `module spider ccdc` to see module versions and how to load them.

## License

CSC provides a national license
which allows unlimited installations for **academic usage** at universities
and non-profit research institutes, as well as,
access to WebCSD from institutional IP (Internet Protocol) address ranges. Currently, the
following universities have access to CSD: Aalto, Helsinki, Oulu,
Eastern-Finland, Jyväskylä, Turku, Åbo Akademi, Lappeenranta University
of Technology, Finnish Defence Forces University. If you want your
university or research institute added, fill in the [License agreement](../img/CSDLicenseAgreementTemplateNAC.pdf) and [contact us via Service Desk](../support/contact.md)

Using the CSD components requires adhering [to these conditions](../img/CSDLicenseAgreementTemplateNAC.pdf).

## Usage

The **Cambridge Structural Database System** has two major components:

-   The Cambridge Structural *Database* ([CSD](https://www.ccdc.cam.ac.uk/solutions/software/csd/))
-   *Software* for search, retrieval, display and analysis of CSD
    contents: ConQuest, VISTA, PreQuest, Superstar, Mercury, GOLD, and
    CSD-CrossMiner.

Software to access and analyse CSD entries:

-   [ConQuest](https://www.ccdc.cam.ac.uk/solutions/software/conquest/) search and retrieval software
-   [Mercury](https://www.ccdc.cam.ac.uk/solutions/software/mercury/) graphical display, analysis and visualisation of data
-   [Hermes](https://www.ccdc.cam.ac.uk/solutions/software/hermes/) Main graphical interface to analysis tools
-   [CSD-Editor](https://www.ccdc.cam.ac.uk/solutions/software/csd-editor/) In-house database creation tools (previously PreQuest)
-   [IsoStar](https://www.ccdc.cam.ac.uk/solutions/software/isostar/) A Knowledge Base of Intermolecular Interactions
-   [Mogul](https://www.ccdc.cam.ac.uk/solutions/software/mogul/) A Knowledge Base of Molecular Geometry
-   [SuperStar](https://www.ccdc.cam.ac.uk/solutions/software/superstar/) Predicting Protein-Ligand interactions using experimental knowledge-base data
-   [WebCSD](https://www.ccdc.cam.ac.uk/solutions/software/webcsd/) browser access to the CSD database
-   [CrossMiner](https://www.ccdc.cam.ac.uk/solutions/software/csd-crossminer/) interactive versatile pharmacophore query tool
-   [DASH](https://www.ccdc.cam.ac.uk/open-source-products/dash-software/) Solving crystal structures from powder diffraction data interactively (only for Windows)

There are three ways to access the CSD System:

-   Local installation (Windows or Linux, takes up a lot of disk space)
-   Using the CSD System via the [Roihu web interface](../computing/webinterface/index.md)
-   WebCSD (limited functionality), point your browser to [CCDC webserver](https://www.ccdc.cam.ac.uk/structures)

Initialize CSD on Roihu-CPU:

```bash
module load ccdc/2026.1
```

### Using CSD as a local installation

A local installation is the recommended way for power users. It works on
Windows and Linux. The full installation requires ~18 GB of disk space.

1.  Download the installation media from the
    [CCDC website](https://www.ccdc.cam.ac.uk/). The download needs the site number
    and confirmation code of your university.
2.  Install the software on your computer.
3.  Activate the product with the CCDC Software Activation tool. The activation
    also needs the site number and confirmation code.

To obtain the required codes, contact either
[CSC Service Desk](../support/contact.md) or the local CSD
administrator at your university. Your university must be covered by the
national license (see [License](#license)).

### Using CSD on Roihu via the web interface

The graphical CSD programs run on Roihu in the
[Roihu web interface](../computing/webinterface/index.md) (Open OnDemand).
You only need a web browser and a CSC user account. Nothing is installed on your computer.
Use the [Accelerated visualization](../computing/webinterface/accelerated-visualization.md) app.

!!! warning "Note"
    Use the Accelerated Visualization app, not the Desktop app. See [Known issues](#known-issues).

1.  [Open the Roihu web interface](https://roihu.csc.fi/) and log in
    using your CSC user account.
2.  Open **Accelerated Visualization** (under *Graphical applications*). Select the **Project**
    and set the resources: **Number of CPU cores**, **Memory (GiB)** and **Time**.
    Leave **Reservation** as *No reservation*. The **Partition** is `vizinteractive`, which reserves one GPU (L40).
3.  Launch the app. When the session has started, connect with a web browser
    (noVNC, **Launch Desktop**).
4.  In the session, open a terminal and move to a suitable working directory.
5.  Load the CSD module with `module load ccdc/2026.1`.

Now you have access to CSD programs, e.g. ConQuest, Hermes, Mercury and Mogul. Run them
by typing `cq`, `hermes`, `mercury`, or `mogul` in the terminal, respectively. Note that
the GUI (Graphical User Interface) performance can be somewhat slow compared to a local installation.

!!! info "Billing"
    The session uses GPU Billing Units: one visualization GPU consumes GPU Billing Units
    at approximately the same rate as a full CPU node consumes CPU Billing Units.
    The maximum runtime is 12 hours. Keep the session open only when you are using it,
    and delete it on the *My Interactive Sessions* page when you are done.

[GOLD](gold.md) has its own entry in Docs CSC.

### Using WebCSD directly with a browser

WebCSD has limited functionality compared to the other options. It provides most
of the search capabilities.

1.  Use a computer that is within the IP (Internet Protocol) address range of a
    licensed university. This can be a computer on the campus network or a
    computer connected through the university VPN.
2.  Point your browser to the [WebCSD service](https://www.ccdc.cam.ac.uk/structures).

Access does not need further authentication. If there are problems,
[contact CSC Service Desk](../support/contact.md).

## Known issues

**Mercury does not start in the Desktop app.**
The error message is `error while loading shared libraries: libOpenGL.so.0`.
The OpenGL library is missing on the Desktop compute nodes. Use the
Accelerated Visualization app instead.

**ConQuest: "Failed to initialize 3D visualiser".**
The error in the log file `~/togl_error_init*.log` is `couldn't choose pixel format`.
The 3D visualiser does not work in the Accelerated Visualization and Desktop apps.
Start ConQuest without it:

```bash
module load ccdc/2026.1
cq -no3d
```

Searches and the 2D structure diagrams work without the 3D visualiser.

The messages `qtwebengine_dictionaries` and `zygote_host_impl_linux.cc ... Permission denied`
when Mercury starts are harmless.

If the CSD programs ask for activation, load the module first
(`module load ccdc/2026.1`). Do not enter a licence key.

## References

New software for searching the Cambridge Structural Database and
visualising crystal structures  
I. J. Bruno, J. C. Cole, P. R. Edgington, M. Kessler, C. F. Macrae, P.
McCabe, J. Pearson and R. Taylor, *Acta Crystallogr.*, **B58**, 389-397,
2002

Program specific references can be found in each of the [online Documentation and Resources](https://www.ccdc.cam.ac.uk/support-and-resources/ccdcresources/)

## More information

-   Product specific [FAQs](https://www.ccdc.cam.ac.uk/support-and-resources/Support/search?c=Product+Reference) and [useful manuals, tutorials etc.](https://www.ccdc.cam.ac.uk/support-and-resources) available at CSD website.
