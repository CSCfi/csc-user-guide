# Customising virtual desktop by adding software & tools for analysis

## Prerequisites

* [Create virtual desktop and volume](sd-desktop-create.md)
* [Access virtual desktop](sd-desktop-access-vm.md)


## Overview

The virtual desktop comes with a limited selection of pre-installed open-source software for analysis (for example, OpenOffice). However, you can use a simple tool called the SD Software Installer, which helps you install the software you need for your project. It doesn't require technical expertise, just follow the step-by-step guidance provided below. Users with technical expertise can also create customised containers using Apptainer or Podman.


<div class="grid cards" markdown>

- :material-check-circle:{ .lg .middle } **Key features**
  { .csc-grid-card-success }

    ---
    
    * **Install software via SD Software Installer:** an easy-to-use tool provided and maintained by CSC that makes it simple to install selected, commonly used software [**software**](#software-available-via-sd-software-installer) on your virtual desktop.
    * **Apptainer software container tool** can be used to add new software to your desktop environment. You can also import software for example as AppImage files, Ubuntu 22.04 compatible binaries or as source code.


- :material-alert:{ .lg .middle } **Limitations**
  { .csc-grid-card-warning }

    ---

    * **Open source software only:** Only open-source software can be installed, as licensed or proprietary software is not supported.
    * **No superuser access:** Users on the SD Desktop do not have superuser access to execute operations requiring elevated permissions.
    * **Isolated from the internet:** The virtual desktops (or virtual machines) are isolated from the internet for security reasons. You can't use tools like Git, Conda or pip to install new software there.
</div>



Below you can find:

* [Default software available in your virtual desktop](#default-software)
* [Software available via SD Software Installer](#software-available-via-sd-software-installer)
* [Add software provided by CSC via SD Software Installer](#add-software-provided-by-csc-via-sd-software-installer)
* [Add your software via Apptainer and Podman (advanced)](#add-your-software-via-apptainer-and-podman-advanced)



## Software in your virtual desktop

=== "Software available via SD Software Installer"

    | **Category**           | **Tool** |
    |------------------------|----------|
    | **Statistics**         | [RStudio 4.5.1](r-in-sd-desktop.md) - R statistics tool with a graphical user interface and help tools for adding libraries. <br> *After installation, right-click the RStudio desktop icon and select: Allow launching.*|
    |                        | [PSPP 2.0.1 ](https://www.gnu.org/software/pspp/) - Open Source alternative for SPSS statistics tool. <br> *After installation, right-click the PSPP desktop icon and select: Allow launching.*|
    |                        | [Octave 9.3.0](https://octave.org/) - Matlab compatible scientific programming language with graphical user interface <br> *After installation, right-click the Octave desktop icon and select: Allow launching.*|
    | **Imaging and Videos** | [Audacity](https://www.audacityteam.org/) - Sound editor. <br> *After installation, right-click the Audacity desktop icon and select: Allow launching.*|
    |                        | [ELAN 6.7](https://archive.mpi.nl/tla/elan/) - Annotation tool for audio and video recordings. <br> *After installation, right-click the ELAN desktop icon and select: Allow launching.*|
    |                        | [OpenShot 3.1.1](https://www.openshot.org/) - Video editor. <br> *This tool works only in Ubuntu 22-based virtual desktops. After installation, right-click the OpenShot desktop icon and select: Run as a program.*|
    |                        | [Praat](https://www.fon.hum.uva.nl/praat/) - Toolkit for speech and sound analysis.|
    |                        | [QuPath 0.6.0](https://github.com/qupath/qupath/) - Software for bioimage analysis.|
    |                        | [Whisper](./tutorials/whisper.md) - Automatic speech recognition.|
    | **Geosciences**        | [QGIS 3.1.1](https://qgis.org/en/site/) - A Free and Open Source Geographic Information System. <br> *[QGIS at CSC servers](../../apps/qgis.md)*|
    | **Biosciences**        | [GATK](https://gatk.broadinstitute.org/hc/en-us) - A genomic analysis toolkit focused on variant discovery.|
    |                        | [GCTA 1.94.1](https://yanglab.westlake.edu.cn/software/gcta/#Overview) - A tool for Genome-wide Complex Trait Analysis.|
    |                        | [GCTB 2.05b](https://cnsgenomics.com/software/gctb/#Overview) - Genome-wide Complex Trait Bayesian analysis.|
    |                        | [IGV 2.16.2](https://igv.org/doc/desktop/) - Integrated Genomics Viewer. <br> *After installation, right-click the IGV desktop icon and select: Allow launching.*|
    |                        | [MultiQC 1.10](https://multiqc.info/) - NGS Read quality checking tool.|
    |                        | [PLINK2](https://www.cog-genomics.org/plink/2.0/) - whole genome association analysis toolset.|                   
    |                        | [PRSice 2.0](https://choishingwan.github.io/PRSice/) - Polygenic Risk Score software for calculating, applying, evaluating, and plotting the results of polygenic risk scores (PRS) analyses.|
    |                        | [Regenie 3.3](https://rgcgithub.github.io/regenie/) - Program for whole genome regression modelling of large genome-wide association studies.|
    |                        | [Salmon 1.9.0](https://combine-lab.github.io/salmon/) - Program to produce transcript-level quantification estimates from RNA-seq data. <br> *[Salmon 1.9.0 at CSC servers](../../apps/salmon.md)*|
    | **Miscellaneous**      | **CSC Tools**, includes: <br>[auto-apptainer](./tutorials/auto-apptainer.md) - Tool to add command line applications using the Apptainer container library provided by CSC.<br> [Backup tool](./tutorials/backup_sd_desktop.md) - Help tool to automate backup and export in SD Desktop.<br> [chipster-installer.sh](./tutorials/chipster-in-sd-desktop.md) - Tool to install local Chipster server to SD Desktop. |
    |                        | [add-python-lib](./tutorials/sd-pythonlibs.md) - Help tool to add Python libraries.|
    |                        | [ARX](https://arx.deidentifier.org/) - Data anonymization tool|
    |                        | [Etherpad](https://etherpad.org/) - tool for collaborative editing (requires Podman compatible virtual machine) | 
    |                        | [OpenRefine](https://openrefine.org/) - Data pre-prosessing and conversion tool for various data formats.|
    |                        | [VS Code 1.90.2](./tutorials/vscode.md) - Code editor. <br> *After installation, right-click the VS Code desktop icon and select: Allow launching.*|
    |                        | [WEKA 3-8-6](https://ml.cms.waikato.ac.nz/weka/index.html) - Data mining software.|

=== "Default software"

    | **Category**              | **Software**                                                                                                                                                                       |
    |---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Office Tools**          | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)   |
    | **Programming**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md) including packages: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
    | **Workflow Engines**      | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/) |
    | **Software Containers**    | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/)         |
    | **Scientific Software**    | - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)             |
    | **Terminals & Interfaces** | - [Byobu](https://www.byobu.org/) <br> - [Jupyter](https://jupyter.org/)   |


## Add software provided by CSC via SD Software Installer

![SD Software Installer](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD_Installer.png){ style="float: right; margin: 0 3em 3em 3em; width: 40%;" }

The SD Software Installer is a CSC‑provided tool that makes it easy to install selected, commonly used [**software**](#software-available-via-sd-software-installer) on SD Desktop, such as RStudio 4.5.1, Whisper, VS Code, and GATK.

You can’t add your own software to the Software Installer, but you can request new tools by [contacting CSC Service Desk](../../support/contact.md) (subject: SD Desktop). 

To install and use the application, please follow the step-by-step tutorial below.  
    
___

### Step 1: Send a request to CSC Service Desk

1. Log in to the [SD Connect service](https://sd-connect.csc.fi). 
    * If you are using SD Connect for the first time, [**upload**](sd-connect-upload.md) a small test file to any bucket (required due to a current technical issue).
2. On the homepage, click **Copy Share ID** next to the project selection menu to copy your project’s Share ID (a 32‑character code, example: 71bbe38a3cd398b48b1f2582dc00297p).
3. Email the CSC Service Desk with the subject “SD Desktop”, requesting access to the Software Installer and including the project Share ID.
4. Once the Service Desk confirms access, move to step 2 below.

![(Share ID)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareID.png)

 ____

### Step 2: Install and use SD Software Installer 

#### 2.1 Install SD Software Installer

1. Log in to [SD Desktop service](https://sd-desktop.csc.fi) and access your virtual desktop. 
Launch **Data Gateway **from navigation on the left side of the screen.
2. Select **SD Connect**.
3. Click **Continue**. 
4. In the next view you are asked to choose a folder for accessible files. Check that **Projects** folder is selected. 
5. Click **Continue**.
6. In the next view click **Open folder**. This opens file browser and you will see folder **Projects**.
7. Navigate to `Projects/SD-Connect/your-project-name`. Locate folder `tools-for-sd-desktop` and open it. **Copy-paste** or **drag-and-drop** file `sd-installer-ubuntu24.desktop` to your desktop.
8. **Right-click **on the icon on your virtual desktop.
9. Select **Allow Launching**.

#### 2.2 Use SD Software Installer

1. Keep the Data Gateway connection open or launch Data Gateway:
    - Select **SD Connect**.
    - Click **Continue**. 
    - In the next view you are asked to choose a folder for accessible files. Check that **Projects** folder is selected. 
    - Click **Continue**.
2. **Launch SD Software Installer** by clicking icon on your virtual desktop. The application will open and you can see the software available. 
3. **Click on the software you want to install.** Keep the Data Gateway connection open for it to be successful. 
Available software includes graphical and command-line applications. For graphical applications, an icon is added to the desktop. 
4. For some applications, part of the installation process happens only when the application is started for the first time. Start the application once after the installation to complete the setup. After that the installed software should work even without an active Data Gateway connection.

![Installing SD Software Installer](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_SD_Installer.png)

____

### Step 3: Software installation for all project members

All software is installed to the directory `/shared-directory/sd-tools/` where the installation files are available for all users of the virtual desktop. However, they don’t automatically appear on each user’s desktop. To make software accessible, project members need to choose between two options:

#### 3.1 Using the Software Installer

The project member can follow the [**steps**](#step-2-install-sd-software-installer-to-your-virtual-desktop) shown earlier: open the Data Gateway, copy the Software Installer to the desktop and launch it.

The Software Installer will detect the tool in the shared folder, skip setup, and automatically create a desktop icon and update the terminal.

#### 3.2 Using a terminal command

In this case the Data Gateway connection is not needed.

* Right-click on the desktop and select **Open Terminal**.
* Press **Ctrl + Alt + Shift** to activate **copy-paste function**.
* Choose Text Input
* Copy the command `/shared-directory/sd-dash-tools/bin/use-sd-tools` from here.
* And paste it into the input bar in the lower part of the screen and press Enter.

In this case as well, the icon will be added to the desktop and the terminal environment will be updated.

____


## Add your software via Apptainer and Podman (advanced)

If you want to add new software to your virtual machine independently, the most convenient way is to build an Apptainer container outside SD Desktop and then import the container through SD Connect to SD Desktop. First convert the installation steps into special files. Then upload them to SD Connect and copy them to your virtual desktop for installation.  The two documents below describe two sample cases on adding software with containers. 

   1. [Importing ready-made Apptainer containers from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creating your own Apptainer container and importing it to SD Desktop](./creating_containers.md)

In Ubuntu24-based virtual machines you can use also Podman container manager. One of the benefits of Podman is that it can utilize Docker containers too.

* [Using Podman in SD Desktop](./tutorials/podman-in-sd-desktop.md)

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Do you need additional software**
  { .csc-grid-card-warning }

    ---
    
    Please don't hesitate to contact [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data). We can support you in your Desktop customisation.

</div>

## Your next steps in this guide

* [Importing data](./sd-desktop-access.md)
* [Exporting data via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)
