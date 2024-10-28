# Software in SD Desktop

When you log into the virtual desktop, you are guided to a digital workspace that looks like a computer screen. This workspace is powered by a type of operating system called Linux, and you can choose between two versions: Ubuntu 22 or CentOS 7 (dismissed in 2024). 
The virtual desktop comes with some basic tools or software that you can use right away (listed below). However, this basic toolkit provides you a rather limited set of open-source software. 

The virtual desktop can also become a versatile research workspace designed to adapt to your specific needs **via customization with** a simple application called Software installer that sypportds you in adding sofwatre and customizing you virtual desktop for thos with techincal expertice, it is possible to created customized containes with apptainer or podman.

  Below you can find:
  - list of software avaulable by defalt in Sd Desktop
  - Adding software: background information anf limitations
  - introduction to SD Sfotware installer application and link to totorial (no previous experience required)
  - introduction to customisation via apteniners and podman and link to totorial  (advances, techincal expertice required). 


Please don't hesitate to contact [CSC Service Desk](../../support/contact.md) if you have any questions about the software selection (subject: Sensitive Data). We can support you in your Desktop customization. Moreover, we are working on developing our services to provide proprietary software. Follow our webpage for constant updates. 



## Default software selection in SD Desktop

Below we list some of the most commonly used tools that are by default installed in SD Desktop machines.
The list is not complete and there are small differences between different linux flavours.

