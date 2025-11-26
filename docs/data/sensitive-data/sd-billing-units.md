# Resource planning for your CSC Project

**Both the CSC project manager and project members are responsible for monitoring the resources consumed by their CSC project: Billing Units (BUs) and storage quota**. When creating a project, you can apply for the default amount of resources, which will be granted immediately. However, **it’s important to plan ahead for the next six months of usage and apply for additional resources twice a year**. 

!!! Note 
    Please note that after each Billing Units application, **there is a two week period during which you cannot submit another request**, thus make sure to apply for resources in advance. You will be notified via email when your project’s Billing Units are running low, so you can apply for more in time and avoid service interruptions.



In the following section, you will learn:

- [What are Cloud and Storage Billing Units and quota](#what-are-cloud-and-storage-billing-units-and-quota)

- [What happens if your project runs out of Billing Units](#what-happens-if-your-project-runs-out-of-billing-units)

- [Step 1: Determine the appropriate Billing Units Package (Basic, Small, Medium or Large)](#step-1-plan-for-the-appropriate-billing-units-package-basic-small-medium-or-large)

- [Step 2: Appply for more billing units in the MyCSC portal]



## What are Cloud and Storage Billing Units and quota

1. **Every active CSC project consumes both Billing Units (BUs) and storage quota.** 
     
- **Billing Units (BUs)** are used to track how much computing power and processing time your project consumes. CSC uses different types of Billing Units to measure resource usage based on the service:
     
- **SD Desktop** consumes **Cloud Billing Units** type, which reflect the use of virtual desktops and compute resources

- **SD Connect** consumes **Storage Billing Units** type, which reflect the amount of data stored in CSC’s cloud infrastructure.
     
- 30 000 Cloud and Storage BUs is usually enough for initial testing. Next, you should estimate your project’s resource and storage needs for the next six months and apply for the required amount using the MyCSC portal. The instructions below will guide you through the process.
      
2. **The storage quota** limits the amount of storage space available:
 
- Default quota (or storage space) for each CSC project with for **SD Connect enabled is 10 TB**, which you can expand up to 200 TB as needed by contacting service desk (subject: Increase Allas quota).

- Default **volume quota for each virtual desktop is up to 200 GB**. This is the storage space used to import files from SD Connect to SD Desktop for the analysis phase. You can expand the volume, before any data has been imported to it, by writing to servicedesk@csc.fi (subject: SD Desktop). 



## What happens if your project runs out of Billing Units?

1. Once all the Cloud Billing Units for your CSC project have been used up, **access to the SD Desktop service will be restricted**. This means that:

- All virtual desktops currently running will automatically be paused.
- You will not be able to access the virtual desktops content's or unpause them, until you have applied for more resources.
- Your data remains unaffected and will not be deleted, even in cases where the total Billing Units reach zero or enter negative values.

!!! Note
    Each project member will receive a notification via email from the MyCSC portal when the Billing Units for your CSC project are about to end.

    
2. Once all quota (or storage space) has been used:

- Data upload to SD Connect will no longer be possible
  
- Data import to SD Desktop will no loner be possible
  

 ## Step 1: plan for the appropriate Billing Units Package (Basic, Small, Medium or Large)

Estimate the Billing Units your project will consume over the next six months for SD Desktop (Cloud BUs Type) and SD Connect (Storag Bus typee) using the examples provided below. This will help you determine which package to apply for in the MY.csc.fi portal. Before you begin, please note:

- Unused Billing Units expire every six months, so request only what you need.

- The Basic, Small and Medium packages have fixed Billing Unit (BU) allocations, while the Large package is flexible and can be defined by you, up to a maximum of 3,000,000 BUs.

- If your virtual desktop has been paused because all billing Units have been already consumed, apply for the Small Package (30,000 BUs). It will be assigned immediately so you can resume work. After two weeks, review if more units are needed.

- after each Billing Units application, **there is a two week period during which you cannot submit another request**. If you are unsure what billing units package you need to apply for, pelase contact us at servicedesk@csc.fi



#### SD Desktop: cloud type billing units

Analysing data in SD Desktop consumes **Cloud Billing Units** based on the type of virtual desktop used. Each virtual desktop can also have a volume (also called disk space), where files can be imported from SD Connect/SD Apply. The volume can be added only during desktop creation (up to 200 GB). If you need larger volume please contact service desk _(subject: Sensitive data)_.

Here’s a table summarizing the Cloud Billing Units required for using **SD desktop** over **6 months** and **1 year** for various desktop options:

| Desktop Option | Cloud Billing Rate (units/hour) |  Cloud Billing Units ( consumed in 6 months) | Select the correct BU Package in My.csc.fi and application frequency |
|----------------|---------------------------|--------------------------|------------------------|
| Small Computation | 5.2 | 22,464 |Small package, 2 times a year: 30.000 BUs assigned immediately| 
| Medium Computation | 10.4 | 44,928 |Small package, 3 times a year: 30.000 BUs assigned immediately  |
| Heavy Computation | 65 | 280,800 |  Medium package, 2 times a year: 300.000 BUs Processed on average within 1-3 days by a Resource Officer |
| Small GPU Computation | 78 | 341,640 | Medium package, 3 times a year: 300.000 BUs Processed on average within 1-3 days by a Resource Officer |
| Big Picture project | 195 | 854,100 | Large package, 2 times a year: 900.00 Bus Generally processed every three weeks by the CSC's Resource Allocation Group |




#### SD Connect: storage type billing units

SD Connect stores data into CSC's infrastructure Allas and provides additional automated encryption and encryption key management. SD Connect consumes Billing Units at a rate of **1.3 Storage BUs per TB per hour**.

Here’s a table summarizing the Storage Billing Units required for storing data in **SD Connect** over **6 months** and **1 year** for various storage sizes:

| Storage Size |  Storage Billing Units (consumed in 6 months) |  Select the correct BU Package in My.csc.fi and application frequency |
|------------------|------------------------------|----------------------------|
| 500 GB (0.5 TB) | 2,847 units | Basic package, 3 times a year: 2.500 BUs assigned immediately |
| 1 TB | 5,694 units | Small package, 2 times a year: 30.000 BUs assigned immediately |
| 10 TB | 56,940 units | Small package, 3 times a year: 30.000 BUs assigned immediately  |
| 100 TB | 569,400 units | Medium package, 3 times a year: 300.000 BUs Processed on average within 1-3 days by a Resource Officer |





## Appply for more billing units in the MyCSC portal


You can apply for more BUs for your CSC project in MyCSC portal. Please note that after each application, there is a two week period during which you cannot submit another Billing units (BUs) request, thus make sure to apply for resources in advance.

1. Sign in to MyCSC with your Haka or Virtu credentials.
2. Go to **Projects** page (left side menu or a hamburger menu at the top right corner).
3. Choose a project and click to open it.
4. In the new view, scroll down to **Resources** window and click **Apply for resources**. A new window will appear (this might take up to 8 seconds).
![Click apply for resources.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_AddResources1.png)
5. In the new window you will see the services you have active in the project (in gray). Press **Next**.
![Continue to billing units.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_MoreBUs_1025.png)

6. In the second view, click on the Billing Units package you need for
   
    - Cloud Billing Unit type (used by SD Desktop)
   
    - Storage Billing Units type (for SD Connect)
 
Click **Next**.

7.  In the next view, click **Add publications**. In the new window, you can search or add publications manually. **Note: Undestandably, if you don't have publications related to this work yet, you can add here any past publication from your research group, even if the project is not directly related**
 
 Click **Add**.
 
8. Next, you will be asked to add keywords. These will become tags that will help you search for the project. Add a keyword (e.g. research) and press **Add**.

9. Next, you need to fill in two more fields: Short overview of (expected) results and Program, software, methods used. 

Click **Next**.

10. In the last view, you can review the project description and field of science. Finally, you can click **Submit**.

When teh Biling Units will be assigned to the CSC Project you will receive an email notification. 


### Log into SD Services

- Now all the preparations are ready and you can start using the services (links to related user guides):

SD Connect:

- [SD Connect overview and key features](./sd_connect.md)
- [SD Connect login instructions](./sd-connect-login.md)
  
SD Desktop:

- [SD Desktop overview and key features](./sd_desktop.md)
- [SD Desktop login instructions](sd-desktop-login.md)
    
