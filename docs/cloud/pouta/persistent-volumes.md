# Persistent volumes

This article describes one of the options to store data in Pouta which
survive turning off the virtual machine.

Persistent volumes, as the name says, remain even when instances are
removed. They  an be  attached to  or detached  from virtual machines
while they are running.

## Creating and attaching volumes in the Pouta web interface

Persistent volumes can be created using either the web interface or
through the command line interface.

In the web interface, use the **Create volume** button on the
*Volumes* page to create a new volume. You may then give a name and a
size for the volume (1 GB is the minimum). The only mandatory argument
is the size of the volume.

![Create persistent Volmume](/img/create-volume-horizon.png)

Once the volume has been created, it can be attached to a running
virtual machine. One volume can be attached to only one virtual
machine at a time.

To attach a volume, first select the *Volumes* view in the Pouta web
interface. Click the arrow symbol next to the **Edit Volume** button
for the volume you want to attach and select **Manage
attachments**. Select the instance (i.e. virtual machine) you want to
attach the volume to in the **Attach to Instance** selector.

![Attach persistent volume](/img/volume-attach-horizon2.png)

## Using attached volumes

The first time you use a attached volume it needs to be initialized.
**This should ONLY be done the FIRST time you use it**, otherwise you
overwrite all your data on the volume. First determine which device is
your volume.

The following is a simple usage example for creating a filesystem
on a volume and mounting the filesystem automatically after a
reboot. Note that this is a simple example and there are many 
cooler ways to manage your file systems.

Once you have logged in to your virtual machine, you can list the
volumes:

    sudo parted -l

You should be able to identify the volume based on its size. For this
exercise, let us say it is `/dev/vdb`. First, we create a file  
system on it. We are going to
use *xfs* because we know it works well in Pouta:

    sudo mkfs.xfs /dev/vdb

Now you can start using it. For example, to mount it under
`/media/volume`, you first need to make sure that the path exists:

    sudo mkdir -p /media/volume

Then you can mount it:

    sudo mount /dev/vdb /media/volume

Finally, you need to change the ownership to be able to read and write data in it.
In the following command, we are assuming the username is cloud-user.

    sudo chown cloud-user:cloud-user /media/volume

After this step, you should be able to use your volume normally.
Once you are done with your operations and you want to detach the volume, please remember to unmount the volume before detaching it!

    sudo umount /dev/vdb

If you want the volume to be available after rebooting the virtual
machine, you need to add it in the `/etc/fstab` configuration file.
You can use the label you previously created for the partition:

    sudo sh -c 'echo "/dev/vdb     /media/volume    xfs    defaults,nofail    0    2" >> /etc/fstab'

## Subsequent additions

After you attach the volume to another machine, you only need to run:

    mkdir -p /media/volume
    mount /dev/vdb /media/volume

After these commands, in order to allow the user of the virtual machine to read and write data on the disk, you might need to give the ownership of the /media/volume folder to the user.

## Creating and attaching volumes with command line tools

Persistent volumes can also be created and attached using the command
line tools:

```
openstack volume create --description "<description>" --size <size> <name>
```

List existing volumes:

```
openstack volume list
```

List existing virtual machines to find the one to which you
want to attach a volume:

```
openstack server list
```

When a volume's status is "available", you can attach it to a virtual
machine (you can use either names or IDs to refer to the VM and the
volume):

```
openstack server add volume <virtual machine> <volume>
```

!!! note
    A volume can only be attached to one virtual machine at a time.

When you no longer need the volume to be attached, you can detach
it. **Before detaching, remember to unmount the volume's filesystem on
the virtual machine to avoid data loss!**

```
openstack server remove volume <server> <volume>
```

## Transferring volumes between other Pouta projects

Occasionally, you may need to transfer your persistent
volumes between Pouta projects. For example, you may need to transfer
large data sets or bootable volumes to colleagues in another Pouta
project. This can be done using volume transfers. Volume transfers
between projects in Pouta are fast, avoid data duplication and
unnecessary data transfers over the network. Transferring a volume to
another project means that your project will no longer have access to it.
Please note Pouta volume transfer works within the same cloud environment
i.e. you can transfer a volume from one cPouta project to another but
not between a cPouta project and ePouta project or vice versa.

To transfer a volume, you must first make sure its status
is **Available**. You can do so by detaching it from the instance
to which it was initially attached. Once your volume is in the available
status, you can initiate volume transfer either using Pouta Web or
the command line interface.

For the Pouta Web interface, go to the *Volumes* view and click the arrow symbol
next to the **Edit Volume** button of the volume you want to transfer and
select **Create Transfer.** Name this transfer request and
click on **Create Volume Transfer.** You will then get the volume transfer
credentials (transfer ID & authorization key).

![Transfer a volume to another project](/img/pouta-volume-transfer-creation.png)

You need to provide these credentials to your colleague to whom you
want to transfer this volume.

Your colleague can accept this volume transfer in his project by going
to his *Volumes* view of the web interface and clicking the **Accept
Transfer** button. They need to then provide the transfer credentials
you generated in the previous step and **Accept Volume Transfer.**
This will transfer the volume to your colleague's project.

![Accept volume transfer](/img/pouta-accept-volume-transfer.png)

Volume transfers can be also done using the command line tools:

    openstack volume transfer request create <name or UUID of volume to transfer>

The output of this command will have the volume transfer credentials
(transfer ID  & Authorization key), note them down and pass them to your
colleague to whom you want to transfer the volume.

Your colleague can accept the transfer request of this volume:

    openstack volume transfer request accept <transferID> <authKey>
