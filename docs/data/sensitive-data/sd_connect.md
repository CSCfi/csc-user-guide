
# SD Connect (Sensitive Data Connect)

## Before you start


* According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always needs to be encrypted when uploaded or stored in CSC services for sensitive data. In this paragraph, we provide instructions on encrypting a copy of your data with CSC encryption key and Crypt4GH. For general information about Crypt4GH check the [Data encryption for data sharing](./crypt4gh_client.md) paragraph or  [crypt4gh GIT site](https://github.com/EGA-archive/crypt4gh.git).
    
* SD Connect facilitates working with sensitive data and it is a user interface for Allas, CSC cloud storage solution. By default a project can store up to 10 TiB of data. The storage space remains available as long as the CSC project is active. CSC does not make backups of the data in SD Connect. You need to **make your own backups** of important datasets.

     
!!! note  
    SD Connect and SD Desktop have not yet been security audited. Because of that users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***


## Login  

To access SD Connect you need to go to [MyCSC](https://my.csc.fi) and set up:

* [**a CSC account**](https://docs.csc.fi/accounts/how-to-create-new-user-account/)
* [**a CSC project**](https://docs.csc.fi/accounts/how-to-create-new-project/)
* add [**Service access to Allas**](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/) (CSC cloud storage solution)
* fill in the [**Description of data processing activities**] form (https://docs.csc.fi/accounts/when-your-project-handles-personal-data/)


Login to SD Connect is currently possible only with Haka (a user identity federation system) and CSC credentials at:

   * [https://sd-connect.csc.fi/](https://sd-connect.csc.fi) 

The interface is compatible with all modern web browsers. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925767-e4fae580-d993-11eb-9fd4-12147dcb956d.png">

<img width="960" alt="SD-Connect-0" src="https://user-images.githubusercontent.com/83574067/124901836-0b033400-dfeb-11eb-96d3-e5416f48f299.png">

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">




## User Interface


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/CMMwzl82dBI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">



Once you log in to SD Connect you access the default front-page: **Browser**.

In this page you can :

* view all **the  buckets available in your CSC project**, in which you can store encrypted sensitive data. The buckets can be created, downloaded, deleted or shared, using the appropriate icons;
   
*  **list and select your CSC project** from the drop down menu bar (top left corner) to visualize buckets belonging to a specific CSC project;

*  open any bucket (double click) and view its content (uploaded files or folders). Any file can be downloaded or shared using the download link. From this view, you can also download the entire bucket, delete files or upload new files and folders;


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925795-ed532080-d993-11eb-8763-f11c975016e6.png">


![sd-connect-1](https://user-images.githubusercontent.com/83574067/122786009-87dca100-d2bc-11eb-8a88-67b9bfc84930.png)


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925806-efb57a80-d993-11eb-8f63-622833e958ef.png">


* clicking on **edit** you can add appropriate tags to buckets or files. 

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925806-efb57a80-d993-11eb-8f63-622833e958ef.png">

![Tags example](https://user-images.githubusercontent.com/83574067/149055176-86461357-29df-4260-a80a-5e43966ea680.png)


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925806-efb57a80-d993-11eb-8f63-622833e958ef.png">



In the  **User information** page you can:

* in **Currently Consumes** view statistics about the selected CSC project resource usage: billing unit consumption and the total project storage usage (default storage 10 TiB);


* in **Project usage** you can view the SD Connect **Project Identifier**, an ID associated to your CSC project. This ID is required when you want to share containers with other CSC projects using SD Connect user interface. It does not contain sensitive information, thus it can be shared with your colleagues or collaborators via email.

* access the **Sharing API tokens** through which you can generate a temporary token (necessary for data upload programmatically, using Swift client. For more info check below).


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926085-37d49d00-d994-11eb-910f-4bcfa56c8589.png">

![SD-Connect-2](https://user-images.githubusercontent.com/83574067/124910227-098a3980-dff4-11eb-8029-57af3abc5cf4.png)


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926095-3a36f700-d994-11eb-8eb7-df1722efdacf.png">




In the **Shared** page:

* in **Shared to the project** you can view the **buckets that other CSC projects (belonging to your colleagues or collaborators) shared with you**. Next to the bucket name, under **Bucket Owner**,  it displays the ID associated with the CSC project to which the bucket belongs to (also called SD Account). With double click you can access the bucket and view the content (if you have reading access) or add files to the container (if you have edits rights).

!!! note
    All the buckets listed here are owned by other users which can decide when to revoke your access. You will not be able to access the file from SD Desktop until you make a copy of the bucket.


* in **Shared with the project** you can view the buckets which  **you shared with other CSC projects**. In this case you own the shared buckets and you can decide when to revoke access. 



<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926120-415e0500-d994-11eb-8455-9b8762c7a58b.png">

![sd-connect-4](https://user-images.githubusercontent.com/83574067/122786163-b22e5e80-d2bc-11eb-8c15-7585e656f0f2.png)
<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926131-4327c880-d994-11eb-81dd-c7b14d8e5f15.png">




## Data encryption and upload (files < 1Gb) - User Interface

SD Connect allows you to encrypt and upload files directly from your web-browser. With the following workflow and choosing the default encryption options, the files will be automatically encrypted with SDS public encryption key. As this is a simplified workflow, it is designed to allow **easy and safe encryption and automated decryption only using SD Desktop for data analysis or other SD services**. If you are interested in using your own encryption key pair or sharing the data with a collaborator, check [the following paragraph](./crypt4gh_client.md)

 
To upload data to SD Connect it is sufficient to:

* use the **drag and drop function** 
 
* click on the **upload** icon in the SD Connect browser window. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

![1](https://user-images.githubusercontent.com/83574067/149009891-a049a79d-b66a-45c5-96a1-e0ea85617b0f.png)

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

You will be then redirected to a new page desplaying the defouald encryption options. Here, you can specify the name of the bukcet in which the data should be uploaded to. If you don't fill in a specific name, the user interface will automatically create a bucket named: upload-nnn (where nnn is replaced with 13 digit number based on creation time). Note that **it is not possible to rename buckets**.

If you create a new bucket use the following **suggestions to name it**:

* Bucket **names must be unique** across all existing buckets in all projects in SD-Connect and Allas. If you can't create a new bucket, it's possible that some other project is already using the name you would like to use. To avoid this kind of situation it is good practice to include some project specific identifiers (e.g. project ID number or acronym) in the bucket names.  
    
* **Avoid using spaces and special characters in bucket names**. Preferred characters are Latin alphabets (a-z), numbers (0-9), dash (-), underscore (\_) and  dot (.). SD Connect can cope with other characters too, but they may cause problems in some other interfaces.

* All bucket **names are public**, so please do not include any confidential information in the bucket names


With the icon  **Click to add files that will be uploaded** you will open a browser window in which you can select the files. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

![SD Connect final 1](https://user-images.githubusercontent.com/83574067/149011263-3225da97-b363-4c0f-9458-ccd1d09f293f.png)


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

Next click on **Encrypt and upload**: each file will be encrypted and uploaded to the bucket in SD Connect.

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

![3](https://user-images.githubusercontent.com/83574067/149011679-38799458-8e8d-4ddb-9a61-142a651b1fcb.png)


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

Once the process is completed, you can return to the SD Connect **browser** window. The encrypted files will show the extention *.c4hg*. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">
![6](https://user-images.githubusercontent.com/83574067/149012441-fc6ec48a-3d87-4cc2-bdd8-5e44e6c3cfd6.png)


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">


## Data Encryption and upload with CSC encryption key (files <100 Gb) - User Interface


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/T4LRJw7HTro" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">


As the workflow decribed above is still under development, files bigger then 1Gb needs to be encrypted  and uploaded in two different steps. However, we have developed a simple encryption tool (Crypt4ghsds GUI) that facilitates data encryption with SDS public encryption key. With this tool it is possible to encrypt only one file at the time.If you need to encrypt **large datasets**, check the instructions on how to programmatically encrypt files with Crypt4GH CLI below. 


!!! note
    As this is a simplified workflow, it is designed to allow **easy and safe encryption and automated decryption only using the Sensitive Data Services**. Using this workflow does not allow you to include your encryption keys. Thus, you will not be able to decrypt this copy of the data unless analizing it in SD Desktop. If you are interested in using your own encryption key pair check [the following paragraph](./crypt4gh_client.md)


* First, **download** the encryption application specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases/tag/sds-v1.0.0):
  
   - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v1.0.0/crypt4sds-python3.7-linux-amd64.zip)
   - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v1.0.0/crypt4sds-python3.7-macos-amd64.zip)
   - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/sds-v1.0.0/crypt4sds-python3.7-windows-amd64.zip)


* **Verify** that the program has been digitally signed by CSC - IT Center for Science. After downloading and unzipping the file, you can find the Crypt4GH application in your download folder.  When you open the application you might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and then click on _Run anyway_. 


* To **Encrypt the files**, open the encryotion tool and  press the  **Select File** button. This opens a file browser that you can use to select the file that will be encrypted. When the file is selected, press the **Encrypt** button. This encrypts the selected file.

* The tool creates a **new encrypted file that is named by adding to the end extension *.c4gh***, located in the same folder as the original file  For example, encrypting file _my_data1.csv_ will produce a new, encrypted file with name _my_data.csv.c4gh_.  Currently, Crypt4GH application does not provide a progress bar and if the file is large the encryption process can last for up to minutes.

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926290-6a7e9580-d994-11eb-958d-1fc30adc05f3.png">

![crypt4gh new](https://user-images.githubusercontent.com/83574067/149019832-0d4b1849-2a16-4de1-8597-a4f11562de61.png)



 <iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/x9uTYZcUFDw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> 
 
<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">


To upload the encrypted file (or a folder containing encrypted data) to SD Connect it is sufficient to:

* use the **drag and drop function** 
 
* click on the **upload** icon in the SD Connect browser window. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">
![1](https://user-images.githubusercontent.com/83574067/149009891-a049a79d-b66a-45c5-96a1-e0ea85617b0f.png)
<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">


* You will be then **redirected to a new page**. As you have already encrypted the data, you can **de-select the option: Encrypt file before upload**. 

* Next, you can specify the name of the bukcet in which the data should be uploaded to. If you don't fill in a specific name, the user interface will automatically create a bucket named: upload-nnn (where nnn is replaced with 13 digit number based on creation time). Note that **it is not possible to rename buckets**. If you create a new bucket use the following **suggestions to name it**. Bucket **names must be unique** across all existing buckets in all projects in SD-Connect and Allas. If you can't create a new bucket, it's possible that some other project is already using the name you would like to use. To avoid this kind of situation it is good practice to include some project specific identifiers (e.g. project ID number or acronym) in the bucket names.  **Avoid using spaces and special characters in bucket names**. Preferred characters are Latin alphabets (a-z), numbers (0-9), dash (-), underscore (\_) and  dot (.). SD Connect can cope with other characters too, but they may cause problems in some other interfaces. All bucket **names are public**, so please do not include any confidential information in the bucket names.

* Next, click on **Upload**. A progress bar will visualize the status of the upload. Once the process is completed, you can return to the SD Connect **browser** window. The encrypted files will show the extention *.c4hg*. 


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">

![example upload 5](https://user-images.githubusercontent.com/83574067/149021515-32567945-c755-4f1d-a940-33dd23f42c46.png)

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">



## Data encryption and upload with CSC encryption key- Command Line Interface

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/l9BjVuUJ4zA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">


!!! note
        Files that have been encrypted with the _CSC Sensitive Data Services public key_, can be decrypted only when imported in SD Desktop, thus using CSC Sensitive Data             Services.
        If you wish to encrypt the data to transfer them to other services, you need to plan the encryption in advance and use your own encryption key pair. For more                 information, check the Data Sharing section in these paragraph below and the [Data encryption for data sharing](./crypt4gh_client.md) paragraph.


For general information about using Crypt4GH at CSC check: 
   * [crypt4gh GIT site](https://github.com/EGA-archive/crypt4gh.git)
 
  

### Step 1: Install the latest version of Crypt4GH encryption tool

**Python 3.6+ required** to use the crypt4gh encryption utility. 
To install Python: https://www.python.org/downloads/release/python-3810/

If you have a working python installation and you have permissions to add libraries to your python installation, you can install Crypt4GH with command:

```text
pip install crypt4gh
```

### Step 2: Download CSC Sensitive Data services Public key

Download CSC Sensitive Data Services public key from the link [here](./csc-sd-services.pub), or copy/paste the three lines from the box below into a new file.
The file should be saved in text-only format. Here we assume that the key file is named as _csc-sd-services.pub_.

```text
-----BEGIN CRYPT4GH PUBLIC KEY-----
dmku3fKA/wrOpWntUTkkoQvknjZDisdmSwU4oFk/on0=
-----END CRYPT4GH PUBLIC KEY-----
```

### Step 3: Encrypt a file

Cryp4GH is able to use several public keys for encryption. This can be very handy in cases were the encrypted data needs to be used by several users or services. Unfortunately SD Connect is not yet compatible with encryption with multiple keys. Because of that you must do the encryption using the CSC Sensitive Data Services public key only, if you plan to upload the data to SD Connect. In this case the syntax of the encryption command is:

```text
crypt4gh encrypt --recipient_pk public-key < input > output
```
For example

```text
crypt4gh encrypt --recipient_pk csc-sd-services.pub < my_data1.csv > my_data1.csv.c4gh
```
The encrypted file (_my_data1.csv.c4gh_) can now be uploaded to SD Connect and will be automatically decrypted when imported in your own private computing environment in SD Desktop.
 

### Data encryption and upload with Allas help tool: a-put

The [allas client utilities](https://github.com/CSCfi/allas-cli-utils/) is a set of command line tools that can be installed and used in Linux and MacOSX machines. If you have these tools, you can use data upload command _a-put_ with command line option _--sdx_ to upload data to Allas/SD Connect so that the uploaded files are automatically encrypted with the CSC Sensitive Data Services public key before the upload. The public key is included to the tool so that you don't need to download your own copy of the key.

You can upload a single file with command like:

```text
a-put --sdx my_data1.csv
```
By default _a-put --sdx_ uploads the encrypted file into bucket that has name _project-number-SD_CONNECT_ . 

You can also upload complete directories and define a specific target bucket. For example the command below will encrypt and upload all the files in directory _my_data_ to SD Connect into bucket _1234_SD_my_data_.
```
a-put --sdx my_data -b 1234_SD_my_data
```



### Programmatic data upload and download with SD Connect

To upload encrypted data to SD Connect programmatically, you need to use your CSC credentials (CSC username and password).

SD Connect is a user interface for CSC Allas object storage. In practice this means that any data which you can access in Allas, can also be imported to SD Desktop with SD-Connect Downloader.

Thus you can use any of the Allas compatible clients to upload your data to SD-Connect programmatically. However, as SD Connect is based on Swift protocol, it is recommended that you use upload tools that are based on swift protocol.


These include:

   * [rclone](../Allas/using_allas/rclone.md) (with normal Allas configuration)
   * [swift command line client](../Allas/using_allas/swift_client.md)
   * [Horizon web interface](../Allas/using_allas/web_client.md) in [https://pouta.csc.fi](https://pouta.csc.fi)
   * [CyberDuck](../Allas/accessing_allas.md#cyberduck-functions) Graphical data transport tool for Windows and Mac.

Note that if you use these tools, you must encrypt your sensitive data, before you upload it to SD Connect.



## Data Sharing with SD Connect user interface

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/fj-KADK1ykY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123925776-e75d3f80-d993-11eb-8c1e-7f77341aa382.png">


!!! Note
        For more information about encryption with private keys check: [Data encryption for data sharing](crypt4gh_client.md).


SD Connect user interface provides a simple way of sharing containers between different projects.

To share a container with another CSC project (and thus one of your colleagues or collaborators) you need to:

* **know in advance the SD Account of the CSC project you want to share a container with** (see above in *User Interface* paragraph, where this can be found)


* in the browser page click on the **share** button on the row of the container in the container listing 

Clicking the button takes you to **Share the container**  view, in which the user needs to specify the project/projects the container is going to be shared to, and what rights to give: 


* select **Grant read permission** if you want your colleagues to be able to see the files and folder inside the container and download them

* select also **Grant write permissions** if you want your colleague to be able to add files and folder to the  shared container select. If you select only this option, your colleague or collaborator will be only able to add files to the container, but not be able to see its content.

* in **Project Indetifiers to share with** add the SD Connect Project Identifier of the project you want to share the container with 

* Next click on **Share**

At this point the user interface will redirect you to the **Shared** page and the container will be listed under **Shared from project**. Here you will be able to interrupt the sharing clicking on **Revoke container access**.


<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926373-7b2f0b80-d994-11eb-8efa-903209dd505e.png">

![sd-connect-6](https://user-images.githubusercontent.com/83574067/122786188-ba869980-d2bc-11eb-93be-cde0f14d0795.png)

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926373-7b2f0b80-d994-11eb-8efa-903209dd505e.png">

![SD-Connec-7](https://user-images.githubusercontent.com/83574067/124917332-5d008580-dffc-11eb-9c70-3647e9538f79.png)

<img width="570" alt="space in user guide" src="https://user-images.githubusercontent.com/83574067/123926373-7b2f0b80-d994-11eb-8efa-903209dd505e.png">

![sd-connect-8](https://user-images.githubusercontent.com/83574067/122786632-2ec13d00-d2bd-11eb-966a-ad2eb6be2589.png)


# Troubleshooting



| Problem           |                                                                                       | Possible Solution                                                                                                                                                                                                                                                                                                                                                            |
|-------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Decryption        | I cannot decrypt the data I downloaded from CSC services.                             | You can decrypt the data only if you have used your own public key for the encryption. If you used a CSC Sensitive Data Services public for the encryption, the data can be decrypted only in SD Desktop. In that case, the decryption is automatic. If you used your collaborator’s public key to encrypt the data, only they can decrypt the data with their private key.  |
| Encryption        | Encryption takes a long time.                                                         | For large files and datasets, the encryption can take up to a few minutes.                                                                                                                                                                                                                                                                                                   |
| Folder encryption | I can not select the folder I want to encrypt with Crypt4GH graphical user interface. | It is not possible to encrypt an entire folder, just single files                                                                                                                                                                                                                                                                                                            |



| Problem       |                                                                                          | Possible solution                                                                                                                                                                                                                               |
|---------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data upload   | I am trying to upload a big file/folder with the user interface and the upload is stuck. | To upload files or folders that are larger than 200 GB, the data should be uploaded programmatically.                                                                                                                                           |
|               | Low upload speed (programmatically)                                                      | Average upload speed can go from 100 to 200 MiB/s. Specific scripts can be used to optimize the upload of large files.                                                                                                                          |
| Bucket        | I am not able to create a new bucket.                                                    | 1)      Check in MyCSC portal that your current project has service access for Allas 2)      Try to use a bucket name that is unique and doesn’t contain special characters. 3)  Select the correct project in SD Connect user interface        |
|               | I cannot find my bucket.                                                                 | Check if the bucket is stored under a different project. If someone has shared the bucket with you, you can find it under the ‘Shared to’ section and copy it. If someone has shared the bucket with you, they could have revoked the sharing.  |
|               | I cannot upload data into my bucket                                                      | Check that your project still has storage space left.                                                                                                                                                                                           |
| Shared bucket | I cannot upload data into a shared bucket.                                               | Your colleague didn’t add editing rights when they shared the bucket.                                                                                                                                                                           |
|               | I cannot see the content of a shared bucker.                                             | Your colleague didn’t add reading rights when they shared the bucket.                                                                                                                                                                           |



    

    
    
  
















