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
Puhti-AI's V100 GPUs should only be used for the following workloads:

 * Machine Learning (ML) / Artificial Intelligence (AI) workloads
 * Code development for porting codes GPUs
 * HPC applications benefitting greatly from GPUs, or even only supporting GPUs. This means that the code should be at least **2x** as fast on one V100 GPU compared to one Puhti node. Please confirm this for your use case and keep the log files and corresponding SLURM jobids in case we ask for them later.


Mahti-AI's A100 GPUs should only be used for the following workloads:

 * ML/AI workloads
 * Code development for porting codes GPUs
 * HPC applications that can use the new hardware features in A100 (tensor cores). This means that the code should be at least **3x** as fast on one A100 GPU compared to one Mahti node. Please confirm this for your use case and keep the log files and corresponding SLURM jobids in case we ask for them later.


The rationale for this policy is:

 * The majority of compute resources are CPU based. Hence it is likely that you (and everyone) will
actually also get results faster due to less queuing if your code can use both CPUs and GPUs.
 * Puhti-AI and Mahti-AI have been specifically funded to be used in
machine learning (ML) and artificial intelligence (AI) related
research. A significant part of these resources must be available for
this use.
 *  ML/AI workloads often use libraries and frameworks specifically optimized for GPUs. Typically, a ML/AI workflow will be many times faster if run on a GPU, compared to running e.g. using a full node of CPUs. Typically, the benefit for GPU optimized other HPC workloads is smaller, although sometimes still faster than with a full CPU node.
 * The significant improvement of the A100 GPU cards in Mahti-AI over V100 in Puhti-AI are the tensor cores. There are many ML/AI workloads
that can make use of them resulting in large speedups, whereas non-AI/ML workloads often don't. Optimal usage of this resource requires ability to utilize the tensor cores.
