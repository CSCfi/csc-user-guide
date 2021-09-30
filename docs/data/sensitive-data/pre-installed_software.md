# Using application software in SD Desktop. 

SD Desktop provides a Remote Desktop view to a Virtual Machine running at an isolated could environment at CSC. The virtual machie contains a limited set of pre-installed software (listed below).

Users are allowed to install their own user level software to SD Desktop, but this can be quite difficult. As SD Desktop is isolated from internet you can't use istallation tools like _git_, _coda_, _cpan_ or _pip_ that are depended on internet connections to external repositories. Further, SD Desktop users can't do any opeartion that need superuser access.

Oftten the most covienient way to add new software to your SD Desktop is to build a Singularity container outside SD Desktop and then import the Singularity ilmage through SD Connect to SD Desktop. The two documents below describe two sample cases on adding software with containers

   1. [Imporing ready made software containders from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creaing you own Singularity contaner and importing that to SD Desktop](./creating_containers.md)

## Pre-installed software in Sensitive Data Desktop (SD Desktop)

The following software are pre-installed on each computing environment (or VM flavour) accessible from SD Desktop.
  
### Operating system and general purpose tools

   * Centos 7 linx with an extended set of system libraries
   * GNOME desktop
   * Java (Open JDK 1.8.)
   * gcc 4.8-5
   * Singularity 3.7.3 
   * Go 1.16 
   * Libreoffice  7.1
   * Firefox
 
## Scientific software 

   * Python 3.7.9 including following packages:      
        * tensorflow nltk spacy scikit-learn seaborn plotly bokeh pydot xgboost lightgbm catboost eli5 torch keras dist-keras elephas gensim scrapy beautifulsoup4 numpy scipy pandas statsmodels matplotlib pyfuse3 crypt4gh trio httpx qrcode 
   * R / RStudio Server

      * Installation matching the `r-env-singularity/4.0.5` module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12)
      * 1000+ pre-installed R packages (versions available on Apr 20 2021)
      * Intel® oneAPI Math Kernel Library (oneMKL)
      * GIS software (PROJ, GDAL, SAGA)
      * CUDA drivers 
      * TensorFlow (used with R TensorFlow back-end)

      * R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12) 
   * GIS software (PROJ, GDAL, SAGA) 
   * CUDA drivers 
   * TensorFlow (used with R TensorFlow back-end) 

