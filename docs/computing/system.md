# Systems


## Puhti supercomputer

Puhti supercomputer was taken in use in August 2019. It is a cluster
system by Atos, with a variety of different node types. It is targeted
at a wide range of workloads, and also larger simulations can be run
before Mahti is in use.


### CPU nodes

Puhti has in total 682 CPU nodes, with a theoretical peak performance
of 1.8 Petaflops. Each node is equiped with two latest generation
Intel Xeon processors, code name Cascade Lake, with 20 cores each
running at 2.1 GHz (Xeon Gold 6230). 


The 682 compute nodes have a mix of memory sizes:

   * 192 GB on 532 nodes
   * 384 GB on 132 nodes, with 40 also containing a 3.6 TB NVMe disk for fast local storage
   * 768 GB on 12 nodes
   * 1.5 TB on 6 nodes

Interconnect is based on HDR InfiniBand by Mellanox. Nodes are connected
with a 100Gbps HDR100 link, and the topology is a fat tree with a
blocking factor of approximately 2:1.


### GPU nodes

The Puhti-AI Artificial intelligence partition has in total 80 nodes
with a total peak performance of 2.7 Petaflops. Each node has two
latest generation Intel Xeon processors, code name Cascade Lake, with
20 cores each running at 2.1 GHz (Xeon Gold 6230). They also have four
Nvidia Volta V100 GPUs with 32 GB of memory each. The nodes are
equipped with 384 GB of main memory and 3.6 TB of fast local storage.

This partition is engineered to allow GPU intensive workloads to scale
well to multiple nodes. The interconnect is based on a dual rail
HDR100 interconnect network connectivity providing 200Gbps aggregate
bandwidth in a non-blocking fat-tree topology.
     


### Storage

Puhti has a 5+ PB Lustre parallel storage system providing space for home, project and scratch storage. 



     