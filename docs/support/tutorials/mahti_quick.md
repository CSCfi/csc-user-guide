# Getting started with Mahti

A quick start guide for Mahti users. It is assumed
that you have previously used CSC supercomputing resources like Puhti, Sisu or Taito. If not, you can start by looking [here](../../computing/overview.md).

**Go to [my.csc.fi](https://my.csc.fi) to apply for access to Mahti or view your projects and their project numbers
if you already have access.**

[TOC]


## Connecting to Mahti

Connect using a normal ssh-client:
```
$ ssh <csc_username>@mahti.csc.fi
```

## Module system:

CSC uses the [Lmod](https://lmod.readthedocs.io) module system.

Modules are set up in a hierarchical fashion, meaning you need to load a compiler 
before MPI and other libraries appear.

More information about modules [here](../../computing/modules.md).

## Compilers and MPI

Currently, Mahti has GNU compiler suite (versions 9.3.0 and 7.4.0), as
well as AMD and Intel compiler suites. No compiler suite is selected
by default, but it needs to be loaded via module system. The MPI
environment in Mahti is OpenMPI, and it needs to be activated also via
module system. For example, in order to use GNU compiler suite, one
can issue the command

```bash
module load gcc openmpi
```

All compiler suites can be used with the `mpicc` (C), `mpicxx` (C++),
or `mpif90` (Fortran) wrappers. We recommend to start with GNU compiler suite,
but for some applications the other suites may provide better performance.

In Mahti, many applications benefit from hybrid MPI/OpenMP
parallelization, so it is recommended to build a hybrid version if it
is supported by application.

More information about compilers [here](../../computing/compiling-mahti.md).

!!! warning "Note" 
    You need to have the MPI module loaded when submitting your jobs

## High performance libraries

Mahti has several high performance libraries installed, more
information [here](../../computing/hpc-libraries.md).

## Applications

More information about specific applications can be found [here](../../apps/alpha.md)


## Running jobs

Mahti uses the [slurm](https://slurm.schedmd.com/documentation.html) batch job system. 

A description of the different slurm partitions can be found [here](../../computing/running/batch-job-partitions.md). 

Instructions on how to submit jobs can be found [here](../../computing/running/creating-job-scripts.md)
and example batch job scripts are found [here](../../computing/running/example-job-scripts-mahti.md)

!!! warning "Note"
    During pilot period, scalability testing **is not** required for
    using **large** partiotion

## Performance considerations

In Mahti, many applications benefit from hybrid MPI/OpenMP parallelization,
however, the optimum ratio of MPI tasks and OpenMP threads depend lot
on particular application as well as on particular input data
set. Mahti supports also hyperthreading, *i.e.* two threads can be run
on the same CPU core. Benefits of hyperthreading depend also on the
application, in some cases it improves performance while in some cases
performance becomes worse. Binding of threads to CPU cores can also have
an impact on performance. 

More information about controlling hybrid applications can be found
[here](../../computing/running/performance-checklist.md#hybrid-parallelization-in-mahti). 


## Storage

The **project based** shared storage can be found under `/scratch/<project>`.
Note that this folder is shared by **all users** in a project. This folder is not meant for long term data storage
and files that have not been used for 90 days will be automatically removed. The default quota for this folder is 1 TB. There is also a persistent **project based**
storage with a default quota of 50 GB. It is located under `/projappl/<project>`. Each user can store up to 10 GB of data in their home directory (`$HOME`).

The disk areas for different supercomputers are separate, *i.e.*
**home**, **projappl** and **scratch** in Puhti cannot be directly
accessed from Mahti.

More detailed information about storage can be found [here](../../computing/disk.md).


## Moving data between Mahti and Puhti

Data can be moved between supercomputers via
[Allas](../../data/Allas/index.md) by first uploading 
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
See [Using rsync](../../data/moving/rsync.md) for more detailed instructions
for *rsync*.
