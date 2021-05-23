
# SD Desktop (Sensitive Data Desktop)

## User Interface and Login 

 
To acces SD Desktop you need a CSC account, a CSC project and service access to SD Destkop and to Allas (CSC cloud storage solution). 
Login is possible with user identity federation systems (ELIXIR AAI, Haka or Virtu ) or with a CSC account at: https://anvil-test.sd.csc.fi/guacamole/#/ using any modern web browser. 

All the project members belonging to a specific CSC project can access the same computing environment (or Virtual machine, VM) in SD Desktop. Currently, it is possible to launch only one VM for one CSC project. Each CSC project has its own virtual private computing environment and each computing environment (or VM) is isolated from other projects or CSC accounts. 

!!! Note: It is the project manager or group leader responsibility to review the list of members belonging to a project frequently in MyCSC and verify who can access the data present in the project using SD Desktop or SD Connect. Remove the project members that do not need to have access to the data when their contribution is no longer needed.  


**Step1. Launching the computing enviroment (or VM)**

Once you Login in SD Destkop Homepage you can launch your VM clicking on _Go to the Launching page_. 

 ![](img/SDkScreenshot_1.png)
 
Here you can:

* select your CSC project

* choose the operating system (for beta versions, only possible operating system is Linux)

* select the preferred VM flavor (based on your study/reaserch) and click on _+ Create_

 ![](img/SDEnScreenshot_2.png)

If the VM is created successfully this message: 




For the beta version of the service, you can choose between six different VM flavors:  

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| standard.tiny    | 1 | 1  | 80 | 0 | 80 | 1   |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 0.25 |
| standard.medium  | 3 | 4  | 80 | 0 | 80 | 1.3 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 1    |
| standard.large   | 4 | 7  | 80 | 0 | 80 | 1.8 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 2    |
| standard.xlarge  | 6 | 15 | 80 | 0 | 80 | 2.5 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 4    |
| standard.xxlarge | 8 | 30 | 80 | 0 | 80 | 3.8 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 8    |
| hpc.3.56core     | 56 | 240 | 80 | 0 | 80 | 4.3 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 96  |
| hpc.4.40core     | 40 | 168 | 80 | 0 | 80 | 4.2 |![](/img/circle_icons/p100.svg)![](/img/circle_icons/r100.svg)![](/img/circle_icons/n100.svg)| 60  |



Example usage 
Statistical analysis of small datasets 
Complex analysis of large datasets 
Parallel computing of large datasets (e.g. machine learning) 

 **Step2. Access to the computing enviroment and softwear installation**
 
From SD Desktop Homapage you can access the _Recent Connections_ or _All connections_ and open the VM with double click.

 ![](img/SDEnScreenshot_3.png)
 
Once the compting enviroment is open, you can start the installation of necessary softwear or packages searching ---- and using the following command-------

Here you can find the comeplete list of software and packages available in SD Desktop: (link ?)


!!! Note: only the project manager or group leader can launch a new VM.  

 
## Data upload 

To import your data you need to:

It is possible to visualize and import data saved in buckets belonging to your projects (note, the same project needs to have service access for Allas (CSC storage solution and SD Connect) and SD Desktop. 

With the following tool, you will be able to import data and automatically decrypt the data if you used SDS public key to encrypted them or to import encrypted data if you used your own encryption keys. 



## Upload of specific scripts from GitHub

If you need to import specific scrips for GitHub or other trusted repositories, you need to: 

    Download the script from the internet to SD Connect in a specific bucket 

    Import the script/ files or other non-sensitive data to SD Desktop 
    
## Active session/ VM disconnection / Kill session

If you turn off the computing environment……….. 


Settings:  

Active session: If you click on click session................ 

 

Preferences: 



## Data export

How to export processed sensitive data or non-sensitive data (results) data from the secure computing environment 

SD Desktop is not connected to the internet for security reasons. Thus, to export the results of your analysis (non-sensitive data) or to export processed sensitive data, please write to servicedesk@csc.fi and use Sensitive Data Services Export Request in the object field. Only the project manager or group leader can make the following request. Add the project number and container ID (?) and save the data that need to be exported in the following folder/directory. The request will be processed by our cloud administrators and it may require up to 10 days to be processed.  

!!!Note: always encrypt sensitive data that need to be exported out of SD Desktop. If the encryption with Crypt4GH is successful, the file name will end with crypth4GH. 
