# Lustre filesystem

Both systems Puhti and Mahti have Lustre, a parallel distributed file system, with some differences in their configuration between the systems.


## Lustre Terminology

The Lustre file system is constituted by a set of I/O servers called Object Storage Servers (OSSs) and disks called Object Storage Targets (OSTs). The metadata operations of a file are controlled by Metadata Servers (MDSs) and stored on Metadata Targets (MDTs). Basically, the servers handle the RPC requests in order to access the files and metadata; the clients do not access storage directly. Each OSS/MDS export multiple OST/MDT in oder to improve the I/O parallelism

* Object Storage Servers (OSSs): They handle RPC requests from the clients in order to access the storage. Moreover, they manage a set of OSTs; each OSS has more than one OST to improve the I/O parallelism
* Object Storage Targets (OSTs): Usually an OST consists of a block of storage devices under RAID configuration. The data are stored in one or more objects, and each object is stored on a separate OST. 
* The Metadata Server (MDS): A server that tracks the locations for all the data so it can decide which OSS and OST will be used. For example, once a file is opened, the MDS is not involved anymore.
* The Metadata Target (MDT): The storage contains information about the data, filenames, permissions, directories, etc. Each file on MDT includes a layout such as the OST number, object identifier.

!["Lustre file system view"](../../img/lustre.png)

*Lustre file system view*

Hint: When a user opens/close a file many times in a loop during the execution of an application, then the workload on MDT increases. When many users do similar approach, then the metadata could be slow and influence many more users, even to be slow edit a file from a login node. Be cautious when you develop your application.

## File striping and alignment

In order to gain from the Lustre performance, your data should be distributed across many OSTs. The distribution across many OSTs is called file striping. During file striping, a file is split in chunks of bytes and are located on different OSTs, so that the read/write operations to perform faster. The default stripe size is 1 MB on our Lustre. As we use the network during file striping, depending on the workload of OSSs and OSTs, the performance is not always as expected. It is important that each process access different stripe of a file during parallel I/O, this can be achieved through stripe alignment. This is the procedure where a process access the file at offsets of the stripe boundaries. Moreover, an MPI process is better to access as less OSTs/OSSs as possible to avoid network contention. When the stripes are aligned then can be uniform distributed on each OST. 

!["Lustre file striping"](../../img/file_striping.png)

*Lustre file striping and alignment*

If in the above example, we had a file of 5 MB, then the OST 0 would have an extra 1 MB of data. If the processes are not aligned then a process could have to access more than one OST and cause network contention issues. 

### Example set stripe equal to 4

```
mkdir experiments
lfs setstripe -c 4 experiments
```

Hint 1: In case you want all the files of a folder to have a new striping, change the striping to an empty folder. The files that are already located in a folder will not change their striping. 

Hint 2: If your application reads/writes only small files, do not increase the striping.



## Differences between Puhti and Mahti systems


