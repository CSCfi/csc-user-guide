# Data management


## SD Desktop and SD Connect: service usage restrictions and CSC project closure (Effective from September 6, 2023)

As of September 6, 2023, we have introduced two significant changes to our service usage accordinggly to CSC's data retention policies, which are currently in effect:

* Billing Unit consumption: When all billing units allocated to a CSC project have been consumed, access to the SD Desktop service will be restricted, and virtual desktops associated with the project will be automatically paused. This means that users will temporarily lose access to the SD Desktop service until additional billing units are allocated to the project.

* CSC Project closure: content stored within the SD Desktop and SD Connect services is subject to permanent deletion 90 days after the closure of a CSC project. **It is important to note that once data is deleted, it cannot be restored.**

To ensure that you are well-informed about these changes and your account status,  all project memebers will receive email notifications when billing units have been consumed and when a  CSC project is scheduled for closure. 

For additional information, please refer to the following links:

* [SD Desktop and SD Connect default storage and billing units consumption](../data/sensitive-data/sd-access.md#processing-sensitive-research-data)
    
* [SD Desktop: service usage restrictions](../data/sensitive-data/sd-access.md#/#service-usage-restrictions-when-billing-units-have-been-consumed)

* [Applying for billing units](../accounts/how-to-apply-for-billing-units.md#applying-for-billing-units)

* [Project lifetime extension](../accounts/how-to-manage-your-project.md/#project-lifetime-extension)


## SD Desktop: Unbuntu OS now available (September 2023)

You can now select the Ubuntu virtual desktop environment when creating a virtual desktop, alongside CentOS 7. 
  

## Technical issues on SD Connect: follow up 2.2.2023

Files uploaded using the SD Connect automated encryption option between November 2, 2022, and December 20, 2022, might be corrupted. 
During the upload phase files are split into short segments, and in some cases, due to a technical issue, the correct segment's order has been lost, making the files unreadable. Therefore, if you have used this function, we advise you to upload a new copy of the files. If this is not possible, don't hesitate to contact us at servicedesk@csc.fi. We will evaluate individual cases to determine if the files can be retrieved.

Currently, SD Connect automated encryption is supported only for files < 1GB. 
Larger files can be encrypted following this workflow:

* [Sensitive data encryption and upload for analysis, up to 100 GB](../../data/sensitive-data/sd_connect.md#sensitive-data-encryption-and-upload-for-analysis-up-to-100-gb)
* [Command Line Interface: data encryption and upload](../../data/sensitive-data/sd_connect.md#command-line-interface-data-encryption-and-upload)


## Sensitive Data services now have an audited computing environment for secondary use of social and health data 8.6.2022

SD Desktop is a certified environment for data processing under the Act on the Secondary Use of Health and Social Data. However, the services provided for this purpose have specific limitations compared to the standard service.

For more information see the user guide:

* [SD Desktop for secondary use](../../data/sensitive-data/sd-desktop-audited.md) and [Accessing SD service](../../data/sensitive-data/sd-access.md) explaining how to apply access to the audited SD Desktop service and describing the use and limitations of the audited environment.

