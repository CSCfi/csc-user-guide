# A_backup: nearly a self sercive backup

CSC does not provide a back-up service as a free service for its' customers. In this chapter we descibe a tool called a_backuop
than can be used to make backup copies of files and directories to Allas.  However, you should remember that this tool does not 
provide a real back up service: The data is stored in one location only and just in a one bucket in Allas. This bucket can be
removed by an authenticated user with one command and after that all the backuos are irreveribely lost. 

<b>a_backup</b> tool provides easy to use command line interface to the <i>restic<i> back up tool.
(https://restic.readthedocs.io/). <i>a_backup</i> automatically creates a project specific back up 
repository to the Allas storage service at CSC and uses that for making cumulative back ups.

Unlike data upload tools like a_put, s3cmd or rclone, a_backup ( or actually the resrtic program behind) stores the imprted 
data as collection hash 


In order to use this tool, you must first open connection to Allas storage service with
command:
   source $allas_conf_path

The connection remains open for three hours.


BACKUP OPERATIONS

a_backup can be used for following five operations:

  a_backup <file_name>  or
  a_backup add <file_name>       Add a new backup version (snapshot) of the given file 
                                 or directory to the back up repository.

  a_backup list                  Lists the snapshots saved to the repository. 
                                 Option: -last lists only the latest versions of different snapshots.
 
  a_backup files <snapshot_id>   List the files that the snapshot includes.

  a_backup find <query>          Find snapshots that contain file or directory that match the given query term.

  a_backup restore <snapshot_id> Retrieves the data of the given snapshot to the local environment. By default 
                                 the stored data is restored to the local directory. Other locations can be 
                                 defined with -target option.

  a_backup delete <snapshot_id>  Deletes a snapshot from the backup repository.

