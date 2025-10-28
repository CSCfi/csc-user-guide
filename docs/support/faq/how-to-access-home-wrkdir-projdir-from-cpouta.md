# How to access directories in Puhti and Mahti from cPouta?

The storage environments of the CSC computing servers (Puhti and Mahti) are not
directly accessible to cPouta because the HPC systems' network is separated
from cPouta for security and performance reasons.

Normally, the recommended way to move data between cPouta and CSC computing
servers is to use Allas. However, if you you need to have direct access to your
data in the HPC servers, you can use `sshfs` to create temporary remote mounts
for your personal directories in Puhti or Mahti.

For example, if user `kkayttaj` would like to mount their scratch directory
(`/scratch/project_2012345`) from Puhti to a Ubuntu-based virtual machine
running in cPouta, they would first need to install `sshfs` to the virtual
machine:

```bash
sudo apt install sshfs
```

In CentOS machines the corresponding command is:

```text
sudo yum install sshfs
```

After that, an empty directory is created to be used as a mount point:

```bash
mkdir puhti_scratch
```

To be able to connect to Puhti and Mahti using an SSH client, you need to set
up SSH keys on your local workstation and register your public key in MyCSC.
Moreover, to make your local SSH keys available also in your cPouta virtual
machine, you need to enable SSH agent forwarding on your local machine. Read
the instructions:

* [How to set up SSH keys](../../computing/connecting/ssh-keys.md)
* [How to enable SSH agent forwarding](../../computing/connecting/ssh-unix.md#authentication-agent)

Once you've set up SSH keys, registered your public key in MyCSC, and
configured SSH agent forwarding on your local workstation, mounting of a remote
directory on Puhti can be done in your cPouta virtual machine with:

```bash
sshfs kkayttaj@puhti.csc.fi:/scratch/project_2012345 ./puhti_scratch
```

Here, you should replace `/scratch/project_2012345` with the scratch directory
of your project.

After this, directory `puhti_scratch` shows the contents of your scratch folder
in Puhti and it can be used as any mounted directory. However, the I/O
performance of the remotely mounted directories is not as good as locally
mounted directories. Because of that, in the case of I/O intensive tasks it may
be more reasonable to copy the data to the local disks of the virtual machine.
Tools like [`scp`](../../data/moving/scp.md) and
[`rsync`](../../data/moving/rsync.md) can be used for that.

To _**unmount**_; the file system, give a command:

```bash
fusermount -u mountpoint
```

For example the remote mount created above, would be removed with commands:

```bash
fusermount -u puhti_scratch
```

See also [Remote disk mounts](../../data/moving/disk_mount.md).
