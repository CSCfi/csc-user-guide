# How to rescue instances?

Openstack offers a rescue mode to recover VMs. It is a command that allows for a different image to boot a VM. This can be used when the virtual machine fails to boot due to a kernel panic, full disk, or when you simply lost access to the private key. By allowing you to boot from a different image, you will be able to mount and edit the files on your current disk and fix the problem.

## Symptoms

### Kernel Panic

Check your instance Console Log (web UI: **Instances** > `<your instance>` > **Log**)

```sh
[    1.041853] Loading compiled-in X.509 certificates
[    1.043433] Loaded X.509 cert 'CentOS Linux kpatch signing key:ea0413152cde1d98ebdca3fe6f0230904c9ef717'
[    1.046556] Loaded X.509 cert 'CentOS Linux Driver update signing key:7f421ee0ab69461574bb358861dbe77762a4201b'
[    1.050310] Loaded X.509 cert 'CentOS Linux kernel signing key:d4115f110055db56c8d605ab752173cfb1ac54d8'
[    1.053448] registered taskstats version 1
[    1.055861] Key type trusted registered
[    1.057771] Key type encrypted registered
[    1.059249] IMA: No TPM chip found, activating TPM-bypass! (rc=-19)
[    1.061680]   Magic number: 14:548:18
[    1.063246]  ep_81: hash matches
[    1.064844] rtc_cmos 00:00: setting system clock to 2018-08-23 08:02:54 UTC(1535011374)
[    1.067954] md: Waiting for all devices to be available before autodetect
[    1.069982] md: If you don't use raid, use raid=noautodetect
[    1.072041] md: Autodetecting RAID arrays.
[    1.073689] md: autorun ...
[    1.074976] md: ... autorun DONE.
[    1.076358] List of all partitions:
[    1.077771] No filesystem could mount root, tried: 
[    1.079600] Kernel panic - not syncing: VFS: Unable to mount root fs onunknown-block(0,0)
[    1.082286] CPU: 1 PID: 1 Comm: swapper/0 Not tainted 3.10.0-862.11.6.el7.x86_64 #1
[    1.085033] Hardware name: Fedora Project OpenStack Nova, BIOS 0.5.1 01/01/2011
[    1.087639] Call Trace:
[    1.088800]  [<ffffffff871135d4>] dump_stack+0x19/0x1b
[    1.090453]  [<ffffffff8710d11f>] panic+0xe8/0x21f
[    1.091982]  [<ffffffff8776c761>] mount_block_root+0x291/0x2a0
[    1.093704]  [<ffffffff8776c7c3>] mount_root+0x53/0x56
[    1.095394]  [<ffffffff8776c902>] prepare_namespace+0x13c/0x174
[    1.097281]  [<ffffffff8776c3df>] kernel_init_freeable+0x1f8/0x21f
[    1.099244]  [<ffffffff8776bb1f>] ? initcall_blacklist+0xb0/0xb0
[    1.101131]  [<ffffffff87101bc0>] ? rest_init+0x80/0x80
[    1.102813]  [<ffffffff87101bce>] kernel_init+0xe/0xf0
[    1.104497]  [<ffffffff871255f7>] ret_from_fork_nospec_begin+0x21/0x21
[    1.106367]  [<ffffffff87101bc0>] ? rest_init+0x80/0x80
[    1.107997] Kernel Offset: 0x5a00000 from 0xffffffff81000000 (relocation range:0xffffffff80000000-0xffffffffbfffffff)
```

The log says that the instance couldn't boot because it can't find root "Kernel panic - not syncing: VFS: Unable to mount root fs onunknown-block(0,0)". The fix is to use (some) previous, working kernel. Since you can't boot the server, you have to make the fix to the Volume (boot files) by using another instance.

### Access denied

The problem can be as simple as:

