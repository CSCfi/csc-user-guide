## Default software available on SD Desktop

Upon logging in to teh virtual desktop, you'll find a standard set of software ready to use. This foundational toolkit ensures you can start working immediately and is based on  a limited set of default open-source software. However, the virtual desktop can also become a versatile research workspace designed to adapt to your specific needs via aspecific customisation with:


* SD Installer: A simple application for easy software additions.
  
* Apptainer and Podman: For those with technical expertise, create customised containers for specialized software setups.

### Pre-installed software:





2. Customizing Your Workspace:

    SD Installer: Use this straightforward application for hassle-free software additions.
    Apptainers: Advanced users can craft customized containers externally and import them seamlessly into SD Desktop. This method offers intricate customization for specific research needs.

!!! Note
    If the list below is not clear or you need specific software to analyze your data, please don't hesitate to contact us at servicedesk@csc.fi (subject: Sensitive Data). We can support you in your Desktop customization. Moreover, we are working on developing our services to provide proprietary software. Follow our webpage for constant updates. 



| ### Pre-installed software: | ### Scientific Software |
| --------------------------- | ------------------------ |
| - CentOS7                   | - **Python 3.9.15**
| - Emacs                     |   - Packages:
| - htlib                     |     - tensorflow
| - LibreOffice               |     - nltk
| - miniconda                 |     - spacy
| - minimap2                  |     - scikit-learn
| - pigz                      |     - seaborn
| - pyro.ai                   |     - plotly
| - Python                    |     - bokeh
| - R + R studio              |     - pydot
| - samtools                  |     - xgboost
| - nextflow                  |     - lightgbm
| - golang                    |     - catboost
|                             |     - eli5
|                             |     - torch
|                             |     - keras
|                             |     - dist-keras
|                             |     - elephas
|                             |     - gensim
|                             |     - scrapy
|                             |     - beautifulsoup4
|                             |     - numpy
|                             |     - scipy
|                             |     - pandas
|                             |     - statsmodels
|                             |     - matplotlib
|                             |     - pyfuse3
|                             |     - crypt4gh
|                             |     - trio
|                             |     - httpx
|                             |     - qrcode
|                             |   - [Instructions for adding Python libraries](./tutorials/sd-pythonlibs.md)
|                             | - **R / RStudio Server**
|                             |   - Installation matching the `r-env-singularity/4.0.5` module on Puhti











### Pre-installed software:


* CentOS7

* Emacs

* htlib

* LibreOffice

* miniconda

* minimap2

* pigz

* pyro.ai

* Python

* R + R studio

* samtools

* nextflow

* golang


 
### Scientific software 

   * Python 3.9.15 including following packages:
        
        * tensorflow nltk spacy scikit-learn seaborn plotly bokeh pydot xgboost lightgbm catboost eli5 torch keras dist-keras elephas gensim scrapy beautifulsoup4 numpy scipy pandas statsmodels matplotlib pyfuse3 crypt4gh trio httpx qrcode 
        * [Instructions for adding Python libraries](./tutorials/sd-pythonlibs.md)
        
   * R / RStudio Server

      * Installation matching the `r-env-singularity/4.0.5` module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12)
      * 1000+ pre-installed R packages (versions available on Apr 20 2021)
      * Intel® oneAPI Math Kernel Library (oneMKL)
      * GIS software (PROJ, GDAL, SAGA)
      * CUDA drivers 
      * TensorFlow (used with R TensorFlow back-end)
      * R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12) 
      * [Rstudio 4.2.2 and all CRAN and Bioconductor libraries can be added with SD-software-installer](./r-in-sd-desktop.md)

### SD Software installer

[SD Software installer](./tutorials/sd-software-installer.md) provides easy-to-use tool to add some commonly used software to SD Desktop.

### Software customisation with Apptainer and Podman

Users can install their own software to SD Desktop, but this requires technical expertise. As SD Desktop is isolated from the internet, you can't directly use installation tools like _git_, _coda_, _cpan_ or _pip_ as they are dependent on internet connections to external repositories. Further, SD Desktop users can't do any operation that needs superuser access.

If you want to add new software to your virtual machine independently, the most convenient way to add new software to your SD Desktop is to build a Apptainer container outside SD Desktop and then import the container through SD Connect to SD Desktop. The two documents below describe two sample cases on adding software with containers.

   1. [Importing ready-made software containers from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creating you own Singularity container and importing it to SD Desktop](./creating_containers.md)


!!! Note
    Please don't hesitate to contact us at servicedesk@csc.fi (subject: Sensitive Data). We can support you in your Desktop customization. 

In Ubuntu22 based virtual machines you can use also Podman container manager. One of the benefits of Podman is that can utilize Docker containers too.

*   [Using Podman in SD Desktop](./tutorials/podman-in-sd-desktop.md)
