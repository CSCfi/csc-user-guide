[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Uploading and encrypting data

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


* [Uploading and encrypting data: overview](#uploading-and-encrypting-data-overview)
* [Uploading and encrypting data: step-by-step](#uploading-and-encrypting-data-step-by-step)

Files uploaded to SD Connect are automatically encrypted and decrypted during download, using the service’s integrated key management system. This functionality supports all file types and formats, with a maximum file size of 100 GB. Larger files or folders can be uploaded programmatically.


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    ___

    All members of a CSC project can upload and download files via SD Connect. To restrict access, files can be shared with another CSC project (Academic type) using **Read to SD Desktop** permission. For assistance, please contact servicedesk@csc.fi (subject: SD Connect). 

</div>

____

## Uploading and encrypting data: overview

SD Connect is built on a cloud object storage infrastructure. Files can only be uploaded into a bucket, created with SD Connect. Bucket is a top-level 'box' used to store files or folders. This has several implications for how your data should be organized and managed:

- **Once files are uploaded to SD Connect, they cannot be edited or modified**. It is therefore important to plan the bucket structure in advance. To simplify data management and avoid issues, it is recommended to create a separate bucket for each dataset or experiment. Avoid placing too many files in a single bucket, each bucket can contain up to 500.000 segmented files.

- **Uploading files into subfolders is not supported.** 

- **Upload duration**: Uploading large files or large batches may take several hours. Uploads are automatically stopped after 8 hours.
  
-  **File segmentation**: Uploaded files are automatically split into segments to optimize storage and performance. This segmentation is not visible in the user interface but can affect performance.
    
- The user interface might be slower when there are more than 2500 files for each folder. In this case please use the [command-line tools for upload and automated key management](./sd-connect-command-line-interface.md). 

____

## Uploading and encrypting data: step-by-step

### 1. Plan bucket names
  
When creating buckets in SD Connect, specific naming rules must be followed to ensure compatibility, which requires some planning. These rules apply only to buckets created in the service, not to subfolders or files uploaded from a local computer. 


<div class="grid cards" markdown>

- :material-check-circle:{ .lg .middle } **Bucket names must:**
  { .csc-grid-card-success }

    ---

    * start with a lowercase letter or a number.
    * be between 3 and 63 characters long.
    * use Latin alphabets (a-z), numbers (0-9) and dash (-).
    * be unique across all existing buckets in all projects in SD Connect and Allas. If you can't create a new bucket, another project may already use the name you have chosen. To avoid this situation, it is good practice to include project specific identifiers (e.g., project ID number or acronym) in the bucket name.


- :material-close-circle:{ .lg .middle } **Bucket names must not contain:**
  { .csc-grid-card-error }

    ---

    * uppercase letters, underscore  (_) and accent letters with diacritics or special marks (åäöe') are not allowed.
    * any confidential information. All bucket names are public.
    * Bucket names can't be modified afterwards.

</div>

___

### 2. Accept cookies

**This action is required only once:** File uploads are supported in Google Chrome and Mozilla Firefox (incognito mode not supported) browsers. On first use, a browser pop-up may request cookie consent. Accepting cookies enables file and folder uploads. 

___

### 3. Upload and encrypt files to a new bucket

1. Log in to SD Connect and select the correct CSC project in the top left corner.
2. Click **Upload** in the top right corner.
3. In the new window, name the destination bucket for your files taking into consideration that some charactes are not allowed: uppercase letters, underscores (_), and letters with diacritics or special marks (e.g., å, ä, ö, é). [See detailed instructions](#1-plan-bucket-names)
4. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. 
5. Click **Upload** to start automatic encryption and upload.
6. Notification about the status of upload will appear and be visible until the upload is completed. Notification also includes a link to the destination bucket.
7. Once the upload is finished, the encrypted files will display the extension .c4gh, this means that they have been successfully encrypted. 

Now the files are accessible for downloading and sharing via SD Connect or for analysis, editing or annotation once imported via SD Desktop. Once files are uploaded and stored, the service begins consuming Billing Units. The default storage quota is 10 TB. When this limit is reached, uploads will no longer be accepted until additional storage is allocated.

![Start upload](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_StartUpload.png)

![Upload](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Upload.png)

___

### 3.1 Upload and encrypt files to an existing bucket

1. Select the correct project and bucket.
![SD Connect Select bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket1.png)

2. Click **Upload** in the top right corner.
![SD Connect Start Upload to an existing bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket2.png)

3. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. Finally click **Upload** to start automatic encryption and upload.
![SD Connect Select bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket3.png)

____

### 3.2 Create an empty bucket

You can create an empty bucket and upload files to it later.

1. Select the correct project. Click **Create bucket**.
![SD Connect Create empty bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_NewBucket.png)

2. Name your bucket taking into consideration that some characters are not allowed: uppercase letters, underscores (_), and letters with diacritics or special marks (e.g., å, ä, ö, é). [See detailed instructions](#1-plan-bucket-names). Finally click **Save**.
![SD Connect Name empty bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_NewBucket1.png)





## The next steps in this guide 

* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Share](./sd-connect-share.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)
