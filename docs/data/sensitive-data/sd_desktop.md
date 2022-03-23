
# SD Desktop (Sensitive Data Desktop)


SD Desktop is a web-user interface that allows you to manage (start, use, delete) a virtual computer (here called Desktop) from your web browser. No previous knowledge of cloud computing is required to use the service. SD Desktop is designed to process sensitive data and provide a secure workspace for collaborative research projects. 
In the following user guide you can learn how to:

* apply for service access;
* set up your virtual Desktop;
* analyze data stored in SD Connect;
* re-use published data stored under controlled access,
* export non sensitive results from the secure virtual Desktop.

## Key features

* **Accessible from any operating system (Mac, Linux or Windows)** via web-browser (e.g., Google Chrome, Firefox) **from the public internet** (without the need of installing client or using a VPN);

* service access requires a CSC account and a CSC project;

* after login to SD Desktop, the user can **start a pre-built computing environment (Linux OS)**, on-demand; available options offer the capability of doing **simple statistical analysis to machine learning**;

* **limited set of pre-installed software (open source)**. Additional **customization** possible writing at servicedesk@csc.fi (subject: Sensitive data);

* process any type of data: text files, images, audio files, video, and genetic data;

* secure and **isolated workspace**, accessible to all the members of the same CSC proejct;

