---
hide:
  - toc
---


# Importing data in your virtual desktop

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/hsUQSrNpaf8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Prerequisites
* [Create virtual desktop](sd-desktop-create.md)
* [Access virtual desktop](sd-desktop-access-vm.md)

Once a virtual desktop is created, each CSC project member can access it through their browser. The virtual desktop is isolated from the internet, so data access must be done through the Data Gateway application. This application allows you to import data from SD Connect or SD Apply. Imported data is saved on the virtual desktop’s external volume for secure analysis.

## Additional information

* **What is an external volume?** Your virtual desktop’s local storage is limited, so it’s recommended to save large data files and collaborative work on the external volume. This volume acts like an external hard drive that can be detached and reattached to different desktops, allowing project members to share and edit files stored there.
* **Adding the external volume:** the external volume can only be added when creating a [new virtual desktop](../sensitive-data/sd-desktop-create.md)
* **Additional volume space:** if you need additional volume space (more than 200 GB), you can request it by writing to CSC Service Desk, (subject: SD Desktop), **please be aware that volume extensions are only possible before any data has been added to the volume**.


## Step by step

### 1. Access data via the Data Gateway application

* [Access](sd-desktop-access-vm.md) your virtual desktop.
* Launch **Data Gateway** by clicking icon on the left side of desktop.
![Launch Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway1.png)

* Select:
    * **SD Connect:** This option is for accessing data you’ve uploaded directly to SD Connect. Enter your CSC username and password (note that copy-paste is disabled for security, so you need to type credentials manually).
    * **SD Apply:** This option is accessible only if the data controller has granted you permission.
    * Click **Login** and then **Continue**.

![Gateway login](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway2.png)


* In the next window click **Continue**. Data Gateway establishes a secure connection between your virtual desktop and your data, and creates **Projects** folder on your virtual desktop (and accessible from the terminal).

![Gateway connection](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess1.png)


* In the next window click **Open folder** to view all files stored in SD Connect or SD Apply. Files are available in read-only mode for secure access. To view them, right-click the file and select the desired application to open it.

!!! Note
    In SD Desktop, **you can access only encrypted files.** Accessing unencrypted data or files encrypted only with your public encryption key will result in an error.

![Gateway open folder](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess2.png)

### 2. Import a copy of the files to your virtual desktop's volume

Keep **Data Gateway** open and click **Open folder**.

1. Select and copy the files or folders from the **Projects** folder.
2. Open **Volume** by clicking icon on the left side of desktop.
3. Paste files or folders into **Volume**. Files or folders will automatically decrypt during the copy process and become available for analysis.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess3.png)


### 3. Set permissions for shared access

After copying files to volume, adjust permissions for folders and files to enable access for other project members. By default, permissions are limited to your access only (orange lock icon).

1. Right-click the folder copied to **Volume** and select **Properties** to adjust folder permissions.
    * Open the **Permissions** tab.
    * Set permissions to Create and Delete Files so they remain accessible when the volume is reattached to a different virtual desktop.
        1. Owner -> Access -> Select “Create and delete files”.
        2. Others -> Access -> Select “Create and delete files”.
        3. Close the permission tab (top left corner).
        4. The orange lock icon will no longer be visible next to the folder and can now be edited by all project members.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions1.png)

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions2.png)

2. Next select **Change Permissions for Enclosed Files** to adjust file permisssions inside the folder.
    * Set permissions to:
        1. Owner -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”. 
        2. Others -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        3. Click **Change**.
        4. Close the permission tab (top left corner).
        5. The orange lock icon will no longer be visible next to the files and can now be edited by all project members.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions3.png)



### 4. Close Data Gateway

You can now disconnect the Data Gateway connection if no further data accessor import are needed by clicking **Disconnect and sign out**.

!!! Note
    If more than 10 Data Gateway connection are left open, Data Gateway will stop working. In this case, [contact CSC Service Desk](../../support/contact.md) (subject: SD Desktop).


### 5. Log out

[Log out](sd-desktop-access-vm.md#log-out-from-virtual-desktop) from virtual desktop.

## Your next steps in this guide

* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)


