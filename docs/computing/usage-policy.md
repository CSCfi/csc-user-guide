# Usage policy

!!! info "Additional information"
    [General Terms of Use for CSC's Services for Research and
    Education](https://research.csc.fi/general-terms-of-use)

## Login nodes

When you login to CSC supercomputers, you end up on one of the login nodes of
the cluster. These login nodes are shared by all users and they are **not**
intended for heavy computing.

The login nodes should be used only for:

* compiling
* managing batch jobs
* moving data
* **light** pre- and postprocessing

Here **light** means **one-core jobs** that finish in **minutes** and require
**less than 1 GiB** of memory at maximum. All other tasks are to be done in
compute nodes either as normal [batch jobs](running/getting-started.md) or as
[interactive batch jobs](running/interactive-usage.md). Programs not adhering to
these rules will be terminated without warning.

!!! warning "Important"
    The login nodes are not meant for long or heavy processes.

## Disk cleaning

Each project has disk space in the directory `/scratch/<project>`. This fast
parallel scratch space is intended for data that is in active use. To ensure
that the parallel disk system does not run out of storage space and to keep
performance acceptable CSC automatically removes files in scratch that have not
been accessed in a long time. The performance of a parallel file system starts
to degrade when it fills up, and the more it fills up, the slower the performance
will get.

The current policy in Puhti is that files that have not been accessed for
**12 months** or more will be removed. This cleaning will happen regularly,
and each time users are informed at least 1 month in advance. CSC also provides
lists of files that are about to be removed and instructions for how one can
transfer important files to more suitable disk systems.

A similar procedure will be introduced on Mahti, but it is not yet in place.
The policy is still that users should keep only actively used data in scratch.

## GPU nodes

Puhti and Mahti GPUs should only be used for workloads that greatly benefit from
GPU capacity compared to using CPUs or which can't be run on CPUs. In particular
AI/ML workloads are prioritized, since many of them cannot be done at all on
CPUs. A good rule of thumb is to compare the [billing unit (BU)](../accounts/billing.md)
usage (_e.g._ with [`seff`](../performance/#quick-start-efficiency-report-with-seff)
or the [billing unit calculator](https://research.csc.fi/pricing)) of the job on
GPUs against CPUs and select the one using less.

For Puhti and Mahti, this means that a full node of CPU cores roughly equals
one GPU. However, since Puhti and Mahti have more CPU capacity than GPU, you
might get access to CPUs with less queuing. Note that [LUMI has a lot of GPU
capacity](https://docs.lumi-supercomputer.eu/hardware/compute/lumig/) which is
also "cheaper" as measured in BUs, and on LUMI it's better to use GPUs if
possible for your research. In any case, always make sure you use resources
efficiently.

## Conda installations

Due to performance issues of Conda-based environments on parallel file systems,
CSC has deprecated the _direct_ usage of Conda installations. This means that any
Conda environments you intend to use must be installed within a container. See
the page [Deprecating Conda](../support/deprecate-conda.md) for more information.

!!! info "Tykky"
    Please consider the [Tykky container wrapper](containers/tykky.md) for easy
    containerization of Conda and pip environments.
