[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)


# Troubleshooting

## On this page: 


- [1. Reporting an issue](#1-reporting-an-issue)
- [2. List of most comment problems](#2-list-of-most-comment-problems)
- [3. Firefox: Interrupted upload workaround](#3-firefox-interrupted-upload-workaround)



!!! Note
    Below you will find solutions to the most common issues encountered with SD Connect. If you need further assistance, please don't hesitate to contact servicedesk@csc.fi with the subject line "SD Services".

## 1. Reporting an issue

If you experience problems when uploading or downloading files, you can export a log of your SD Connect session. The log contains technical information that can help investigate the issue.

To export the session logs:

- When the issue occurs, do not close your browser or log out from the service. 
- Go to the SD Connect home page.
- Select **Support** in the top-right corner.
- From the drop-down menu, select **Export session logs.**
- A file named sd-connect-log-[date].log will be downloaded to your computer.
- Send the log file to servicedesk@csc.fi with the subject SD Connect and include a short description of the issue you encountered.


## 2. List of most comment problems


| Problem | Description | Solution |
|---------|-------------|----------|
|Service access|I can not access SD Connect|1. Verify in the MyCSC portal if your CSC project has service access to SD Connect and accepted CSC’s terms of use.<br>2. Link your Haka account to your CSC account.<br>3. SD Connect is not supported during private browsing with Firefox (incognito mode).|
||I can not access SD Connect, an error tells me that it was not possible to perform elevation/authentication|Activate multi-factor authentication (MFA) on your CSC profile in the MyCSC portal (necessary since October 2024). [See more details here](../../accounts/mfa.md).|
||I end up in a loop of login requests|We suggest you to use Chrome as better supported browser. If you are using Firefox, login will be again successful if you clear history and cookies.|
|Label next to bucket name| There is the label *urgent* or *by the end of 2026* next to the bucket name |Bucket needs to be converted to a new format to regain access or show correct size|
|Data access|I no longer can see my CSC project| CSC projects created before 2013 are not supported by the user interface. Please contact us for support|
||I can not access files stored in SD Connect using SD Desktop service |Unencrypted files are not accessible via the SD Desktop service. Only files encrypted using the SD Connect (user interface or programmatically) are visible in the secure computing environment.|
|Bucket creation|I can not create a new bucket |Try using a unique bucket name that doesn’t contain special characters. Select the correct CSC project in the SD Connect user interface.|
|Bucket not visible|I cannot find a bucket |Check if the bucketis stored under a different project. If someone has shared the folder with you, you can find it under the Shared to section and copy it. If someone shared the folder with you, they could have revoked the sharing permissions.|
|Manual decryption with Crypt4gh|Cannot open or decrypt files downloaded from SD Connect|1. You can not decrypt files that have been encrypted with the SD Connect user interface and default option before October 2024. In this case, the files have been encrypted with the service-specific encryption key and are automatically decrypted when accessed using the SD Desktop service. Please [contact CSC Service Desk](../../support/contact.md) for support.<br>2. Add the extension `.c4gh` to the downloaded files if it is missing and decrypt it using your private encryption key.|
|Data upload - download|I am trying to upload a large file/folder with the user interface, and the upload is not responding|Files or folders larger than 100 GB should be uploaded programmatically. SD Connect user interface supports only data uploads that last up to 8 hours.|
||I cannot upload data into a bucket|Check if your CSC project has storage space left and apply for more quota. [See more details here](../../accounts/how-to-increase-disk-quotas.md).|
||Low upload speed (programmatically)|Upload and download speed depends on the local network.|
|Shared bucket|I cannot upload data into a shared bucket|Only folders shared with 'collaborate' permissions allow data uploads.|
||I cannot download the content of a shared bucket|Only folders shared with 'transfer' or 'collaborate' permissions allows you to download a copy of the content.|



## 3. Firefox: Interrupted upload workaround

If you encounter issues with file uploads or downloads in Firefox, try the following steps: 

1. Open **SD Connect** in Firefox.
2. Click the **☰ menu** in the top-right corner of Firefox.
3. Select **More tools**.
4. Select **Web Developer Tools**.
5. Select the **Application** tab.
    - If **Application** is not visible, select **`>>`** and then **Application**.
6. From the left-hand menu, select **Service Workers**.
7. Find the service worker associated with **SD Connect** and select **Unregister**.
8. Close Developer Tools and refresh the **SD Connect** page.
9. Try uploading or downlaoding the file again.







## Features in SD Connect

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)
