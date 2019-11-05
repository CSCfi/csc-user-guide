# How to access my CSC home/wrkdir/project directories from ePouta?

It's possible to access your regular CSC $HOME, $WRKDIR and even application directories from cPouta in the same way it is possible to access them from outside CSC. These directories are not directly accessible to cPouta because the HPC systems network is separated for security and performance reasons. However if you install `sshfs` tool to you virtual machine you can create a temporary remote mounts for your personal directories in Taito or Sisu.

For example, if user _kkayttaj_ would like to mount his $WRKDIR from Taito to a Ubuntu based virtual machine running in cPouta, he would first need to install sshfs too to the virtual machine:

```
sudo apt install sshfs
```

After that, an empty directory is created to be used as a mount point:

```
mkdir taito_wrk
```

Next the mounting is done with command:

```
sshfs kkayttaj@taito.csc.fi:/wrk/kkayttaj ./taito_wrk
```

After this, directory _taito_wrk_ shows the content of $WRKDIR in Taito and it can be used as any mounted directory. However, the I/O performance of the remotely mounted directories is not as good as locally mounted directories. Because of that, in the case of I/O intensive tasks it may be more reasonable to copy the data to the local disks of the virtual machine. Tools like `scp` and `rsync` can be used for that.

To _**unmount**_; the file system, give a command:

```
fusermount -u _mountpoint_
```

For example the remote mount created above, would be removed with commands:

```
fusermount -u taito_wrk
```
