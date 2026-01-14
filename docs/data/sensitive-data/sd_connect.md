[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Store and share with Sensitive Data Connect

- [Overview](#overview)
- [Key features and limitations](#key-features-and-limitations)
- [Version history](#version-history)
- [Your next steps in this guide](#features-in-sd-connect)

## Overview

!!! Note
    SD Connect is unsuitable for data processing under the Act on the Secondary Use of Health and Social Data. Please check [SD Desktop for secondary use](./sd-desktop-audited.md) to learn about the precise requirements.

Sensitive Data (SD) Connect enables the secure storage and sharing of sensitive research data. It automatically encrypts files during upload and decrypts them during download through an easy-to-use interface. For files larger than 100 GB, a command-line tool is available which also provides automated key management.

SD Connect also supports collaborative research, allowing data collection and sharing within the platform. Files stored are encrypted and can be accessed for analysis, annotation, or editing through SD Desktop.

You can browse through the main topics of the manual using the navigation bar on the left side of this page or the search function.

## Key features and limitations

<div class="grid cards" markdown>

- :material-check-circle-outline:{ .lg .middle } **Key features**

    ---

    - User-friendly interface compatible fully compatible with Chrome web browser.
    - Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).
    - Files up to 100 GB are automatically encrypted and decrypted during upload and download via a web browser. For larger files, a programmatic tool (SD-lock/unlock) is available. Automated encryption key management.
    - Enhanced login security with multi-factor authentication (MFA).
    - Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data (default space 10 TB, if additional space is required, [contact CSC Service Desk](../../support/contact.md)).

- :material-alert-outline:{ .lg .middle } **Limitations**

    ---

    - Firefox in private mode is not supported.
    - Tagging files is not currently supported.
    - CSC projects created before 2013 are incompatible with the current user interface and will not be displayed. For assistance, please contact us.  
    - In October 2024, SD Connect was updated. Files from the previous version are still compatible, but you may encounter issues due to file format changes. For step-by-step instructions on downloading files stored with the previous version, [please check this page](./sd-connect-download.md))

</div>



<div class="grid cards" markdown>

- :material-information-outline:{ .lg .middle } **General considerations**

    ---

    - SD Connect is based on an object storage solution. Files are called objects, they are stored as file segments and can not be directly edited. All files (sensitive or non-sensitive, e.g. scripts) stored in SD Connect must be encrypted.
    - The storage space remains available as long as the CSC project is active. All data will be deleted 90 days after account termination or project closure, accordingly to [CSC's General Terms of Use](https://research.csc.fi/general-terms-of-use).
    - CSC does not provide backups of the data stored in SD Connect. Therefore, we advise you to maintain **backups** of important datasets.
    - SD Connect service only supports processing of encrypted files, whether sensitive or non-sensitive (e.g., scripts).

</div>


## Version history

### Version 2.0 (current version):

In October 2024 we introduced several enhancements over the original version to improve user experience, security, performance, and automation. Below is a summary of the key new features.

> * **Service Access via MyCSC**:
Requires CSC account and project, SD Connect service access, and multi-factor authentication enabled on your CSC account.

> * **User Interface**:
Redesigned based on user feedback.

> * **Automated Encryption and Upload**:
Upload via user interfaces supports files up to 100 GB; larger files can be automatically uploaded via command line.

> * **Automated Decryption and Download**:
Available for folders or single files for all project members.

> * **Key Management**:
Automatically provided by the service.

> * **Uploading Encrypted Files**:
Not allowed; all files are encrypted during upload.

> * **Folder Sharing**:
Supports three types of data sharing:

> * **Data transfer and Collection**:
Collaborative analysis on SD Desktop (without downloading extra copies).

> * **Command-Line Utility Tool**:
SD Lock/Unlock provides automated key management; requires temporary token access.

> * **Compatibility with Allas**:
Files uploaded after October 7, 2024 are visible in Allas but not downloadable directly; size may be incorrect.

### Previous version (discontinued):

> * **Service Access via MyCSC**:
Requires CSC account and project and Allas service access.

> * **User Interface**:
Standard interface.

> * **Automated Encryption and Upload**:
Limited to files < 1 GB.

> * **Automated Decryption and Download**:
Not available.

> * **Key Management**:
Not available.

> * **Uploading Encrypted Files**:
Optional; unencrypted files could be uploaded.

> * **Folder Sharing**:
Sharing supported only via manual encryption and decryption.

> * **Command-Line Utility Tool**:
Available but required manual encryption and did not support automated key management.

> * **Compatibility with Allas**:
Files visible and downloadable.


## Features in SD Connect

- [Login](./sd-connect-login.md)
- [Upload](./sd-connect-upload.md)
- [Share](./sd-connect-share.md)
- [Download](./sd-connect-download.md)
- [Delete](./sd-connect-delete.md)
- [Command line interface](./sd-connect-command-line-interface.md)
- [Troubleshooting](./sd-connect-troubleshooting.md)
