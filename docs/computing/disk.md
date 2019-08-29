# Disk areas

In Puhti there are three main disk areas: **home**, **projappl** and **scratch**.
These directories have specific purpose and you should be familiar with them before you start using Puhti.

|        |  Default quota   | Personal/project |  Environment variable |  path                          | Cleaning       |
|--------|------------------|------------------|-----------------------|--------------------------------|----------------|  
| Home   | 10 GiB           | Personal         | $(HOME)               | /home/<user-name>              |  No            | 
| Projappl | 50 GiB         | Project          |   Not available       | /projappl/project_<project_id> | No             |
| Scratch | 1 TiB           | Project          |   Not available       | /scratch/project_<project_id>  | Yes - 90 days  |


## Home directory

Each Puhti user has a home directory (`$HOME`) that can contain up to 10 GB of data.
Home directory is the default directory into which you end up when you login to Puhti. 
However, typically you should move further to your projects _scratch directory_ when you work in Puhti.
This is because your home directory is not ment for data analysis or computing, but just for storing configurations files, 
and other small personal data. If you fill up your home directory so that no new files can't be created there, it will couse many problems for your account.

Note, that home directory is the only user specific directory in Puhti. Other directories are project specific. If you are a memeber in several projects you have access to several _scratch_ or _projappl_ directories, but still you have just one home directory. Home directory is not automatically backed up by CSC (the same applies to all directories in Puhti), so if some data is accidentally deleted by the user, it can't be recovered.

## Scratch directory

Each project has 1 TB of scartch disk space in directory `/scratch/<project_id>`.
This fast paralle scratch space is intented to be used as a temporary storage space for the data that is used in Puhti.
Scratch directory is not meant for long term data storage and **files that have not been used for 90 days will be
automatically removed**.

Note that this folder is shared by **all users** in a project. 

As the path of the project directory is dependent on the project ID, you must first find our the project number you want to use.
You can check the project names from [MyCSC portal](https://my.csc.fi). 

For example if you are member inpouta projects, _project_2002291_ and _project_3587167_ the you have access to scartch directories:
```
/scratch/project_2002291
/scratch/project_3587167
```
Moving to scratch directory of project_2002291 is done with command:
```
cd /scratch/project_2002291
```
Note that all CSC projects do not have Puhti access so you don't necessary find a _scratch_ or _projappl_ directory for all your CSC projects. To get an overview of your directories in Puhti, run command:
```
csc-workspaces
```
If you are mostly using just one project in Puhti, you can set environment variables $SCRATCH and $PROJAPPL to point to the scratch and projappl directories of a CSC project. This setting can be done with commmad:
<pre>
csc-workspaces set <i>project_ID</i>
</pre>

Scratch folder is accessible for all the members of the project. 

As mentoned earlier, scratch directory is intended for only processing data. The data, that should be preserverd for longer time should be copied to Allas storage server. Backup file from Puhti to Allas will ppeaer here, once Allas storageservice becomes available. 





## Projaappl directory

Project application folder for storing applications you have compiled yourself, libraries,
etc. there is also a persistent **project based** storage with a
default quota of 50 GB. It is located under
`/projappl/project_<project_id>`.  Project based means that this is
not a personal storage space, but is shared with all members of the
project team.

It is not meant for running applications, use scratch for that
purpose.



