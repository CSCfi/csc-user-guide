# Systems



The Puhti supercomputer was launched on September 2, 2019. It is an
Atos cluster system with a variety of different node types. It is
targeted at a wide range of workloads, e.g. single core to medium sized
jobs, AI workloads, jobs requiring large amounts of memory or local scratch space.

The Mahti supercomputer will be launched in April, 2020 (FIXME). It is
a watercooled Atos BullSequana XH2000 system with a uniform set of
compute nodes with a large amount of cores and a very powerful
interconnect.  It is targeted at medium to large workloads, each
utilizing full nodes. Also, there are no local disks or GPUs in the system.


Both of them have a fairly similar compute environment, and there is a
wide range of workloads that can utilize both efficiently. At the same
time their hardware is different, and this makes some workloads
uniquely suitable for either Puhti or Mahti.


!!! warning "Login nodes: important note for Puhti and Mahti"
    The login nodes can be used for **light** pre- and postprocessing, compiling
    applications and moving data. All other tasks are to be done in the 
	compute nodes using the [batch job system](running/getting-started.md). 
	Programs not adhering to these rules will be terminated without warning. 
	Note that compute nodes can be used also [interactively](running/interactive-usage.md)


## Puhti  



### Compute

**Puhti** has a total of **682 CPU nodes**, with a theoretical peak
performance of 1,8 petaflops. Each node is equipped with two Intel
Xeon processors, code name _Cascade Lake_, with 20 cores each running
at 2,1 GHz. The interconnect is based on Mellanox HDR InfiniBand. The
nodes are connected with a 100 Gbps HDR100 link, and the topology is a
fat tree with a blocking factor of approximately 2:1.

The **Puhti AI** artificial intelligence partition has a total of **80 GPU
nodes** with a total peak performance of 2,7 petaflops. Each node has
two latest generation Intel Xeon processors, code name _Cascade Lake_,
with 20 cores each running at 2,1 GHz. They also have four Nvidia
Volta V100 GPUs with 32 GB of memory each. The nodes are equipped with
384 GB of main memory and 3,6 TB of fast local storage. This partition
is engineered to allow GPU-intensive workloads to scale well across
multiple nodes. The interconnect is based on a dual-rail HDR100
interconnect network connectivity providing 200 Gbps of aggregate
bandwidth in a non-blocking fat-tree topology.


### Nodes


| Name      |  Number of nodes |  Compute       | Cores                  | Memory  | Local disk |     
|-----------|------------------|----------------|------------------------|---------|------------|
| M         |  532             | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 192 GiB |            |
| L         |  92              | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 384 GiB |            |
| IO        |  40              | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 384 GiB |  3600 GiB  |
| XL        |  12              | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 768 GiB |            |
| BM        |  12              | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 1,5 TiB |            |
| GPU       |  80              | Xeon Gold 6230<br>Nvidia V100  | 2 x 20 cores @ 2,1 GHz<br> 4 GPUs connected with NVLink | 384 GiB<br>4 x 32 GB |  3600 GiB  |

In addition to the compute nodes above, Puhti has two login nodes with 40 cores and 2900 GiB
[local disk](disk.md#login-nodes) each. 


### Storage

Puhti has a 4.8 PB Lustre parallel storage system providing space for [home](disk.md#home-directory), 
[project](disk.md#projappl-directory) and [scratch](disk.md#scratch-directory) storages. 


## Mahti


### Compute 

**Mahti** has a total of **1404 CPU nodes**, with a theoretical peak
performance of 7.5 Petaflops. Each node is equipped with two AMD EPYC
7H12 processors, code name _Rome_, with 64 cores each running at 2,6
GHz. This means that there are in total 128 physical cores per node
each of which can run two threads using symmetric
multithreading. There is 256 GiB of memory per node, and no local
disks.

The interconnect is based on Mellanox HDR InfiniBand. The nodes are
connected with a 200 Gbps HDR link, and the topology is dragonfly+. A
dragonfly+ topology consists of multiple groups of node, each of which
is internally connected with a fat tree topology. Between the groups
there is all-to-all connectivity connecting the different groups
together. In Mahti there are 3 cabinets with 234 nodes in each group
(also called cell). These are connected with a 1.7:1 blocking fat
tree. There are in total 6 groups, and between the groups there is
fully non-blocking all-to-all connectivity. The total bisection
bandwidth is 87 Tbps (CHECKME). 

### Storage

Mahti has a 8.7 PB Lustre parallel storage system providing space for [home](disk.md#home-directory), 
[project](disk.md#projappl-directory) and [scratch](disk.md#scratch-directory) storages. 


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
