
# SD Desktop (Sensitive Data Desktop)


## Before you start

* Independently of the login method used, you need your **CSC username and password to import data** into your SD Desktop computing environment. If you don't remember it, check how to reset it at [Account: How to change password](https://docs.csc.fi/accounts/how-to-change-password/)

* **All the project members belonging to a specific CSC project can access the same computing environment in SD Desktop.** Currently, it is possible to **launch 3 Desktops (or workspaces) for each CSC project**. Each CSC project has its own virtual private computing environment and **each computing environment is isolated from other CSC projects or CSC accounts, unless you authorize it**.

* It is the project manager or group leader responsibility to review the list of members belonging to a project frequently in MyCSC and verify who can access the data present in the project using SD Desktop or SD Connect. Remove the project members that do not need to have access to the data when their contribution is no longer needed.  

* Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***


## Step1 : Login 

To access SD Desktop you need:

* **a CSC account**

* **a CSC project**

* **Service access to SD Desktop.**


To import (or download) encrypted sensitive data to SD Desktop you need:

* **service access to Allas** (CSC cloud storage solution).


Login to SD Desktop is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https:/sd-desktop.csc.fi using any modern web browser.

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595830-ab5fdb80-d071-11eb-8eee-d90db85aa7ad.png">

<img width="960" alt="sd-desktop-0" src="https://user-images.githubusercontent.com/83574067/122118478-bbd54380-ce30-11eb-95cc-589e6cb68a84.png">



## Step 2: Launching your Desktop (or private computing environment)

Once you login, in SD Desktop **Homepage** you can launch your private and secure cloud computing enviroment, accessible all along the duration of your project. 

