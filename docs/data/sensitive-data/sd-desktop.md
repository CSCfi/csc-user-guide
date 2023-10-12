# Analyse and compute with Sensitive Data Desktop

## Overview

Sensitive Data (SD) Desktop allows you to analyze sensitive research data from your web browser securely. With this user interface, you can easily manage (start, use, delete) a virtual computer (here called desktop, technically defined as virtual machine). In addition, SD Desktop provides a secure workspace for collaborative research projects. 

[![Desktop-overview](images/desktop/desktop_overviewnew1.png)](images/desktop/desktop_overviewnew1.png)


### Key features

* Accessible from any operating system (Mac, Linux or Windows) via a web browser (e.g., Google Chrome, Firefox) from the public internet (without the need to install a client or use a VPN).

* Only members of the same CSC project can access the virtual desktop. One CSC project can create up to three desktops. 

* Four pre-built computing options (Linux OS) are available (for simple statistical analysis and machine learning).  Supports analysis of any data type: text files, images, audio files, video, and genetic data. Further customisation is possible by writing to servicedesk@csc.fi (subject: Sensitive data);

* The secure analysis environment is isolated from the internet: the only way to import and export data is via the SD Connect service.


**Limitations**:

* The project manager's or group leader's responsibility is to frequently review the list of members belonging to a project in MyCSC and verify who can access SD Desktop or SD Connect. Remove the project members who do not need access to the data when their contribution is no longer needed.

* Only open-source software is available. We do not provide virtual desktops with GPUs, Windows, or Linux Ubuntu operating systems. 

!!! Note 
    The standard SD Desktop service is unsuitable for data processing under the Secondary Use of Health and Social Data Act. Please check this manual: [SD Desktop for secondary use](./sd-desktop-audited.md) to learn about the precise requirements and access datasets approved by the Findata authority.



### Authentication

Login to SD Desktop is possible with identity federation systems (Haka, Virtu, CSCLogin or LSLogin) at:

[**https://sd-desktop.csc.fi**](https://sd-desktop.csc.fi)

from any modern web-browser.

After entering your username and password, you need to verify your identity with a second verification step (or Multi-factor Authentication, MFA). Enter the verification code provided via mobile application and press on _Continue_.

For specific guidance, see the [MFA section](../../accounts/mfa.md).

[![Authentication](images/desktop/desktop_login-mfa1.png)](images/desktop/desktop_login-mfa1.png)

