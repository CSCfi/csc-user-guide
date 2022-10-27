# Usage policy

## Login nodes
When you login to CSC supercomputers, you end up to one of the login nodes of the cluster.
These login nodes are shared by all users and they are **not** intended for heavy computing.

The login nodes should be used only for:

 * compiling
 * managing batch jobs
 * moving data
 * **light** pre- and postprocessing

Here **light** means **one-core-jobs** that finish in **minutes** and require **a less than 1 GiB** of memory at maximum.
All the other tasks are to be done in compute nodes either as normal [batch jobs](running/getting-started.md)
or as [interactive batch jobs](running/interactive-usage.md).
Programs not adhering to these rules will be terminated without warning.

!!! warning "Important"
    The login nodes are not meant for long or heavy processes.

## Disk cleaning

Each project has disk space in the directory
`/scratch/<project>`. This fast parallel scratch space is intended for
data that is in active use. To ensure that the parallel disk system
does not run out of storage space, and to keep performance acceptable
CSC automatically removes files in scratch that have not been accessed
in a long time. The performance of a parallel file system
starts to degrade when it fills up, and the more it fills up, the
slower the performance will get.

The current policy is in Puhti that files that have not been accessed
for **12 months** or more will be removed. This cleaning will happen
regularly, and each time users are informed at least 1 month in
advance. CSC also provides lists of files that are about to be removed
and instructions for how one can transfer important files to more
suitable disk systems.

A similar procedure will be introduced on Mahti, but it is not yet in
place. The policy is still that users should keep only actively used
data in scratch.


## GPU nodes

Puhti and Mahti GPUs should only be used for workloads that greatly benefit of GPU capacity compared to using CPU or which can't be run on CPU. A good rule of thumb is to compare the [billing unit (BU)](../accounts/billing.md) usage (_e.g._ with [`seff`](performance/#quick-start-efficiency-report-with-seff) or the [billing unit calculator](https://research.csc.fi/pricing)) on the job on GPU with CPU and select the one using less. For Puhti and Mahti, this means that a full node of CPU cores roughly equals one GPU. Note, that [LUMI has a lot of GPU capacity](https://docs.lumi-supercomputer.eu/hardware/compute/lumig/) which is also "cheaper" as measured in BUs, and on LUMI it's better to use GPUs if possible for your research. In any case, always make sure you use resources efficiently.

