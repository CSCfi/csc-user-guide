# Ephemeral storage

Some Pouta virtual machine [flavors](vm-flavors-and-billing.md) have an *ephemeral storage* in
addition to the root disk. This works as additional storage for the
duration of the instance. This storage is not saved with the instance.
This storage **does not** get saved when you create a snapshot of an
image. It is not copied along with resizes or migrations. It is
especially important to note regarding the io.\* flavors that the
storage is based on RAID0 arrays optimized for performance, providing
no redundancy whatsoever.

The ephemeral storage is visible as an additional disk to the virtual
machine (usually /dev/vdb). You need to format and mount it before you can use it:

    sudo mkfs.ext4 /dev/vdb
    sudo mkdir /mnt/myephdisk
    sudo mount /dev/vdb /mnt/myephdisk

You also need to add an entry in the /etc/fstab file on the
machine to make sure the disk gets mounted after a reboot:

    sudo umount /mnt/myephdisk/
    sudo e2label /dev/vdb EPHEMERAL
    sudo echo "LABEL=EPHEMERAL   /mnt/myephdisk   ext4  defaults,nofail 0 2 " >> /etc/fstab
    sudo mount /mnt/myephdisk

After the storage has been mounted, you need to change the ownership to be able to read and write data in it.
In the following command, we are assuming the username is cloud-user.

    sudo chown cloud-user:cloud-user /mnt/myephdisk

Please note that some legacy flavors (tiny, mini, small, medium, large, fullnode) also
contained an ephemeral disk which was preformatted and mounted
automatically.
