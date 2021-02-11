# Disk areas

CSC supercomputers have three main disk areas: **home**, **projappl** and **scratch**. Please familiarize yourself with the areas and their specific purposes.
The disk areas for different supercomputers are separate, *i.e.*
**home**, **projappl** and **scratch** in Puhti cannot be directly
accessed from Mahti. A more technical description about the Lustre filesystem used in these directoties can be found [here](lustre.md).

|              |  Owner    | Environment variable | Path                                            | Cleaning      |
| ------------ |  -------- | -------------------- | ----------------------------------------------- | ------------- |
| **home**     |  Personal | `$(HOME)`            | <small>`/users/<user-name>`</small>             | No            |
| **projappl** |  Project  | Not available        | <small>`/projappl/<project>`</small>            | No            |
| **scratch**  |  Project  | Not available        | <small>`/scratch/<project>`</small>             | Yes - 90 days |



These disk areas have quotas for both the amount of data and total number of files:

|              | Capacity | Number of files      |
| -------------| ---------|----------------      |
| **home**     | 10 GiB   |  100 000 files       |
| **projappl** | 50 GiB   |  100 000 files       |
| **scratch**  | 1 TiB    |  1 000 000 files     |

See [Increasing Quotas](#increasing-quotas) for instructions on how to apply for increased quota.

## Home directory

Each user has a home directory (`$HOME`) that can contain up to 10 GB of
data.

The home directory is the default directory where you begin after
logging in to supercomputer. However, typically you should change to your
project's _scratch_ directory when working because the
**home directory is not intended for data analysis or computing**. Its
purpose is to store configuration files and other minor personal
data. A home directory exceeding its capacity causes various account
problems.

The home directory is the only user-specific directory in supercomputers. All other directories
are project-specific. If you are a member of several projects, you also have access
to several _scratch_ or _projappl_ directories, but still have only one home directory.

!!! note
    The home directory is not automatically backed up by CSC (the same applies to
    all directories), which means that data accidentally deleted by the
    user cannot be recovered.


## Scratch directory


Each project has by default 1 TB of scratch disk space in the directory `/scratch/<project>`.

This fast parallel scratch space is intended as temporary storage
space for the data that is used in supercomputers. The scratch directory is not intended for
long-term data storage and **any files that have not been used for 90 days will
be automatically removed**.

## ProjAppl directory

Each project has also a 50 GB project application disk space in the directory
`/projappl/<project>`.

It is intended for storing applications you have compiled yourself and libraries
etc. that you are sharing within the project. It is not a personal storage space but it
is shared with all members of the project team.

It is not intended for running applications, so please run them in _scratch_ instead.

## Using Scratch and ProjAppl directories


An overview of your directories in a supercomputer you are currently
logged on can be displayed with:

```text
csc-workspaces 
```
The above command displays all _scratch_ and _projappl_ directories you have access to.

For example, if you are member in two projects, with unix groups _project_2012345_
and _project_3587167_, then you have access to two scratch and projappl directories:

<pre>[kkayttaj@puhti ~]$ <b>csc-workspaces</b> 
Disk area               Capacity(used/max)  Files(used/max)  Project description  
----------------------------------------------------------------------------------
Personal home folder
----------------------------------------------------------------------------------
/users/kkayttaj                2.05G/10G       23.24k/100k

Project applications 
----------------------------------------------------------------------------------
/projappl/project_2012345     3.056G/50G       23.99k/100k   Ortotopology modeling
/projappl/project_3587167     10.34G/50G       2.45/100k     Metaphysics methods

Project scratch 
----------------------------------------------------------------------------------
/scratch/project_2012345        56G/1T         150.53k/1000k Ortotopology modeling
/scratch/project_3587167       324G/1T         5.53k/1000k   Metaphysics methods
</pre>

Moving to the scratch directory of project_2012345:
```text
cd /scratch/project_2012345
```
Please note that not all CSC projects have Puhti/Mahti access, so you may not
necessarily find a _scratch_ or _projappl_ directory for all your CSC projects.


**The _scratch_ and _projappl_ directories are shared by all the members of the
project**. All new files and directories are also fully accessible for other
group members (including read, write and execution permissions). If you want
to restrict access from your group members, you can reset the permissions with
the _chmod_ command.

Setting read-only permissions for your group members for the directory
*my_directory*:
```text
chmod -R g-w my_directory
```

As mentioned earlier, the _scratch_ directory is only intended for processing data.
Any data that should be preserved for a longer time should be copied to the
_Allas_ storage server. Instructions for backing up files from CSC
supercomputers to Allas can be found in the [Allas guide](../data/Allas/index.md).

## Moving data between supercomputers

Data can be moved between supercomputers via Allas by first uploading
the data in one supercomputer and then downloading in another
supercomputer. This is the recommended approach if the data should also
be preserved for a longer time.

Data can also be moved directly between the supercomputers with the
_rsync_ command. For example, in order to copy *my_results* (which can be
either file or directory) from
Puhti to the directory */scratch/project_2002291* in Mahti, one can
issue in Puhti the command: 
```bash
rsync -azP my_results <username>@mahti.csc.fi:/scratch/project_2002291
```
See [Using rsync](../data/moving/rsync.md) for more detailed instructions
for *rsync*.

## Increasing Quotas


You can use **MyCSC portal** to [manage quotas of the _scratch_ and _projappl_ directories](../accounts/how-to-increase-disk-quotas.md).

Remember that even after the quota is increased, the automatic cleaning
process will continue removing idle files from the _scratch_ directory.
Data that is not under active computing should be stored in the Allas
storage service.

Remember also, that you can increase these values only to some extent. 
Especially in the case of number of files, you should reconsider your 
data work flow, if it requires that tens of millions
of files are stored to the _scratch_ area.

## Additional disk areas

### Login nodes

All of the login nodes have 2900 GiB of fast local storage. The storage
is located under `$TMPDIR` and is separate for each login node.  

The local storage is good for compiling applications and performing 
pre- and post-processing that require heavy IO operations, for example packing and unpacking 
archive files. 

!!! Note
    The local storage is meant for **temporary** storage and is cleaned frequently.
    Remember to move your data to a shared disk area after completing your task. 

### Compute nodes in Puhti 

Interactive batch jobs as well as jobs running in the IO- and gpu-nodes have local fast storage available. In interactive batch jobs this local disk area is defined with environment variable $TMPDIR and in normal batch jobs with $LOCAL_SCRATCH. The size of this storage space is defined in the batch job resource request (max. 3600 GB).

These local disk areas are designed to support I/O intensive computing tasks and cases where you need to process large amounts (over 100 000 files) of small files. These directories are cleaned once the batch job finishes. Thus, in the end of a batch job you must copy all the data that you want to preserve from these temporary disk areas to _scratch_ directory or to Allas. 

For more information see: [creating job scripts](running/creating-job-scripts-puhti.md#local-storage). 

