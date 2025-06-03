[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Uploading and encrypting data

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Your data is automatically encrypted when you upload data to SD Connect. This is suitable for all file types and formats, but it is supported only for files up to 100 GB and folders smaller than 1 TB. Largers files or folders can be and uploaded [programmatically](./sd-connect-command-line-interface.md).

!!! Note
    If this is your first time using the service, a pop-up may appear in your browser asking you to accept cookies. Please click Accept to enable uploading files and folders.

## Upload and encrypt files to a new folder

1. Log in to SD Connect.
2. Select the correct CSC project in the top left corner.
3. Click **Upload** in the top right corner.
4. In the new window, name the destination folder for your files.
5. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. Click **Upload** to start automatic encryption and upload.
6. Notification about the status of upload will appear and be visible until the upload is completed. Notification also includes a link to the destination folder.
7. Once the upload is finished, the encrypted files are accessible for downloading and sharing via SD Connect or for analysis, editing or annotation via SD Desktop.

!!! info "Folder names"

    * Folder name should start with a lowercase letter or a number.
    * Folder name should be between 3 and 63 characters long.
    * Use Latin alphabets (a-z), numbers (0-9) and dash (-). 
    * Uppercase letters, underscore  (_) and accent letters with diacritics or special marks (åäöe') are not allowed.
    * Folder names must be unique across all existing folders in all projects in SD Connect and Allas. If you can't create a new folder, another project may already use the name you have chosen. To avoid this situation, it is good practice to include projec specific identifiers (e.g., project ID number or acronym) in the folder name.
    * Remember, all folder names are public; please do not include any confidential information.
    * Folder names can't be modified afterwards.



![SD Connect Upload](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Upload.png)


## Upload and encrypt files to an existing folder

1. Select the correct folder (by double-click).
2. Click **Upload** in the top right corner and follow steps from 4 to 6 in above paragraph.

## Upload and encrypt files to a new folder

You can create a folder and upload files to it later.

1. Click **Create folder**.
2. Name your folder.
3. Click **Save**.

![SD Connect Create folder](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_CreateFolder.png)

!!! warning "Warning"

    Members in the same CSC project can download and decrypt data from SD Connect. This can be limited by sharing files with **Read to SD Desktop** permission. [Read about use case](./sd-connect-share-read-to-sd-desktop.md)

!!! Note "Additional considerations"

    - Large files (> 100 GB) may take hours to upload, and uploads stop after 8 hours.
    - The user interface might be slower when there are more than 2500 files for each folder. In this case please user the [command-line tools for upload and automated key management](./sd-connect-command-line-interface.md). 
    - Files can't be edited in SD Connect; download them for editing or  access them via SD Desktop. 
    - Uploading files into subfolders is currently not supported.
    - SD Connect displays your encrypted files as virtual folders. Plan your folder structure carefully—organize files by projects, themes, or logical structures to improve accessibility and workflow. This also helps when sharing access with others. For assistance, contact CSC Service Desk (subject: Sensitive data).

## Features in SD Connect

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)
