# Managing data on Puhti and Mahti scratch disks

An important task for all users on Puhti and Mahti is to manage what data resides in project folders in `scratch`. These are only intended as temporary storage space for data that is in active use. All other data should be removed, or stored in other more suitable storage systems. Users are not expected to use all of their quota, the maximum quota is only meant for short term bursts. 

Also note that:

 * A Lustre parallel file system starts to lose performance when more than approximately 70% of disk space is used, and the more the disks fill up, the slower the performance will get. CSC has allocated more quota than there is space, hence it is not even possible for all users to use their `scratch` folders for longer term storage. 
 *  There are no backups of `scratch` disk area. Do not trust it to store all of your research data.
 *  Removing files decreases the BU consumption of your project, since you are billed for disk usage and not quota as before 2022. 

We kindly ask all users to help to keep disk usage manageable, and performance reasonable. Please do the following tasks:

* **Remove files** that are not needed anymore in your project's `scratch` folder. Note that we cannot bring back files that you delete by mistake so do these operations carefully!
* **Compress files** if it reduces file size. Ascii text files usually compress very well. Test with one file first. If the file size drops by 50%, go ahead and compress all similar files.
* **Move files** not in active use now, but that need to be available later during the project. The typical model is to move the files to 
[Allas](../../data/Allas/index.md). We recommend to use [a-tools](../../data/Allas/using_allas/a_commands.md) for small to medium sized data transfers, in particular when you have a large amount of small files.  These tools make the usage of Allas safer, and can make your data management easier. For very large data transfers we recommend using [rclone](../../data/Allas/using_allas/rclone.md). A tutorial for data transfer is available at [allas-examples](../../data/Allas/allas-examples.md).
* **Archive files** that should be available longer than the lifetime of compute projects. Options for this can be for example your organizations own storage systems, or [IDA safe storage for research data](https://www.fairdata.fi/en/).


## Identifying where you have data

If you have a large amount of files, analyzing how much data you have in different folders can be time consuming and also heavy on the file system. Our recommendations for tools that can show the amount of data in folders:

* **Avoid** using `find` options like `-size` or similar
* **Avoid** using `du`
* **Do** use `lue` or `lfs find --lazy`

CSC has developed an approximate tool called LUE (Lustre usage explorer) for reporting amount of data in folders. [Read the documentation at LUE](../../support/tutorials/lue.md) before using it. `lfs find --lazy` has some edge-case where it can be as bad as `du` or silently fail to get correct size information. Run `man lfs-find` for further instructions and information on its limitations.

!!! Note
    No matter what tool you use you should never try to list or process all files in your project or `scratch` folder with a single command. Instead you should run commands on specific subdirectories with limited amount of files and data. The total amount of used data is available from the `csc-workspaces` command.

## Future automatic removal of files

There is a policy of removing files older than 90 days from `scratch` (not `projappl`) to ensure that only actively used data resides on the disk. **This policy has not yet been implemented, but we plan to take this cleaning procedure in use later in 2022**. Before we take it in use we will warn you and give instructions for how to manage what files are affected.



