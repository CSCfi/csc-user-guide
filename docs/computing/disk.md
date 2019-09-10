# Disk areas

Puhti has three main disk areas: **home**, **projappl** and **scratch**. Please familiarize yourself with the areas and their specific purposes before using Puhti.


|              |  Owner    | Environment variable | Path                                            | Cleaning      |
| ------------ |  -------- | -------------------- | ----------------------------------------------- | ------------- |
| **home**     |  Personal | `$(HOME)`            | <small>`/users/<user-name>`</small>             | No            |
| **projappl** |  Project  | Not available        | <small>`/projappl/<project>`</small>            | No            |
| **scratch**  |  Project  | Not available        | <small>`/scratch/<project>`</small>             | Yes - 90 days |


There are the default quotas:

|              | Capacity   | Number of files   |
| -------------| --------   | -------------     |
| **home**     | 10 GiB     | 100 000 files     |
| **projappl** | 50 GiB     | 100 000 files     |
| **scratch**  | 1 TiB      | 1 000 000 files   |

See [Increasing Quotas](#increasing-quotas) for instructions on how to apply for increased quota.


## Home directory

Each Puhti user has a home directory (`$HOME`) that can contain up to 10 GB of
data.

The home directory is the default directory where you begin after
logging in to Puhti. However, typically you should change to your
project's _scratch_ directory when working with Puhti because the
**home directory is not intended for data analysis or computing**. Its
purpose is to store configuration files and other minor personal
data. A home directory exceeding its capacity causes various account
problems.

The home directory is the only user-specific directory in Puhti. All other directories
are project-specific. If you are a member of several projects, you also have access
to several _scratch_ or _projappl_ directories, but still have only one home directory.

!!! note
    The home directory is not automatically backed up by CSC (the same applies to
    all directories in Puhti), which means that data accidentally deleted by the
    user cannot be recovered.


## Scratch directory

Each project has 1 TB of scratch disk space in the directory
`/scratch/<project>`.

This fast parallel scratch space is intended as temporary storage
space for the data that is used in Puhti. The scratch directory is not intended for
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

An overview of your directories in Puhti:
```text
csc-workspaces 
```

The above command displays all _scratch_ and _projappl_ directories you have access to within
active projects with Puhti access. You can find the projects' names and
other project information at the [MyCSC portal](https://my.csc.fi). In MyCSC it is the "unix group" that
defines the name of the disk folders in _scratch_ and _projappl_ directories. 

For example, if you are member in two projects, with unix groups _project_2002291_
and _project_3587167_, then you have access to their scratch directories:
```text
/scratch/project_2002291
/scratch/project_3587167
```
Moving to the scratch directory of project_2002291:
```text
cd /scratch/project_2002291
```
Please note that not all CSC projects have Puhti access, so you may not
necessarily find a _scratch_ or _projappl_ directory for all your CSC projects.

If you are mostly involved in only one Puhti project, you can set the
environment variables $SCRATCH and $PROJAPPL to point at the _scratch_ and
_projappl_ directories of a CSC project:
<pre>
csc-workspaces set <i>project</i>
</pre>

The _scratch_ and _projappl_ directories are shared by **all the members of the
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
_Allas_ storage server. Instructions for backing up files from Puhti to Allas
will be included in this guide as soon as the Allas storage service is available.


## Increasing Quotas


The quota of the _scratch_ and _projappl_ directories can be increased, but only if the
analysis or computing task requires more data to be simultaneously available
on the disk environment of Puhti than what is allowed by the quota. In these cases,
please send a request to
_servicedesk@csc.fi_.  In the request, please indicate the project,
storage size needed, purpose and duration of the quota
extension. In the future, the process for increasing quotas will be
improved. Please allow for some delay in serving this kind of requests.

Data that is not under active computing should be stored in the Allas
storage service.

Note that the extended scratch quota consumes your CSC billing unit
quota regardless of how much data you actually have in the scratch
directory. See [billing](../accounts/billing.md) for details.
Furthermore, even after the quota is increased, the automatic cleaning
process will continue removing idle files from the _scratch_ directory.


## Additional disk areas

### Login nodes

All of the login nodes have 2900 GiB of fast local storage. The storage
is located under `$TMPDIR` and is separate for each login node.  

The local storage is good for compiling applications and performing 
pre- and postprocessing that require heavy IO operations, for example packing and unpacking 
archive files. 

!!! Note
    The local storage is meant for **temporary** storage and is cleaned frequently.
    Remember to move your data to a shared disk area after completing your task. 

### Compute nodes 

The IO- and gpu-nodes have local fast storage available upon request for jobs.
For more information see: [creating job scripts](running/creating-job-scripts.md#local-storage). 
**Do not use `$TMPDIR` for storage on compute nodes.**
