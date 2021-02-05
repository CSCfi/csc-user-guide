# Getting started with Mahti

This is a quick start guide for Mahti users. It is assumed that you have
previously used CSC supercomputing resources like Puhti, Sisu or
Taito. If not, you can start by looking
[here](../../computing/overview.md).

**Go to [my.csc.fi](https://my.csc.fi) to apply for access to Mahti or
view your projects and their project numbers if you already have
access.**

[TOC]

## Connecting to Mahti

Connect using a normal ssh-client:
```
$ ssh yourcscusername@mahti.csc.fi
```
Where **yourcscusername** is the username you get from CSC.

## Module system

Modules are set up in a hierarchical fashion, meaning you need to load
a compiler before MPI and other libraries appear. CSC uses the
[Lmod](https://lmod.readthedocs.io) module system. More information
about modules [here](../../computing/modules.md).

Default modules, which are loaded automatically, are `gcc/9.3.0`,
`openmpi/4.0.3` and `openblas/3.10`.

## Compilers and MPI

Currently, Mahti has GNU compiler suites (versions 9.3.0 and 7.4.0), as
well as AMD and Intel compiler suites. All compiler suites can be used
with the `mpicc` (C), `mpicxx` (C++), or `mpif90` (Fortran)
wrappers. We recommend to start with the GNU compiler suite, but for some
applications the other suites may provide better performance.

In Mahti, many applications benefit from hybrid MPI/OpenMP
parallelization, so it is recommended to build a hybrid version if it
is supported by your application.

More information about compilers [here](../../computing/compiling-mahti.md).

!!! warning "Note" 
    You need to have the MPI module loaded when submitting your jobs

## High performance libraries

Mahti has several high performance libraries installed, more
information [here](../../computing/hpc-libraries.md).

## Applications

More information about specific applications can be found [here](../../apps/alpha.md).
Note, the preinstalled selection is not as large as on Puhti.

## Running jobs

Like Puhti, Mahti uses the [slurm](https://slurm.schedmd.com/documentation.html)
batch job system. A description of the different slurm partitions can
be found [here](../../computing/running/batch-job-partitions.md).

Instructions on how to submit jobs can be found [here](../../computing/running/creating-job-scripts-mahti.md)
and example batch job scripts are found [here](../../computing/running/example-job-scripts-mahti.md)

## Performance considerations

In Mahti, many applications benefit from hybrid MPI/OpenMP parallelization,
however, the optimum ratio of MPI tasks and OpenMP threads depends a lot
on the particular application as well as on particular input data
set. Mahti supports also simultaneous multithreading (SMT), *i.e.* two threads can be run
on the same physical CPU core. Benefits of multithreading depend also on the
application, in some cases it improves performance while in some cases
performance becomes worse. Binding of threads to CPU cores can also have
an impact on performance. 

More information about controlling hybrid applications can be found
[here](../../computing/running/performance-checklist.md#hybrid-parallelization-in-mahti). 

## Storage

The **project based** shared storage can be found under
`/scratch/<project>`.  Note that this folder is shared by **all
users** in a project. This folder is not meant for long term data
storage and files that have not been used for 90 days will be
automatically removed. The default quota for this folder is 1
TB. There is also a persistent **project based** storage with a
default quota of 50 GB. It is located under
`/projappl/<project>`. Each user can store up to 10 GB of data in
their home directory (`$HOME`).

The disk areas for different supercomputers are separate, *i.e.*
**home**, **projappl** and **scratch** in Puhti cannot be directly
accessed from Mahti.

More detailed information about storage can be found [here](../../computing/disk.md).

## Moving data between Mahti and Puhti

Data can be moved between supercomputers via
[Allas](../../data/Allas/index.md) by first uploading 
the data from one supercomputer and then downloading it to the other.
This is the recommended approach if the data should also
be preserved for a longer time.

Data can also be moved directly between the supercomputers with the
_rsync_ command. For example, in order to copy *my_results* (which can be
either a file or a directory) from
Puhti to the directory */scratch/project_2002291* in Mahti, one can
issue in Puhti the command: 
```bash
rsync -azP my_results <username>@mahti.csc.fi:/scratch/project_2002291
```
See [Using rsync](../../data/moving/rsync.md) for more detailed instructions
for *rsync*.

## How Mahti and Puhti differ?

If you are new to supercomputes, or the details below is unfamiliar, you
likely should start with [Puhti](puhti_quick.md) and some [introductory tutorials](env-guide/overview.md) first.
In a nutshell, Mahti is meant for large parallel jobs, and Puhti for a wide
variety of small to medium sized jobs including special resources.

|Resource                | Mahti           | Puhti                             |
|------------------------|-----------------|-----------------------------------|
|Resources are granted   | By full nodes   | By finer detail (cores/memory/...)|
|Minimum job size        | 128 cores (1 node)| 1 core (1/40 node)              |
|Maxmimum job size (cores) | 200 nodes (*) (25600)| 100 (**) nodes (40000)           |
|Memory per node (average per core) | 245 GB (2 GB)   |  192 - 1500 GB (4 - 37 GB) |
|GPUs                    | no              | yes                               |
|Fast local disk         | no              | yes (NMVe)                        |
|Preinstalled applications |  ~15          | ~120                              |

<pre>
(*) And even more via Grand Challenge calls.
(**) To be scaled down to 25 nodes in autumn 2020.
</pre>
