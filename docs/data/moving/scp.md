Copying files between different linux, MacOSX or UNIX servers can be done with the `scp` command. Thus you can use scp to transport data between CSC and your local environment or between different file systems at CSC.


The basic syntax for copying data from a local machine to a remote machine is:
```bash
scp /path/to/file user@server.example.fi:/path/to/remote/destination
```
And correspondingly the syntax to copy files from a remote machine to a local machine is:

```bash
scp user@server.example.fi:/path/to/file /path/to/local/destination
```

The command to copy a local file _data.txt_ from the current directory to Puhti the user _bob_:s  home directory would be:

```bash
scp data.txt bob@puhti.csc.fi:~/
```
The special symbol `~` points to the users home directory.


To copy complete directories you should use `scp` command with option **-r**.
```bash
scp -r /path/to/data_directory bob@puhti.csc.fi:/scratch/project_#####/data_dir 
```
The above command will copy the directory with all its content to Puhti. The directory will be created 
in _/scratch/project_#####_.

Copying the data from CSC environment to local computer is done in the same way:
```bash
scp bob@puhti.csc.fi:/scratch/project_#####/data.txt .
```
The `.` symbol points to the current local directory. Use the `csc-workspaces` command on Puhti to show available
disk areas. 


In the commands above, files and directories have been copied one at a time. However, scp can copy several files at a time:
```bash
scp data1.txt data2.txt data3.txt bob@puhti.csc.fi:~/
```

You can also use  wild cards when defining the files to be copied. For example to copy all files with extension _.txt_ in the current directory to Puhti, you could use the command:

```bash
scp *.txt kkayttaj@puhti.csc.fi:~/
```
By default the copied files are treated as new files, but if you add option **-p** to the `scp` command, then the copied file will inherit the date and access mode information from the original file.
