# Systems

CSC's computing environment consists of supercomputers Puhti and
Mahti, and the quantum learning machine Kvasi. Puhti and Mahti have a
fairly similar compute environment, and there is a wide range of
workloads that can utilize both efficiently. At the same time their
hardware is different, and this makes some worklods uniquely suitable
for either Puhti or Mahti.

In addition to the national resources, CSC's data center in Kajaani hosts the pan-European pre-exascale supercomputer LUMI. The CPU-partition of LUMI has been available since early 2022, while the largest partition of the system consisting of GPU-accelerated nodes is projected to be available in late 2022.

## LUMI

LUMI is one of the three European pre-exascale supercomputers. It's an HPE Cray EX supercomputer consisting of several partitions targeted for different use cases. The largest partition of the system is the "LUMI-G" partition consisting of GPU accelerated nodes using a future-generation AMD Instinct GPUs. In addition to this, there is a smaller CPU-only partition, "LUMI-C" that features AMD EPYC "Milan" CPUs and an auxiliary partition for data analytics with large memory nodes and some GPUs for data visualization. Besides partitions dedicated to computation, LUMI also offers several storage partitions for a total of 117 PB of storage space.

- [LUMI user documentation](https://docs.lumi-supercomputer.eu/)

- [A more technical description of LUMI](https://docs.lumi-supercomputer.eu/hardware/)

- [How does LUMI-C differ from Mahti?](lumi-vs-mahti.md)

## Puhti 

The Puhti supercomputer, Atos BullSequana X400 cluster based on Intel
CPUs, was launched on September 2, 2019. It has a powerful CPU
partition with almost 700 nodes with a range of memory sizes and local
storage options, all connected with a fast interconnect. Puhti allows
the user to reserve compute and memory resources flexibly, and the
user can run anything from interactive single core data processing to
medium scale simulations spanning multiple nodes. 

There are also 80 GPU nodes, with total of 320 Nvidia Volta V100 GPUs. This partition is
suitable for all kinds workloads capable of utilizing GPUs, even heavy
AI models that span multiple nodes. 

Puhti has  wide selection of [scientific software](../apps/by_system.md#puhti) installed.

- [A more technical description of Puhti](systems-puhti.md)

## Mahti

The Mahti supercomputer, Atos BullSequana XH2000 system based on AMD
CPUs, was launched on August 26, 2020. Mahti is designed for
massively parallel jobs requiring high floating point performance and
a fast interconnect. The system has in total 1404 nodes equipped with
powerful AMD Rome CPUs. These are connected with a fast interconnect,
allowing jobs to scale across the full system. In Mahti user reserves
full nodes so that the jobs can extract full performance from each
node. Mahti is in particular geared towards medium to large scale
simulations requiring Petaflops of compute power. Also smaller
parellel workloads that are able to use full nodes efficiently can
utilize Mahti. 

There are also 24 GPU nodes, with total of 96 Nvidia Ampere A100 GPUs. This partition is
suitable for all kinds workloads capable of utilizing GPUs, even heavy
AI models that span multiple nodes. A subset of the A100 GPUs are sliced into smaller GPUs 
with one seventh of the compute and memory capacity of a full A100 GPU. These can be used for 
interactive workloads, courses and code development.

The selection of installed [scientific software](../apps/by_system.md#mahti) in
Mahti is more limited than in Puhti.

- [A more technical description of Mahti](systems-mahti.md)
