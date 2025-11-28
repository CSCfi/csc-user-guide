# Remote disk mounts

--8<-- "auth-update-ssh.md"

With remote disk mounts you can access your CSC directories in a way that
resembles the usage of an external disk or USB memory stick. Using this
approach normally requires installing some extra software to your local
computer, but it also makes the usage very fluent as no `scp` or other data
transfer programs are needed to move files between your local machine and CSC.

On macOS and Linux machines, `sshfs` can be used to mount certain disk areas at
CSC to a user's own machine. With this tool the remote disk areas at the
servers of CSC can be used just like local directories. To use `sshfs`, your
local Linux machine must have [FUSE](https://github.com/libfuse/libfuse) and
[`sshfs`](https://github.com/libfuse/sshfs) installed. In the case of macOS,
the required packages are [macFUSE and SSHFS](https://osxfuse.github.io/).

Please note that you need to have set up SSH keys and uploaded your public key
to MyCSC in order to work with remote disk mounts, just as when connecting over
regular SSH.
[Read how to set up SSH keys here](../../computing/connecting/ssh-keys.md).

## Using sshfs in Linux

Once `sshfs` is installed on your Linux machine, you can create a remote disk
mount with command syntax:

```bash
sshfs username@hostname:/path/to/dir /path/to/mountpoint
```

For example, to make the home directory of user _kayttaja_ on Puhti visible to
a local Linux computer, one would execute the following commands on the local
machine:

```bash
mkdir csc_home
sshfs kayttaja@puhti.csc.fi:/users/kayttaja csc_home
```

!!! info "Note"
    If you have stored your SSH key file with a non-default name or in a
    non-default location (somewhere else than `~/.ssh/id_<algorithm>`), you
    must specify where to look for the key as follows:

    ```bash
    sshfs username@hostname:/path/to/dir /path/to/mountpoint -o IdentityFile=/path/to/key
    ```

    Also, on macOS you might need to add the `-o defer_permissions` option to
    the `sshfs` command in case you are getting `Permission denied` errors
    after mounting.

The first command creates an empty directory that will be used as the mount
point in the second command. When the remote mount is established, you can use
the directory as any directory on your Linux system. For example, to list the
contents of the CSC home directory of _kayttaja_, one could just type the
command:

```bash
ls csc_home
```

If no path is specified, the default mounted remote directory is the user's
home directory.

To unmount the file system, give the command:

```bash
fusermount -u mountpoint
```

For our example, the command would be:

```bash
fusermount -u csc_home
```

On macOS, replace the `fusermount -u` command with `umount`.
