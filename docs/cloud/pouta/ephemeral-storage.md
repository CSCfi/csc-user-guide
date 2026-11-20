# Ephemeral storage

Some Pouta virtual machine [flavors](vm-flavors-and-billing.md) have *ephemeral storage* in
addition to the root disk. This works as additional storage for the duration of the instance.

!!! warning
    Data in ephemeral storage is not preserved when the instance is deleted, when you create a snapshot, or when the instance is resized or migrated.

It is especially important to note that the ephemeral storage on io.\* flavors
(except io.2.\*) is based on RAID0 arrays optimized for performance, providing
no redundancy whatsoever. On io.2.\* flavors, however, the storage is based on
RAID1, which offers more safety against data loss.

The ephemeral storage is visible to the virtual machine as an additional
disk (usually /dev/vdb). Depending on the image and metadata chosen
when creating the virtual machine, the disk might already be formatted
as `vfat` and mounted at `/mnt`. If that is the case and it suits your
needs, you can start using the disk right away.

If you need to format the disk with a different filesystem (or it is
neither formatted nor mounted), you can follow this procedure:

First make sure that the volume is not mounted:

    sudo umount /dev/vdb

and that there is no entry in `/etc/fstab` for this disk:

    cat /etc/fstab

Look for a line containing `/dev/vdb` or `LABEL=EPHEMERAL`,
and comment it out (adding `#` at the beginning of the line).

Now you can continue to format and mount it. We are using the ext4 filesystem in the example below:

    sudo mkfs.ext4 /dev/vdb
    sudo mkdir /mnt/myephdisk
    sudo mount /dev/vdb /mnt/myephdisk

You also need to add an entry in `/etc/fstab` to make sure the disk gets
mounted after a reboot:

    sudo umount /mnt/myephdisk/
    sudo e2label /dev/vdb EPHEMERAL
    sudo bash -c 'echo "LABEL=EPHEMERAL   /mnt/myephdisk   ext4  defaults,nofail 0 2" >> /etc/fstab'
    sudo mount /mnt/myephdisk

After the storage has been mounted, you need to change the ownership to be able to read and write data in it.
In the following command, we assume the username is `cloud-user`.

    sudo chown cloud-user:cloud-user /mnt/myephdisk

Please note that some legacy flavors (tiny, mini, small, medium, large, fullnode) also
had an ephemeral disk that was preformatted and mounted
automatically.
