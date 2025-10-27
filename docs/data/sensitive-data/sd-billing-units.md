# Resource planning for your CSC Project

Both the CSC project manager and project members are responsible for monitoring the resources consumed by their CSC project: Billing Units (BUs) and storage quota. When creating a project, you can apply for the default amount of resources, which will be granted immediately. However, it’s important to plan ahead for the next six months of usage and apply for additional resources twice a year. 

Please note that after each Billing Units application, there is a two week period during which you cannot submit another request, thus make sure to apply for resources in advance. You will be notified via email when your project’s Billing Units are running low, so you can apply for more in time and avoid service interruptions.


!!! default "Billing Units and quota"

     **Every active CSC project consumes both Billing Units (BUs) and storage quota.** 
     
     **Billing Units (BUs)** are used to track how much computing power and processing time your project consumes. CSC uses different types of Billing Units to measure resource usage based on the service:
     
     - **SD Desktop** consumes **Cloud Billing Units** type, which reflect the use of virtual desktops and compute resources
     - **SD Connect** consumes **Storage Billing Units** type, which reflect the amount of data stored in CSC’s cloud infrastructure.
     
     - 30 000 Cloud and Storage BUs is usually enough for initial testing. You can [apply for billing units](sd-use-case-new-user-project-manager.md#4-apply-for-more-billing-units) in MyCSC portal.
      
      **The storage quota** limits the amount of storage space available:
 
      - Default quota (or storage space) for each CSC project with for SD Connect enabled is 10 TB, which you can expand up to 200 TB as needed by contacting service desk (subject: Increase Allas quota).
      - Default volume quota for each virtual desktop is up to 200 GB. This is the storage space used to import files from SD Connect to SD Desktop for the analysis phase. You can expant the volume, before any data has       been imported to it, by writing to servicedesk@csc.fi (subject: SD Desktop). 


1. [SD Connect BU consumption](#1-create-csc-account)
2. [SD Desktop BU consmption](#2-create-new-csc-project)
3. [What happens if your project runs out of Billing Units?](#3-data-protection)
4. [Apply for more billing units ](#5-if-you-have-a-research-team-add-them-to-be-your-project-members)



#### SD Connect BU consumption

SD Connect stores data into CSC's infrastructure Allas and provides additional automated encryption and encryption key management. SD Connect consumes Billing Units at a rate of **1.3 Storage BUs per TB per hour**.

Here’s a table summarizing the Storage Billing Units required for storing data in **SD Connect** over **6 months** and **1 year** for various storage sizes:

| Storage Size |  Storage Billing Units (6 Months) |  Storage Billing Units (1 Year) |
|------------------|------------------------------|----------------------------|
| 500 GB (0.5 TB) | 2,847 units | 5,694  units |
| 1 TB | 5,694 units | 11,388 units |
| 10 TB | 56,940 units | 113,880 units |
| 100 TB | 569,400 units | 1,138,800 units |

#### SD Desktop BU consumption

Analysing data in SD Desktop consumes **Cloud Billing Units** based on the type of virtual desktop used. Each virtual desktop can also have a volume (also called disk space), where files can be imported from SD Connect/SD Apply. The volume can be added only during desktop creation (up to 200 GB). If you need larger volume please contact service desk _(subject: Sensitive data)_.

Here’s a table summarizing the Cloud Billing Units required for using **SD desktop** over **6 months** and **1 year** for various desktop options:

| Desktop Option | Cloud Billing Rate (units/hour) |  Cloud Billing Units (6 Months) | Cloud Billing Units (1 Year) |
|----------------|---------------------------|--------------------------|------------------------|
| Small Computation | 5.2 | 22,464 | 44,928 |
| Medium Computation | 10.4 | 44,928 | 89,856 |
| Heavy Computation | 65 | 280,800 |  561,600 |
| Small GPU Computation | 78 | 341,640 | 683,748 |
| Big Picture project | 195 | 854,100 | 1,708,770 |

#### What happens if your project runs out of Billing Units?

Once all the Cloud Billing Units for your CSC project have been used up, **access to the SD Desktop service will be restricted**. This means that:

- All virtual desktops currently running will automatically be paused.
- You will not be able to access the virtual desktops content's or unpause them, until you have applied for more resources.
- Your data remains unaffected and will not be deleted, even in cases where the total Billing Units reach zero or enter negative values.

!!! Note
    Each project member will receive a notification via email from the MyCSC portal when the Billing Units for your CSC project are about to end.

    
### Apply for more billing units 

You can apply for more BUs for your CSC project in MyCSC portal. Please note that after each application, there is a two week period during which you cannot submit another Biliing units (BUs) request, thus make sure to apply for resources in advance.

1. Sign in to MyCSC with you Haka or Virtu credentials.
2. Go to **Projects** page (left side menu or a hamburger menu at the top right corner).
3. Choose a project and click to open it.
4. In the new view, scroll down to **Resources** window and click **Apply for resources**. A new window will appear (this might take up to 8 seconds).
![Click apply for resources.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_AddResources1.png)
5. In the new window you will see the services you have active in the project (in gray). Press **Next**.
![Continue to billing units.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_MoreBUs_1025.png)
6. In the second view, click on the Billing Units package you need (e.g. M) for:
    - Cloud Billing Unit type (used by SD Desktop)
    - Storage Billing Units type (for SD Connect)
    - Click **Next**.
7.  In the next view, click **Add publications**. In the new window, you can search or add publications manually. If you don't have publications directly related to this work yet, any past publication from your research group will be fine. Click **Add**.
    - Next, you will be asked to add keywords. These will become tags that will help you search for the project. Add a keyword (e.g. research) and press **Add**.
    - Next, you need to fill in two more fields: Short overview of (expected) results and Program, software, methods used. 
    - Click **Next**.
9. In the last view, you can review the project description and field on science. Finally, you can click **Submit**.


### Log into SD Services

- Now all the preparations are ready and you can start using the services (links to related user guides):

SD Connect:

- [SD Connect overview and key features](./sd_connect.md)
- [SD Connect login instructions](./sd-connect-login.md)
  
SD Desktop:

- [SD Desktop overwvire and key features](./sd_desktop.md)
- [SD Desktop login instructions](sd-desktop-login.md)
    
