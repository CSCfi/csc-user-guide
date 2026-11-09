# Using Tar over SSH to move many files

--8<-- "ssh-ca.md"

Linux tools such as `scp` and `rsync` are commonly used to transfer files
between a remote server and a local machine. However, these tools are not
very practical for moving many small files.

A simple, much faster solution is to write a (compressed) tar package
containing your data directly to the target system. This is accomplished by
piping the output of `tar` over an `ssh` connection. Writing the archive
directly to the destination helps also to conserve disk space on the source
system.

For general information about tar, see
[Packing and compression tools](../../support/tutorials/env-guide/packing-and-compression-tools.md).

## Examples

### Transferring data between your local computer and Roihu

All following commands are executed on a local workstation, which is assumed to
have the required tools (`tar`, `ssh` and, optionally, `gzip`/`bzip2`) installed.
Roihu is used as the example remote server.

The general syntax is:

```bash
tar c <directory_to_transfer> | ssh <username>@roihu-cpu.csc.fi 'cat > <target_path_on_roihu>'
```

For example, the command to copy a directory `myfiles` from your local machine
to the directory `/scratch/project_2001234` on Roihu would be:

```bash
tar c myfiles | ssh <username>@roihu-cpu.csc.fi 'cat > /scratch/project_2001234/myfiles.tar'
```

!!! info "Note"
    If you have stored your SSH key or certificate file with a non-default name
    or in a non-default location (somewhere else than `~/.ssh/id_<algorithm>`
    and `~/.ssh/id_<algorithm>-cert.pub`), you must specify where `ssh` should
    look for the files using the `-i` option, e.g:

    ```bash
    tar c myfiles | ssh -i <path_to_private_key> -i <path_to_certificate> <username>@<host> 'cat > /scratch/project_2001234/myfiles.tar'
    ```

    The rest of this page assumes the key and certificate are stored in a
    default location using standard naming, so the `-i` flag is omitted. Note
    that SSH certificates are required for connecting to Roihu only.

To extract the tar archive at the same time, replace the `cat` command as:

```bash
tar c myfiles | ssh <username>@roihu-cpu.csc.fi 'tar x -C /scratch/project_2001234'
```

Conversely, you could also copy data located on the remote server to your local
machine using a command like:

```bash
ssh <username>@roihu-cpu.csc.fi 'tar c -C <parent_directory_on_roihu> <directory_to_transfer>' > <archive_on_local_machine>
```

For example, the command to copy a folder `myfiles` located in
`/scratch/project_2001234` to your local machine would be:

```bash
ssh <username>@roihu-cpu.csc.fi 'tar c -C /scratch/project_2001234 myfiles' > myfiles.tar
```

To extract the archive at the same time:

```bash
ssh <username>@roihu-cpu.csc.fi 'tar c -C /scratch/project_2001234 myfiles' | tar x
```

!!! info "Enable compression"
    The above commands did not use compression. Replace `tar c` (`tar x`) with
    `tar cz` or `tar cj` (`tar xz` or `tar xj`) to enable gzip or bzip2
    compression (decompression). Note that some files do not benefit from
    compression (e.g. binary files or files that are already compressed), in
    which case it is faster to transfer without compressing.

!!! info "Avoid verbose output"
    Adding `v` option (e.g. `tar czv`) will produce verbose output, i.e. list
    the processed files in the console. This slows down the transfer process
    when moving many small files, so it is recommended to avoid using it.

### Transferring data directly between CSC supercomputers

To transfer data directly between CSC supercomputers, you must be able to access
the SSH keys you've set up on your local workstation for authenticating to CSC
supercomputers. For Roihu, a valid SSH certificate is also needed. This is
accomplished by forwarding your SSH agent including your SSH keys (and
certificate) to the supercomputer you're first connecting to.

- [SSH agent forwarding instructions for Linux/macOS](../../computing/connecting/ssh-unix.md#ssh-agent-forwarding)
- [SSH agent forwarding instructions for Windows](../../computing/connecting/ssh-windows.md#ssh-agent-forwarding)

After this, data can be transferred directly between CSC supercomputers using
same syntax as above. For example, the command to transfer a directory
`/scratch/project_2001234/myfiles` on Roihu to directory
`/scratch/project_462000123` on LUMI would be:

```bash
tar c -C /scratch/project_2001234 myfiles | ssh <username>@lumi.csc.fi 'cat > /scratch/project_462000123/myfiles.tar'
```

The same could be accomplished while working on LUMI as follows:

```bash
ssh <username>@roihu-cpu.csc.fi 'tar c -C /scratch/project_2001234 myfiles' > /scratch/project_462000123/myfiles.tar
```

## Performance comparison

Below is a rough comparison of the time taken to transfer a directory with many
small files to Roihu. Each file is 100 KiB in size and no compression is
applied.

| Number of files        | `tar` + `ssh` | `scp`    |
|-----------------------:|--------------:|---------:|
| 100                    | 0.5 s         | 2.4 s    |
| 1000                   | 1.3 s         | 20.5 s   |
| 10000                  | 9.4 s         | 201.2 s  |

## More information

- [Packing and compression tools](../../support/tutorials/env-guide/packing-and-compression-tools.md)
