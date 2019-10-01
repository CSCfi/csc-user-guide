# a_backup: nearly a self-service backup

CSC does not provide a backup service as a free service for its' customers. In this chapter we describe a tool called *a_backup*
that can be used to make backup copies of files and directories to Allas.  However, you should remember that this tool does not 
provide a real backup service - the data is stored in one location only and just in one bucket in Allas. This bucket can be
removed by an authenticated user with only one command and after that all the backups are irreversibly lost. 

`a_backup` tool provides an easy-to-use command-line interface to the [restic](https://restic.readthedocs.io/) backup tool.
 `a_backup` automatically creates a project specific backup 
repository to the Allas storage service at CSC and uses that for making cumulative backups.

Unlike data upload tools like `a_put`, `s3cmd put` or `rclone copy`, the tool `a_backup` (or actually the restic program behind) stores the imported data as a collection hash.


In order to use this tool, you must first open connection to Allas storage service with
command:
```
source $allas_conf_path
```

**Note:** The connection remains open for three hours.

&nbsp;


**BACKUP OPERATIONS**

`a_backup` can be used for the following six operations:

 - `a_backup <file_name>`  or `a_backup add <file_name>`   
 	Adds a new backup version (snapshot) of the given file or directory to the backup repository.

 - `a_backup list`   
 	Lists the snapshots saved to the repository. Using the option **-last** lists only the latest versions of different snapshots.
 
 - `a_backup files <snapshot_id>`   
 	Lists the files that the snapshot includes.

 - `a_backup find <query>`          
 	Finds snapshots that contain file or directory that match the given query term.

 - `a_backup restore <snapshot_id>`  
 	Retrieves the data of the given snapshot to the local environment. 
	By default, the stored data is restored to the local directory. Other locations can be defined with *-target* option.

 - `a_backup delete <snapshot_id>`  
 	Deletes a snapshot from the backup repository.


&nbsp;

