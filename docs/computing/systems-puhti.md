---
search:
  boost: 2
---

# Technical details about Puhti

### Compute

**Puhti** has a total of **682 CPU nodes**, with a theoretical peak
performance of 1,8 petaflops. Each node is equipped with two Intel
Xeon processors, code name _Cascade Lake_, with 20 cores each running
at 2,1 GHz. The cores support AVX-512 vector instructions and VNNI
instructions for AI _inference_ workloads. The interconnect is based
on Mellanox HDR InfiniBand. The
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
| M         |  484             | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 192 GiB |            |
| M-IO      |  48              | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 192 GiB |  1490 GiB  |
| L         |  92              | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 384 GiB |            |
| L-IO      |  40              | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 384 GiB |  3600 GiB  |
| XL        |  12              | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 768 GiB |  1490 GiB  |
| BM-IO     |  6               | Xeon Gold 6230 | 2 x 20 cores @ 2,1 GHz | 1,5 TiB |  5960 GiB  |
| GPU       |  80              | Xeon Gold 6230<br>Nvidia V100  | 2 x 20 cores @ 2,1 GHz<br> 4 GPUs connected with NVLink | 384 GiB<br>4 x 32 GB |  3600 GiB  |

In addition to the compute nodes above, Puhti has two login nodes with 40 cores and 2900 GiB
[local disk](disk.md#login-nodes) each.


### Storage

Puhti has a 4.8 PB Lustre parallel storage system providing space for
[home](disk.md#home-directory), [project](disk.md#projappl-directory) and
[scratch](disk.md#scratch-directory) storages.

Current Lustre configuration for Puhti is:

| Storage area | # OSTs | # MDTs |
|--------------|--------|--------|
| home         |  24    |   4    |
| projappl     |  24    |   4    |
| scratch      |  24    |   4    |

Please see [Lustre documentation](lustre.md) for the terminology.

All the OSTs and MDTs are shared across the storage areas, thus the
performance should be similar between them. The peak I/O performance
in Puhti is around ~50 GB/s with 64 compute nodes under dedicated
access to the system.
