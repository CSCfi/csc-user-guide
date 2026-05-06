[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Create virtual desktops

With the SD Desktop service, you can create virtual computers for analysing sensitive data. On your virtual desktop, you can analyse sensitive research data through your web browser securely. In addition, SD Desktop provides a secure workspace for collaborative research projects. You can create multiple desktops for one CSC project and it doesn't require technical expertise.

## Step by step

1. Select correct CSC project from dropdown on the left side.
2. Click **Create desktop**.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop.png)

### In Create desktop window 

1. Select a name for your desktop. Choose a clear and descriptive name - especially if you're working on multiple projects - and make sure it only contains letters or numbers, with no special characters or spaces.
2. Select operating system. We recommend to choose **Linux Ubuntu22**. If you want to create a GPU desktop, please contact servicedesk@csc.fi (subject 'SD Desktop') before creation to confirm availability and receive further instructions.
3. Select a pre-built desktop option based on your needs. [See options below](#virtual-desktop-options)
4. Write **optional** description or note about the desktop to help your team members understand its purpose and contents.
5. Click **Create**. The window will now close and desktop creation will start.

After returning to the main page, you’ll see a list of your desktops. Creating a desktop can take up to 30 minutes, during which a "Creating" label will appear next to its name. If you try to open it too soon, you’ll get an error message. Once the status changes to "Running", the desktop is ready to use.

![Create desktop window.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop2.png)

![Access desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM.png)

### Virtual desktop options

| Use | Description | Technical specifications | Correspondent Pouta flavor | Cloud Billing Units consumption |
|---|---|---|---|---|
| **Small computation** | Ideal for simple statistical analysis, watching videos, or listening to audio files. Comparable to a personal laptop. | 6 cores, 15 GB memory, 80 GB root disk | standard.xlarge | About 48 000 Cloud Billing Units/year |
| **Medium computation** | Ideal for running specific scripts for complex statistical analysis (e.g. genetic data). Comparable to a powerful IT-managed laptop. | 8 cores, 30 GB memory, 80 GB root disk | standard.xxlarge | About 98 000 Cloud Billing Units/year |
| **Heavy computation** | Ideal for non-interactive programmatic analysis (machine learning) that requires heavy computation. Not recommended for simple analysis due to high resource consumption. | 28 cores, 176 GB memory, 80 GB root disk | hpc.6.28core | About 565 000 Cloud Billing Units/year |
| **Small GPU computation** | Available only upon request. Contact servicedesk@csc.fi (subject: “SD Desktop”) before creation to confirm availability and receive further details. | – | – | – |
| **Big Picture project** | Available only upon request. Contact servicedesk@csc.fi (subject: “SD Desktop”) before creation to confirm availability and receive further details. | – | – | – |


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } 
  { .csc-grid-card-warning }

    * All virtual GPU desktops created **without prior approval** will be deleted to ensure optimal use of limited resources. Please contact servicedesk@csc.fi (subject "Sensitive Data") for more information and planning.

    * Your virtual desktop is **accessible to all project members upon creation** and **consumes billing units** from your CSC project until [paused](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) or [deleted](./sd-desktop-manage.md#deleting-a-virtual-desktop)

    * Each CSC project supports 5 virtual desktops, with 10 project members allowed to connect simultaneously to each desktop.

    * All desktops come with a set of pre-installed open-source software managed by CSC. More informations about the list of pre-installed software and customisation is available [here](./sd-desktop-software.md).

    * **Delete or pause unused desktops**: Ensure to [delete](./sd-desktop-manage.md#deleting-a-virtual-desktop) or [pause](./sd-desktop-manage.md#pausing-or-unpausing-a-virtual-desktop) your desktop when not in use. Unused desktops trigger email notifications after 14 days of inactivity.

</div>


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

