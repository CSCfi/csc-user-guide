# Retroactive billing: how to request Billing Units for SD Desktop external volumes 

## Intorduction

Starting from 1 June 2026, SD Desktop external volumes billing units consption of Cloud-type billing units will be automatically allocated to your CSC project instead of manually assigned. Volumes usage from January 2026 to 26 May 2026 will also be charged retroactively.

If by then your project does not have enough billing units, the CSC project Billing Units balance will go negative, your virtual desktop will be paused, the project will be closed after 60 days, and all data will be permanently deleted 90 days after closure. To avoid disruption, please apply for additional billing units via the MyCSC portal as soon as possible, as processing times may vary.

Note!!!

To prepare for this change, please take the following steps and reserve sufficient time, as completing them may require some effort:

If you need support with these steps, are unsure whether your virtual desktop has a storage volume, or are unsure how many billing units to apply for, please contact service@csc.fi (subject: SD Desktop) and include your project number and virtual desktop name.



## 1. Step 1: verify how many volumes your project has in usage and thier size


1. [Login](./sd-desktop-login.md) to SD Desktop. All your virtual desktops are listed at the home page under **All connections**.

2. Select project (e.g. `project_NNNNN`) and click **plus icon**.
  
3. Now you can see all virtual desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name. If you encounted a black screen, yoru virtual desktop is probably paused and needs to be ressumed. 
   
4. On the left navitation bar click on the volume icon and check the volume size.
   
5. Reapeat these steps for all teh virtual desktop in your CSC project. 

![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

Add here image of volume from GitLab


## 2. Calculate how many billing units the virtual desktop volume consumes and which package you should apply for

Volumes consume 4.7 Cllouyd Biulling unites /Tib/ Hour. Here’s a table summarizing the Cloud Billing Units required for using **volumes** over **one year** for various options and correstpiondent Billing Units package you can apply for via the MYCSC portal.

| Volume Option | Cloud Billing Rate (units/TiB/hour) |  Cloud Billing Units (consumed in 1 year) | Select the correct BU Package in MyCSC and application frequency |
|----------------|---------------------------|--------------------------|------------------------|
| 200 GB | 4.7 | 4 000 |Small package, 2 times a year: 30 000 BUs assigned immediately| 
| 1 TB | 4.7 | 20 000 |Small package, 2 times a year: 30 000 BUs assigned immediately  |
| 10 TB | 4.7 | 200 000 |  Medium package, 2 times a year: 300 000 BUs Processed on average within 1-3 days by a Resource Officer |


## 3. Verify in MyCSC if your CSC project has enough billing units

1. Go to the MyCSC portal: https://my.csc.fi

2. Select your project

3. Check whether your project has sufficient billing units

4. If your project does not have enough billing units, apply for additional units by following these steps.

Please note:

* Any project member can apply for additional billing units

* Small packages are assigned immediately, while medium packages may take up to 3 days to be processed

* After submitting an application, there is a two‑week period during which you cannot submit another request. For this reason, it is important to apply early.

* During the application process, you will be asked to attach scientific publications. If you do not yet have publications directly related to this work, you may include any relevant past publications from your research group, even if they are not directly linked to the project.
