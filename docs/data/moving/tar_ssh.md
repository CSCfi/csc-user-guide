
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


## Transfer files with compression

```bash
tar czvf - /file/or/folder /some/other/file/or/folder | ssh username@server  "cd /path/to/transfer/file/or/folder && tar xvzf - "
```

For ex., the command to copy a file (_file.txt_) and folder (_folder_) from your computer to the _scratch_ partition of your project (_project_123456_) on Puhti, would be:

```bash
tar czvf - file.txt folder | ssh username@puhti.csc.fi "cd /scratch/project_123456 && tar xzvf - "
```

You can also copy files and/or folders which are located on the remote server onto local machine, using the command 

```bash
ssh username@server "cd /path/to/file/or/folder/to/be/transferred && tar czvf - file(or folder)" | tar xzvf - 
```

For ex., the command to copy a folder (_folder_) from the _scratch_ partition of your project (_project_123456_) on Puhti to your computer, would be:

```bash
ssh username@puhti.csc.fi "cd /scratch/project_123456 && tar czvf - folder" | tar xzvf - 
```

!!! note 
* Both systems (your computer as well as the remote server) must support `ssh` and have `tar` and `gzip` installed. 
* If you are using bzip2 (`tar cjvf`) for compression, `bzip2` must be installed on the systems.
* On CSC servers (Puhti and Mahti), these linux tools are already installed.

## Transfer files without compression

If you have to transfer files that you know cannot be compressed much (for ex., binary files) or are already in compressed format, it is faster to transfer them without any further compression.

### From local machine to remote server:

```bash
tar cvf - /file/or/folder /some/other/file/or/folder | ssh username@server "cd /path/to/transfer/file/or/folder && tar xvzf - "
```

### From remote server to local machine:

```bash
ssh username@server "cd /path/to/file/or/folder/to/be/transferred && tar cvf - file(or folder)" | tar xvf -
```

!!! note
If you are transferring a lot of small files, your transfer speed may be slowed down by console output. 
Just remove the `v` parameter to stop printing transferred files in the console.
