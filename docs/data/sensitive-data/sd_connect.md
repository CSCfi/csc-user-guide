# Store and share with Sensitive Data Connect

## Overview

Sensitive Data (SD) Connect allows you to store and share sensitive research data. The service provides a user interface that automatically encrypts files during upload and automatically decrypts them during downland. For large files (>100 GB), a command line tool can be used.

SD Connect serves as a workspace for collaborative research projects, facilitating data collection and sharing. Encrypted files stored in SD Connect are directly available for analysis, annotation or editing via SD Desktop.

Contents:

* [Key features](./sd_connect.md#key-features)

* [Limitations](./sd_connect.md#limitations)

* [Overview of SD Connect 2.0 features](./sd_connect.md#overview-of-sd-connect-20-features)

You can browse through the main topics of the manual using the navigation bar on the left side of this page or the search function.


## Key features

* User-friendly interface compatible with fully compatible by Chrome. Firefox (excluding private mode in Firefox) **can be also used, but there are some known limitations.**

* Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).

* Files up to 100 GB are automatically encrypted and decrypted during upload and download via a web browser. For larger files, a programmatic tool (SD-lock/unlock) is available. Automated encryption key management.

* Enhanced login security with multi-factor authentication (MFA).

* Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data (default space 10 TB, additional space required contact CSC Service Desk). **In addition, you can** describe or organize each file or folder with specific tags.


## Limitations

* SD Connect is based on an object storage solution. Files are called objects, they are stored as file segments and can not be directly edited. All files (sensitive or non-sensitive, e.g. scripts) stored in SD Connect must be encrypted. 

* Automated encryption is currently limited to files < 1GB. Larger files (up to 100 GB) can be encrypted with the Cryp4GH application and uploaded using SD Connect or programmatically (>100GB).

* SD Connect user interface is compatible with all modern web browsers but not supported during Firefox private browsing. 

*  The storage space remains available as long as the CSC project is active. All data will be deleted 90 days after account termination or project closure, accordingly to [CSC's General Terms of Use](https://research.csc.fi/general-terms-of-use). 

* CSC does not provide backups of the data stored in SD Connect. Therefore, we advise you to maintain **backups** of important datasets.

* SD Connect service only supports processing of encrypted files, whether sensitive or non-sensitive (e.g., scripts).

* A new version of SD Connect was released in October 2024. Files uploaded with the previous version are still compatible with the new interface, but you may experience issues due to changes in the file format. If you encounter any difficulties, please contact us. For more details on the changes, please refer to link.


!!! Note
    SD Connect is unsuitable for data processing under the Act on the Secondary Use of Health and Social Data. Please check [SD Desktop for secondary use](./sd-desktop-audited.md) to learn about the precise requirements.


## Overview of SD Connect 2.0 features

**SD Connect 2.0** introduces several enhancements over the original version of the service, aimed at improving user experience, security, performance and automation. Below is a summary of the key features and their differences compared to the  **SD Connect 1.0**.

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
<td>

Supports files up to 100 GB
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
<td>Automated encryption and decryption for data transfer</td>
<td>Manual encryption and decryption</td>
</tr>
<tr>
<td>

Command line utility tool
</td>
<td>

SD Lock/Un-lock provide automated key management, this requires temporary token access.
</td>
<td>Not available</td>
</tr>
<tr>
<td>

Compatibility with Allas
</td>
<td>Files uploaded with after October 7, 2024 are visible in Allas but not downloadable; size may be incorrect.</td>
<td>Files visible and downloadable</td>
</tr>
</table>
