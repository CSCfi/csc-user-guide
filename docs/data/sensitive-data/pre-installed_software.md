
# List of pre-installed software in Sensitive Data Desktop (SD Desktop)

All the following software  are pre-installed on each computing enviroment (or VM flavour) accessible from SD Desktop.
  
# Basix Linux Desktop 

**Operating system: Centos 7 with GNOME desktop**

Pre-installed software: 

* Python 3.7.9 including following packages: 

tensorflow nltk spacy scikit-learn seaborn plotly bokeh pydot xgboost lightgbm catboost eli5 torch keras dist-keras elephas gensim scrapy beautifulsoup4 numpy scipy pandas statsmodels matplotlib pyfuse3 crypt4gh trio httpx qrcode 

* Go 1.16 
*	Libreoffice (currently being installed) 
 
# Scientific Analysis Desktop 

**R / RStudio Server Singularity container**

General concept: 

* R + RStudio Server versions matched with Puhti r-env-singularity module 
* First production version based on r-env-singularity/4.0.5 (R 4.0.5 + RStudio Server 1.4.1106, MRAN snapshot dating to xxxx, Bioconductor 3.12) 


Wider installations in container: 

* CentOS7 + long list of libraries 
* Python 
* 1000+ R packages (JH will add link to install script) 
* GIS software (PROJ, GDAL, SAGA) 
* CUDA drivers 
* TensorFlow (used with R TensorFlow back-end) 
* JH will add links to container recipe files 

Requirements from VM perspective: 

* Sif file in appropriate location (e.g. /opt/r-env-singularity/4.0.5) 
* Singularity 
* Browser (Firefox) 
* Launch scripts in /usr/bin (4 in total: single- and multi-threaded R / RStudio) 
* Many R packages assume / require web access to function properly, setting up connections will depend on user 
* Things JH ran on Anvil 
* Yum-installed Singularity + created folder in /opt 
* Downloaded sif + launch scripts from Allas, made scripts executables 
 
# Basic Windows Desktop 

**Operating system: Windows Server 2016**

Pre-installed-software: 
*Python 3.7.9 
* Go 1.16.2 
* Firefox web browser (no internet connectivity)  

# Genome Data Analysis Linux Desktop (to be build)  

**Operating system: Centos 7 with GNOME desktop**

Pre-installed software: 
* R + R Studio (same as Scientific Analysis Desktop)
* Python (same as Basic Linux Desktop) 
* samtools 1.10 
* bcftools 1.10.2 
* htslib 1.10.2 
* unix2dos 
* dos2unix 
* md5sum 
* plink (1.9) 
* prettify (plink) 
* plink2 (2.0) 

# Data:  
•	1000genomes mitokondrion vcf ja tbi hakemistossa /data 


Notes:
1) there are Juha's notes in the list
2) why mitocondrial data?
3) how do we explain to the user what they should use?
4) video/audio files?
5) Windows server? 
6) Are 2 customers included?



















