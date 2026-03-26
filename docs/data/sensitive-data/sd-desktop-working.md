[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Working with your Desktop: tips and essentials

## Prerequisites
* [Create virtual desktop](sd-desktop-create.md)
* [Access virtual desktop](sd-desktop-access-vm.md)

## Work and collaborate in a virtual desktop

Once a virtual desktop has been created, all members of your CSC project can access it. When you log in, you will enter a virtual computer running on a Linux operating system. If you are new to Linux, it might feel a little different from other systems like Windows or macOS.

No technical experience is required to work with it, but while Windows is designed to be user-friendly from the start, Linux can have a learning curve, especially if you need to use the command line. 

The guide below provides clear instructions to help you get comfortable with both Linux and the SD Desktop’s security setup:

- [Security-related features and limitations](sd-desktop-working.md#security-related-features-and-limitations)
- [Introduction to Linux and virtual desktop](sd-desktop-working.md#introduction-to-linux-and-virtual-desktop)
- [Copy-paste from your laptop to virtual desktop](sd-desktop-working.md#copy-paste-from-your-laptop-to-virtual-desktop)
- [Default software available in SD Desktop](sd-desktop-working.md#default-software-available-in-sd-desktop)



## Introduction to Linux and virtual desktop

Linux is an open-source operating system, meaning it is free to use, and its code is openly available for people to view and modify. It's commonly used in many research applications due to its stability, security, and flexibility.

- **Look and feel**: Linux may look slightly different from Windows, depending on the “desktop environment” used. But don’t worry – it still has familiar elements like windows folders and menus. You will find the main menu at the top left corner, where you can access all available software.
  
- **File structure**: Instead of “My Documents” or drives labeled C: or D:, Linux has a different way of organising files. The main directory starts with /, and you’ll see folders like /home for your personal files.
  
- **Benefits**: Linux is very stable and less likely to crash, making it ideal for long or intensive computing tasks.


## Storage locations in SD Desktop (Important!)

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/r0S1NNN2eQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

When you log in to SD Desktop (Ubuntu), you will see several storage locations or folders on the desktop's navigation bar:

- **Home** or **File folder** is your personal directory inside the virtual desktop and works like the internal disk of a laptop. It is only accessible to you, otehr projectm memebrs cannot access it. It is intended only for temporary files and small working materials, and it will be lost if you updated virtual desktop and storing data there might cause the virtual destop disk to get full and the vrtual desktop to get stuck and no loner accessible.

- **Volume**: 

-   **Data Gateway application**: You can also makage impiort and export from the virtual desltop. it is an application that helps you access the data stored on SD Apply (for Secondary Use proejct type) or SD Connect (CSC Academic porject type). Via this applciation you can copy the dataset insude the virtual desktop voluem for analsysis, the applicaiton will creatde a decryped copy of it. 
-
-
-   , on the other hand, is your project’s encrypted external volume. It is detachable from the virtual machine, automatically mounted when you start SD Desktop, and designed for all long‑term and original research data. This volume is persistent across updates and shared with other members of your project.
-
-
- Shared-directory, is provided for transferring data between SD Desktop and other Sensitive Data services; it is not intended for long‑term storage.


Below is an image showing the basic functions of a virtual desktop. Click the image to open it in a new window.

[![Virtual desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png)](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png){ target="_blank" }



## Copy-paste from your laptop to virtual desktop

The copy-paste function from your computer/laptop to your virtual desktop is limited for security reasons. However it is possible to copy-paste text with Clipboard. Copy-paste works only in one direction: from your computer to virtual desktop.

### Step by step

1. Open the virtual desktop and press **Ctrl + Alt + Shift** to open the **Clipboard panel.** 
2. Select **Text input** to enable copy-paste. Clipboard panel will close automatically. Do not close the Clipboard panel with Ctrl + Alt + Shift, as this may disable copy-paste.
3. You can now copy text from your computer (**Ctrl + C or right-click)** and paste it in the virtual desktop (**Ctrl + V or right click**). 

!!! Note
    You need to enable the copy-paste function each time you start a virtual desktop session.


![SD Desktop Clipboard screenshot](images/desktop/SD-Desktop-Clipboard.png)  
*Appearance of the Clipboard (Guacamole tools) may vary a bit depending on browser and local operating system.*

## Default software available in SD Desktop

**You can work with your virtual desktop like with a standard computer**, accessing several pre-installed programs from the applications menu bar (top left corner). Examples include Open Office, image-viewing applications, video and audio players, Jupyter Notebooks etc. You can also open a terminal and use Linux from the command line. 

Below we list some of the most commonly used tools that are by default installed in the virtual desktop. The list is not complete and there are small differences between different desktop options. 


If you want to install software that is not included by default (for example, RStudio), you can use the SD-Software Installer. This simple application provides a list of additional software and guides you through the installation process, no technical expertise required. To learn how, please follow the next guide: [Customisation - software & tools](./sd-desktop-software.md) For more advanced users, it's also possible to install other tools using containerized applications with Aptainer or Podman.



| **Category**              | **Software**                                                                                                                                                                       |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Office Tools**          | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                         |
| **Programming**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md) including packages: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R & RStudio**           | [R / RStudio Server](sd-desktop-working.md#accessing-rstudio-from-virtual-desktop) <br> - Matching the r-env-singularity/4.0.5 module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - 1000+ pre-installed R packages (versions available on Apr 20, 2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - GIS software (PROJ, GDAL, SAGA) <br> - CUDA drivers <br> - TensorFlow (used with R TensorFlow back-end) <br> - R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)                 |
| **Workflow Engines**      | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                                                                                                |
| **Software Containers**    | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (Only in Ubuntu machines)                                                                                                                             |
| **Scientific Software**    | - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                                                                                                                          |
| **Terminals & Interfaces** | - [Byobu](https://www.byobu.org/) (Only in Ubuntu machines.) <br> - [Jupyter](https://jupyter.org/)                                                                                                                         |

## Accessing RStudio from virtual desktop

For a step by step guide, see: [Installing RStudio via SD-Software Installer](r-in-sd-desktop.md) No technical expertise required.


## Your next steps in this guide

* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)