```sh
$ ssh cloud-user@<floating-ip>
cloud-user@<floating-ip>: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

## How to fix the issue, nova rescue

Note that there are always several ways to fix any problem, this FAQ is mainly meant to show one of the ways to fix these kinds of problems. Also meanwhile you are allowed to edit Grub boot parameters, the root single mode access is disabled by default for security reasons. The procedure to perform a rescue is as follows:

1. You need to have installed the [OpenStack command line tools](../../cloud/pouta/install-client.md). And you have to login, and see [Configure your terminal environment for OpenStack](../../cloud/pouta/install-client.md#configure-your-terminal-environment-for-openstack) for reference.

1. Get the server's ID, and store it in an environment variable called: `INSTANCE_UUID`:

	```sh
	$ openstack server list
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+
	| ID                                   | Name      | Status | Networks                   | Image | Flavor         |
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+
	| 55555566-ffff-4a52-5735-356251902325 | comp1     | ACTIVE | net=192.168.211.211        |       | standard.small |
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+

	```

1. Get the image ID. You can store the ID into an environment variable `IMAGE_UUID`. You should use the same image as your instance: (The ID may vary from the example below)

	```sh
	$ openstack image list
	+--------------------------------------+----------------------+--------+
    | ID                                   | Name                 | Status |
	+--------------------------------------+----------------------+--------+
	| 56b70226-0c52-48c6-973f-3f726b5e7dc0 | CentOS-7             | active |
	| 2d20266d-43f7-499e-b6e6-090b09416b16 | CentOS-7-Cuda        | active |
	| c80adfec-05a8-4c42-8922-4bccdf90df40 | CentOS-8-Stream      | active |
	| 2ca237c5-bd0a-4469-ae9f-20878dd288a9 | Fedora Cloud Base 31 | active |
	| ee19819d-17d5-4f71-ac38-e024d046eb6a | Ubuntu-18.04         | active |
	| 668d235f-e6e4-421d-964c-0016f9560206 | Ubuntu-20.04         | active |
	| aea0bf58-85fb-4f9c-b2ea-ffa6c7a07c02 | Ubuntu-22.04         | active |
	| 3a9aad67-0f9c-4493-b574-17fe28d40afc | cirros               | active |
	+--------------------------------------+----------------------+--------+
	```

1. Shutdown the instance:

	```sh
	openstack server stop $INSTANCE_UUID
	```

1. Check that the VM is stopped:
	
	```sh
	openstack server list
	```

	The Status should be `SHUTOFF`

1. You are now ready to launch the rescue of the instance:

	```sh
	openstack server rescue --image $IMAGE_UUID $INSTANCE_UUID
	```

1. Make sure that the instance is in rescue mode with:

	```sh
	openstack server list
	```

	The Status should be `RESCUE`

## Connecting

### Using ssh 

The rescue image will get the same SSH keys as configured in the VM you are rescuing,
so you should be able to ssh into the instance, using the same user and IP as the normal ones.

```sh
ssh <default-user>@<floating-ip>
```

You will get this warning: `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`. This is what is called the `host keys`, they are stored in the VM's disk, and they change because you are booting using a different disk. Fix it by removing the line of your instance IP address from the file `~/.ssh/known_hosts`. An alternative way is the execution of the following command:

```sh
ssh-keygen -f "~/.ssh/known_hosts" -R "$INSTANCE_IP"
```

### Using Pouta's web console (with Cirros)

In some cases, like when you lose the private SSH key, you will need to use Pouta's web console. For this to work, you need to select the **Cirros** image in the step 3 above.

Login in Pouta's web interface: <https://pouta.csc.fi>. Look for your instance and click in `console`.

![Web console](/img/pouta-web-console.png)

The username and password should be printed in the console text, above the login.

!!! Warning "Cirros"
    The Cirros image is a small Linux distribution image with limited software support and security updates. It should be used only for rescue operations when normal SSH access is not possible.

	Cirros doesn't support XFS filesystem which Almalinux uses.

## Mount the disk 

1. Check what volumes you have. If you don't have any other volumes attached it should look something like this:

	```sh
	$ lsblk
	NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
	vda     253:0    0  3.5G  0 disk
	├─vda1  253:1    0  2.5G  0 part /
	├─vda14 253:14   0    4M  0 part
	├─vda15 253:15   0  106M  0 part
	└─vda16 259:0    0  913M  0 part
	vdb     253:16   0   80G  0 disk
	├─vdb1  253:17   0   79G  0 part
	├─vdb14 253:30   0    4M  0 part
	├─vdb15 253:31   0  106M  0 part /boot/efi
	└─vdb16 259:1    0  913M  0 part /boot
	```

1. Now you want to mount `vdb1` to `/tmp/mnt` and go to that directory:

	```sh
	$ sudo mkdir -p /tmp/mnt
	$ sudo mount /dev/vdb1 /tmp/mnt/
	```

## Edit bootloader (Grub)

Sometimes, the problem can comes from a faulty kernel. You can edit the Grub to display the boot menu when you start the machine.

1. Locate the `boot` partition in the `lsblk` command ran previously


1. In this example, the `boot` partition is `/dev/vdb16`. Run these commands to mount the different volumes needed: (`root` volume is already mounted. See section [above](#mount-the-disk))

	```sh
	sudo mount /dev/vdb16 /tmp/mnt/boot
	sudo mount --bind /dev /tmp/mnt/dev
	sudo mount --bind /sys /tmp/mnt/sys
	sudo mount --bind /proc /tmp/mnt/proc
	```

1. Now, we'll edit the grub. The files to edit are slightly different on `Almalinux` and `Ubuntu`:

	#### Almalinux

	```sh
	sudo vi /tmp/mnt/etc/default/grub
	```

	Change `GRUB_TIMEOUT` to `15` (for example). Save and exit.

	#### Ubuntu

	```sh
	sudo vi /tmp/mnt/etc/default/grub.d/50-cloudimg-settings.cfg
	```

	Change `GRUB_TIMEOUT` to `15` (for example). Save and exit.

	```sh
	sudo vi /tmp/mnt/etc/default/grub
	```

	Change `GRUB_TIMEOUT_STYLE` to `menu`. Save and exit.

1. Now, it's time to update the grub with our modifications. Run these commands:

	#### Almalinux

	```sh
	sudo chroot /tmp/mnt
	sudo grub2-mkconfig -o /boot/grub2/grub.cfg
	```

	#### Ubuntu

	```sh
	sudo chroot /tmp/mnt
	update-grub
	```

Now, you can exit the VM and unrescue it by following the procedure [here](#get-out-of-rescue)

When the VM boots, you will see the boot menu and you will be able to choose a different kernel.

## Use `chroot` to change the `/` folder

In case that your instance has issues due to some broken packages or drivers, then you can switch to your original and fix the problems using the following commands:

```sh
$ sudo mv /tmp/mnt/etc/resolv.conf{,.bak}
$ sudo cp /etc/resolv.conf /tmp/mnt/etc/resolv.conf
$ sudo chroot /tmp/mnt
```

The `chroot` has now changed your root folder `/` to `/tmp/mnt/` (your VM's disk partition). And can do any fix or change like uninstalling or reinstalling a package. 

## Get out of rescue

1. Log out from the instances and `unrescue` the instance:

	```sh
	openstack server unrescue $INSTANCE_UUID
	```

1. It would be a good idea to verify that a restart works after the kernel reinstallation:

	```sh
	ssh <default-user>@<floating-ip> reboot
	```

    wait to boot and ssh to it again:

	```sh
	ssh <default-user>@<floating-ip>
	```

    It should work as before the incident happened.


## If your instance boot from a bootable volume

If you are in this case:

```
$ openstack server list
+--------------------------------------+-------------------+--------+------------------------------------------------+--------------------------+-----------------+
| ID                                   | Name              | Status | Networks                                       | Image                    | Flavor          |
+--------------------------------------+-------------------+--------+------------------------------------------------+--------------------------+-----------------+
| 8bbffd1b-99b2-494a-9501-890db20fc2a7 | machine           | ACTIVE | project_200xxxx=192.168.1.0, 123.45.67.89      | N/A (booted from volume) | standard.small  |
```

You can boot a new machine and attach the volume to edit the files.


!!! Warning  
    Before deleting the machine, be sure that the volume won't be deleted automatically. You can check this by running this command:

	```sh
	$ openstack server show $INSTANCE_UUID | grep 'volumes_attached'

      volumes_attached   | delete_on_termination='False', id='6183d89e-59ac-4b25-b2d5-ef802fd5ef82'
	```

1. Delete the machine that boots from the volume

    ```sh
    $ openstack server delete $INSTANCE_UUID
    ```

1. Create a new machine (boot from an image) and attach the volume

1. Associate a Floating IP and connect to it

1. SSH to the newly created machine and identify the volume. vdb1 is likely the partition you're looking for.

    ```sh
    $ lsblk

    NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
    vda     253:0    0   80G  0 disk
    ├─vda1  253:1    0   79G  0 part /
    ├─vda14 253:14   0    4M  0 part
    ├─vda15 253:15   0  106M  0 part /boot/efi
    └─vda16 259:0    0  913M  0 part /boot
    vdb     253:16   0   20G  0 disk
    ├─vdb1  253:17   0   19G  0 part
    ├─vdb14 253:30   0    4M  0 part
    ├─vdb15 253:31   0  106M  0 part
    └─vdb16 259:1    0  913M  0 part
    ```

1. Create a mount point and mount the partition
   
	```sh
	$ sudo mkdir -p /tmp/mnt
	$ sudo mount /dev/vdb1 /tmp/mnt/
	```

1. You can now edit the files you need in `/tmp/mnt`

Once you're done, you can simply shutdown the vm, detach the volume and start a new machine with the bootable volume.
