# Roihu disk areas

Roihu provides three main shared disk areas: **home**, **projappl**, and **scratch**.
In addition, each compute node provides a local temporary disk area that
is available only during a job or interactive session on that node.
Please familiarize yourself with the areas and their specific
purposes.

Roihu users can also apply for separate dataset projects.
These provide access to a dedicated disk area, **projdata**, intended for sharing
datasets between multiple projects. Unlike computational projects, dataset projects
do not include `scratch` or `projappl` directories.

These directories are shared across the login and compute nodes on the system, and are based on the Lustre filesystem.
See [a more technical description of the Lustre filesystem on CSC supercomputers](lustre.md).

!!! warning "CSC does not backup your data!"
    None of the disk areas are automatically backed up by CSC! 
    Deleted files **cannot be recovered**. To avoid unintended data loss, make sure
    to perform regular backups to, for example, [Allas](../data/Allas/index.md). See also the
    [allas-backup tool](../data/Allas/using_allas/a_backup.md).

|             |Owner   |Environment variable|Path                  |Cleaning             |Automatic backup|
|-------------|--------|--------------------|----------------------|---------------------|----------------|
|**home**     |Personal|`${HOME}`           |`/users/<user-name>`  |No                   |No              |
|**projappl** |Project |Not defined         |`/projappl/<project>` |No                   |No              |
|**scratch**  |Project |Not defined         |`/scratch/<project>`  |180 days             |No              |
|**projdata** |Project |Not defined         |`/projdata/<project>` |No                   |No              |

These disk areas have quotas for both the amount of data and total number of files:

|            |Capacity|Number of files|Notes                         |
|------------|--------|---------------|------------------------------|
|**home**    |15 GiB  |150 000 files  |                              |
|**projappl**|15 GiB  |150 000 files  |                              |
|**scratch** |250 GiB |500 000 files  |                              |
|**projdata**|0 GiB   |0 files        |Must be applied for separately|

!!! info "LUE (not implemented 2026-04-22)"
    To easily check the amount of data and number of files within a given folder on
    the parallel file system, please consider using the [LUE](../support/tutorials/lue.md)
    tool. This tool is significantly faster than tools like `stat` or `du` and causes
    much less load on the file system.

