# Lustre file system

CSC supercomputers use [Lustre](https://www.lustre.org/) as the parallel distributed file system.
This article provides a brief technical description of Lustre.

## Lustre architecture

Lustre separates file data and metadata into separate
services. **Data** is the actual contents of the file, while
**metadata** includes information like file size, permissions, access
date etc.

The Lustre file system consists of a set of I/O servers called Object
Storage Servers (OSSs) and disks called Object Storage Targets (OSTs)
which store the actual data. The metadata of a file are controlled by
Metadata Servers (MDSs) and stored on Metadata Targets
(MDTs). Basically, the servers handle the requests for accessing the
file contents and metadata; the applications do not access disks
directly. Lustre systems use typically multiple OSSs/MDSs together
with multiple OSTs/MDTs to provide parallel I/O capabilities.

* *Object Storage Servers* (OSSs): They handle requests from the clients
  in order to access the storage. Moreover, they manage a set of OSTs;
  each OSS can have more than one OST to improve the I/O parallelism.
* *Object Storage Targets* (OSTs): Usually, an OST consists of a block of
  storage devices under RAID configuration. The data is stored in one or more
  objects, and each object is stored on a separate OST.
* *Metadata Server* (MDS): A server that tracks the locations for all the
  data so it can decide which OSS and OST will be used. For example, once a
  file is opened, the MDS is not involved any more.
* *Metadata Target* (MDT): The storage contains information about
  the files and directories such as file sizes, permissions, access
  dates. For each file MDT includes information about the layout of
  data in the OSTs such as the OST numbers and object identifiers.

!["Schematic picture of compute nodes accessing OSTs and MDTs via OSS and DST servers via network. The acronyms and relations are explained also in the text."](../img/lustre.png 'Lustre file system view')

*Lustre file system view*

Lustre is designed for efficient parallel I/O for large
files. However, when dealing with small files and intensive metadata
operations, the MDS/MDT can become a bottleneck. For example, when a
user opens/closes a file many times in a loop, the workload on
MDT increases. When several users do similar operations, the metadata
operations can slow down the whole system and influence many users. As login
and compute nodes share the file system, this can show up even as slow
editing of files in a login node. Also, if in a parallel application
the different processes perform a lot of operations on the same small
files, metadata operations can slow down. Innocent looking Linux
commands can also increase metadata workload: for example `ls -l`
prints out file metadata, and giving the command in a directory with
lots of files causes many requests to MDS.

## File striping and alignment

In order to gain from parallel I/O with Lustre, the data should be
distributed across many OSTs. The distribution across many OSTs is
called **file striping**. Logically, a file is a linear sequence of
bytes. In file striping, the file is split in chunks
of bytes that are located on different OSTs, so that the read/write
operations can be performed concurrently.

Striping can increase the bandwidth available for accessing files,
however, there is also an overhead due to increase in network
operations and possible server contention. Thus, striping is normally
beneficial only for large files.

As the supercomputers have many more nodes than OSSs/OSTs, the I/O
performance can vary a lot depending on the I/O workload of the whole
supercomputer.

In a parallel program, performance is improved when each parallel process
accesses a different stripe of a file during parallel I/O. Moreover, in order
to avoid network contention each process should access as few OSTs/OSSs as
possible. This can be achieved through stripe alignment. Best
performance is obtained when the data is distributed uniformly to
OSTs, and the parallel processes access the file at offsets that
correspond to stripe boundaries.

!["Schematic showing a file split into chunks and each stored in a different OST."](../img/file_striping.png 'Lustre file striping and alignment')

*Lustre file striping and alignment*

If in the above example, we had a file of 5 MB, then the OST 0 would
have an extra 1 MB of data. If the data would be distributed evenly
between four processes, each process would have 1.5 MB and the access
would not be stripe aligned: first process needs to access OST 0 and
1, next process OST 1 and 2, *etc.* processes are not aligned. This
could now cause network contention issues.

### Controlling striping

The default stripe size in CSC's Lustre is 1 MB and stripe count is 1,
i.e. by default the files are not striped. Stripe settings can be,
however, changed by user which can at best improve the I/O performance
a lot.

The stripe settings for a file or directory can be queried with the
`lfs getstripe` command

```
lfs getstripe my_file
```
which prints out:
```
my_file
lmm_stripe_count:  2
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    0
lmm_stripe_offset: 11
    obdidx         objid        objid         group
        11      29921659    0x1c8917b             0
        20      29922615    0x1c89537             0

```
The output shows that the file is distributed over two OSTs (stripe
count 2), output also shows that the particular OSTs are 11 and 20.

For a directory, the output shows the settings that will be used for
any files to be created in the directory.

Stripe configuration can be set with the `lfs setstripe` command. In
most cases, it is enough to set the stripe count with the `-c`
option, however, also other options can be set, see e.g. `man
lfs-setstripe` or [Lustre
wiki](https://wiki.lustre.org/Configuring_Lustre_File_Striping).

```
mkdir experiments
lfs setstripe -c 4 experiments
touch experiments/new_file
```
Executing now `lfs getstripe experiments/new_file` outputs:
```
experiments/new_file
lmm_stripe_count:  4
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    0
lmm_stripe_offset: 6
    obdidx         objid        objid         group
         6      29925064    0x1c89ec8             0
         1      29925258    0x1c89f8a             0
        19      29926834    0x1c8a5b2             0
        15      29921764    0x1c891e4             0

```

!!!! Note If the file is already created with a specific stripe, you
     can not change it. Also, if you move a file, its stripe settings will not
     change. In order to change striping, file needs to be copied:

* using `setstripe`, create a new, empty file with the desired stripe settings
  and then copy the old file to the new file, or
* setup a directory with the desired configuration and copy (not move) the
  file into the directory.

## Differences between Puhti and Mahti

Puhti and Mahti have similar storage areas
[home](disk.md#home-directory), [project](disk.md#projappl-directory)
and [scratch](disk.md#scratch-directory), however, their the Lustre
configuration is not the same.

|  Name       | Puhti  |        | Mahti  |        |
|-------------|--------|--------|--------|--------|
|**Disk area** | **# OSTs** | **# MDTs** | **# OSTs** | **# MDTs** |
| home        |  24    |   4    |    8    |   1    |
| projappl    |  24    |   4    |    8    |   1    |
| scratch     |  24    |   4    |   24    |   2    |


One main difference is that for Mahti there are separate MDTs between
`scratch`, `home`, and `project`, thus the metadata performance does
not interfere from the different file systems. Moreover, the `scratch` on
Mahti can have better performance than the other storage areas if your
application and the data size is big enough because of more OSTs and MDTs. On
Puhti, all the OSTs and MDTs are shared across the storage areas, thus the
performance should be similar between them.

The peak I/O performance for Mahti is around to 100 GB/sec for write
and 115 GB/sec for read. However, this performance was achieved on
dedicated system with 64 compute nodes, which means around to 1.5
GB/sec per compute node. If more nodes are used or many jobs do
significant I/O, then you will not achieve 1.5 GB/sec, including also
that maybe the I/O pattern of an application is not efficient. The
corresponding performance for Puhti is half of that of Mahti.

## Best practices

* If possible, avoid using `ls -l` as the information on ownership and
  permission metadata is stored on MDTs, the file size metadata is available
  from OSTs. Use `ls` instead if you do not need the extra information.

* Avoid saving a large number of files in a single directory, better to split
  in more directories.

* If possible, avoid accessing a large number of small files on Lustre.

* Make sure that the stripe count for small files is 1.

* If an application opens a file for reading, then open the file in read mode
  only.

* Increase striping count for parallel access, especially on large files:
    * The striping factor should be a factor of the number of used processes
      performing parallel I/O
    * A rule of thumb is to use as striping the square root of the file size
      in GB. If the file is 90 GB, the square root is 9.5, so use at least 9
      OSTs.
    * If you use, for example, 16 MPI processes for parallel I/O, the number
      of the used OSTs should be less or equal to 16.

For more details, please consult our [Lustre performance
optimization tutorial](../support/tutorials/lustre_performance.md).
