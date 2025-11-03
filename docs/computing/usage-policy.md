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
[interactive batch jobs](running/interactive-usage.md). Programs not adhering
to these rules will be terminated without warning.

!!! warning "Important"
    The login nodes are not meant for long or heavy processes.

## Disk cleaning

Each project has disk space in the directory `/scratch/<project>`. This fast
parallel scratch space is intended for data that is in active use. To ensure
that the parallel disk system does not run out of storage space and to keep
performance acceptable,
[CSC automatically removes files in Puhti scratch](../support/tutorials/clean-up-data.md#automatic-removal-of-files)
that have not been accessed in a long time. The performance of a parallel file
system starts to degrade when it fills up, and the more it fills up, the slower
the performance will get.

This cleaning will happen regularly, and each time users are informed at least
1 month in advance. CSC also provides lists of files that are about to be
removed and instructions for how one can transfer important files to more
suitable disk systems.

**The cleaning is stricter for projects with larger quotas**:

* For projects that have a **scratch quota of 5 TiB or more**, files that have
  not been accessed (opened, read, modified) in the last **90 days** will be
  deleted.
* For other projects with **smaller scratch quotas**, files that have not been
  accessed (opened, read, modified) in the last **180 days** will be deleted.

You can use the `csc-workspaces` command to see which cleaning cycle your
projects are subject to.

**Mahti:** A similar procedure will be introduced on Mahti if the disk usage
grows enough to warrant it. The policy is still that users should keep only
actively used data in scratch.

## GPU nodes

Puhti and Mahti GPUs should only be used for workloads that greatly benefit
from GPU capacity compared to using CPUs or which can't be run on CPUs. In
particular AI/ML workloads are prioritized, since many of them cannot be done
at all on CPUs. A good rule of thumb is to compare the
[Billing Unit (BU)](../accounts/billing.md) usage (_e.g._ with
[`seff`](./performance.md#quick-start-efficiency-report-with-seff) or the
[Billing Unit calculator](https://research.csc.fi/resources/#buc))
of the job on GPUs against CPUs and select the one using less. One CPU BU and one 
GPU BU are equal in terms of cost.

For Puhti and Mahti, this means that a full node of CPU cores roughly equals
one GPU. However, since Puhti and Mahti have more CPU capacity than GPU, you
might get access to CPUs with less queuing. Note that
[LUMI has a lot of GPU capacity](https://docs.lumi-supercomputer.eu/hardware/lumig/)
which is also "cheaper" as measured in BUs, and on LUMI it's better to use GPUs
if possible for your research. In any case, always make sure you use resources
efficiently.

## Conda installations

Due to performance issues of Conda-based environments on parallel file systems,
CSC has deprecated the _direct_ usage of Conda installations. This means that
any Conda environments you intend to use must be installed within a container.
See [Conda best practices](../support/tutorials/conda.md) for more information.

!!! info "Tykky"
    Please consider the [Tykky container wrapper](containers/tykky.md) for easy
    containerization of Conda and pip environments.

## Running out of Billing Units

When a project runs out of Billing Units, the ability to use
the service will be limited in three phases.  If you are still
actively using the project you can lift the limitations by
[applying](../accounts/how-to-apply-for-billing-units.md) for more
Billing Units.

In the first phase the ability to submit new jobs is limited:

* If you run out of Storage BUs, no new jobs can be submitted to any
partition 
* If you run out of CPU BUs, no new jobs can be submitted to CPU partitions
* If you run out of GPU BUs, no new jobs can be submitted to GPU partitions

In other words, running out of CPU or GPU BUs only affects the
corresponding partition type, while Storage BUs affect all. Jobs that
are running are not interrupted and will run until completion/timeout.


In the second step data access is limited. When you run out of storage
BUs a 30-day grace period starts, after which access to `/projappl`
and `/scratch` folders is disabled. No data is deleted, it is only
access that is disabled. Data will, however, still be removed from
`/scratch` during the [normal cleaning process](#disk-cleaning). Note that
having negative balance for CPU or GPU BUs does not trigger this step,
only a negative Storage BU balance.


If you are not using a project actively we encourage you to migrate any data
that you still need within the 30-day grace period and then
[close the project](../accounts/how-to-manage-your-project.md#project-closure)
in MyCSC. 

In the third phase the project is closed after a 60-day grace period
if you have run out of BUs of any type. If the project still has a
negative amount of Billing Units of any type after 60 days, it will be
closed.



## Slurm job management by CSC

* CSC will not change job parameters like length or priority. 
* CSC can terminate jobs if they are misusing resources. E.g., if resources
  (CPU cores, GPUs, memory) are severely underutilized or IO is overloading
  the storage system.
