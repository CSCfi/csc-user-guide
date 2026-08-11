[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Create virtual desktop and volume

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/wb4TwsqNCRE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/KgdGueesSe4" title="Luo virtuaalinen työpöytä SD Desktop -palvelussa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

With the SD Desktop service, you can create virtual computers for analysing sensitive data via web browser. In addition, SD Desktop provides a secure workspace for collaborative research projects. You can create up to six virtual desktops for one CSC project. Creating a virtual desktop doesn't require technical expertise.


1. [Log in to SD Desktop](#1-log-in-to-sd-desktop)

2. [Select correct options](#2-select)

3. [Add an external volume](#3-add-an-external-volume-virtual-external-hard-drive)

4. [Create virtual desktop](#4-create-virtual-desktop)

5. [Make sure your CSC project has sufficient Billing Units](#5-make-sure-your-csc-project-has-sufficient-billing-units-bu)

6. [Important considerations](#6-important-considerations)

## Step by step

### 1. Log in to SD Desktop

* Log in to SD Desktop.
* Click **Go to SD Desktop Management**.

![Go to SD Desktop Management.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

### 2. Select

1. correct CSC project
2. operating system. **Please select Default Ubuntu 22.04** as the operating system. Other available operating systems are only available after contacting the service desk and following specific instructions.

4. name for your desktop. A descriptive name is useful, especially if you are working on multiple projects. Note, that the name should only include letters or numbers, and you shouldn't use special characters or spaces in the name.
5. a pre-built desktop option based on your needs. [See options below](#virtual-desktop-options).

![Virtual desktop selections.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_SelectProject.png)

#### Virtual desktop options

|  | Use  | Technical specifications | Corresponding Pouta Flavor | Cloud Billing Units consumption |
|-|-|-|-|-|
|  **Small computation** | Ideal for analyzing sensitive data using office software (for example: similar to simple statistical analysis with Excel, watching videos, listening to audio files, and working on text files). You can compare this desktop to your laptop. | Core 6; Memory 15 GB; Root disk 80 GB; | standard.xlarge | 5.2 Cloud Billing Units/h |
|  **Medium computation**  | Ideal for running complex statistical or genome analysis (for example: using the command line to run specific scripts). You can compare this desktop to a powerful laptop provided by your organization's IT unit. | Core 8; Memory 30 GB; Root disk 80 GB | standard.xxlarge | 10.92 Cloud Billing Units/h |
| **Heavy computation**| Ideal for running non-interactive programmatic analysis (machine learning) that requires heavy computation. Please do not choose this option for simple analysis, as it consumes considerable resources. | Core 20; Memory 87 GB; Root disk 80 GB  | hpc.4.20 core | 39 Cloud Billing Units/h|
| **Small GPU computation**| This option is available only upon request. Please contact servicedesk@csc.fi (subject 'SD Desktop') before creation to confirm availability and receive further details | 1 GPU  | 78 Cloud Billing Units/h |  |
| **Big Picture project**| This option is available only upon request. Please contact servicedesk@csc.fi  (subject 'SD Desktop') before creation to confirm availability and receive further details | 1 GPU | 195 Cloud Billing Units/h |  |

!!! note
    All virtual GPU desktops created **without prior approval** will be deleted to ensure optimal use of limited resources. Please contact servicedesk@csc.fi (subject "Sensitive Data") for more information and planning. 

### 3. Add an external volume (virtual external hard drive)

When creating a desktop, you must also add a volume, where you will import the data for analysis. 

1. Choose a size that covers the combined size of your dataset and working files via the user interface, up to 200 GB. An empty volume can be extended with additional storage upon request to service desk, after desktop creation and if no data or files have been saved on it. To request an extension, contact [CSC Service Desk](../../support/contact.md), *(subject: SD Desktop) and share your CSC project number, virtual desktop  and volume name. If you are unsure about which volume size you should choose for your project, contact us for support. 

2. Name your volume. Note, that the volume name should not include special characters or spaces.

* It’s recommended to save critical analyses or files on the volume, which can also act as a backup if the virtual desktop becomes unresponsive.
  
* **You can detach and attach a volume from your virtual desktop** on the SD Desktop Management page. This can be compared to connecting/disconnecting a USB stick to your laptop. This feature is available only on desktops created after February 2023. For additional details, refer to: [Managing volume and desktops](./sd-desktop-manage.md).

*  Volumes consume 4.7 Cloud Billing units/TiB/hour until deleted. 

![Add volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Volume.png)

### 4. Create virtual desktop

4. Click *Create desktop*. The operation is entirely automated and can take up to 30 minutes. If you try accessing the virtual desktop during this process, an error message will be displayed asking you to return later. 

!!! Note
    After clicking "Create," please be aware that the confirmation notification may take up to 90 seconds to appear at the bottom of the page. If you are unsure whether the action was successful, please reach out to us at the service desk. We apologize for any inconvenience this may cause.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)


### 5. Make sure your CSC project has sufficient Billing Units (BU).

Once created, your virtual desktop and any associated storage volumes begin consuming resources, measured in Cloud Billing Units (BU), from your project allocation.

**Please review the following important information:**

1. Ensure sufficient Billing Units (BU) are available in your project before creating a virtual desktop. If necessary, [apply for additional BU by following the step-by-step guide, which includes example estimates to help you determine your requirements.](sd-billing-units.md). 

2. Virtual desktops consume Billing Units based on the selected option. When a virtual desktop is [paused](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop), consumption is significantly reduced; however, approximately 3,200 BU per year will still be charged until the virtual desktop is deleted [deleted](./sd-desktop-manage.md#deleting-a-virtual-desktop).

3. External volumes consume Billing Units continuously based on their allocated size. Charges apply regardless of whether the volume is attached to a virtual desktop or whether the desktop is running or paused. Billing continues until the volume is deleted.

4. If your project's BU balance becomes negative:

* All virtual desktops in the project will be automatically paused.

* You will not be able to create new virtual desktops.

* The CSC project will be scheduled for closure after 60 days. After approximately 90 days, the project and all associated content will be permanently deleted.

You will receive automated email notifications throughout the process, including warnings, status updates, and instructions on any actions that may be required.



## 6. Important considerations

* Your virtual desktop is **accessible to all the CSC project members upon creation**. All project members can import file, install software, permanently delete the virtual desktop and its entire content. Only the CSC project manager can export files from the secure environment. 

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

