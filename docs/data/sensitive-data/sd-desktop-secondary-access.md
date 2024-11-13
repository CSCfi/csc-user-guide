# Working with your virtual desktop

Once your virtual Desktop is launched, each CSC project member can securely access it from their browser at any time.

## Access virtual desktop

After log in, you will see all your virtual desktops listed at the front page, under *All connections*. 

* **All connections**. Select project (e.g. `project_NNNNN`) and click the plus-sign. There you can see all desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name.
* **Recent connections**. Your recently used virtual desktops appear also here.

![check the paragraph below](../sensitive-data/images/desktop/SD-Desktop-Frontpage.png)


When you open the connection, a virtual computing environment will open in your browser. If you are accessing the virtual desktop for the first time, you will see the panel getting started, from which you can, for example, adjust the screen resolution.

**You can work with your virtual desktop like with a standard computer**, accessing several pre-installed programs from the applications menu bar (top left corner). Examples include Open Office, image-viewing applications, video and audio players, Jupyter Notebooks etc. You can also open a terminal and use Linux from the command line. For more information on accessing R-Studio, please [check the paragraph below](#rstudio-on-sd-desktop).

### Security-related features of the audited SD Desktop include:

* The computing environment is **isolated from the internet**. You can, for example, open a Firefox web browser, but you are not able to access any site on the internet. You will also not be able to access any repositories directly.

* The copy-paste function from your computer/laptop to your virtual desktop is limited for security reasons. [Instructions how to copy-paste](#copy-paste-from-your-laptop-to-virtual-desktop).

### You can close your connection to your virtual Desktop in two ways:

1. **Log out** from your Desktop (in the workspace view, top right corner of the browser, select your *username* and *log out*). This will close all applications in your virtual Desktop and disconnect the work session. You will be able to re-access the virtual Desktop at any time by logging in to the services.

2. **Reconnecting to an analysis session**:

2.1 Closing the browser window: If you have started the analysis programmatically (e.g., by running a script), you can safely close the browser window without interrupting the ongoing processes. Your tools and interfaces will remain open when you reconnect to your desktop, allowing you to continue working.
      
2.2 Reconnecting to an old session: You can reconnect to a previous session only if the browser window is exactly the same size as when the original session was in use. This is typically only possible if you're using the SD Desktop in full-screen mode on the same machine. If the window size has changed, you will most likely be unable to reconnect to the old session.

!!! Note
    **Never use the lock or reboot buttons** in SD Desktop as you will not be able to connect to the Desktop again after that.

[![Access-virtual-Desktop](images/desktop/desktop-access.png)](images/desktop/desktop-access.png)


## Accessing data using Data Gateway

The virtual desktop is isolated from the internet, so data access must be done through the Data Gateway application. This application allows you to import data from SD Apply. Imported data is saved on the virtual desktop’s external volume for secure analysis.

### Prerequisites

* **What is an external volume?** Your virtual desktop’s local storage is limited, so it’s recommended to save large data files and collaborative work on the external volume. This volume acts like an external hard drive that can be detached and reattached to different desktops, allowing project members to share and edit files stored there.
* **Adding the external volume:** the external volume can only be added when creating a [new virtual desktop](../sensitive-data/sd-desktop-create.md)
* **Additional volume space:** if you need additional volume space (more than 200 GB), you can request it by writing to CSC Service Desk, (subject: SD Desktop), **please be aware that volume extensions are only possible before any data has been added to the volume**.

### Step 1: Open Data Gateway

Once you sign in to your virtual Desktop, you can access the data by following these steps:

1. Open **Data Gateway** (you can find the application on your desktop);
2. Select **SD Apply**;
3. Click on **Continue**;
4. In the new window, under the second step, click on **Create**. The application will create a new folder called **Projects** accessible from your Desktop or programmatically through the terminal.
5. Click on **Open folder**.
6. The files have been encrypted using the sensitive data public encryption key, and you will be able to access their content in *read-only mode*. The current streaming speed can be up to 50 MB/s.

!!! Note
    The _Projects_ folder is **available only when the Data Gateway application is open**. If you close or disconnect the application, you will not be able to access the data stored in the data service unless you previously made a full copy of it inside your Desktop. Thus, Data Gateway needs to be open and connected during data processing.

[![Desktop-register-access](images/desktop/desktop-register-gateway.png)](images/desktop/desktop-register-gateway.png)


### Step 2: import a copy of the files on your virtual desktop's volume

1. Keep Data Gateway connection open: select and copy the files or folders from the Projects folder.
2. Paste them into the external volume within your virtual desktop, located on the left side menu.
3. Files or folders will automatically decrypt during the copy process and become available for analysis.

[![Desktop-data-import](images/desktop/desktop-gateway-import.png)](images/desktop/desktop-gateway-import.png)

### Step 4: setting permissions for shared access

After copying files to the external volume, adjust permissions to enable access for other project members. By default, permissions are limited to your access only, so these steps ensure that others can view and edit the data.

1. **Adjust folder permissions**:
    * Right-click the folder on the external volume, select Properties, and open the Permissions tab.
    * Set permissions to Create and Delete Files for each user to allow full access.
  
2. **Adjust file permissions**:
    * For individual files, right-click each file, select Properties, and change permissions to Read and Write.
    * For folders, set permissions to Create and Delete Files so they remain accessible when the volume is reattached to a different virtual desktop.

Once permissions are set, your files are ready for collaborative work, and all project members with access can view and analyze them.

### Step 5: close the Data Gateway application

You can now disconnect the Data Gateway connection if no further data accessor import are needed.

!!! Note
    If more than 10 data gateway connection are left open, the data gateway will stop working. In this case, [contact CSC Service Desk](../../support/contact.md) (subject: SD Desktop).


[![Desktop-data-import](images/desktop/desktop-gateway-import.png)](images/desktop/desktop-gateway-import.png)


### Copy-paste from your laptop to virtual desktop

The copy-paste function from your computer/laptop to your virtual desktop is limited for security reasons. However it is possible to copy-paste text with Clipboard:

* Copy text normally from your computer (Cntrl+C).
* Go to virtual desktop and open a Clipboard with a key combination **Cntrl+Alt+Shift**.
* Paste your text to the Clipboard.
* Copy the text again from the Clipboard. Please note that the Cntrl+C won't work here, use the mouse right-click instead.
* Now you can paste the text inside your virtual desktop.
* When you are ready, close the Clipboard with **Cntrl+Alt+Shift**.

![SD Desktop Clipboard screenshot](images/desktop/SD-Desktop-Clipboard.png)

## Default programs available on the Desktop and software customisation

Each virtual Desktop is pre-built and contains a limited set of default open-source software (listed below). The virtual Desktop is isolated from the internet and **importing of software is restricted**, as required by the data permit authority. Thus, users cannot directly import software/scripts or other files on to their virtual Desktop when working with secondary use data. 

If you need a specific program that is not pre-installed, it is recommended to [contact CSC Service Desk](../../support/contact.md) **before applying for the data permit**. This way, we can figure out if it is possible to customise your virtual desktop. 

**You can work with your virtual desktop like with a standard computer**, accessing several pre-installed programs from the applications menu bar (top left corner). Examples include Open Office, image-viewing applications, video and audio players, Jupyter Notebooks etc. You can also open a terminal and use Linux from the command line. For more information on accessing R-Studio, please [check the paragraph below](#accessing-rstudio).

Below we list some of the most commonly used tools that are by default installed in the virtual desktop. The list is not complete and there are small differences between different desktop options.

| **Category**              | **Software**                                                                                                                                                                       |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Office Tools**          | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                         |
| **Programming**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md) including packages: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R & RStudio**           | [R / RStudio Server](sd-desktop-working.md#accessing-rstudio) <br> - Matching the r-env-singularity/4.0.5 module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - 1000+ pre-installed R packages (versions available on Apr 20, 2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - GIS software (PROJ, GDAL, SAGA) <br> - CUDA drivers <br> - TensorFlow (used with R TensorFlow back-end) <br> - R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)                 |
| **Workflow Engines**      | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                                                                                                |
| **Software Containers**    | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (Only in Ubuntu machines)                                                                                                                             |
| **Scientific Software**    | - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                                                                                                                          |
| **Terminals & Interfaces** | - [Byobu](https://www.byobu.org/) (Only in Ubuntu machines.) <br> - [Jupyter](https://jupyter.org/)                                                                                                                         |


### RStudio on SD Desktop

To access RStudio on SD Desktop, open the terminal from the *Applications* tab in your virtual Desktop and launch RStudio with:

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

 * **paste** the URL in Firefox
 * after a few seconds, you can **input the username and password** (given by the terminal) and access the server.

!!! Note
    When using RStudio, you need to save your data in **shared-directory** if your colleagues need to access the same files.


[![Desktop-rstudio](images/desktop/desktop-rstudio.png)](images/desktop/desktop-rstudio.png)


## Limitations to SD Desktop

To comply with the regulation, SD Desktop for secondary use is **completely isolated from the internet and other services**. You can, for example, open a Firefox web browser, but you are not able to access any site on the internet.

**The import of data and software is restricted in SD Desktop**. You cannot import any data or software yourself for security reasons. If you are working with a dataset for which you have received a permit from a data controller, the only way to access the data for analysis is by utilizing a specific application called **Data Gateway**. 

**Data export from SD Desktop is also restricted**. Only *non-sensitive* results can be exported from the workspace, and those can only be exported by the CSC project manager. Instructions for exporting your results are provided in the next paragraph.

Encrypted files will be **visible in read-only mode**. This solution allows you to process large amounts of data without storing any copy on your virtual Desktop. However, this means that the files cannot be edited in SD Desktop.

Lastly, we are not yet providing a virtual Desktop with Windows operating system or with GPUs. However, we are working on it, and you can find more information on the future developments of the services on our webpage.
