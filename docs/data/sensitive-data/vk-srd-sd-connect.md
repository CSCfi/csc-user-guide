
# Store and share with Sensitive Data Connect


## Overview

Sensitive Data (SD) Connect allows you to store sensitive research data in the CSC's cloud storage solution Allas. With this user interface, you can easily encrypt and upload files from your web browser. As a result, SD Connect can serve as a workspace for collaborative research projects, facilitating data collection and sharing.  In addition, encrypted files stored in SD Connect are directly available for analysis, annotiation or editing via the SD Desktop service. 

[![SDConnect-overview](images/connect/connect_overviewnew.png)](images/connect/connect_overviewnew.png)

Contents:

* [Key features](./sd_connect.md)
  
* [Authentication](./sd_connect.md#authentication)

* [User Interface](./sd_connect.md#user-interface)
  
* [Introduction to data encryption compatible with sensitive data services](./sd_connect.md#introduction-to-data-encryption-compatible-with-sensitive-data-services)
 
 * [Data encryption and upload for analysis (less than 1 GB)](./sd_connect.md#sensitive-data-encryption-and-upload-for-analysis-less-than-1-gb) (Default analysis)

* [Data encryption and upload for analysis (up to 100 GB)](./sd_connect.md#sensitive-data-encryption-and-upload-for-analysis-up-to-100-gb)
 
* [Data encryption and upload for storage and sharing (less than 1 GB)](./sd_connect.md#sensitive-data-encryption-and-upload-for-storage-and-sharing-less-than-1-gb) (Data storage and transfer)
 

* [Data sharing](./sd_connect.md#data-sharing) 
 
* [Data download and decryption](./sd_connect.md#data-download-and-decryption) (Data storage and transfer)
 
* [Command Line Interface: data encryption and upload](./sd_connect.md#command-line-interface-data-encryption-and-upload) (Advanced)
 
 
* [Command Line Interface: data encryption for data sharing](./sd_connect.md#command-line-interface-encryption-for-data-sharing) (Advanced)
 
* [Troubleshooting](./sd_connect.md#troubleshooting)


You can browse through the main topics of the manual using the navigation bar on the left side of this page or the search function.

## Key features

* Accessible via web browser from your computer (Mac, Linux, or Windows) and any location (no need to install specific programs or use a VPN).

* Automated encryption and data upload via a web browser for small files (1<GB). Larger files (100<GB) can be encrypted using an application and uploaded to the web browser or programmatically (100>GB).

* Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data (default space 10 TB, additional space required contact servicedesk@csc.fi). In addition, you can describe or organize each file or bucket with specific tags. 


**Limitations**:

* SD Connect is based on an object storage solution. Files are called objects, they are stored as file segments and can not be directly edited. All files (sensitive or non-sensitive, e.g. scripts) stored in SD Connect must be encrypted. 

* Automated encryption is currently limited to files <1GB. Lager files (up to 100 GB) can be encrypted with the Cryp4GH application and uploaded using SD Connect or programmatically (>100GB).

* SD Connect user interface is compatible with all modern web browsers but not supported during Firefox private browsing. 

*  The storage space remains available as long as the CSC project is active. All data will be deleted 90 days after account termination or project closure, accordingly to [CSC's General Terms of Use](https://research.csc.fi/general-terms-of-use). 

* CSC does not provide backups of the data stored in SD Connect. Therefore, we advise you to maintain **backups** of important datasets.

!!! Note
    Files uploaded using the automated encryption option between November 2, 2022, and December 2022 might be corrupted. This is because during data upload, files are split into short segments, and in some cases, the correct segment's order has been lost, making the files unreadable. Therefore, if you have used this function and can not re-upload a copy of the same data, don't hesitate to contact us at servicedesk@csc.fi. We need to evaluate individual cases to determine if the files can be retrieved. Currently, SD Connect automated encryption is supported only for files <1GB.


!!! Note
    SD Connect is unsuitable for data processing under the Act on the Secondary Use of Health and Social Data. Please check [SD Desktop for secondary use](./sd-desktop-audited.md) to learn about the precise requirements.



## Authentication

After creating a CSC account, a CCS project and appling for Allas service access, login to SD Connect is currently possible only with CSC credentials and  Haka (a user identity federation system) at:

   * [https://sd-connect.csc.fi](https://sd-connect.csc.fi) 


!!! Note
    The interface is compatible with all modern web browsers but does not support Firefox private browsing (incognito mode). 

[![SDConnect-login](images/connect/SDConnect-login.png)](images/connect/SDConnect-login.png)