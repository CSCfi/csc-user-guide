# Data management

## SD Desktop: CentOS 7 will no longer be supported after June 2024

We are implementing a security update for our virtual desktop operating system. As part of this update, the old operating system known as Linux CentOS 7 will no longer be supported after June 2024. Instead, we'll be transitioning exclusively to an operating system called Ubuntu for our virtual desktops. 

If you're currently using a virtual desktop with CentOS 7 and anticipate running your analyses beyond June, please reach out to us at **servicedesk@csc.fi *subject: Sensitive data***. We will assist you in evaluating whether there is a need to transition to a new virtual desktop and provide assistance with creating a plan for transferring your data and results accordingly.

## SD Desktop copy-paste functionality via Clipboard is now available, 7.3.2024
Copy-paste functionality via **Clipboard -feature** is now available in your virtual desktop, enabling easy transfer of text from your computer to your secure environment: [Copy-paste instructions for SD Desktop](../../data/sensitive-data/sd-desktop-access.md#copy-paste-from-your-laptop-to-virtual-desktop). 

* The Clipboard acts as a secure intermediary, facilitating the one-way transfer of data from your laptop to the virtual desktop, guaranteeing that copied text remains isolated from other processes and preventing unauthorized access to sensitive information.

* As a reminder, data exports from the virtual desktop are possible via the Data Gateway, and they are managed by the project manager or CSC's helpdesk. For more information please see [Export data from SD Desktop](../../data/sensitive-data/sd-desktop-export.md).

## SD Connect (Beta) now available, 13.12.2023

A new version of SD Connect is now available for testing purposes. The updated user interface offers automated file encryption and decryption (up to 100 GB) along with key management. Additionally, three levels of sharing permissions are accessible across CSC projects. This version is in Open Beta. Kindly use it for testing scenarios and avoid relying on it for storing critical data until it transitions to a stable release. Please provide feedback by [contacting CSC Service Desk](../contact.md) (subject: Sensitive Data) to contribute to service improvement.

Preliminary user guide is available [here](../../data/sensitive-data/sd-connect-beta.md)

## SD Desktop and SD Connect: service usage restrictions and CSC project closure, 8.9.2023

As of September 6, 2023, we have introduced two significant changes to our service usage according to CSC's data retention policies, which are currently in effect:

* Billing Unit consumption: when all billing units allocated to a CSC project have been consumed, access to the SD Desktop service will be restricted, and virtual desktops associated with the project will be automatically paused. This means that users will temporarily lose access to the SD Desktop service until additional billing units are allocated to the project.

* CSC Project closure: content stored within the SD Desktop and SD Connect services is subject to permanent deletion 90 days after the closure of a CSC project. **It is important to note that once data is deleted, it cannot be restored.**

To ensure that you are well-informed about these changes and your account status,  all project members will receive email notifications when billing units have been consumed and when a  CSC project is scheduled for closure. 



## SD Desktop: Ubuntu OS now available, 8.9.2023

You can now select the Ubuntu virtual desktop environment when creating a virtual desktop, alongside CentOS 7.
  

## Technical issues on SD Connect: follow up 2.2.2023

Files uploaded using the SD Connect automated encryption option between November 2, 2022, and December 20, 2022, might be corrupted. 
During the upload phase files are split into short segments, and in some cases, due to a technical issue, the correct segment's order has been lost, making the files unreadable. Therefore, if you have used this function, we advise you to upload a new copy of the files. If this is not possible, don't hesitate to contact us at servicedesk@csc.fi. We will evaluate individual cases to determine if the files can be retrieved. Currently, SD Connect automated encryption is supported only for files < 1GB. 



## Sensitive Data services now have an audited computing environment for secondary use of social and health data 8.6.2022

SD Desktop is a certified environment for data processing under the Act on the Secondary Use of Health and Social Data. However, the services provided for this purpose have specific limitations compared to the standard service.


