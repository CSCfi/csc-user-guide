# Software in SD Desktop

Upon logging in to the virtual desktop, you start a graphical Linux enviroment (Ubuntu22 or CentOS 7) with a standard set of software ready to use. This basic toolkit provides you a rather limited set of open-source software. This document lists of most commonly used default software tools in SD Desktop. 
However,you can extend the software selection with e.g. following ways.

* SD Installer: A simple application for easy software additions using pacakges pre build at CSC.
  
* Apptainer and Podman: For those with technical expertise, create customized containers for specialized software setups.




Please don't hesitate to contact [CSC Service Desk](../../support/contact.md) if you have any queistions about the software selection (subject: Sensitive Data). We can support you in your Desktop customization. Moreover, we are working on developing our services to provide proprietary software. Follow our webpage for constant updates. 

However, the virtual desktop can also become a versatile research workspace designed to adapt to your specific needs **via customization with**:

* SD Installer: A simple application for easy software additions.
  
* Apptainer and Podman: For those with technical expertise, create customized containers for specialized software setups.


Default software selection


## Default software in SD Desktop:

The list is not complete and there are small diffenreces between different linux flavour,
   ### Office tools:
   - [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)

   ### Programming
  - go
  - Python3 including packages: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode
   - *R / RStudio Server**
  - Matching the r-env-singularity/4.0.5 module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12)
  - 1000+ pre-installed R packages (versions available on Apr 20, 2021)
  - Intel® oneAPI Math Kernel Library (oneMKL)
  - GIS software (PROJ, GDAL, SAGA)
  - CUDA drivers
  - TensorFlow (used with R TensorFlow back-end)
  - R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)  

   ### Workflow engines:
   - Nextflow
   - Snakemake

   ### Software containers
   - Apptainer
   - Podman (Only in Ubuntumachines)

   ### Scientific Software
   - plink
   - samtools
   - minimap2




## SD Software installer

[SD Software installer](./tutorials/sd-software-installer.md) provides an easy-to-use tool to add some commonly used software to SD Desktop. (Eg. Rstudio 4.2.2, Whisper, VSCode and GATK). SD Software installer is based on installation scripts provided by CSC. Users can't add their own tools to the SD Software istalled, but you can send requests for new tools to be added. 
 
   
## Software customisation with Apptainer and Podman

Users can install their own software to SD Desktop, but this requires technical expertise. As SD Desktop is isolated from the internet, you can't directly use installation tools like _git_, _coda_, _cpan_ or _pip_ as they are dependent on internet connections to external repositories. Further, SD Desktop users can't do any operation that needs superuser access.

If you want to add new software to your virtual machine independently, the most convenient way to add new software to your SD Desktop is to build an Apptainer container outside SD Desktop and then import the container through SD Connect to SD Desktop. The two documents below describe two sample cases on adding software with containers.

   1. [Importing ready-made software containers from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creating you own Singularity container and importing it to SD Desktop](./creating_containers.md)


!!! Note
    Please don't hesitate to contact [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data). We can support you in your Desktop customization. 

In Ubuntu22-based virtual machines you can use also Podman container manager. One of the benefits of Podman is that it can utilize Docker containers too.

*   [Using Podman in SD Desktop](./tutorials/podman-in-sd-desktop.md)
