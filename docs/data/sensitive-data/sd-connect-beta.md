# SD Connect (Beta)

The updated SD Connect user interface offers automated file encryption and decryption (up to 100 GB) along with key management. Additionally, three levels of sharing permissions are accessible across CSC projects.

!!! info "Note"
    This version is in Open Beta, occasional service interruptions may occur. Please use this version for testing scenarios and avoid relying on it for storing critical data until it transitions to a stable release. Please provide feedback by [contacting CSC Service Desk](../../support/contact.md) (subject: Sensitive Data) to contribute to service improvement. Thank you for your cooperation.

Content:

[TOC]

## Overview of updates

| Feature                                             | SD Connect                      | SD Connect (Beta) NEW!                     |
|-----------------------------------------------------|---------------------------------------|------------------------------------------------|
| Url|  https://sd-connect.csc.fi (released April 2022)|  https://sd-connect.sd.csc.fi (available from December 2023) |
| Service access|   Based on CSC account and project, requires Allas service access| Based on CSC account and project, requires SD Connect (Beta) service access, Requires multi-factor authentication |   
| User interface |    -     |    Redesigned (based on user's feedback)    |  
| Automated encryption and upload via browser          | Limited to small files (<1 GB)         | Available for files up to 100 GB               |
| Automated decryption during download via browser    | Not available                       | Available for downloading entire folders or single files for all project members |
| Key management                                      | Not available                        | Provided automatically by the service |    
| Possibility of uploading and storing unencrypted files | Available as optional  |Not available, all files and subfolders are encrypted during upload|
| Folder sharing: read only via SD Desktop | Available  | Available|
| Folder sharing: data transfer | Manual encryption and decryption | Automated encryption and decryption |
| Folder sharing: data collection |Manual encryption and decryption   |  Automated encryption and decryption   |
| Command line utility tool                           | Automated encryption and key management not available | In test phase                                       |
| Compatibility with Allas| Files uploaded in Allas are visible and can be downloaded via SD Connect | File uploaded in Allas are visible, but cannot be downloaded or decrypted via SD Connect, file size is not correct|

## Service access 

To access SD Connect (Beta) follow [instructions](./sd-use-case-new-user-project-manager.md) and activate **SD Connect Beta** service.

## Login

Due to an ongoing technical challenge, double login is required. We apologize for the complexity of this process. Please follow these steps:

1. Navigate to <https://sd-connect.sd.csc.fi>. We suggest to use Google Chrome for optimal service performance, Firefox is also supported. Please, clear browser history and cookies if you have accessed the service before. 
2. Choose the login method (CSC Login, Haka) and click on *Login*. In the new page, enter username and password, and click on *Login*.
3. Verify your identity with the temporary code (Multi-factor authentication); click on *Continue*.
4. You might now encounter an additional page stating that your account needs to go through identity verification. Please press on *Proceed* to continue at the bottom of the message.
5. You will now be redirected one more time to the login page. Here, please select again the login method (Haka or CSC Login) and press on *Login*. In the new page, add again your username and password and press on *Login*. After this final step, you should be able to access the service. Please, clear browser history and cookies if errors occur.

[![Project](images/connect/beta-login.png)](images/connect/beta-login.png)

## Features in SD Connect 

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)