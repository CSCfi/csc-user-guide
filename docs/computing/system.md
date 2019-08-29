# Systems


## Puhti supercomputer

Puhti supercomputer was taken in use in August 2019. It is a cluster
system by Atos, with a variety of different node types. It is targeted
at a wide range of workloads, and also larger simulations can be run
before Mahti is in use.


**Puhti** has in total **682 CPU nodes**, with a theoretical peak
performance of 1.8 Petaflops. Each node is equiped with two latest
generation Intel Xeon processors, code name Cascade Lake, with 20
cores each running at 2.1 GHz.  Interconnect is based on HDR
InfiniBand by Mellanox. Nodes are connected with a 100Gbps HDR100
link, and the topology is a fat tree with a blocking factor of
approximately 2:1.

**Puhti-AI** Artificial intelligence partition has in total **80 GPU
nodes** with a total peak performance of 2.7 Petaflops. Each node has
two latest generation Intel Xeon processors, code name Cascade Lake,
with 20 cores each running at 2.1 GHz. They also have four Nvidia
Volta V100 GPUs with 32 GB of memory each. The nodes are equipped with
384 GB of main memory and 3.6 TB of fast local storage.

This partition is engineered to allow GPU intensive workloads to scale
well to multiple nodes. The interconnect is based on a dual rail
HDR100 interconnect network connectivity providing 200Gbps aggregate
bandwidth in a non-blocking fat-tree topology.


| Name      |  Number of nodes |  Compute       | Cores                  | Memory  | Local disk |     
|-----------|------------------|----------------|------------------------|---------|------------|
| M         |  532             | Xeon Gold 6230 | 2 x 20 cores @ 2.1 GHz | 192 GiB |            |
| L         |  92              | Xeon Gold 6230 | 2 x 20 cores @ 2.1 GHz | 384 GiB |            |
| IO        |  40              | Xeon Gold 6230 | 2 x 20 cores @ 2.1 GHz | 384 GiB |  3600 GiB  |
| XL        |  12              | Xeon Gold 6230 | 2 x 20 cores @ 2.1 GHz | 768 GiB |            |
| BM        |  12              | Xeon Gold 6230 | 2 x 20 cores @ 2.1 GHz | 1.5 TiB |            |
| GPU       |  80              | Xeon Gold 6230<br>Nvidia V100  | 2 x 20 cores @ 2.1 GHz<br> 4 GPUs connected with NVLink | 384 GiB<br>4 x 32GB |  3600 GiB  |




### Storage

Puhti has a 5+ PB Lustre parallel storage system providing space for home, project and scratch storage. 



     