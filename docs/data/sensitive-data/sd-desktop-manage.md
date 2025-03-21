---
hide:
  - toc
---


# Managing volumes and virtual desktops

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/rYpuUwm8LhQ" title="Manage virtual desktops in the SD Desktop service" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## SD Desktop management

With the SD Desktop service, you can easily manage volumes and pause, reboot or delete your virtual desktops. Managing desktops happens in **SD Desktop management** page.

* [Detaching and attaching a volume](#detaching-and-attaching-a-volume)
* [Pausing or unpausing a virtual desktop](#pausing-or-unpausing-a-virtual-desktop)
* [Rebooting a virtual desktop](#rebooting-a-virtual-desktop)
* [Deleting a virtual desktop](#deleting-a-virtual-desktop)

!!! Note
    These options are available only on virtual desktops created after February 2, 2023. Please [contact service desk](../../support/contact.md) if you are working with older desktops. 

![Go to SD Desktop Management.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

## Detaching and attaching a volume 

### Detach a volume from your virtual desktop

With the option **Detach volume**, you can easily disconnect a volume from your virtual desktop. The volume and its content will be stored in the same CSC project where it was initially created. You can compare this operation to disconnecting or attaching a hard drive to your laptop. 

1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop on the homepage under **All connections**.

2. Save and close all the files on the volume to prevent data corruption and log out from the virtual desktop.

3. On the homepage, click **SD Desktop management**.

4. At the bottom of the page, under **Available desktops** choose the correct virtual desktop, and in the same row, on the right side, click **Detach volume**.
Confirm the operation through the notification.

![Detach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)

### Attach a volume to a new virtual desktop

When you want to access the data saved in the detached volume, you can attach it to a new virtual desktop.

1. [Log in](./sd-desktop-login.md) to SD Desktop. On the homepage, click **SD Desktop management**.

2. At the bottom of the page, under Desktop selection choose the necessary options (CSC project, operating system etc.). Follow steps 1-2 in these [instructions](./sd-desktop-create.md).

3. Under **Add External Volume (optional)** click **Choose from existing volumes**. Dropdown will show available volumes stored in the same CSC project. Leave fields **Volume size** and **Volume name** empty. 

4. Click on **Create desktop**.


!!! note
    - A detached volume can not be attached to an existing virtual desktop, only to new virtual desktops during creation phase. 
    - The content of a detached volume can not be accessed or deleted.
    - To delete or access the volume content, attach it to a desktop with the same operating system during the desktop creation phase. 
    - Volumes can not be moved or transferred between CSC projects for security reasons.

![Attach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Attach_volume.png)


## Pausing or unpausing a virtual desktop

You can pause a virtual desktop. In this manner, the desktop will stop consuming billing units. 

### Pausing a virtual desktop

1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop on the homepage under **All connections**.

2. Close all the programs, save or close all the files, and log out from the virtual desktop to prevent data corruption. 

3. On the SD Desktop homepage, click **Go To SD Desktop Management**.

4. At the bottom of the page, under **Available desktops** choose the correct virtual desktop, and in the same row, on the right side, click **Pause desktop**. 

5. Confirm the operation via the notification. Pausing a desktop may take up to 30 minutes.

!!! note
    You can't access or detach a volume while a desktop is paused.

![Pause desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Pause_desktop.png)

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


