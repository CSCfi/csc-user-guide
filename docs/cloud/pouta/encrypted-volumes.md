# Encrypted persistent volumes

This article explains how to use an encrypted persistent volume in Pouta.
The volume is encrypted inside the virtual machine (VM) using LUKS
(Linux Unified Key Setup), ensuring that data stored on the volume
remains encrypted at rest. Only users with the encryption passphrase can
access the volume's contents. The volume is encrypted and decrypted inside the virtual machine using
LUKS.

!!! info
    If you are handling sensitive data, consider the
    [Sensitive Data services](../../data/sensitive-data/index.md) or [ePouta](index.md#accessing-the-pouta-services),
    which are designed for that purpose.

## Prerequisites
 
- A running Pouta VM. See
  [Creating a virtual machine](launch-vm-from-web-gui.md#launching-a-virtual-machine).
- A persistent volume attached to the VM. See
  [Creating and attaching a volume in the Pouta web interface](persistent-volumes.md#creating-and-attaching-a-volume-in-the-pouta-web-interface).
- The `cryptsetup` package.

## Identifying the new device
 
After attaching the volume, log in to the VM (Virtual Machine) via SSH
(Secure SHell) and list the block devices:
 
```
lsblk
```
 
The root disk is `/dev/vda`. The newly attached volume appears as the
next free device, typically `/dev/vdb`. Confirm it has the expected size
and no filesystem:
 
```
sudo lsblk -f /dev/vdb
```
 
The `FSTYPE` column should be empty. The rest of this article assumes the
device is `/dev/vdb`.

## Installing cryptsetup

The Ubuntu 26.04 LTS image used for testing includes `cryptsetup`
by default. To verify that it is installed, run:

```
cryptsetup --version
```

If `cryptsetup` is not installed, install it using your package manager.

On Ubuntu and Debian:

```
sudo apt update
sudo apt install -y cryptsetup
```

On Rocky Linux and AlmaLinux:
 
```
sudo dnf install -y cryptsetup
```

## Creating the LUKS container
 
Format the volume as a LUKS2 container. This step is performed **only the
first time** the volume is used:
 
```
sudo cryptsetup luksFormat --type luks2 /dev/vdb
```
 
You will be asked to type `YES` in uppercase to confirm and then to enter
a passphrase twice. Choose a strong passphrase and store it in a password
manager.
 
Verify that the container was created:
 
```
sudo cryptsetup luksDump /dev/vdb
```
 
The output shows `Version: 2`, the cipher (`aes-xts-plain64` by default),
and one occupied keyslot.

## Opening the container and creating a filesystem
 
Opening the LUKS container creates a decrypted device at
`/dev/mapper/<name>`:
 
```
sudo cryptsetup luksOpen /dev/vdb securedata
```
 
You will be asked for the passphrase. The name `securedata` is arbitrary;
any name can be used.
 
Create the XFS filesystem on the decrypted device:
 
```
sudo mkfs.xfs /dev/mapper/securedata
```
 
Create a mount point and mount the device:
 
```
sudo mkdir -p /media/securedata
sudo mount /dev/mapper/securedata /media/securedata
```
 
Change the ownership so a normal user can write to the volume. The
example below uses `ubuntu`.

```
sudo chown ubuntu:ubuntu /media/securedata
```
 
Verify the result:
 
```
lsblk -f
```
 
`/dev/vdb` shows `FSTYPE crypto_LUKS` and the `securedata` mapping below
it shows `FSTYPE xfs` mounted at `/media/securedata`.

## Backing up the LUKS header

The LUKS header contains metadata and keyslots required to unlock the
encrypted volume. The keyslots store encrypted versions of the master
encryption key.

If the header is overwritten or corrupted, the data on the volume
becomes permanently unrecoverable, even if the correct passphrase is
known.

Create a header backup:

```
sudo cryptsetup luksHeaderBackup /dev/vdb \
    --header-backup-file ~/vdb-luks-header.bin

sudo chmod 0400 ~/vdb-luks-header.bin
```

Copy the header backup off the VM (for example, to your workstation
using `scp`). The header backup and the passphrase are both required to
unlock the volume.

## Managing the encrypted volume

### Closing the container

Before shutting down the VM or when you want to make the volume
inaccessible, unmount the filesystem and close the LUKS container:

```
sudo umount /media/securedata
sudo cryptsetup luksClose securedata
```

After this, the device contains only encrypted data and
`/dev/mapper/securedata` no longer exists.

### Opening the container

After a reboot or when the volume is needed again, open and mount it:

```
sudo cryptsetup luksOpen /dev/vdb securedata
sudo mount /dev/mapper/securedata /media/securedata
```

### Checking status

```
sudo cryptsetup status securedata
```

### Detaching the volume

Always close the LUKS container before detaching the volume:

```
sudo umount /media/securedata
sudo cryptsetup luksClose securedata
```

Then detach the volume from VM using [this guide](persistent-volumes.md#creating-and-attaching-a-volume-in-the-pouta-web-interface).

!!! warning
    Detaching a volume while it is still mounted or open can corrupt the
    filesystem.

### Reattaching the volume

The same encrypted volume can be attached to the same or another VM.

After attaching the VM in the same manner as above then follow:

```
lsblk
sudo cryptsetup luksOpen /dev/vdb securedata
sudo mount /dev/mapper/securedata /media/securedata
```

The same passphrase is required, and the data remains unchanged.

!!! info
    The device name is not guaranteed to be `/dev/vdb`. Always verify
    the correct device using `lsblk` before unlocking.

### Managing passphrases
 
LUKS2 supports up to 32 keyslots. Having at least two passphrases is
recommended so that one can be rotated or recovered if forgotten.
 
Add an additional passphrase:
 
```
sudo cryptsetup luksAddKey /dev/vdb
```
 
You will be asked for an existing passphrase and then for the new one.
 
Remove a passphrase:
 
```
sudo cryptsetup luksRemoveKey /dev/vdb
```
 
You will be asked for the passphrase to remove.
 
!!! warning
    Do not remove the last remaining passphrase. The volume becomes
    unrecoverable.
 
List the keyslots in use:
 
```
sudo cryptsetup luksDump /dev/vdb
```

### Snapshots of encrypted volumes

Create snapshots as described in
[volume snapshots](snapshots.md#volume-snapshots).

When a new volume is created from a snapshot, it must be unlocked using
the same passphrase that was valid at the time the snapshot was taken.

### Expanding an encrypted volume

Extend the volume as described in
[expanding size of the attached volume in the Pouta web interface](persistent-volumes.md#expanding-size-of-the-attached-volume-in-the-pouta-web-interface) to a new size.
After increasing the size of a volume, the additional space is not yet available inside the LUKS container or the filesystem.

On the VM, unmount the filesystem and close the encrypted container:
```
sudo umount /media/securedata
sudo cryptsetup luksClose securedata
```

Next, detach and reattach the volume. Verify that `/dev/vdb` reflects the new size:
`lsblk` should show the new size. 

Then reopen the encrypted container, resize the LUKS mapping, remount the filesystem, and grow the XFS filesystem:

```
sudo cryptsetup luksOpen /dev/vdb securedata
sudo cryptsetup resize securedata
sudo mount /dev/mapper/securedata /media/securedata
sudo xfs_growfs /dev/mapper/securedata
```

Verify the new size:
 
```
df -h /media/securedata
```

For more information about expanding a volume, see [expanding size of the attached volume in the Pouta web interface](persistent-volumes.md#expanding-size-of-the-attached-volume-in-the-pouta-web-interface).
