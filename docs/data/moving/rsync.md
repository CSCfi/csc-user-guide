# Using rsync for data transfer and synchronization

**Rsync** is a data transfer tool that can be used much like the `scp` command.
When transferring data, `rsync` checks the difference between the source and
target files and only transfers the parts that have changed. This makes `rsync`
suitable for:

1. **Synchronizing folders**. Using `scp` or `cp` would copy and transfer
   everything, while `rsync` will only copy and transfer the modifications.
2. **Transferring large files**. `rsync` can be set to save progress, so if the
   transfer is interrupted, it can be resumed at the same point.

The basic command syntax of `rsync` is:

```bash
rsync -options source target
```

If the data source or target location is a remote site, it is defined with the
syntax:

```bash
username@server:/path/on/server
```

However, both the target and source can also be located on the same machine. In
that case you can just give directory paths to source and target sites.

The table below lists the most commonly used options:

|Option      |Argument|Description|
|------------|--------|-----------|
|`-r`        |        |Recurse into directories|
|`-a`        |        |Use archive mode: copy files and directories recursively and preserve access permissions and timestamps|
|`-v`        |        |Verbose mode|
|`-z`        |        |Compress|
|`-e`        |`ssh`   |Specify the remote shell to use|
|`-n`        |        |Show what files would be transferred|
|`--partial` |        |Keep partially transferred files|
|`--progress`|        |Show progress during transfer|
|`-P`        |        |Same as `--partial --progress`|

So the command for transferring a local folder to Puhti, while showing the
progress and keeping partially transferred files, would for example be:

```bash
rsync -rP /path/to/local/folder username@puhti.csc.fi:/path/to/target
```

This would either:

1. Create a folder on Puhti at `/path/to/target/folder` if the folder was not
   present before. In this case, everything in the local folder will be
   transferred.
2. Synchronize the source and target folders if the folder already exists on
   Puhti. In this case, only changes we have made will be transferred.

And the same thing in reverse:

```bash
rsync -rP username@puhti.csc.fi:/path/to/target/folder /path/to/local
```

!!! warning
    `rsync` will always overwrite any changes made to the target, even if they
    are newer than the source!
