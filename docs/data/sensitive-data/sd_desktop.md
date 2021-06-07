
# SD Desktop (Sensitive Data Desktop)

## User Interface and Login 

To access SD Desktop you need:

* **a CSC account**
* **a CSC project**
* **Service access to SD Destkop.**

To import (or download) encrypted sensitive data to SD Desktop you need:
* **service access to Allas** (CSC cloud storage solution). 

Login to SD Desktop is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https://anvil-test.sd.csc.fi/guacamole/#/ using any modern web browser. (last not trhough yet).

***All the project members belonging to a specific CSC project can access the same computing environment (or Virtual machine, VM) in SD Desktop.*** Currently, it is possible to launch only one VM for one CSC project. Each CSC project has its own virtual private computing environment and each computing environment (or VM) is isolated from other projects or CSC accounts. 

!!! Note: It is the project manager or group leader responsibility to review the list of members belonging to a project frequently in MyCSC and verify who can access the data present in the project using SD Desktop or SD Connect. Remove the project members that do not need to have access to the data when their contribution is no longer needed.  

!!!Note: Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***


## Step1: Launching your private computing environment (or VM) in SD Desktop


Once you Login in SD Desktop _Homepage_ you can launch your VM by clicking on _Go to the Launching page_. 

<img width="607" alt="SDDkSreenshot_1" src="https://user-images.githubusercontent.com/83574067/121067523-d590de00-c7d3-11eb-9fa9-e4675ab76f97.png">

 ![](img/SDDkScreenshot_1.png)
 
Here you can:

* select your CSC project

* choose the operating system (for beta versions, only possible operating system is Linux)

* select the preferred VM flavor (based on your study/reaserch) and click on _+ Create_

 ![](img/SDDkScreenshot_2.png)
 

If the VM is created successfully: 




For the beta version of the service, you can choose between six different VM flavors:  

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Light Computation  | 3 | 4  | 80 | 0 | 80 | 1.3 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 1    |
| Small Computation   | 4 | 7  | 80 | 0 | 80 | 1.8 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 2    |
| Memdium Computation | 6 | 15 | 80 | 0 | 80 | 2.5 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 4    |
| Heavy Computation | 8 | 30 | 80 | 0 | 80 | 3.8 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 8    |




Example usage:

Light Computation : suitable to test the service (e.g. familiarise witht he user interface)

Small Computation  : statistical analysis

Memdium Computation : complex analysis of large datasets (e.g. genetic sequences)

Heavy Computation :Parallel computing of large datasets (e.g. machine learning) 


## Step2: Access to the computing environment and software installation

 
From SD Desktop _Homepage_ you can access:

_Recent Connections_ or _All connections_ and open your  private computing enviroment (or VM) with double click.


<img width="641" alt="SDDkSreenshot_3" src="https://user-images.githubusercontent.com/83574067/121067560-e04b7300-c7d3-11eb-81c0-db5bf0eb81f3.png">


 ![](img/SDDkScreenshot_3.png)
 
Once the computing environment is open, you can start the installation of necessary software or searching for specific packages using the search bar or  using the following command:

`` bla bla bla``



!!! Note: if you and your colleagues want to ***access the same computing enviromen*** in SD Desktop you all need to belong to the ***same CSC project as project members.***

 
## Importing encrypted sensitive data to SD Desktop

To import your data you need to:  

CLI https://kannu.csc.fi/s/dXHeTy27LcAQATx    (T account and name)

It is possible to visualize and import data saved in buckets belonging to your projects. 

!!! Note, to access your encrypted data in SD Desktop, the same CSC project needs to have service access for Allas (CSC storage solution and SD Connect) and SD Desktop. 

If you use SDS public key to encrypt the data you will be able to import and decrypt the data automatically with the client:

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




Notes: 
1) how do they install stuff
2) how do they import stuff
3) naming of the VMs...confusing
4) Adjust table
5) examples use VM
6) Need to indicated container?
7) Check homepage (what did we add there)?
         




