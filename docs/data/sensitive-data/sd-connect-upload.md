[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Uploading and encrypting data

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Files uploaded to SD Connect are automatically encrypted and decrypted during download, using the service’s integrated key management system. This functionality supports all file types and formats, with a maximum file size of 100 GB. Larger files or folders can be uploaded programmatically.


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    ___

    All members of a CSC project can upload and download files via SD Connect. To restrict access, files can be shared with another CSC project (Academic type) using **Read to SD Desktop** permission. For assistance, please contact servicedesk@csc.fi (subject: SD Connect). 

</div>
    

## Step by step

### 1. Plan the number of buckets needed

SD Connect is built on a cloud object storage infrastructure. Files can only be uploaded into  a bucket, created with SD Connect. Bucket is a top-level 'box' used to store files or folders. This has several implications for how your data should be organized and managed:

- **Once files are uploaded to SD Connect, they cannot be edited or modified**.  It is therefore important to plan the bucket structure in advance. To simplify data management and avoid issues, it is recommended to create a separate bucket for each dataset or experiment. Avoid placing too many files in a single bucket, each bucket can contain up to 500.000 segmented files.

- **Uploading files into subfolders is not supported.** 

- **Upload duration**: Uploading large files or large batches may take several hours. Uploads are automatically stopped after 8 hours.
  
-  **File segmentation**: Uploaded files are automatically split into segments to optimize storage and performance. This segmentation is not visible in the user interface but can affect performance.
    
- The user interface might be slower when there are more than 2500 files for each folder. In this case please use the [command-line tools for upload and automated key management](./sd-connect-command-line-interface.md). 


### 2. Plan bucket names
  
When creating buckets in SD Connect, specific naming rules must be followed to ensure compatibility, which requires some planning. 


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    Bucket name can not be modified after their creation with SD Connect. 

</div>
    
These rules apply only to buckets created in the service, not to subfolders or files uploaded from a local computer. 

**Bucket names must**:

* start with a lowercase letter or a number.
* be between 3 and 63 characters long.
* use Latin alphabets (a-z), numbers (0-9) and dash (-).
* be unique across all existing buckets in all projects in SD Connect and Allas. If you can't create a new bucket, another project may already use the name you have chosen. To avoid this situation, it is good practice to include project specific identifiers (e.g., project ID number or acronym) in the bucket name.
    
**Bucket names must not contain**:

* uppercase letters, underscore  (_) and accent letters with diacritics or special marks (åäöe') are not allowed.
* all folder names are public; please do not include any confidential information.
* Bucket names can't be modified afterwards.


### 3. Accept cookies

File uploads are supported in Google Chrome and Mozilla Firefox (incognito mode not supported) browsers. On first use, a browser pop-up may request cookie consent. Accepting cookies enables file and folder uploads. This action is required only once.

### 4. Upload and encrypt files to a new bucket

1. Log in to SD Connect and select the correct CSC project in the top left corner.
2. Click **Upload** in the top right corner.
3. In the new window, name the destination bucket for your files taking into consideration that some charactes are not allowed: uppercase letters, underscores (_), and letters with diacritics or special marks (e.g., å, ä, ö, é). [See detailed instructions](#2-plan-bucket-names)
4. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. 
5. Click **Upload** to start automatic encryption and upload.
6. Notification about the status of upload will appear and be visible until the upload is completed. Notification also includes a link to the destination bucket.
7. Once the upload is finished, the encrypted files will display the extension .c4gh, this means that they have been successfully encrypted. 

Now the files are accessible for downloading and sharing via SD Connect or for analysis, editing or annotation once imported via SD Desktop. Once files are uploaded and stored, the service begins consuming Billing Units. The default storage quota is 10 TB. When this limit is reached, uploads will no longer be accepted until additional storage is allocated.

![SD Connect Upload](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Upload.png)


## 5. Upload and encrypt files to an existing bucket

1. Select the correct bucket.
2. Click **Upload** in the top right corner and follow steps from 5 to 9 in above paragraph.

### 6. Create a bucket

You can create a empty bucket and upload files to it later.

1. Click **Create bucket**.
2. Name your bucket taking into consideration that some characters are not allowed: uppercase letters, underscores (_), and letters with diacritics or special marks (e.g., å, ä, ö, é). [See detailed instructions](#2-plan-bucket-names)
3. Click **Save**.

![SD Connect Create bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_NewBucket.png)



## The next steps in this guide 

* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Share](./sd-connect-share.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)
