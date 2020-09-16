# Getting started with Puhti

This is a quick start guide for Puhti users. It is assumed
that you have previously used CSC cluster resources like Taito/Sisu. If not,
you can start by looking [here](../../computing/overview.md).

**Go to [my.csc.fi](https://my.csc.fi) to apply for access to Puhti or view your projects and their project numbers
if you already have access.** On Puhti, you can also use command `csc-projects`.

[TOC]


## Connecting to Puhti

Connect via [NoMachine](../../apps/nomachine.md) or using a normal ssh-client:
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

More information about compilers [here](../../computing/compiling-puhti.md).

## High performance libraries

Puhti has several high performance libraries installed, more
information [here](../../computing/hpc-libraries.md).


## MPI
Currently the system has a few different MPI implementations installed:

- hpcx-mpi
- mpich
- intel-mpi

We recommend to test using 
_hpcx-mpi_ first, this one is from the network vendor and is based on OpenMPI. 

 **You will need to have the MPI module loaded when submitting your jobs.**

More information about [building](../../computing/compiling-puhti.md#building-mpi-applications) and
[running](../../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs) MPI applications. 


## Applications

More information about specific applications can be found [here](../../apps/alpha.md)

!!! warning "Default python"
    Python is available through the _python-env_ module. This will replace the system python call with python 3.7. The anaconda environment has a lot of regularly used packages installed by default.



## Running jobs

Puhti uses the [slurm](https://slurm.schedmd.com/documentation.html) batch job system. 

A description of the different slurm partitions can be found [here](../../computing/running/batch-job-partitions.md). Note that the GPU partitions are available from the normal login nodes. 

Instructions on how to submit jobs can be found [here](../../computing/running/creating-job-scripts-puhti.md)
and example batch job scripts are found [here](../../computing/running/example-job-scripts-puhti.md)

!!! note "Very important change!!"
    You have to specify your billing project in your batch script with the `--account=<project>`
    flag. Failing to do so will cause your job to be held with the reason “_AssocMaxJobsLimit_”.
    Running `srun` directly also requires the flag.

More information about billing [here](../../accounts/billing.md) and common queuing 
system error messages in the [FAQ](../faq/why-does-my-batch-job-fail.md).

## Network

- Login nodes can access the Internet 
- Compute nodes can access the Internet 

## Storage

The **project based** shared storage can be found under `/scratch/<project>`.
Note that this folder is shared by **all users** in a project. This folder is not meant for long term data storage
and files that have not been used for 90 days will be automatically removed. The default quota for this folder is 1 TB. There is also a persistent **project based**
storage with a default quota of 50 GB. It is located under `/projappl/<project>`. Each user can store up to 10 GB of data in their home directory (`$HOME`).

You can [check your current disk usage](../faq/disk-quota-exceeded.md) with `csc-workspaces`, more detailed information about storage can be found [here](../../computing/disk.md).


## Moving data from Taito to Puhti

Taito.csc.fi cluster was finally closed in June 2020. The disks are still accessible via 
[datamangler](../../../data/Allas/migration_tutorial/#datamangler), 
now is the last change to salvage your important data.

The new Allas object storage service provides a platform that you can use to store your data that is currently in Taito.
Puhti does not provide permanent storage space for research data. Even if you would continue your work immediately in Puhti, it is good to make a more permanent copy of your data to Allas. This is done if you do the data migration from Taito to Puhti through Allas.

*    [Data migration tutorials](../../data/Allas/migration_tutorial.md)
*    [Allas user guide](../../data/Allas/index.md)

## Linux basics Tutorial for CSC

If you are new to Linux command line or using supercomputers, please consult [this tutorial section](env-guide/overview.md)!


