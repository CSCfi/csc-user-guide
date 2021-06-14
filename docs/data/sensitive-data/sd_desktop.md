
# SD Desktop (Sensitive Data Desktop)

## Step1 : Login 




To access SD Desktop you need:

* **a CSC account**

* **a CSC project**

* **Service access to SD Destkop.**


To import (or download) encrypted sensitive data to SD Desktop you need:

* **service access to Allas** (CSC cloud storage solution). 


Login to SD Desktop is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https:/sd-desktop.csc.fi using any modern web browser. 


!!! note  Indipendently of the login method used, you need your **CSC username and password to import sensitive data** in your SD Desktop computing enviroment (or workspace). If you don't remeber it, check how to reset it at [Account: How to change password] (https://docs.csc.fi/accounts/how-to-change-password/)




!!! note **All the project members belonging to a specific CSC project can access the same computing environment in SD Desktop.** Currently, it is possible to launch only one Desktop (or workspace) for each CSC project. Each CSC project has its own virtual private computing environment and each computing environment (or VM) is isolated from other projects or CSC accounts. 




!!! note It is the project manager or group leader responsibility to review the list of members belonging to a project frequently in MyCSC and verify who can access the data present in the project using SD Desktop or SD Connect. Remove the project members that do not need to have access to the data when their contribution is no longer needed.  




!!! note Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***








## Step 2: Launching your Desktop (your private work environment)




Once you fisrt login in SD Desktop _Homepage_ you can launch your Desktop by clicking on _Go to the Launching page_. 






[![SD Desktop homepage](images/small/sd-desktop-1.png)](images/large/sd-desktop-1.png)


<img width="958" alt="SD Desktop 1" src="https://user-images.githubusercontent.com/83574067/121861598-9ea25700-cd02-11eb-8ba0-4d10b0094f7e.png">


 ![](img/SDDkScreenshot_1.png)
 
 
 
 
 
 
 
 
 
Here you can:

* select your CSC project

* choose the operating system (for beta versions, only possible operating system is Linux ChentOS 7)

* select the preferred computing enviroment (based on your needs) and click on _+ Create instance_


Next, the system will create your private work space in SD Desktop. The process is completely authomated and might take up to 30 minutes. During this time, you can close your browser / log out /leave your browser window open/

If the process is sucessfull you will be able to see........

You might encounter this error: write to servicedesk@csc.fi and use SD Desktop launch in the email subject.







<img width="960" alt="SD Desktop 2" src="https://user-images.githubusercontent.com/83574067/121864441-9697e680-cd05-11eb-8b68-ec01eec86943.png">








In SD Dekstop (Open Beta) you can choose between four different Desktops:  

|Desktop for|CPU|Storage capacity|Billing unites|example usage|
|--- |:---:|:---:|:---:|:---:|
| Light Computation  | add | add  | add | testing the services |
| Small Computation   | add | add | add | statistical analysis of smal datasets | 
| Memdium Computation | add | add | add |  complex analysis of lasrge datasets |
| Heavy Computation | add | add | add | parallel computing e.g. machine learning | 


 A complete updated list of pre-sintalled sofware is available here:

https://github.com/CSCfi/csc-user-guide/blob/sensitive-data/docs/data/sensitive-data/pre-installed_software.md







## Step2: Access to your Desktop (or private work enviroment)



 
Once you have launched your privite work enviroment, you will be able to access it in SD Desktop **Connection page** (homepage):

* in **All connections** you can select a CSC project and after clicking on the + icon, you can open your Desktop clicking on the project name (example project_NNNNNN_NNNNN)

* in **Recent connections** you can click on the work enviroment image

A black screen might appear for a few second, depending on yout internet connection. Iven after you log out, the Desktop will always be available for computation and consume billing units, unitil you will delete it. 










<img width="960" alt="SD Desktop 4" src="https://user-images.githubusercontent.com/83574067/121869624-e7f6a480-cd0a-11eb-9436-55e4adcf5b4f.png">


 ![](img/SDDkScreenshot_3.png)


!!! note If you and your colleagues/ collaborators want to ***access the same SD Desktop you** you need to belong to the ***same CSC project as project members, and you all need service access to SD Desktop***








In SD Desktop you can **access a pre-installe list of software** from the top right corner in the **application drop down menu**.

