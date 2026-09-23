## Manage virtual desktops: pausing, unpausing, restarting, deleting


## On this page: 

- 1. [Overview] (#1-overview)
- 2. [Pausing a virtual desktop](#2-pausing-a-virtual-desktop)
- 3. [Unpausing a virtual desktop](#3-unpausing-a-virtual-desktop)
- 4. [Restarting a virtual desktop](#4-restarting-a-virtual-desktop)
- 5. [Deleting a virtual desktop](#5-deleting-a-virtual-desktop)

## 1. Overview

**Virtual desktops consume Cloud Billing Units** from your CSC project while they are running. To avoid unnecessary usage, ensure you can pause or delete desktops when not in use. Desktops that remain inactive trigger email notifications to all the CSC project members after 14 days of inactivity. **Volumes consume Cloud Billing Units** starting from the moment they are created - whether or not they’re attached to a virtual desktop and whether or not the desktop a volume is attached to is paused.

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Pausing is not intended as a long‑term method for storing data**
  { .csc-grid-card-warning }

    ---
    
     CSC cannot guarantee the functionality of desktops paused for extended periods or not updated after service upgrades, including situations where required actions have not been performed.

</div>




### 2. Pausing a virtual desktop


1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop from the homepage.

2. Close all the programs, save or close all the files, and log out from the virtual desktop to prevent data corruption. 

3. On the SD Desktop homepage, click **Manage desktop**.

4. Click **Pause**. 

5. Confirm the operation via the notification. Pausing a desktop may take up to 30 minutes.

![Pause desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_PauseDesktop.png)

### 3. Unpausing a virtual desktop

You can unpause a virtual desktop if the CSC project is active and Cloud Billing Units balance is positive.

1. [Log in](./sd-desktop-login.md) to SD Desktop.

2. On the SD Desktop homepage, click **Manage desktop** on the right side of the correct desktop.

3. Click **Unpause**. 

4. Confirm the operation via the notification.

![Unpause desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_UnpauseDesktop.png)

___

## 4. Restarting a virtual desktop

If your virtual desktop or software becomes unresponsive, you can restart it. All files and software saved on the virtual desktop will remain accessible.

<div class="grid cards" markdown>

- :material-information:{ .lg .middle } **Info**
  { .csc-grid-card-info }
    
    ---
  
    **If the Data Gateway application becomes unresponsive** due to old sessions running in the background, there's no need to restart your desktop. Instead, you can utilize the terminal to identify and halt the process. For assistance, please [contact CSC Service Desk](../../support/contact.md), subject "Sensitive data."

</div>

1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop from the homepage.

2. Close all the programs, save or close all the files, and log out from the virtual desktop to prevent data corruption. 
    
3. On the SD Desktop homepage, click **Manage desktop** on the right side of the correct desktop.

4. Click **Restart**. 
    
5. Confirm the operation via the notification. Restarting a desktop may take up to 30 minutes.

![Restart desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_RestartDesktop.png)

___


## 5. Deleting a virtual desktop

At the end of your analysis, you can delete entire virtual desktop, and all files saved to it by you or other project members. 

<div class="grid cards" markdown>

- :material-close-circle:{ .lg .middle } **Warning**
  { .csc-grid-card-error }
    
    You cannot undo this action. Please contact all the project members before deleting a virtual desktop.
    
</div>

1. [Log in](./sd-desktop-login.md) to SD Desktop.

2. On the SD Desktop homepage, click **Manage desktop** on the right side of the correct desktop.

3. Click **Delete**. 

4. Confirm the operation via the notification. 

![Delete desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_DeleteDesktop.png)

___


## Your next steps in this guide

* [Accessing virtual desktop](./sd-desktop-access-vm.md)
* [Working with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)
