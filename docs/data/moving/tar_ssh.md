# Using Tar over SSH to move many files

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

All following commands are executed on a local workstation, which is assumed to
have the required tools (`tar`, `ssh` and, optionally, `gzip`/`bzip2`) installed.
Puhti is used as the example remote server.

The general syntax is:

```bash
tar c <directory_to_transfer> | ssh <username>@puhti.csc.fi 'cat > <target_path_on_puhti>'
```

For example, the command to copy a directory `myfiles` from your local machine
to the directory `/scratch/project_2001234` on Puhti would be:

```bash
tar c myfiles | ssh <username>@puhti.csc.fi 'cat > /scratch/project_2001234/myfiles.tar'
```

To extract the tar archive at the same time, replace the `cat` command as:

```bash
tar c myfiles | ssh <username>@puhti.csc.fi 'tar x -C /scratch/project_2001234'
```

Conversely, you could also copy data located on the remote server to your local
machine using a command like:

```bash
ssh <username>@puhti.csc.fi 'tar c -C <parent_directory_on_puhti> <directory_to_transfer>' > <archive_on_local_machine>
```

For example, the command to copy a folder `myfiles` located in
`/scratch/project_2001234` to your local machine would be:

```bash
ssh <username>@puhti.csc.fi 'tar c -C /scratch/project_2001234 myfiles' > myfiles.tar
```

To extract the archive at the same time:

```bash
ssh <username>@puhti.csc.fi 'tar c -C /scratch/project_2001234 myfiles' | tar x
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

## Performance comparison

Below is a rough comparison of the time taken to transfer a directory with many
small files to Puhti. Each file is 100 KiB in size and no compression is
applied.

| Number of files        | `tar` + `ssh` | `scp`    |
|-----------------------:|--------------:|---------:|
| 100                    | 0.5 s         | 2.4 s    |
| 1000                   | 1.3 s         | 20.5 s   |
| 10000                  | 9.4 s         | 201.2 s  |

## More information

- [Packing and compression tools](../../support/tutorials/env-guide/packing-and-compression-tools.md)
