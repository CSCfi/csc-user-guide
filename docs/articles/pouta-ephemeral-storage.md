#Ephemeral storage

Some Pouta virtual machine flavors have ephemeral storage in addition to a root disk. 
This works as additional storage for the duration of the instance. This storage does not 
get saved when the instance shuts down. This storage does not get saved when you create a 
snapshot of an image. It's especially imporant to note regarding the io.* flavors that 
the storage is based on RAID0 arrays optimized for performance, providing no redundancy whatsoever.

For a detailed explanation of ephemeral storage (and other storage options), you can see storage 
concepts section in the OpenStack user guide.

The ephemeral storage is visible as an additional disk to the virtual machine (usually /dev/vdb). 
You will need to format and mount it first before you can use it:

<pre>sudo mkfs.ext4 /dev/vdb
sudo mount /dev/vdb /mnt</pre>

You will also need to add an entry to the /etc/fstab file on the machine to make sure the disk gets mounted after a reboot:

<pre>sudo umount /mnt/
sudo e2label /dev/vdb EPHEMERAL
sudo echo "LABEL=EPHEMERAL   /mnt   ext4  defaults 0 2 " >> /etc/fstab
sudo mount /mnt
</pre>
The legacy flavors (tiny, mini, small, medium, large, fullnode) also contain an ephemeral disk, 
which is preformatted and mounted automatically.
