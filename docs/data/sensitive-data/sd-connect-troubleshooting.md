---
hide:
  - toc
---


# Troubleshooting

| Problem | Description | Solution |
|---------|-------------|----------|
|Service access|I can not access SD Connect|1. Verify in the MyCSC portal if your CSC project has service access to SD Connect and accepted CSC’s terms of use.<br>2. Link your Haka account to your CSC account.<br>3. SD Connect is not supported during private browsing with Firefox (incognito mode).|
||I can not access SD Connect, an error tells me that it was not possible to perform elevation/authentication|Activate multi-factor authentication (MFA) on your CSC profile in the MyCSC portal (necessary since October 2024). [See more details here](../../accounts/mfa.md).|
||I end up in a loop of login requests|We suggest you to use Chrome as better supported browser. If you are using Firefox, login will be again successful if you clear history and cookies.|
|Data access|I no longer can see my CSC project|CSC projects created before 2013 are not supproted by the user interface. Please contact us for support|
||I can not see files uploaded via an older version of SD Connect|Unencrypted files are no longer visible using SD Connect 2.0 since October 2024.|
||I can not access files stored in SD Connect using SD Desktop|Unencrypted files are not accessible via the SD Desktop service (you can use a Allas user interfaces for managing non encrypted data). Only files encrypted using the SD service encryption key are visible in the secure computing environment (or encrypted using SD Connect default option). Refresh the Data Gateway application.|
|Folder creation|I can not create a new folder|Try using a unique folder name that doesn’t contain special characters. Select the correct CSC project in the SD Connect user interface.|
|Folder not visible|I cannot find my folder|Check if the folder is stored under a different project. If someone has shared the folder with you, you can find it under the Shared to section and copy it. If someone shared the folder with you, they could have revoked the sharing permissions.|
|Folder deletion|I can not delete an empty folder|If the folder has been created in November or December 2022, [contact CSC Service Desk](../../support/contact.md) (subject: sensitive data).|
|Manual decryption with Crypt4gh|Cannot open or decrypt files downloaded from SD Connect|1. You can not decrypt files that have been encrypted with the SD Connect user interface and default option before October 2024. In this case, the files have been encrypted with the service-specific encryption key and are automatically decrypted when accessed using the SD Desktop service. Please [contact CSC Service Desk](../../support/contact.md) for support.<br>2. Add the extension `.c4gh` to the downloaded files if it is missing and decrypt it using your private encryption key.|
|Data upload - dowload|I am trying to upload a large file/folder with the user interface, and the upload is not responding|Files or folders larger than 100 GB should be uploaded programmatically. SD Connect user interface supports only data uploads that last up to 8 hours.|
||I cannot upload data into my folder|Check if your CSC project has storage space left and apply for more quota. [See more details here](../../accounts/how-to-increase-disk-quotas.md).|
||Low upload speed (programmatically)|Upload and download speed depends on the local network.|
|Shared folder|I cannot upload data into a shared folder|Only folders shared with 'collect' permissions allow data uploads.|
||I cannot download the content of a shared folder|Only folders shared with 'transfer' or 'collect' permissions allows you to download a copy of the content.|
|Tags|Adding tag does not work|Currently tag feature is not supported|

## Features in SD Connect

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)
