[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Managing volumes


## On this page:

* [Introduction](#attaching-or-detaching-a-volume)
* [Attaching a volume](#attach-a-volume-to-a-virtual-desktop)
* [Setting correct permissions and detaching a volume](#detach-a-volume-from-a-virtual-desktop)
* [Deleting a volume](#deleting-a-volume)

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    These options are available only on virtual desktops created after February 2, 2023. Please [contact service desk](../../support/contact.md) if you are working with older desktops. Multiple volumes can be attached to a virtual desktop only if the desktop was created after September 28, 2026. A single volume cannot be attached to multiple virtual desktops.
</div>

___

## Attaching or detaching a volume 

![Detach and attach volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Move_volume.png){ style="float: right; margin: 0 3em 3em 3em; width: 35%;" }

When you want to save, access or delete the data in a volume, you need to [attach](#attach-a-volume-to-a-virtual-desktop) it to a virtual desktop that uses same operating system as the volume. This is similar to connecting a USB stick to your laptop.

[Detaching](#detach-a-volume-from-a-virtual-desktop) a volume can be compared to disconnecting a USB stick from your laptop. The volume and its content will remain stored in the same CSC project where it was originally created. The content of a detached volume can not be accessed or deleted, you need to attach it to a virtual desktop first.


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    Volumes can not be transferred between CSC projects for security reasons.

</div>
___

### Attach a volume to a virtual desktop

* [Log in](./sd-desktop-login.md) to SD Desktop. On the SD Desktop homepage, click **Manage volumes** on the right side of the correct desktop.

![Manage volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_ManageVolumes.png)

#### In Manage volumes window

1. You will see a list of volumes that are available to be attached and/or are attached to the desktop. Click **Attach** on the right side of the volume you want to attach to the desktop. 
2. Close the window when you are ready.

![Attach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AttachVolume.png)

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

    If you haven't **SD Tools installer** already installed on your virtual desktop, follow these [instructions](sd-desktop-software.md#21-install-sd-software-installer).

    1. Keep the **Data Gateway** connection open or launch Data Gateway:
        - Select **SD Connect**.
        - Click **Continue**. 
        - In the next view you are asked to choose a folder for accessible files. Check that **Projects** folder is selected. 
        - Click **Continue**.
    2. **Launch SD Software Installer** by clicking the icon on your virtual desktop. The application will open and you can see the software available. 
    3. Install **CSC Tools** by clicking corresponding button. Wait for confirmation.

        ![Launch SD Installer](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CSC-tools2.png)

    4. Open terminal from to left side of the desktop. Type in `pre-volume-detach`. This command fixes the access permissions. 

        ![Install CSC Tools](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CSC-tools3.png)

    6. Next, the command tells if there are other project members who should run this command as well. You should inform them if this happens. 
    7. You are then asked whether you want to make a backup copy of your home directory to the volume, allowing you to import its contents to the new virtual machine. Type y or n (Yes/No).
    8. Next, the command asks whether you want to make a backup copy of your shared directory, which contains software installations. Type y or n (Yes/No). 




??? default "Method 2: Set access permissions manually"

    By default, permissions are limited to your access only (orange lock icon).

    1. Right-click the folder and select **Properties**.
        ![Select properties](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Permissions1.png)

    2. Open the **Permissions** tab.
        ![Select permissions tab](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Permissions2.png)

    3. Set permissions to **Create and Delete Files**:
       
        * Owner -> Access -> Select “Create and delete files”.
        * Group -> Access -> Select “Create and delete files”.
        * Others -> Access -> Select “Create and delete files”.
            
        ![Set folder permissions](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Permissions3.png)

    * Next select **Change Permissions for Enclosed Files** button to adjust file permisssions inside the folder.
    * Set permissions to **Create and Delete files**:

        * Owner -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        * Group -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        * Others -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.

        ![Set file permissions](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Permissions4.png)

    6. Click **Change**.
    7. Close the permission tab (top right corner).
    
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


