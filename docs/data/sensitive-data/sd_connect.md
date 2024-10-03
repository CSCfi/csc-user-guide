# Store and share with Sensitive Data Connect

## Overview

Sensitive Data (SD) Connect allows you to store sensitive research data in the CSC's cloud storage solution Allas. With this user interface, you can easily encrypt and upload files from your web browser. As a result, SD Connect can serve as a workspace for collaborative research projects, facilitating data collection and sharing.  In addition, encrypted files stored in SD Connect are directly available for analysis, annotation or editing via the SD Desktop service. 

Contents:

* [Key features](./sd_connect.md#key-features)

* [Limitations](./sd_connect.md#limitations)

* [User interface](./sd_connect.md#user-interface)

You can browse through the main topics of the manual using the navigation bar on the left side of this page or the search function.


## Key features

* Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).

* Automated encryption and data upload via a web browser for small files (<1GB). Larger files (<100GB) can be encrypted using an application and uploaded to the web browser or programmatically (>100GB).

* Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data (default space 10 TB, additional space required contact [CSC Service Desk](../../support/contact.md)). In addition, you can describe or organize each file or bucket with specific tags. 


## Limitations

* SD Connect is based on an object storage solution. Files are called objects, they are stored as file segments and can not be directly edited. All files (sensitive or non-sensitive, e.g. scripts) stored in SD Connect must be encrypted. 

* Automated encryption is currently limited to files <1GB. Larger files (up to 100 GB) can be encrypted with the Cryp4GH application and uploaded using SD Connect or programmatically (>100GB).

* SD Connect user interface is compatible with all modern web browsers but not supported during Firefox private browsing. 

*  The storage space remains available as long as the CSC project is active. All data will be deleted 90 days after account termination or project closure, accordingly to [CSC's General Terms of Use](https://research.csc.fi/general-terms-of-use). 

* CSC does not provide backups of the data stored in SD Connect. Therefore, we advise you to maintain **backups** of important datasets.

!!! Note
    Files uploaded using the automated encryption option between November 2, 2022, and December 2022 might be corrupted. This is because during data upload, files are split into short segments, and in some cases, the correct segment's order has been lost, making the files unreadable. Therefore, if you have used this function and can not re-upload a copy of the same data, don't hesitate to contact us at [CSC Service Desk](../../support/contact.md). We need to evaluate individual cases to determine if the files can be retrieved. Currently, SD Connect automated encryption is supported only for files <1GB.

!!! Note
    SD Connect is unsuitable for data processing under the Act on the Secondary Use of Health and Social Data. Please check [SD Desktop for secondary use](./sd-desktop-audited.md) to learn about the precise requirements.


## Overview of SD Connect 2.0 features

**SD Connect 2.0** introduces several enhancements over the original version of the service, aimed at improving user experience, security, performance and automation. Below is a summary of the key features and their differences compared to the  **SD Connect 1.0**.

<table>
<tr>
<th>

**Feature**
</th>
<th>

**SD Connect 2.0**
</th>
<th>

**SD Connect 1.0 (has been discontinued)**
</th>
</tr>
<tr>
<td>

**Service Access via** [https://my.csc.fi](https://my.csc.fi/welcome)
</td>
<td>

* CSC account and project
* Requires SD Connect service access
* Requires multi-factor authentication enable on your CSC account
</td>
<td>

CSC account and project

Requires Allas  service access
</td>
</tr>
<tr>
<td>

**User Interface**
</td>
<td>Redesigned based on user feedback</td>
<td>Standard interface</td>
</tr>
<tr>
<td>

**Automated Encryption and Upload**
</td>
<td>

Supports files up to **100 GB**
</td>
<td>

Limited to files \< **1 GB**
</td>
</tr>
<tr>
<td>

**Automated Decryption During Download**
</td>
<td>Available for folders or single files for all project members</td>
<td>Not available</td>
</tr>
<tr>
<td>

**Key Management**
</td>
<td>Automatically provided by the service</td>
<td>Not available</td>
</tr>
<tr>
<td>

**Uploading unencrypted files**
</td>
<td>Not allowed; all files are encrypted during upload</td>
<td>Optional; unencrypted files could be uploaded</td>
</tr>
<tr>
<td>

**Folder sharing** 
</td>
<td>Automated encryption and decryption for data transfer</td>
<td>Manual encryption and decryption</td>
</tr>
<tr>
<td>

**Command Line utility tool**
</td>
<td>

* SD-Lock Un-Lock provide automated key management
* requires temporary token access
</td>
<td>Not available</td>
</tr>
<tr>
<td>

**Compatibility with Allas**
</td>
<td>Files uploaded with after October 7, 2024 are visible in Allas but not downloadable; size may be incorrect</td>
<td>Files visible and downloadable</td>
</tr>
</table>

###
