[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Transfer health and social data for secondary use via SD Connect

## On this page:

- [1. SD Connect overview](#1-sd-connect-overview)
- [2. Login to SD Connect](#2-login-to-sd-connect)
- [3. Uploading and encrypting data](#3-uploading-and-encrypting-data)

---

## 1. SD Connect overview

Sensitive Data (SD) Connect enables the secure storage and sharing of sensitive data. It automatically encrypts files during upload through an easy-to-use interface. For uploads larger than 100 GB, a command-line tool is available which also provides automated key management.

<div class="grid cards" markdown>

- :material-check-circle:{ .lg .middle } **Key features**
  { .success-card }

    ---

    - User-friendly interface fully compatible with Chrome web browser.
    - Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).
    - Uploads up to 100 GB are automatically encrypted and decrypted during upload and download via a web browser. For larger uploads, a programmatic tool (SD-lock/unlock) is available. Automated encryption key management.
    - Enhanced login security with multi-factor authentication (MFA).
    - Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data.
 
</div>

---

## 2. Login to SD Connect

### Step by step

1. **Navigate to [SD Connect](https://sd-connect.csc.fi)**. We recommend using Google Chrome for the best experience.
2. **Choose your login method**. Select CSC Login, Haka, Virtu or Life Science login then click Login.
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

#### 3.1. Upload and encrypt files to an existing bucket

1. Select the correct project and bucket.
![SD Connect Select bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket1.png)

2. Click **Upload** in the top right corner.
![SD Connect Start Upload to an existing bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket2.png)

3. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. Finally click **Upload** to start automatic encryption and upload.
![SD Connect Select bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_UploadExistingBucket3.png)

---
