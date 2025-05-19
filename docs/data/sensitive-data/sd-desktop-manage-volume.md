# Managing volumes

* [Attaching a volume](#attach-a-volume-to-a-virtual-desktop)
* [Detaching a volume](#detach-a-volume-from-a-virtual-desktop)
* [Deleting a volume](#deleting-a-volume)


## Attach a volume to a virtual desktop

When you want to access the data saved in the detached volume, you can attach it to a new virtual desktop.

1. [Log in](./sd-desktop-login.md) to SD Desktop. On the SD Desktop homepage, click **Manage volumes** on the right side of the correct desktop.

2. In the new window you will see volumes that are attached to the desktop and/or are available to be attached.

4. Click **Attach** on the right side of the volume you want to attach to the desktop. 

5. You need to restart your desktop to access the volume. You can restart your desktop via notification or do it later in **Manage desktop** menu if desktop is in use.

![Attach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Attach_volume.png)

## Detach a volume from a virtual desktop

With the option **Detach volume**, you can easily disconnect a volume from your virtual desktop. The volume and its content will be stored in the same CSC project where it was initially created. You can compare this operation to disconnecting or attaching a hard drive to your laptop. 

1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop.

2. Save and close all the files on the volume to prevent data corruption and log out from the virtual desktop.

3. On the SD Desktop homepage, click **Manage volumes** on the right side of the correct desktop.

4. In the new window choose the correct virtual volume, and in the same row, on the right side, click **Detach**. Confirm the operation through the notification.

![Detach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)


!!! note
    - The content of a detached volume can not be accessed or deleted.
    - To delete or access the volume content, attach it to a desktop with the same operating system during the desktop creation phase. 
    - Volumes can not be moved or transferred between CSC projects for security reasons.


