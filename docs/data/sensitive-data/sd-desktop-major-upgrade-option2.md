# Option 2: Virtual desktop has a volume and you plan to continue the analysis long-term

Choose this if you want to use the latest features and your analysis will continue long-term. Before you begin, make sure you read the instructions carefully and agree on the approach with your colleagues.

## Step-by-step

### Step 1: Save all important data to the volume

All project members should save data they want to keep to the volume. 

* Log in to SD Desktop.
* Access the correct desktop.
* Open **Volume**.
* Save data to the volume. 

### Step 2: Set permissions for shared access

After saving files to volume, adjust permissions for folders and files to enable access for other project members. By default, permissions are limited to your access only (orange lock icon).

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


### Step 3: Detach the volume

1. Log out of your virtual desktop.

2. Make sure you you have correct CSC project selected in **Select project** dropdown. Then click **Manage volumes** on the right side of the correct desktop.

![Manage volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_ManageVolumes.png)

#### In Manage volumes window

1. You will see a list of volumes. Click **Detach** on the right side of the volume you want to detach from the desktop. 
2. Close the window when you are ready.

![Detach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_DetachVolume.png)

### Step 4: Create a new virtual desktop

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


### Step 5: Attach a volume to a virtual desktop

*  When you desktop is running, click **Manage volumes** on the right side of the correct desktop.

![Manage volumes.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_ManageVolumes.png)

#### In Manage volumes window

1. You will see a list of volumes. Click **Attach** on the right side of the volume you want to attach to the desktop. 
2. Close the window when you are ready.

![Attach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AttachVolume.png)

* Access your desktop and verify that all data is accessible.

### Step 6: Add software provided by CSC via SD Software Installer

![SD Software Installer](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD_Installer.png){ style="float: right; margin: 0 3em 3em 3em; width: 40%;" }

The SD Software Installer is a CSC‑provided tool that makes it easy to install selected, commonly used [**software**](#software-available-via-sd-software-installer) on SD Desktop, such as RStudio 4.5.1, Whisper, VS Code, and GATK.

You can’t add your own software to the Software Installer, but you can request new tools by [contacting CSC Service Desk](../../support/contact.md) (subject: SD Desktop). 

To install and use the application, please follow the step-by-step tutorial below.  
    
___

#### Step 1: Send a request to CSC Service Desk

1. Log in to the [SD Connect service](https://sd-connect.csc.fi). 
    * If you are using SD Connect for the first time, [**upload**](sd-connect-upload.md) a small test file to any bucket (required due to a current technical issue).
2. On the homepage, click **Copy Share ID** next to the project selection menu to copy your project’s Share ID (a 32‑character code, example: 71bbe38a3cd398b48b1f2582dc00297p).
3. Email the CSC Service Desk with the subject “SD Desktop”, requesting access to the Software Installer and including the project Share ID.
4. Once the Service Desk confirms access, move to step 2 below.

![(Share ID)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareID.png)

 ____

#### Step 2: Install and use SD Software Installer 

1. Log in to [SD Desktop service](https://sd-desktop.csc.fi) and access your virtual desktop. Launch **Data Gateway **from navigation on the left side of the screen.
2. Select **SD Connect**.
3. Click **Continue**. 

    ![Installing SD Software Installer - Login](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_SD_Installer1.png)

4. In the next view you are asked to choose a folder for accessible files. Check that **Projects** folder is selected. 
5. Click **Continue**.

    ![Installing SD Software Installer - Choose folder](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_SD_Installer2.png)

6. In the next view click **Open folder**. This opens file browser and you will see folder **Projects**.
7. Navigate to `Projects/SD-Connect/your-project-name`. Locate folder `tools-for-sd-desktop` and open it. 

    ![Installing SD Software Installer - Open Projects folder](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_SD_Installer3.png)


8. **Copy-paste** or **drag-and-drop** file `sd-installer-ubuntu24.desktop` to your desktop. **Right-click** on the `sd-installer-ubuntu24.desktop` icon on your virtual desktop.
9. Select **Allow Launching**.
10. Application is now ready to be used. See [**instructions**](#22-use-sd-software-installer)

    ![Installing SD Software Installer - Install and launch](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_SD_Installer4.png)



### Step 6: Delete old virtual desktop to save resources

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