* **process a large amount of data** stored encrypted in SD Connect via data streaming (default disk space 280 GB, if additional space required contact servicedesk@csc.fi (subject: Sensitive data).



## Before you start

* Independently of the login method used, you need a **CSC username and password to access or import encrypted data* * into your virtual Desktop. If you don't remember it, check how to reset it at [Account: How to change password](../../accounts/how-to-change-password.md)


* **All the members belonging to a specific CSC project can access the same computing virtual Desktop.** Currently, it is possible to **launch 3 virtual Desktops (or computing enviroment) for each CSC project**. Each CSC project has its own private Desktop, and **each Desktop is isolated from other CSC projects or CSC accounts unless you authorize it**.

* The project manager's or group leader's responsibility is to frequently review the list of members belonging to a project in MyCSC and verify who can access the data present in the project using SD Desktop or SD Connect. Remove the project members who do not need access to the data when their contribution is no longer needed.  

* SD Connect and SD Desktop have not yet been security audited. Because of that, users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by Findata.




## Overview

![SD Desktop](https://user-images.githubusercontent.com/83574067/155133488-ab99aa45-cff8-4531-9542-d34ae944fc58.png)


## Service access 

To access SD Desktop go to [MyCSC](https://my.csc.fi) and:

* set up [a CSC account](../../accounts/how-to-create-new-user-account.md);
* [join](../../accounts/how-to-add-members-to-project.md) or set up [a CSC project](../../accounts/how-to-create-new-project.md);
* fill in the [description of data processing activities](../../accounts/when-your-project-handles-personal-data.md) form;
* add [service access to SD Connect and SD Desktop](../../accounts/how-to-add-service-access-for-project.md);
* activate [multi-factor authentication](../../accounts/mfa.md) on your account.

For specific guidance regarding these steps or appling for resources for your CSC proejct (e.g billing units or disk quota) check the [Accounts](../../accounts/index.md) paragraph at the beginning of CSC user guide.



## Authentication

<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/VebHTUonOSs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Login to SD Desktop is possible with identity federation systems (Haka, Virtu and [Elixir Login](https://elixir-europe.org/register) or with  CSC Login at:

[**https://sd-desktop.csc.fi**](https://sd-desktop.csc.fi),

using any modern web browser (e.g. Google Chrome, Firefox). 

After login, **verify your identity** by entering the verification **code** provided via the mobile application. For specific guidance regarding the verification step, check the [multi-factor authentication](../../accounts/mfa.md) paragraph at the beginning of CSC user guide.



![Authentication](images/desktop/desktop-login-1.png)


## Setting up a virtual Desktop
  
<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/VebHTUonOSs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Once you have access to the service, you can launch your virtual computer (Desktop), choosing between four pre-built options. This operation can be carried out with a few simple steps and does not require any technical knowledge. Next, the services will start your virtual Desktop (or, in technical terms: launch a virtual machine) and create a secure connection between CSC and your browser. After launch, your virtual Desktop will be directly available for use every time you log in to the service. Moreover, the running Desktop will consume billing units (or resources) from your CSC project until the Desktop is deleted. 

Each Desktop is CSC project-specific and supports the launch of **3 virtual Desktops**. In addition, each Desktop supports the simultaneous connection of **10 project members**.
Thus, if you add colleagues/collaborators as project members in the same CSC project, they will also be able to connect to a virtual Desktop and access the data stored in your project. Furthermore, all the Desktop are provided with the same software (pre-installed and managed by CSC). The complete and updated list can be found in the following paragraph: [Pre-installed list of software](./pre-installed_software.md).

 
To start your Desktop, in SD Desktop Connection page, click on **Go To SD Desktop Management** page:

* **select your CSC project**, 

* **choose the operating system** (currently the only possible operating system  is Linux CentOS 7);
  
* optionally, you can  assign a specific name to the Desktop;
  
* optionally, you can extend your Desktop's disk space (or storage capability) by clicking on **add an external disk**. You can add up to 200 GB. The default disk space is 80 GB. Note: you can extend the disk space only before launching the Desktop. Additional disk space can be required writing at servicedesk@csc.fi (subject: Sensitive data);

* **select** the preferred computing environment (based on your needs) and click on **Launch Desktop**. The operation is entirely automated and can take **up to 30 minutes**. If you try to access the virtual Desktop and see a black screen, come back later. 



![Launch-virtual-Desktop](images/desktop/desktop-2.png)



In SD Desktop, you can choose between **four different pre-built options **:  

*  **Light computation**: this option is ideal for testing the services (for example, test how to start a Desktop, check out how it looks, try to access data stored in SD Connect). You can compare this Desktop to a  laptop with limited capacities, which probably freezes when you open too much software or more than three colleagues connect to it simultaneously. For this reason, we advise you to start this type of Desktop only for testing purposes and delete it when the testing is completed. Techincal specifications: **Core:3; memory 4 GiB; Root: 80 GB; Correspondent Pouta Flavour: standar.medium; Billing Units: 1.3 units/h**.

* **Small computation**: this option is ideal for analyzing sensitive data using office software (for example: similar to simple statistical analysis with Excel, watching videos, listening to audio files, working on text files). You can compare this Desktop to your working laptop. Techincal specifications: **Core:6; memory 15 GiB; Root: 80 GB; Correspondent Pouta Flavour: standar.xlarge; Billing Units: 5.2 units/h**.

* **Medium computation**: this option is ideal for running complex statistical or genome analysis (for example: use the command line to run specific scripts). You can compare this Desktop to a powerful laptop provided by your IT unit. Techincal specifications:**Core:8; memory 30 GiB; Root: 80 GB; Correspondent Pouta Flavour: standar.xxlarge; Billing Units: 10.4 units/h**.

* **Heavy computation**: this option is ideal for running non-interactive programmatic analysis (for example, machine learning). Technical specifications: **Core:8; memory 168 GiB; Root: 80 GB; Correspondent Pouta Flavour: hpc4.4core; Billing Units: 78 units/h**. Please do not choose the Heavy computation option for simple computing or analysis, as it consumes many resources. 



![Launch-virtual-Desktop](images/desktop/desktop-3.png)


!!! Note
        If you don't know the best Desktop option for your needs, please contact us at servicedesk@csc.fi (email subject: Sensitive Data). 


Unfortunately, we are not yet providing a virtual Desktop with GPUs or Windows, Linux Ubuntu operating systems. However, we are working on it, and you can find more information on the future developments of the services on our webpage. 

In the following paragraphs, we will discuss how to work with a Desktop, which software is available and how it is possible to customize your workspace. 



## Working with your virtual Desktop

Once your private virtual computer (Desktop) is launched, each CSC project member can securely connect to from their browser, at any time.

When you log in to SD Desktop **Homepage**,  you will be able to access your private Desktop in:

* **Recent connections**, clicking on the image of your Desktop (visible only if you recently accessed the virtual Desktop)

* **All connections** if you click on + you can see all the connections associated with each project (e.g. project_NNNNN_NNNN). If you click on the connection ID you will also access your Desktop. 



![Access-virtual-Desktop](images/desktop/desktop-4.png)


These are the main working space features:

* the computing environment (visible from your browser) is isolated from the internet;

* the copy-paste function from your computer/laptop to the browser visualizing your virtual Desktop is entirely disabled for security reasons;

* when you access the virtual Desktop for the first time, you will be able to see the setting board. From here, you can, for example, adjust the screen resolution;


* from the menu bar (top left corner), you can use several pre-installed software: for example, Open Office, audio, video, images,  Jupiter Notebook. Ru studio.(Complete list below);

* if you plan to work with other colleagues on the same files, save them in the **Shared-directory**. The files can be open, chaned, edited by all the members of the same CSC project;

* you can access or import data in the vistual Desktop using the Data Gateway applciation (see below for more information);

* as previously mentioned, you can **log out** from your computing environment at any moment (in the workspace view, top right corner of the browser, select your username and log out). Logging out will disconnect the work session. You will always be able to reaccess your Desktop after logging in to the SD Desktop service. 

!!! Note
    **Never use the lock or reboot buttons** in SD Desktop as you will not be able to connect to the Desktop again after that.
 
    
iframe width="280" height="155"![Launch-virtual-Desktop](images/desktop/desktop-6.png)
     
![Launch-virtual-Desktop](images/desktop/desktop-6.png)
  
  

## Accessing encrypted sensitive data within SD Desktop


As the virtual Desktop is isolated from the Internet, the only way to access data for analysis is utilizing a specific application called Data Gateway.
This application will allow you to access encrypted data stored in SD Connect or a specific dataset for which you have been granted access via SD Apply for re-use.
Encrypted files will be **visible in read-only mode (similarly to opening a pdf file or streaming a YouTube video)**. This solution allows you to process large amounts of data without storing any copy on your virtual Desktop. 


!!! Note
    In SD Desktop, you  can access only files encrypted with the Sensitive Data Services encryption key or using SD Connect. If you try to access unencrypted data or files encrypted only with your public encryption key, this will result in an error. If you experience any problem with Desktops launched before March 2022, don't hesitate to contact us at servicedesk@csc.fi (subject: sensitive data). 
   
### Accessing encrypted data stored in SD Connect using Data Gateway

Once you sign in to your virtual Desktop, you can access encrypted data stored in SD Connect by following these steps:

* Open **Data Gateway** (you can find the application on your Desktop);

* select SD Connect;

* add your **CSC credentials** (username and password. Note: we disabled the copy/paste options for security reasons; thus, you need to type in your password);

* **Click on Login** and next clic on **Continue**;

[![Data-Gateway-1](images/desktop/data-gateway-1.png)]

[![Data-Gateway-2](images/desktop/data-gateway-2.png )]


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
    Your private workspace in SD Desktop is completely isolated from the Internet for security reasons. If you need to visualize or import specific scripts into your Desktop (for example, from GitHub or other trusted repositories), you can use the procedure described above.



## Available software provided on SD Desktop

 Currently, each virtual Desktop (or virtual computer) is pre-built and contains a limited set of pre-installed open source software (listed below). 

Users are allowed to install their own user level software to SD Desktop, but this requires techincal experties. As SD Desktop is isolated from internet you can't use istallation tools like _git_, _coda_, _cpan_ or _pip_ that are depended on internet connections to external repositories. Further, SD Desktop users can't do any opeartion that need superuser access.

Often the most covienient way to add new software to your SD Desktop is to build a Singularity container outside SD Desktop and then import the Singularity ilmage through SD Connect to SD Desktop. The two documents below describe two sample cases on adding software with containers

   1. [Importing ready made software containers from a public repository to SD Desktop](./sd-desktop-singularity.md)
   2. [Creating you own Singularity contaner and importing it to SD Desktop](./creating_containers.md)


!!! Note
    If the list below is not clear of if you need a specific software for anlyzing your data, please don't esitate to contact us at servicedesk@csc.fi (subject: Sensitive Data). We can support you in your Desktop customization. Morevere, we are working on the development of our services to provide also prorpietary software. Follow our future developments webpage for constant updates. 
    
   

**Pre-installed software**:



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


 
 
## RStudio in SD Desktop

To access RStudio in SD Desktop open the terminal in your virtual Desktop and launch RStudio with:

```text
start-rstudio-server
```

This will return a URL and a service specific password:

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
* after a few seconds, you can input the username and password (service specific) and access the server.

!!! Note
    Also when using RStudio, you need to save your data in **Shared-directory** if your colleagues need to work on the same files.


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">
![RStudio Final](https://user-images.githubusercontent.com/83574067/122616050-4f597f00-d092-11eb-9e6f-1984572d8a63.png)
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">



## Deleting your computing environment
  
At the end of your research or your analysis, you can delete your Desktop and all the data in it. 

In SD Desktop Homepage click on **Go to the launching page**. Here, in **Available instances** click on **Delete Desktop**. 


!!! note
    All the data present in the computing environment will be deleted and it will not be possible to retrieve them.

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">

![Screeshot_SDDesktop_0109_deletingvm](https://user-images.githubusercontent.com/83574067/131730561-12a229e7-b4d8-4c9d-868a-718f5014271d.png)

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">


##  Data export from SD Desktop

For security reasons, your Desktop is isolated from the internet and it is not possible to export data from the virtual computing environment. 

For more information write to servicedesk@csc.fi (email subject SD Desktop)

## Troubleshooting

| Problem               |                                                                                                                                    | Possible solution                                                                                                                                                                                                                                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access                | Launched a new Desktop, but now the screen is balck/freezed.                                                                       | The creation of a new Desktop can take up to 30 minutes. Come back later.                                                                                                                                                                                                                                                        |
|                       | Cannot login to SD Desktop                                                                                                         | Create a CSC account and a project in the MyCSC portal. Add service access for Allas (a CSC storage solution) and SD Desktop to your project.                                                                                                                                                                                    |
|                       | Cannot turn off my Desktop.                                                                                                        | You can log out from Desktop at any moment (in the workspace view, top right corner of the browser, select your username and log out). You will always be able to access your Desktop again after logging in. Never use the lock or reboot buttons in SD Desktop as after that you will not be able to connect the desktop again |
| Collaborative project | My collaborator added me to their CSC project, but I cannot access SD Desktop.                                                     | Accept the terms of use and add service access for SD Desktop in the MyCSC portal.                                                                                                                                                                                                                                               |
|                       | Me and my colleague are members of the same CSC project. I cannot see the data they have analysed/edited  in our private Desktop.  | Save the files in the Shared directory, if you need to work on/edit files or datasets with your colleagues.                                                                                                                                                                                                                      |
|                       | Cannot add more project members to the same Desktop.                                                                               | Your Desktop has too many simultaneous connections. Max 10 users can use the same Desktop at the same time. Furthermore, each individual user can have only one active connection to one Desktop. Remember to log out of the Desktop to end the active session.                                                                  |
| Copy- Paste Function  | I cannot copy and paste my password or commands from outside the Desktop.                                                          | We disabled the copy/paste options for security reasons, thus you need to type in everything manually. Alternatively, you can import documents or scripts to SD Connect and do the copy-paste process inside SD Desktop.                                                                                                         |
| Data export           | Cannot export results.                                                                                                             | Currently, a user can not export any data out from the SD Desktop for security reasons. We are implementing a feature to SD Desktop for data export later this year. Check our webpage for more information.                                                                                                                     |
| Data Import           | The SD Connect Downloader client doesn’t work when I add my credentials.                                                           | Use the username and password of your CSC account. Check that your project has service access for Allas (a CSC storage solution). Check that you haven’t changed your environment variables. Do not use passwords that contain @                                                                                                 |
|                       | I imported data from SD Connect with the Downloader client but the data isn't decrypted.                                           | If you want the data to be automatically decrypted in SD Desktop, you need to encrypt the files with a CSC Sensitive Data Services public key.                                                                                                                                                                                   |
|                       | Need to import more than 80 GB of data. I already have an extra volume.                                                            | SD Connect Downloader client saves a copy of the data in SDCONNECTDATA folder (which has a disk space limit of 80 GB). You can make a link to the added volume from your terminal: `ls -s /path_to_volume_mount_point ~/SDCONNECTDATA`                                                                                           |
| Disk space/ Volume    | Cannot add disk space to my Desktop.                                                                                               | It’s possible to add disk space only when you are launching a new Desktop.                                                                                                                                                                                                                                                       |
|                       | Cannot make a copy of a big dataset.                                                                                               | Check that you have enough disk space on your Desktop. The maximum disk space of each Desktop is 280 GB.                                                                                                                                                                                                                         |
| Mac OS                | Mac keyboard is not recognized e.g. command+C is not translated to CTRL+C.                                                         | You need to change the keyboard settings.                                                                                                                                                                                                                                                                                        |
| Software              | Cannot open RStudio on my Desktop.                                                                                                 | To access RStudio in SD Desktop, you need to open the terminal in your virtual Desktop and launch RStudio with start-rstudio-server.Check for more instructions above inthe user guide.                                                                                                                                          |
|                       | Need a software not provided in Desktop                                                                                            | Contact us at servicedesk@csc.fi (subject SD Desktop)                                                                                                                                                                                                                                                                            |









[![Service-access](images/desktop/try-smaller2.png)](images/desktop/try-smaller.png) [![Service-access](images/desktop/try-smaller2.png)](images/desktop/try-smaller.png)


[![Service-access](images/desktop/try-smaller-combined.png)](images/desktop/try-larger-combined.png) 



Deprecated:
## Importing encrypted sensitive data to SD Desktop 

The SD Connect Downloader application will be available only till December 2021.
  
<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/3UQLfYABP7A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> 

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595580-5b811480-d071-11eb-9b99-9dcad8b4ac17.png">


Once you are logged in into your SD Desktop **you can import encrypted sensitive data stored in SD Connect**.

!!! Note
    **If you use the CSC Sensitive Data Service public encryption key to encrypt the data, the files are  automatically decrypted**.  If you use your own key pair to encrypt the data, the application will make a copy and you need to manually decrypt them using Crypt4GH CLI. 

To import the data:

* **Open SD Connect Downloader client** (you can find the link to the application on your Desktop)

* insert your **CSC credentials** (username and password. Note: we disabled the copy/paste options for security reasons, thus you need to type in your password)

* select your CSC project

* select the correct bucket 

* select the files you want to import 

* click on **download objects** (the application will make a copy of the encrypted files in SD Desktop).

* click on **open download location**

The files are downloaded to a directory called SDCONNECTDATA which is in the user's home directory. The folder is automatically opened by Open Download Location.

Note: **If you used CSC Sensitive Data Service public encryption key to encrypt the data, the files are automatically decrypted **. 

If you used your own key pair to encrypt the data, the application will make a copy and you need to manuallay decrypt them using Crypt4GH CLI. 

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">
<img width="960" alt="SD Desktop 5" src="https://user-images.githubusercontent.com/83574067/121872988-9223fb80-cd0e-11eb-8c5b-7e19a2111407.png">
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">

For security reasons, your private workspace in SD Desktop is **completely isolated from the Internet**. If you need to import specific scripts in SD Desktop (for example from GitHub or other trusted repositories) you need to use the same procedure described before:

* download your scripts from GitHub and save them in a specific bucket in SD Connect

* access SD Desktop and use the SD Connect Downloader to make a copy of the scripts







