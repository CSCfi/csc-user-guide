[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Managing virtual desktops and volumes

With the SD Desktop service, you can easily manage your virtual desktops and volumes. 

* [Detaching or attaching a volume](#detaching-or-attaching-a-volume)
* [Pausing or resuming a virtual desktop](#pausing-or-unpausing-a-virtual-desktop)
* [Rebooting a virtual desktop](#rebooting-a-virtual-desktop)
* [Deleting a virtual desktop](#deleting-a-virtual-desktop)
* [Deleting a volume](#deleting-a-volume)

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    These options are available only on virtual desktops created after February 2, 2023. Please [contact service desk](../../support/contact.md) if you are working with older desktops. 

</div>

___

## Detaching or attaching a volume 

![Detach and attach volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Move_volume.png){ style="float: right; margin: 0 3em 3em 3em; width: 40%;" }

Detaching a volume can be compared to disconnecting a USB stick from your laptop. The volume and its content will be stored in the same CSC project where it was initially created. 

When you want to save data to the volume or access the data saved in the volume, you need to attach it to a virtual desktop. You can compare this operation to connecting a USB stick to your laptop.

* The content of a detached volume can not be accessed or deleted. 
* To access or delete content on a volume, you need to attach it to a virtual desktop that uses same operating system as the volume.
* Volumes can not be moved or transferred between CSC projects for security reasons.

___

### Detach a volume from a virtual desktop

#### Step 1: Set access permissions of the volume to read and write

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Ensuring full access to data on a volume across desktops**
  { .csc-grid-card-warning }

    ___
    
    Before detaching a volume, make sure all files and folders have read and write access for all project members. This is due to fact that in the new virtual machine, where the volume will be used afterwards, the mappings between machine specific user ID numbers and user accounts may be different than in the original virtual machine. In practice this means that the user account that owns of the data may change on the way.

</div>


??? default "Method 1: Use CSC Tools to set access permissions"

    1. If you haven't **SD Tools installer** already installed on your virtual desktop, follow these [instructions (Steps 1-2)](./sd-desktop-software.md#step-1-send-a-request).
    2. Launch **SD Tools installer**. Remember that you've to have **Data Gateway** application open for it to work.
    3. Install **CSC Tools** by clicking corresponding button. Wait for confirmation.
    ![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_CSCTools_1.png)

    4. Open terminal from to left side of the desktop. Type in `pre-volume-detach`. This command fixes the access permissions. 
    ![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_CSCTools_2.png)
    6. Next, the command tells if there are other project members who should run this command as well. You should inform them if this happens. 
    7. You are then asked whether you want to make a backup copy of your home directory to the volume, allowing you to import its contents to the new virtual machine. Type y or n (Yes/No).
    8. Next, the command asks whether you want to make a backup copy of your shared directory, which contains software installations. Type y or n (Yes/No). 


??? default "Method 2: Set access permissions manually"

    By default, permissions are limited to your access only (orange lock icon).

    1. Right-click the folder and select **Properties**.
    2. Open the **Permissions** tab.
    3. Set permissions to **Create and Delete Files**:
       
        * Owner -> Access -> Select “Create and delete files”.
        * Group -> Access -> Select “Create and delete files”.
        * Others -> Access -> Select “Create and delete files”.
            
        ![Set folder permissions](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions2.png)

    * Next select **Change Permissions for Enclosed Files** button to adjust file permisssions inside the folder.
    * Set permissions to **Create and Delete files**:

        * Owner -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        * Group -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        * Others -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        * Click **Change**.

        ![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions3.png)

    5. Close the permission tab (top right corner).
    
    The orange lock icon will no longer be visible next to folders and files and they can now be edited by all project members.     
        
    **Note:** If you open the enclosed file permission settings again, it looks like the settings haven't changed even though the permissions have been set correctly.


#### Step 2: Detach a volume from a virtual desktop

1. [Log in](./sd-desktop-login.md) to SD Desktop. On the SD Desktop homepage, click **Access desktop** on the right side of the correct desktop.

2. Save and close all the files on the volume to prevent data corruption and log out from the virtual desktop.

3. On the SD Desktop homepage, click **Manage volumes** on the right side of the correct desktop.

![Manage volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_ManageVolumes.png)

#### In Manage volumes window

1. You will see a list of volumes that are available to be attached and/or are attached to the desktop. Click **Detach** on the right side of the volume you want to detach from the desktop. 
2. Close the window when you are ready.

![Detach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_DetachVolume.png)

___

### Attach a volume to a virtual desktop

* [Log in](./sd-desktop-login.md) to SD Desktop. On the SD Desktop homepage, click **Manage volumes** on the right side of the correct desktop.

![Manage volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_ManageVolumes.png)

#### In Manage volumes window

1. You will see a list of volumes that are available to be attached and/or are attached to the desktop. Click **Attach** on the right side of the volume you want to attach to the desktop. 
2. Close the window when you are ready.

![Attach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AttachVolume.png)

___

## Pausing or unpausing a virtual desktop

Virtual desktops should be paused when not actively used to reduce the use of CSC computing resources and prevent unnecessary consumption of Cloud Billing Units. 

Volumes consume Cloud Billing Units even while the virtual desktop is paused.

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    ---
    
    Pausing is **not intended as a long‑term method for storing data.** CSC cannot guarantee the functionality of desktops paused for extended periods or not updated after service upgrades, including situations where required actions have not been performed.

</div>

### Pausing a virtual desktop


1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop from the homepage.

2. Close all the programs, save or close all the files, and log out from the virtual desktop to prevent data corruption. 

3. On the SD Desktop homepage, click **Manage desktop**.

4. Click **Pause**. 

5. Confirm the operation via the notification. Pausing a desktop may take up to 30 minutes.

![Pause desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_PauseDesktop.png)

### Unpausing a virtual desktop

You can unpause a virtual desktop if the CSC project is active and Cloud Billing Units balance is positive.

1. [Log in](./sd-desktop-login.md) to SD Desktop.

2. On the SD Desktop homepage, click **Manage desktop** on the right side of the correct desktop.

3. Click **Unpause**. 

4. Confirm the operation via the notification.

![Unpause desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_UnpauseDesktop.png)

___

## Restarting a virtual desktop

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


## Deleting a virtual desktop

At the end of your analysis, you can delete entire virtual desktop, and all files saved to it by you or other project members. 

<div class="grid cards" markdown>

- :material-close-circle:{ .lg .middle } **Warning**
  { .csc-grid-card-error }
    
    You cannot undo this action. Please contact all the project members before deleting a virtual desktop. ´
    
</div>

1. [Log in](./sd-desktop-login.md) to SD Desktop.

2. On the SD Desktop homepage, click **Manage desktop** on the right side of the correct desktop.

3. Click **Delete**. 

4. Confirm the operation via the notification. 

![Delete desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_DeleteDesktop.png)

___

## Deleting a volume

At the end of your analysis, you can delete a volume, and all files saved to it by you or other project members. 

<div class="grid cards" markdown>

- :material-close-circle:{ .lg .middle } **Warning**
  { .csc-grid-card-error }

    You cannot undo this action. Please contact all the project members before deleting a volume. 

</div>

1. If the volume is attached to a desktop detach it first. 
2. On the SD Desktop homepage, click **Volumes** tab.
3. Click **Delete** on the right side of the correct volume.
4. Confirm deleting the volume via notification.

![Delete volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_DeleteVolume.png)

___



## Your next steps in this guide

* [Accessing virtual desktop](./sd-desktop-access-vm.md)
* [Working with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)


