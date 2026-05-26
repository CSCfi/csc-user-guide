[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Working with your virtual desktop: tips and essentials

## Prerequisites
* [Create virtual desktop](sd-desktop-create.md)
* [Access virtual desktop](sd-desktop-access-vm.md)


## Overview


SD Desktop is a secure environment designed specifically for analysing sensitive data and some features may work differently than a regular computer. For each of these features, a specific step-by-step guide is available. If you are using the service for the first time, reviewing these guides will help you become familiar with how everything works.


<div class="grid cards" markdown>

- :material-laptop:{ .lg .middle } **Introduction to virtual deskop**
  { .csc-grid-card-info }

    ---

    Learn basics of your virtual desktop.

    [Read more](#introduction-to-virtual-desktop)

- :material-apps:{ .lg .middle } **Software**
  { .csc-grid-card-info }
  
    ---

    Learn about software available in the virtual desktop environment.

    [Read more](sd-desktop-software.md)

- :material-harddisk:{ .lg .middle } **Where to save your data**
  { .csc-grid-card-info }

    ---

    Explanation of Home directory, Volume, and Shared directory, including how and when to use them.

    [Read more](#where-to-save-your-data-in-virtual-desktop)

- :material-lightbulb-on-outline:{ .lg .middle } **Tips**
  { .csc-grid-card-info }

    ---

    Best practices for working efficiently in your virtual desktop.

    [Read more](#tips)

</div>





## Introduction to virtual desktop

Below is an image showing the basic functions of a virtual desktop. Click the image to open it in a new window.

[![Virtual desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew-Overview.png)](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew-Overview.png)


<div class="grid cards" markdown>

- :material-check-circle:{ .lg .middle } **Key features**
  { .csc-grid-card-success }

    ---

    
    
    * **Shared file access for team members:** All CSC project members can access the virtual desktop. Files saved in the shared directory or external volume are available to others, enabling safe collaboration.

    * **The virtual desktop is completely isolated from the internet**. You can open a browser, but cannot access websites or online repositories, reducing security risks.

    * **The virtual desktop runs on Linux**, a secure and stable operating system suited for research. No prior experience is required, though the command line may take some learning. 

    * **A maximum of 10** CSC project members can be logged in and use a virtual desktop at the same time.


- :material-alert:{ .lg .middle } **Limitations**
  { .csc-grid-card-warning }

    ---

    * **Controlled file access and export with Data Gateway:** Each project member can import files to the virtual desktop using the Data Gateway application. Files can be imported only via SD Connect (direct upload), while data export is limited to the CSC Project Manager for security.

    * **Only encrypted files are accessible.** Unencrypted files will not appear and must first be encrypted using SD Connect. Data Gateway encrypts all exported files, adding extra data protection.

    * **Open source software only:** Only open-source software can be installed, as licensed or proprietary software is not supported.

</div>







## Where to save your data in virtual desktop

When you log in to the virtual desktop, you will see several icons on the left navigation bar, including several storage locations. Each one works differently, so it’s important to know where to save your research data.

| Name | Usage | Sharing | Data loss risk |
|------|-------|---------|----------------|
| **Data Gateway application** | Use this application to access your data via a secure connection. When you copy data through Data Gateway into the virtual desktop, it creates a decrypted working copy. This copy should always be saved inside the external volume (see below). Only the CSC Project Manager can export data. | — | — |
| **Files folder/ Home directory** | The internal storage of your virtual desktop—similar to the built‑in disk of a laptop. | Only you can see and access files stored here. | **Do not save large files here. If the system disk becomes full, the operating system will stop working and, in the worst case, the virtual desktop may become permanently unusable.** If the virtual desktop is deleted or crashes, everything in Home directory will be permanently lost. |
| **Volume** | An external storage space attached to the virtual desktop, similar to a removable drive (like a USB stick). Use a volume to store a copy of working copy of datasets you are analysing, results, scripts and notebooks, any important files you don’t want to lose. | It is shared with all members of your project. | If the virtual desktop crashes or runs out of disk space, your data in the volume remains safe. You can easily move  volume to a new virtual desktop after a service upgrade or if the virtual desktop becomes unusable. |
| **Shared directory** | Small shared folder visible to all project members. It should be used only for temporary transfers or exchanging small files. Move files quickly to the Volume if they need to be saved. | Visible to all project members | **Do not save large files here. If the system disk becomes full, the operating system will stop working and, in the worst case, the virtual desktop may become permanently unusable.** If the virtual desktop is deleted or crashes, everything in Shared directory will be permanently lost.  |

## Tips


### Change virtual desktop's resolution

If you switch between different laptops or use external monitors, the virtual desktop may not always display correctly. In those cases, adjusting the screen resolution can quickly restore a usable view:

??? default "Step by step"

    1. Click **Power icon** in top right corner of the desktop.

    2. Click **Gear icon**.

    3. **Settings** window is now open. In the left sidebar, select **Displays**.

    4. Under** Resolution**, open the dropdown menu and choose the resolution you prefer.

    5. Click **Apply**.
    
    6. Click **Keep Changes** if you're happy with the new resolution or **Revert Changes** if you want to try another resolution.

    ![Change resolution in virtual desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Resolution.png)


### Copy-paste text from your laptop to virtual desktop

For security reasons, copy-pasting from your own computer to SD Desktop is limited. You can still transfer text with a few extra steps, as explained in the instructions below. These restrictions ensure that no unauthorized data is copied or exported from the secure environment.
 
<div class="grid cards" markdown>

  - :material-alert:{ .lg .middle } 
    { .csc-grid-card-warning }

      - Copy-paste works only in one direction: **from your computer to virtual desktop**.
      - You need to **enable the copy-paste function each time** you start a virtual desktop session.

</div>

??? default "Step by step"

    1. Access the virtual desktop and press **Ctrl + Alt + Shift** to open the **Clipboard panel.** 
    2. Select **Text input** to enable copy-paste. Clipboard panel will close automatically. Do not close the Clipboard panel with Ctrl + Alt + Shift, as this may disable copy-paste.
    3. There is now a black bar at the bottom of the screen, which indicates that copy-paste is enabled.
    4. Open or create a document you want to edit. You can now copy text from your computer **(Ctrl + C or right-click)** and paste it in the virtual desktop **(Ctrl + V or right click)**. 
    5. To disable copy-paste press **Ctrl + Alt + Shift** to open the **Clipboard panel**, then select **None**. 

    ![Clipboard panel in virtual desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Clipboard.png)









## Your next steps in this guide

* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)

