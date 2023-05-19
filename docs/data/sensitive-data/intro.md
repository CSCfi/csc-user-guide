# Sensitive Data (SD) Services for research

## Introduction 

Sensitive Data (SD) services for research provide CSC customers with a secure workspace accessible via a web browser that can be used for processing sensitive data according to CSC's General Terms of Use.

Sensitive Data services for research consist of five components:

[![SD-service-overview](images/introduction/icons.png)](images/introduction/icons.png)

* Sensitive Data Connect: a user interface for importing and storing sensitive data to CSC's cloud storage solution (Allas). SD Connect also facilitates sharing or transferring encrypted sensitive data during the active phases of research projects ([service description on research.csc.fi](https://research.csc.fi/-/sd-connect)). 

* Sensitive Data Desktop: a user interface that provides access to a secure virtual computer (or virtual Desktop). It enables secure computation and analysis of sensitive data. 

* Sensitive Data Submit and Federated EGA (*pilot phase*): allows publishing of sensitive and biomedical data under controlled access ([service description research.csc.fi](https://research.csc.fi/-/fega)). 

* Sensitive Data Apply (*pilot phase*): promotes data reuse allowing data owners to manage access to published datasets via a simple user interface.

These services are suitable for processing **sensitive research data**. In addition, a **restricted version of SD Desktop is provided for processing register-based research under the Finnish Act on Secondary Use of Health and Social Data**. The regulation applies when health and social information is collected and saved in a register, for example, during examination in health care services or while applying for social benefits, and in a second moment, the original information is used for a different purpose, for example, research. In this case, the processing is possible only in a certified computing environment in compliance with Act on the Secondary Use and the Findata Authority's Regulation. The limitations are outlined in the SD Desktop ([service description on research.csc.fi](https://research.csc.fi/-/sd-desktop)).

In this manual, you can find an overview of each service's key features and limitations, step-by-step instructions and video tutorials (specific sections are marked as *advanced* if technical expertise is required), and quick solutions in the troubleshooting table. 

!!! Note
    Sensitive data is only accessible with appropriate authorization, rights, or permission. With SD services, access is always managed by the data controller via specific service components in compliance with the GDPR and national regulations. For example, you can directly manage research data access, uploads, or data export using SD Connect and SD Desktop. In contrast, access to register data via SD Desktop is operated by CSC's helpdesk, based on the data permit issued by the Findata Authority, and in compliance with Finnish regulations. 
    
The following section of this manual provides an overview of permission management via SD services based on the data type and legal bases for data processing and a summary of the main documentation that should be considered. 



## Useful terminology: services and technical aspects

**Allas**: CSC's cloud storage service. SD Connect is an interface that facilitates sensitive data encryption and storage in Allas. Users can also access Allas programmatically with interfaces for non-sensitive data.

**Billing units**: billing units are used to monitor the resource. SD Connect and SD Desktop usage consume billing units. 

**Bucket/Container**: These terms refer to the main folder (technically called root folder) where encrypted files are stored in SD Connect/Allas. The bucket/container name is visible on the internet. You can have multiple buckets in the same project (up to 1000), but each bucket must have a unique name throughout the storage system (including other projects). By default, the data in a bucket is accessible just to the project members. However, you can share and grant access to other CSC projects or users with SD Connect.

**CSC Project**: using CSC services is based on projects: all your data in CSC belong to a project. Each project has a primary user, the CSC project manager, who can add members and manages access to the services. A project manager is responsible for the project's activities and acts as the data controller (or academic organization) representative. They, for example, need to describe which type of sensitive data the project is processing.

**Disk quota**:  storage space available to CSC's services users. SD Connect has a default quota of 10 TB. You can apply for more storage space by writing to servicedesk@csc.fi. 


**Multi-factor Authentication**: When you log in to the SD Desktop service, you must undergo an extra verification step next to provide a username and password. In this way, your account is more secure. The extra verification step is called: "Two-Step Verification" or "Multifactor Authentication", because you are proving your identity via a different method. In this case, you need to type in a one-time code (6 digits) obtained by opening a mobile app. The code is unique and valid for a limited amount of time.

**Object**: the technical name for a file stored in a cloud object storage like Allas (or uploaded to CSC via SD Connect). This definition underlines that files stored in SD Connect /  Allas can not be directly modified unless transferred or copied into a computing environment. Still, they can be accessed in read-only mode from a cloud computing environment (e.g. SD Desktop). 

**Project Identifier**: a synonym of CSC Project ID when using the command-line tool. The SD Connect user interface is displayed under User Information> Project usage and displayed as a series of 32 numbers and letters: e.g. AUTH_3a66dbf90b2940dc9c651362af595b23.


**Virtual machine (VM) or virtual desktop**: a virtual computing environment (or virtual computer) that works as a physical computer. It has a processor, memory, and operating system but exists only as a code or a partition of the host computer in CSC's data center. The virtual machines used for Sensitive Data services are entirely isolated from the internet for security reasons.

**Virtual machine flavor (VM flavor) or pre-built desktop option**: a flavor defines the resources and configurations of a cloud computing environment. It specifies the computing, memory, and storage capacity that can be assigned to the virtual machine.


## Useful terminology: data protection

**Data Controller and Data Processor** According to the GDPR, a data controller is an individual or organization that determines the purposes and means of processing sensitive personal data, and it is usually an academic organization. On the other hand, a data processor is an individual or organization that processes personal data on the controller's behalf, for example, an IT service provider, in this case, CSC.


**Data Processing Agreement (DPA)**: a data processing agreement (DPA) is a contract between the Data Controller and the Data Processor. It regulates the particularities of data processing – such as its scope and purpose – as well as the relationship between the controller and the processor. For more information, see the section [when your project handles personal data](../../accounts/when-your-project-handles-personal-data.md#data-processing-agreement) at the beginning of this user guide and [CSC General terms of use](https://research.csc.fi/general-terms-of-use) and [CSC Data Processing Agreement](https://research.csc.fi/data-processing-agreement) on research.csc.fi. 


**Data Protection Impact Assessment (DPIA)**: A Data Protection Impact Assessment (DPIA) is required under the GDPR for operations that are 'likely to result in a high risk to the rights and freedoms of natural persons'. More information is provided [here](https://tietosuoja.fi/en/list-of-processing-operations-which-require-dpia) by the Finnish Office of the Data Protection Ombudsman and specific support by your home organization's legal office. 


**Sensitive Data**: Sensitive data is data that needs to be protected against unauthorized access. Data protection may be required due to legal or ethical reasons, personal privacy, and proprietary considerations. Sensitive data can include for example:
* Personal sensitive data (e.g. health, genetic and personal information, racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health, data concerning a natural person's sex life or sexual orientation, data relating to criminal convictions and offenses or related security measures, data that may identify a person)
* Ecological data (e.g. location of endangered species or other conservation efforts)
* Confidential data (e.g. trade secrets)
* Data that is otherwise deemed sensitive.
