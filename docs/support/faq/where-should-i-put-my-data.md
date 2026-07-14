# Where should I put my data?

The Roihu supercomputer uses a parallel file system called
*Lustre*. Data on Lustre is accessible from all nodes of a system, and is thus
the best place to store the data that you need for computations. Please note
that you can not directly access data on Roihu from Mahti or vice versa, i.e.
they have their own Lustre file systems. You can, however, move data between
Roihu and Mahti using tools such as [rsync](../../data/moving/rsync.md).

See the [detailed data migration guide](../tutorials/roihu-data.md) from Mahti and Puhti to Roihu.

More specifically, Roihu has three main disk areas: *home*,
*projappl* and *scratch*. The home directory (accessible using the `$HOME`
environment variable) is the only user-specific directory. The other
directories scratch and projappl are project-based and shared by all members of
a project. You can access them at `/scratch/<project>` and
`/projappl/<project>`, respectively, where `<project>` should be replaced by
the actual ID of your CSC project (see
[How to find information about my projects](./how-to-find-information-about-projects.md)).
This also means that if you are a member of several projects, you also have
access to multiple scratch and projappl directories. You will, however,
only have one home directory.

| What do you need? | Recommended location |
|---|---|
| Temporary input, output and intermediate data for one computational project | `/scratch/<project-id>` (Roihu) |
| Software, scripts and small reference files shared within one computational project | `/projappl/<project-id>` (Roihu) |
| One actively used dataset that several Roihu computational projects need to read | `/dataset/<dataset-project-id>` (Roihu) |
| Backups, inactive data or longer-term object storage | Allas or LUMI-O |
| Published or preserved research data | An appropriate research data repository or preservation service |

The `/dataset` directory is not included in a normal computational project in Roihu.
To use it, apply for a separate
[Roihu dataset project](../../computing/roihu-dataset-project.md).

When logging in to Roihu, you should change to your project's
scratch directory because the home directory is not intended for storing data
that is required for analysis or computing. Its purpose is to store
configuration files and other **minor** user-specific data (default quota 10
GB). A directory exceeding its capacity causes various problems (see
[Disk quota exceeded](disk-quota-exceeded.md)). The scratch disk is the main
disk area to store your active research data (default quota 250 GB on Roihu), while
projappl is intended, for example, for project-wide installations of custom
software and libraries (default quota 15 GB on Roihu). See
[more information about the disk areas](../../computing/roihu-disk.md).

!!! note "CSC does not back up your data!"
    None of the disk areas are automatically backed up by CSC. This means that
    data accidentally deleted by the user cannot be recovered in any way. Also
    keep in mind that files on the scratch disk that have not been used in 180
    days will be automatically deleted.
    
    To avoid unintended data loss, please move files that are not in active use
    away from scratch and remember to take regular backups of your important
    data to, for example, Allas or your own organization's storage systems.

One of the main use cases of [Allas](../../data/Allas/index.md) is to store
data that is not in active on the CSC supercomputers. Before working on the
data on an HPC system, copy it from Allas to the supercomputer (*stage in*).
When the data is no longer actively used it can be *staged out*, i.e. uploaded
back to Allas.

Read more about
[common use cases of Allas](../../data/Allas/using_allas/common_use_cases.md)
and see the
[example of hosting a dataset](../../data/Allas/allas_project_example.md).
