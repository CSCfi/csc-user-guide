# Getting started with Puhti

This is a quick start guide for Puhti users. It is assumed that you have previously
used CSC cluster resources like Taito/Sisu. If not, you can start by looking at
[overview of CSC supercomputers](../../computing/index.md).

**Go to [MyCSC](https://my.csc.fi) to apply for access to Puhti or view your projects
and their project numbers if you already have access.** You can also use the command
`csc-projects`.

[TOC]

## Connecting to Puhti

Connect using a normal ssh-client:

```bash
ssh yourcscusername@puhti.csc.fi
```

Where `yourcscusername` is the username you get from CSC.

There is also a [web interface](../../computing/webinterface/index.md) available at
[www.puhti.csc.fi](https://www.puhti.csc.fi), where you can log in with your CSC user name.
In this interface you can manage files, launch interactive applications and list jobs, quotas
and project statuses. You can use it also for graphical applications.

## Module system

CSC uses the [Lmod](https://lmod.readthedocs.io) module system.

Modules are set up in a hierarchical fashion, meaning you need to load a compiler
before MPI and other libraries appear.

See [more information about modules](../../computing/modules.md).

## Compilers

The system comes with two compiler families installed, the Intel OneAPI and GCC compilers.
We have installed `intel-oneapi-compilers-classic/2021.6.0` and `intel-oneapi-compilers/2022.1.0`
of the Intel compilers, and for GCC 11.3, 9.4 and 8.5 are available.

See [more information about compilers](../../computing/compiling-puhti.md).

## High performance libraries

Puhti has several high performance libraries installed, see [more
information about libraries](../../computing/hpc-libraries.md).

## MPI

Currently the system has a two MPI implementations installed:

- openmpi
- intel-oneapi-mpi

We recommend to test using `openmpi` first.

!!! warning "Note"
    You need to have the MPI module loaded when submitting your jobs.

More information about [building](../../computing/compiling-puhti.md#building-mpi-applications) and
[running](../../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs) MPI applications.

## Applications

More information about specific applications can be found [here](../../apps/alpha.md)

!!! Python
    System Python is available by default both in Puhti and Mahti without loading any module. Python 3
    (= 3.6.8) is available as `python3`. The default system Python does not include any optional Python
    packages. Several other [Python](../../apps/python.md) installations are available via the module system.
    [python-data](../../apps/python-data.md) is a good first choice, it includes a lot of regularly used
    packages.

## Running jobs

Puhti uses the [Slurm](https://slurm.schedmd.com/documentation.html) batch job system.

A description of the different Slurm partitions can be found
[here](../../computing/running/batch-job-partitions.md). Note
that the GPU partitions are available from the normal login nodes.

Instructions on how to submit jobs can be found [here](../../computing/running/creating-job-scripts-puhti.md)
and example batch job scripts are found [here](../../computing/running/example-job-scripts-puhti.md)

!!! note "Very important change!!"
    You have to specify your billing project in your batch script with the `--account=<project>`
    flag. Failing to do so will cause your job to be held with the reason `AssocMaxJobsLimit`.
    Running `srun` directly also requires the flag.

More information about billing [here](../../accounts/billing.md) and common queuing
system error messages in the [FAQ](../faq/why-does-my-batch-job-fail.md).

## Network

- Login nodes can access the Internet
- Compute nodes can access the Internet

## Storage

The **project based** shared storage can be found under `/scratch/<project>`.
Note that this folder is shared by **all users** in a project. This folder is
not meant for long term data storage and files that have not been used for 90
days will be automatically removed. **This policy has not yet been fully
implemented, but we plan to take this cleaning procedure fully in use later
in 2022.**

The default quota for this folder is 1 TB. There is also a persistent
**project based** storage with a default quota of 50 GB. It is located
under `/projappl/<project>`. Each user can store up to 10 GB of data in
their home directory (`$HOME`).

You can [check your current disk usage](../faq/disk-quota-exceeded.md) with
`csc-workspaces`. More detailed information about storage can be found
[here](../../computing/disk.md) and a guideline on managing data on the
`/scratch` disk [here](clean-up-data.md). See also the [LUE tool](lue.md)
for efficiently querying how much data/files you have in a directory.

## Linux basics Tutorial for CSC

If you are new to Linux command line or using supercomputers, please consult
[this tutorial section](env-guide/overview.md)! See also the materials of the
[CSC Computing Environment self-learning course](https://csc-training.github.io/csc-env-eff/).
