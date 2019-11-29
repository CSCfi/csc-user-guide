# Overview

Puhti is CSC's supercomputer. It has been available for CSC users since
2 September 2019. It contains CPU nodes with a range a memory sizes as well as a large GPU partition (Puhti AI). Please see the
[specifications](system.md) for details on the nodes and storage systems.

## Accessing Puhti

To gain access, please go to [my.csc.fi](https://my.csc.fi) to apply for
access to Puhti. Further instructions are provided in the Accounts section
of this user guide.

## Connecting to Puhti

Connect using a ssh client:
```
ssh <csc_username>@puhti.csc.fi
```
This will connect you to one of the login nodes. If you need to connect
to a specific login node, use the command:

```
ssh <csc_username>@puhti-login<number 1-2>.csc.fi
```
For instructions on how to connect using Putty or establishing
a graphical connection, see the [connecting](connecting.md) page.


!!! warning "Important"
    The login nodes can be used for compiling, moving data and **light** pre- and postprocessing. 
    **Light** means that these **one-core-jobs**
    should finish in **minutes** and require **a few GiB** of memory at maximum. 
    All other tasks are to be done in the compute nodes using the [batch job system](running/getting-started.md). Programs not adhering to these rules will be terminated without warning. Note that compute nodes can be used also [interactively](running/interactive-usage.md)



## Using Puhti

* [System](system.md): What computational resources does Puhti have
* [Disk areas](disk.md): What places are there for storing data on Puhti 
* [Modules](modules.md): How to find the programs you need
* [Applications](../apps/index.md): Application specific instructions.
* [Running jobs](running/getting-started.md): How to run programs on Puhti 
* [Compiling applications](compiling.md): Using compilers and building your applications   

