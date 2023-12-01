# How to resize an instance or volume in Pouta
## Resize an instance
### Using a snapshot
We might face performance issue with your initial instance and you'd like to run your instance with a bigger flavor?  
It's possible to proceed by taking a snapshot of your instance and then boot the new instance with the new flavor using the snapshot.  
You can find more information about snapshot [here](../../cloud/pouta/snapshots.md) and how to proceed.

### Using the resize functionality 
!!! Warning    
    I/O flavors [cannot be resized](../../cloud/pouta/vm-flavors-and-billing.md#io-flavors_2) to a different family flavors.  
    It's possible to resize from a `standard` flavor *family* to a `hpc` flavor *family*. Nothing will prevent you to do that but it's **highly not recommended!**  
    You may lose data during the process and CSC is not responsible. We recommend to only resize to the flavors of the same *family*

In the **Actions** menu of your instance, choose **Resize** to begin the process:  

![resize-button](img/resize_button.png)

A window will open. Select the new flavor:

![resize-windows](img/resize_window.png)

Click **Resize**

Wait few minutes and during the process, it will ask you to confirm the resize:

!!! error-label
    When your instance is in `Confirm Resize/Migrate` it means that you can connect to your instance to check if everything is working fine because your instance is already converted into the new flavor.  
    In the case that you spot something wrong, you can revert to the previous state with the `Revert Resize/Migrate` button in the drop menu.  
    Be aware that an automatic confirm process will be triggered after three days of pending status `Confirm or Revert Resize/Migrate`

![confirm-resize](img/confirm_resize.png)

After the process finished, you should have your instance with a flavor.


## Resize a volume
!!! Notes  
    You can only extend a volume. Currently, shrink a volume is not supported in Openstack.

Pouta let you create [external volumes](../../cloud/pouta/storage.md). If your initial volume is too small, you can resize it.

!!! Note
    If your volume is attached to your instance, you must detach it to be able to resize

From the Volumes page, in the **Actions** menu, click **Extend Volume**:

![resize-volume](img/resize_volume.png)

A window will open. Enter the new amount of your volume:

![resize-volume-window](img/resize_volume_window.png)

Click **Extend Volume**

You should see the new size of your volume.

You can now attach the new volume back to your instance.
