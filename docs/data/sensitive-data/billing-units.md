# Billing units

!!! default "Billing Units"

     **Every active CSC project consumes both Billing Units (BUs) and storage quota.** 
     
     **Billing Units (BUs)** are used to track how much computing power and processing time your project consumes. CSC uses different types of Billing Units to measure resource usage based on the service:
     
     - **SD Desktop** consumes **Cloud Billing Units** type, which reflect the use of virtual desktops and compute resources
     - **SD Connect** consumes **Storage Billing Units** type, which reflect the amount of data stored in CSC’s cloud infrastructure.
     - 30 000 Cloud and Storage BUs is usually enough for initial testing. You can apply for more billing units later in MyCSC.
     
     **The quota** limits the amount of storage space available. Default quota (or storage space) for each CSC project with for SD Connect enabled is 10 TB, which you can expand up to 200 TB as needed by contacting service desk (subject: Increase Allas quota).
     

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