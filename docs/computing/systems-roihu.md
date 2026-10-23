# Roihu supercomputer

## Schedule

```mermaid
graph LR;
    A{{"<b>September 2025</b>
        Roihu installation
        in progress"}} --> B;
    B{{"<b>April 2026</b>
        Pilot phase
        starts"}} --> C;
    C{{"<b>June 2026</b>
        Roihu general
        availability (GA)"}} --> D;
    D{{"<b>End of July 2026</b>
        Puhti <i>computing
        services</i> shut down"}} --> E;
    E{{"<b>End of August 2026</b>
        Mahti <i>computing
        services</i> shut down"}} --> F;
    F{{"<b>Mid October 2026</b>
        Puhti <i>storage
        services</i> shut down"}} --> G;
    G{{"<b>Mid October 2026</b>
        Mahti <i>storage services</i>
        shut down"}}
    style A fill:#dceeceff;
    style B fill:#dceeceff;
    style C fill:#dceeceff;
    style D fill:#dceeceff;
    style E fill:#dceeceff;
    style F fill:#dceeceff;
    style G fill:#dceeceff;
```

Puhti and Mahti have been retired as of 15 October 2026, and are no longer accessible.

## Compute

Roihu has a total of 486 CPU nodes and 132 GPU nodes. The
high-performance LINPACK (HPL) performance is estimated to be 10.5 PFlop/s for
the CPU nodes and 23.4 PFlop/s for the GPU nodes, resulting in an aggregate HPL
performance of 33.9 PFlop/s for the full system.

The CPU nodes have two 192-core AMD Turin 9965 CPUs each, amounting to
186 624 CPU cores altogether. The CPUs are based on the AMD Zen 5 architecture,
which supports the AVX-512 vector instruction set. 414 of the CPU nodes
have 768 GiB of memory, while the remaining 72 nodes have an extended
memory of 1 536 GiB each.

Each GPU node is equipped with 4 Nvidia GH200 Grace Hopper superchips.
Each GH200 superchip comprises one Hopper (H100) GPU and one Grace CPU with
72 ARM CPU cores, which are connected via a very fast interface. Each
GH200 superchip has 120 GiB CPU memory and 96 GiB GPU memory, providing
a total of 480 GiB CPU memory per node. This results in a total of 528 GPUs and
38 016 CPU cores in the whole GPU partition.

The system also provides four visualization nodes with two Nvidia L40 GPUs
each, as well as four high-memory CPU nodes with 6 TiB memory and higher
single-thread performance.

### Nodes

!!! note "Node names"
     The node names below describe the different node types in Roihu. Batch job partitions and allocation types in Slurm may use different names. 
     See the [Slurm partition documentation](running/batch-job-partitions.md) for how to request these resources in Slurm.

| Name | Number of nodes | Compute        | Cores                          | Memory (GiB) | Local disk (TB) |
|:-----|----------------:|---------------:|-------------------------------:|-------------:|----------------:|
| M    | 414             | AMD Turin 9965 | 2 x 192 cores (x86) @ 2.25 GHz | 768          | 0.96            |
| L    | 72              | AMD Turin 9965 | 2 x 192 cores (x86) @ 2.25 GHz | 1536         | 0.96            |
| XL   | 4               | AMD Turin 9555 | 2 x 64 cores (x86) @ 3.20 GHz  | 6144         | 15.36           |
| V    | 4               | AMD Turin 9335<br>Nvidia L40 | 2 x 32 cores (x86) @ 3.40 GHz<br>2 x GPUs | 384<br>2 x 48 | 15.36 |
| GPU  | 132             | Nvidia GH200   | 4 x 72 cores (ARM)<br>4 x GPUs | 4 x 120<br>4 x 96 | 0.96 |

Due to differences in CPU architecture between the CPU and GPU nodes (x86 and
ARM, respectively), Roihu provides separate login nodes for CPU and GPU
workloads: `roihu-cpu.csc.fi` and `roihu-gpu.csc.fi`.

Based on whether your workload targets CPUs or GPUs, please connect to the
appropriate login node when installing software or submitting jobs.
[More information about connecting](connecting/index.md).

The operating system of Roihu is Red Hat Enterprise Linux 9 (RHEL9).

## Storage

### Parallel file system

Roihu has two independent flash-based DDN EXAScaler Lustre file systems –
a 6.0 PiB Scratch space and a 0.5 PiB storage system for project applications
and users' personal Home directories. Separate file systems ensure
responsiveness of Home and ProjAppl even under heavy Scratch usage.

The peak I/O performance of Roihu Scratch is around 560 GB/s
for read and 280 GB/s for write. The Home and ProjAppl disk areas have read
and write bandwidths of 120 GB/s and 100 GB/s, respectively.

Roihu Scratch disk is regularly cleaned of files that
have not been accessed in the last 180 days (90 days for projects with a
scratch quota of 5 TiB or more) to prevent inactive data from accumulating
on the system.

