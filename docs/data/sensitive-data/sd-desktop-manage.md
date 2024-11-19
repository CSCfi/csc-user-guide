# Managing volumes and virtual desktops

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/rYpuUwm8LhQ" title="Manage virtual desktops in the SD Desktop service" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

With the SD Desktop service, you can easily manage volumes and pause, reboot or delete your virtual desktops. Below we illustrate the main available options. 

!!! Note
    These options are available only on virtual desktops created after February 2, 2023. Please [contact service desk](../../support/contact.md) if you are working with older desktops. 

* [Detaching and reattaching a volume](#detaching-and-reattaching-a-volume)
* [Pausing or unpausing a virtual desktop](#pausing-or-unpausing-a-virtual-desktop)
* [Rebooting a virtual desktop](#rebooting-a-virtual-desktop)
* [Deleting a virtual desktop](#deleting-a-virtual-desktop)

## Detaching and reattaching a volume 

### Detach a volume from your virtual desktop

With the option **Detach volume**, you can easily disconnect a volume from your virtual desktop. The volume and its content will be stored in the same CSC project where it was initially created. You can compare this operation to disconnecting or attaching a hard drive to your laptop. 

1. Save and close all the files on the volume to prevent data corruption and log out from the virtual desktop.

2. Login to SD Desktop. On the homepage, click **SD Desktop management**.

3. At the bottom of the page, under **Available desktops** choose the correct virtual desktop, and in the same row, on the right side, click **Detach volume**.
Confirm the operation via notification.

### Reattach a volume to a new virtual desktop

When you want to access the data saved in the detached volume, you can reattach it to a new virtual desktop.

1. Login to SD Desktop. On the homepage, click **SD Desktop management**.

2. At the bottom of the page, under Desktop selection choose the necessary options (CSC project, operating system etc.). Follow steps 1-2 in these [instructions](./sd-desktop-create.md).

3. Under **Add External Volume (optional)** click **Choose from existing volumes**. The user interface will visualize available volumes stored in the same CSC project. Leave fields **Volume size** and **Volume name** empty. 

4. Click on **Create desktop**.


!!! note
    * A detached volume can not be reattached to an existing virtual desktop, only to new virtual desktops during creation phase. 
    - The content of a detached volume can not be accessed or deleted.
    - To delete or access the volume content, attach it to a desktop with the same operating system during the desktop creation phase. 
    -Volumes can not be moved or transferred between CSC projects for security reasons.

[![Desktop-volume](images/desktop/volume.png)](images/desktop/volume.png)

## Pausing or unpausing a virtual desktop

You can pause a virtual desktop. In this manner, the desktop will stop consuming billing units. 

To pause the desktop:

1. Close all the programs, save/close all the files, and log out from the virtual desktop to prevent data corruption.

2. On the SD Desktop homepage, click on _Go To SD Desktop Management_;

3. Here, under _Available desktops_ select the correct virtual desktop, and in the same row, on the right side, click on _Pause desktop_. Note: you can not detach a volume or access a paused desktop. 

4. A message will ask to confirm the operation, which can take up to 30 minutes.

You can unpause the virtual desktop at any time from the same page. Also, in this case, the restart processes can take up to 30 minutes:

1. On the SD Desktop homepage, click on _Go To SD Desktop Management_;

2. Here, under _Available desktops_ select the correct virtual desktop, and in the same row, on the right side, click on _Resume_. 

!!! Note
    Restarting a paused desktop is only possible for active CSC projects with available billing units. 

[![Desktop-volume](images/desktop/pause.png)](images/desktop/pause.png)


## Rebooting a virtual desktop

If your virtual desktop or software becomes unresponsive, you can reboot (restart) it. After the reboot, all files and software saved on the virtual desktop will remain accessible.

!!! Note
    If the Data Gateway application becomes unresponsive due to old sessions running in the background, there's no need to restart your desktop. Instead, you can utilize the terminal to identify and halt the process. For assistance, please [contact CSC Service Desk](../../support/contact.md), subject "Sensitive data."

To reboot a desktop:

1. Close all programs and ensure you save/close any files to prevent data corruption.
    
2. Go to the SD Desktop homepage and select "Go To SD Desktop Management."
    
3. Scroll to the end of the page. Here, under "Available desktops," choose the relevant virtual desktop. On the right side of the same row, click "Options" and then select "Reboot."
    
4. Confirm the operation when prompted. The process may take up to 30 minutes.



## Deleting a virtual desktop

At the end of your analysis, you can delete your virtual desktop, including the external volume and all files saved in it. You cannot undo this action:

1. On SD Desktop Homepage, click on _Go to SD Desktop Management page_.

2. Under _Available desktops_ select the correct virtual desktop.

3. On the same row, on the right side, click on _Options_ and on _Delete_.

!!! Note
    Please contact all the project members before deleting a virtual desktop. With this action, you will delete the entire workspace, including all files saved in the virtual desktop or external volume by other project members. 



 [![Desktop-delete](images/desktop/desktop-deleting.png)](images/desktop/desktop-deleting.png)
