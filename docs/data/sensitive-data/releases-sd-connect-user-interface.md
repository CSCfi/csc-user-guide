# SD Connect: release Page

This page summarizes the major releases of SD Connect, highlighting improvements in usability, security, automation and data‑sharing workflows.


## SD Connect v2.0.0 – Major Enhancement Release ( User interface October 2024, Command Line tools February 2025)

### Overview
SD Connect v2.0.0 introduces a significantly improved user experience with a redesigned web user interface, automated encryption features and expanded sharing workflows.

## Key Features in v2.0.0

### Service Access via MyCSC

Requires CSC account, project membership, SD Connect service access and MFA.


### Redesigned User Interface

Modern layout based on direct user feedback.


### Improved upload and dowload perfomance

Upload through UI supports files up to 100 GB. Larger files can be uploaded automatically via command line. Available for both folders and single files for all project members.


### Automated Key Management

Fully automated key management during encryption and decryption provided by the service, via web user interface and command line tools. 


### Encrypted Upload Policy

Uploading unencrypted files is no longer possible; all uploads are encrypted automatically.


### Advanced Folder Sharing

Three supported modes: Data transfer, collaboration and read only via SD Desktop. Prevents unnecessary copies of data.


### Command‑Line Tool Improvements

The new command line tools, called SD Lock/Un-lock, now supports automated key management using temporary tokens.


### Backward compatbolity
Files uploaded before 7 Oct 2024 are visible in Allas (not downloadable; size may appear incorrect).



| Feature | SD Connect v2.0.0 | SD Connect v1.0.0 (discontinued) |
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


## SD Connect v1.0.0 – Original Release June 2021 (Discontinued)

## Overview
The original version introduced the foundational storage and encryption concept, requiring more manual steps for secure handling of data. It has since been replaced by the new SD Connect.

## Key Capabilities in v1.0.0

### Service Access Requirements

Required CSC account, project, and Allas service access.


### Standard User Interface

Basic interface for file operations.


### Limited Upload Size

Uploads with automated encryotion restricted to files under 1 GB.


### No Automated Decryption or Download

Manual operations required.


### Manual Key Management

Users needed to manage their own encryption keys.


### Optional Encryption

Users could choose to upload unencrypted files.


### Sharing Via Manual Processes

Sharing required manual encryption/decryption workflows.


### Command‑Line Tool

Required full manual encryption; no automated key management.


### Allas Compatibility

Files visible and downloadable.
