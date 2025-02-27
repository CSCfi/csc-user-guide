# Create virtual desktops

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/wb4TwsqNCRE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/KgdGueesSe4" title="Luo virtuaalinen työpöytä SD Desktop -palvelussa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

With the SD Desktop service, you can create virtual computers for analysing sensitive data. On your virtual desktop, you can analyze sensitive research data through your web browser securely. In addition, SD Desktop provides a secure workspace for collaborative research projects. You can create up to three virtual desktops for one CSC project. Creating a virtual desktop doesn't require technical expertise.

## Step by step

### 1. Log in to SD Desktop

* Log in to SD Desktop.
* Click **Go to SD Desktop Management**.

![Go to SD Desktop Management.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

### 2. Select

1. correct CSC project
2. operating system. We recommend to choose **Linux Ubuntu22**, since there will be no updates published for Linux CentOS7 after June 30, 2024.
3. name for your desktop. A descriptive name is useful, especially if you are working on multiple projects. Note, that the name should only include letters or numbers, and you shouldn't use special characters or spaces in the name.
4. a pre-built desktop option based on your needs. [See options below](#virtual-desktop-options)

![Virtual desktop selections.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_SelectProject.png)

#### Virtual desktop options

|  | Use  | Technical specifications | Correspondent Pouta Flavor | Billing Units consumption |
|-|-|-|-|-|
|  **Small computation** | Ideal for analyzing sensitive data using office software (for example: similar to simple statistical analysis with Excel, watching videos, listening to audio files, and working on text files). You can compare this desktop to your laptop. | Core 6; Memory 15 GB; Root disk 80 GB; | standard.xlarge | 5.2 billing units/h|
|  **Medium computation**  | Ideal for running complex statistical or genome analysis (for example: using the command line to run specific scripts). You can compare this desktop to a powerful laptop provided by your organization's IT unit. | Core 8; Memory 30 GB; Root disk 80 GB | standard.xxlarge | 10.4 billing units/h |
| **Heavy computation**| Ideal for running non-interactive programmatic analysis (machine learning) that requires heavy computation. Please do not choose this option for simple analysis, as it consumes considerable resources. | Core 28; Memory 176 GB; Root disk 80 GB  | hpc.6.28 core | 65 billing units/h |
| **Small GPU computation**| This option is available only upon request. Please contact servicedesk@csc.fi (subject 'SD Desktop') before creation to confirm availability and receive further details |  |  |  |
| **Big Picture project**| This option is available only upon request. Please contact servicedesk@csc.fi  (subject 'SD Desktop') before creation to confirm availability and receive further details |  |  |  |

!!! note
    All virtual GPU desktops created **without prior approval** will be deleted to ensure optimal use of limited resources. Please contact servicedesk@csc.fi (subject "Sensitive Data") for more information and planning. The medium GPU computation option has been deprecated in October 2024. 


### 3. Add an external volume (virtual external hard drive)

Add an external  volume to your virtual desktop, extending default storage (80 GB) up to 200 GB.

1. Choose a size that covers the combined size of your dataset and working files. If you are unsure about which volume size you should choose, send an email to [CSC Service Desk](../../support/contact.md).

2. Name your volume. Note, that the volume name should not include special characters or spaces.

* It’s recommended to save critical analyses or files on the volume, which can also act as a backup if the virtual desktop becomes unresponsive. Please note that after the virtual desktop is set up, the volume can only be extended with additional storage if no data or files have been saved on it. To request an extension, contact [CSC Service Desk](../../support/contact.md), *(subject: SD Desktop)*.

* **You can detach and attach a volume from your virtual desktop** on the SD Desktop Management page. This can be compared to connecting/disconnecting a hard drive to your laptop. This feature is available only on desktops created after February 2023. For additional details, refer to: [Managing volume and desktops](./sd-desktop-manage.md).

![Add volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Volume.png)

### 4. Create virtual desktop

Finally, click *Create desktop*. The operation is entirely automated and can take up to 30 minutes. If you try accessing the virtual desktop during this process, an error message will be displayed asking you to return later.

!!! Note
    After clicking "Create," please be aware that the confirmation notification may take up to 30 seconds to appear. If you are unsure whether the action was successful, please reach out to us at the service desk. We apologize for any inconvenience this may cause.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)

## Important considerations

* Your virtual desktop is **accessible to all project members upon creation** and **consumes billing units** from your CSC project until [paused](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) or [deleted](./sd-desktop-manage.md#deleting-a-virtual-desktop)

* Each CSC project supports up to 3 virtual desktops, with 10 project members allowed to connect simultaneously to each desktop.

* All desktops come with a set of pre-installed open-source software managed by CSC. More informations about the list of pre-installed software and customisation is available [delete](./sd-desktop-software.md).

* **Delete or pause unused desktops**: Ensure to [delete](./sd-desktop-manage.md#deleting-a-virtual-desktop) or [pause](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) your desktop when not in use. Unused desktops trigger email notifications after 14 days of inactivity.
  

!!! info "Need assistance?"
    If you're uncertain about which desktop to choose or need support for your research, contact [CSC Service Desk](../../support/contact.md) with the subject "Sensitive data".


## Your next steps in this guide

* [Managing volumes and virtual desktops](./sd-desktop-manage.md)
* [Accessing virtual desktop](./sd-desktop-access-vm.md)
* [Working with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)

