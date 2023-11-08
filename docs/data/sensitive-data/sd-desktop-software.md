# Software in SD Desktop

Upon logging in to the virtual desktop, you start a graphical Linux enviroment (Ubuntu22 or CentOS 7) with a standard set of software ready to use. This basic toolkit provides you a rather limited set of open-source software. This document lists of most commonly used default software tools in SD Desktop and represents methods that can be used to expand the software selection

Please don't hesitate to contact [CSC Service Desk](../../support/contact.md) if you have any queistions about the software selection (subject: Sensitive Data). We can support you in your Desktop customization. Moreover, we are working on developing our services to provide proprietary software. Follow our webpage for constant updates. 

However, the virtual desktop can also become a versatile research workspace designed to adapt to your specific needs **via customization with**


## Default software selection in SD Desktop

Below we list some of the most commonly used tools that are by default installed in SD Desktop machines.
The list is not complete and there are small diffenreces between different linux flavours.

### Office tools:
   - [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)

### Programming
  - [go](https://go.dev/)
  - [Python3](./tutorials/sd-pythonlibs.md) including packages: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode
  - [R / RStudio Server](./sd-desktop-access.md#accessing-rstudio)
     - Matching the r-env-singularity/4.0.5 module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12)
     - 1000+ pre-installed R packages (versions available on Apr 20, 2021)
     - Intel® oneAPI Math Kernel Library (oneMKL)
     - GIS software (PROJ, GDAL, SAGA)
     - CUDA drivers
     - TensorFlow (used with R TensorFlow back-end)
     - R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)  

### Workflow engines:
   - [Nextflow](https://www.nextflow.io/)
   - [Snakemake](https://snakemake.readthedocs.io/en/stable/)

### Software containers
   - [Apptainer](https://apptainer.org/)
   - [Podman](https://podman.io/) Only in Ubuntu machines.
   
### Scientific Software
   - [Plink 1.9](https://www.cog-genomics.org/plink/)
   - [Samtools 1.8](http://www.htslib.org/)
   - [Minimap2 2.26](https://github.com/lh3/minimap2)

### Terminals and interfaces
   - [Byobu](https://www.byobu.org/) (Only in Ubuntu machines.)
   - [Jupyter](https://jupyter.org/)


## Adding software

As SD desktop virtual machines are isolated from internet, installing additional software and libraries is not straight forward. The lack of network connection means that you can't use installation tools like _git_, _coda_, _cpan_ or _pip_ in the normal fashion, as they are dependent on external repositories. Further, SD Desktop users can't do any operation that needs superuser access. Adding extra software is possible, but it requires that the installation processes is converted into files that can be uploaded to SD Connect and from there copied to your SD Desktop environment for installation and usage.

In general, we recommend using Apptainer containers for importing the software you need, but apptainer is the only option.

### SD Software installer

[SD Software installer](./tutorials/sd-software-installer.md) provides an easy-to-use tool to add some commonly used software to SD Desktop. (Eg. Rstudio 4.2.2, Whisper, VSCode and GATK). SD Software installer is based on installation scripts provided by CSC. Users can't add their own tools to the SD Software istaller, but you can send requests for new tools to be added. 
   - [SD Software installer](./tutorials/sd-software-installer.md)
 
   
### Software customisation with Apptainer and Podman

If you want to add new software to your virtual machine independently, the most convenient way is to build an Apptainer container outside SD Desktop and then import the container through SD Connect to SD Desktop. The two documents below describe two sample cases on adding software with containers.

   1. [Importing ready-made Apptainer containers from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creating you own Apptainer container and importing it to SD Desktop](./creating_containers.md)

In Ubuntu22-based virtual machines you can use also Podman container manager. One of the benefits of Podman is that it can utilize Docker containers too.

*   [Using Podman in SD Desktop](./tutorials/podman-in-sd-desktop.md)


!!! Note
    Please don't hesitate to contact [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data). We can support you in your Desktop customization. 