It is known from our guide that both Puhti and Mahti have the storage areas Puhti [home](./../disk.md#home-directory), [project](./../disk.md#projappl-directory) and [scratch](./../disk.md#scratch-directory). However, the Lustre configuration, is not the same between them. 

|             |Puhti   |        | Mahti   |        |
|-------------|--------:|--------|--------:|--------|
|**Storage area** | **# OSTs** | **# MDTs** | **# OSTs** | **# MDTs** |
| home        |  24    |   4    |    8    |   1    | 
| projappl    |  24    |   4    |    8    |   1    |
| scratch     |  24    |   4    |   24    |   2    |


|             |Mahti   |        |
|-------------|--------|--------|
|**Storage area** | **# OSTs** | **# MDTs** |
| home        |   8    |   1    |   
| projappl    |   8    |   1    |
| scratch     |  24    |   2    |



One main difference is that for Mahti there are separate MDTs between `scratch`, `home`, and `project`, thus the performance does not interfere from the different filesystems. Moreover, the `scratch` on Mahti can have better performance than the other storage areas if your application and the data size is big enough because of more OSTs and MDTs. On Puhti, all the OSTs and MDTs are shared across the storage areas, thus the performance should be similar between them.

The peak performance for Mahti when it was one signle filesystem and not as it is now configured, it was around to ~100 GB/s for read or write and using 64 compute nodes. This performance is under dedicated access to the system, handling one file per process, not for single shared file. The performance for Puhti is around two times less than Mahti.



## Best practices 

* If possible, avoid using `ls -l` as the information on ownership and permission metadata is stored on MDTs, the file size metadata is available from OSTs. Use `ls` instead if you do not need the extra information.

* Avoid saving a large number of files in a single directory, better to split in more directories.

* If possible, avoid accessing a large number of small files on Lustre

* If an application opens a file for reading, then open the file in read mode only


Increase striping count for parallel access, especially on large files:
* The striping factor should be a factor of a number of processes performing parallel I/O
* A rule of thumb is to use as striping the square root of the file size in GB. If the file is 90 GB, the square root is 9.5, so use at least 9 OSTs.
* If you use for example, 16 MPI processes for parallel I/O, the number of the used OSTs should be less or equal to 16.

* There is no need to stripe in a case of one file per MPI process 

* How to increase the stripping of a file or a directory to 16:

```
lfs setstripe -c 16 filename
```

* If the file is already created with a specific stripe, you can not change its stripe. Then copy the older file to the new one. Also, if you copy a file under a new striped folder, the file will get the new stripe. If you move a file under a folder, its stripe will not change.


* How to check the stripping of a file or a directory

```
lfs getstripe filename

path/filename
lmm_stripe_count:  24
lmm_stripe_size:   1048576
lmm_pattern:       raid0
lmm_layout_gen:    0
lmm_stripe_offset: 22
	obdidx		 objid		 objid		 group
	    22	       7561377	     0x7360a1	             0
	     8	       7557109	     0x734ff5	             0
	     4	       7561274	     0x73603a	             0
...
	    19	       7561455	     0x7360ef	             0
	    15	       7556931	     0x734f43	             0

```

In the above example, the file is using the 24 OSTs of Mahti and the stripe size is 1 MB. 

##MPI I/O Aggregators

* During a collective I/O operation, the buffers on the aggregated nodes are buffered through MPI, then these nodes write the data to the I/O servers.

* Example 8 MPI processes, 4 MPI processes per computing node, collective I/O, all the processes write on the same file. 

!["MPI I/O aggregators"](../../img/aggregators.png)

* MPI I/O Aggregators example *

By default, for collective I/O, the OpenMPI on Mahti defines 1 MPI I/O aggregator per compute node. This means that in our example above, only 2 MPI processes do the actual I/O. They gather the data from the rest of the processes (phase 1), and in the second phase they send the data to the storage. The usage of the default MPI aggregators could be enough, but in many cases, it is not.



## ROMIO Hints

* Hints for Collective Buffering (Two-Phase I/O) and more focus on Lustre

| Hint                | Description                                                                                                      |
|---------------------|------------------------------------------------------------------------------------------------------------------|
|cb_buffer_size       | The buffer size, in bytes, of the intermediate buffer used in two-phase collective I/O                           |
|romio_cb_read        | Collective read operations during collective buffering, values: enable, disable, automatic                       |
|romio_cb_write       | Collective write operations during collective buffering, values: enable, disable, automatic                      |
|romio_no_indep_rw    | Controls if no independent read/write is enabled or not, values: enable, disable, automatic                      |
|cb_config_list       | Defines how many MPI I/O aggregators can be user per node, values: *:X where X aggregators per each compute node |
|cb_nodes             | The maximum number of aggregators to be used                                                                     |

* How can I change the MPI I/O hints?

Create a text file with the required commands and declare inside your submission script:

```
export ROMIO_HINTS=/path/file
```

Replace the `path` and `file`

* How can I increase the number of the MPI I/O aggregators per node

 * Create or edit a text file with the content:

```
cb_config_list *:2
``` 
  This will activate 2 MPI processes per each compute node of your job to operate as MPI I/O aggregator.

* Change hints in the code of an application (code example):

```
...
call MPI_Info_create(info,ierror)
call MPI_Info_set(info,'romio_cb_write','enable',ierror)
...
call MPI_File_open(comm,filename,amode,info,fh,ierror)
...
```

* In some cases it is better to activate some hints than let the heuristics to decide with the automatic option

* How to see the used hints and their values?

 * Declare in yoru submission script:

```
export ROMIO_PRINT_HINTS=1
```

 * Then in your output, if and only if there is collective I/O, you will see the hints, for example:

```
key = cb_buffer_size            value = 33554432
key = romio_cb_read             value = enable
key = romio_cb_write            value = enable
key = cb_nodes                  value = 64
key = romio_no_indep_rw         value = false
key = romio_cb_pfr              value = disable
...
```
This is useful in order to be sure that your declarations were really used

