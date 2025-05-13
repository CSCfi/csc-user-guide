# Disk areas

CSC supercomputers have three main disk areas: **home**, **projappl** and **scratch**.
In addition to these disk areas visible to all compute and login nodes, each node has a
**local temporary disk area** that is visible to the particular compute node during a batch
job or shell session, only. Please familiarize yourself with the areas and their specific
purposes. The disk areas for different supercomputers are separate, *i.e.* **home**,
**projappl** and **scratch** in Puhti cannot be directly accessed from Mahti. Also
[a more technical description of the Lustre filesystem](lustre.md) used in these directories
is available.

!!! warning "CSC does not backup your data!"
    None of the disk areas are automatically backed up by CSC! This means that data accidentally
    deleted by the user cannot be recovered in any way. To avoid unintended data loss, make sure
    to perform regular backups to, for example, [Allas](../data/Allas/index.md). See also the
    [allas-backup tool](../data/Allas/using_allas/a_backup.md).

|            |Owner   |Environment variable|Path                 |Cleaning                 |Automatic backup|
|------------|--------|--------------------|---------------------|-------------------------|----------------|
|**home**    |Personal|`${HOME}`           |`/users/<user-name>` |No                       |No              |
|**projappl**|Project |Not available       |`/projappl/<project>`|No                       |No              |
|**scratch** |Project |Not available       |`/scratch/<project>` |180 days on Puhti        |No              |

These disk areas have quotas for both the amount of data and total number of files:

|            |Capacity|Number of files|
|------------|--------|---------------|
|**home**    |10 GiB  |100 000 files  |
|**projappl**|50 GiB  |100 000 files  |
|**scratch** |1 TiB   |1 000 000 files|

!!! info "LUE"
    To easily check the amount of data and number of files within a given folder on
    the parallel file system, please consider using the [LUE](../support/tutorials/lue.md)
    tool. This tool is significantly faster than tools like `stat` or `du` and causes
    much less load on the file system.

