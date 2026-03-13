[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Store and share with Sensitive Data Connect

- [Overview](#overview)
- [Key features](#key-features)
- [Limitations](#limitations)
- [Your next steps in this guide](#features-in-sd-connect)

## Overview

Sensitive Data (SD) Connect enables the secure storage and sharing of sensitive research data. It automatically encrypts files during upload and decrypts them during download through an easy-to-use interface. For files larger than 100 GB, a command-line tool is available which also provides automated key management.

SD Connect also supports collaborative research, allowing data collection and sharing within the platform. Files stored are encrypted and can be accessed for analysis, annotation, or editing through SD Desktop.

You can browse through the main topics of the manual using the navigation bar on the left side of this page or the search function.

## Key features

- User-friendly interface compatible fully compatible with Chrome web browser.
- Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).
- Files up to 100 GB are automatically encrypted and decrypted during upload and download via a web browser. For larger files, a programmatic tool (SD-lock/unlock) is available. Automated encryption key management.
- Enhanced login security with multi-factor authentication (MFA).
- Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data (default space 10 TB, if additional space is required, [contact CSC Service Desk](../../support/contact.md)).

## Limitations

Known temporary issues:

- Firefox in private mode is not supported.
- Tagging files is not currently supported.
- CSC projects created before 2013 are incompatible with the current user interface and will not be displayed. For assistance, please contact us.  
- In October 2024, SD Connect was updated. Files from the previous version are still compatible, but you may encounter issues due to file format changes. For step-by-step instructions on downloading files stored with the previous version, [please check this page](./sd-connect-download.md))

General considerations:

- SD Connect is based on an object storage solution. Files are called objects, they are stored as file segments and can not be directly edited. All files (sensitive or non-sensitive, e.g. scripts) stored in SD Connect must be encrypted.
- The storage space remains available as long as the CSC project is active. All data will be deleted 90 days after account termination or project closure, accordingly to [CSC's General Terms of Use](https://research.csc.fi/general-terms-of-use).
- CSC does not provide backups of the data stored in SD Connect. Therefore, we advise you to maintain **backups** of important datasets.
- SD Connect service only supports processing of encrypted files, whether sensitive or non-sensitive (e.g., scripts).

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
