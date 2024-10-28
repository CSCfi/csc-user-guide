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


### SD Software installer

SD Software installer provides an easy-to-use tool to add some commonly used software to SD Desktop (Eg. Rstudio 4.2.2, Whisper, VSCode and GATK). SD Software installer is based on installation scripts provided by CSC. Users can't add their own tools to the SD Software installer, but you can send requests for new tools to be added. Please follow this step-by-step totutorial: 

   - [SD Software installer](./tutorials/sd-software-installer.md)
 
   
### Software customisation with Apptainer and Podman

If you want to add new software to your virtual machine independently, the most convenient way is to build an Apptainer container outside SD Desktop and then import the container through SD Connect to SD Desktop. The two documents below describe two sample cases on adding software with containers.

   1. [Importing ready-made Apptainer containers from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creating your own Apptainer container and importing it to SD Desktop](./creating_containers.md)

In Ubuntu22-based virtual machines you can use also Podman container manager. One of the benefits of Podman is that it can utilize Docker containers too.

*   [Using Podman in SD Desktop](./tutorials/podman-in-sd-desktop.md)


!!! Note
    Please don't hesitate to contact [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data). We can support you in your Desktop customisation. 
