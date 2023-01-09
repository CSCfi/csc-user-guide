
# Sensitive Data services for research


## Introduction to the user guide

In this user guide, you can find:

* an overview and **key features** of each service;

* step-by-step instructions on accessing and setting up the services; technical knowledge or expertise are not required to use the services.  Specific paragraphs are marked as *advanced* if technical and coding skills are necessary;

* quick technical suggestions in the **troubleshooting table**;

* video tutorials helpful to get started. 

For general information, see the [Sensitive Data (SD) services webpage](https://research.csc.fi/sensitive-data-services-for-research), [FAQs](../../faq/index.md#sensitive-data-services-for-research), and services descriptions in [CSC's service catalog](https://research.csc.fi/service-catalog).

You can also learn more from example cases for:

* [sensitive data analysis](https://research.csc.fi/example-case-5-sensitive-data-analysis);

* [sensitive data storage, collection and transfer](https://research.csc.fi/example-case-6-sensitive-data-storage-and-transfer);

* [sensitive data reuse](https://research.csc.fi/example-case-7-sensitive-data-reuse).

<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/U74CvhPR16E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Introduction to the services


Sensitive Data (SD) services for research provide CSC customers a secure workspace, accessible via a web browser, that can be used for processing sensitive data according to [CSC General terms of use ](https://research.csc.fi/general-terms-of-use).

Sensitive Data services for research consist of five components:

* Sensitive Data Connect ([service description](https://research.csc.fi/-/sd-connect)): a user interface for importing and storing sensitive data to CSC's cloud storage solution (Allas). SD Connect also facilitates sharing or transferring encrypted sensitive data during the active phases of research projects. 

* Sensitive Data Desktop ([service description](https://research.csc.fi/-/sd-desktop)): a user interface that provides access to a secure virtual computer (or virtual Desktop). It enables secure computation and analysis of sensitive data. In addition, a restricted version of SD Desktop is provided for processing registry data (secondary use of health and social data). The limitations are described in a separate user guide (see: SD Desktop for secondary use).

* Sensitive Data Submit and Federated EGA ([service description](https://research.csc.fi/-/fega)) (pilot phase): allow publishing of sensitive and biomedical data under controlled access. 

* Sensitive Data Apply (pilot phase): promotes data reuse allowing data owners to manage access to published datasets via a simple user interface.

<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/YcgeuatWf9g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



## Legal agreements

The General Data Protection Regulation and Finnish national laws regulate sensitive personal data processing. To comply with these regulations, specific data processing and framework agreements between the Data Controllers (academic organization) and CSC (as the Data Processor) must be in place. 

For further information, see also:

* [CSC General terms of use](https://research.csc.fi/general-terms-of-use);
* [CSC Data Processing Agreement](https://research.csc.fi/data-processing-agreement);
* [Definition of sensitive data](https://research.csc.fi/definition-of-sensitive-data);
* [Technical and organizational security measures for the protection of sensitive data in CSC Sensitive Data service](./technical-organisational-sec-measures.pdf).

Moreover, when creating a CSC project using the MyCSC portal, you are guided to the "Description of processing activities" form, where you describe the type of data you are processing. 

You can then download these documents and share them with the legal services in your organisation or the Data Controller's representative. If you have any questions or additional legal agreements are needed between your organisation and CSC, contact us at servicedesk@csc.fi (email subject: Sensitive Data).


<iframe width="280" height="155"srcdoc="https://www.youtube.com/embed/1LHpDiap5Lo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Useful terminology

**Allas**: a cloud storage service of CSC. SD Connect is an interface that facilitates sensitive data encryption and storage in Allas. Users can also access Allas programmatically with interfaces for non-sensitive data.

**Billing units**: billing units are used to monitor the resource (when CSC services are free-of-charge or when the user pays to use the services).

**Bucket/Container**: these two terms refer to the main folder (technically called root folder) where data are stored in SD Connect/Allas. The bucket/container name is visible on the internet. You can have multiple buckets in the same project (up to 1000), but each bucket must have a unique name throughout the whole storage system (including other projects). By default, the data in a bucket is accessible just to the project members. However, you can share and grant access to other CSC projects or users with SD Connect.

**CSC Project**: using CSC services is based on projects: all your data in CSC belong inside a project. You can be a project member in one or multiple projects. Each project has a primary user, the CSC project manager, who can add members and services to the project. A project manager is responsible for the activities of the project. They, for example, need to describe which type of sensitive data the project is processing.

**Disk quota**: this is a limited set to control the storage space available to CSC services users. SD Connect has a default quota of 10 TB. You can apply for more writing at servicedesk@csc.fi. 

**Data Processing Agreement (DPA)**: a data processing agreement (DPA) is a contract between the Data Controller and the Data Processor. It regulates the particularities of data processing – such as its scope and purpose – as well as the relationship between the controller and the processor: [CSC General terms of use](https://research.csc.fi/general-terms-of-use) and [CSC Data Processing Agreement](https://research.csc.fi/data-processing-agreement).

**Multi-factor Authentication**: When you log in to the SD Desktop service, you must undergo an extra verification step to authenticate by providing a username and password. In this way, your account is more secure. The extra verification step is called:"Two-Step Verification" or "Multifactor Authentication", because you are proving your identity via a different method. In this case, you need to type in a one-time code (6-digits) obtained by opening a mobile app on your phone. The code is unique and valid for a limited amount of time.

**Object**: technical name for a file stored in a cloud object storage like Allas (or uploaded to CSC via SD Connect). This definition underlines that files stored in SD Connect /  Allas can not be directly modified unless transferred or copied into a computing environment. Still, they can be accessed in read-only mode from a cloud computing environment (e.g. SD Desktop). 

**Project Identifier**: a synonym of CSC Project ID when using the command-line tool. In the SD Connect user interface is displayed under User Information> Project usage and displayed as a series of 32 numbers and letters: e.g. AUTH_3a66dbf90b2940dc9c651362af595b23.

**Virtual machine (VM)**: a virtual computing environment (or virtual computer) that works as an actual physical computer. It has a processor, memory, and operating system, but it exists only as a code or a partition of the host computer in CSC’s data center. The VMs used for the Sensitive Data services are entirely isolated from the internet for security reasons.

**Virtual machine flavor (VM flavor)**: a flavor defines the resources and configurations of a cloud computing environment. It specifies the compute, memory, and storage capacity that can be assigned to the virtual machine.



# Applying for SD services access

Sensitive Data Services are available for all CSC customers. To access CSC's services for sensitive data using [MyCSC](https://my.csc.fi) portal:

   1. Create a user account.

   3. Create or join a CSC project and add project members.

   4. Fill in the Description of processing activities form and accepct CSC's Data processing agreement.
    
   5. Each project member needs to **add service access to Allas and  SD Desktop**.

   6. Activate the additional security verification (or Multi-factor Authentication) on your account by **scanning the QR code with an application** (e.g. Google Authenticator).

   7. Apply for billing units or disk quota.

For video tutorials and guidance regarding these steps, check the [Accounts](../../accounts/index.md) paragraph at the beginning of this user guide.


!!! Note
    Applying access to the SD Desktop environment for secondary use differs from the abovementioned process. See instructions in [the specific user guide SD Desktop for secondary use](./sd-desktop-audited.md#service-access).

Once you have completed these steps, you can log in to SD services with identity federation systems (Haka, Virtu, CSC Login, or LSLogin) at:

   * [https://sd-connect.csc.fi](https://sd-connect.csc.fi) 
   * [https://sd-desktop.csc.fi](https://sd-desktop.csc.fi)

with any modern web-browser.

!!! Note
    LSLogin (LifeScience login, previously known as ELIXIR login) is available only after linking your CSC account to your LifeScience account (under your profile in MyCSC).
  
