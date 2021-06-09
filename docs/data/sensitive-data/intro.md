# Sensitive Data Services for Reaserch








## Introduction

**SD Connect (Sensitive Data Connect)** and **SD Desktop (Sensitive Data Desktop)** (beta versions) are web user interfaces which allow you to:

* Access your own secure and personalized computing environment in CSC cloud computing platform (ePouta)

* Securely compute and process sensitive data with your project members and collaborators without the needs of generating multiple copies of your data

* Easily share, collect and store **encrypted sensitive data** for the duration of your project in CSC cloud storage solution (Allas)








## Getting access

To access CSC's services for sensitive data using [MyCSC](https://my.csc.fi) portal:

1. Create a **user account**

3. Create or join a **CSC project** and add project members

4. Fill in the **Personal Data Handling form** and agree with CSC **Data Processing Agreement**. 
    
5. **Each project member** needs to **add service access to SD Desktop and to Allas** (in case you want to use SD Connect, a user interface for CSC cloud storage solution called Allas)

6. Apply for billing units or disk quota

For specific guidance regarding these steps check the [Accounts](https://docs.csc.fi/accounts/) paragraph in the beginning of this user guide. 








## Useful terminology:

**Bucket**: is a container in which all your data/files/directories are stored. You can have multiple buckets for each project. Each bucket is accessible just to you, all the project members and CSC users you personally give access to using MyCSC or SD Connect. The container name is visible to the internet. 

**CSC Project**: all your data in CSC belong inside a project. You can have one project or multiple projects. When you set up a project you can add project members, you need to define a project manager, and you need to described which type of sensitive data you are processing. 

**CSC Project ID**: It can be sourced using the following command using the CLI        or from this link        or from SD Connect User . It defines and it is used for

**CSC Project name**: MY CSC project ID (NNNNN)

**SD Connect Account**: It is the CSC project ID in Open Stak, it is used to define the project with who you share your containers in SD Connect. It is a synonim of CSC Project ID when using the command line tool. In the SD Connect user interface is displayed unser * User Information> Project usage * and displayed as series of  32 numbers and letters: e.g. AUTH_3a66dbf90b2940dc9c651362af595b23. 

**Virtual machine (VM)**: is a virtual computing environment which works like a real-physical computer. It has a processor, memory and operating system but it exists only as a code or a partition of the host computer. VMs used for the Sensitive Data Services currently support only Linux operating system and are completely isolated from the internet for security reasons. 

**Virtual machine flavor (VM flavor)**: a flavor defines the resources and configurations of a cloud computing environment. It specifies the compute, memory, and storage capacity that can be assigned to virtual machine. 



Notes that require discussion:

-Add here also encryption?
-What document is required for people that are processign sensitive data but not personal data? where do they sign the DPA?
-Does it even make any sense to define bukect if in the SD Connect UI are called containers?
- how can I source the project ID with CLI in Opne stack? or with CSC resources if I know---?
- AUHT is still present in SD Connect

  

