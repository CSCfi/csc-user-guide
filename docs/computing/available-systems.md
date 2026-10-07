# Systems

!!! note "Puhti and Mahti have been decommissioned"
    Puhti and Mahti have been replaced by Roihu, CSC's next-generation
    supercomputer. Their storage and login nodes remain available until
    15 October 2026 for data migration purposes only.

    [Learn more about Roihu :material-arrow-right:](systems-roihu.md)

CSC's computing environment consists of the national supercomputer Roihu, which
replaced the retired Puhti and Mahti systems in 2026. In addition, CSC's data
center in Kajaani hosts the pan-European pre-exascale supercomputer LUMI. The
CPU-partition of LUMI has been available since early 2022, while the largest
partition of the system consisting of GPU-accelerated nodes became available
in 2023.

## Roihu

The Roihu supercomputer, BullSequana XH3000 hybrid system, is CSC's
national supercomputer, replacing the retired Puhti and Mahti systems.
Roihu is designed as a versatile system for CPU and GPU computing, AI workloads,
data-intensive research and applications requiring large memory.

Roihu consists of two main partitions: **Roihu-CPU** and **Roihu-GPU** that have separate login nodes
and software environments. The CPU partition contains AMD EPYC
CPUs, while the GPU partition is based on NVIDIA GH200 Grace Hopper Superchips.
The system also includes special-purpose nodes for visualization and high-memory
tasks, and will provide enhanced support for processing sensitive and confidential data.

- [More information about Roihu](systems-roihu.md)

## LUMI

LUMI is one of the three European pre-exascale supercomputers. It's an HPE Cray
EX supercomputer consisting of several partitions targeted for different use
cases. The largest partition of the system is the "LUMI-G" partition consisting
of GPU accelerated nodes using a future-generation AMD Instinct GPUs. In
addition to this, there is a smaller CPU-only partition, "LUMI-C" that features
AMD EPYC "Milan" CPUs and an auxiliary partition for data analytics with large
memory nodes and some GPUs for data visualization. Besides partitions dedicated
to computation, LUMI also offers several storage partitions for a total of 117
PB of storage space.

- [LUMI user documentation](https://docs.lumi-supercomputer.eu/)
- [A more technical description of LUMI](https://docs.lumi-supercomputer.eu/hardware/)
