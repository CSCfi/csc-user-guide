
# Manage CSC project

Contents:

* [Billing units and storage usage](#billing-units-and-storage-usage)
    * [SD Connect - billing units and storage space](#sd-connect---billing-units-and-storage-space)
    * [SD Desktop - billing units and disk space](#sd-desktop---billing-units-and-disk-space)
    * [What happens if your project runs out of billing units?](#what-happens-if-your-project-runs-out-of-billing-units)
    * [Billing unit calculator for estimating billing units consumption](#billing-unit-calculator-for-estimating-billing-units-consumption)
* [Closing your CSC project](#closing-csc-project)
    * [What happens to your data after the CSC project expires or is closed](#what-happens-to-your-data-after-the-csc-project-expires-or-is-closed)



## Billing units and storage usage

**Billing Unit (BU)** is CSC's own unit system, that measures, how much resources project consumes. Every project consumes billing units, but most cases **no actual payment** is required. Sensitive Data services are free of charge for research purposes. [Read more about free use cases from research.csc.fi](https://research.csc.fi/free-of-charge-use-cases){ target="_blank" }.

When you start a new project, you should plan ahead for your CSC project's resource usage. This includes considering the amount of storage space (i.e. quota) and billing units consumption while using the services. When you start a new project with CSC, you receive 10,000 billing units by default. This is enough for small testing. However, you should estimate how many BU’s your project will consume **during 1 year** and apply more if needed. You can apply more billing units trough MyCSC resource application. Read more: [applying for billing units](../../accounts/how-to-apply-for-billing-units.md) and [increasing quotas](../../accounts/how-to-increase-disk-quotas.md#increasing-the-storage-capacity-in-allas).

* [Billing unit calculator](#billing-unit-calculator-for-estimating-billing-units-consumption) will help you to estimate how many BUs your CSC project will require. You can find SD Desktop from the calculator, when you move to right with the arrows. You can estimate SD Connect billing unit consumption by using Allas -option at the calculator.

### SD Connect - billing units and storage space

SD Connect stores data to [Allas](../Allas/index.md). Default storage space for SD Connect/Allas is 10 TB, which you can expand up to 200 TB as needed. If you need even more storage capacity, please contact [service desk](../../support/contact.md) *(subject: Sensitive data)*. 

Storing data in SD Connect/Allas consumes billing units at a rate of **1 billing unit per TB per hour**. This means that storing 1 TB of data in SD Connect/Allas consumes 24 billing units daily and 8760 billing units annually.

### SD Desktop - billing units and disk space

By default, the disk space in SD Desktop is 80 GB, and you have the option to increase it up to 280 GB by adding an external volume during the creation of a virtual desktop. If you need more storage for data analysis, please contact [service desk](../../support/contact.md) *subject: Sensitive Data.*
Analyzing data in SD Desktop consumes billing units based on the type of virtual desktop used. The rates are as follows:

* Small computation: 5.2 billing units per hour
* Medium computation: 10.4 billing units per hour
* Heavy computation: 52 billing units per hour

## What happens if your project runs out of billing units?

Once all the billing units for your CSC project have been used up, **your access to the SD Desktop service will be restricted**. This means that all virtual desktops currently running will automatically be paused, and you won't be able to access their content. However, **your data remains unaffected and will not be deleted**, even in cases where the total billing units reach zero or enter negative values.

!!! Note 
    You will get a notification via email when your billing units have been consumed.
  



## Billing unit calculator for estimating billing units consumption

Billing unit calculator will help you to estimate how many BUs your CSC project will require. You can find SD Desktop from the calculator when you move to right with the arrows. You can estimate SD Connect billing unit consumption by using Allas option in the calculator.

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>



# Closing CSC project

Default lifetime for the project is **one year**. [Project manager](#step-by-step-tutorial-for-project-manager) can extend project's lifetime or close the project in [MyCSC](https://my.csc.fi){ target="_blank" }. If project lifetime ends, it will be closed automatically. You'll receive an email notification when your project is about to expire, so please keep your contact information up to date in MyCSC.

[More about project closure](../../accounts/how-to-manage-your-project.md#project-closure)

## What happens to your data after the CSC project expires or is closed

* **Services will be disabled**: SD Connect and SD Desktop services will be disabled, and you won't be able to access them anymore.

* **Data will be deleted after 90 days**: Any data stored within SD Connect or SD Desktop, including files, virtual desktops, and volumes, will be permanently removed after 90 days from the project's closure. This measure is in place to ensure the secure handling of your data, aligning with CSC's policies.

!!! Note
    All **content within the services will be permanently deleted 90 days** after the project is closed. Once deleted, it cannot be restored or recovered.
