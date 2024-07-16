
Linux tools such as `scp` and `rsync` are commonly used to transfer files _to_ and _from_ remote servers.
However, these tools are not very practical for tasks such as:

* copying a lot of small files
* copying big text files or image files in uncompressed formats (such as BMP or TIFF)
* retain attributes (permissions or user/group IDs) while transferring files
* not enough disk space to create a compressed archive of files/folder that needs to be transferred

A simple solution for such tasks is to directly pipe (redirect, `|`) the output of `tar` 
(linux command for archiving files/folders in a compressed format) through `ssh` 
(linux command for securing encrypted connection between two hosts over a network) to 
transfer the compressed archive on another host. 

The table below lists the most commonly used `tar` command operations and options:

|Option         |  Role     | Description                                |
|---------------|-----------|--------------------------------------------|
|`-c`           | Operation | Creates a new archive                      |
|`-x`           | Operation | Extract one or more items from an archive  |
|`-t`           | Operation | Lists an archive's contents                |
|`-r`           | Operation | Appends files to an existing archive       |
|`-A`           | Operation | Appends archives to an existing archive    |
|`-u`           | Operation | Updates archive with new files             |
|`--delete`     | Operation | Deletes a member from the archive          |
|`-f`           | Option    | Specifies the file                         |
|`-v`           | Option    | Verbose mode                               |
|`-z`           | Option    | Read or write compressed archives in gzip format|
|`-j`           | Option    | Read or write compressed archives in bzip2 format|
|`-C`           | Option    | Changes the directory                      |


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
