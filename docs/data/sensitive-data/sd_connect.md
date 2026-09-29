[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Store and share with Sensitive Data Connect


## On this page: 

- [Overview](#overview): understand the key features and limitations
- [General considerations](#general-considerations): learn what to consider before getting started


## Overview

Sensitive Data (SD) Connect enables the secure storage and sharing of sensitive research data. It automatically encrypts files during upload and decrypts them during download through an easy-to-use interface. For uploads larger than 100 GB, a command-line tool is available which also provides automated key management.

SD Connect also supports collaborative research, allowing data collection and sharing within the platform. Files stored are encrypted and can be accessed for analysis, annotation, or editing through SD Desktop.

You can browse through the main topics of the manual using the navigation bar on the left side of this page or the search function.


<div class="grid cards" markdown>

- :material-check-circle:{ .lg .middle } **Key features**
  { .csc-grid-card-success }

    ---

    - User-friendly interface fully compatible with Chrome web browser.
    - Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).
    - Uploads up to 100 GB are automatically encrypted and decrypted during upload and download via a web browser. For larger uploads, a programmatic tool (SD-lock/unlock) is available. Automated encryption key management.
    - Enhanced login security with multi-factor authentication (MFA).
    - Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data (default space 10 TB, if additional space is required, [contact CSC Service Desk](../../support/contact.md)).
 


- :material-close-circle:{ .lg .middle } **Limitations**
  { .csc-grid-card-error }


    Known temporary issues:

    - Firefox in private mode is not supported.
    - CSC projects created before 2013 are incompatible with the current user interface and will not be displayed. For assistance, please contact servicedesk@csc.fi (subject: SD Connect)
    - Files stored with earlier versions can still be accessed, but additional steps may be required. Accessing files before September 2026 may require [bucket name conversion](./sd-connect-conversion.md), while files uploaded before October 2024 require [manual decryption](./sd-connect-download.md))
  
</div>

### General considerations:

- SD Connect is based on an object storage solution. Files are stored as objects, which consist of file segments and cannot be directly edited. All files stored in SD Connect, whether sensitive or non-sensitive (e.g., scripts), must be encrypted.
- The storage space remains available as long as the CSC project is active. All data will be deleted 90 days after account termination or project closure, according to [CSC's General Terms of Use](https://research.csc.fi/general-terms-of-use).
- CSC does not provide backups of the data stored in SD Connect. Therefore, we advise you to maintain **backups** of important datasets.
- Only files encrypted using SD Connect are visible via SD Desktop services.
- **Consider network connection when transferring large files. Transfer speed can vary significantly depending on the connection type, available bandwidth and network traffic**. For example, a 50 GB file upload takes approximately 1 hour and 30 minutes using a connection with measured speeds of 60 Mbps download and 80 Mbps upload.


!!! Note
    SD Connect is unsuitable for data processing under the Act on the Secondary Use of Health and Social Data. Please check [SD Desktop for secondary use](./sd-desktop-audited.md) to learn about the precise requirements.


## Features in SD Connect

- [Login](./sd-connect-login.md)
- [Upload](./sd-connect-upload.md)
- [Share](./sd-connect-share.md)
- [Download](./sd-connect-download.md)
- [Delete](./sd-connect-delete.md)
- [Command line interface](./sd-connect-command-line-interface.md)
- [Troubleshooting](./sd-connect-troubleshooting.md)
