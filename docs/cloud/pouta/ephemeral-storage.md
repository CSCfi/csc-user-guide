# Ephemeral storage

Some Pouta virtual machine [flavors](vm-flavors-and-billing.md) have an *ephemeral storage* in
addition to the root disk. This works as additional storage for the
duration of the instance. This storage is not saved with the instance.
This storage **does not** get saved when you create a snapshot of an
image. It is not copied along with resizes or migrations. It is
especially important to note regarding the io.\* flavors that the
storage is based on RAID0 arrays optimized for performance, providing
no redundancy whatsoever. Regarding io.2.\* flavors, the storage is based on RAID1, offering
more safety, avoiding the loss of files.

The ephemeral storage is visible as an additional disk to the virtual
machine (usually /dev/vdb). Depending on the image and metadata chosen
when creating the virtual machine, the disk might be already formated
as `vfat` and mounted in `/mnt`. If this is case and this fits your use
case, you can just start to use the disk.

If you need to format the disk with a different filesystem (or it is not
formatted nor mounted), you can follow this procedure:

First make sure that the volume is not mounted:

    sudo umount /dev/vdb

and that there is no entry in `/etc/fstab` for this disk:

    cat /etc/fstab

Look for a line containing `/dev/vdb` or `LABEL=EPHEMERAL`,
and comment it out (adding `#` at the beginning of the line).

Now you can continue to format and mount it. We are using ext4 in the example below:

    sudo mkfs.ext4 /dev/vdb
    sudo mkdir /mnt/myephdisk
    sudo mount /dev/vdb /mnt/myephdisk

You also need to add an entry in the /etc/fstab file on the
machine to make sure the disk gets mounted after a reboot:

    sudo umount /mnt/myephdisk/
    sudo e2label /dev/vdb EPHEMERAL
    sudo bash -c 'echo "LABEL=EPHEMERAL   /mnt/myephdisk   ext4  defaults,nofail 0 2 " >> /etc/fstab'
    sudo mount /mnt/myephdisk

After the storage has been mounted, you need to change the ownership to be able to read and write data in it.
In the following command, we are assuming the username is cloud-user.

    sudo chown cloud-user:cloud-user /mnt/myephdisk

Please note that some legacy flavors (tiny, mini, small, medium, large, fullnode) also
contained an ephemeral disk which was preformatted and mounted
automatically.
