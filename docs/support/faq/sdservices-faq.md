# Sensitive Data (SD) Services for Research
   

#### Are CSC Sensitive Data services the right solution for my research project and how do I get started?


If you are new to CSC and the Sensitive Data (SD) services, we recommend contacting servicedesk@csc.fi (subject: SD services). We can arrange an online meeting to discuss your research project, introduce the available services, explain any current limitations and help you determine whether the services are suitable for your needs.

We can also provide the relevant documentation needed by your organization and data support personnel to assess whether the services meet your organization's security and privacy requirements.

Getting started depends on your use case. For most research projects, you simply need to create a CSC account and project before accessing the services. 

If you are working with register data under the Act on Secondary Use, contact us before planning for the data permit and we will guide you through the on boarding process. If you are planning to use Federated EGA (FEGA), a separate service agreement is required, and we can help you get started.



## Research data storage and analysis

#### Who can access my data and workspace?

You decide who can access your data. CSC provides the tools and services, while access rights are managed by you.

By default, all members of a CSC project have the same permissions. They can access, manage, share and analyze data via SD Connect and SD Desktop. The only exception is data export from the secure environment, which is restricted to authorized only to the CSC project manager,  usually the research group the Principal Investigator (PI) or designated project manager (postdoc, PhD student).

If needed, access rights can be further restricted. For example, some users can be granted read-only access or access only to specific datasets. If you would like to implement more detailed access controls, please contact the CSC Service Desk at servicedesk@csc.fi.


#### How can I share data with collaborators?

1. Share access to the entire project

You can invite your collaborators directly to your CSC project. Once they have joined the project, they can access, upload, download the project's data stored in SD Connect and analyse it in SD Desktop.

2. Share specific buckets or folders

If your collaborators already have a CSC account and their own CSC project, you can share data with them through SD Connect. Shared buckets can be used for:

Data transfer: collaborators can download the contents of a shared bucket or folder.
Collaboration: collaborators can upload, modify, and delete files within the shared folder.

Please note that sharing in SD Connect is managed at the bucket level. This means that you share an entire bucket or folder and all of its contents. Individual files cannot be shared separately.

3. Read-only access 

Collaborators can access shared data only for analysis within the secure computing environment without being able to export it. If you would like to enable this option, please contact us at servicedesk@csc.fi.


#### How much storage space is available in SD Connect and SD Desktop?

When you create a CSC account and project, you are allocated 10 TB of storage space in SD Connect. 

To analyze data in SD Desktop, the data must first be copied from SD Connect to the virtual desktop's storage volume. By default, an SD Desktop volume provides approximately 200 GB of storage space. Additional storage can be provided as long as the volume is empty and no sensitive data has been uploaded to it.

Please note: when your storage quota is full, you will no longer be able to upload files to SD Connect, and data exports from SD Desktop may fail without a clear error message. If the storage space allocated to an SD Desktop virtual machine becomes full, the virtual desktop may become unresponsive or unusable.

If you need additional storage, please contact servicedesk@csc.fi with the subject "SD Services". 


#### What software is available for data analysis and can I install additional software?

SD Desktop only provides only Linux Ubuntu22 computing environments with a limited amount of open-source software installed, including Libre Office (with LibreOffice Calc, a spreadsheet program similar to Microsoft Excel, and LibreOffice Writer,  a word processor similar to Microsoft Word), R Studio and Python. We are not providing proprietary software, but we could help you install on your private desktop an open-source version. 
For further information and for desktop customisation see: [Default programs available on SD Desktop](../../data/sensitive-data/sd-desktop-software.md).  
Don't hesitate to get in touch with us at servicedesk@csc.fi (subject SD services) for specific technical support.


#### What happens to my data when the CSC project expires or billing units end?

If your CSC project runs out of Billing Units, all the virtual desktop in your project will be automatically paused and become inaccessible. If the project is not renewed or additional Billing Units are not granted, the project will be closed after 60 days. Please note that all data stored in SD Connect and SD Desktop, including files, virtual desktops, and storage volumes, will be permanently deleted 90 days after the project is closed or expires.


#### Can I get root or sudo access in SD Desktop?

No. Your account has only normal user level privileges. Providing sudo rights to a user would compromise the security of you SD Desktop environment.

#### How does SD Desktop differ from ePouta?

SD Desktop is a web-user interface that allows you to connect to your virtual computing environment securely. CSC manages SD Desktop: we manage the connection, access, and security. SD Desktop is suitable for collaborative projects across Finnish organizations and provides the computational capability to research organizations that do not have an ePouta tenant.

ePouta is an infrastructure provided to research organizations, and the organization's own IT unit manages its access and network. ePouta works on extending an academic organization infrastructure and provides all the flexibility and requirements decided by the organization. 

#### How SD Connect differs from Allas and Allas UI?

SD Connect is a service for storing and sharing sensitive research data that uses Allas as the underlying storage platform. Allas is CSC's general purpose cloud storage service, 

The main difference is that SD Connect (user interface and command line tools) provides automated encryption, decryption and encryption key management, whereas Allas does not provide data encryption. 

#### Register data analysis under the Finnish Act on Secondary Use



#### How can I access and analyze data provided by Findata or a well-being county via SD Services?



#### Can I combine register data with my own data?



#### How do I export results and what happens when my permit expires?



#### How do I add project members?


