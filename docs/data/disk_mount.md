## Remote disk mounts

With remote disk mounts you can use your CSC directories in a way that resembles the usage of an external disk or USB memory stick. Using this approach normally requires installing some extra software to your local computer, but it also makes the usage very fluent as no `scp` or other data transfer programs are needed to move files between local computer and CSC.

On Mac OSX and linux machines, **sshfs** can be used to mount some disk areas at CSC to users own machine. With this tool the remote disk areas at the servers of CSC can be used just like local directories. To be able to use `sshfs` you local Linux machine must have [FUSE]( http://fuse.sourceforge.net/) and [sshfs]( https://github.com/libfuse/sshfs) installed. In the case of MacOSX the required packages are OSXFUSE and SSHFS <https://osxfuse.github.io>

**Using sshfs in Linux**

Once sshfs is installed in your Linux machine you can create remote disk mount with command syntax:
```bash
sshfs username@hostname:/path/to/dir /path/to/mountpoint
```

For example, to make the home directory on Taito of user _kayttaja_ visible to a local Linux computer, execute command:
```bash
mkdir csc_home
sshfs kayttaja@taito.csc.fi:/homeappl/home/kayttaja ./csc_home
```

 

The first command creates an empty directory that will be used as the mount point in the second command. When the remote mount is established, you can use the directory as any directory in your Linux system. For example, to see the content of the CSC home directory of _kayttaja_, you could now give a command:

```bash
ls csc_home
```

If no path is specified, the default mounted remote directory is the users home directory.

To unmount the file system, give the command:
```bash
fusermount -u mountpoint
```

For our example, the command would be:
```bash
fusermount -u csc_home
```
