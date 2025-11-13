[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Importing data in your virtual desktop

## Prerequisites
* [Create virtual desktop](../sensitive-data/sd-desktop-secondary-create.md)
* [Access virtual desktop](../sensitive-data/sd-desktop-secondary-access-vm.md)

Once a virtual desktop is created, each CSC project member can access it through their browser. The virtual desktop is isolated from the internet, so data access must be done through the Data Gateway application. This application allows you to import data from SD Connect or SD Apply. Imported data is saved on the virtual desktop’s external volume for secure analysis.

## Additional information

* **What is an external volume?** Your virtual desktop’s local storage is limited, so it’s recommended to save large data files and collaborative work on the external volume. This volume acts like an external hard drive that can be detached and reattached to different desktops, allowing project members to share and edit files stored there.
* **Adding the external volume:** the external volume can only be added when creating a [new virtual desktop](../sensitive-data/sd-desktop-secondary-create.md)
* **Additional volume space:** if you need additional volume space (more than 200 GB), you can request it by writing to CSC Service Desk, (subject: SD Desktop), **please be aware that volume extensions are only possible before any data has been added to the volume**.


## Step by step

### 1. Access data via the Data Gateway application

* [Access](sd-desktop-secondary-access-vm.md) your virtual desktop.
* Launch **Data Gateway** by clicking icon on the left side of desktop.
* Select **SD Apply:**. This option is accessible only if the data controller has granted you permission.
* Click  **Continue**.

![Launch Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_LaunchGateway1.png)


* In the next window click **Continue**. Data Gateway establishes a secure connection between your virtual desktop and your data, and creates **Projects** folder on your virtual desktop (and accessible from the terminal).

![Gateway connection](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess1.png)


* In the next window click **Open folder** to view all files stored in SD Connect or SD Apply. Files are available in read-only mode for secure access. To view them, right-click the file and select the desired application to open it.

![Gateway open folder](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess2.png)

### 2. Import a copy of the files to your virtual desktop's volume

Keep **Data Gateway** open and click **Open folder**.

1. Select and copy the files or folders from the **Projects** folder.
2. Open **Volume** by clicking icon on the left side of desktop.
3. Paste files or folders into **Volume**. Files or folders will automatically decrypt during the copy process and become available for analysis.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess3.png)


### 3. Set permissions for shared access

After copying files to volume, adjust permissions for folders and files to enable access for other project members. By default, permissions are limited to your access only.

1. Right-click the folder copied to **Volume** and select **Properties** to adjust folder permissions.
    * Open the **Permissions** tab.
    * Set permissions to Create and Delete Files so they remain accessible when the volume is reattached to a different virtual desktop.
        1. Owner -> Access -> Select “Create and delete files”.
        2. Group -> Access -> Select “Create and delete files”.
        3. Others -> Access -> Select “Create and delete files”.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions1.png)

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions2.png)

2. Next select **Change Permissions for Enclosed Files** to adjust file permisssions inside the folder. 
    * Set permissions to:
        1. Owner -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”. 
        2. Group -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        3. Others -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        4. Click **Change**.

Note that if you open the enclosed file permission settings again it looks like the settings haven't changed even though the permissions have been set correctly. 

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions3.png)

Now all project members with access can view and analyze files.

### 4. Close Data Gateway

You can now disconnect the Data Gateway connection by clicking **Disconnect and sign out** if no further data import are needed at this point.

!!! Note
    If more than 10 Data Gateway connection are left open, Data Gateway will stop working. In this case, [contact CSC Service Desk](../../support/contact.md) (subject: SD Desktop).


### 5. Log out

[Log out](sd-desktop-access-vm.md#log-out-from-virtual-desktop) from virtual desktop.


