[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Transfer health and social data for secondary use via SD Connect

## Prerequisites

- [Access SD Connect as a Data Controller for secondary use of health and social data](sd-use-case-secondary-use-data-controller.md)

## On this page:

1. [Overview](#1-delivering-secondary-use-data-via-sd-connect---overview): Delivering secondary use data via SD Connect
2. [Login to SD Connect](#2-login-to-sd-connect)
3. [Upload and encrypt data](#3-upload-and-encrypt-data)
4. [Manage datasets](#4-manage-datasets)

---

## 1. Overview

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

## 3. Upload and encrypt data

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

#### Step by step

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

## 4. Manage datasets

The datasets will remain in your control after they are uploaded to the buckets and shared with the users. You can upload more data, remove files, and also remove the data access from the users.

### 4.1 Delivering additional data

You can add data to any existing dataset by [uploading new files to the bucket](#31-upload-and-encrypt-files-to-an-existing-bucket) created for the data permit. Remember to use unique file names to avoid overwriting the old files.

---

### 4.2 Removing corrupted or incorrect files

You can remove data from any existing dataset by deleting files from the bucket.

!!! warning If the researchers are no longer allowed to use these files in their analysis, you need to also request them to remove any possible working copies of the files from their SD Desktop environment.

#### 4.2.1 Deleting a file

1. Select the correct project and bucket.
![SD Connect Select bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket1.png)

2. Click **Delete** on right side of each file you want to delete.
![Delete a file](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Delete.png)

3. Confirm by clicking **Delete items** from the notification.
![SD Connect Confirm delete](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_DeleteConfirm.png)

---

#### 4.2.2 Deleting multiple files

1. Select the correct project and bucket.
2. Select **Display options** from top right corner of file list. Then select **Hide pagination** from the same menu. Now all files are displayed on one page. 
![SD Connect Display options](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_DeleteMultiple1.png)

3. Select **checkbox** on top left corner of the file list. Click **Delete** from the toolbar appearing on top of file list.
![SD Connect Delete files](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_DeleteMultiple2.png)
4. Confirm by clicking **Delete items** from the notification.
![SD Connect Confirm delete](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_DeleteConfirmMultiple.png)

---

#### 4.2.3 Deleting subfolder

1. Select the correct project and bucket.
2. Find correct subfolder and open it.
3. Delete all files inside the subfolder, [see instructions](#422-deleting-multiple-files). Subfolder is deleted automatically when all files in it are deleted.

---

### 4.3 Cancelling the data access

!!! warning If the researchers are no longer allowed to use these files in their analysis, you need to also request them to remove any possible working copies of the files from their SD Desktop environment.

#### 4.3.1 Delete the data files

You can cancel the data access permanently by [deleting the data files](#422-deleting-multiple-files). 

#### 4.3.2 Delete sharing permission

In addition, you can cancel the data access either permanently or temporarily by deleting the sharing permissions from the bucket.

1. Select correct project from the top-left corner. Click **Share** button on the right side of the bucket.
![Share](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Share1.png)

2. In the Share window **scroll down to This project is shared to title**. Delete permission by clicking **Delete** button on the right side of the project.
![Change permissions](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareDeletePermission1.png)

3. A notification will open above the project list. **You may have to scroll up to see it.** Confirm your choise by clicking **Delete Permissions** button.
![Accept](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareDeletePermission2.png)


---

<div class="grid cards" markdown>
  
- :material-alert:{ .lg .middle } **Data permit expiration and data deletion**
  { .warning-card }
  
    You can [delete datasets](#422-deleting-multiple-files) from your organisation's project independently in SD Connect. However, when a data permit expires, the Sensitive Data support team will delete all files associated with the dataset from your project.
    The data will be deleted 90 days after the project in which the data users analyze the data is closed, which usually corresponds to the data permit's expiration date. However, if the project is closed earlier, the data will be removed regardless of whether the data permit remains valid.
    CSC, as the service provider of the processing environment, removes the data in accordance with the regulations and CSC's data retention policy (see [General Terms of Use for CSC's Services for Research and Education](https://research.csc.fi/general-terms-of-use)).

</div>
