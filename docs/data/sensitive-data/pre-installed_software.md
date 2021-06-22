# Using application software in SD Desktop. 

SD Desktop provides a Remote Desktop view to a Virtual Machine running at an isolated could environment at CSC. The virtual machie contains a limited set of pre-installed software (listed below).

Users are allowed to install their own user level software to SD Desktop, but this can be quite difficult. As SD Desktop is isolated from internet you can't use istallation tools like _git_, _coda_, _cpan_ or _pip_ that are depended on internet connections to external repositories. Further, SD Desktop users can't do any opeartion that need superuser access.

In practice the only reasonable way to add your own software to your SD Desktop is to build a Singularity container outside SD Desktop and then import the Singularity ilmage through SD Connect to SD Desktop.


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
      * R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12) 
   * GIS software (PROJ, GDAL, SAGA) 
   * CUDA drivers 
   * TensorFlow (used with R TensorFlow back-end) 
   * samtools 1.10 
   * bcftools 1.10.2 
   * htslib 1.10.2 
   * unix2dos 
   * dos2unix 
   * md5sum 
   * plink (1.9) 
   * prettify (plink) 
   * plink2 (2.0)






















