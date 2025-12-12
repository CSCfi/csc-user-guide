# SD Desktop action required: migrate to a supported version before 2026

All virtual desktops created before 8 September 2023 use an operating system that will no longer be supported in 2026. To keep your data, you must save it to the virtual desktop’s volume and migrate it to a new Ubuntu-based virtual desktop. Below you can find the exact steps needed. 

**NOTE: Correct access permissions must be set before detaching the volume from your virtual desktop to avoid permanent data loss. To assist you, we offer step-by-step online sessions on the dates below. Please confirm your preferred time slot, the process should take about one hour.**

Available time slots:

- Mondays at 12:00: December 15, December 22, January 12, January 19
  
- Thursdays at 14:00: December 11, December 18, January 15


# Moving volume to a new virtual desktop: step by step




## Step 1: Login to SD Desktop and second verification step
    
- Go to login page: https://sd-desktop.csc.fi
  
- Log in with MyCSC-credentials or Haka. Enter your username and password.
  
- You need to verify your identity with a second verification step (i.e. Multi-factor Authentication, MFA). Enter the verification code provided via your MFA mobile application (e.g. Google Authenticator) from your organisation via HAKA or the one provided by CSC when using CSC usarname and passwrod (more informations available [here](../../accounts/mfa.md#multi-factor-authentication-mfa-guide). 

- Press Continue


## Step 2: access your virtual desktop

1. All your virtual desktops are listed at the home page under **All connections**.

2. Select project (e.g. `project_NNNNN`) and click **plus icon**.
  
3.  Now you can see all desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name.

!!! note
    If you encouter a black screen, your veitual desktop might be paused. To resume it, on the SD Desktop homepage, click **Go To SD Desktop Management**.

4. At the bottom of the page, under **Available desktops**, select the correct virtual desktop. In the same row, click **Options** on the right, then choose **Resume**.

!!! note
    Resuming a paused desktop is only possible for active CSC projects with available Cloud Billing Units.

![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

![Resume desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Resume_desktop.png)


## Step 3: save all the necessary data on the desktop volume

* **What is an external volume?** This volume acts like an external hard drive that can be detached and reattached to different desktops, allowing project members to share and edit files stored there.

1. Open **Volume** by clicking icon on the left side of desktop.

2. Paste files or folders into **Volume**.
  
![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess3.png)



## Step 4: Set permissions for shared access

Adjust permissions for folders and files to enable access for other project members. By default, permissions are limited to your access only. Permissions for all other folders and files must be adjusted by the original user who saved them on the volume to enable access for other project members. 

1. Right-click the folder copied to **Volume** and select **Properties** to adjust folder permissions.
    * Open the **Permissions** tab.
    * Set permissions to Create and Delete Files so they remain accessible when the volume is reattached to a different virtual desktop.
        1. Owner -> Access -> Select “Create and delete files”.
        2. Group -> Access -> Select “Create and delete files”.
        3. Others -> Access -> Select “Create and delete files”.
        4. Close the permission tab (top left corner).
        5. The orange lock icon will no longer be visible next to the folder and can now be edited by all project members.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions1.png)

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions2.png)

2. Next select **Change Permissions for Enclosed Files** to adjust file permisssions inside the folder.
    * Set permissions to:
        1. Owner -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        2. Group -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        3. Others -> Files -> Select “Read and write”. Folders -> Select “Create and delete files”.
        4. Click **Change**.
        5. Close the permission tab (top left corner).
        6. The orange lock icon will no longer be visible next to the files and can now be edited by all project members.
        7. Note that if you open the enclosed file permission settings again, it looks like the settings haven't changed even though the permissions have been set correctly.

3. You can now log out from the virtual desktop and return to the service main page.

[Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions3.png)


## Step 5: detach the volume

- On the SD Desktop service homepage, click **SD Desktop management**.

- At the bottom of the page, under **Available desktops** choose the correct virtual desktop, and in the same row, on the right side, click **Detach volume**.

!![Detach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)


### Attach the volume to a new virtaul desktop with Linux Ubuntu22 operating systhem

You can attach the volume  to a new virtual desktop by:

1. On the service homepage, click **SD Desktop management**.

2. Selection all the necessary options: CSC project number, Operating systehm: Linus Ubuntu22, name, virtual desktop option. 

3. Under **Add External Volume (optional)** click **Choose from existing volumes**. Dropdown will show available volumes stored in the same CSC project. Leave fields **Volume size** and **Volume name** empty. 

4. Finally, click *Create desktop*. Please be aware that the confirmation notification may take up to 60 seconds to appear. If you are unsure whether the action was successful, please reach out to us at the service desk. We apologize for any inconvenience this may cause.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)



# When the virtual desktop does not have a volume

## Data export via airlock



## Step 1: access your virtual desktop

1. All your virtual desktops are listed at the home page under **All connections**.

2. Select project (e.g. `project_NNNNN`) and click **plus icon**.
  
3.  Now you can see all desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name.

!!! note
    If you encouter a black screen, your veitual desktop might be paused. To resume it, on the SD Desktop homepage, click **Go To SD Desktop Management**.

4. At the bottom of the page, under **Available desktops**, select the correct virtual desktop. In the same row, click **Options** on the right, then choose **Resume**.

!!! note
    Resuming a paused desktop is only possible for active CSC projects with available Cloud Billing Units.

![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

![Resume desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Resume_desktop.png)

## Step 2: update the ailock component

If the virtual desktop has not been used in a long time, the airlcok component used for data export needs to be updated. Infact, Virtual desktops created before August 2025 display an incorrect error that blocks data export via the Data Gateway application and programmatically, even when accessed by the CSC Project Manager. To resolve this issue, a one time workaround is available. 

Log in to your virtual desktop.  Open the terminal (right-click).

- Open the clipboard with the key combination `Ctrl + Alt + Shift` and activate the copy-paste function by selecting Input method → Text input. 
  The Clipboard panel will close automatically after the selection, and the input bar will appear at the bottom of the virtual desktop.

- Copy the following commands into the input bar. They will be visible in the terminal.  
  You can paste them with `Ctrl + C` or by right-clicking.

    ```bash
    mkdir -p /shared-directory/.certs
    ```

    **Press Enter**

    ```bash
    cp $FS_CERTS /shared-directory/.certs/
    ```

    **Press Enter**

    ```bash
    openssl s_client -showcerts -verify 5 -connect aai.sd.csc.fi:443 < /dev/null \
    | awk '/-----BEGIN CERTIFICATE-----/{c++} c==3{print}/-----END CERTIFICATE-----/&&c==3{exit}' \
    >> /shared-directory/.certs/ca.crt
    ```

    **Press Enter**

    ```bash
    echo "export FS_CERTS=/shared-directory/.certs/ca.crt" >> ~/.profile
    ```

    **Press Enter**

- **Log out** from the virtual desktop and try the export again.

## Step 3: encrypt and export files

Ask for support to servicedesk@csc.fi (SD services) for planning this step. 




