[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Create virtual desktops and volumes

![Virtual desktop and volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/VM_and_volume.png){ style="float: right; margin: 0 3em 3em 3em; width: 45%;" }

SD Desktop lets you create a protected environment for both individual work and collaborative research projects sdirectly through your web browser. All steps are completed through an easy-to-use interface, and no technical expertise is required.

1. [**Create virtual desktop:**](#create-virtual-desktop) Create secure virtual desktops for analysing sensitive research data.
2. [**Create volume:**](#create-volume) You need a volume to store your data. 
3. **Attach volume to desktop:** After creating a volume, simply attach it to your virtual desktop. 


## Create virtual desktop

You can create **up to three desktops** within a single CSC project, with **up to 10 project members** allowed to connect simultaneously to each desktop. Your virtual desktop is accessible to all project members upon creation.

All desktops come with a set of **pre‑installed open‑source software** managed by CSC. More information about the available software and customization options is available [here](./sd-desktop-software.md).

Desktops consume **Cloud Billing Units** from your CSC project while they are running. To avoid unnecessary usage, ensure you [pause](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) or [delete](./sd-desktop-manage.md#deleting-a-virtual-desktop) desktops when not in use. Desktops that remain inactive trigger email notifications after 14 days of inactivity.

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }
    
    All virtual GPU desktops created **without prior approval** will be deleted to ensure optimal use of limited resources. Please contact servicedesk@csc.fi (subject "Sensitive Data") for more information and planning.

</div>

### Step by step

1. Select correct CSC project from dropdown on the left side.
2. Click **Create desktop**.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop.png)

#### In Create desktop window 

1. Select a name for your desktop. Choose a clear and descriptive name - especially if you're working on multiple projects - and make sure it only contains letters or numbers, with no special characters or spaces.
2. Select operating system. We recommend to choose **Linux Ubuntu22**. If you want to create a GPU desktop, please contact servicedesk@csc.fi (subject 'SD Desktop') before creation to confirm availability and receive further instructions.
3. Select a pre-built desktop option based on your needs. [See options below](#virtual-desktop-options)
4. Write **optional** description or note about the desktop to help your team members understand its purpose and contents.
5. Click **Create**. The window will now close and desktop creation will start.

After returning to the main page, you’ll see a list of your desktops. Creating a desktop can take up to 30 minutes, during which a "Creating" label will appear next to its name. If you try to open it too soon, you’ll get an error message. Once the status changes to "Running", the desktop is ready to use.

![Create desktop window.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop2.png)

![Access desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM.png)

#### Virtual desktop options

| Use | Description | Technical specifications | Correspondent Pouta flavor | Cloud Billing Units consumption |
|---|---|---|---|---|
| **Small computation** | Ideal for simple statistical analysis, watching videos, or listening to audio files. Comparable to a personal laptop. | 6 cores, 15 GB memory, 80 GB root disk | standard.xlarge | About 48 000 Cloud Billing Units/year |
| **Medium computation** | Ideal for running specific scripts for complex statistical analysis (e.g. genetic data). Comparable to a powerful IT-managed laptop. | 8 cores, 30 GB memory, 80 GB root disk | standard.xxlarge | About 98 000 Cloud Billing Units/year |
| **Heavy computation** | Ideal for non-interactive programmatic analysis (machine learning) that requires heavy computation. Not recommended for simple analysis due to high resource consumption. | 28 cores, 176 GB memory, 80 GB root disk | hpc.6.28core | About 565 000 Cloud Billing Units/year |
| **Small GPU computation** | Available only upon request. Contact servicedesk@csc.fi (subject: “SD Desktop”) before creation to confirm availability and receive further details. | – | – | – |
| **Big Picture project** | Available only upon request. Contact servicedesk@csc.fi (subject: “SD Desktop”) before creation to confirm availability and receive further details. | – | – | – |



## Create volume

You can create **up to five volumes** per project. You need a volume to store your data. A volume works like a virtual USB stick: it can be attached to one virtual desktop at a time or moved between desktops within the same CSC project. The volume also acts as a backup if the virtual desktop becomes unresponsive.

Volumes consume Clour Billing Units per GB per hour, starting from the moment they are created - whether or not they’re attached to a virtual desktop. Check billing unit comsumption from table below.

A volume **can only be extended** with additional storage before any data or files are saved on it. To request a storage extension, contact CSC Service Desk (subject: SD Desktop).

### Step by step

1. Select correct CSC project from dropdown on the left side.
2. Click **Create volume**. 

![Create volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateVolume.png)

#### In Create volume window 

1. Select a name for your volume. Choose a clear and descriptive name - especially if you're working on multiple projects - and make sure it only contains letters or numbers, with no special characters or spaces.

2. Choose from the available options the one that covers the combined size of your dataset and working files. If you have a dataset larger than 1000 GB, contact [CSC Service Desk](../../support/contact.md).

3. Write **optional** description or note about the volume to help your team members understand its purpose and contents.

4. Click **Create**. The window will now close and volume creation will start.

Back on the main page, you will see a list of your volumes. You can now proceed to attach it to your desktop.

![Create volume window.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateVolume2.png)

![Volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Volumes.png)

#### Volume options

| Name   | Size (GB) | Cost (BU/h) |
|--------|-----------|-------------|
| Large  | 1000      | 3.5         |
| Medium | 500       | 1.75        |
| Small  | 200       | 0.7         |

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

