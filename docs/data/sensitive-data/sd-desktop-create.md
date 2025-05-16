[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Create virtual desktops

With the SD Desktop service, you can create virtual computers for analysing sensitive data. On your virtual desktop, you can analyze sensitive research data through your web browser securely. In addition, SD Desktop provides a secure workspace for collaborative research projects. You can create up to three virtual desktops for one CSC project. Creating a virtual desktop doesn't require technical expertise.

## Step by step

1. Select correct CSC project from dropdown on the left side.
2. Click **Create desktop**.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop.png)



### In Create desktop window 

1. Select name for your desktop. A descriptive name is useful, especially if you are working on multiple projects. Note, that the name should only include letters or numbers, and you shouldn't use special characters or spaces in the name.
2. Select operating system. We recommend to choose **Linux Ubuntu22**, since there will be no updates published for Linux CentOS7 after June 30, 2024.
3. Select a pre-built desktop option based on your needs. [See options below](#virtual-desktop-options)
4. (optional) Write description or note about the desktop for your team. This helps other team members understand its purpose and contents.
5. Click **Create**. The operation is entirely automated and can take up to 30 minutes. If you try accessing the virtual desktop during this process, an error message will be displayed asking you to return later.

![Create desktop window.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop2.png)


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

