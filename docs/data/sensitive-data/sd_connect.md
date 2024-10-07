# Store and share with Sensitive Data Connect

## Overview

Sensitive Data (SD) Connect enables the secure storage and sharing of sensitive research data. It automatically encrypts files during upload and decrypts them during download through an easy-to-use interface. For files larger than 100 GB, a command-line tool is available which also provides automated key management.

SD Connect also supports collaborative research, allowing data collection and sharing within the platform. Files stored are encrypted and can be accessed for analysis, annotation, or editing through SD Desktop.


Contents:

* [Key features](./sd_connect.md#key-features)

* [Limitations](./sd_connect.md#limitations)

* [Overview of SD Connect 2.0 features](./sd_connect.md#overview-of-sd-connect-20-features)

You can browse through the main topics of the manual using the navigation bar on the left side of this page or the search function.


## Key features

* User-friendly interface compatible fully compatible with Chrome web browser.

* Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).

* Files up to 100 GB are automatically encrypted and decrypted during upload and download via a web browser. For larger files, a programmatic tool (SD-lock/unlock) is available. Automated encryption key management.

* Enhanced login security with multi-factor authentication (MFA).

* Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data (default space 10 TB, additional space required contact CSC Service Desk). 


## Limitations

Known temporary issues: 

* Firefox (except in private mode) is supported, but some known limitations exist.

* Tagging files is not currently supported.

* Accessing the service requires logging in twice by entering your username and password.
  
* In October 2024, SD Connect was updated. Files from the previous version are still compatible, but you may encounter issues due to file format changes. For step-by-step instructions on dowlaoding files stored witht eh previos version, please check this [information].(/sd-connect-download-old-version.md)

General considerations: 

* SD Connect is based on an object storage solution. Files are called objects, they are stored as file segments and can not be directly edited. All files (sensitive or non-sensitive, e.g. scripts) stored in SD Connect must be encrypted. 

*  The storage space remains available as long as the CSC project is active. All data will be deleted 90 days after account termination or project closure, accordingly to [CSC's General Terms of Use](https://research.csc.fi/general-terms-of-use). 

* CSC does not provide backups of the data stored in SD Connect. Therefore, we advise you to maintain **backups** of important datasets.

* SD Connect service only supports processing of encrypted files, whether sensitive or non-sensitive (e.g., scripts).


!!! Note
    SD Connect is unsuitable for data processing under the Act on the Secondary Use of Health and Social Data. Please check [SD Desktop for secondary use](./sd-desktop-audited.md) to learn about the precise requirements.


## Overview of SD Connect 2.0 features

The current version of the service, SD Connect 2.0, introduces several enhancements over the original version to improve user experience, security, performance, and automation. Below is a summary of the key new features and their differences compared to the previous version.

<table>
<tr>
<th>

Feature
</th>
<th>

SD Connect 2.0
</th>
<th>

SD Connect 1.0 (has been discontinued)
</th>
</tr>
<tr>
<td>

Service access via MyCSC (https://my.csc.fi/)
</td>
<td>

Requires CSC account and project, SD Connect service access and multi-factor authentication enabled on your CSC account
</td>
<td>

Requires CSC account and project and Allas service access
</td>
</tr>
<tr>
<td>

User interface
</td>
<td>Redesigned based on user feedback</td>
<td>Standard interface</td>
</tr>
<tr>
<td>

Automated encryption and upload
</td>
<td>Upload via user interfaces supports files up to 100 GB, larger files can be autmatically uplaoded during upload via command line
</td>
<td>

Limited to files < 1 GB
</td>
</tr>
<tr>
<td>

Automated decryption during download
</td>
<td>Available for folders or single files for all project members</td>
<td>Not available</td>
</tr>
<tr>
<td>

Key management
</td>
<td>Automatically provided by the service</td>
<td>Not available</td>
</tr>
<tr>
<td>

Uploading unencrypted files
</td>
<td>Not allowed; all files are encrypted during upload</td>
<td>Optional; unencrypted files could be uploaded</td>
</tr>
<tr>
<td>

Folder sharing 
</td>
<td> Supports 3 different type of data sharing: for data transfer, collection or collaborative analysis on Sd Desktop (without the possibility of downlaoding extra copis of the files) </td>
<td> Sharing was supported only via manual encryption and decryption</td>
</tr>
<tr>
<td>

Command line utility tool
</td>
<td>

SD Lock/Un-lock provide automated key management, this requires temporary token access.
</td>
<td> Available but required manual encryption and did not support automated key management</td>
</tr>
<tr>
<td>

Compatibility with Allas
</td>
<td>Files uploaded with after October 7, 2024 are visible in Allas but not downloadable directly from it; size may be incorrect.</td>
<td>Files visible and downloadable</td>
</tr>
</table>
