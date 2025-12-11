# SD Desktop action required: migrate to a supported version before 2026

All virtual desktops created before 8 September 2023 use an operating system that will no longer be supported in 2026. To keep your data, you must save it to the virtual desktop’s volume and migrate it to a new Ubuntu-based virtual desktop. Below you can find the exact steps needed. 

**NOTE: Correct access permissions must be set before detaching the volume from your virtual desktop to avoid permanent data loss. To assist you, we offer step-by-step online sessions on the dates below. Please confirm your preferred time slot, the process should take about one hour.**

Available time slots:

- Mondays at 12:00: December 15, December 22, January 12, January 19
  
- Thursdays at 14:00: December 11, December 18, January 15


# Transfer all necessary files to a new virtual desktop with the Linux Ubuntu operating system by following these steps:


## Step 1: Login to SD Desktop and second verification step
    
- Go to login page: https://sd-desktop.csc.fi
  
- Log in with MyCSC-credentials or Haka. Enter your username and password.
  
- You need to verify your identity with a second verification step (i.e. Multi-factor Authentication, MFA). Enter the verification code provided via your MFA mobile application (e.g. Google Authenticator) from your organisation via HAKA or the one provided by CSC when using CSC usarname and passwrod (more informations available here: https://docs.csc.fi/accounts/mfa/).

- Press Continue


## Step 2: access your virtual desktop

- All your virtual desktops are listed at the home page under **All connections**.

- Select project (e.g. `project_NNNNN`) and click **plus icon**.
  
- Now you can see all desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name.

- Note: if you encouter a black screen, your veitual desktop might be paused. To resume it, on the SD Desktop homepage, click **Go To SD Desktop Management**.

- At the bottom of the page, under **Available desktops**, select the correct virtual desktop. In the same row, click **Options** on the right, then choose **Resume**.

!!! note
    Resuming a paused desktop is only possible for active CSC projects with available Cloud Billing Units.

![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

![Resume desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Resume_desktop.png)


## Step 3: save all the necessary data on the volume

* **What is an external volume?** This volume acts like an external hard drive that can be detached and reattached to different desktops, allowing project members to share and edit files stored there.

- Open **Volume** by clicking icon on the left side of desktop.

- Paste files or folders into **Volume**. 
![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess3.png)

## Step 4: set correct permissions

Before you detach a volume, it is good the set access permissions of files and directories such that all project members have both read and write access to all the data in the volume. This is due to fact that in the new virtual machine, where the volume will be used afterwards, the mappings between machine specific user ID numbers and user accounts may be different than in the original virtual machine. In practice this means that the user account that owns of the data may change on the way.

**You can do this permission set-up with linux command pre-volume-detach that you can take in use by installing CSC Tools with SD tools installer. In addition to fixing the access permissions of the user who is running the command, it checks if there are other users that should run this command too. Further, the command allows you to make a backup copy of your home directory to the volume so that you can import the contents of your home directory to the new virtual machine.**

## STep 4: Set permissions for shared access

After copying files to volume, adjust permissions for folders and files to enable access for other project members. By default, permissions are limited to your access only (orange lock icon).

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

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions3.png)

Note that if you open the enclosed file permission settings again, it looks like the settings haven't changed even though the permissions have been set correctly.

** Log out**

## Step 5: detach the volume

- On the SD Desktop service homepage, click **SD Desktop management**.

- At the bottom of the page, under **Available desktops** choose the correct virtual desktop, and in the same row, on the right side, click **Detach volume**.

![Detach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)


### Detach a volume from your virtual desktop

When you want to access the data saved in the detached volume, you can attach it to a new virtual desktop.

1. [Log in](./sd-desktop-login.md) to SD Desktop. On the homepage, click **SD Desktop management**.

2. At the bottom of the page, under Desktop selection choose the necessary options (CSC project, Linus Ubuntu22 as operating system etc). 

3. Under **Add External Volume (optional)** click **Choose from existing volumes**. Dropdown will show available volumes stored in the same CSC project. Leave fields **Volume size** and **Volume name** empty. 

4. Finally, click *Create desktop*. Please be aware that the confirmation notification may take up to 30 seconds to appear. If you are unsure whether the action was successful, please reach out to us at the service desk. We apologize for any inconvenience this may cause.

![Create desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_CreateButton.png)




** Before february 2024? 23 not possible to detach reattach volule
gateway prbably not working



## Datea Gatewat certificate
source $HOME/.profile
sda-fuse

## Airlock export
intructions


All virtual desktop created before 8.9.2023 are based on the operating systehm that is no longer supported in 2026. For thsi reason, if data stored in the virtual desktopa are still needed, each user needs to save all the dat in their virtual desktop's volume and follow the process before to migrate the volume to a new virtual desktop.

Following the process below and setting correct access premission before detaching the volume is critical for ensuring that there is no dat aloss during the process. 



https://github.com/CSCfi/csc-user-guide/blob/fm-centos/docs/data/sensitive-data/migration-to-ubuntu.md



Your CSC project has two virtual desktops running the CentOS 7 operating system, which will soon no longer be supported:

* Project: 2003139
* Virtual desktop name: EraPermed-1661806495 and project_2003139-1667363501

Please choose one of the following options:

1. If you no longer need it: delete the virtual desktop and all its content permanently by following these steps: https://docs.csc.fi/data/sensitive-data/sd-desktop-secondary-manage/#deleting-a-virtual-desktop or confirm by replying to this email that the virtual desktop does not contain sensitive data and authorize us to delete it.

2. Transfer all necessary files to a new virtual desktop with the Linux Ubuntu operating system by following these steps:

  * Save all files on the volume: https://docs.csc.fi/data/sensitive-data/sd-desktop-secondary-access/#2-import-a-copy-of-the-files-to-your-virtual-desktops-volume
  * Set permissions for all project members: https://docs.csc.fi/data/sensitive-data/sd-desktop-secondary-manage/#before-detaching
  * Detach the volume
  * Create a new Ubuntu virtual desktop and during the creation process add the volume: https://docs.csc.fi/data/sensitive-data/sd-desktop-secondary-create/
  * Delete the old virtual desktop once everything works.

To prevent any data loss, we offer online support sessions with step by step guidance. Please reply to this email with your preferred time slot from the options below:

- Mondays at 12:00: December 15, December 22, January 12, January 19
- Thursdays at 14:00: December 11, December 18, January 15

