
# Sensitive Data services for research


## Introduction to the user guide

In this user guide, you can find:

* an overview and **key features** of each service;

* step-by-step instructions on accessing and setting up the services; technical knowledge or expertise are not required to use the services.  Specific paragraphs are marked as *advanced* if technical and coding skills are necessary;

* quick technical suggestions in the **troubleshooting table**;

* video tutorials helpful to get started. 

For general information, see:
[Sensitive Data services webpage](https://research.csc.fi/sensitive-data-services-for-research), general [FAQs](../../support/faq/index.md#sensitive-data-services-for-research), services descriptions in [CSC's service catalog](https://research.csc.fi/service-catalog).


## Introduction to the services


Sensitive Data services for research provide CSC customers a secure workspace, accessible via a web browser, that can be used for processing sensitive data according to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use).

Sensitive Data services for research consist of five components:

* Sensitive Data Connect ([service description](https://research.csc.fi/-/sd-connect)): a user interface for storing and sharing encrypted sensitive data during the active phases of research projects. 

* Sensitive Data Desktop ([service description](https://research.csc.fi/-/sd-desktop)): a user interface that provides access to a secure virtual computer (or virtual Desktop). This enables secure computation and analysis of sensitive data. A restricted version of SD Desktop is provided for the processing registry data (secondary use of health and social data). The limitations are described in a separate user guide (see: SD Desktop for secondary use).

* Sensitive Data Submit and Federated EGA ([service description](https://research.csc.fi/-/fega)) (pilot phase): allow publishing of sensitive and biomedical data under controlled access. 

* Sensitive Data Apply (pilot phase): promotes data reuse allowing data owners to manage access to published datasets via a simple user interface.


## Legal agreements

The General Data Protection Regulation and Finnish national laws regulate sensitive personal data processing.
 To comply with these regulations, specific data processing and framework agreements between the Data Controllers (academic organization) and CSC (as the Data Processor) must be in place.
For further information see also: [CSC General terms of use](https://research.csc.fi/general-terms-of-use) and [CSC Data Processing Agreement](https://research.csc.fi/data-processing-agreement) and [Definition of sensitive data](https://research.csc.fi/definition-of-sensitive-data).

To facilitate this process, when you create a new CSC project using the MyCSC portal, you are guided to  CSC's Data Processing Agreement (DPA) and to d the "Description of processing activities" form, where you describe the type of data you are processing. You can then download these documents and **share them with the legal services in your organisation** or the Data Controller's legal representative. If you have any questions or additional legal agreements are needed between your organisation and CSC, contact us at servicedesk@csc.fi (email subject: Sensitive Data).

In case you need to draft a **Data Protection Impact Assessment (DPIA)** (to identify and minimise the data protection risks of a projec) you can find the technical and organizational security measures for the protection of sensitive data in CSC Sensitive Data service available for download [here](./technical-organisational-sec-measures.pdf).

<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/1LHpDiap5Lo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Getting access

Sensitive Data Services are available for all CSC customers. To access CSC's services for sensitive data using [MyCSC](https://my.csc.fi) portal:

   1. Create a **user account**.

   3. Create or join a **CSC project** and add project members.

   4. Fill in the **Description of processing activities form** and agree with CSC **Data Processing Agreement**.
    
   5. **Each project member** needs to **add service access to SD Desktop and to Allas** (in case you want to use SD Connect, a user interface for the CSC cloud storage solution called Allas).
   
   6. Activate Multi-factor Authentication.

   7. Apply for billing units or disk quota.

For specific guidance regarding these steps, check the [Accounts](../../accounts/index.md) paragraph at the beginning of this user guide.

Applying access to the audited SD Desktop environment differs from the abovementioned process. See instructions in [the user guide](./sd-desktop-audited.md#service-access).


## Useful terminology

**Allas**: a cloud storage service of CSC. SD Connect is an interface that facilitates sensitive data encryption and storage in Allas. Users can also access Allas programmatically with interfaces for non-sensitive data.

**Billing units**: billing units are used to monitor the resource when CSC services can are free-of-charge or when the user pays the use of the services.

**Bucket/Container**: these two terms refer to the main folder (technically called root folder) where data are stored in SD Connect/Allas. The bucket/container name is visible on the internet. You can have multiple buckets in the same project (up to 1000), but each bucket must have a unique name throughout the whole storage system (including other projects). By default, the data in a bucket is accessible just to the project members. However, you can share and grant access to other CSC projects or users with SD Connect.

**CSC Project**: using CSC services is based on projects: all your data in CSC belong inside a project. You can be a project member in one or multiple projects. Each project has a primary user, the CCS project manager, who can add members and services to the project. A project manager is responsible for the activities of the project. They, for example, need to describe which type of sensitive data the project is processing.

**Disk quota**: this is a limited set to control the storage space available to CSC services users. SD Connect has a default quota of 10 TB. You can apply for more writing at servicedesk@csc.fi. 

**Data Processing Agreement (DPA)**: a data processing agreement (DPA) is a contract between the Data Controller and the Data Processor. It regulates the particularities of data processing – such as its scope and purpose – as well as the relationship between the controller and the processor: [CSC General terms of use](https://research.csc.fi/general-terms-of-use) and [CSC Data Processing Agreement](https://research.csc.fi/data-processing-agreement).

**Multi-factor Authentication**: When you log in to the SD Desktop service, you need to go through an extra verification step next to authenticate by providing a username and password. In this way, your account is more secure. The extra verification step is called:"Two-Step Verification" or "Multifactor Authentication", because you are proving your identity via a different method. In this case, you need to type in a one-time code (6-digits) obtained by opening a mobile app on your phone. The code is unique and valid for a limited amount of time. 

**Object**: is the technical name for a file stored in a cloud object storage like Allas (or uploaded to CSC via SD Connect). This definition underlines that files stored in SD Connect /  Allas can not be directly modified unless transferred or copied into a computing environment. Still, they can be accessed in read-only mode from a cloud computing environment (e.g. SD Desktop). 

**Project Identifier**: it is a synonym of CSC Project ID when using the command-line tool. In the SD Connect user interface is displayed under User Information> Project usage and displayed as a series of 32 numbers and letters: e.g. AUTH_3a66dbf90b2940dc9c651362af595b23.

**Virtual machine (VM)**: is a virtual computing environment (or virtual computer) that works as an actual physical computer. It has a processor, memory, and operating system, but it exists only as a code or a partition of the host computer in CSC’s data center. The VMs used for the Sensitive Data services are entirely isolated from the internet for security reasons.

**Virtual machine flavor (VM flavor)**: a flavor defines the resources and configurations of a cloud computing environment. It specifies the compute, memory, and storage capacity that can be assigned to the virtual machine.
