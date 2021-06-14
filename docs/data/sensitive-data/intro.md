
# Sensitive Data Services for Reaserch


## Introduction

Sensitive Data Services (SD Services) provide CSC customers a secure
cloud computing environment, that can be used for processing sensitive
data. The SD Services have increased security, compared to the
HPC (Puhti and Mahti) and general purpose cloud environments (cPouta and Rahti) of CSC.
Thus data, that can't be processed in these environments may still processed in the
SD Services environment.

Compared to the secure ePouta cloud environment, SD services are
easier to access and share. The service can be used from everywhere and it does
not require a dedicated network connection between the user and CSC. This makes the service easy to take in use and also enables studies, where researchers from different organizations need to share a secure work space.

The SD Services consists of two components:

   * **SC Connect** is a web user interface to import data to SD Services-
   * **SD Desktop** provides a web user interface to a project specific secure virtual desktop. This virtual machine desktop is not connected to the internet. This enables secure computation and processing of sensitive data. All project members and collaborators can access this desktop so you don't need to generate multiple copies of your data. As data can't be exported from SD desktop, it can be used to provide a limited and restricted access to a specific dataset.  
 



## Getting access

SD Services are available for all CSC customers.
To access CSC's services for sensitive data using [MyCSC](https://my.csc.fi) portal:

1. Create a **user account**

3. Create or join a **CSC project** and add project members

4. Fill in the **Personal Data Handling form** and agree with CSC **Data Processing Agreement**.
    
5. **Each project member** needs to **add service access to SD Desktop and to Allas** (in case you want to use SD Connect, a user interface for CSC cloud storage solution called Allas)

6. Apply for billing units or disk quota

For specific guidance regarding these steps check the [Accounts](https://docs.csc.fi/accounts/) paragraph in the beginning of this user guide.





## Useful terminology:

**Allas**: The general purpose data storage service of CSC. At the moment SD-connect is using Allas as the storage service and you can in practice consider Allas and SD Connect as just one service. However, ongoing development of SD connect is likely to make it diverge from the standard Allas service in the future.

**Bucket/Container**: In object storage systems the storage spaces into which files are stored are called in some tools as _containers_ and in some tools as _bukcets_. These two terms refer to the same thing: the kind-of root directories in your storage area in Allas/SD Connect. The bucket/container name is visible to the internet. You can have multiple buckets in the same project (up to 500), but each bucket must have a name that is unique throughout the whole storage system (including other projects). By default the data in a bucket is accessible just to the project members. However you can grant access to other CSC projects  or users with SD Connect.

**CSC Project**: all your data in CSC belong inside a project. You can have one project or multiple projects. When you set up a project you can add project members, you need to define a project manager, and you need to describe which type of sensitive data you are processing.

**CSC Project ID**: It can be sourced using the following command using the CLI        or from this link        or from SD Connect User . It defines and it is used for

**CSC Project name**: MY CSC project ID (NNNNN)

**SD Connect Account**: It is the CSC project ID in Openstack, it is used to define the project with whom you share your containers in SD Connect. It is a synonym of CSC Project ID when using the command line tool. In the SD Connect user interface is displayed unser * User Information> Project usage * and displayed as a series of  32 numbers and letters: e.g. AUTH_3a66dbf90b2940dc9c651362af595b23.

**Virtual machine (VM)**: is a virtual computing environment which works like a real-physical computer. It has a processor, memory and operating system but it exists only as a code or a partition of the host computer. VMs used for the Sensitive Data Services currently support only Linux operating systems and are completely isolated from the internet for security reasons.

**Virtual machine flavor (VM flavor)**: a flavor defines the resources and configurations of a cloud computing environment. It specifies the compute, memory, and storage capacity that can be assigned to the virtual machine.



Notes that require discussion:

-Add here also encryption?
-What document is required for people that are processing sensitive data but not personal data? Where do they sign the DPA?
-Does it even make any sense to define buckets if in the SD Connect UI are called containers?
- how can I source the project ID with CLI in Openstack? or with CSC resources if I know---?
- AUHT is still present in SD Connect






 


