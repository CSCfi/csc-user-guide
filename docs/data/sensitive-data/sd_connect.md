# Store and share with SD Connect

## Overview

Sensitive Data (SD) Connect allows you to store and share sensitive research data. SD Connect serves as a workspace for collaborative research projects, facilitating data collection and sharing. Encrypted files stored in SD Connect are directly available for analysis, annotiation or editing via SD Desktop. 


### Key features

* User-friendly interface compatible with Chrome and Firefox (excluding private mode in Firefox).

* Use via web browser from your computer (Mac, Linux, or Windows) and from any location (no need to install specific programs or use a VPN).

* Automated encryption and data upload via a web browser for files up to 100 GB. Larger files (100<GB) can be encrypted using an application and uploaded programmatically.

* Supports encryption and storage of any file type: text files, images, audio files, video, and genetic data (default space 10 TB, additional space required contact [CSC Service Desk](../../support/contact.md)). In addition, you can describe or organize each file or bucket with specific tags. 

* Automated key management. 

* Enchanced security at login with multi-factor authentication (MFA).


### Limitations

* SD Connect is based on an object storage solution. Files are called objects, they are stored as file segments and can not be directly edited. All files (sensitive or non-sensitive, e.g. scripts) stored in SD Connect must be encrypted. 

*  The storage space remains available as long as the CSC project is active. All data will be deleted 90 days after account termination or project closure, accordingly to [CSC's General Terms of Use](https://research.csc.fi/general-terms-of-use). 

* CSC does not provide backups of the data stored in SD Connect. Therefore, we advise you to maintain **backups** of important datasets.

!!! Note
    Files uploaded using the automated encryption option between November 2, 2022, and December 2022 might be corrupted. This is because during data upload, files are split into short segments, and in some cases, the correct segment's order has been lost, making the files unreadable. Therefore, if you have used this function and can not re-upload a copy of the same data, don't hesitate to contact us at [CSC Service Desk](../../support/contact.md). We need to evaluate individual cases to determine if the files can be retrieved. Currently, SD Connect automated encryption is supported only for files <1GB.

!!! Note
    SD Connect is unsuitable for data processing under the Act on the Secondary Use of Health and Social Data. Please check [SD Desktop for secondary use](./sd-desktop-audited.md) to learn about the precise requirements.
