
# SD Desktop (Sensitive Data Desktop)

SD Desktop is a web-user interface that allows you to manage (start, use, delete) a virtual computer (here called Desktop, technically defined as vitual machine) from your web browser. No previous knowledge of cloud computing or programming expertise are required to use the service. SD Desktop is designed to process sensitive data and provide a secure workspace for collaborative research projects.

In the following user guide, you can learn how to:

* apply for service access;
* set up your virtual Desktop;
* analyze data stored in SD Connect;
* re-use published data stored under controlled access,
* export non-sensitive results from the secure virtual Desktop.

## Key features

* Accessible from any operating system (Mac, Linux or Windows) via web-browser (e.g., Google Chrome, Firefox) from the public internet (without the need of installing a client or using a VPN).

* Only the memerbs of the same CSC project can access the same virtual Desktop.

* After login to SD Desktop, the user can start a pre-built computing environment (Linux OS), on-demand; available options offer the capability of doing simple statistical analysis to machine learning.

* Virtual Desktops are not connected to internet: the only way to import and export data is SD Connect service;

* SD Desktop can be used to work with any type of data: text files, images, audio files, video, and genetic data. However the virtual Desktop include a limited set of pre-installed software (open source). Additional tools can be imported through SD Connect and additional customization is possible writing at servicedesk@csc.fi (subject: Sensitive data);

