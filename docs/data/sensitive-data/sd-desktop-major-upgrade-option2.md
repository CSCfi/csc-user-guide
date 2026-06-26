# Option 2: Virtual desktop has a volume and you plan to continue the analysis long-term

Choose this if you want to use the latest features and your analysis will continue long-term. Before you begin, make sure you read the instructions carefully and agree on the approach with your colleagues.

## Step-by-step

* [Step 1: Access desktop](#step-1-access-desktop)
* [Step 2: Save all important data to the volume](#step-2-save-all-important-data-to-the-volume)
* [Step 3: Set permissions for shared access](#step-3-set-permissions-for-shared-access)
* [Step 4: Detach the volume](#step-4-detach-the-volume)
* [Step 5: Create a new virtual desktop](#step-5-create-a-new-virtual-desktop)
* [Step 6: Attach a volume to a virtual desktop](#step-6-attach-a-volume-to-a-virtual-desktop)
* [Step 7: Delete old virtual desktop to save resources](#step-7-delete-old-virtual-desktop-to-save-resources)
* [Step 8: Customising virtual desktop](#step-8-customising-virtual-desktop)


### Step 1: Access desktop

1. [Login](./sd-desktop-login.md) to SD Desktop. Select the correct CSC project in the top left corner. Now you can see all desktops in this project.

2. Make sure the virtual desktop you want to access is running. If it is paused, you need to [unpause](sd-desktop-manage.md#unpausing-a-virtual-desktop) it before you can access it.
  
3. Access virtual desktop by clicking **Access desktop** on right side of the desktop name.

When you open the connection, a virtual desktop will open in your browser in a new window. 

![Access virtual desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM2.png)


### Step 2: Save all important data to the volume

All project members should save data they want to keep to the volume. 

* Open **Volume**.
* Save data to the volume. 

![Open volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Volume.png)

### Step 3: Set permissions for shared access

All project members should set permissions to their own files.

After saving files to volume, adjust permissions for folders and files to enable access for other project members. By default, permissions are limited to your access only (orange lock icon). 

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





### Step 4: Detach the volume

1. Log out of your virtual desktop.

2. Make sure you you have correct CSC project selected in **Select project** dropdown. Then click **Manage volumes** on the right side of the correct desktop.

![Manage volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_ManageVolumes.png)

#### In Manage volumes window

1. You will see a list of volumes. Click **Detach** on the right side of the volume you want to detach from the desktop. 
2. Close the window when you are ready.

![Detach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_DetachVolume.png)

### Step 5: Create a new virtual desktop

1. Make sure you you have correct CSC project selected in **Select project** dropdown.
2. Click **Create desktop**.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop.png)

#### In Create desktop window 

1. **Select a name** for your desktop. Choose a clear and descriptive name - especially if you're working on multiple projects - and make sure it only contains letters or numbers, with no special characters or spaces.
2. **Select operating system.** We recommend to choose **Linux Ubuntu22**. If you want to create a GPU desktop, please contact servicedesk@csc.fi (subject 'SD Desktop') before creation to confirm availability and receive further instructions.
3. **Select a pre-built desktop option** based on your needs. [See options below](#virtual-desktop-options)
4. Write **optional** description or note about the desktop to help your team members understand its purpose and contents.
5. Click **Create**. The window will now close and desktop creation will start.

After returning to the main page, you’ll see a list of your desktops in **Desktops tab**. Creating a desktop can take up to 30 minutes, during which a **Creating** label will appear next to its name. If you try to open it too soon, you’ll get an error message. Once the status changes to **Running**, the desktop is ready to use.

![Create desktop window.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_CreateDesktop2.png)

![Access desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM.png)


### Step 6: Attach a volume to a virtual desktop

When you desktop is running, click **Manage volumes** on the right side of the correct desktop.

![Manage volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_ManageVolumes.png)

#### In Manage volumes window

1. You will see a list of volumes. Click **Attach** on the right side of the volume you want to attach to the desktop. 
2. Close the window when you are ready.

![Attach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AttachVolume.png)

* Access your desktop and verify that all data is accessible.


### Step 7: Delete old virtual desktop to save resources

Users should delete old desktops to save resources.

<div class="grid cards" markdown>

- :material-close-circle:{ .lg .middle } **Warning**
  { .csc-grid-card-error }
    
    You cannot undo this action. Please contact all the project members before deleting a virtual desktop.
    
</div>

1. Log out of your virtual desktop.

2. On the SD Desktop homepage, click **Manage desktop** on the right side of the old desktop.

3. Click **Delete**. 

4. Confirm the operation via the notification. 

![Delete desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_DeleteDesktop.png)


### Step 8: Customising virtual desktop

Continue to customise your desktop and learn about [available software](sd-desktop-software.md).