| **Category**              | **Software**                                                                                                                                                                       |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Office Tools**          | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                         |
| **Programming**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md) including packages: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R & RStudio**           | [R / RStudio Server](./sd-desktop-access.md#accessing-rstudio) <br> - Matching the r-env-singularity/4.0.5 module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - 1000+ pre-installed R packages (versions available on Apr 20, 2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - GIS software (PROJ, GDAL, SAGA) <br> - CUDA drivers <br> - TensorFlow (used with R TensorFlow back-end) <br> - R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)                 |
| **Workflow Engines**      | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                                                                                                |
| **Software Containers**    | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (Only in Ubuntu machines)                                                                                                                             |
| **Scientific Software**    | - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                                                                                                                          |
| **Terminals & Interfaces** | - [Byobu](https://www.byobu.org/) (Only in Ubuntu machines.) <br> - [Jupyter](https://jupyter.org/)                                                                                                                         |


## Adding software: background information

The virtual desktops (or virtual machines) are intentionally isolated from the internet for security reasons. Consequently, the process of adding supplementary software and libraries is not straightforward. The absence of a network connection precludes the use of conventional installation tools such as _git_, _coda_, _cpan_ or _pip_ in their typical fashion, as these tools rely on external repositories. Furthermore, users on the SD Desktop do not possess the necessary superuser access to execute operations requiring elevated permissions.
Adding extra software to SD Desktop is possible, but it involves converting the installation steps into special files. These files are then uploaded to SD Connect and copied to your SD Desktop for installation. For this process, we recommend using Apptainer containers for importing the software you need, but Apptainer is not the only option. You can also import software for example as Appimage files, Ubuntu 22.04 compatible binaries or as source code.


## SD Software installer

SD Software installer provides an easy-to-use tool to add some commonly used software to SD Desktop (Eg. Rstudio 4.2.2, Whisper, VSCode and GATK). SD Software installer is based on installation scripts provided by CSC. Users can't add their own tools to the SD Software installer, but you can send requests for new tools to be added. Please follow this step-by-step totutorial: 


<iframe width="512" height="288" srcdoc="https://www.youtube.com/embed/S4hpjPy-TDQ" title="How to install software on SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


### Step 1: send a request 

* ***Login to [SD Connect service](https://sd-connect.csc.fi)*** and if you have never uplaoded any files, please uplaod a small test file in a folder. Unfortunately there is currently a techincal problem if you have never uplaoded files.
  
* In SD Connect user inetrface, please check what is the Share ID for your CSC project, a unique 32-digit code associated with a CSC project, on the top left corner of teh user inetrface and sharing with us via email at servicedesk@csc.fi (subject: SD Services) indicating that you wish that the SD software installer would be 
made available for your project.

![(screenshot)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID.png)


### Step2: installing the SD Software Installer on your virtual desktop

* Log in to [SD Desktop service](https://sd-desktop.csc.fi/guacamole/#/), access your virtual dekstop. Here open the **Data Gateway** application, select SD Connect and enter your CSC username and password. Next click on Open. Do not close the Data Gateway application.
  
* If the software installation help tools are enabled for your project, then you should have folder `tools-for-sd-desktop` included in the directory that Data Gateway created (in `Projects/SD-Connect/your-project-name`).

* Open `tools-for-sd-desktop` folder and from there, drag/copy file `sd-installer-centos7.desktop` or `sd-installer-ubuntu22.desktop` to your desktop.
Select the version that matches the operating system of your SD Desktop (e.g. Ubuntu). 

[![Installing-sd-installer](../images/desktop/sd-installer1.png)](../images/desktop/sd-installer1.png)

**Figure 1.** Copying `sd-installer.desktop` file to SD desktop.
 
* Double-click the copy of the installer tool in your desktop to start the software installation tool. In Ubuntu based virtual desktops you
need to right-click the and select _Allow Launching_ before you can use the installer.

[![sd-installer](../images/desktop/sd-installer2.png)](../images/desktop/sd-installer2.png)

**Figure 2.** SD Software installer

### Step 3: Usage

* In order to use the installer, you must have an active Data Gateway connection running and
mounting of the SD Connect data should be done through the default location in the file system
(_Projects_ directory in the users home directory).

* The installer shows a panel of buttons that allow you to install a software by just clicking the button.
The available software include graphical and command line applications. For graphical applications, a launching icon is added 
to the desktop. All software is installed to directory `/shared-directory/sd-tools/` where the installation is available for all the
users of the virtual desktop.

* In case of some applications, part of the installation process occurs only when the application is started for the first time.
Thus, you should start the application once after the installation, to make sure that the process is completed. After that
the installed software should work also when Data Gateway connection has not been opened.


### Software avalable

| **Category**          | **Tool**                                                                                                                                                                                                                     |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Statistics**        | [RStudio 4.2.2](../r-in-sd-desktop.md) - R statistics tool with a graphical user interface and help tools for adding libraries. <br> *After installation, right-click the RStudio desktop icon and select: Allow launching.*   |
|                       | [PSPP](https://www.gnu.org/software/pspp/) - Open Source alternative for SPSS statistics tool. <br> *After installation, right-click the PSPP desktop icon and select: Allow launching.*                                    |
| **Imaging and Videos**| [Audacity](https://www.audacityteam.org/) - Sound editor. <br> *After installation, right-click the Audacity desktop icon and select: Allow launching.*                                                                      |
|                       | [ELAN 6.7](https://archive.mpi.nl/tla/elan/) - Annotation tool for audio and video recordings. <br> *After installation, right-click the ELAN desktop icon and select: Allow launching.*                                       |
|                       | [OpenShot 3.1.1](https://www.openshot.org/) - Video editor. <br> *This tool works only in Ubuntu 22-based virtual desktops. After installation, right-click the OpenShot desktop icon and select: Run as a program.*        |
|                       | [QuPath 0.4.2](https://github.com/qupath/qupath/) - Software for bioimage analysis.                                                                                                                                        |
|                       | [Whisper](whisper.md) - Automatic speech recognition.                                                                                                                                                                         |
| **Geosciences**       | [QGIS 3.1.1](https://qgis.org/en/site/) - A Free and Open Source Geographic Information System. <br> *[QGIS at CSC servers](../../../apps/qgis.md)*                                                                         |
| **Biosciences**       | [GATK](https://gatk.broadinstitute.org/hc/en-us) - A genomic analysis toolkit focused on variant discovery.                                                                                                               |
|                       | [GCTA 1.94.1](https://yanglab.westlake.edu.cn/software/gcta/#Overview) - A tool for Genome-wide Complex Trait Analysis.                                                                                                     |
|                       | [GCTB 2.05b](https://cnsgenomics.com/software/gctb/#Overview) - Genome-wide Complex Trait Bayesian analysis.                                                                                                               |
|                       | [IGV 2.16.2](https://igv.org/doc/desktop/) - Integrated Genomics Viewer. <br> *After installation, right-click the IGV desktop icon and select: Allow launching.*                                                           |
|                       | [MultiQC 1.10](https://multiqc.info/) - NGS Read quality checking tool.                                                                                                                                                    |
|                       | [PRSice 2.0](https://choishingwan.github.io/PRSice/) - Polygenic Risk Score software for calculating, applying, evaluating, and plotting the results of polygenic risk scores (PRS) analyses.                              |
|                       | [Regenie 3.3](https://rgcgithub.github.io/regenie/) - Program for whole genome regression modelling of large genome-wide association studies.                                                                                 |
|                       | [Salmon 1.9.0](https://combine-lab.github.io/salmon/) - Program to produce transcript-level quantification estimates from RNA-seq data. <br> *[Salmon 1.9.0 at CSC servers](../../../apps/salmon.md)*                     |
| **Miscellaneous**     | [auto-apptainer](./auto-apptainer.md) - Tool to add command line applications using the Apptainer container library provided by CSC.                                                                                         |
|                       | [add-python-lib](./sd-pythonlibs.md) - Help tool to add Python libraries.                                                                                                                                                  |
|                       | [Backup tool](./backup_sd_desktop.md) - Help tool to automate backup and export in SD Desktop.                                                                                                                             |
|                       | [VS Code 1.90.2](./vscode.md) - Code editor. <br> *After installation, right-click the VS Code desktop icon and select: Allow launching.*                                                                                   |
|                       | [WEKA 3-8-6](https://ml.cms.waikato.ac.nz/weka/index.html) - Data mining software.                                                                                                                                         |

 

   
## Software customisation with Apptainer and Podman (advanced)

If you want to add new software to your virtual machine independently, the most convenient way is to build an Apptainer container outside SD Desktop and then import the container through SD Connect to SD Desktop. The two documents below describe two sample cases on adding software with containers.

   1. [Importing ready-made Apptainer containers from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creating your own Apptainer container and importing it to SD Desktop](./creating_containers.md)

In Ubuntu22-based virtual machines you can use also Podman container manager. One of the benefits of Podman is that it can utilize Docker containers too.

*   [Using Podman in SD Desktop](./tutorials/podman-in-sd-desktop.md)


!!! Note
    Please don't hesitate to contact [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data). We can support you in your Desktop customisation. 
