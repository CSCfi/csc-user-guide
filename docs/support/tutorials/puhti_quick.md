# Puhti quick start guide
A quick start guide for Puhti users. It is assumed
that you have previously used CSC cluster resources like Taito/Sisu.

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
[running](../../computing/running/creating-job-scripts.md/#mpi-based-batch-jobs) MPI applications. 


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
    You have to specify your billing project in your batch script with the `--account=project_<project_number>` 
    flag. Failing to do so will cause your job to be held with the reason “_AssocMaxJobsLimit_”.
    Running `srun` directly also requires the flag.


## Network

- Login nodes can access the Internet 
- It is currently not possible to ssh to the compute nodes
- Compute nodes **do not** currently have Internet access 

## Storage

The **project based** shared storage can be found under `/scratch/project_<project_id>`.
Note that this folder is shared by **all users** in a project. This folder is not meant for long term data storage
and files that have not been used for 90 days will be automatically removed. The default quota for this folder is 1 TB. There is also a persistent **project based**
storage with a default quota of 50 GB. It is located under `/projappl/project_<project_id>`. Each user can store up to 10 GB of data in their home directory (`$HOME`).

More detailed information about storage can be found [here](../../computing/disk.md).
