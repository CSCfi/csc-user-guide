# Overview

Puhti and Mahti are CSC's supercomputers. Puhti has been available for CSC users since
2 September 2019 and Mahti has been available since 16 april 2020.

Puhti contains CPU nodes with a range a memory sizes as well as a large GPU partition (Puhti AI), while
Mahti contains homogeneous CPU nodes and is meant for larger jobs (minimum 128 CPU-cores). 
See [specifications](system.md) for details on the systems.

## Accessing Puhti and Mahti

To gain access, please go to [my.csc.fi](https://my.csc.fi) to apply for
access to the supercomputers. Further instructions are provided in the Accounts section
of this user guide.

## Connecting to the supercomputers

Connect using a ssh client:

```
ssh <csc_username>@puhti.csc.fi
```
or
```
ssh <csc_username>@mahti.csc.fi
```


This will connect you to one of the login nodes. If you need to connect
to a specific login node, use the command:

```
ssh <csc_username>@puhti-login<number 1-2>.csc.fi
```
or
```
ssh <csc_username>@mahti-login<number 1-2>.csc.fi
```


For instructions on how to connect using Putty or establishing
a graphical connection, see the [connecting](connecting.md) page.

## Usage policy

When you login to CSC supercomputers, you end up to one of the login nodes of the cluster.
These login nodes are shared by all users and they are **not** intended for heavy computing. 

The login nodes should be used only for:

 * compiling
 * manging batch jobs
 * moving data 
 * **light** pre- and postprocessing
  
Here **light** means **one-core-jobs** that finish in **minutes** and require **a few GiB** of memory at maximum.
All the other tasks are to be done in compute nodes either as normal [batch jobs](running/getting-started.md)
or as [interactive batch jobs](running/interactive-usage.md).
Programs not adhering to these rules will be terminated without warning.

!!! warning "Important"
    The login nodes are not meant for long or heavy processes.


## Using Puhti and Mahti

* [System](system.md): What computational resources are available 
* [Disk areas](disk.md): What places are there for storing data on Puhti and Mahti 
* [Modules](modules.md): How to find the programs you need
* [Applications](../apps/index.md): Application specific instructions.
* [Running jobs](running/getting-started.md): How to run programs on the supercomputers 
* [Compiling applications](compiling.md): Using compilers and building your applications   

