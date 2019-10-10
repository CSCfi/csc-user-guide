# Moving to Puhti from Taito and Sisu

A quick start guide for Puhti users. It is assumed
that you have previously used CSC cluster resources like Taito/Sisu. If not,
you can start by looking [here](../../computing/overview.md).

**Go to [my.csc.fi](https://my.csc.fi) to apply for access to Puhti or view your projects and their project numbers
if you already have access.**

[TOC]


## Connecting to Puhti

Connect using a normal ssh-client:
```
$ ssh <csc_username>@puhti.csc.fi
```

## Module system:

CSC uses the [Lmod](https://lmod.readthedocs.io) module system.

Modules are set up in a hierarchical fashion, meaning you need to load a compiler 
before MPI and other libraries appear.

More information about modules [here](../../computing/modules.md).

## Compilers

The system comes with two compiler families installed, the Intel and GCC compilers. 
We have installed both the 18 and 19 versions of the Intel compiler, and for GCC 9.1, 8.3 and 7.4 are available.
The pgi compiler 19.7 is available for building gpu applications.

More information about compilers [here](../../computing/compiling.md).



## MPI
Currently the system has a few different MPI implementations installed:

- hpcx-mpi
- mpich
- intel-mpi

We recommend to test using 
_hpcx-mpi_ first, this one is from the network vendor and is based on OpenMPI. 

 **You will need to have the MPI module loaded when submitting your jobs.**

More information about [building](../../computing/compiling.md#building-mpi-applications) and
[running](../../computing/running/creating-job-scripts.md#mpi-based-batch-jobs) MPI applications. 


## Applications

More information about specific applications can be found [here](../../apps/alpha.md)

!!! warning "Default python"
    Python is available through the _python-env_ module. This will replace the system python call with python 3.7. The anaconda environment has a lot of regularly used packages installed by default.



## Running jobs

Puhti uses the [slurm](https://slurm.schedmd.com/documentation.html) batch job system. 

A description of the different slurm partitions can be found [here](../../computing/running/batch-job-partitions.md). Note that the GPU partitions are available from the normal login nodes. 

Instructions on how to submit jobs can be found [here](../../computing/running/creating-job-scripts.md)
and example batch job scripts are found [here](../../computing/running/example-job-scripts.md)

!!! note "Very important change!!"
    You have to specify your billing project in your batch script with the `--account=<project>`
    flag. Failing to do so will cause your job to be held with the reason “_AssocMaxJobsLimit_”.
    Running `srun` directly also requires the flag.

More information about billing [here](../../accounts/billing.md)

## Network

- Login nodes can access the Internet 
- Compute nodes can access the Internet 
- It is currently not possible to ssh to the compute nodes


## Storage

The **project based** shared storage can be found under `/scratch/<project>`.
Note that this folder is shared by **all users** in a project. This folder is not meant for long term data storage
and files that have not been used for 90 days will be automatically removed. The default quota for this folder is 1 TB. There is also a persistent **project based**
storage with a default quota of 50 GB. It is located under `/projappl/<project>`. Each user can store up to 10 GB of data in their home directory (`$HOME`).

More detailed information about storage can be found [here](../../computing/disk.md).


## Moving data from Taito to Puhti

Taito.csc.fi cluster will be closed at the end of 2019. If you have some data that you want to preserve in the directories of Taito ( including $HOME, $WRKDIR and project directories) you have copy the data elsewhere before 1.1. 2020.

The new Allas object storage service provides a platform that you can use to store your data that is currently in Taito.
The new Puhti server, that is replacing Taito, does not provide permanent storage space for research data. Even if you would continue your work immediately in Puhti, it is good to make a more permanent copy of your data to Allas. This is done if you do the data migration from Taito to Puhti through Allas.

*    [Data migration tutorials](../../data/Allas/migration_tutoria.md)
*    [Allas user guide](../../data/Allas/index.md)




