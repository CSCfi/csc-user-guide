
# SD Connect (Sensitive Data Connect)

## Before you start

* According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always needs to be encrypted when uploaded or stored in CSC services for sensitive data. Check the [encryption paragraph](./data_ecryption.md) for more information about encryption with Crypt4GH. 
    
* SD Connect is based on the [Allas](./data/allas/overview.md) cloud storage service. SD Connect is a user interface that facilitate working with sensitive data. 
The general rules and methods of usage are the same as in Allas. By default a project can store up to 10 TiB of data. The storage space remains available as long as the CSC project is active. You should not consider SD Connect as a permanent data storage. Instead, you should have a plan about what will happen to the data when project is closed. 
CSC does not make backups of the data in SD Connect. You need to **make your own backups** of important datasets. 
     
!!! note  
    SD Connect and SD Desktop has not yet been security audited. Because of that users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***


## Login 

To access SD Connect you need:

* **a CSC account**
* **a CSC project**
* **Service access to Allas** (CSC cloud storage solution)

Login to SD Connect is currently possible only with Haka (a user identity federation system) at https://sd-connect.csc.fi/ using any modern web browser. If you do not have an Haka account and can not access the user interface, you can still upload data programmatically, directly into Allas (see the end of this paragraph). 


<img width="854" alt="SD-Connect-0" src="https://user-images.githubusercontent.com/83574067/122104560-73ae2500-ce20-11eb-9ca8-eaa0e3e3f199.png">



## User Interface

Once you login in SD Connect you access the default front-page: **Browser**.

In this page you can :

* view all **the  buckets available in your CSC project**, in which you can store encrypted sensitive data. The buckets can be created, downloaded, deleted or shared, using the appropriate icons;
   
*  **list and select your CSC project** from the drop down menu bar (top left corner) to visualize buckets belonging to a specific CSC project;

*  open any bucket (double click) and view its content (uploaded files or folders). Any file can be downloaded or shared using the download link. From this view, you can also download the entire bucket, delete files or upload new files and folders.



![sd-connect-1](https://user-images.githubusercontent.com/83574067/122786009-87dca100-d2bc-11eb-8a88-67b9bfc84930.png)






In the  **User information** page you can:

* in **Currently Consumes** view statistics about the selected CSC project resource usage: billing unit consumption and the total project storage usage (defoult storage 10 TiB);

* in **Project usage** you can view the **SD Connect Account, an ID associated to your CSC project**. This ID is required when you want to share containers with other CSC projects using SD Connect user interface. It does not contain sensitive information, thus it can be shared with your colleagues or collaborators via email.

* access the **Token icon** through which you can generate a temporary token (necessary for data upload programmatically, using Swift client. For more info check below).









In the **Shared** page:

* in **Shared to the project** you can view the **buckets that other CSC projects (belonging to your colleagues or collaborators) shared with you**. Next to the bucket name, under **Bucket Owner**,  it is displayed the ID associated to CSC project to which the bucket belongs to (also called SD Account). With double click you can access the bucket and view the content (if you have reading access) or add files to the container (if you have edits rights). 

!!! note 
    All the buckets listed here are owned by another users that can decide when to revoke your access. You will not be able to access the file from SD Desktop until you make a copy of the container. 

* in **Shared with the project** you can view the buckets which  **you shared with other CSC projects**. In this case you own the shared buckets and you can decide when to revoke access. 



![sd-connect-4](https://user-images.githubusercontent.com/83574067/122786163-b22e5e80-d2bc-11eb-8c15-7585e656f0f2.png)



## Data encryption with CSC-sd-encryption key and Crypt4GH GUI for SDS.

With the following workflow, you can use a graphical user interface (Crypt4sds GUI) developed by CSC to **encrypt and import a copy of your data to SD Desktop**.  

!!! note
    As this is a simplified workflow, it is designed to allow **easy and safe encryption and automated decryption only using the Sensitive Data Services**. Using this workflow does not allow you to include your encryption keys. Thus, you will not be able to decrypt this copy of the data. If you are interested in using your own encryption key pair check the [encryption paragraph](./data_ecryption.md)


* **Step 1**: You can **download** the user interface specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases/tag/sds-v0.1.0):
  
   - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v0.1.0/crypt4sds-python3.7-linux-amd64.zip)
   - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v0.1.0/crypt4sds-python3.7-macos-amd64.zip)
   - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v0.1.0/crypt4sds-python3.7-windows-amd64.zip)

* **Step 2**: Verify that the program has been digitally signed by CSC - IT Center for Science.  After  downloading and unzipping the file, you can find the Crypt4GH application in your download folder. 

When you open the application you might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and then click on _Run anyway_. 


<img width="385" alt="SDEnScreenShoot_2" src="https://user-images.githubusercontent.com/83574067/121065507-82b62700-c7d1-11eb-84ab-e6745eb76289.png">

* **Step 3**: Prepare your files

With Crypt4GH GUI it is possible to encrypt only one file at the time.

* If you need to encrypt **multiple files**, save them in one directory/folder and zip the folder (right click on the folder and click on _Send to_, next select _Compressed (zipped) folder_).
* If you need to encrypt **large datasets**, check the instructions on how to programmatically encrypt files with Crypt4GH.

<img width="468" alt="SDEnScreenshot_5" src="https://user-images.githubusercontent.com/83574067/121065613-a0838c00-c7d1-11eb-9326-c9f36d0503fc.png">

* **Step 4**: Encrypt the files

* Open the Encryption tool

* Next, press the  **Select File** button. This opens a file browser that you can use to select the file that will be encrypted. When the file is selected, press the **Encrypt** button. This encrypts the selected file.

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
  


![sd-connect-5](https://user-images.githubusercontent.com/83574067/122786181-b9556c80-d2bc-11eb-9a8f-3bea273eddab.png)


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


![sd-connect-6](https://user-images.githubusercontent.com/83574067/122786188-ba869980-d2bc-11eb-93be-cde0f14d0795.png)
![sd-connect-7](https://user-images.githubusercontent.com/83574067/122786201-bc505d00-d2bc-11eb-832a-9771eb80da72.png)
![sd-connect-8](https://user-images.githubusercontent.com/83574067/122786632-2ec13d00-d2bd-11eb-966a-ad2eb6be2589.png)





## Data upload with other clients

SD Connect is using Allas object storage for storing data. In practice thie means that any data which you can access i Allas, can also be dowloaded to SD Desktop with SD-Conect Dowloader. Thus you can use any of the Allas compatible clients to upload your data to SD-Connect. Hower, as SD Connect is based on Swift protocol, it is recommended that you use upload tools that are based on swift protocol. These include:
   * [rclone](../Allas/using_allas/rclone.md) (with normal Allas confi guration)
   * [swith command line client](../Allas/using_allas/swift_client.md)
   * [Horizon web interface](../Allas/using_allas/web_client.md) in [https://pouta.csc.fi](https://pouta.csc.fi)
   * [CyberDuck](../Allas/accessing_allas.md#cyberduck-functions) Grafical data transport tool for Windos and Mac.

Note that if you use these tools, you must encrypt your sensitive data, before you upload it to Allas. 

    
    
    
    
    
    
    
    
  
















