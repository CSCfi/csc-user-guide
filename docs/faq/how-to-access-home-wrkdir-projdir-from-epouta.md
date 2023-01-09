# How to access directories in Puhti and Mahti from cPouta?

The storage environments of the CSC computing servers (Puhti and Mahti) are not directly accessible to cPouta because the HPC systems network is separated from cPouta for security and performance reasons. 

Normally, the recommended way to move data between cPouta and CSC computing servers, is to use Allas. However if you you need to have direct access to your data in the HPC servers, you can use `sshfs` to create a temporary remote mounts for your personal directories in Puhti or Mahti.

For example, if user _kkayttaj_ would like to mount his scratch directory (/scratch/project_2012345) from Puhti to a Ubuntu based virtual machine running in cPouta, he would first need to install sshfs too to the virtual machine:

```
sudo apt install sshfs
```
In Centos machines the corresponding command is:

```text
sudo yum install sshfs
```

After that, an empty directory is created to be used as a mount point:

```
mkdir puhti_scratch
```

Next the mounting is done with command:

```
sshfs kkayttaj@puhti.csc.fi:/scratch/project_2012345 ./puhti_scratch
```

(Here, you should replace /scratch/project_2012345 with the scratch directory of your project).

After this, directory _puhti_scratch_ shows the content of scratch in Puhti and it can be used as any mounted directory. However, the I/O performance of the remotely mounted directories is not as good as locally mounted directories. Because of that, in the case of I/O intensive tasks it may be more reasonable to copy the data to the local disks of the virtual machine. Tools like `scp` and `rsync` can be used for that.

To _**unmount**_; the file system, give a command:

```
fusermount -u mountpoint
```

For example the remote mount created above, would be removed with commands:

```
fusermount -u puhti_scratch
```
