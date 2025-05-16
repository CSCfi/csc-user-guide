# Managing volumes

* [Detaching and attaching a volume](#detaching-and-attaching-a-volume)
* [Deleting a volume](#deleting-a-volume)

## Detaching and attaching a volume 

### Detach a volume from your virtual desktop

With the option **Detach volume**, you can easily disconnect a volume from your virtual desktop. The volume and its content will be stored in the same CSC project where it was initially created. You can compare this operation to disconnecting or attaching a hard drive to your laptop. 

1. [Log in](./sd-desktop-login.md) to SD Desktop. Access the correct virtual desktop.

2. Save and close all the files on the volume to prevent data corruption and log out from the virtual desktop.

3. On the SD Desktop homepage, click **Manage volumes**.

4. In the new window choose the correct virtual desktop, and in the same row, on the right side, click **Detach**. Confirm the operation through the notification.

![Detach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)

### Attach a volume to a new virtual desktop

When you want to access the data saved in the detached volume, you can attach it to a new virtual desktop.

1. [Log in](./sd-desktop-login.md) to SD Desktop. On the homepage, click **SD Desktop management**.

2. At the bottom of the page, under Desktop selection choose the necessary options (CSC project, operating system etc.). Follow steps 1-2 in these [instructions](./sd-desktop-create.md).

3. Under **Add External Volume (optional)** click **Choose from existing volumes**. Dropdown will show available volumes stored in the same CSC project. Leave fields **Volume size** and **Volume name** empty. 

4. Click on **Create desktop**.


!!! note
    - A detached volume can not be attached to an existing virtual desktop, only to new virtual desktops during creation phase. 
    - The content of a detached volume can not be accessed or deleted.
    - To delete or access the volume content, attach it to a desktop with the same operating system during the desktop creation phase. 
    - Volumes can not be moved or transferred between CSC projects for security reasons.

![Attach volume.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Attach_volume.png)