!!! info "Quotas and cleaning"
    While it is possible to [apply for increased quotas](#increasing-quotas), we
    recommend that you always first ensure that the data you have stored on the
    shared file system is really needed and in active use. Unused data should be
    moved to e.g. [Allas](../data/Allas/index.md). A general tutorial on [managing
    and cleaning data on Puhti and Mahti disks](../support/tutorials/clean-up-data.md)
    is also available.

## Home directory

Each user has a home directory (`$HOME`) that can contain up to 10 GB of data.

The home directory is the default directory where you begin after logging in to CSC supercomputers.
However, typically you should change to your project's `scratch` directory when working because
the **home directory is not intended for data analysis or computing**. Its purpose is to store
configuration files and other minor personal data. A home directory exceeding its capacity
causes various account problems.

The home directory is the only user-specific directory in supercomputers. All other directories
are project-specific. If you are a member of several projects, you also have access to several
`scratch` or `projappl` directories, but still have only one home directory.

## Scratch directory

Each project has by default 1 TB of scratch disk space in the directory `/scratch/<project>`.

This fast parallel scratch space is intended as temporary storage space for the
data that is used in the supercomputer. The scratch directory is not intended
for long-term data storage. To ensure that the disks do not fill up CSC will
regularly delete files that have not been accessed in a long time. In Puhti the
current policy is to remove files that have not been accessed for more than 180
days (scratch quota less than 5 TiB) or 90 days (scratch quota 5 TiB or more).
In Mahti a similar cleaning procedure will be introduced, but is not yet
active. See [Usage policy](usage-policy.md#disk-cleaning) page for details on
the current policy.

Make sure to consult our tutorial for [tips and guidelines on how to
manage your data on `scratch`](../support/tutorials/clean-up-data.md).

## Projappl directory

Each project has also a 50 GB project application disk space in the directory
`/projappl/<project>`.

It is intended for storing compiled software binaries, source code, libraries
and small-scale reference data that are shared within a project. It is not a
personal storage space, but it is shared with all members of a project. Note
that no files in this folder will be removed automatically.

Please note that `projappl` quota is limited, and the disk area is not meant
for storing active research data. Thus, please do not submit jobs from or write
large-scale data to your project's `projappl` directory, but use `scratch`
instead for this purpose. Note that the self-installed applications you run
can and should still be stored in `projappl`.

## Using scratch and projappl directories

An overview of your directories in the supercomputer you are currently logged on can be
displayed with:

```bash
csc-workspaces 
```

The above command displays all `scratch` and `projappl` directories you have access to.
It also displays which of your projects are subject to the 90 day `scratch` cleaning
cycle and which to the 180 day `scratch` cleaning cycle.

For example, if you are a member in two projects, with unix groups `project_2000123`
and `project_2001234`, then you have access to two `scratch` and `projappl` directories:

```text
[kkayttaj@puhti-login11 ~]$ csc-workspaces 

Disk area               Capacity(used/max)  Files(used/max)  Cleanup
----------------------------------------------------------------------
Personal home folder

/users/kkayttaj                 4.4G/10G         24K/100K        n/a
----------------------------------------------------------------------
Project: project_2000123 "Project X"

/projappl/project_2000123        24G/50G         36K/100K        n/a
/scratch/project_2000123        103G/1.0T       389K/1.0M       180d
----------------------------------------------------------------------
Project: project_2001234 "Project Y"

/projappl/project_2001234        85G/100G       282K/600K        n/a
/scratch/project_2001234        7.2T/8.0T       2.7M/5.0M        90d
----------------------------------------------------------------------
```

Moving to the scratch directory of `project_2000123`:

```bash
cd /scratch/project_2000123
```

Please note that not all CSC projects have Puhti/Mahti access, so you may not
necessarily find a `scratch` or `projappl` directory for all your CSC projects.

!!! Note
    The `scratch` and `projappl` directories are shared by all the members of the
    project. All new files and directories are also fully accessible for other
    group members (including read, write and execution permissions).

If you want to restrict access from your group members, you can reset the permissions
with the `chmod` command. Setting read-only permissions for your group members for
the directory `my_directory`:

```bash
chmod -R g-w my_directory
```

As mentioned earlier, the `scratch` directory is only intended for processing data.
Any data that should be preserved for a longer time should be copied to the *Allas*
object storage server. Instructions for backing up files from CSC supercomputers to
Allas can be found in the [Allas guide](../data/Allas/index.md).

## Moving data between supercomputers

Data can be moved between supercomputers via Allas by first uploading the data in
one supercomputer and then downloading in another supercomputer. This is the
recommended approach if the data should also be preserved for a longer time.

Data can also be moved directly between the supercomputers with the `rsync` command.
For example, in order to copy `my_results` (which can be either file or directory)
from Puhti to the directory `/scratch/project_2002291` in Mahti, one can issue in
Puhti the command:

```bash
rsync -azP my_results yourcscusername@mahti.csc.fi:/scratch/project_2002291
```

See [Using rsync](../data/moving/rsync.md) for more detailed instructions for `rsync`.

## Increasing quotas

You can use the **MyCSC portal** to [manage quotas of the `scratch` and `projappl`
directories](../accounts/how-to-increase-disk-quotas.md).

Remember that even after the quota is increased, the planned automatic cleaning process
will continue removing idle files from the `scratch` directory. Data that is not under
active computing should be stored in the Allas storage service.

Remember also that you can increase these values only to some extent. Especially regarding
the number of files, you should reconsider your data workflow if it requires that tens
of millions of files are stored in the `scratch` area.

!!! info
    To find out how much data/files you have on the disk, please use our [LUE
    tool](../support/tutorials/lue.md) which is much more performant than standard
    tools such as `stat` or `du`.

## Temporary local disk areas

If the application depends on the use of temporary files, the suitability of
the filesystem may have a large effect on the performance of the application,
see section *Mind your I/O - it can make a big difference* in the [Performance
checklist](running/performance-checklist.md#mind-your-io-it-can-make-a-big-difference).

Please note that some applications use temporary files "behind the scenes". Usually these
applications read some environment variable that points to a suitable disk area, such as
`$TMPDIR`.

Some nodes have local disks that can be used to speed up your work when the temporary files
are only needed within a single login- or compute node.

### Login nodes

Each of the login nodes have 2900 GiB of fast local storage. The storage is located under
`$TMPDIR` and is separate for each login node.  

The local storage is good for compiling applications and performing pre- and post-processing
that require heavy I/O operations, for example packing and unpacking archive files.

!!! Note
    The local storage is meant for **temporary** storage and is cleaned frequently.
    Remember to move your data to a shared disk area after completing your task.

### Compute nodes with local SSD (NVMe) disks

Jobs running in the I/O- and GPU-nodes in Puhti and Mahti have local fast storage
available. In interactive batch jobs launched with [sinteractive](running/interactive-usage.md),
this local disk area is defined with environment variable `$TMPDIR` and in normal batch jobs
with `$LOCAL_SCRATCH`. The size of this storage space is defined in the batch job resource request.
Different nodes have different amounts of disks, see [Puhti technical details](systems-puhti.md)
for a detailed list of all node types in Puhti. In normal compute nodes, there are 1490 GiB and 3600 GiB
disks. In big memory nodes there are 1490 GiB and 5960 GiB disks, and in GPU-nodes there are
3600 GiB disks. To save resources, and to ensure your jobs do not queue for resources for too
long, it is a good idea to only reserve what you actually need. In Mahti there are 60 CPU nodes with 3500 GiB
local disks in the `small` and `interactive` partitions. The GPU nodes have 3600 GiB local disks.

These local disk areas are designed to support I/O intensive computing tasks and cases where you
need to process large amounts (over 100 000) of small files. These directories are cleaned once
the batch job finishes. Thus, in the end of a batch job you must copy all the data that you want
to preserve from these temporary disk areas to `scratch` directory or to Allas.

For more information see [creating job scripts](running/creating-job-scripts-puhti.md#local-storage).

### Compute nodes without local SSD (NVMe) disks

In Puhti we simply recommend using compute nodes with NVMe disks (`$LOCAL_SCRATCH`) for the
applications that require temporary local storage.

In Mahti, where only some compute nodes have local NVMe disks, it is also possible to store a relatively
small amount of temporary files in memory. In practice, the applications can use the directory
`/dev/shm` for this, for example by setting `export TMPDIR=/dev/shm`. Please note that the use
of `/dev/shm` consumes memory, so less is left available for the applications. This may lead to
applications running out of memory sooner than expected and failing in the compute node, but
this usually does no other harm. The plus side is that if it works, it should be fast.

However, in Puhti, as well as Mahti `small`, `interactive` and GPU partitions, where applications
from multiple users can share the same node, running out of memory by filling up `/dev/shm` will
crash other users applications, too! **In these cases it is not recommended to use `/dev/shm` at all.**