After launch, you can login into your Desktop from your internet browser at any time. If you add colleagues/collaborats as project members in the same CSC project, they will be able to access the same secure computing environment. To access the same files or datasets, you need to save them in the same **shared folder** (read more below).


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122592729-5b7f1580-d06d-11eb-8913-9219c864954b.png">
![SD-Desktop-1final](https://user-images.githubusercontent.com/83574067/122592168-a0567c80-d06c-11eb-97f3-0c19675cd7e6.png)
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122592746-6174f680-d06d-11eb-8d9b-6315c9766b46.png">


To launch your Desktop, in Homepage, click on **Launching page** :

* **select your CSC project**

* **choose the operating system** (for beta versions, only possible operating system is Linux CentOS 7)

* **select** the preferred computing environment (based on your needs) and click on **Launch Desktop**

The system will create a secure connection to your private computing enviroment. The process is completely automated and might take **up to 30 minutes**. 

In SD Dekstop (Open Beta) you can choose between **four different Desktops **:  

|Desktop |Core|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Corrispondet Flavour|Example usage|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|
|Light computation |3|4 |80 |standard.medium |testing the service |1.3|
|Samll computation |6|15|80 |standard.xlarge |office software|5.2|
|Medium computation|8|30|80 |standard.xxlarge |running statistical or genome alaysis |10.4|
|Heavy computation |8|168|80 |hpc4.40core|non-interactive programmatic computation|78|


If you are not sure what is the best option for your needs/reaserch, contact us at servicedesk@csc.fi (email subject:SD Desktop). Do not choose the Heavy computation option for simple computing or analysis, as it consumes large amout of resources.

All the Destkop are provided with the same software. The complete and update list can be found in the following paragraph [Pre-installed list of software](https://github.com/CSCfi/csc-user-guide/blob/sensitive-data/docs/data/sensitive-data/pre-installed_software.md).


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122593105-db0ce480-d06d-11eb-8a42-aab26cf289b8.png">
![SD-Desktop-2final](https://user-images.githubusercontent.com/83574067/122608199-79a44000-d084-11eb-80c6-40dab45004ac.png)
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122593108-dcd6a800-d06d-11eb-9b51-2faaf2937b3a.png">



If the launch is successful, when you return to SD Desktop **Homepage**  you will be able to access the computing enviroment from:

* **Recent connection**, clicking on the image of your Desktop

* **All connection** if you click on + you can see all the connections associated to each project (e.g. project_NNNNN_NNNN). If you click on the connection ID you will also be able to acess your computing enviroment. 


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">
![SD-Desktop-Connection](https://user-images.githubusercontent.com/83574067/122604935-66db3c80-d07f-11eb-8364-df60b0e71699.png)
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595580-5b811480-d071-11eb-9b99-9dcad8b4ac17.png">



In the Desktop you will be able to access different applications from the manu bar on the page top left corner (e.g. Open Office; Jupyter Notebook etc). 
If you need to work on files or datasets with your colleagues, save them in the **Shared-directory**. The file will be visible and accessible to all the members of the same CSC project. 
As previously mentioned, you can **logout** from your computing workspace in SD  Desktop at any moment (in the workspace view, top left corner of the browser, select your username and log out). SD Desktop will keep on computing and running jobs. You will always be able to access your Desktop again after logging in.


<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">
<img width="960" alt="SD-Desktop-Home" src="https://user-images.githubusercontent.com/83574067/122606520-ba4e8a00-d081-11eb-8a43-454776ab87d6.png">
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595580-5b811480-d071-11eb-9b99-9dcad8b4ac17.png">



## Step 3: Importing encrypted sensitive data to SD Desktop


Once you are logged in into your SD Desktop private workspace **you can import encrypted  sensitive data stored in SD Connect**.

!!! Note
    **If you used CSC Sensitive Data Service public encryption key to encrypt the data, the files  will be decrypted automatically**.  If you used your own key pair to           encrypt the data, the application will make a copy and you need to manullay decrypt them using Crypt4GH CLI. 

To import the data:

* **Open SD Connect Downloader client** (you can find the link to the application on your Desktop)

* insert your **CSC credentials** (username and password. Note: we disabled the copy/paste options for security reasons, thus you need to type in your password)

* select your CSC project

* select the correct bucket 

* select the files you want to import 

* click on **download objects** (the application will make a copy of the encrypted files in SD Dekstop).

* click on **open download location**

The files are downloaded to a directory called SDCONNECTDATA which is in the user's home directory. The forlder is automatically opened by Open Download Location.

Note: **If you used CSC Sensitive Data Service public encryption key to encrypt the data, the files  will be decrypted automatically**. 

If you used your own key pair to encrypt the data, the application will make a copy and you need to manullay decrypt them using Crypt4GH CLI. 

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">
<img width="960" alt="SD Desktop 5" src="https://user-images.githubusercontent.com/83574067/121872988-9223fb80-cd0e-11eb-8c5b-7e19a2111407.png">
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">

For security reasons, your private workspace in SD Desktop is **completely isolated from the Internet**. If you need to import specific scripts in SD Desktop (for example from GitHub or other trusted repositories) you need to use the same procedure described before:

* download your scripts from GitHub and save them in a specific container in SD Desktop

* access SD Desktop and use the SD Connect Downloader to make a copy of the scripts
 
 
 
## Step 4: RStudio in SD Desktop

To access RStudio in SD Desktop

R Studio can use the directory with R studio

STart R Studio server it luanches the server in the local enviroemnt. Contact services usinf the URL and then it will ask username and passsword. It will take a few seconds, and in the next page you can service specific password (



 ![Rstudio tot](https://user-images.githubusercontent.com/83574067/122614020-80d04b80-d08e-11eb-8232-25ba81108f2a.png)






## Step 5:  Deleting your work environment
  
At the end of your research or your analysis, you can delete your computing enviroment and all the data in it. 

In SD Desktop Homepage click on **Go to launching page**. Here, in **Available istances** click on **Delete Desktop**. 


!!! note
    All the data present in the computing environment will be deleted and it will not be possible to retrieve them.

<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">
![SD_Desktop_deletingF](https://user-images.githubusercontent.com/83574067/122610703-c25df800-d088-11eb-8e44-2792c1bc2e6c.png)
<img width="574" alt="space" src="https://user-images.githubusercontent.com/83574067/122595541-4efcbc00-d071-11eb-9e34-ad96e414f506.png">


## Step 6: Data export from SD Desktop

For security reseanse, Desktop is isolated from the internet and it is not possible to export data from the virtual computing environment. 
For more information write to servicedesk@csc.fi (email subject SD Desktop)









  
