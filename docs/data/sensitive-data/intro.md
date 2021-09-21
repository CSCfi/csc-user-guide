
# Sensitive Data Services for Research


## Introduction

Sensitive Data Services for Research  (SD Services) provide CSC customers a secure cloud computing environment that can be used for processing sensitive data according to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use). The services are currently released in Open Beta. To learn more about SD services future development check the [Sensitive Data Services for Research webpage](https://research.csc.fi/sensitive-data).

SD Services  (Open Beta) consists of two components:

   * **SC Connect** is a web user interface for importing data to SD Services and for facilitating sensitive data management.
   
   * **SD Desktop** is a web user interface that provides access to a secure virtual computing environment ( or virtual desktop). This virtual desktop is not connected to the internet. This enables secure computation and processing of sensitive data. All CSC project members and collaborators can access the same computing environment (or desktop ) so you don't have to generate multiple copies of your data. As data can't be exported from SD desktop, it can be used to provide a limited and restricted access to a specific dataset.  
 
SD Services have increased security, compared to the HPC (Puhti and Mahti) and general purpose cloud environments (cPouta and Rahti) of CSC.
Thus data that can't be processed in these environments may still be processed in SD Services environment.

Compared to the secure ePouta cloud environment, SD services are easier to access and share. The service can be used from everywhere and it does not require a dedicated network connection between the user and CSC. This makes the service easy to take in use and also enables studies, where researchers from different organizations need to share a secure work space.




## Getting access

SD Services are available for all CSC customers.
To access CSC's services for sensitive data using [MyCSC](https://my.csc.fi) portal:

   1. Create a **user account**

   3. Create or join a **CSC project** and add project members

   4. Fill in the **Personal Data Handling form** and agree with CSC **Data Processing Agreement**
    
   5. **Each project member** needs to **add service access to SD Desktop and to Allas** (in case you want to use SD Connect, a user interface for CSC cloud storage solution called Allas)

   6. Apply for billing units or disk quota

For specific guidance regarding these steps check the [Accounts](../../accounts/index.md) paragraph in the beginning of this user guide.





<figure class="video_container">

<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/wbSf9wR305A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

 <iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/x7PjZdJUh4c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> 

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/-d8yiaLTLmQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> 

</figure>




## Quickstart guide for data analysis with SD Desktop

This quickstart guides you through importing encrypted sensitive data in your private Desktop for data analysis.

<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/ClG8mae8e3k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



[![Landing page](images/small/landing-page.png)](images/large/landing-page.png)
[![My profile](images/small/my-profile.png)](images/large/my-profile.png)
[![Change password](images/small/change-password.png)](images/large/change-password.png)


## Quickstart guide for data analysis with SD Connect

This quickstart guides you through  encrypted sensitive data with personal encryption keys for data sharing using SD Connect.


<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/OOa3oKy5Xs4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>





## Useful terminology:

**Allas**: The general purpose data storage service of CSC. At the moment SD-connect is using Allas as a storage service and you can in practice consider Allas and SD Connect as just one service. However, ongoing development of SD connect is likely to make it diverge from the standard Allas service in the future.

**Bucket/Container**: In object storage systems the storage spaces into which files are stored are called in some tools as _containers_ and in some tools as _bukcets_. These two terms refer to the same thing: the kind-of root directories in your storage area in Allas/SD Connect. The bucket/container name is visible to the internet. You can have multiple buckets in the same project (up to 500), but each bucket must have a name that is unique throughout the whole storage system (including other projects). By default the data in a bucket is accessible just to the project members. However you can grant access to other CSC projects or users with SD Connect.

**CSC Project**: Using CSC services is based on projets: all your data in CSC belong inside a project. You can belong to one or multiple projects. Each project has a main user, project manager, who can add members and services to the project. Project manager is responsible for the activities of the project. She for example needs to describe which type of sensitive data the project is processing.

**SD Connect Account**: It is the CSC project ID in Openstack, it is used to define the project with whom you share your containers in SD Connect. It is a synonym of CSC Project ID when using the command line tool. In the SD Connect user interface is displayed under *User Information> Project usage* and displayed as a series of  32 numbers and letters: e.g. AUTH_3a66dbf90b2940dc9c651362af595b23.

**Virtual machine (VM)**: is a virtual computing environment which works like a real-physical computer. It has a processor, memory and operating system but it exists only as a code or a partition of the host computer. VMs used for the Sensitive Data Services currently support only Linux operating systems and are completely isolated from the internet for security reasons.

**Virtual machine flavor (VM flavor)**: a flavor defines the resources and configurations of a cloud computing environment. It specifies the compute, memory, and storage capacity that can be assigned to the virtual machine.
