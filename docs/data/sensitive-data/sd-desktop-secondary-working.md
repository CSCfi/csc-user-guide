[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Working with your Desktop: tips and essentials

## Prerequisites
* [Create virtual desktop](../sensitive-data/sd-desktop-secondary-create.md)
* [Access virtual desktop](../sensitive-data/sd-desktop-secondary-access-vm.md)

## Work and collaborate in a virtual desktop

Once a virtual desktop has been created, all members of your CSC project can access it. When you log in, you will enter a virtual computer running on a Linux operating system. If you are new to Linux, it might feel a little different from other systems like Windows or macOS.

No technical experience is required to work with it, but while Windows is designed to be user-friendly from the start, Linux can have a learning curve, especially if you need to use the command line. 

The guide below provides clear instructions to help you get comfortable with both Linux and the SD Desktop’s security setup:

- [Security-related features and limitations](sd-desktop-secondary-working.md#security-related-features-and-limitations)
- [Introduction to Linux and virtual desktop](sd-desktop-secondary-working.md#introduction-to-linux-and-virtual-desktop)
- [Copy-paste from your laptop to virtual desktop](sd-desktop-secondary-working.md#copy-paste-from-your-laptop-to-virtual-desktop)
- [Default software available in SD Desktop](sd-desktop-secondary-working.md#default-software-available-in-sd-desktop)
- [Accessing RStudio from virtual desktop](sd-desktop-secondary-working.md#accessing-rstudio-from-virtual-desktop)

## Security-related features and limitations

SD Desktop is a secure environment designed specifically for analysing sensitive data and some features may work differently than a regular computer. For each of these features, a specific step-by-step guide is available. If you are using the service for the first time, reviewing these guides will help you become familiar with how everything works.

!!! Note

    - **Isolated from the internet**: your virtual desktop is completely isolated from the internet. This means that although you can open a web browser like Firefox, you will not be able to access websites or online repositories directly. This feature helps keep your data safe by reducing the risk of online threats.
    
    - **Controlled file access and export with Data Gateway**: Each project member can import files to the virtual desktop for analysis by using a  secure application called [Data Gateway](./sd-desktop-access.md). Files can be imported only via SD Apply service. Data export can be performed only by CSC helpdesk to follow the Findata regulation. Export of anonymous results can be requested from [CSC Service Desk](../../support/contact.md)(subject: SD Desktop).
  
    - **Limited storage space**: The virtual desktop is designed primarily for data analysis and has limited storage space. To expand storage, you can add an external volume (such as an external hard drive) during the desktop setup. This external volume is accessible to all project members and also serves as a backup for imported data.
  
    - **Open source software only**: Only open-source software can be installed in the virtual desktop, as it does not currently support licensed or proprietary software. Each virtual desktop comes with a default set of pre-installed software. If the software you need is not listed below, please [contact CSC Service Desk](../../support/contact.md) for support (subject: SD Desktop).
  
    - **Copy-paste restrictions**: For security reasons, copy-pasting from your own computer to SD Desktop is limited. You can still transfer text with a few extra steps, as explained in the copy-paste instructions below. These restrictions ensure that no unauthorized data is copied or exported from the secure environment.
  
    - **Shared file access for team members**: Any files saved in the shared-directory or on the external volume can be accessed by other project members working in the virtual desktop, allowing safe collaboration.

## Introduction to Linux and virtual desktop

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/r0S1NNN2eQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Linux is an open-source operating system, meaning it is free to use, and its code is openly available for people to view and modify. It's commonly used in many research applications due to its stability, security, and flexibility.

- **Look and feel**: Linux may look slightly different from Windows, depending on the “desktop environment” used. But don’t worry – it still has familiar elements like windows folders and menus. You will find the main menu at the top left corner, where you can access all available software.
  
- **File structure**: Instead of “My Documents” or drives labeled C: or D:, Linux has a different way of organising files. The main directory starts with /, and you’ll see folders like /home for your personal files.
  
- **Benefits**: Linux is very stable and less likely to crash, making it ideal for long or intensive computing tasks.

Below is an image showing the basic functions of a virtual desktop. Click the image to open it in a new window.

[![Virtual desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png)](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png){ target="_blank" }



## Copy-paste from your laptop to virtual desktop

The copy-paste function from your computer/laptop to your virtual desktop is limited for security reasons. However it is possible to copy-paste text with Clipboard. Copy-paste works only in one direction: from your computer to virtual desktop.

### Step by step

1. Go to virtual desktop and open the Clipboard with a key combination **Ctrl+Alt+Shift** and click *Paste*.
2. Activate the copy-paste function by selecting input method ***Text input*** (the Clipboard panel will close automatically after the selection).
3. Now you can copy text normally from your computer (Ctrl+C or mouse right click).
4. Paste the text inside your virtual desktop (Ctrl+V).

    Note: Don't close Clipboard panel with **Cntrl+Alt+Shift**, this might disable the copy-paste function. Please note you have to activate the copy-paste function again every time you use your virtual desktop.

    ![SD Desktop Clipboard screenshot](images/desktop/SD-Desktop-Clipboard.png)  
    *Appearance of the Clipboard (Guacamole tools) may vary a bit depending on browser and local operating system.*

## Default software available in SD Desktop

**You can work with your virtual desktop like with a standard computer**, accessing several pre-installed programs from the applications menu bar (top left corner). Examples include Open Office, image-viewing applications, video and audio players, Jupyter Notebooks etc. You can also open a terminal and use Linux from the command line. For more information on accessing R-Studio, please [check the paragraph below](#accessing-rstudio-from-virtual-desktop).

Below we list some of the most commonly used tools that are by default installed in the virtual desktop. The list is not complete and there are small differences between different desktop options.

| **Category**              | **Software**                                                                                                                                                                       |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Office Tools**          | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                         |
| **Programming**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md) including packages: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R & RStudio**           | [R / RStudio Server](sd-desktop-working.md#accessing-rstudio-from-virtual-desktop) <br> - Matching the r-env-singularity/4.0.5 module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - 1000+ pre-installed R packages (versions available on Apr 20, 2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - GIS software (PROJ, GDAL, SAGA) <br> - CUDA drivers <br> - TensorFlow (used with R TensorFlow back-end) <br> - R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)                 |
| **Workflow Engines**      | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                                                                                                |
| **Software Containers**    | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (Only in Ubuntu machines)                                                                                                                             |
| **Scientific Software**    | - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                                                                                                                          |
| **Terminals & Interfaces** | - [Byobu](https://www.byobu.org/) (Only in Ubuntu machines.) <br> - [Jupyter](https://jupyter.org/)                                                                                                                         |

### Software available via request 

Please contact [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data Services) if you want to bring in additional software into SD Desktop. We will provide you with further instructions. 

Below you can find a list of tools available in our software package. 

| **Category**          | **Tool**                                                                                                                                                                                                                     |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Statistics**        | [RStudio 4.2.2](r-in-sd-desktop.md) - R statistics tool with a graphical user interface and help tools for adding libraries. <br> *After installation, right-click the RStudio desktop icon and select: Allow launching.*   |
|                       | [PSPP](https://www.gnu.org/software/pspp/) - Open Source alternative for SPSS statistics tool. <br> *After installation, right-click the PSPP desktop icon and select: Allow launching.*                                    |
| **Imaging and Videos**| [Audacity](https://www.audacityteam.org/) - Sound editor. <br> *After installation, right-click the Audacity desktop icon and select: Allow launching.*                                                                      |
|                       | [ELAN 6.7](https://archive.mpi.nl/tla/elan/) - Annotation tool for audio and video recordings. <br> *After installation, right-click the ELAN desktop icon and select: Allow launching.*                                       |
|                       | [OpenShot 3.1.1](https://www.openshot.org/) - Video editor. <br> *This tool works only in Ubuntu 22-based virtual desktops. After installation, right-click the OpenShot desktop icon and select: Run as a program.*        |
|                       | [Praat](https://www.fon.hum.uva.nl/praat/) - Toolkit for speech and sound analysis.                                                                                                                                       |  
|                       | [QuPath 0.4.2](https://github.com/qupath/qupath/) - Software for bioimage analysis.                                                                                                                                        |
|                       | [Whisper](./tutorials/whisper.md) - Automatic speech recognition.                                                                                                                                                                         |
| **Geosciences**       | [QGIS 3.1.1](https://qgis.org/en/site/) - A Free and Open Source Geographic Information System. <br> *[QGIS at CSC servers](../../apps/qgis.md)*                                                                         |
| **Biosciences**       | [GATK](https://gatk.broadinstitute.org/hc/en-us) - A genomic analysis toolkit focused on variant discovery.                                                                                                               |
|                       | [GCTA 1.94.1](https://yanglab.westlake.edu.cn/software/gcta/#Overview) - A tool for Genome-wide Complex Trait Analysis.                                                                                                     |
|                       | [GCTB 2.05b](https://cnsgenomics.com/software/gctb/#Overview) - Genome-wide Complex Trait Bayesian analysis.                                                                                                               |
|                       | [IGV 2.16.2](https://igv.org/doc/desktop/) - Integrated Genomics Viewer. <br> *After installation, right-click the IGV desktop icon and select: Allow launching.*                                                           |
|                       | [MultiQC 1.10](https://multiqc.info/) - NGS Read quality checking tool.                                                                                                                                                    |
|                       | [PRSice 2.0](https://choishingwan.github.io/PRSice/) - Polygenic Risk Score software for calculating, applying, evaluating, and plotting the results of polygenic risk scores (PRS) analyses.                              |
|                       | [Regenie 3.3](https://rgcgithub.github.io/regenie/) - Program for whole genome regression modelling of large genome-wide association studies.                                                                                 |
|                       | [Salmon 1.9.0](https://combine-lab.github.io/salmon/) - Program to produce transcript-level quantification estimates from RNA-seq data. <br> *[Salmon 1.9.0 at CSC servers](../../apps/salmon.md)*                     |
| **Miscellaneous**     | [auto-apptainer](./tutorials/auto-apptainer.md) - Tool to add command line applications using the Apptainer container library provided by CSC.                                                                                         |
|                       | [add-python-lib](./tutorials/sd-pythonlibs.md) - Help tool to add Python libraries.                                                                                                                                                  |
|                       | [Backup tool](./tutorials/backup_sd_desktop.md) - Help tool to automate backup and export in SD Desktop.                                                                                                                   |
|                       | [OpenRefine](https://openrefine.org/) - Data pre-prosessing and conversion tool for various data formats.                                                                                                                                         |
|                       | [VS Code 1.90.2](./tutorials/vscode.md) - Code editor. <br> *After installation, right-click the VS Code desktop icon and select: Allow launching.*                                                                                   |
|                       | [WEKA 3-8-6](https://ml.cms.waikato.ac.nz/weka/index.html) - Data mining software.                                                                                                                                         |


## Accessing RStudio from virtual desktop

The computing environment i.e. virtual desktop (visible from your browser) is isolated from the internet. For example, you can open a Firefox web browser in your virtual desktop but not access any site online. At this moment, you will also not be able to access any repositories directly. To open R Studio for data analysis the following steps are required:

1. Open the terminal.

2. Launch RStudio with:

    ```text
    start-rstudio-server
    ```

![Access R-Studio](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_RStudio1.png)


* This will return a URL and a service-specific password:

    ```text
    RStudio Server - Sensitive Data Desktop Edition
    ---------------------------------------------------------------------------------------
    Copy/Paste this URL into Firefox:

    http://localhost:8787/

    -----------------------------------------------------------------------------------------
    Enter these at the RStudio Server sign-in screen
    ----------------------------------------------------------------------------------------
    Username: accountname  Password: Example23241232
    ----------------------------------------------------------------------------------------
    To stop RStudio Server: Ctrl+C
    ```

3.  Copy the URL and paste it in Firefox to open the R-Studio login page.
4. Enter your username and password to access the server.

!!! Note
    Only files saved in the external volume are accessible to other project members using RStudio.

![Access R-Studio](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_RStudio2.png)

Read next:

- [How to import data for analysis in your desktop](./sd-desktop-secondary-access.md)
- [How to manage your virtual desktop (delete, pause, detach volume etc.)](./sd-desktop-secondary-manage.md)
