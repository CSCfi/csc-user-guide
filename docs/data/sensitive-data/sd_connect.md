
# SD Connect (Sensitive Data Connect)

## Before you start

* According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always needs to be encrypted when uploaded or stored in CSC services for sentive data. Check the [encryption paragraph](./data_ecryption.md) for more information about encryption with Crypt4GH. 
    
* SD Connect is based on the [Allas](./data/allas/overview.md) cloud storage service. SD Connect is a user interface that facilitate working with sensitive data. 
The genral rules and methods of usage are the same as in Allas. By default a project can strore up to 10 TiB of data. The storage space remains availabe as long as the project is active. You should not consider SD Connect as a permanent data storage. Instead, you should have a plan about what will happen to the data when proect is closed. 
CSC does not make backups of the data in SD Connect. You need to **make your own backups** of important datasets. 
     
!!! note  
    SD Connect and SD Desktop has not yeat been security audited. Because of that users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***


## Login 

To access SD Connect you need:

* **a CSC account**
* **a CSC project**
* **Service access to Allas** (CSC cloud storage solution)

Login to SD Connect is currently possible only with Haka (an user identity federation systems) at https://sd-connect.csc.fi/ using any modern web browser. If you do not have an Haka account and can not access the user interface, you can still upload data programmatically, directly into Allas (see the end of this paragraph). 


<img width="854" alt="SD-Connect-0" src="https://user-images.githubusercontent.com/83574067/122104560-73ae2500-ce20-11eb-9ca8-eaa0e3e3f199.png">



## User Interface

Once you Login in SD Connect you access the default front-page: **Browser**.

In this page you can :

* view all **the  buckets available in your CSC project**, in which you can store encrypted sensitive data. The bukects can be created, downloaded, deleted or shared, using the appropriate icons;
   
*  **list and select your CSC project** from the drop down menu bar (top left corner) to visualize buckets belonging to a specific CSC project;

*  open any bucket (double click) and view its content (uploaded files or folders). Any file can be downloaded or shared using the download link. From this view, you can also download the entire bucket, delete file or upload new files and folders.



<img width="956" alt="SD-Connect-1copy" src="https://user-images.githubusercontent.com/83574067/122087350-4906a100-ce0d-11eb-91ac-c39df3dedb23.png">





In the  **User information** page you can:

* in **Currently Consumes** view statistics about the selected CSC project resource usage: billing unit consumption and the total project storage usage (defoult storage 10 TiB);

* in **Project usage** you can view the **SD Connect Account, an ID associated your CSC project**. This ID is required when you want to share containers with other CSC projects using SD Connect user interface. It does not containe sensitive information, thus it can be sharer with your colleagues or collaborators via email.

* access the **Token icon** through which you can generate a temporary token (necessary for data upload programmatically, using Swift client. For more info check below).



<img width="925" alt="SD-Connect-2" src="https://user-images.githubusercontent.com/83574067/122105837-e5d33980-ce21-11eb-8fa9-988ee305a9d3.png">




In the **Shared** page:

* in **Shared to the project** you can view the **bukets that other CSC projects (belonging to your colleagues or collaborators) shared with you**. Next to the bucket name, under **Containeor Owner**,  it is displayed the ID associated to CSC project to which the bucket belongs to (also called SD Account). With double click you can access the bucket and view the content (if you have reading access) or add files to the container (if you have edits rights). 

!!! note 
    All the container listed here are own by another users that can decide when revoke your access. You will not be able to access the file from SD Dekstop untill you make a copy of the container. 

* in **Shared with the project** you can view the bukets which  **you shared with other CSC projects**. In this case you own the shared bukets and you can decide when revoke access. 



<img width="959" alt="SD-Connect-3" src="https://user-images.githubusercontent.com/83574067/122087777-c7fbd980-ce0d-11eb-9ccb-c98fdb897e02.png">



## Data encryption with CSC-sd-encryption key and Crypt4GH GUI for SDS.

With the following workflow, you can use a graphical user interface (Crypt4sds GUI) developed by CSC to **encrypt and import a copy of your data to SD Desktop**.  

!!! note
    As this is a simplified workflow, it is desigend to allow **easy and safe encryption and automated decription only using the Sensitive Data Services**. Using this workflow does not allow you to include your encryption keys. Thus, you will not be able to descrypt this copy of the data. If you are interested in using your own encryption key pair check the [encryption paragraph](./data_ecryption.md)


* **Step 1**: You can **download** the user interface specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases/tag/sds-v0.1.0):
  
   - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v0.1.0/crypt4sds-python3.7-linux-amd64.zip)
   - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v0.1.0/crypt4sds-python3.7-macos-amd64.zip)
   - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v0.1.0/crypt4sds-python3.7-windows-amd64.zip)

