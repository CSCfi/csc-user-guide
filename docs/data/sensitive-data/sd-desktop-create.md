[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Create virtual desktop and volume

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/wb4TwsqNCRE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/KgdGueesSe4" title="Luo virtuaalinen työpöytä SD Desktop -palvelussa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

With the SD Desktop service, you can create virtual computers for analysing sensitive data via web browser. In addition, SD Desktop provides a secure workspace for collaborative research projects. You can create up to six virtual desktops for one CSC project. Creating a virtual desktop doesn't require technical expertise.

## Step by step

### 1. Log in to SD Desktop

* Log in to SD Desktop.
* Click **Go to SD Desktop Management**.

![Go to SD Desktop Management.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

### 2. Select

1. correct CSC project
2. operating system. **Please select Default Ubuntu 22.04** as the operating system.
Choosing another option will cause the virtual desktop to stop working. Other operating systems are only available after contacting the service desk and following specific instructions.

4. name for your desktop. A descriptive name is useful, especially if you are working on multiple projects. Note, that the name should only include letters or numbers, and you shouldn't use special characters or spaces in the name.
5. a pre-built desktop option based on your needs. [See options below](#virtual-desktop-options). Please note that running desktops are the main source of Billing Units consumption. When paused, consumption is significantly reduced, but ~3,200 BU per year are still charged until the virtual desktop is deleted.


![Virtual desktop selections.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_SelectProject.png)

#### Virtual desktop options

|  | Use  | Technical specifications | Corresponding Pouta Flavor | Cloud Billing Units consumption |
|-|-|-|-|-|
|  **Small computation** | Ideal for analyzing sensitive data using office software (for example: similar to simple statistical analysis with Excel, watching videos, listening to audio files, and working on text files). You can compare this desktop to your laptop. | Core 6; Memory 15 GB; Root disk 80 GB; | standard.xlarge | 5.2 Cloud Billing Units/h |
|  **Medium computation**  | Ideal for running complex statistical or genome analysis (for example: using the command line to run specific scripts). You can compare this desktop to a powerful laptop provided by your organization's IT unit. | Core 8; Memory 30 GB; Root disk 80 GB | standard.xxlarge | 10.92 Cloud Billing Units/h |
| **Heavy computation**| Ideal for running non-interactive programmatic analysis (machine learning) that requires heavy computation. Please do not choose this option for simple analysis, as it consumes considerable resources. | Core 28; Memory 176 GB; Root disk 80 GB  | hpc.6.28 core | 65 Cloud Billing Units/h |
| **Small GPU computation**| This option is available only upon request. Please contact servicedesk@csc.fi (subject 'SD Desktop') before creation to confirm availability and receive further details | 1 GPU  | 78 Cloud Billing Units/h |  |
| **Big Picture project**| This option is available only upon request. Please contact servicedesk@csc.fi  (subject 'SD Desktop') before creation to confirm availability and receive further details | 1 GPU | 195 Cloud Billing Units/h |  |

!!! note
    All virtual GPU desktops created **without prior approval** will be deleted to ensure optimal use of limited resources. Please contact servicedesk@csc.fi (subject "Sensitive Data") for more information and planning. The medium GPU computation option has been deprecated in October 2024. 


### 3. Add an external volume (virtual external hard drive)

When creating a desktop, you must also add a volume, where you will import the data for analysis. External volumes consume Cloud Billing Units continuously based on their size, regardless of whether they are attached to a desktop or if the associated desktop is paused. Charges continue until the volume is deleted.

1. Choose a size that covers the combined size of your dataset and working files. If you are unsure about which volume size you should choose, send an email to [CSC Service Desk](../../support/contact.md).

2. Name your volume. Note, that the volume name should not include special characters or spaces.

* It’s recommended to save critical analyses or files on the volume, which can also act as a backup if the virtual desktop becomes unresponsive. Please note that after the virtual desktop is set up, the volume can only be extended with additional storage if no data or files have been saved on it. To request an extension, contact [CSC Service Desk](../../support/contact.md), *(subject: SD Desktop)*.

* **You can detach and attach a volume from your virtual desktop** on the SD Desktop Management page. This can be compared to connecting/disconnecting a USB stick to your laptop. This feature is available only on desktops created after February 2023. For additional details, refer to: [Managing volume and desktops](./sd-desktop-manage.md).


| Volume Option | Cloud Billing Rate (units/TiB/hour) |  Cloud Billing Units (consumed in 1 year) | Select the correct BU Package in MyCSC and application frequency |
|----------------|---------------------------|--------------------------|------------------------|
| 200 GB | 4.7 | 8 000 | Small package, once a year: 30 000 BUs assigned immediately| 
| 1 TB | 4.7 | 41 000 | Small package, 2 times a year: 30 000 BUs assigned immediately  |
| 10 TB | 4.7 | 402 000 | Medium package, 2 times a year: 300 000 BUs Processed on average within 1-3 days by a Resource Officer |


![Add volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Volume.png)

### 4. Create virtual desktop and verify if your project has sufficient Billing Units

4. Finally, click *Create desktop*. The operation is entirely automated and can take up to 30 minutes. If you try accessing the virtual desktop during this process, an error message will be displayed asking you to return later.

!!! Note
    After clicking "Create," please be aware that the confirmation notification may take up to 90 seconds to appear at the bottom of the page. If you are unsure whether the action was successful, please reach out to us at the service desk. We apologize for any inconvenience this may cause.

4.2 The virtual desktop and external volume will start consuming your CSC project resources (also referred to as Cloud Billing Units, BU). Please ensure that your project has sufficient Billing Units available. If needed, apply for additional BU in advance.

**Important:**
- If your project’s BU becomes negative, your CSC project will be suspended after 60 days.
- After approximately 90 days, the project and all its content will be automatically deleted.
You will receive automated email notifications to keep you informed and provide instructions throughout the process.


![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)

## Important considerations

* Your virtual desktop is **accessible to all project members upon creation**. A running virtual desktop and a volume **consumes Cloud Billing Units type** from your CSC project until [paused](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) or [deleted](./sd-desktop-manage.md#deleting-a-virtual-desktop)

* Each CSC project supports up to 6 virtual desktops, with 10 project members allowed to connect simultaneously to each desktop.

* All desktops come with a set of pre-installed open-source software managed by CSC. Read more about [pre-installed software and customisation.](./sd-desktop-software.md).

* **Delete or pause unused desktops**: Ensure to [delete](./sd-desktop-manage.md#deleting-a-virtual-desktop) or [pause](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) your desktop when not in use. You will receive email notifications after 14 days of inactivity.
  

!!! info "Need assistance?"
    If you're uncertain about which desktop to choose or need support for your research, contact [CSC Service Desk](../../support/contact.md) with the subject "SD Services".


## Your next steps in this guide

* [Managing volumes and virtual desktops](./sd-desktop-manage.md)
* [Accessing virtual desktop](./sd-desktop-access-vm.md)
* [Working with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)

