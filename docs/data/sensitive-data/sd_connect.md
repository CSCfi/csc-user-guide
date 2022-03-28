
# SD Connect (Sensitive Data Connect)

SD Connect is a web-user interface that allows you to encrypt and upload sensitive data to CSC from your web browser. You can compare these services to a virtual hard drive that you can use to store your research data in the cloud securely. No specific technical expertise is required to use the service. SD Connect is designed to store and easily share sensitive data, providing a secure workspace for collaborative research projects. All the data stored in SD Connect can be accessed via SD Desktop for data analysis if encrypted with the Sensitive Data services public encryption key (default data upload in SD Connect).

In the following user guide, you can learn how to:

* apply for service access;
* encrypted and upload sensitive data via a web browser using SD Connect;
* encrypted and upload sensitive data programmatically;
* download and decrypt data using the Crypt4gh application.


## Key features

* Accessible via web browser from your computer (Mac, Linux, or Windows) and from any location (no need to install specific programs or use a VPN).

* Only your colleagues (or CSC project members) can access encrypted files stored in the same CSC project. 

* Data upload and automated encryption via drag-drop using web browser (less than 100 GB, larger datasets can be uploaded programmatically).

* Can be used to store any file type: text files, images, audio files, video, and genetic data (default space 10 TB, additional space required contact servicedesk@csc.fi). Each files, folder or bucket can be defined with specific tags. By default, a project can store up to 10 TiB of data.

* Facilitates secure data sharing (via URL) with other CSC projects.

* Data stored in SD Connect can be accessed via SD Desktop for data analysis (if they are encrypted using the Sensitive Data services public encryption key, the default option during data upload via SD Connect).


* **Limitations**:

Data (sensitive or non-sensitive, e.g. scripts) stored in SD Connect/ Allas must be encrypted. Files and folders are stored in buckets: this is the technical name for the main folder in which all the files (also called objects) are located in SD Connect. Files stored in SD Connect/Allas can be directly analysed in read-only mode from SD desktop, but they can not be directly edited unless they are copied inside the virtual Desktop. 


## Before you start

* According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data must be encrypted when uploaded or stored in CSC services for sensitive data. This paragraph provides instructions on encrypting a copy of your data with SD Connect or with a specific application called Crypt4GH. 
    
* SD Connect facilitates working with sensitive data, and it is a user interface for Allas, CSC cloud storage solution. By default, a project can store up to 10 TiB of data. The storage space remains available as long as the CSC project is active. CSC does not make backups of the data in SD Connect. You need to **make your own backups** of important datasets.

     
!!! note  
    SD Connect and SD Desktop have not yet been security audited. Because of that, users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***


## Service access 

