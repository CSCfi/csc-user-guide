
# SD Desktop (Sensitive Data Desktop)


## Before you start

* Independently of the login method used, you need a **CSC username and password to import data** into your Desktop computing environment. If you don't remember it, check how to reset it at [Account: How to change password](../../accounts/how-to-change-password.md)


* **All the project members belonging to a specific CSC project can access the same computing environment in SD Desktop.** Currently, it is possible to **launch 3 Desktops (or workspaces) for each CSC project**. Each CSC project has its own virtual private computing environment and **each computing environment is isolated from other CSC projects or CSC accounts, unless you authorize it**.

* It is the project manager's or group leader's responsibility to review frequently the list of members belonging to a project in MyCSC and verify who can access the data present in the project using SD Desktop or SD Connect. Remove the project members that do not need to have access to the data when their contribution is no longer needed.  

* SD Connect and SD Desktop have not yet been security audited. Because of that, users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by Findata.


## Login 


<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/VebHTUonOSs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595830-ab5fdb80-d071-11eb-8eee-d90db85aa7ad.png">


To access SD Desktop you need:

* **a CSC account**

* **a CSC project**

* **Service access to SD Desktop.**


To import (or download) encrypted sensitive data to SD Desktop you need:

* **service access to Allas** (CSC cloud storage solution).
  

Login to SD Desktop is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https:/sd-desktop.csc.fi using any modern web browser.

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595830-ab5fdb80-d071-11eb-8eee-d90db85aa7ad.png">

<img width="960" alt="sd-desktop-0" src="https://user-images.githubusercontent.com/83574067/122118478-bbd54380-ce30-11eb-95cc-589e6cb68a84.png">



## Launching your Desktop (or private computing environment)
  
<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/VebHTUonOSs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

  
After launch, you can login into your Desktop from any modern internet browser. Each Desktop will be accessible all along the duration of your CSC project.

Each Desktop is CSC project specific. Thus, if you add colleagues/collaborators as project members in the same CSC project, they will be able to access the same Desktop. To edit the same files or datasets, you need to save them in the same *shared folder*.

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122592729-5b7f1580-d06d-11eb-8913-9219c864954b.png">
![SD-Desktop-1final](https://user-images.githubusercontent.com/83574067/122592168-a0567c80-d06c-11eb-97f3-0c19675cd7e6.png)
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122592746-6174f680-d06d-11eb-8d9b-6315c9766b46.png">


To launch your Desktop, in Homepage, click on **Go To Launching Page** :

* **select your CSC project**

* **choose the operating system** (for beta versions, only possible operating system is Linux CentOS 7)
  
* optionally, you can name the Desktop (**update: 1 September 2021**).
  
* optionally, you can extend the disk space clicking on **add an external disk**. You can add up to 200 GB. The default disk space is 80 GB. Note: you can extend the disk space only before launching the Desktop (**update: 1 September 2021**).

* **select** the preferred computing environment (based on your needs) and click on **Launch Desktop**

The system will create a secure connection to your private computing environment. The process is completely automated and might take **up to 30 minutes**. 

In SD Desktop (Open Beta) you can choose between **four different Desktops **:  

|Desktop |Core|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Correspondent Flavour|Example usage|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|
|Light computation |3|4 |80 |standard.medium |testing the service |1.3|
|Small computation |6|15|80 |standard.xlarge |office software|5.2|
|Medium computation|8|30|80 |standard.xxlarge |running statistical or genome analysis |10.4|
|Heavy computation |8|168|80 |hpc4.40core|non-interactive programmatic computation|78|


If you are not sure what is the best option for your needs/research, contact us at servicedesk@csc.fi (email subject: SD Desktop). Do not choose the Heavy computation option for simple computing or analysis, as it consumes a large amount of resources.

All the Desktop are provided with the same software. The complete and updated list can be found in the following paragraph: [Pre-installed list of software](./pre-installed_software.md).


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122593105-db0ce480-d06d-11eb-8a42-aab26cf289b8.png">
  
![Screenshot_SD_Desktop_0109_launchingpage](https://user-images.githubusercontent.com/83574067/131730263-374e5188-a7ee-4e03-a890-e7112745e2e3.png)

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122593108-dcd6a800-d06d-11eb-9b51-2faaf2937b3a.png">



If the launch is successful, when you return to SD Desktop **Homepage**,  you will be able to access the computing environment from:

* **Recent connections**, clicking on the image of your Desktop

* **All connections** if you click on + you can see all the connections associated with each project (e.g. project_NNNNN_NNNN). If you click on the connection ID you will also be able to access your computing environment. 


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">
![SD-Desktop-Connection](https://user-images.githubusercontent.com/83574067/122604935-66db3c80-d07f-11eb-8364-df60b0e71699.png)
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595580-5b811480-d071-11eb-9b99-9dcad8b4ac17.png">


In the Desktop you will be able to access different applications from the menu bar on the page top left corner (e.g. Open Office, Jupter Notebook ).
If you need to work on files or datasets with your colleagues, save them in the **Shared-directory**. The file will be visible and accessible to all the members of the same CSC project. 

As previously mentioned, you can **logout** from your computing environment at any moment (in the workspace view, top right corner of the browser, select your username and log out). Logging out will disconnect the work session. You will always be able to access your Desktop again after logging in. **Never use the lock or reboot buttons** in SD Desktop as after that you will not be able to connect to the Desktop again.


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">

 ![Screeshoot_SDDesktop_0109_wrokspace](https://user-images.githubusercontent.com/83574067/131730403-3e96b440-9750-4bda-a5ef-7703d0d9c3ee.png)

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595580-5b811480-d071-11eb-9b99-9dcad8b4ac17.png">



## Importing encrypted sensitive data to SD Desktop
  
  

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





  
