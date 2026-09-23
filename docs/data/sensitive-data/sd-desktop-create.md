[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Create virtual desktops and volumes

## On this page:

1. [Create virtual desktop](#1-create-virtual-desktop)
1.1 [Step by step]
1.2 [Virtual desktop options]
2. [Create volume]
2.1 [Step by step]
2.2 [Volume options]




SD Desktop lets you create a secure virtual workspace for working with sensitive data, either individually or with other members of your CSC project. Everything can be set up directly through your web browser, and no technical expertise is required.

To start working with data, you create:

1. a virtual desktop, which provides the computing environment where you analyse your data; and
2. a storage volume, which provides additional storage space that can be attached to the virtual desktop. You can import data from SD Connect to this volume for analysis.

You can create, access, and manage both the virtual desktop and storage volume through the SD Desktop user interface.

![Virtual desktop and volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/VM_and_volume.png){ style="float: right; margin: 0 3em 3em 3em; width: 45%;" }


## 1. Create virtual desktop


You can create **up to three virtual desktops** within a single CSC project, with **up to 10 project members** allowed to connect simultaneously to each desktop. Your virtual desktop is accessible to all project members upon creation.

All desktops come with **pre‑installed open‑source software** managed by CSC. More information about software and customization options is available [here](./sd-desktop-software.md).

Desktops consume **Cloud Billing Units** from your CSC project while they are running. To avoid unnecessary usage, [pause](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) or [delete](./sd-desktop-manage.md#deleting-a-virtual-desktop) desktops when not in use. Desktops that remain inactive trigger email notifications after 14 days of inactivity.


<div class="grid cards" markdown>

- :material-close-circle:{ .lg .middle } **Desktop storage limit**
  { .csc-grid-card-error }
    
    Desktops have 80 GB of storage by default. **If you save more than 80 GB of data to your desktop, it becomes unresponsive and you may lose your data**. To avoid this, please create and attach a [**volume**](#create-volume) to your desktop and save your data there.

</div>


### 1.1 Step by step

1. Select correct CSC project from drop down on the left side.
2. Click **Create desktop**.

**In  the new Create desktop window**:

1. **Select a name** for your desktop. Choose a clear and descriptive name - especially if you're working on multiple projects - and make sure it only contains letters or numbers, with no special characters or spaces.
2. **Select operating system.** We recommend to choose **Linux Ubuntu22**. If you want to create a GPU desktop, please contact servicedesk@csc.fi (subject 'SD Desktop') before creation to confirm availability and receive further instructions.
3. **Select a pre-built desktop option** based on your needs. [See options below](#virtual-desktop-options)
4. Write **optional** description or note about the desktop to help your team members understand its purpose and contents.
5. Click **Create**. The window will now close and desktop creation will start.

After returning to the main page, you’ll see a list of your desktops in **Desktops tab**. Creating a desktop can take up to 30 minutes, during which a **Creating** label will appear next to its name. If you try to open it too soon, you’ll get an error message. Once the status changes to **Running**, the desktop is ready to use.


![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop.png)

![Create desktop window.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop2.png)

![Access desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM.png)

#### 1.2 Virtual desktop options

| Use | Description | Technical specifications | Correspondent Pouta flavor | Cloud Billing Units consumption per hour | Cloud Billing Units consumption per year |
|---|---|---|---|---|---|
| **Small computation** | Ideal for simple statistical analysis, watching videos, or listening to audio files. Comparable to a personal laptop. | 6 cores, 15 GB memory, 80 GB root disk | standard.xlarge | 5.6 Cloud Billing Units/h |  About 49 000 Cloud Billing Units/year |
| **Medium computation** | Ideal for running specific scripts for complex statistical analysis (e.g. genetic data). Comparable to a powerful IT-managed laptop. | 8 cores, 30 GB memory, 80 GB root disk | standard.xxlarge | 11.32 Cloud Billing Units/h | About 99 000 Cloud Billing Units/year |
| **Heavy computation** | Ideal for non-interactive programmatic analysis (machine learning) that requires heavy computation. Not recommended for simple analysis due to high resource consumption. | Core 20; Memory 87 GB; Root disk 80 GB | hpc.4.20 core | 39 Cloud Billing Units/h| About 565 000 Cloud Billing Units/year |
| **Small GPU computation** | Available only upon request. Contact servicedesk@csc.fi (subject: “SD Desktop”) before creation to confirm availability and receive further details. | – | – | – | – |
| **Big Picture project** | Available only upon request. Contact servicedesk@csc.fi (subject: “SD Desktop”) before creation to confirm availability and receive further details. | – | – | – | – |

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }
    
    All virtual GPU desktops created **without prior approval** will be deleted to ensure optimal use of limited resources. Please contact servicedesk@csc.fi (subject "Sensitive Data") for more information and planning.

</div>



## 2. Create volume


<div class="grid cards" markdown>

- :material-close-circle:{ .lg .middle } **Desktop storage limit**
  { .csc-grid-card-error }
    
    Desktops have 80 GB of storage by default. **If you save more than 80 GB of data to your desktop, it becomes unresponsive and you may lose your data**. To avoid this, please create and attach a **volume** to your desktop and save your data there.

</div>


You can create **up to five volumes** per CSC project. A volume works like a virtual USB stick: it can be attached to one virtual desktop at a time or moved between desktops within the same CSC project. The volume also acts as a backup if a virtual desktop becomes unresponsive.

**Volumes consume Cloud Billing Units** starting from the moment they are created, whether or not they’re attached to a virtual desktop. Check billing unit consumption from the [table](#volume-options) below.

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }
    
   
    A volume **can only be extended** with additional storage before any data or files are saved on it. To request a storage extension, contact CSC Service Desk (subject: SD Desktop).

</div>

### 2.1 Step by step

1. Select correct CSC project from dropdown on the left side.
   
2. Click **Create volume**. 

**In Create volume window**:

1. **Select a name** for your volume. Choose a clear and descriptive name - especially if you're working on multiple projects - and make sure it only contains letters or numbers, with no special characters or spaces.

2. **Choose from the available options** the one that covers the combined size of your dataset and working files. 

3. Write **optional** description or note about the volume to help your team members understand its purpose and contents.

4. Click **Create**. The window will now close and volume creation will start.
   
5. Back on the main page, you will see a list of your volumes in **Volumes tab**. 


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }
    
    If you have a dataset **larger than 1 TB**, contact [CSC Service Desk](../../support/contact.md).

</div>


![Create volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateVolume.png)

![Create volume window.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateVolume2.png)

![Volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Volumes.png)

#### 2.2 Volume options

| Name   | Size (GB) | Cost (BU/TiB/h) |
|--------|-----------|-------------|
| Small  | 200       | 4.7        |
| Medium | 500       | 4.7        |
| Large  | 1000      | 4.7        |


<div class="grid cards" markdown>

- :material-information:{ .lg .middle } **Info**
  { .csc-grid-card-info }
    
    If you're uncertain about which desktop or volume to choose or need support for your research, contact [CSC Service Desk](../../support/contact.md) with the subject "SD Services".

</div>


### 3. Attach volume to desktop

Once you have created a virtual desktop and a volume, you can attach them. Desktops created after 28 September 2026 support multiple volumes, while earlier desktops support only one. Each volume can be attached to only one desktop at a time.

Continue to the next section of this user guide to learn how to manage and [attach](sd-desktop-manage.md#attaching-or-detaching-a-volume) volumes. 



## Your next steps in this guide

* [Managing volumes and virtual desktops](./sd-desktop-manage.md)
* [Accessing virtual desktop](./sd-desktop-access-vm.md)
* [Working with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)