Roihu also provides a separate Dataset disk area for actively used
datasets that need to be shared between multiple computational projects.
A dataset project provides a shared disk area for common datasets under
`/dataset/<dataset-project-id>`, helping to avoid duplicate copies and
simplifying access management between projects.

See [Roihu dataset project](roihu-dataset-project.md) for details.

### Local storage capacity

Each Roihu CPU and GPU node provides 960 GB of local NVMe storage
for temporary files created during jobs.

High-memory (XL) and visualization (VIZ) nodes provide additional capacity and
faster performance in their local storage, with a total of 13 TiB of local NVMe storage per node.

There are two kinds of node-local storage. **Automatic temporary storage**
(`$TMPDIR`) is available in every job without a reservation and free of
charge. **Reservable local scratch** (`$LOCAL_SCRATCH`) is only available on
the XL and V nodes, is reserved through Slurm with the `--gres=nvme` option,
and consumes billing units. The amounts that a single user can access in
their jobs depend on the system [partition](running/batch-job-partitions.md)
they use:

=== "Automatic (`$TMPDIR`)"

    | Allocation type         | Available per user | Read / Write speeds |
    |:------------------------|-------------------:|---------------------|
    | R (shared nodes)        | 20 GiB             | 5000 / 1400 MB/s    |
    | N (full nodes)          | 600 GiB            | 5000 / 1400 MB/s    |
    | G (GPU nodes)           | 150 GiB            | 5000 / 1400 MB/s    |
    | Hugemem (XL) nodes      | 578 GiB            | 6700 / 4000 MB/s    |
    | V (visualization nodes) | 14 TiB             | 6700 / 4000 MB/s    |

=== "Reservable (`$LOCAL_SCRATCH`)"

    | Node type               | Maximum reservable | Read / Write speeds |
    |:------------------------|-------------------:|---------------------|
    | Hugemem (XL) nodes      | 13 TiB             | 6700 / 4000 MB/s    |
    | V (visualization nodes) | 6.5 TiB per user   | 6700 / 4000 MB/s    |

Reservable local scratch has not yet been implemented on visualization nodes (V).
Until it is available, jobs on these nodes can use the full `$TMPDIR` allocation shown above.

Once reservable local scratch is implemented, the amount of `$TMPDIR` available per user on visualization nodes will be reduced.

Users can also request temporary storage from a shared pool of
disaggregated NVMe resources, providing approximately 180 TB of
total usable capacity.
The storage is accessed over the network and appears as local
scratch storage within a Slurm job. See the [Roihu disk areas]
(disk.md#disaggregated-storage) documentation for details.

## Network

The network of Roihu is based on an InfiniBand NDR interconnect. Each CPU node
is connected to the network with one 200 Gb/s link, while in the GPU
partition there are four 200 Gb/s links per node, one per GPU.

## Software and programming environment

We provide a comprehensive stack of pre-installed HPC libraries and
scientific software on Roihu.
Instructions for installing applications are provided in
[the getting started with Roihu tutorial](../support/tutorials/roihu.md#installing-software)

The programming environment of Roihu includes:

* The GNU compiler stack
* The AOCC compiler stack
* CUDA and NVIDIA HPC Software Development Kit (SDK)
* OpenMPI as the main MPI library

Roihu also features a web interface for easy-to-use
interactive access and running graphical user interfaces.

A list of currently supported applications on Roihu can be found on the
[applications page](../apps/by_availability.md#roihu).

## Sensitive data services in Roihu

CSC supercomputers, including Roihu, are maintained according to the best practices of HPC
management: processes are planned and documented, systems are constantly monitored, and
security patches are applied without delay.
Further, all users log in using two-factor authentication.
Thus, these environments are quite secure by default.
However, CSC can't guarantee that there is no risk of a data breach, as
new security incidents emerge from time to time.

For use cases that require higher security, Roihu is being developed to support workflows
that require enhanced controls for handling sensitive and confidential data.
Roihu will introduce dedicated capabilities for regulated data workflows.

The sensitive data capability will be introduced after Roihu's initial availability.
Pilot use of the sensitive computing environment is currently estimated to begin in autumn 2026,
with general availability potentially following in early 2027, depending on the results and
experiences from the pilot phase.

The user workflow is expected to resemble CSC’s current Sensitive Data Desktop to HPC job submission model,
where sensitive data jobs are submitted from a secure environment (SD Desktop) and input/output data are
handled through protected data services (SD Connect). The jobs will be executed in job-specific isolated
environments that will not be able to access the internet or the shared disk areas of Roihu.

Read more about the [sensitive data services at CSC](../data/sensitive-data/index.md).

## More information

* [Getting started with Roihu](../support/tutorials/roihu.md)
* [Frequently asked questions](../support/faq/roihu.md)
* [See the latest Roihu presentation slides](https://a3s.fi/docs-files/roihu-presentation.pdf)
  (updated 2026-06-15)
* Do you have questions about Roihu?
  Please [contact CSC Service Desk](../support/contact.md), we're happy to
  help!

![Roihu supercomputer – now available for use!](https://a3s.fi/docs-files/ROIHU_MACHINE_Transp.png 'Roihu supercomputer – now available for use!')
