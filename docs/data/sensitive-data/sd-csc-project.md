
# Manage CSC project

To access CSC services, you need both a CSC account and membership in a CSC project. This allows you to apply for service access, manage team members, set data permissions and apply for additional resources. Although using SD Connect and SD Desktop is free of charge for research purposes according to CSC’s terms of use, CSC tracks the resources consumed by each CSC project through Billing Units. 


!!! Note
    The default lifetime of a CSC project is one year. All data stored in SD Connect or SD Desktop, including files, virtual desktops and volumes, will be permanently      deleted 90 days after the project closure/ expiration.

To effectively manage your CSC projects and its resources, please learn more information below: 

* [Project closure expiration and data deletion](#project-closure-expiration-and-data-deletion)
* [Billing units and storage usage](#billing-units-and-storage-usage)
* [What happens if your project runs out of billing units?](#what-happens-if-your-project-runs-out-of-billing-units)


## Project closure, expiration, and data deletion

The default lifetime of a CSC project is one year. As a project manager, you can either extend the project duration or close it through MyCSC.

*  You will receive an email notification from the MyCSC portal when your project is about to expire. Please keep your contact information up to date in MyCSC to ensure you receive this notification.
* After the project is closed, access to SD Connect and SD Desktop services will be disabled.
* All data stored in SD Connect or SD Desktop, including files, virtual desktops, and volumes, will be permanently deleted 90 days after the project closure/ expiration.

!!! Note
    Once data is deleted in line with CSC's data retention policy, it cannot be restored or recovered.



## Billing units and storage usage

The Billing Unit (BU) is CSC’s metric for tracking resource consumption for each CSC projects. As each service consumes billing units. When starting a project, consider your resource needs, including storage and billing units consumption. Each project starts with 10,000 billing units, typically enough for initial testing. 

You will get a notification via email from the My CSC portal when your billing units are about to end. \* Please apply more billing units for your project in [MyCSC](https://my.csc.fi/login){ target="\_blank" }.

Estimate your annual usage and apply for more units through the MyCSC portal if needed.

#### What happens if your project runs out of billing units?

Once all the billing units for your CSC project have been used up, **your access to the SD Desktop service will be restricted**. This means that:

* all virtual desktops currently running will automatically be paused
* you won't be able to access the virtual desktops content or unpause them, until you have applied for more resources. 
* your data remains unaffected and will not be deleted**, even in cases where the total billing units reach zero or enter negative values.

#### Applying for more billing units

You will get a notification via email from the My CSC portal when your billing units are about to end. You can apply more billing units for your CSC project and:

* login to [MyCSC](https://my.csc.fi/login){ target="\_blank" } 
* follow [these steps](./accounts/how-to-apply-for-billing-units.md)

Below, you can find more details about Billing Units consumption for SD Connect and SD Desktop, including a table summarizing the billing units required for storing data in SD Connect or using SD Desktop over 6 months and 1 year.

#### SD Connect BU consumption

SD Connect stores data to Allas. Default storage space for SD Connect/Allas is 10 TB, which you can expand up to 200 TB as needed. If you need even more storage capacity, please contact service desk _(subject: Increase Allas quota)_. Storing data in SD Connect/Allas consumes billing units at a rate of **1 billing unit per TB per hour**. This means that storing 1 TB of data in SD Connect/Allas consumes 24 billing units daily and 8760 billing units annually.

Here’s a table summarizing the billing units required for storing data in **SD Connect** over **6 months** and **1 year** for various storage sizes:

| **Storage Size** | **Billing Units (6 Months)** | **Billing Units (1 Year)** |
|------------------|------------------------------|----------------------------|
| 500 GB (0.5 TB) | 2,160 units | 4,320 units |
| 1 TB | 4,320 units | 8,640 units |
| 10 TB | 43,200 units | 86,400 units |
| 100 TB | 432,000 units | 864,000 units |

#### SD Desktop BU consumption

Analysing data in SD Desktop consumes billing units based on the type of virtual desktop used. Each virtual desktop can also have a volume (also called disk space), where files can be imported from SD Connect/SD Apply. The volume can be added only during desktop creation (up to 200 GB). If you need larger volume please contact service desk _(subject: Sensitive data)_.

Here’s a table summarizing the billing units required for using **SD desktop** over **6 months** and **1 year** for various desktop options:

| Desktop Option | Billing Rate (units/hour) | Billing Units (6 Months) | Billing Units (1 Year) |
|----------------|---------------------------|--------------------------|------------------------|
| Small Computation | 5.2 | 22,464 | 44,928 |
| Medium Computation | 10.4 | 44,928 | 89,856 |
| Heavy Computation | 52 | 224,640 | 449,280 |
| Small GPU Computation | 120 | 518,400 | 1,036,800 |
| Medium GPU Computation | 200 | 864,000 | 1,728,000 |
    

