# Managing data on supercomputer scratch disks

An important task for all users on CSC supercomputers is to manage what data resides in project
folders in `scratch`. These are only intended as temporary storage space for data that is in
active use. All other data should be removed, or stored in other more suitable storage systems.
Users are not expected to use all of their quota, the maximum quota is only meant for
short-term bursts.

Also note that:

* A Lustre parallel file system starts to lose performance when more than approximately 70% of
  disk space is used, and the more the disks fill up, the slower the performance will get.
  CSC has allocated more quota than there is space, hence it is not even possible for all users
  to use their `scratch` folders for longer term storage.
* There are **no backups** of `scratch` disk area. Do not trust it to store all of your research data.
* Removing files decreases the Storage BU consumption of your project, since `scratch`
  usage is [billed](../../computing/hpc-billing.md#storage) per TiB-hour.

We kindly ask all users to help to keep disk usage manageable, and performance reasonable.
Please do the following tasks:

* **Remove files** that are not needed anymore in your project's `scratch` folder.
  Note that we cannot bring back files that you delete by mistake so do these operations carefully!
* **Compress files** if it reduces file size. Ascii text files usually compress very well.
  Test with one file first. If the file size drops by 50%, go ahead and compress all similar files.
  [See here for available compression tools](env-guide/packing-and-compression-tools.md).
* **Move files** not in active use now, but that need to be available later during the project.
  The typical model is to move the files to [Allas](../../data/Allas/index.md).
  We recommend to use [a-tools](../../data/Allas/using_allas/a_commands.md) for small to
  medium sized data transfers, in particular when you have a large amount of small files.
  These tools make the usage of Allas safer, and can make your data management easier.
  For very large data transfers we recommend using [rclone](../../data/Allas/using_allas/rclone.md).
  A tutorial for data transfer is available at [Allas HPC tutorial](../../data/Allas/allas-roihu.md).
* **Archive files** that should be available longer than the lifetime of compute projects.
  Options for this can be for example your organizations own storage systems, or
  [IDA safe storage for research data](https://www.fairdata.fi/en/).

## Identifying where you have data

If you have a large amount of files, analyzing how much data you have in different folders can
be time consuming and also heavy on the file system. Our recommendations for tools that can
show the amount of data in folders:

* **Avoid** using `find` options like `-size` or similar
* **Avoid** using `du`
* **Do** use `lue` or `lfs find --lazy`

CSC has developed an approximate tool called LUE (Lustre usage explorer) for reporting amount of
data in folders. [Read the documentation at LUE](../../support/tutorials/lue.md) before using it.
`lfs find --lazy` has some edge-case where it can be as bad as `du` or silently fail to get correct
size information. Run `man lfs-find` for further instructions and information on its limitations.

!!! Note
    No matter what tool you use you should never try to list or process all files in your project
    or `scratch` folder with a single command. Instead you should run commands on specific
    subdirectories with limited amount of files and data. The total amount of used data is
    available from the `csc-workspaces` command.

## Automatic removal of files

There is a [policy](../../computing/usage-policy.md#disk-cleaning) of removing files
older than **180 days** (`scratch` quota less than 5 TiB) or **90 days** (`scratch` quota
5 TiB or more) from `scratch` (not `projappl`) to ensure that only actively used data
resides on the disk.

Files that will be deleted in the next clean up are listed in so called "purge lists" files.
These are split up by project, and can be found on Lustre at one of the locations below.
Only members of the project groups can access the project directories.
If your project is newly created, your project might not yet have its own subdirectory in
the `purge_lists` directory, in which case it won't participate in the automatic cleaning.

* `/scratch/purge_lists/<PROJECT NAME>/path_summary.txt`

In case the `path_summary.txt` file does not exist, your project did not have any files that matched
the clean-up criteria, and thus nothing will be deleted from it. To indicate that the file is
intentionally missing, CSC will place a file named `nothing-to-remove-for-your-project` in your
project's purge_lists subdirectory, so check for the existence of this file as well.

As part of the automated cleaning process, the files will change names. Before the cleaning has
begun, each project that is part of the clean-up will have a file named `path_summary.txt`.
In special cases where a project is exempt from the upcoming cleaning, or requires more time to
transfer files, the administrators will rename the file to something else, usually
`path_summary.txt-later-delete`. Once a project has been processed by the automated cleaning,
the file will be renamed to `path_summary.txt-stashed`. These files are still readable to projects,
so that it is possible to refer to the list also after the cleaning is performed.
The previous round's files will be archived when the next round of cleaning is about to begin.
You can check whether your project's purge list has been updated recently by checking its last
modification date. In the example below, the file is a few months old, so it is clearly from
the prior round of cleaning:

```bash
$ stat -c %y /scratch/purge_lists/project_2001659/path_summary.txt-stashed
2023-05-23 00:35:28.000000000 +0300
$ date +%F
2023-08-04
```

Another file which is put into each project's `purge_lists` directory is the `total_size.txt` file.
This file contains a precalculated size estimate based on the numbers inside the `path_summary.txt`
files. This file exists for every project, and is created automatically when the purge lists are
generated. The file might look like this:

```bash
$ cat /scratch/purge_lists/project_2001659/total_size.txt
Total size: 798343125192 bytes = 743.515 GiB = 0.726 TiB
```

With this information, you are able to estimate how much time might be required to back up the
data elsewhere, if you want to keep everything on the purge list outside of the `scratch` file
system.
