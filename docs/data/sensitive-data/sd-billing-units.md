# Resource planning for your CSC Project


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **When your project runs out of billing units**
  { .csc-grid-card-error }

    ___

    When an academic CSC project runs out of Billing Units, project members have **60 days** to apply for more. **If Billing Units balance remain negative after those 60 days, the project will be closed and all data is deleted.**[**Read more**](#when-your-project-runs-out-of-billing-units)
    
</div>


Every active CSC project consumes both Billing Units (BUs) and storage quota. When you create a project, CSC grants a default amount of Billing Units (BUs) and storage quota immediately. 

**Both the CSC project manager and all project members share responsibility for:**

- Monitoring how many [**Billing Units**](#what-are-billing-units) the project has left.
- Monitoring how much of the [**storage quota**](#what-is-storage-quota) is being used.
- [**Planning 6 months ahead**](#step-1-estimate-the-appropriate-billing-units-packages-for-your-project) project's resource usage.
- [**Applying for more Billing Units**](#step-2-apply-for-billing-units-via-mycsc-portal) around 2-4 times a year.


## What are Billing Units 
   
**Billing Units (BUs)** are used to track how much computing power and processing time your project consumes. CSC uses different types of Billing Units to measure resource usage based on the service:

- **SD Desktop** consumes **Cloud Billing Units** type, which reflect the number of virtual desktops running and the number of volumes you've created. Each virtual desktop in SD Desktop can have a volume, where files can be imported from SD Connect/SD Apply. The volume appears inside the virtual desktop similarly to how a USB drive appears on a personal computer. The volume can be added only during desktop creation (up to 200 GB). If you need larger volume please contact service desk _(subject: Sensitive data)_.

- **SD Connect** consumes **Storage Billing Units** type, which reflect the amount of data stored in CSC’s cloud infrastructure. The more data you store and the longer you store it, the more Storage BUs are used.

- When you create a project, **30 000 Cloud and Storage BUs** are usually enough for initial testing. 

### How to monitor Billing Units usage

You can monitor Billing Units usage in MyCSC portal. 

1. Log in to [MyCSC](https://my.csc.fi).
2. Navigate to your project's view. 
3. Scroll down to **Resources** window.
4. You can see **Cloud Billing Units** and **Storage Billing Units** usage under from their respective tabs.

![Billing Units in MyCSC](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_BUs.png)


### When your project runs out of Billing Units

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle }
  { .csc-grid-card-error }

     When an academic CSC project runs out of Billing Units, project members have **60 days** to apply for more. **If Billing Units remain balance negative after those 60 days, [the project will be closed and all data is deleted.](sd-use-case-new-user-project-manager.md//#5-project-lifetime-billing-units-and-data-retention)**. You’ll receive email notifications in advance when Billing Units are running low. 

    To prevent this, the project manager should:

    1. Apply for more [**Billing Units**](sd-billing-units.md#step-2-apply-for-billing-units-via-mycsc-portal) via MyCSC. This can be also done by a project member.
    2. [**Extend**](../../accounts/how-to-manage-your-project.md#project-lifetime-extension) the project’s lifetime via MyCSC. This can be done only be the project manager.

</div>

Until you apply for more BUs you will have a **limited access to the SD Desktop**:

- All virtual desktops currently running will automatically be paused in SD Desktop.
- You will not be able to access the virtual desktops content's or unpause them.

   

## What is Storage Quota 

The storage quota defines how much space is available for your project’s data. It represents a capacity limit, not a consumable resource. 

For CSC projects with SD Connect enabled, the default quota is 10 TB. If needed, this can be increased up to 200 TB by contacting the Service Desk (subject line: Increase Allas quota).

### How to monitor Storage Quota usage

You can monitor Storage Quota in MyCSC portal. 

1. Log in to [MyCSC](https://my.csc.fi).
2. Navigate to your project's view. 
3. Scroll down to **Services** window.
4. Click **Allas**. You can see Storage Quota usage under **Usage** at the bottom of the window.

![Storage Quota in MyCSC](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_Quota.png)

### When your project runs out of quota

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **What happens to your project and services:**
  { .csc-grid-card-warning }

    ---

    - Data upload to SD Connect will no longer be possible.
    - Data import to SD Desktop will no longer be possible.
    
</div>


### How to increase quota

If you have less quota available than is needed, apply for more:

  - Send email to Service Desk (subject line: Increase Allas quota). It takes few days to process your application.
  - You will receive email when your quota is available.


## Plan resource usage
  
### Step 1: Estimate the appropriate Billing Units packages for your project

Estimate the Billing Units your project will consume over the next six months for SD Desktop (Cloud Billing Units) and SD Connect (Storage Billing Units) using the examples provided below. This will help you determine which package to apply for via MyCSC portal. Before you begin, please note:

<div class="grid cards" markdown>

- :material-information:{ .lg .middle } **Billing Unit Packages**
  { .csc-grid-card-info }

    ---
    - Unused Billing Units expire every six months, so request only what you need.
    - The Basic, Small and Medium packages have fixed Billing Unit (BU) allocations, while the Large package is flexible and can be defined by you, up to a maximum of 3,000,000 BUs.
    - If your virtual desktop has been paused because all Billing Units have been already consumed, apply for the Small Package (30,000 BUs) from my.csc.fi. It will be assigned immediately, allowing you to resume work. After two weeks, review your usage to see if additional units are needed.
    
</div>


#### SD Desktop: Cloud Billing Units

**SD Desktop** consumes **Cloud Billing Units** type, which reflect the number of virtual desktops running and the number of volumes you've created. Each virtual desktop can also have a volume (also called disk space), where files can be imported from SD Connect/SD Apply. 

Here’s a table summarizing the Cloud Billing Units required for using **virtual desktops** over **one year** for various options:

| Desktop Option | Cloud Billing Rate (units/hour) |  Cloud Billing Units (consumed in 1 year) | Select the correct BU Package in MyCSC and application frequency |
|----------------|---------------------------|--------------------------|------------------------|
| Small Computation | 5.2 | 48 000 |Small package, 2 times a year: 30 000 BUs assigned immediately| 
| Medium Computation | 10.92 | 98 000 |Small package, 4 times a year: 30 000 BUs assigned immediately  |
| Heavy Computation | 65 | 565 000 |  Medium package, 2 times a year: 300 000 BUs Processed on average within 1-3 days by a Resource Officer |
| Small GPU Computation | 78 | 685 000 | Medium package, 3 times a year: 300 000 BUs, Processed on average within 1-3 days by a Resource Officer |
| Big Picture project | 195 | 1 700 000 | Large package, 2 times a year: 900 000 BUs, Generally processed every three weeks by the CSC's Resource Allocation Group |


Here’s a table summarizing the Cloud Billing Units required for using **volumes** over **one year** for various options:

| Volume Option | Cloud Billing Rate (units/hour) |  Cloud Billing Units (consumed in 1 year) | Select the correct BU Package in MyCSC and application frequency |
|----------------|---------------------------|--------------------------|------------------------|
| 200 GB | 4.7 | 4 000 |Small package, 2 times a year: 30 000 BUs assigned immediately| 
| 1 TB | 4.7 | 20 000 |Small package, 2 times a year: 30 000 BUs assigned immediately  |
| 10 TB | 4.7 | 200 000 |  Medium package, 2 times a year: 300 000 BUs Processed on average within 1-3 days by a Resource Officer |


#### SD Connect: Storage Billing Units

SD Connect stores data into CSC's infrastructure Allas and provides additional automated encryption and encryption key management. SD Connect consumes Billing Units at a rate of **1.4 Storage BUs per TB per hour**.

Here’s a table summarizing the Storage Billing Units required for storing data in **SD Connect** over **6 months** for various storage sizes:

| Storage Size |  Storage Billing Units (consumed in 6 months) |  Select the correct BU Package in MyCSC and application frequency |
|------------------|------------------------------|----------------------------|
| 500 GB (0.5 TB) | 3 000  units | Basic package, 3 times a year: 2 500 BUs assigned immediately |
| 1 TB | 6 000 units | Small package, 2 times a year: 30 000 BUs assigned immediately |
| 10 TB | 60 000 units | Small package, 3 times a year: 30 000 BUs assigned immediately  |
| 100 TB | 600 000 units | Medium package, 3 times a year: 300 000 BUs Processed on average within 1-3 days by a Resource Officer |


### Step 2: Apply for billing units via MyCSC portal

You can apply for more BUs for your CSC project via MyCSC portal. 

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Restrictions about applying for Billing Units**
  { .csc-grid-card-warning }

    ---

    After you apply for additional Billing Units, there is a two‑week period during which you cannot submit another application. Because of this, it’s important to request additional resources early. You will receive an email notification when your project’s Billing Units are running low, giving you enough time to apply for more before service avaibility is affected.
    
</div>


1. Sign in to MyCSC with your Haka or Virtu credentials.
2. Go to **Projects** page (left side menu or a hamburger menu at the top right corner).
3. Choose a project and click to open it.
4. In the new view, scroll down to **Resources** window and click **Apply for resources**. A new window will appear (this might take up to 8 seconds).
![Apply Billing Units in MyCSC](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_Apply_BUs.png)
5. In the new window you will see the services you have active in the project (in gray). Press **Next**.
![Continue to billing units.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_MoreBUs_1025.png)

6. In the second view, click on the Billing Units package you need for
   
    - Cloud Billing Unit type (used by SD Desktop)
    - Storage Billing Units type (for SD Connect)
    - Click **Next**.

7.  In the next view, click **Add publications**. In the new window, you can search or add publications manually. **Note: Undestandably, if you don't have publications related to this work yet, you can add here any past publication from your research group, even if the project is not directly related.** Click **Add**.
 
8. Next, you will be asked to add keywords. These will become tags that will help you search for the project. Add a keyword (e.g. research) and press **Add**.

9. Next, you need to fill in two more fields: Short overview of (expected) results and Program, software, methods used. Click **Next**.

10. In the last view, you can review the project description and field of science. Finally, you can click **Submit**.

11. When the Biling Units will be assigned to the CSC Project you will receive an email notification. 






### Log into services

- Now all the preparations are ready and you can start using the services. Below you'll find links to related user guides:

**SD Connect:**

- [SD Connect overview and key features](./sd_connect.md)
- [SD Connect login instructions](./sd-connect-login.md)
  
**SD Desktop:**

- [SD Desktop overview and key features](./sd_desktop.md)
- [SD Desktop login instructions](sd-desktop-login.md)
    
