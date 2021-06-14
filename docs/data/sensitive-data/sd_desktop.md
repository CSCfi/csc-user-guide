
# SD Desktop (Sensitive Data Desktop)

## Step1 : Login 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
To access SD Desktop you need:

* **a CSC account**

* **a CSC project**

* **Service access to SD Desktop.**


To import (or download) encrypted sensitive data to SD Desktop you need:

* **service access to Allas** (CSC cloud storage solution).


Login to SD Desktop is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https:/sd-desktop.csc.fi using any modern web browser.


!!! note 
    Independently of the login method used, you need your **CSC username and password to import sensitive data** in your SD Desktop computing environment       (or workspace). If you don't remember it, check how to reset it at [Account: How to change password] (https://docs.csc.fi/accounts/how-to-change-password/)




!!! note 
    All the project members belonging to a specific CSC project can access the same computing environment in SD Desktop.** Currently, it is possible to         launch only one Desktop (or workspace) for each CSC project. Each CSC project has its own virtual private computing environment and each computing         environment (or VM) is isolated from other projects or CSC accounts.




!!! note 
    It is the project manager or group leader responsibility to review the list of members belonging to a project frequently in MyCSC and verify who can       access the data present in the project using SD Desktop or SD Connect. Remove the project members that do not need to have access to the data when         their contribution is no longer needed.  




!!! note 
    Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***








## Step 2: Launching your Desktop (your private work environment)
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 

Once you login in SD Desktop **Homepage** you can launch your Desktop by clicking on **Go to the Launching page**.

Here you can:

* **select your CSC project**

* **choose the operating system** (for beta versions, only possible operating system is Linux CentOS 7)

* **select** the preferred computing environment (based on your needs) and click on  + icon and on **Create instance**


Next, the system will create your private work space in SD Desktop. The process is completely automated and might take up to 30 minutes. During this time, you can close your browser / log out /leave your browser window open/

If the process is successful you will be able to see........

You might encounter this error: write to servicedesk@csc.fi and use SD Desktop launch in the email subject.


In SD Dekstop (Open Beta) you can choose between **four different Desktops or workspaces**:  

|Desktop for|CPU|Storage capacity|Billing unites|example usage|
|--- |:---:|:---:|:---:|:---:|
| Light Computation  | add | add  | add | testing the services |
| Small Computation   | add | add | add | statistical analysis of small datasets |
| Medium Computation | add | add | add |  complex analysis of large datasets |
| Heavy Computation | add | add | add | parallel computing e.g. machine learning |

&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 

A complete updated list of **preinstalled software** available in every worsksapce is can be found here:

https://github.com/CSCfi/csc-user-guide/blob/sensitive-data/docs/data/sensitive-data/pre-installed_software.md


&nbsp;   
&nbsp; 
&nbsp; 
&nbsp; 

<img width="958" alt="SD Desktop 1" src="https://user-images.githubusercontent.com/83574067/121861598-9ea25700-cd02-11eb-8ba0-4d10b0094f7e.png">
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp;
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 

<img width="960" alt="SD Desktop 2" src="https://user-images.githubusercontent.com/83574067/121864441-9697e680-cd05-11eb-8b68-ec01eec86943.png">
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 
&nbsp; 


## Step3: Importing encrypted sensitive data to SD Desktop
&nbsp;
&nbsp;
&nbsp;
&nbsp;
Once you are logged in into your SD Desktop private workspace you can import encrypted data stored in SD Connect:

* **Open SD Connect Downloader client** (link available on the Desktop...bit confusing :-) )

* insert your **CSC credentials** (username and password. Note: we disabled the copy/paste options for security reasons, thus you need to type in your password)

* **select your CSC project**

* **select the correct bucket (or container)**

* **select the files** you want to import

* **click on download objects** (the client will make a copy of the encrypted files in SD Dekstop. If you used CSC Sensitive Data Services public key the data will be decrypted automatically)

* click on **open download location**

* then **I am not sure where they find the folder : XXXX**


<img width="960" alt="SD Desktop 5" src="https://user-images.githubusercontent.com/83574067/121872988-9223fb80-cd0e-11eb-8c5b-7e19a2111407.png">
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;



Video example: https://kannu.csc.fi/s/dXHeTy27LcAQATx    (T account and name) this will be re-done by Aada


!!! note 
     Open Beta version of SD Desktop has only **40 GB of disk space.** If you are trying to import more then 40 GB of data you will see the following            error: XXXXX
&nbsp; 
&nbsp;   
&nbsp;   
&nbsp; 

For security reasons, your private work space in SD Desktop is **completely isolated from the Internet**. If you need to import specific scripts in SD Desktop (for example from GitHub or other trusted repositories) you need to use the same procedure described before:

* download your scripts from GitHub and save them in a specific container in SD Desktop

* access SD Desktop and use the SD Connect Downloader to make a copy of the scripts
 

!!! note To access your encrypted data in SD Desktop, **the same CSC project needs to have service access for Allas (CSC storage solution) and SD Desktop**.


## Step 4: Logging out; Killing connection; Deleting your work environment
&nbsp;
&nbsp;
&nbsp;
&nbsp;

As previously mentioned, you can **logout** from your computing workspace in SD  Desktop at any moment (in the workspace view, top left corner of the browser, select the XXX icon, select your username and log out). SD Desktop will keep on computing and running jobs. You will always be able to access your Desktop again after logging in.


From SD Desktop Homepage you can **Kill your connection to SD Desktop**:

* on the top right corner of the browser, select your user name and select **settings**

* in the **Active session** window, select your connection and next click on **Kill Connection**

meaning: ?



At the end of your research or your analysis, you can delete your private workspace in:

* SD Desktop Homepage

* click on **Go to launching page**

* click on **Delete Instance**


!!! note
    All the data present in the computing environment will be deleted and it will not be                         possible to retrieve them.
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<img width="960" alt="SD Desktop 6" src="https://user-images.githubusercontent.com/83574067/121877371-3445e280-cd13-11eb-870d-99767242d402.png">
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
## Step 5: Data export from SD Desktop
&nbsp;
&nbsp;
&nbsp;
&nbsp;
SD Desktop is not connected to the internet for security reasons.

To export processed sensitive data or non-sensitive data (results) data from your Desktop you need to:

* make a request writing to ***servicedesk@csc.fi*** and use **SD Desktop (Export Request)** in the object field

Note! **Only the project manager or group leader** can make the request

* Add the CSC project number and bucket or container ID in SD Connect in which the data need will be exported by CSC Cloud administrators

* The request will be **processed by CSC cloud administrators** and it may require **up to 10 days to be processed**.  

!!! note
    **Only the project manager or group leader** can apply for an export request.

!!! note
     Always **encrypted sensitive data which need to be exported out of SD Desktop.** If the encryption with Crypt4GH is successful, the file name will end with .c4gh



 Unclear points:

 - how do we define it? private computing environment / private workspace / Desktop (might be a bit confusing)
 - killing session meaning
 - how to access R studio and Python Crypt 4GH? Can they install their own encryption tool?







  
