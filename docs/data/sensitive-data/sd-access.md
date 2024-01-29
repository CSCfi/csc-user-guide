# Start here: accessing Sensitive Data services 
  
In this section, discover how to access Sensitive Data (SD) services for the firs time. Learn to manage your project's billing unit consumption, storage space, project members and what happens to your data upon project closure.

Contents:

 * [Access SD Connect and SD Desktop for the first time](#access-sd-connect-and-sd-desktop-for-the-first-time)
 * [Project manager and memebers](#project-manager-and-members)
 * [Project resources and storage space](#project-resources-and-storage-space)
 * [Closing the project](#closing-the-project)
 * [Billing units calculator](#billing-unit-calculator)

## Access SD Connect and SD Desktop for the first time

1. **Create a [CSC account](../../accounts/how-to-create-new-user-account.md)** by logging in at the [MyCSC portal](https://my.csc.fi){ target="_blank" }.

2. **Create new CSC project** or join to existing CSC project.

3. **Fill the form** *Personal data handling / GDPR document*. 

4. **[Add service access](../../accounts/how-to-add-service-access-for-project.md)**
to SD Connect and SD Desktop. Please note that every project member must approve the terms of use personally.

4. **[Apply for resources](../../accounts/how-to-apply-for-billing-units.md)** (i.e. billing units, BU's). Please check your email after applying for resources. The result will be there.

6. **Add project members**.

7. **[Activate Multi-factor Authentication (MFA)](../../accounts/mfa.md)**. This is mandatory for Sensitive Data services. All project members must activate MFA personally.

=== "1. CSC account"
    [![How to start with SD services.](./images/introduction/HowToGetStarted_SD.svg

=== "2. Project"
    Screenshot tähän

=== "3. Forms"
    Screenshot tähän

=== "4. Services"
    Screenshot tähän

=== "5. Resources"
    Screenshot tähän

=== "6. Members"
    Screenshot tähän

=== "7. MFA"
    Screenshot tähän


## Project manager and members

### Project manager

* The person who created the project in MyCSC, is the project manager. You can change project manager by contacting [service desk](../../support/contact.md).

* Project manager can manage project members, project's lifetime, storage space and resources (i.e. billing units).

* Only the project manager can export data from SD Desktop.

!!! note ""
    **Keep project manager's CSC account active.** Otherwise the project will be [closed](#closing-the-project). You can keep CSC account active by changing password once a year and keeping user information such as email address up to date.

    You can manage your user information and project members in [MyCSC](https://my.csc.fi){ target="_blank" }.

### Project members

All project members have equal access permissions to the project files.

* **SD Connect:** project members can upload, download and delete project files.
* **SD Desktop:** project members can upload data and analyze it, but they can not export anything from SD Desktop. Only the project manager can export data from SD Desktop.

## Project resources and storage space

The use of CSC services is measured with **billing units (BUs)**. Every project consumes billing units, even if they are free of charge. Sensitive Data services are free of charge for research purposes. [Read more about free use cases from research.csc.fi](https://research.csc.fi/free-of-charge-use-cases){ target="_blank" }.

When you start a new project, you should plan ahead for your CSC project's resource usage. This includes considering the amount of storage space (i.e. quota) and billing units consumption while using the services. When you start a new project with CSC, you receive 10,000 billing units by default. This is enough for small testing. You can apply more billing units trough MyCSC resource application. Read more: [applying for billing units](../../accounts/how-to-apply-for-billing-units.md) and [increasing quotas](../../accounts/how-to-increase-disk-quotas.md).

* **[Billing unit calculator](#billing-unit-calculator)** will help you to estimate how many BUs your CSC project will require. You can find SD Desktop from the calculator, when you move to right with the arrows.

### SD Connect billing units and storage space

SD Connect stores data to [Allas](../Allas/index.md). Default storage space for SD Connect/Allas is 10 TB, which you can expand up to 200 TB as needed. If you need even more storage capacity, please contact [service desk](../../support/contact.md) (subject: Sensitive data). 

Storing data in SD Connect/Allas consumes billing units at a rate of **1 billing unit per TB per hour**. This means that storing 1 TB of data in SD Connect/Allas consumes 24 billing units daily and 8760 billing units annually.

### SD Desktop billing units and storage space

By default, the disk space in SD Desktop is 80 GB, and you have the option to increase it to 280 GB by adding an external volume during the creation of a virtual desktop. If you need more storage for data analysis, please contact [service desk](../../support/contact.md) (subject: Sensitive Data).
Analyzing data in SD Desktop consumes billing units based on the type of virtual desktop used. The rates are as follows:

* Small computation: 5.2 billing units per hour
* Medium computation: 10.4 billing units per hour
* Heavy computation: 52 billing units per hour


### What happens if your project runs out of billing units?

Once all the billing units for your CSC project have been used up, **your access to the SD Desktop service will be restricted**. This means that all virtual desktops currently running will automatically be paused, and you won't be able to access their content. However, **your data remains unaffected and will not be deleted**, even in cases where the total billing units reach zero or enter negative values.

* You get a notification via email when your billing units have been consumed.
  
#### How to regain access to your virtual desktop

 Apply billing units and unpause your virtual desktop:

1. [Apply for more billing units](../../accounts/how-to-apply-for-billing-units.md) for your project. This will give you a positive balance to continue using the service.

1. Log in to [SD Desktop](https://sd-desktop.csc.fi){ target="_blank" }.

1. On the SD Desktop homepage, click on ***Go To SD Desktop Management***.

1. Under ***Available desktops*** select the correct virtual desktop, and in the same row, on the right side, click on ***Resume***.

!!! Note
    Restarting a paused desktop is possible only for [active CSC projects](../../accounts/how-to-manage-your-project.md) with available billing units.




## Closing the project

Defautl lifetime for the project is **one year**. [Project manager](#project-manager) can extend project's lifetime or close the project in [MyCSC](https://my.csc.fi){ target="_blank" }. If project lifetime ends, it will be closed automatically. You'll receive an email notification when your project is about to expire, so please keep your contact information up to date in MyCSC.

[More about project closure](../../accounts/how-to-manage-your-project.md#project-closure)

### What happens to your data after the CSC project expires or is closed

* **Services will be disabled**: SD Connect and SD Desktop services will be disabled, and you won't be able to access them anymore.

* **Data will be deleted after 90 days**: Any data stored within SD Connect or SD Desktop, including files, virtual desktops, and volumes, will be permanently removed after 90 days from the project's closure. This measure is in place to ensure the secure handling of your data, aligning with CSC's policies.

!!! Note ""
    Please note that all **content within the services will be permanently deleted 90 days** after the project is closed. Once deleted, it cannot be restored or recovered.


## Billing unit calculator

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>


