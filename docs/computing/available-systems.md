# Systems

CSC's computing environment consists of supercomputers Puhti and
Mahti, and the quantum learning machine Kvasi. Puhti and Mahti have a
fairly similar compute environment, and there is a wide range of
workloads that can utilize both efficiently. At the same time their
hardware is different, and this makes some worklods uniquely suitable
for either Puhti or Mahti. 

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

[A more technical description about Puhti](systems-puhti.md).

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
AI models that span multiple nodes. 

The selection of installed [scientific software](../apps/by_system.md#mahti) in
Mahti is more limited than in Puhti.

[A more technical description about Mahti](systems-mahti.md).


## Kvasi

**The Quantum Learning Machine**

Quantum computers differ from their classical counterparts when it comes to the basic 
computational operators. Before QPUs can be utilized, they require tailor-made programs 
and algorithms. With Kvasi, the user can explore and develop algorithms 
for quantum computers. Read here [detailed instructions on how to access](kvasi.md)

Kvasi provides an ecosystem for developing and simulating quantum algorithms in both 
ideal, and realistic, noisy conditions. With Kvasi, you can optimize your algorithm 
for a specific hardware (QPU), with specific connections and basic gate operations.

The algorithms can be developed either at a level close to the hardware, using 
the Atos Quantum Assembler (AQASM) language, or using a higher level, Python based 
language and ready-made libraries. The QLM comes with several ready-made examples.
You can also download and run locally [myQLM](./kvasi.md#myqlm) - a light-weight version of the 
QLM ecosystem.
