[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Managing virtual desktops

With the SD Desktop service, you can easily pause, reboot or delete your virtual desktops. 

* [Pausing or unpausing a virtual desktop](#pausing-or-unpausing-a-virtual-desktop)
* [Rebooting a virtual desktop](#rebooting-a-virtual-desktop)
* [Deleting a virtual desktop](#deleting-a-virtual-desktop)

!!! Note
    These options are available only on virtual desktops created after February 2, 2023. Please [contact service desk](../../support/contact.md) if you are working with older desktops. 



## Pausing or unpausing a virtual desktop

You can pause a virtual desktop. In this manner, the desktop will stop consuming billing units. 

### Pausing a virtual desktop


1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop from the homepage.

2. Close all the programs, save or close all the files, and log out from the virtual desktop to prevent data corruption. 

3. On the SD Desktop homepage, click **Manage volume**.

4. Click **Pause desktop**. 

5. Confirm the operation via the notification. Pausing a desktop may take up to 30 minutes.

!!! note
    You can't access or detach a volume while a desktop is paused.

![Pause desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_PauseDesktop.png)

### Resuming a virtual desktop

1. [Log in](./sd-desktop-login.md) to SD Desktop. On the SD Desktop homepage, click **Go To SD Desktop Management**.

2. At the bottom of the page, under **Available desktops**, select the correct virtual desktop. In the same row, click **Options** on the right, then choose **Resume**.

!!! note
    Resuming a paused desktop is only possible for active CSC projects with available billing units. 

![Resume desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Resume_desktop.png)


## Rebooting a virtual desktop

If your virtual desktop or software becomes unresponsive, you can reboot it. After the reboot, all files and software saved on the virtual desktop will remain accessible.

!!! Note
    If the Data Gateway application becomes unresponsive due to old sessions running in the background, there's no need to reboot your desktop. Instead, you can utilize the terminal to identify and halt the process. For assistance, please [contact CSC Service Desk](../../support/contact.md), subject "Sensitive data."

To reboot a desktop:

1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop on the homepage under **All connections**.

2. Close all programs and ensure you save or close any files to prevent data corruption.
    
3. On the SD Desktop homepage, click **Go To SD Desktop Management**.
    
4. At the bottom of the page, under **Available desktops**, select the correct virtual desktop. In the same row, click **Options** on the right, then choose **Reboot**.
    
5. Confirm the operation via the notification. Rebooting a desktop may take up to 30 minutes.

![Reboot desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Reboot_desktop.png)

## Deleting a virtual desktop

At the end of your analysis, you can delete your virtual desktop, including the external volume and all files saved in it. You cannot undo this action:

1. [Log in](./sd-desktop-login.md) to SD Desktop. On the SD Desktop homepage, click **Go To SD Desktop Management**.

2. At the bottom of the page, under **Available desktops**, select the correct virtual desktop. In the same row, click **Options** on the right, then choose **Delete**.

!!! Note
    Please contact all the project members before deleting a virtual desktop. With this action, you will delete the entire workspace, including all files saved in the virtual desktop or external volume by other project members. 

![Delete desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Delete_desktop.png)


## Your next steps in this guide

* [Accessing virtual desktop](./sd-desktop-access-vm.md)
* [Working with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)