* **Step 2**: Verify that the program has been digitally signed by CSC - IT Center for Science.  After the downloading and unzippling the file, you can find the Crypt4GH application in your download folder. 

When you open the application your might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietokniikan keskus Oy) and then click on _Run anyway_. 


<img width="385" alt="SDEnScreenShoot_2" src="https://user-images.githubusercontent.com/83574067/121065507-82b62700-c7d1-11eb-84ab-e6745eb76289.png">

* **Step 3**: Prepare your files

With Crypt4GH GUI it is possible to encrypt only one file at the time.

* If you need to encrypt **multiple files**, save them in one directory/folder and zip the folder (right click on the folder and click on _Send to_, next select _Compressed (zipped) folder_).
* If you need to encrypt **large datasets**, check the instructions on how to programmatically encrypt files with Crypt4GH.

<img width="468" alt="SDEnScreenshot_5" src="https://user-images.githubusercontent.com/83574067/121065613-a0838c00-c7d1-11eb-9326-c9f36d0503fc.png">

* **Step 4**: Encrypt the files

* Open the Encryption tool

* Next, presse the  **Select File** button. This opens a file browser that you can use to select the file that will be encrypted. When the file is selected, press the **Encrypt** button. This encrypts the selected file.

Encryption creates a new encrypted file that is named by adding to the end extension *.c4gh*. For example, encrypring file _my_data1.csv_ will produce a new, encrypted file with name _my_data.csv.c4h_.  Currently,Crypt4GH application does not provid a progress bar. If the file/zipped folder contains a big dataset, the encryption process can last for up to minutes.

The ecrypted file is now ready to be uploaded to _SD Connect_.

![Crytp4sds](https://user-images.githubusercontent.com/83574067/122655808-243c6180-d15e-11eb-82b6-40ba33dbd274.png)


* If you need to encrypt **large datasets**, check the instructions on how to programmatically encrypt files with Crypt4GH.



## Data upload 

To upload encrypted data in SD Connect it is suffiecint to use the **drag and drop function** (files or datasets less then 100 GB) in the browser page. Once the upload has started, a progress bar will visulize the status of the upload. For bigger datasets or files, **you can upload files programmatically** using the clients described later below.

If you did not create a buket yet, the user interface will automatically create a buket named: upload-nnnnnnnnnnnnn. Note that **it is not possible to rename buckets**.

If you create a new buket use the following **suggestions to name it**:

* Bucket **names must be unique** across all existing bucket in CSC storage solution
    
* Bucket names must **not contain uppercase characters or underscores or non-ASCII (ä, ö etc.) characters**
    
* All bucket **names are public**, so please do not include any confidential information in the bucket names
 
Example: ns-123456-raw-data-ddmmyy
  

<img width="953" alt="SD-Connect-4" src="https://user-images.githubusercontent.com/83574067/122090796-d5ff2980-ce10-11eb-986f-911c9a1f47bf.png">



## Data Sharing 

SD Connect user interface provides a simple way of sharing containers between different projects.

To share a container with another CSC project (and thus one of your colligues or collaborators) you need to:

* **know in advance the SD Account of the CSC project you want to share a contaner with** (see above in Step1, where this can be found)

* in the browser page click on the **share** button on the row of the container in the container listing 

Clicking the button takes you to **Share the container**  view, in which the user needs to specify the project/projects the container is going to be shared to, and what rights to give: 

* select **Grant read permission** if you want your colleagues to be able to see the files and folder inside the container and dowload them

* select also **Grant write permissions** if you want your colloeague to be able to add files and folder to the  shared conainer select. If you seelct only this option, your collieague or collaborator will be only able to add files to the container, but not be able to see its content.

* in **UUIDs to share with** add the SD Account of the project you want to share the container with 

* Next click on **Share**

At this point the user interface will redirect you to the **Shared** page and the container will be listed under **Shared from project**. Here you will be able to interrupt the sharing clicking on **Revoke container access**.


<img width="960" alt="SD-Connect-7" src="https://user-images.githubusercontent.com/83574067/122095850-8d4a6f00-ce16-11eb-9be2-093aaecc1b49.png">

<img width="960" alt="SD-Connect-5b" src="https://user-images.githubusercontent.com/83574067/122095933-a18e6c00-ce16-11eb-9232-a676097ef4b4.png">

<img width="960" alt="SD-Connect-6" src="https://user-images.githubusercontent.com/83574067/122095870-93405000-ce16-11eb-9e7e-f54914566827.png">




## Data upload and dowload using CLI for SD Connect

For uploading or dowloading data with a CLI, we suggest the use of [Swift Client](https://docs.csc.fi/data/Allas/using_allas/swift_client/)

Breafly:

* intsall swift in


    
    
    
    
    
    
    
    
  
