!!! info "Quotas and cleaning"
    While it is possible to [apply for increased quotas](#increasing-quotas), we
    recommend that you always first ensure that the data you have stored on the
    shared file system is really needed and in active use. Unused data should be
    deleted or moved to e.g. [Allas](../data/Allas/index.md). A general tutorial on [managing
    and cleaning data on Puhti and Mahti disks](../support/tutorials/clean-up-data.md)
    is also available.

## Home directory

Each user has a home directory (`$HOME`) that can contain up to 15 GB of data on Roihu.

The home directory is the default location after logging in.
However, it is not intended for data analysis or running jobs.
Its purpose is to store configuration files and other minor personal data.
Be wary of the remaining quota in your home directory,
a home directory exceeding its capacity can cause various account problems.

The home directory is the only user-specific directory in supercomputers. All other directories
are project-specific. If you are a member of several projects, you also have access to several
`scratch` or `projappl` directories, but still have only one home directory.

For all computing work, you should use your project's `scratch` directory.

## Scratch directory

Each project on Roihu has, by default, 250 GiB of scratch disk space in the
directory `/scratch/<project>`.

The scratch directory is a fast parallel filesystem intended temporary storage of
data used in computation, and should contain i.e. any input and output files of your
programs. 
You should aim to run your jobs on the supercomputer in this `scratch` directory.

The scratch directory is **not intended for long-term storage**. Files that have not 
been accessed for a long time may be automatically removed to free up space.
The current policy on Roihu is to remove files that have not been accessed for
more than 180 days.

Make sure to consult our tutorial for [tips and guidelines on how to
manage your data on `scratch`](../support/tutorials/clean-up-data.md).

## Projappl directory

Each project on Roihu has also a 15 GB project application disk space
in the directory `/projappl/<project>`.

Use the projappl area for storing compiled software binaries, source code, libraries, scripts
and small-scale reference data that are shared within a project. It is not a
personal storage space, as it is shared with all members of a project.
Files in projappl are not automatically removed, but the quota is limited.

Please do not submit jobs from or write
large-scale data to your project's `projappl` directory, but use `scratch`
instead for this purpose. Note that any self-installed applications you run
can and should still be stored in `projappl`.


## Using scratch and projappl directories

An overview of your directories in the supercomputer you are currently logged on can be
displayed with:

```bash
csc-workspaces 
```

The above command displays all `scratch` and `projappl` directories you have access to.
It also displays which of your projects are subject to the 180 day `scratch` cleaning cycle.

For example, if you are a member in two projects, with unix groups `project_2000123`
and `project_2001234`, then you have access to two `scratch` and `projappl` directories:

```text
[kkayttaj@roihu-login11 ~]$ csc-workspaces 

Disk area               Capacity(used/max)  Files(used/max)  Cleanup
----------------------------------------------------------------------
Personal home folder

/users/kkayttaj                 4.4G/15G         24K/150K        n/a
----------------------------------------------------------------------
Project: project_2000123 "Project X"

/projappl/project_2000123        24G/15G         36K/150K        n/a
/scratch/project_2000123        103G/250G       389K/500k        180d
----------------------------------------------------------------------
Project: project_2001234 "Project Y"

/projappl/project_2001234        25G/100G       282K/1.0M       n/a
/scratch/project_2001234         7.2/10TB       2.1M/2.5M       180d
----------------------------------------------------------------------
```

Moving to the scratch directory of `project_2000123`:

```bash
cd /scratch/project_2000123
```

Note that not all CSC projects have Roihu access, so you may not
necessarily find a `scratch` or `projappl` directory for all your CSC projects.

!!! Note
    The `scratch` and `projappl` directories are shared by all the members of the
    project. All new files and directories are also fully accessible for other
    group members (including read, write and execution permissions) by default.

If you need to restrict access from your group members, you can reset the permissions
with the `chmod` command as usual. In general, we recommend that you allow the group
members the access, but use a subdirectory with your username for your data, for example

```
/scratch/project_2000123/$USER
```

This way the data is accessible to other group members in case of long vacations, etc,
but the ownership is still clear and organized. Note, some programs change the file permissions
from the defaults, which may restrict the access from group members.

As mentioned earlier, the `scratch` directory is only intended for processing data.
Any data that should be preserved for a longer time should be copied to the *Allas*
object storage server. Instructions for backing up files from CSC supercomputers to
Allas can be found in the [Allas guide](../data/Allas/index.md).

## Projdata directory

Roihu users can apply for separate dataset projects, which provide access to shared disk
area under `/projdata/<project>`, but no computational resources.

Unlike normal computational projects, dataset projects do not include scratch or projappl
directories. Instead, they are designed specifically for sharing data between multiple
projects.

Write access to a projdata directory is restricted to a single project, while multiple
other projects can be granted read access to this disk area.

!!! note
     Dataset projects are intended for data sharing and active use, not long-term storage.</br>
     For long term storage, consider using [Allas](../data/Allas/index.md).

## Moving data between supercomputers

Data can be moved directly between supercomputers using
[rsync](../data/moving/rsync.md) command.

See our [data migration guide](../support/tutorials/roihu-data.md) for migrating data
from Puhti/Mahti to Roihu.

## Increasing quotas

You can use the **MyCSC portal** to [manage quotas of the `scratch` and `projappl`
directories](../accounts/how-to-increase-disk-quotas.md).

Remember that even after the quota is increased, the planned automatic cleaning process
will continue removing idle files from the `scratch` directory. Data that is not under
active computing should be stored in the Allas storage service.

Quota increases are limited. If your workflow requires storing very large
numbers of files (e.g. millions), you should reconsider your data workflow,
as this can lead to performance issues on the whole filesystem.

!!! info
    To find out how much data/files you have on the disk, please use our [LUE
    tool](../support/tutorials/lue.md) (not implemented 2026-04-22) which is much more performant than standard
    tools such as `stat` or `du`.

## Temporary local disk areas

Roihu compute nodes provide fast local disk storage that can significantly improve 
performance for I/O-intensive workloads.

This storage is available via the environment variable `$TMPDIR`, which many
applications use automatically for temporary files.

Local disk is node-specific and available on the login node, as well as in a job
or interactive session. It is intended for temporary files that do not need to be
shared between nodes.

### Login nodes

Each login node on both Roihu-CPU and Roihu-GPU provides 80 GB of local storage under `$TMPDIR`.

The local storage is intended for compiling applications and performing pre- and post-processing
that require heavy I/O operations, for example packing and unpacking archive files.

!!! Note
    The local storage is meant for **temporary** storage and is cleaned frequently.
    Remember to move your data to a shared disk area after completing your task.

### Compute nodes

All compute nodes in Roihu provide fast NVMe local storage.

These local disk areas are designed to support I/O intensive computing tasks and cases where you
need to process large amounts (over 100 000) of small files.

Data in local storage is removed when the job finishes. You must copy any results you want to
keep to `scratch` or Allas before the job ends.

Based on your [Slurm job reservation](running/batch-job-partitions.md) type, you will have access
to the following amount of local disk space:

| Allocation type           | Quota per user |
|:--------------------------|---------------:|
| R (Shared nodes)          | 20 GiB         |
| N (Full nodes)            | 600 GiB        |
| G (GPU nodes)             | 150 GiB        |
| XL (Hugemem nodes)        | 1.6 TiB        |
| VIZ (Visualization nodes) | 6.5 TiB        |

The disk space can be accessed under `$TMPDIR`, and does not need to be separately reserved in
your job script to be usable. Using the local disk does not consume [billing units](../accounts/billing.md).
