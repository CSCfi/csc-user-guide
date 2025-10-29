[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Uploading and encrypting data

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Files uploaded to SD Connect are automatically encrypted and decrypted during download, using the service’s integrated key management system. This functionality supports all file types and formats, with a maximum file size of 100 GB. Larger files or folders can be uploaded programmatically. Once files are uploaded and stored, the service begins consuming billing units. The default storage quota is 10 TB. When this limit is reached, uploads will no longer be accepted until additional storage is allocated.

Note !!!

     All members of the same CSC project have access to upload and download files stored via SD Connect. This can be limited by sharing files with **Read to SD Desktop** permission. [Read about use case](./sd-connect-share-read-to-sd-desktop.md) and please contact servicedesk@csc.fi (suject: SD Connect) for assistance.            


## Step by step

### 1. Plan the number of folders needed 

SD Connect is based on a cloud object storage infrastructure. This means that:

- once files are uploaded, they are split into segments to optimize storage and performance. This segmentation is not visible through the user interface, but it has important implications for how data should be managed. The user interface might be slower when there are more than 2500 files for each folder. In this case please user the [command-line tools for upload and automated key management](./sd-connect-command-line-interface.md). 
  
-  ** Once files are uploaded to SD Connect, they cannot be edited or changed**. Therefore, it is important to plan ahead how datasets and files will be organized in SD Connect before you start uploading. To keep things simple and avoid problems, we recommend creating a separate folder for each experiment or dataset. Try to use clear folder names so it’s easy to find things later and avoid putting too many files in one folder (each folder has a limit of 500.000 segmented files).

-  Uplaods into subfolders is not supported

-  Large files /uplaods may take hours to upload and uploads stop after 8 hours.

#### 2. Plan folder names
  
 !!! info "Folder names"

    * Folder name should start with a lowercase letter or a number.
    * Folder name should be between 3 and 63 characters long.
    * Use Latin alphabets (a-z), numbers (0-9) and dash (-). 
    * Uppercase letters, underscore  (_) and accent letters with diacritics or special marks (åäöe') are not allowed.
    * Folder names must be unique across all existing folders in all projects in SD Connect and Allas. If you can't create a new folder, another project may already use the name you have chosen. To avoid this situation, it is good practice to include projec specific identifiers (e.g., project ID number or acronym) in the folder name.
    * Remember, all folder names are public; please do not include any confidential information.
    * Folder names can't be modified afterwards.


## 3. Accept cockies

File uploads are supported in Google Chrome and Mozilla Firefox (incognito mode not supported) browsers. On first use, a browser pop-up may request cookie consent. Accepting cookies enables file and folder uploads. This action is required only once.

## 4. Upload and encrypt files to a new folder

1. Log in to SD Connect.
2. Select the correct CSC project in the top left corner.
3. Click **Upload** in the top right corner.
4. In the new window, name the destination folder for your files taking into consideration that soem caractes are not allowed: uppercase letters, underscores (_), and letters with diacritics or special marks (e.g., å, ä, ö, é) (please see parapgh 2). 
5. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. Click **Upload** to start automatic encryption and upload.
7. Notification about the status of upload will appear and be visible until the upload is completed. Notification also includes a link to the destination folder.
8. Once the upload is finished, the encrypted files will display the extentsion .c4gh, this means that they have been successfully encrypted. 
9. Now the files are accessible for downloading and sharing via SD Connect or for analysis, editing or annotation once imported via SD Desktop.



![SD Connect Upload](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Upload.png)


## Upload and encrypt files to an existing folder

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
