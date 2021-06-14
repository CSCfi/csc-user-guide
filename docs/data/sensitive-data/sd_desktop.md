
# SD Desktop (Sensitive Data Desktop)

## Step1 : Login 

To access SD Desktop you need:

* **a CSC account**

* **a CSC project**

* **Service access to SD Destkop.**
* 

To import (or download) encrypted sensitive data to SD Desktop you need:

* **service access to Allas** (CSC cloud storage solution). 


Login to SD Desktop is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https:/sd-desktop.csc.fi using any modern web browser. 


!!! note  Indipendently of the login method used, to import sensitive data in your SD Desktop computing enviroment, you need your CSC username and password. If you don't remeber it, check how to reset it at: https://docs.csc.fi/accounts/how-to-change-password/




!!! note ***All the project members belonging to a specific CSC project can access the same computing environment in SD Desktop.*** Currently, it is possible to launch only one VM for one CSC project. Each CSC project has its own virtual private computing environment and each computing environment (or VM) is isolated from other projects or CSC accounts. 




!!! note It is the project manager or group leader responsibility to review the list of members belonging to a project frequently in MyCSC and verify who can access the data present in the project using SD Desktop or SD Connect. Remove the project members that do not need to have access to the data when their contribution is no longer needed.  




!!! note Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***








## Step 2: Launching your Desktop (your private work environment)


Once you fisrt login in SD Desktop _Homepage_ you can launch your Desktop by clicking on _Go to the Launching page_. 









<img width="958" alt="SD Desktop 1" src="https://user-images.githubusercontent.com/83574067/121861598-9ea25700-cd02-11eb-8ba0-4d10b0094f7e.png">


 ![](img/SDDkScreenshot_1.png)
 
 
 
 
 
 
 
 
 
Here you can:

* select your CSC project

* choose the operating system (for beta versions, only possible operating system is Linux ChentOS 7)

* select the preferred computing enviroment (based on your needs) and click on _+ Create instance_


Next, the system will create your private work space in SD Desktop. The process is completely authomated and might take up to 30 minutes.

If the process is sucessfull you will be able to see........

You might encounter this error: write to servicedesk@csc.fi and use SD Desktop launch in the email subject.







<img width="960" alt="SD Desktop 2" src="https://user-images.githubusercontent.com/83574067/121864441-9697e680-cd05-11eb-8b68-ec01eec86943.png">








In SD Dekstop (Open Beta) you can choose between four different Desktops:  

|Desktop for|CPU|Storage capacity|Billing unites|example usage|
|--- |:---:|:---:|:---:|:---:|
| Light Computation  | 3 | 4  | 80 | testing the services |
| Small Computation   | 4 | 7  | 80 | statistical analysis of smal datasets | 
| Memdium Computation | 6 | 15 | 80 |  complex analysis of lasrge datasets |
| Heavy Computation | 8 | 30 | 80 | parallel computing e.g. machine learning | 




Once the computing environment is open you can access the pre-installed software in each Desktop:

A complete updated list is available here:

https://github.com/CSCfi/csc-user-guide/blob/sensitive-data/docs/data/sensitive-data/pre-installed_software.md







## Step2: Access to your Desktop (or private work enviroment)

 
Once you have launched your privite work enviroment, you will be able to access it in SD Desktop *Connection page*:

* in **All connections** you can select a CSC project and after clicking on the + icon, you can open your Desktop clicking on the project name (example project_NNNNNN_NNNNN)

* in **Recent connections** you can click on the work enviroment image

The Desktop will always be available for computation and consume billing units unitil you will delete it. 


!!! note If you and your colleagues want to ***access the same SD Desktop you** all need to belong to the ***same CSC project as project members.***









<img width="960" alt="SD Desktop 4" src="https://user-images.githubusercontent.com/83574067/121869624-e7f6a480-cd0a-11eb-9436-55e4adcf5b4f.png">


 ![](img/SDDkScreenshot_3.png)




 
## Importing encrypted sensitive data to SD Desktop

To import from SD Connect your data you need to:  

* Open the SD Connect Dowloader client

* insert your CSC credentials (username and password) (They might not remeber it? WHat id they login with HAKA?)

* select the correct  CSC project

* select the correc container

* select the file/ folders you want to import

* click on dowload objects (the client will make a copy of the encrypted files/ folders in SD Dekstop, if you used CSC Sensitive Data Services public key the data will be deencrypted automatically)

* click on open dowload location

* then I am not sure where they find the folder : XXXX

* If you use your own encryption key pair, you can import the encrypted data. 


Video example:

CLI https://kannu.csc.fi/s/dXHeTy27LcAQATx    (T account and name), need to be redone or blured


!!! Note, to access your encrypted data in SD Desktop, the same CSC project needs to have service access for Allas (CSC storage solution and SD Connect) and SD Desktop. 



If you use your own encryption keys instead, you can import the encrypted data. 


## Upload of specific scripts from GitHub

If you need to import specific scrips for GitHub or other trusted repositories, you need to: 

    Download the script from the internet to SD Connect in a specific bucket 

    Import the script/ files or other non-sensitive data to SD Desktop 
    
    
## Active session/ VM disconnection / Kill session

If you turn off the computing environment……….. 


Settings:  

Active session: If you click on click session................ 

 

Preferences: 



## Data export from SD Desktop

How to export processed sensitive data or non-sensitive data (results) data from the secure computing environment 

SD Desktop is not connected to the internet for security reasons. Thus, to export the results of your analysis (non-sensitive data) or to export encrypted processed sensitive data:

* **Only the project manager or group leader** can make the  request writing to ***servicedesk@csc.fi*** and use **SD Desktop (Export Request)** in the object field

* Add the CSC project number and buket or container ID in SD Connect in which the data need will be exported by CSC Cloud administrators

* The request will be processed by our cloud administrators and it may require up to 10 days to be processed.  

!!!Note: always encrypt sensitive data that need to be exported out of SD Desktop. If the encryption with Crypt4GH is successful, the file name will end with  .c4gh


## End of your project and computing enviroment deletion

AT the end of your project or analisys, you can delete the computing enviroment going in:

* SD Desktop Homepage
* Launch the VM
* Select Delet

Note: all the data present in teh computing enviroment will be deleted and it will not be possible to retreve them. 




Notes: 
1) how do they install stuff
2) how do they import stuff
3) naming of the VMs...confusing for some users
4) Adjust table
5) examples use VM
6) Need to indicated container? can they import the all container? is there a progress bar? how fast is it? do they always have to use a client? 
Does the dowloader yous CSC account only? Where do they find the info if they do not remeber it?

8) Check homepage (what did we add there)?
         




