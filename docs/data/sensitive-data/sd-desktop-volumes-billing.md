# Changes to Billing of SD Desktop External Volumes

## Introduction

Starting June 3, 2026, **SD Desktop external volumes will consume Cloud Billing Units from your CSC project**. Previously allocated manually to your organization, these units will now be visible directly in your project. 

To avoid service disruption, please ensure you have sufficient billing units for the next 5–6 months by following the step-by-step guidance below. If needed, apply for additional Billing Units via the MyCSC portal as soon as possible. Processing times may vary, so please allow sufficient time.


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **When your project runs out of Billing Units**
  { .csc-grid-card-error }

    ___

    Please note that your CSC project must have sufficient Billing Units to remain active. If the Billing Unit balance of your CSC project becomes negative your virtual desktop will be paused, the CSC project will be closed after 60 days and all project data will be permanently deleted 90 days after project closure.

</div>




### Step 1: check if your virtual desktop have an external volume


1. [Login](./sd-desktop-login.md) to SD Desktop. All your virtual desktops are listed at the home page under **All connections**.

2. Select project (e.g. `project_NNNNN`) and click **plus icon**.
  
3. Now you can see all virtual desktops that belong to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name. If you encounter a black screen, your virtual desktop is probably paused and needs to be [resumed](sd-desktop-manage.md#resuming-a-paused-virtual-desktop). 
   
4. On the left navigation bar click on the volume icon and check the volume size.
   
5. Repeat these steps for all the virtual desktops in your CSC projects. 

![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

![Volume size](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop-VolumeSize.png)


### Step 2: Calculate how many billing units the virtual desktop volume consumes and which Billing unites package you should apply for

Volumes consume 4.7 Cloud Billing Units/Tib/ Hour. Below is a table summarizing the Cloud Billing Units required for using **volumes** over **one year** for various options and correspondent Billing Units package you can apply for via MyCSC.

| Volume Option | Cloud Billing Rate (units/TiB/hour) |  Cloud Billing Units (consumed in 1 year) | Select the correct BU Package in MyCSC and application frequency |
|----------------|---------------------------|--------------------------|------------------------|
| up to 1 TB | 4.7 | 1 600 |Small package, 1 times a year: 30 000 BUs assigned immediately  |
| 10 TB | 4.7 | 17 000 |  Medium package, 1 times a year: 30 000 BUs Processed on average within 1-3 days by a Resource Officer |


### Step 3: Verify in MyCSC if your CSC project has enough Billing Units and apply for more if needed

1. Log in to [MyCSC](https://my.csc.fi).
2. Navigate to your project's view. 
3. Scroll down to **Resources** window.
4. You can see **Cloud Billing Units** usage under its tab.
5. If your project doesn't have enough Cloud Billing Units, [**apply for additional units**](sd-billing-units.md#step-2-apply-for-billing-units-via-mycsc-portal).
6. If you had received email notifications about Billing Units are running low, you need to extend the project’s lifetime via MyCSC. This can be done only be the project manager.

![Billing Units in MyCSC](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_BUs.png)


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    ___

    * Any project member can apply for additional Billing Units.
    * Small packages are assigned immediately, while Medium packages may take up to 3 days to be processed.
    * After submitting an application, there is a two‑week period during which you cannot submit another request. For this reason, it is important to apply early.
    * During the application process, you will be asked to attach scientific publications. If you do not yet have publications directly related to this work, you may include any relevant past publications from your research group, even if they are not directly linked to the project.

In addition, Billing Units consumed by external volumes between January 1, 2026 and May 26, 2026 will be charged retroactively. These charges will be applied automatically to your CSC project and will consume your project’s Billing Unit balance.
