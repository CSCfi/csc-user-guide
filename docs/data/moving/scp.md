Copying files between different Linux, MacOSX or UNIX servers can be done with the `scp` command. Thus you can use scp to transport data between CSC and your local machine or between different file systems at CSC.


The basic syntax for copying data from a local machine to a remote server is:

```bash
scp /path/to/file username@server:/path/to/remote/destination
```

And correspondingly the syntax to copy files from a remote server to a local machine is:

```bash
scp username@server:/path/to/file /path/to/local/destination
```

For example, the command to copy a local file (_data.txt_) from the current directory to Puhti, to the user's (_bob_:s)  home directory would be:

```bash
scp data.txt bob@puhti.csc.fi:~/
```

The special symbol `~` points to the users home directory.


To copy complete directories, you should use `scp` command with option **-r**.
Use the `csc-workspaces` command on Puhti to show available disk areas. 

```bash
scp -r /path/to/data_directory bob@puhti.csc.fi:/scratch/project_2001234/data_dir 
```

The above command will copy the directory (data_directory) with all its content to Puhti at _/scratch/project_2001234/data_dir_.

Copying the data from CSC server to your local machine is done in the same way:

```bash
scp bob@puhti.csc.fi:/scratch/project_2001234/data.txt .
```

The `.` symbol points to the current local directory on your local machine. 

In the commands above, files and directories have been copied one at a time. However, `scp` can also copy several files at a time:

```bash
scp data1.txt data2.txt data3.txt bob@puhti.csc.fi:~/
```

You can also use  wild cards when defining the files to be copied. 
For example, to copy all files with extension _.txt_ from the current directory on your local machine to your home directory on Puhti, you could use the command:

```bash
scp *.txt bob@puhti.csc.fi:~/
```

By default the copied files are treated as new files, but if you add option **-p** to the `scp` command, then the copied file will inherit the date and access mode information from the original file.
