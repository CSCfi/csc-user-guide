# SD Connect: release page

This page summarizes the major releases of SD Connect, highlighting improvements in usability, security, automation and data‑sharing workflows.


## SD Connect v2.0.0 – Major Upgrades (User interface October 2024, Command Line tools February 2025)

## Overview

SD Connect v2.0.0 introduces a significantly improved user experience with a redesigned web user interface, automated encryption features and expanded sharing workflows.

## Key features

- Service sccess via MyCSC: requires CSC account, CSC project membership, SD Connect service access and MFA.

- Redesigned web user interface: modern layout based on direct user feedback (Google Chrome and Firfox supported). 

- Improved upload and dowload perfomance: upload through UI supports files up to 100 GB. Larger files can be uploaded  and encrypted automatically via command line. Available for both folders and single files for all project members.

- Automated enryption, deryption and key management: fully automated key management during encryption and decryption provided by the service, via web user interface and command line tools. 

- Encrypted upload policy: uploading unencrypted files is no longer possible; all uploads are encrypted automatically.

- Advanced folder sharing: for data transfer, collaboration and read only via SD Desktop. Prevents unnecessary copies of data.

- Command‑Line tool improvements: the new command line tools, called SD Lock/Un-lock, now supports automated key management using temporary tokens, automate encryption and decryption. 

- Backward compatbolity: files uploaded with the service via user inetrface before 7 Oct 2024 will not be automatically decrypted. Files size may appear incorrect. 



| Feature | SD Connect v2.0.0  (currentky in use)| SD Connect v1.0.0 (discontinued) |
|---------|----------------|----------------------------------------|
|Service access via [MyCSC](https://my.csc.fi)|Requires CSC account and project, SD Connect service access and multi-factor authentication enabled on your CSC account|Requires CSC account and project and Allas service access|
|User interface|Redesigned based on user feedback|Standard interface|
|Automated encryption and upload|Upload via user interfaces supports files up to 100 GB, larger files can be automatically uploaded during upload via command line|Limited to files < 1 GB|
|Automated decryption and download|Available for folders or single files for all project members|Not available|
|Key management|Automatically provided by the service|Not available|
|Uploading encrypted files|Not allowed; all files are encrypted during upload|Optional; unencrypted files could be uploaded|
|Folder sharing|Supports 3 different type of data sharing: for data transfer, collection or collaborative analysis on SD Desktop (without the possibility of downloading extra copies of the files)|Sharing was supported only via manual encryption and decryption|
|Command-line utility tool|SD Lock/Un-lock provide automated key management, this requires temporary token access|Available but required manual encryption and did not support automated key management|
|Compatibility with Allas|Files uploaded with after October 7, 2024 are visible in Allas but not downloadable directly from it; size may be incorrect|Files visible and downloadable|


## SD Connect v1.0.0 – Original release June 2021 (Discontinued)

## Overview
The original version introduced the foundational storage and encryption concept, requiring more manual steps for secure handling of data. It has since been replaced by the new SD Connect.

## Key features 

- Service access: Required CSC account, CSC project and Allas service access.

- Standard user interface: basic interface for file operations.

- Limited upload size: Uploads with automated encryotion restricted to files under 1 GB.

- Download: manual decryotion required.

- Key management: users needed to manage their own encryption keys.

- Optional encryption: users could choose to upload unencrypted files.Sharing required manual encryption/decryption workflows.

- Command‑Line tool: Required full manual encryption; no automated key management.