To access SD Desktop go to [MyCSC](https://my.csc.fi) and:

* set up [a CSC account](../../accounts/how-to-create-new-user-account.md);
* [join](../../accounts/how-to-add-members-to-project.md) or set up [a CSC project](../../accounts/how-to-create-new-project.md);
* fill in the [description of data processing activities](../../accounts/when-your-project-handles-personal-data.md) form;
* add [service access to Allas](../../accounts/how-to-add-service-access-for-project.md);


For specific guidance regarding these steps, check the [Accounts](../../accounts/index.md) paragraph at the beginning of this user guide.


## Authentication

Login to SD Connect is currently possible only with CSC credentials and  Haka (a user identity federation system) at:

   * [https://sd-connect.csc.fi/](https://sd-connect.csc.fi) 

The interface is compatible with all modern web browsers. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925767-e4fae580-d993-11eb-9fd4-12147dcb956d.png">

<img width="960" alt="SD-Connect-0" src="https://user-images.githubusercontent.com/83574067/124901836-0b033400-dfeb-11eb-96d3-e5416f48f299.png">

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">



## User Interface pages

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/CMMwzl82dBI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Once you log in to SD Connect, you can access three main pages: 

* the default **Browser** page, where are listed the buckets (or main folders) in which your encrypted files are stored;
* the **Shared** page, where you can manage shared buckets;
* the **User information** page, where you can visualise the resources consumed by your CSC project and the Project Identifier.


### Browser page

In this view, you can :

* see all **the buckets available in your CSC project**, where you can store encrypted data. The buckets can be created, downloaded, deleted or shared using the appropriate icons. Note: SD Connect displays all the data uploaded in Allas using CSC interfaces for non-sensitive data management. 
   
*  **list and select your CSC project** from the drop-down menu bar (top left corner) to visualize buckets belonging to a specific CSC project;

*  open any bucket (double click) and view its content (uploaded files or folders). Any file can be downloaded or shared using the download link. From this view, you can also download the entire bucket, delete files or upload new files and folders;


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925795-ed532080-d993-11eb-8763-f11c975016e6.png">

![SD Connect Image 1](https://user-images.githubusercontent.com/83574067/149062070-7541673f-9fc1-445a-a790-80aa5f296e0c.png)


* clicking on **edit**, you can type in and add **appropriate tags** to describe buckets or files. 

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925806-efb57a80-d993-11eb-8f63-622833e958ef.png">

![SD Connect image 2](https://user-images.githubusercontent.com/83574067/149062085-a149fe12-0d9a-4dd2-87d4-d2e82ca2bbc4.png)


### User information page

In this view, you can:

* in **Currently Consumes** view statistics about the selected CSC project resource usage: billing unit consumption and the total project storage usage (default storage 10 TiB);

* in **Project usage**, you can view the SD Connect **Project Identifier**, an ID associated with your CSC project. This ID is required when you want to share containers with other CSC projects using the SD Connect user interface. It does not contain sensitive information. Thus it can be shared with your colleagues or collaborators via email.

* access the **Sharing API tokens** through which you can generate a temporary token (necessary for data upload programmatically, using Swift client).


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926085-37d49d00-d994-11eb-910f-4bcfa56c8589.png">

![SD-Connect-2](https://user-images.githubusercontent.com/83574067/124910227-098a3980-dff4-11eb-8029-57af3abc5cf4.png)

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

![1](https://user-images.githubusercontent.com/83574067/149009891-a049a79d-b66a-45c5-96a1-e0ea85617b0f.png)


![SD Connect 0](https://user-images.githubusercontent.com/83574067/158693924-21da1d2d-fddf-4ed2-980c-186c198c823d.png)

### Shared page


On the **Shared** page:

* in **Shared to the project**, you can view the **buckets that other CSC projects (belonging to your colleagues or collaborators) shared with you**. Next to the bucket name, under **Bucket Owner**,  it displays the ID associated with the CSC project to which the bucket belongs (also called SD Account). With a double click, you can access the bucket and view the content (if you have reading access) or add files to the container (if you have edits rights).

!!! note
    All the buckets listed here are owned by other users, which can decide when to revoke your access. You will not be able to access the file from SD Desktop until you make a copy of the bucket.


* in **Shared with the project**, you can view the buckets which  **you shared with other CSC projects**. In this case, you own the shared buckets, and you can decide when to revoke access. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926120-415e0500-d994-11eb-8455-9b8762c7a58b.png">
![sd-connect-4](https://user-images.githubusercontent.com/83574067/122786163-b22e5e80-d2bc-11eb-8c15-7585e656f0f2.png)
<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926131-4327c880-d994-11eb-81dd-c7b14d8e5f15.png">


## Introduction to data encryption compatible with Sensitive Data services

Files uploaded to Sensitive Sensitive data services need to be encrypted. Once uploaded, encrypted data are accessible from each service component, while the original files are always encrypted: during data storage or analysis. **Data encryption does not require technical expertise**. 

We integrated the encryption as an automated step in the SD Connect user interface, specifically for files less than 100 GB. All the data uploaded using SD Connect are automatically encrypted with the Sensitive Data services public encryption key. However, you can choose different options to encrypt your data for analysis or sharing. 

Briefly, the services use an encryption method called  _asymmetric encryption_,  based on two interlinked encryption keys:

   1) A **public key**is always used for data encryption, but it can not be used to decrypt the data. You can share your public key with others, e.g. your collaborators and they will then be able encrypt data with your public key. 

   2) A **secret key**, (also called a private key) is used to decrypt a file encrypted with the corresponding public key. This key is password protected and can not be shared with others. 


**When using SD Connect to upload  data to CSC, you have three possibilities for encryption:**

   1) You can simply upload the data using SD Connect, via your web browser, with the **default encryption options**. The files will be encrypted with the services encryption key and compatible with other services components. They will be decrypted in an automated manner when accessed using SD Desktop, but you will not be able to decrypt the files after download.  We are developing a new feature that will simplify the download option and will be soon available as part of the SD Connect user interface.
   
   2)  You can upload the data using SD Connect via web browser, and **add your public encryption key**. The files will be encrypted with the services encryption key by default, and they will be compatible with other services components. However, you will also be able to download and decrypt the data when necessary.
   
   3)  You can upload the data using SD Connect via your web-browser, and add **multiple encryption keys**. For example, your public encryption key and your collaborator's public encryption key. The files will be encrypted with the services encryption key by default; they will be compatible with other services components. However, you and your collaborator will also be able to download and decrypt the data when necessary.


   
This encryption method is  based on Crypt4GH. A tool initially designed to encrypt and share human genetic data according to the [Global Alliance for Genomics and Health](https://www.ga4gh.org/) (GA4GH) standard, which can be used to encrypt any type of data.
CSC has developed a simple application which will allow you to generate your encryption keys. In the following paragraph we will illustrate all the necessary steps to encryt yoru files using SD Connect or programmatically. 


## Sensitive data encryption and upload (default, less than 100 GB) 

SD Connect allows you to encrypt and upload files or folders directly from your web browser (file smaller than 100 GB). With the following workflow, the file will be **encrypted by default** with the Sensitive Data encryption key. In this manner,  encrypted files will be safely stored in SD Connect and can be directly analysed using other Sensitive Data services components (for example, in your virtual Desktop). However, you will not be yet able to decrypt the files after downloading without extra steps, which might require our support. We are developing a new feature that will simplify the download option.


The necessary steps are the following: 
 
1- To upload folders and files to SD Connect, use the **drag and drop function**.  The **upload** icon in the SD Connect browser window to select and upload files.


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

![1](https://user-images.githubusercontent.com/83574067/149009891-a049a79d-b66a-45c5-96a1-e0ea85617b0f.png)


2- You will be **redirected to a new page displaying the default encryption options**. 

3- Here, you can specify the bucket's name in which the data should be uploaded to. The user interface will automatically create a bucket named: upload-nnn (with a 13 digit number based on creation time). Note that **it is not possible to rename buckets**.


4- If you create a new bucket use the following **suggestions to name it**:

* Bucket **names must be unique** across all existing buckets in all projects in SD-Connect and Allas. If you can't create a new bucket, it's possible that some other project is already using the name you would like to use. To avoid this kind of situation, it is good practice to include some project-specific identifiers (e.g. project ID number or acronym) in the bucket names.  
    
* **Avoid using spaces and special characters in bucket names**. Preferred characters are Latin alphabets (a-z), numbers (0-9), dash (-), underscore (\_) and  dot (.). SD Connect can cope with other characters too, but they may cause problems in some other interfaces.

* All bucket **names are public**, so please do not include any confidential information in the bucket names


5- With the icon  **Click to add files that will be uploaded**  you will open a browser window in which you can select and add more files. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

![SD Connect final 1](https://user-images.githubusercontent.com/83574067/149011263-3225da97-b363-4c0f-9458-ccd1d09f293f.png)



6-  Next click on **Encrypt and upload**: each file will be automatically encrypted and uploaded to the bucket in SD Connect. 

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">
![3](https://user-images.githubusercontent.com/83574067/149011679-38799458-8e8d-4ddb-9a61-142a651b1fcb.png)



7- Once the process is completed, you can return to the SD Connect **browser** window. The encrypted files will show the extension *.c4gh*. 

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">
![6](https://user-images.githubusercontent.com/83574067/149012441-fc6ec48a-3d87-4cc2-bdd8-5e44e6c3cfd6.png)

## Sensitive data encryption and upload with multiple encryption keys (less than 100 GB) 

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/T4LRJw7HTro" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Using SD Connect user interface, you can encrypt your files with multiple encryption keys simultaneously. 

Below, we will illustrate how to generate your encryption key pair using a simple application called Crypt4GH and how the public encryption key can then be used to encrypt files via your web-browser, using SD Connect. 


### Step 1: Install the Crypt4GH application

CSC has developed a simple application which will allow you to generate your encryption keys and to decrypt data using when necessary. 
Download the version specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases):  

  - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.2.0/crypt4gh-gui-python3.8-linux-amd64.zip)
   - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.2.0/crypt4gh-gui-python3.8-macos-amd64.zip)
   - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.2.0/crypt4gh-gui-python3.8-windows-amd64.zip)

Please check that the tool has been digitally signed by CSC - IT Center for Science. After the download, you can find the Crypt4GH application in your downloads folder.

![Crypt4GH in downloads folder](./images/SDEnScreenShot_1.png).

When you open the application for the first time you might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and then click on _Run anyway_.

![Crypt4GH security warning](./images/SDEnScreenShot_2.png)

### Step 2: Generate your encryption keys

1. Open the application and click on _Generate Keys_ (on the top right corner).
1. The tool will open a new window and ask you to insert a password (_Private Key Passphrase_). This password will be associated with your secrete key. Please, use a strong password!
1. When you click on _OK_, the tool will generate a key pair consisting of a secrate key (your username_crypt4gh.key) and a public key (your username_crypt4gh.pub).
1. The keys/file names will be displayed in the Activity Log with the following message:

```
Key pair has been generated, your private key will be auto-loaded the next time you launch this tool:
Private key: username_crypt4gh.key
Public key: username_crypt4gh.pub
All the fields must be filled before file encryption will be started
```


The keys will be generated and saved to the same folder in which the application resides.

!!! Note
    If you lose or forget your private key, or the password to it, you will be unable to decrypt the files. Do not share your private key or your password.
    You need to create your keys only once and use them for all your encryption needs but you can of course choose to generate separate keys for encryption as you       wish.

![Crypt4GH key generation](./images/SDEnScreenshot_4.png)


### Step 3: Upload your data to SD Connect



### Step 4:   data to SD Connect



    
