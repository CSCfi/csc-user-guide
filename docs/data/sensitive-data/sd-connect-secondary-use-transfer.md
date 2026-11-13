[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Transfer health and social data for secondary use via SD Connect

## Prerequisites

- [Access SD Connect as a Data Controller for secondary use of health and social data](sd-use-case-secondary-use-data-controller.md)

## On this page:

1. [Delivering secondary use data via SD Connect - overview](#1-delivering-secondary-use-data-via-sd-connect---overview)
2. [Login to SD Connect](#2-login-to-sd-connect)
3. [Uploading and encrypting data](#3-uploading-and-encrypting-data)
4. [Manage datasets](#4-manage-datasets)

---

## 1. Delivering secondary use data via SD Connect - overview

Sensitive Data (SD) Connect enables the secure storage and sharing of sensitive data. It automatically encrypts files during upload through an easy-to-use interface. For uploads larger than 100 GB, a command-line tool is available which also provides automated key management.

With secondary use data, it is essential to **follow the practises presented in this user guide to comply with the Findata regulation and the Secodary Use Act**. Researches can access the data delivered for them only on SD Desktop service and via a specific Secondary Use type CSC project, which restricts the data access only to the authorized individuals and for the duration of the data permit.

<div class="grid cards" markdown>

- :material-check-circle:{ .lg .middle } **Key features**
  { .success-card }

    ---

    - User-friendly interface fully compatible with Chrome web browser.
    - Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).
    - Uploads up to 100 GB are automatically encrypted during upload via a web browser. For larger uploads, a programmatic tool (SD-lock/unlock) is available. Automated encryption key management.
    - Enhanced login security with multi-factor authentication (MFA).
    - Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data.
 
- :material-alert:{ .lg .middle } **Restrictions for secondary use**
  { .warning-card }

  ---

  - Each dataset must be uploaded to a dedicated bucket created by the Sensitive Data services team based on the data permits.
 
</div>

---

## 2. Login to SD Connect

### Step by step

1. **Navigate to [SD Connect](https://sd-connect.csc.fi)**. We recommend using Google Chrome for the best experience.
2. **Choose your login method**. Select CSC Login, Haka or Virtu then click Login.
3. **Enter your details**. Type in your username and password, then click Login.
4. **Verify your identity**. As a second verification step, enter the temporary code from your mobile authenticator app and click Continue. If prompted, please accept cookies to proceed.
5. You should now have access to SD Connect. If you see an additional message about identity verification, click Proceed to continue.
6. **Troubleshooting tip**. If you run into any issues, try clearing your browser history and cookies before logging in again. Note that Firefox private mode is not supported.

![SD Connect login](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Login.png)

---

## 3. Uploading and encrypting data

Files uploaded to SD Connect are automatically encrypted during upload using the service’s integrated key management system. This functionality supports all file types and formats, with a maximum upload size of 100 GB. Larger files can be uploaded programmatically.

SD Connect is built on a cloud object storage infrastructure. Files can only be uploaded into a bucket, created with SD Connect. Bucket is a top-level 'box' used to store files or folders, and each bucket can contain up to 500.000 segmented files. This has several implications for how your data should be organized and managed:

- **Once files are uploaded to SD Connect, they cannot be edited or modified**.
  
- **Uploading files into folders is not supported.** 

- **Upload duration**: Uploading large files or large batches may take several hours. Uploads are automatically stopped after 8 hours.
  
-  **File segmentation**: Uploaded files are automatically split into segments to optimize storage and performance. This segmentation is not visible in the user interface but can affect performance.
    
- The user interface might be slower when there are more than 2500 files in each folder. In this case please use the [command-line tools for upload and automated key management](./sd-connect-command-line-interface.md).
  
- File uploads are supported in Google Chrome and Mozilla Firefox (incognito mode not supported) browsers. On first use, a browser pop-up may request cookie consent. Accepting cookies enables file and folder uploads. 

### 3.1. Upload and encrypt files to an existing bucket

Sensitive Data support team will create a bucket in SD Connect for each dataset, share the bucket name with you, and grant Read-only access to the bucket for the CSC project in which the data users will analyze the data in the isolated SD Desktop environment.

One bucket is created for each dataset based on a data permit. In other words, each bucket contains only one dataset and should include all data covered by the same data permit.

Data users create their CSC projects based on their data permits and can access only the data uploaded to the bucket shared with their project. If the same data users have multiple separate data permits, the datasets must be uploaded to separate buckets, and the users must have separate CSC projects for each data permit.

#### Step by step instructions:

1. Select the correct project and the bucket created for the dataset.
![SD Connect Select bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket1.png)

2. Click **Upload** in the top right corner.
![SD Connect Start Upload to an existing bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket2.png)

3. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. Finally click **Upload** to start automatic encryption and upload.
![SD Connect Select bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket3.png)

!!! warning "Note"
    - Make sure you **use only SD Connect user interface or command line tools** for uploading data. If you use Allas user interface or command line tools, the data won't be encrypted, and the data storage is not compatible with the Findata regulation.
    - **Do not share the buckets directly with users** using a Share ID provided by the user. Access granted via a Share ID extends to the entire CSC project, which may include members not covered by the data permit. Only the Sensitive Data support team can verify that the project was created specifically for the shared dataset and contains only users authorized to process the data.
    - **Only "Read to SD Desktop" permission** for data sharing in SD Connect is compatible with the Findata regulation.

---

### 4. Manage datasets

The datasets will remain in your control after they are uploaded to the buckets and shared with the users. You can upload more data, remove files, and also remove the data access from the users.

1. **Delivering additional data**: You can add data to any existing dataset by [uploading new files to the bucket](#4-upload-each-dataset-to-a-dedicated-bucket) created for the data permit. Remember to use unique file names to avoid overwriting the old files.
2. **Removing corrupted or incorrect files**: You can remove data from any existing dataset by [deleting files from the bucket](sd-connect-delete.md). NOTE! If the users are no longer allowed to use these files in their analysis, you need to also request that they remove any possible working copies of the files from their SD Desktop environment.
3. **Cancelling the data access**: You can terminate the data access any time by [removing the sharing of the bucket](sd-connect-share.md#4-delete-sharing-permission) and/or [deleting the data files](sd-connect-delete.md). However, same applies here as with removing files: if the data can no longer be used in any analysis, the users need to be instructed to remove all working copies of the data.

---

<div class="grid cards" markdown>
  
- :material-alert:{ .lg .middle } **Data permit expiration and data deletion**
  { .warning-card }
  
    You can [delete datasets](sd-connect-delete.md) from your organisation's project independently in SD Connect. However, when a data permit expires, the Sensitive Data support team will delete all files associated with the dataset from your project.
    The data will be deleted 90 days after the project in which the data users analyze the data is closed, which usually corresponds to the data permit's expiration date. However, if the project is closed earlier, the data will be removed regardless of whether the data permit remains valid.
    CSC, as the service provider of the processing environment, removes the data in accordance with the regulations and CSC's data retention policy (see [General Terms of Use for CSC's Services for Research and Education](https://research.csc.fi/general-terms-of-use)).

</div>
