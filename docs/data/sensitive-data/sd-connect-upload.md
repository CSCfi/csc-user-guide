[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Uploading and encrypting data

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Files uploaded to SD Connect are automatically encrypted and decrypted during download, using the service’s integrated key management system. This functionality supports all file types and formats, with a maximum file size of 100 GB. Larger files or folders can be uploaded programmatically.

!!! Note
     All members of the same CSC project have access to upload and download files stored via SD Connect. This can be limited by sharing files with **Read to SD Desktop** permission to a diferent CSC project Academic type. Please contact servicedesk@csc.fi (suject: SD Connect) for assistance.            


## Step by step

### 1. Plan the number of folders needed

SD Connect is built on a cloud object storage infrastructure. Files can only be uplaoded into top-level or 'main folders' creatd with SD Connect:  a top-level 'box' used to store files or folders. This has several implications for how your data should be organized and managed:

- **Once files are uploaded to SD Connect, they cannot be edited or modified**.  It is therefore important to plan the folder structure in advance. To simplify data management and avoid issues, it is recommended to create a separate folder for each dataset or experiment. Avoid placing too many files in a single folder, each folder can contain up to 500.000 segmented files.The user interface might be slower when there are more than 2500 files for each folder. In this case please user the [command-line tools for upload and automated key management](./sd-connect-command-line-interface.md). 

- **Subfolders not supported**: Uploading files into subfolders is not supported.

- **Upload duration**: Uploading large files or large batches may take several hours. Uploads are automatically stopped after 8 hours.
  
-  **File segmentation**: Uploaded files are automatically split into segments to optimize storage and performance. This segmentation is not visible in the user interface but can affect performance. When an SD Connect folder contains more than 2,500 files, the interface may become slower. In such cases, it is recommended to use the command-line tools for uploading and automated key management.


### 2. Plan folder names
  
When creating folders in SD Connect, specific naming rules must be followed to ensure compatibility, which requires some planning. 

!!! Note
    Top level folder name can not be modified after their creation with SD Connect. 
    These rules apply only to top-level folders created in the service, not to subfolders uploaded from a local computer. 

**Folder names must**:

* start with a lowercase letter or a number.
* be between 3 and 63 characters long.
* use Latin alphabets (a-z), numbers (0-9) and dash (-).
* be unique across all existing folders in all projects in SD Connect and Allas. If you can't create a new folder, another project may already use the name you have chosen. To avoid this situation, it is good practice to include projec specific identifiers (e.g., project ID number or acronym) in the folder name.
    
**Folder names must not contain**:

* Uppercase letters, underscore  (_) and accent letters with diacritics or special marks (åäöe') are not allowed.
* all folder names are public; please do not include any confidential information.
* Folder names can't be modified afterwards.


### 3. Accept cookies

File uploads are supported in Google Chrome and Mozilla Firefox (incognito mode not supported) browsers. 

On first use, a browser pop-up may request cookie consent. Accepting cookies enables file and folder uploads. This action is required only once.

### 4. Upload and encrypt files to a new folder

1. Log in to SD Connect.
2. Select the correct CSC project in the top left corner.
3. Click **Upload** in the top right corner.
4. In the new window, name the destination folder for your files taking into consideration that some caractes are not allowed: uppercase letters, underscores (_), and letters with diacritics or special marks (e.g., å, ä, ö, é) (please see paragraph 2). 
5. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. Click **Upload** to start automatic encryption and upload.
7. Notification about the status of upload will appear and be visible until the upload is completed. Notification also includes a link to the destination folder.
8. Once the upload is finished, the encrypted files will display the extentsion .c4gh, this means that they have been successfully encrypted. 
9. Now the files are accessible for downloading and sharing via SD Connect or for analysis, editing or annotation once imported via SD Desktop.
10. Once files are uploaded and stored, the service begins consuming billing units. The default storage quota is 10 TB. When this limit is reached, uploads will no longer be accepted until additional storage is allocated.



![SD Connect Upload](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Upload.png)


### Upload and encrypt files to an existing folder

1. Select the correct folder (by double-click).
2. Click **Upload** in the top right corner and follow steps from 4 to 6 in above paragraph.

## Create a folder

You can create a folder and upload files to it later.

1. Click **Create folder**.
2. Name your folder taking into consideration that soem caractes are not allowed: uppercase letters, underscores (_), and letters with diacritics or special marks (e.g., å, ä, ö, é) (please see pargraph 2). 
3. Click **Save**.

![SD Connect Create folder](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_CreateFolder.png)



## The next steps in this guide 

* [Upload](./sd-connect-upload.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Share](./sd-connect-share.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)