* **Process a large amount of data** stored encrypted in SD Connect via data streaming (default disk space 280 GB, if additional space required contact servicedesk@csc.fi (subject: Sensitive data) or via SD Apply (for data re-use).



## Before you start

* All the members belonging to a specific CSC project can access the same computing virtual Desktop. Currently, it is possible to launch 3 virtual Desktops (or computing environment) for each CSC project. Each CSC project has its private Desktop, and each Desktop is isolated from other CSC projects or CSC accounts unless you authorize it.

* The project manager's or group leader's responsibility is to frequently review the list of members belonging to a project in MyCSC and verify who can access SD Desktop or SD Connect. Remove the project members who do not need access to the data when their contribution is no longer needed.

* SD Connect and SD Desktop have not yet been security audited. Because of that, users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by Findata.

## Overview

![Desktop-overview](images/desktop/desktop-overview.png)


## Service access 

Access to SD Desktop is based on CSC user accounts and projects. If you don't have CSC account and project you need to:

* set up [a CSC account](../../accounts/how-to-create-new-user-account.md);
* [join](../../accounts/how-to-add-members-to-project.md) or set up [a CSC project](../../accounts/how-to-create-new-project.md);
* fill in the [description of data processing activities](../../accounts/when-your-project-handles-personal-data.md) form;
* add [service access to Allas and SD Desktop](../../accounts/how-to-add-service-access-for-project.md).

For specific guidance regarding these steps or applying for resources for your CSC project (e.g, billing units or disk quota), check the [Accounts](../../accounts/index.md) paragraph at the beginning of this user guide. Note that you always need to use your CSC username and password when you access data stored in SD Connect from yoru virtual Desktop. If you don't remember your CSC password, you can [reset it](../../accounts/how-to-change-password.md).  

### Authentication

<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/VebHTUonOSs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Login to SD Desktop is possible with identity federation systems (Haka, Virtu and [Elixir Login](https://elixir-europe.org/register) or with CSC Login at:

[**https://sd-desktop.csc.fi**](https://sd-desktop.csc.fi)

from any modern web-browser.


### Setting up a virtual Desktop
  
<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/VebHTUonOSs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Once you have access to the service, you can launch your virtual computer (Desktop), choosing between four pre-built options. This operation can be carried out with a few simple steps and does not require any technical experties. Next, the services will start your virtual Desktop (or, in technical terms: launch a virtual machine) and create a secure connection between CSC and your browser. After launch, your virtual Desktop will be directly available for use every time you log in to the service. Moreover, the running Desktop will consume billing units (or resources) from your CSC project until it is deleted.

Each CSC project supports the launch of 3 virtual Desktops. In addition, each Desktop supports the simultaneous connection of 10 project members. Thus, if you add colleagues/collaborators as project members in the same CSC project, they will also be able to connect to a virtual Desktop and access the data stored in your project. Furthermore, all the Desktop are provided with the same software (pre-installed and managed by CSC). The complete and updated list can be found in the following paragraph.


To start your virtual Desktop, log in to the services and in **Connection** page, click on **Go To SD Desktop Management page**. 

Here you can specify several parametes:

* **Select your CSC project**.

* **Choose the operating system**. Currently the only possible operating system is Linux CentOS 7 but in the future there will be other options too.

* **Assign a name for your virtual Desktop**. It is good practice to assign a descriptive name for a Desktop so that all project members can easily identify it later on.

* Choose one of the **virtual Desktop** pre-built options (Light, Small, Medium or Heavy computing), based on your computing and memory needs. The default disk (or storage) space for all Desktop is 80 GB. You can extend your Desktop disk space by selecting option: **add an external disk**. You can add up to 200 GB. Note: you can't extend the disk space after you have lauched the virtual Desktop. Additional disk space later on can be required writing at servicedesk@csc.fi (subject: Sensitive data);

When all the settings are done, press the **Launch Desktop** button. The launch operation is entirely automated and can take **up to 30 minutes**. If you try to access the virtual Desktop and see a black screen, come back later. 


![Launch-virtual-Desktop](images/desktop/desktop-2.png)


You can choose between **four different pre-built virtual Desktop options **:


*  **Light computation**. Techincal specifications: **Core:3; memory 4 GiB; Root disk: 80 GB; Correspondent Pouta Flavour: standard.medium; Billing Units: 1.3 units/h**. This option is ideal for testing the services (for example, test how to start a Desktop, check out how it looks, try to access data stored in SD Connect, delete the Desktop). You can compare this Desktop to a laptop with limited capacities, which probably freezes when you open too much software or more than three colleagues connect to it simultaneously. For this reason, we advise you to start this type of Desktop only for testing purposes and delete it when the testing is completed. 

* **Small computation**. Techincal specifications: **Core:6; memory 15 GiB; Root disk: 80 GB; Correspondent Pouta Flavour: standar.xlarge; Billing Units: 5.2 units/h**. This option is ideal for analysing sensitive data using office software (for example: similar to simple statistical analysis with Excel, watching videos, listening to audio files, working on text files). You can compare this Desktop to your working laptop. 

* **Medium computation**. Techincal specifications:**Core:8; memory 30 GiB; Root disk: 80 GB; Correspondent Pouta Flavour: standar.xxlarge; Billing Units: 10.4 units/h**. This option is ideal for running complex statistical or genome analysis (for example: use the command line to run specific scripts). You can compare this Desktop to a powerful laptop provided by your IT unit. 

* **Heavy computation**: Technical specifications: **Core:40; memory 168 GiB; Root disk: 80 GB; Correspondent Pouta Flavour: hpc4.40core; Billing Units: 78 units/h**. This option is ideal for running non-interactive programmatic analysis (for example, machine learning) that require heavy computation. Please do not choose this option for simple analysis, as it consumes much resources. 


![Launch-virtual-Desktop](images/desktop/desktop-3.png)


!!! Note
        If you don't know the best Desktop option for your needs, please contact us at servicedesk@csc.fi (email subject: Sensitive Data). 


Unfortunately, we are not yet providing a virtual Desktop with GPUs or Windows, Linux Ubuntu operating systems. However, we are working on it, and you can find more information on the future developments of the services on our webpage. 

In the following paragraphs, we will discuss how to work with a virtual Desktop, which software is available and how it is possible to customise your workspace.




### Working with your virtual Desktop

Once your private virtual computer (Desktop) is launched, each CSC project member can securely access it from their browser at any time.

When you log in to SD Desktop **Homepage**,  you will be able to access your virtual Desktop in:

* **Recent connections**, clicking on the image of your Desktop (visible only if you recently accessed it)

* **All connections** if you click on + you can see all the connections associated with each project (e.g. project_NNNNN_NNNN). If you click on the connection ID you will also access your Desktop. 



![Access-virtual-Desktop](images/desktop/desktop-4.png)


When you open the connection, a virtual computing environment (Linux Centos operating system) will open into your browser. When you access the virtual Desktop for the first time, you will see the getting started panel, from which you can, for example, adjust the screen resolution.

You can work with this virtual Desktop like in a standard computing environment.  From the applications menu bar (top left corner) you can access several pre-installed programs. Examples include Open Office, image viewing applications, video and audio players, Jupiter Notebook etc. You can also open a terminal and use Linux from command line. To start using R-Studio please check the paragraph below.


Security-related features SD Desktop include:

* the computing environment (visible from your browser) is isolated from the internet. You can, for example, open a Firefox web browser, but you are not able to access any site on the internet. At this moment, you will also not be able to access any repositories directly.

* you can access or import data only data stored in SD Connect using the Data Gateway application (see below for more information);

* the copy-paste function from your computer/laptop to the browser visualizing your virtual Desktop is entirely disabled for security reasons. You can anyhow use this function inside your browser.


You can close your connection to your virtual Desktop in two ways:

1.  _Log out_ from your Desktop (in the workspace view, top right corner of the browser, select your _username_ and _log out_). This will close all applications in your virtual Desktop and disconnect the work session. You will be able to access the virtual Desktop at any time after logging in to the services.

2. If you started a data analysis programmatically (you are running a script) you can close the browser window. This doesn't interfere with the processes running. Thus, when you reconnect to your Desktop, you have all your tools and interfaces still open and can continue working. However, remember to log out from the Desktop once the analysis is finished. If you leave more than ten connections open, you will be unable to re-access the services. 


!!! Note
    **Never use the lock or reboot buttons** in SD Desktop as you will not be able to connect to the Desktop again after that.
 
    
![Launch-virtual-Desktop](images/desktop/desktop-5.png)
     

### RStudio in SD Desktop

To access RStudio in SD Desktop, open the terminal in your virtual Desktop and launch RStudio with:

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
    Also when using RStudio, you need to save your data in **Shared-directory** if your colleagues need to work on the same files.


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">
![RStudio Final](https://user-images.githubusercontent.com/83574067/122616050-4f597f00-d092-11eb-9e6f-1984572d8a63.png)
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">


## Accessing encrypted sensitive data within SD Desktop

As the virtual Desktop is isolated from the internet, the only way to access data for analysis is by utilizing a specific application called _Data Gateway_.
This application will allow you to access encrypted data stored in SD Connect or a specific dataset for which you have been granted access via SD Apply for re-use.
Encrypted files will be **visible in read-only mode (similarly to opening a pdf file or streaming a YouTube video)**. This solution allows you to process large amounts of data without storing any copy on your virtual Desktop. 

!!! Note
    In SD Desktop, you can access only files encrypted with the Sensitive Data Services encryption key or using SD Connect. If you try to access unencrypted data or files encrypted only with your public encryption key, this will result in an error. If you experience any problem with Desktops launched before March 2022, don't hesitate to contact us at servicedesk@csc.fi (subject: sensitive data). 
   
### Accessing encrypted data stored in SD Connect using Data Gateway

Once you sign in to your virtual Desktop, you can access encrypted data stored in SD Connect by following these steps:

* Open **Data Gateway** (you can find the application on your Desktop);

* select SD Connect;

* add your **CSC credentials** (username and password. Note: we disabled the copy/paste options for security reasons; thus, you need to type in your password);

* **Click on Login** and next click on **Continue**;

![Data-Gateway-1](images/desktop/data-gateway-1.png)

![Data-Gateway-2](images/desktop/data-gateway-2.png )


* In the new window, at the end of the page, click on **create Data Gateway**. The application will create a new folder called **Projects** accessible from your Desktop or programmatically the terminal. Next, click on **Open folder**.

![Data-Getewa-3y](https://user-images.githubusercontent.com/83574067/158682331-183db935-3380-4e30-84c8-1f91508da9e8.png)

![Data-Gateway-4](https://user-images.githubusercontent.com/83574067/158682773-68e05a99-95dc-435e-a643-de8af5021f6f.png)


*   If the files have been encrypted using SD Connect or the **sensitive data public encryption key**, you will be able to access their content in read-only mode. The current streaming speed can be up to 50 MB/s. 

![Data-Gateway-5](https://user-images.githubusercontent.com/83574067/158682863-a82bdffa-0e3c-4888-a11e-15f32d4841dc.png)

![Data-Gateway-6](https://user-images.githubusercontent.com/83574067/158682916-0db649e9-6bf1-4ed4-930f-8a4c93e1a93e.png)


!!! Note 
    The Projects folder is **available only when the Data Gateway application is open**. If you sign out from the application, you will not access the data stored in other Sensitive Data services unless you previously made a full copy of it inside your Desktop. Thus, Data Gateway needs to be open during data processing in streaming mode.


### Importing data inside the Desktop

**If you need to edit the files/data**:

 * access the files of interest in the Project folder **using Data Gateway**;
 
 *  Select all the necessary files from the Project folder, make a **copy** and save it in the virtual Desktop **home directory** (the files will be visible only from your browser) or in the **shared folder** (in this case, the files will be accessible also by all the CSC project members). 

 
!!! Note
    Your private workspace in SD Desktop is completely isolated from the internet for security reasons. However, you can use the procedure described above if you need to visualize or import specific scripts into your Desktop (for example, from GitHub or other trusted repositories).

###  Accessing published data for re-use via SD Apply


Data Gateway can also be used to access data published under controlled access via other CSC services for sensitive data. To access a specific dataset in your virtual Desktop, you need first to apply for it using SD Apply service. When the data owner (or Data Access Committee) has granted you access, you will be able to access the dataset in SD Desktop for a limited time.

<img width="960" alt="Screenshot 2022-03-16 222235" src="https://user-images.githubusercontent.com/83574067/158684026-959e7b8d-d910-4a77-919a-414c8623b8ec.png">

If you did not yet apply for access to a specific dataset or if the access period has ended and you try to access the data using the Data gateway application, you will encounter an error message. 

<img width="960" alt="10" src="https://user-images.githubusercontent.com/83574067/158683211-3a390e9e-f576-4a2b-8638-07c399c1b4fe.png">


SD Apply is currently in the pilot phase. Please contact us at servidesk@csc.fi (subject: sensitive data) for more information.


## Default programs available on SD Desktop

Each virtual Desktop (or virtual computer) is pre-built and contains a limited set of default open-source software (listed below). 

!!! Note
    If the list below is not clear or you need specific software to analyze your data, please don't hesitate to contact us at servicedesk@csc.fi (subject: Sensitive Data). We can support you in your Desktop customization. Moreover, we are working on developing our services to provide proprietary software. Follow our webpage for constant updates. 


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


### Software customisation

Users can install their user-level software to SD Desktop, but this requires technical expertise. As SD Desktop is isolated from the internet, you can't use installation tools like _git_, _coda_, _cpan_ or _pip_ dependent on internet connections to external repositories. Further, SD Desktop users can't do any operation that needs superuser access.

The most convenient way to add new software to your SD Desktop is to build a Singularity container outside SD Desktop and then import the Singularity image through SD Connect to SD Desktop. The two documents below describe two sample cases on adding software with containers.

   1. [Importing ready-made software containers from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creating you own Singularity container and importing it to SD Desktop](./creating_containers.md)


!!! Note
    Please don't hesitate to contact us at servicedesk@csc.fi (subject: Sensitive Data). We can support you in your Desktop customization. 

##  Data export from SD Desktop

Your virtual Desktop is isolated from the internet for security reasons. Only the CSC project manager can export results or data from the secure workspace using the airlock application, currently available only programmatically. Note: all the files exported from the virtual Desktop need to be encrypted. 

Below you can find step-by-step instructions to encrypt and export data from SD Desktop to SD Connect, where you can download and decrypt it. 

![Data-export](images/desktop/airlock.png)

**1- Generate your encryption key pair** (secret key and public key) with the Crypt4GH application (you can skip this paragraph if you already have a key pair).

* Install the Crypt4GH application:

CSC has developed a simple application that will allow you to generate your encryption keys and decrypt data when necessary. 
Download the version specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases):  

  - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.2.0/crypt4gh-gui-python3.8-linux-amd64.zip)
   - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.2.0/crypt4gh-gui-python3.8-macos-amd64.zip)
   - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.2.0/crypt4gh-gui-python3.8-windows-amd64.zip)

Please check that the tool for Windows has been digitally signed by CSC - IT Center for Science. After the download, you can find the Crypt4GH application in your downloads folder.

* When you open the application for the first time, you might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and then click on _Run anyway_.

* Generate your encryption keys:

- Open the Crypt4GH application and click on _Generate Keys_ (on the top right corner).
- The tool will open a new window and ask you to insert a password (_Private Key Passphrase_). This password will be associated with your secret key. Please, use a strong password.
- When you click on _OK_, the tool will generate a key pair consisting of a secret key (your username_crypt4gh.key) and a public key (your username_crypt4gh.pub).
- The keys/file names will be displayed in the Activity Log with the following message:

```
Key pair has been generated, your private key will be auto-loaded the next time you launch this tool:
Private key: username_crypt4gh.key
Public key: username_crypt4gh.pub
All the fields must be filled before file encryption will be started
```

The keys will be generated and saved to the same folder in which the application resides.

!!! Note
    * If you lose or forget your secret key, or the password, you will be unable to decrypt the files.
    * Do not share your secret key or your password.
    * You need to **create your keys only once** and use them for all your encryption needs, but you can of course, choose to generate separate keys for encryption as you wish.


**2- Upload the public key to SD Connect**. 

* You can easely upload the public key to SD Connect via drag and drop. You will be **redirected to a new window displaying the default encryption options**. 

* Next, you can specify the bucket's name to which the public encryption key should be uploaded. If you don't fill in a specific term, the user interface will automatically create a bucket named with a 13 digit number (based on creation time). 

* Click on **Encrypt and upload**: the public key will be encrypted and uploaded to the bucket in SD Connect. Only encrypted files are visible and accessible via SD Desktop; thus, even your public encryption key must be encrypted during upload.

<img width="960" alt="export" src="https://user-images.githubusercontent.com/83574067/160693019-e0bafc69-7bc6-4cb4-bca4-37db0e124b63.png">



**3- Import the public key inside the Desktop**.

Once the upload process is completed, you can access your virtual Desktop. Using the Data Gateway application, access the bucket with the public key. You can now import a copy of your public key inside the virtual Desktop (via copy/paste function). 


**4- Encrypt the restuls**.

Open the terminal (right click) and encrypt with your public key the files you want to export. Crypt4GH is already installed on each Desktop and accessible programmatically. 

The syntax of the encryption command is:

```text
crypt4gh encrypt --recipient_pk public-key < input > output
```

Where public-key is your public key (username.pub), input is the file you want to export (my_results.csv), and output is the encrypted file (my_results.csv.c4gh)

For example:

```text
crypt4gh encrypt --recipient_pk your-username.pub < my_results.csv > my_results.csv.c4gh
```

**5- Exporting the results from the private Deskotp**.

Once the file is encrypted, only the CSC project manager can export the encrypted files.

From the terminal type the following syntax:

```text
airlock-client-vX.X  <<username>> <<data_output_bucket>> <<filename>>
```

Where *username* is your CSC account username, *data_output_bukcet* is the name that you want to give to the bucket into which the results are exported. The airlock client will generate the bucket automatically, in the same CSC project in which your Desktop is. *Filename* is the name of the encrypted files that you want to export.

For example:

```text
airlock-client-vX.X  cscuser  analysis-2022  results-03.csv.c4gh
```

Press enter and add your CSC account password. Note: if you try to upload an unencrypted file, the airlock client will automatically encrypt it with the Sensitive Data public key for security reasons and export it to SD Connect. Here, you will be able to download the file but you will not be able to decrypt it.

7- The exported file is now available in SD Connect/Allas. After downloading the file in your local environment, you can decrypt it with your secret encryption key, using the Crypt4GH application or programmatically. For specific guidance check the following [paragraph](./sd_connect.md#data-download-and-decryption).
For more information and support, write to servicedesk@csc.fi (email subject SD Desktop)



## Deleting your virtual Desktop
  
At the end of your analysis, you can delete your virtual Desktop and all the files in it.

You can not undo this action:
  
* On SD Desktop Homepage, click on **Go To SD Desktop Management page**. 
* Here, under **Available instances** click on **Delete Desktop**. 


!!! note
    All the data present in the computing environment will be deleted, and it will not be possible to retrieve them. You will delete the entire virtual workspace,       and your colleagues (or the other CCS project members) will lose their results and data imported to it. For this reason, please get in touch with all the           project members and export all the results of your analysis from the virtual workspace, before deleting a virtual Desktop.

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">

![Screeshot_SDDesktop_0109_deletingvm](https://user-images.githubusercontent.com/83574067/131730561-12a229e7-b4d8-4c9d-868a-718f5014271d.png)
s
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">




## Troubleshooting

| Problem               |                                                                                                                                    | Possible solution                                                                                                                                                                                                                                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access                | Launched a new Desktop, but now the screen is black/frozen.                                                                       | The creation of a new Desktop can take up to 30 minutes. Come back later.                                                                                                                                                                                                                                                        |
|                       | Cannot log in to SD Desktop                                                                                                         | Create a CSC account and a project in the MyCSC portal. Add service access for Allas (a CSC storage solution) and SD Desktop to your project.                                                                                                                                                                                    |
|                       | Cannot turn off my Desktop.                                                                                                        | You can log out from Desktop at any moment (in the workspace view, top right corner of the browser, select your username and log out). You will always be able to reaccess your Desktop after logging in. Never use the lock or reboot buttons in SD Desktop as after that, you will not be able to connect the Desktop again |
| Collaborative project | My collaborator added me to their CSC project, but I cannot access SD Desktop.                                                     | Accept the terms of use and add service access for SD Desktop in the MyCSC portal.                                                                                                                                                                                                                                               |
|                       | Me and my colleague are members of the same CSC project. I cannot see the data they have analysed/edited in our private Desktop.  | Save the files in the Shared directory if you need to work on/edit files or datasets with your colleagues.                                                                                                                                                                                                                      |
|                       | Cannot add more project members to the same Desktop.                                                                               | Your Desktop has too many simultaneous connections. Max 10 users can use the same Desktop at the same time. Furthermore, each user can have only one active connection to one Desktop. Remember to log out of the Desktop to end the active session.                                                                  |
| Copy- Paste Function  | I cannot copy and paste my password or commands from outside the Desktop.                                                          | We disabled the copy/paste options for security reasons. Thus you need to type in everything manually. Alternatively, you can import documents or scripts to SD Connect and do the copy-paste process inside SD Desktop.                                                                                                         |
| Data export           | Cannot export results.                                                                                                             | Only the CSC project manager can export encrypted results from the SD Desktop for security reasons.                                                                                                                  |
| Data Access           | The Data Gateway application doesn’t work when I add my credentials.                                                           | Use the username and password of your CSC account. Check that your project has service access for Allas (a CSC storage solution). Check that you haven’t changed your environment variables. Do not use passwords that contain @                                                                                                 |
|                       | I imported data from SD Connect with the Data gateway application but the data isn't decrypted.                                           | If you want the data to be automatically decrypted in SD Desktop, you need to encrypt the files using also the CSC Sensitive Data Services public key.                                                                                                                                                                                   |
|                       | Need to import more than 80 GB of data. I already have an extra volume.                                                            | You can link the added volume from your terminal: `ls -s /path_to_volume_mount_point ~/SDCONNECTDATA`                                                                                           |
| Disk space/ Volume    | Cannot add disk space to my Desktop.                                                                                               | It’s possible to add disk space only when launching a new Desktop.                                                                                                                                                                                                                                                       |
|                       | Cannot make a copy of a big dataset.                                                                                               | Check that you have enough disk space on your Desktop. The maximum disk space of each Desktop is 280 GB, but it can be extended contacting servicedesk@csc.fi                                                                                                                                                                                                                        |
| Mac OS                | Mac keyboard is not recognized e.g. command+C is not translated to CTRL+C.                                                         | You need to change the keyboard settings.                                                                                                                                                                                                                                                                                        |
| Software              | Cannot open RStudio on my Desktop.                                                                                                 | To access RStudio in SD Desktop, you need to open the terminal in your virtual Desktop and launch RStudio with start-rstudio-server.Check for more instructions above in the user guide.                                                                                                                                          |
|                       | Need software not provided in Desktop                                                                                            | Contact us at servicedesk@csc.fi (subject SD Desktop)                                                                                                                                                                                                                                                                            |