A complete updated list is available here:

https://github.com/CSCfi/csc-user-guide/blob/sensitive-data/docs/data/sensitive-data/pre-installed_software.md



To **acess R Studio or Phyton** you can run the follwoing script:



To share files or datasets with your colleagues, you can save them in the **shared folder**. 

!!! note: even if you are using the same workspace in SD Desktop, in the open beta versionsof SD Desktop you will not be able to simultaneurly work on the same file (as, for security reasons the work enviroment is isolated form the internet).





<img width="960" alt="SD Desktop 3" src="https://user-images.githubusercontent.com/83574067/121873934-913f9980-cd0f-11eb-8c76-30be9f2e0f5b.png">














 
## Step3: Importing (or downloading) encrypted sensitive data to SD Desktop




To import your encrypted data from SD Connect to your SD Desktop you need to:  

* **Open  SD Connect Dowloader client** (link available on the Desktop)

* insert your **CSC credentials** (username and password. Note: we disabled the copy/paste options for security reasons, thus you need to type in your passoword)

* **select your CSC project**

* **select the correc bucket (or container)**

* **select the files** you want to import

* **click on dowload objects** (the client will make a copy of the encrypted files in SD Dekstop. If you used CSC Sensitive Data Services public key the data will be deencrypted automatically)

* click on **open dowload location**

* then **I am not sure where they find the folder : XXXX**


<img width="960" alt="SD Desktop 5" src="https://user-images.githubusercontent.com/83574067/121872988-9223fb80-cd0e-11eb-8c5b-7e19a2111407.png">




Video example: https://kannu.csc.fi/s/dXHeTy27LcAQATx    (T account and name) this will be re-done by Aada


!!! note Open Beta version of SD Dekstop has only 40 GB of disk space. If you are trying to import more then 40 GB of data you will see the following error: XXXXX






For security reasons, your private work space in SD Desktop is **completely isolated from the Internet**. If you need to import specific scripts in SD Desktop (for example from GitHub or other trusted repositories) you need to use the same procedure described before:

* dowload your scripts  from GitHub and save them in a specific conatiner in SD Desktop

* access SD Desktop and use the SD Connect Dowloader to make a copy of the scripts 
 
 
 

!!! note To access your encrypted data in SD Desktop, **the same CSC project needs to have service access for Allas (CSC storage solution) and SD Desktop**. 

    
    
## Step 4: Logging out; Killing connection; Deleting your work enviroment

As previuosy mentioned, you can **logout** from your computing workspace in SD  Desktop at any moment (in the workspace view, top left corner of the browser, select the XXX icon, select your username and log out). SD Desktop will keep on comptuting and runnign jobs. You will always be able to access again your Desktop after log in.


From SD Desktop Homapge you can **Kill your connection to SD Desktop**: 

* on the top right corner fo the browser, select your user name and select **settings**

* in the **Active session** window, select your connection and next click on Kill connection

meaning: ?



AT the end of your reaserch or your analysis, you can delete the computing enviroment going in:

* SD Desktop Homepage

* click on **Go to launcing page**

* click on **Delete Instance**


!!! note: all the data present in the computing enviroment will be deleted and it will not be possible to retreve them. 



<img width="960" alt="SD Desktop 6" src="https://user-images.githubusercontent.com/83574067/121877371-3445e280-cd13-11eb-870d-99767242d402.png">





## Step 5: Data export from SD Desktop




SD Desktop is not connected to the internet for security reasons.

To export processed sensitive data or non-sensitive data (results) data from your Desktop you need to:

* **Only the project manager or group leader** can make the  request writing to ***servicedesk@csc.fi*** and use **SD Desktop (Export Request)** in the object field

* Add the CSC project number and bucket or container ID in SD Connect in which the data need will be exported by CSC Cloud administrators

* The request will be **processed by CSC cloud administrators** and it may require **up to 10 days to be processed**.  

!!! note Always **encrypt sensitive data that need to be exported out of SD Desktop.** If the encryption with Crypt4GH is successful, the file name will end with .c4gh



 Unclear points:
 - private computing enviroment / private work space / Desktop (mught be a bit confusing)
 - killing session
 - how access R studio and Phyton Crypt4GH? Can they install their own encryption tool?




