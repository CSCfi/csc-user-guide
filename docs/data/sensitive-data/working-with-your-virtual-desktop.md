# Working with your virtual Desktop

Once your virtual Desktop is launched, each CSC project member can securely access it from their browser at any time.

When you log in to SD Desktop **Homepage**, you will be able to access your virtual Desktop in:

* **Recent connections**, by clicking on the image of your Desktop (visible only if you have recently accessed it)
* **All connections**, if you click on the "+"-icon you can see all the connections associated with each project (e.g. project_NNNNN_NNNN). You can access your virtual Desktop by clicking on the connection ID.

When you open the connection, a virtual computing environment will open into your browser. When you access the virtual Desktop for the first time, you will see a *getting started* panel, from which you can, for example, adjust the screen resolution.

You can work with this virtual Desktop like in a standard computing environment. From the *Applications* menu bar (top left corner) you can access several pre-installed programs. Examples include Open Office, image viewing applications, video and audio players, Jupiter Notebook etc. You can also open a terminal and use Linux from the command line. To start using R-Studio please check the following paragraph.

**Security-related features of the audited SD Desktop include:**

* the computing environment is **isolated from the internet**. You can, for example, open a Firefox web browser, but you are not able to access any site on the internet. You will also not be able to access any repositories directly.
* the copy-paste function from your computer/laptop to the virtual Desktop is entirely disabled for security reasons. You can anyhow use this function inside virtual Desktop.

**You can close your connection to your virtual Desktop in two ways:**

1. **Log out** from your Desktop (in the workspace view, top right corner of the browser, select your *username* and *log out*). This will close all applications in your virtual Desktop and disconnect the work session. You will be able to re-access the virtual Desktop at any time by logging in to the services.
2. If you started a data analysis programmatically (you are running a script) you can close the browser window. This doesn't interfere with the processes running. Thus, when you reconnect to your Desktop, you have all your tools and interfaces still open and can continue working. However, remember to log out from the Desktop once the analysis is finished. If you leave more than ten connections open, you will be unable to re-access the services.

!!! Note
    **Never use the lock or reboot buttons** in SD Desktop as you will not be able to connect to the Desktop again after that.

[![Access-virtual-Desktop](images/desktop/desktop-access.png)](images/desktop/desktop-access.png)


## Accessing data using Data Gateway

Once you sign in to your virtual Desktop, you can access the data by following these steps:

1. Open **Data Gateway** (you can find the application on your desktop);
2. Select **SD Apply**;
3. Click on **Continue**;
4. In the new window, under the second step, click on **Create**. The application will create a new folder called **Projects** accessible from your Desktop or programmatically through the terminal.
5. Click on **Open folder**.
6. The files have been encrypted using the sensitive data public encryption key, and you will be able to access their content in *read-only mode*. The current streaming speed can be up to 50 MB/s.

!!! Note
    The Projects folder is **available only when the Data Gateway application is open**. If you close or disconnect the application, you will not be able to access the data stored in the data service unless you previously made a full copy of it inside your Desktop. Thus, Data Gateway needs to be open and connected during data processing.

[![Desktop-register-access](images/desktop/desktop-register-gateway.png)](images/desktop/desktop-register-gateway.png)

## If you need to edit files/data

 * Access the files of interest in the *Project*-folder using **Data Gateway**;
 * Select all the necessary files from the *Project*-folder, make a **copy** and save it in the virtual Desktop's **home directory** (the files will be visible only from your browser) or in the **shared folder** (in this case, the files will be accessible also by the other CSC project members).

[![Desktop-data-import](images/desktop/desktop-gateway-import.png)](images/desktop/desktop-gateway-import.png)


## Default programs available on the Desktop and software customisation

Each virtual Desktop is pre-built and contains a limited set of default open-source software (listed below). The virtual Desktop is isolated from the internet and **importing of software is restricted**, as required by the data permit authority. Thus, users cannot directly import software/scripts or other files on to their virtual Desktop when working with secondary use data. 

If you need a specific program that is not pre-installed, it is recommended to contact us at servicedesk@csc.fi, **before applying for the data permit**. This way, we can figure out if it is possible to customise your virtual Desktop. If the program is compatible with the computing environment, you need to specify in your permit application the list of additional software, which will be provided directly by Findata.

### Pre-installed software:

* CentOS7 (Operating system)
* Emacs (Text editor)
* htLib (A library)
* LibreOffice (An open-source alternative to Microsoft Office)
* miniconda (Installer for conda, a bootstrap version of Anaconda)
* minimap2 (A sequence alignment program)
* pigz (A compression tool for files)
* pyro.ai (A tool for deep probabilistic modeling)
* Python
* R + R studio
* SAMtools (Programs for interacting with high-throughput sequencing data)
* nextflow (A workflow orchestrator)
* Go (Programming language)

### Scientific software

**Python 3.7.9** including following packages:

 * Beautiful Soup, Bokeh, CatBoost, crypt4gh, Distributed Keras, Elephas, ELI5, Gensim, HTTPX, Keras, LightGBM, Matplotlib, NLTK, NumPy, pandas, Plotly, pydot, pyfuse3, PyTorch, QRcode, Scikit-learn, SciPy, Scrapy, Seaborn, spaCy, Statsmodels, TensorFlow, Trio, XGBoost.

**R / RStudio Server** with the following properties:

 * Installation matching the `r-env-singularity/4.0.5` module on Puhti (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12)
 * 1000+ pre-installed R packages
 * Intel® oneAPI Math Kernel Library (oneMKL)
 * GIS software (PROJ, GDAL, SAGA)
 * CUDA drivers
 * TensorFlow (used with R TensorFlow back-end)
 * R + RStudio Server versions matched with Puhti r-env-singularity module (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)

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

**The import of data and software is restricted in SD Desktop**. You cannot import any data or software yourself for security reasons. If you are working with a dataset for which you have received a permit from Findata, the only way to access the data for analysis is by utilizing a specific application called **Data Gateway**. 

**Data export from SD Desktop is also restricted**. Only *non-sensitive* results can be exported from the workspace, and those can only be exported by the CSC project manager. Instructions for exporting your results are provided in the next paragraph.

Encrypted files will be **visible in read-only mode**. This solution allows you to process large amounts of data without storing any copy on your virtual Desktop. However, this means that the files cannot be edited in SD Desktop.

Lastly, we are not yet providing a virtual Desktop with Windows operating system, or with GPUs. However, we are working on it, and you can find more information on the future developments of the services on our webpage.
