
## Default programs available on SD Desktop

Each virtual desktop (or virtual computer) is pre-built and contains a limited set of default open-source software (listed below). Additionally, you can find step-by-step guidance below on customizing your virtual desktop using the [SD Software installer](./tutorials/sd-software-installer.md), an easy-to-use tool that allows you to add commonly used software. It is also possible to customize the virtual desktop with Apptainer and Podman (advanced).

!!! Note
If the list below is unclear, or if you need specific software to analyze your data that is not yet available in this user guide, please do not hesitate to contact us at servicedesk@csc.fi (subject: Sensitive Data). We can assist you in customizing your virtual desktop.


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

### Accessing RStudio 

Open the terminal and launch RStudio with:

```text
start-rstudio-server
```

This will return a URL and a service-specific password:

```
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

Next:

* paste the URL in Firefox 
* after a few seconds, you can input the username and password (service-specific) and access the server.

!!! Note
    Only file saved in shared-directory or external volume are accessible to other project memebers using RSudio.


[![Desktop-rstudio](images/desktop/desktop-rstudio.png)](images/desktop/desktop-rstudio.png)



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
    
