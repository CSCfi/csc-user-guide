[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Importing data in your virtual desktop

## Prerequisites
* [Create virtual desktop](sd-desktop-create.md)
* [Access virtual desktop](sd-desktop-access-vm.md)

Once a virtual desktop is created, each CSC project member can access it through their web browsers. The virtual desktop is isolated from the internet, so data access must be done through the Data Gateway application. This application allows you to import data from SD Connect or SD Apply. 

<div class="grid cards" markdown>

- :material-close-circle:{ .lg .middle } **Desktop storage limit**
  { .csc-grid-card-error }
    
    Desktops have 80 GB of storage by default. **If you save more than 80 GB of data to your desktop, it becomes unresponsive and you may lose your data**. To avoid this, please create and attach a [**volume**](sd-desktop-create.md#create-volume) to your desktop and save your data there.

</div>



## Step by step

You can import data via Data Gateway application or programmatically.

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Note**
  { .csc-grid-card-warning }

    In SD Desktop, **you can access only encrypted files.** Accessing unencrypted data or files encrypted only with your public encryption key will result in an error.
    
</div>

### 1.1 Import data to your virtual desktop via the Data Gateway application

1. Launch **Data Gateway** by clicking icon on the left side of desktop.
2. Select:
    * **SD Connect:** This option is for accessing data you’ve uploaded directly to SD Connect. 
    * **SD Apply:** This option is accessible only if the data controller has granted you permission.
3. Click **Continue**.

    ![Launch Data Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Import1.png)

4. In the next view you are asked to choose a folder for accessible files. Check that **Projects** folder is selected. 
5. Click **Continue**.

    ![Selet folder](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Import2.png)

6. In the next window click **Open folder**.
7. Now you  can see all files stored in SD Connect or SD Apply. Files are available in read-only mode for secure access. To view them, right-click the file and select the desired application to open it. Locate the buckets/files you want to import.

    ![Open folder](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Import3.png)


8. Open **Volume** from left side menu.


    ![Open volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Import4.png)


9. **Select and copy** the files or buckets from the **Projects** folder.
10. **Paste** files or folders into **Volume**. Files or folders will automatically decrypt during the copy process and become available for analysis.

    ![Copy and paste files](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Import5.png)




### 1.2 Import data to your virtual desktop programmatically

1. 

### 2. Set permissions for shared access

After copying files to volume, adjust permissions for folders and files to enable access for other project members. By default, permissions are limited to your access only (orange lock icon).

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

### 4. Close Data Gateway

You can now disconnect the Data Gateway by clicking **Disconnect and sign out** if you no longer need to access to the data or import new data.

!!! Note
    If more than 10 Data Gateway connection are left open, Data Gateway will stop working. In this case, [contact CSC Service Desk](../../support/contact.md) (subject: SD Desktop).


### 5. Log out

[Log out](sd-desktop-access-vm.md#log-out-from-virtual-desktop) from virtual desktop.

## Your next steps in this guide

* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)


