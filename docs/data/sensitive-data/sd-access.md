# Accessing Sensitive Data (SD) services 
  
In this section, discover how to access SD services for processing sensitive research data. Learn to manage billing unit consumption and what happens to your data upon project closure.

Contents:

 * [How to start with SD services](#how-to-start-with-sd-services);
 * [Project manager and project memebers](#project-manager-and-project-members);
 * [Resources and storage space](#resources-and-storage-space);
 ---- kesken ---
 * [What happens to your data when your CSC project expires or is closed](./sd-access.md#what-happens-to-your-data-when-your-csc-project-expires-or-is-closed);
 * [Billing units calculator](./sd-access.md#default-storage-space-and-billing-units-consumption).

## How to start with SD Services
### Access SD Connect and SD Desktop for the first time


1. Create a [CSC account](../../accounts/how-to-create-new-user-account.md) by logging in at the [MyCSC portal](https://my.csc.fi).

2. Create new CSC project or join to existing CSC project.

3. Fill the forms: *Description of processing activities form (???)* and *Personal data handling / GDPR document*. 

4. Add service access to **SD Connect** and **SD Desktop**. Please note that every project member must approve the terms of use personally.

5. Apply for resources (i.e. billing units, BU's). Please check your email after applying for resources. The result will be there.

6. Add project members.

7. Activate Multi-factor Authentication (MFA). This is mandatory for Sensitive Data services. All project members must activate MFA personally.

For video tutorials and further guidance, check the [Accounts](../../accounts/index.md) section at the beginning of this manual.


## Project manager and project members

### Project manager

* The person who created the project in MyCSC, is the project manager. You can change project manager by contacting service desk.

* Project manager can manage project members, storage space and resources (i.e. billing units).

* Only the project manager can export data from SD Desktop.

Keep project manager's CSC account active. Otherwise the project will be closed. You can keep CSC account active by changing password once a year and keeping user information such as email address up to date.

You can manage your user information and project members in MyCSC.

### Project member

All project members have equal access permissions to the project files.

* **SD Connect:** project members can upload, download and delete project files.
* **SD Desktop:** project members can upload data and analyze it, but they can not export anything from SD Desktop. Only the project manager can export data from SD Desktop.

## Resources and storage space

Sensitive Data services are free of charge for research purposes. [Read more about free use cases from research.csc.fi](https://research.csc.fi/free-of-charge-use-cases)
The use of CSC's services is measured with billing units (BUs). Every projects consumes billing units, even if they are free of charge. 

When you start a new project, you should plan ahead for your CSC project's resource usage. This includes considering the amount of storage space (i.e. quota) and billing units consumption while using the services. When you start a new project with CSC, you receive 10,000 billing units by default. This is enough for small testing. You can apply more billing units trough MyCSC resource application. Read more: [applying for billing units](../../accounts/how-to-apply-for-billing-units.md) and [increasing quotas](../../accounts/how-to-increase-disk-quotas.md).

* Billing unit calculator will help you to estimate how many BUs your CSC project will require. You can find SD Desktop from the calculator (move to right with the arrows)
  
--- Loppu tarkistamatta  t. Suvi 29.1. ---

### SD Connect billing and quota

When you apply for a new CSC project, the default quota (storage space) for SD Connect/Allas is 10 TB, which can be expanded up to 200 TB as needed. If you require additional storage capacity, please reach out for support at [CSC Service Desk](../../support/contact.md) (subject: Sensitive data).

Storing data in SD Connect/Allas consumes billing units at a rate of 1 billing unit per TB per hour. This means that storing 1 TB of data in Allas consumes 24 billing units daily and 8760 billing units annually.

### SD Desktop billing and quota

By default, the disk space in SD Desktop is 80 GB, and you have the option to increase it to 280 GB by adding an external volume during the creation of a virtual desktop. If you need more storage for data analysis, reach out for support at [CSC Service Desk](../../support/contact.md) (subject: Sensitive data).

Analyzing data in SD Desktop consumes billing units based on the type of virtual desktop used. The rates are as follows:

* Small computation: 5.2 billing units per hour;
* Medium computation: 10.4 billing units per hour;
* Heavy computation: 52 billing units per hour.



## Service usage restrictions when billing units have been consumed

Once all the billing units for your CSC project have been used up, your access to the SD Desktop service will be restricted. This means that all virtual desktops currently running will automatically be paused, and you won't be able to access their content. It's important to note that your data remains unaffected and will not be deleted, even in cases where the total billing units reach zero or enter negative values.

* **Notification**: You'll be notified via email when your billing units have been consumed.
  
* **Regaining access to your virtual desktop**: To regain access to your virtual desktop, just follow these easy steps:

1. Apply for more billing units by visiting the [MyCSC portal](https://my.csc.fi). This will give you a positive balance to continue using the service.

2. Log in to SD Desktop and unpause your virtual desktop. On the SD Desktop homepage, click on _Go To SD Desktop Management_; Here, under _Available desktops_  select the correct virtual desktop, and in the same raw, on the right side, click on _Resume_.

!!! Note
    Restarting a paused desktop is only possible for active CSC projects with available billing units. 




## What happens to your data when your CSC project expires or is closed

When your CSC project reaches its expiration date or is closed, there are a few important things to know about your data:

* **Service Discontinuation**: both SD Connect and SD Desktop services will be disabled, and you won't be able to access them anymore.

* **Data Deletion**: Any data stored within these services, including files, virtual desktops, and volumes, will be permanently removed after 90 days from the project's closure. This measure is in place to ensure the secure handling of your data, aligning with CSC's policies.

* **Notification**: We'll keep you informed about the status of your project. You'll receive an email notification when your project is about to expire, so you can plan accordingly. For example, you can apply for a project lifetime extension of one year loggin in to [MyCSC portal](https://my.csc.fi).

!!! Note
    Please note that all content within the services will be permanently deleted 90 days after the project is closed, and once deleted, it cannot be restored or recovered.


### Billing unit calculator

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>


