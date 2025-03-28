[Table of contents of user guide](sd-services-toc.md) 

# Using SD Connect to receive sensitive research data

This document provides instructions of how a research group can use SD Connect to receive **sensitive data** from external 
data provider like a sequencing center. The procedure presented here is applicable in cases where the data will analyzed in
SD Desktop or in a computer that has internet connection.

In some sensitive data environments internet connection is not available. In those cases, please check the alternative 
approach, defined in:

   * [Using Allas to receive sensitive research data](./sequencing_center_tutorial.md)


## SD Connect

SD Connect is part of the CSC sensitive data services that provide free-of-charge sensitive data processing environment for 
academic research projects at Finnish universities and research institutes. SD Connect adds an automatic encryption layer to the Allas object storage system of CSC, so that it can be used for securely storing sensitive data. SD Connect can be used for storing any kind of sensitive research data during the active working phase of a research project. 
SD Connect is however not intended for data archiving. You must remove your data from SD Connect when the research project ends.

There is no automatic backup processes in SD Connect. In technical level SD Connect is very reliable and fault-tolerant, 
but if you, or some of your project members, remove or overwrite some data in SD Connect, 
it is permanently lost. Thus, you might consider making a backup copy of your data to some other location.

Please check the [SD Connect documentation](./sd_connect.md) for more details about SD Connect.


## 1. Obtaining a storage space in SD Connect

If you are already using SD Connect service, you can skip this chapter and start from chapter 2.
Otherwise, do following steps to get access to SD Connect.


### 1.1. Create a user account

If you are not yet CSC customer, register yourself to CSC. You can do these steps in the 
CSC’s customer portal [MyCSC](https://my.csc.fi). 

Create a CSC account by logging in to MyCSC with Haka or Virtu. Remember to activate multi factor 
authentication for your CSC account in order to be able to use SD Connect-


### 1.2. Create or join a project

In addition to CSC user account, users must either join an existing CSC computing project 
or set up a new computing project. You can use the same project to access other 
CSC services too like SD Desktop, Puhti, or Allas.

If you are eligible to act as a [project manager](https://research.csc.fi/prerequisites-for-a-project-manager), you can create a new CSC project in MyCSC and apply access to SD Connect.
Select 'Academic' as the project type.  As a project manager, you can invite other users as members to your project. 

If you wish to be joined to an existing project, please ask the project manager to add your CSC user account to the 
project member list.

### 1.3. Add SD Connect access for your project

Add _SD Connect_ service to your project in MyCSC. Only the project manager can add services. 
After you have added SD Connect, to the project, the other project members need to login to 
MyCSC and approve the terms of use for the service before getting access to SD Connect. 

After these steps, your project has 10 TB storage space available in SD Connect. 
Please [contact CSC Service Desk](../../support/contact.md) if you need more storage space. 


## 2. Creating a shared folder

### 2.1. Creating a new root folder in SD Connect

Once the service is enabled, you can login to [SD Connect interface](https://sd-connect.csc.fi). 
After connecting, check that **Current project** setting refers to the CSC project 
that you want to use. After that you can click the **Create folder** button to 
create a new folder to be shared with the data provider.

Avoid using spaces (use _ instead) and special characters in the folder names as they may cause problems in some cases. 
Further, add some project specific feature, like project acronym, to the name, as the root folder needs to have an unique name 
among all root folders of all SD Connect and Allas projects.

### 2.2 Sharing the folder

For sharing you need to know the _Sharing ID_ string of the data producer. You should request this 32 characters long 
random string form the data producer by email. 

Do to the sharing, go to the folder list in SD Connect and press the share icon of the folder you wish to share.
Then copy the project ID to the first field of the sharing tool and select **Collaborate** as the sharing permission type.

Now sharing is done and you can send the name of the shared bucket to the data producer by email.


### 2.3 Revoke bucket sharing after data transport

Moving large datasets (several terabytes) of data to SD Connect can take a long time. 
Once the producer tells that all data has been imported to the shared folder in Allas, you remove the external 
access rights in SD Connect interface. Click the _share_ icon of the shared 
folder and press **Delete** next to the project ID of the data producer.


## 3. Using encrypted data 

By default data stored to SD Connect is accessible only to the members of the CSC project. However project members can
share the folder to other CSC projects.

The project members can download the data to their own computers using the SD Connect WWW interface
that automatically decrypts the data after downloading.

The data can be accessed in [SD Desktop](https://sd-desktop.csc.fi) too, using the _Data Gateway_ 
tool.

In Linux and Mac computers, you can install a local copy of _allas-cli-utils_ tools that provides command line 
tools to download (_a-get_) and upload ( a-put --sdc ) data from and to SD Connect.

* [Using SD Connect data with a-commands](sd-connect-and-a-commands.md)


