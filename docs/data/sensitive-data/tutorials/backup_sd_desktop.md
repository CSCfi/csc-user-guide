# Backup server for SD Desktop

For security reasons only the Project Manager can export data from SD Desktop. Thus normal SD desktop users can not 
make backup copiens of the data that they have in SD Desktop. This tutorial demonstrates the usage of backup_server.sh 
process and sd-backup commands that provide a way for SD Users to backup their data to SD Connect.

## Installation 

The tools for running backup process are not by default installed in SD Desktop Virtual Machines. Thus the first step is that the Projet 
manager installs the **SD Backup tool** package using the **SD-tools-installer**. 

Log in to your SD Desktop and open **Data Gateway**. If the software installation help tools are enabled for your project, then you should have folder: 
**tools-for-sd-desktop** included in the directory that Data Gateway created ( in Projects/SD-Connect/_your-project-name_). If you don't find _tools-for-sd-desktop_ 
directory through data gateway **send a request to servicedesk@csc.fi**. In the request, indicate that you wish that the SD Desktop software installation help tools would 
be made available for your project.  You must also include to the message the  **Project identifier string** of your project.
You can check this random string for example in the [SD Connect service](https://sd-conenct.csc.fi). There you find the 
Project Identifier in the **User information** view. 


Open _tools-for-sd-desktop_ folder and from there, drag/copy file **sd-installer.desktop** to your desktop.

[![Installing-sd-installer](../images/desktop/sd-installer1.png)](./images/desktop/sd-installer1.png)

**Figure 1.** Copying sd-installer.desktop file to SD desktop.
 
Double click the copy of _sd-installer.desktop_ to start the software installation tool. Use this tool to install _SD Backup_ tool
to your SD Desktop virtual machine if you have not yet done so. 

## Project Mangers Starts backup server

When the SD Backup tool is installed, the Project Manager should start new terminal session, and there start a virtual terminal session with command:

```text
screen
```
An then launch the backup process with command:

```text
sd-backup-server.sh
```
When launched _sd-backup-server.sh_ asks for the CSC password of the Project Manger. 

After that the project manager can leave the virtual session running in background by pressing:
__Ctrl+a+d__.

This way the _sd-backup-server.sh_ command remains active in the virtual terminal session even when the connection to SD Desktop is closed.

The actual server process is very simple. It checks the content of the backup directory once in a minute and moves the contents of this directory 
to a bucket in SD Connect. The data is encrypted with CSC public key only so that the backups can be used only in SD Desktop environment.
The default backup directory is _/shared-data/auto-backup_ and taget bucket in SD Connect is sdd-backup-_vitual-machine-name_. 

Note that the server is not able to check if the given password was correct. If a wrong password was given then backup requests will fail. 
Thus it may be good to test the backup process once the server is running.

## Doing backups

When the backup server is running, all users of the VM can use command _sd-backup_ to make a backup copy of the dataset to SD Connect.
The syntax of the sd-backup command is:

```t
sd-backup file.csv
```
or
```text
sd-backup directory
```
The command copies the given file or directory to the backup directory from where the server process is able to move it to SD Connect.
In SD Connect a timestamp is added to the file name in order to make the file name unique. In addition a metadata file is
created. This file contains information about the user who requested the backup, original host and location of the file. If backup is done for 
a directory, then the content of the directory is stored as one tar-archive file and the metadatafile will contain list of the backuped files. 
 
For example, for a file called _my_data.csv_ that locates in SD Desktop virtual machine called _secserver-1683868755_, a backup command:

```text
sd-backup  my_data.csv
```
Will create a backupfile that will be available through Data-gateway in path:
```text
Projects/SD-Connect/project_number/sdd-backup-secserver-1683868755/my_data.csv-2023-05-15-07:41
```

Note that you have to refresh the Data Gateway connection in order to see the changes in SD Connect.
