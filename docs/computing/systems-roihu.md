# Technical details about Roihu

!!! note
    This page contains preliminary information about CSC's next national
    supercomputer Roihu, which is projected to be in researchers' use early
    2026. Please note that the details may evolve over time.

## Compute

**Roihu** will have a total of 486 CPU nodes and 132 GPU nodes. The
high-performance LINPACK (HPL) performance is estimated to be 10.5 PFlop/s for
the CPU nodes and 23.4 PFlop/s for the GPU nodes, resulting in an aggregate HPL
performance of 33.9 PFlop/s for the full system.

The CPU nodes will have two 192-core AMD Turin CPUs each, amounting to 186 624
CPU cores altogether. The CPUs are based on the AMD Zen 5 architecture, which
supports the AVX-512 vector instruction set.

Each GPU node will be equipped with 4 Nvidia GH200 GPUs, i.e., 528 GPUs in
total. Each GPU is accompanied by 72 ARM CPU cores for a total of 38 016 ARM
CPU cores on the GPU nodes.

The system will also provide special GPU nodes for visualization, as
well as huge memory nodes.

## Storage

Roihu will have 6.5 PiB of fully flash-based storage based on DDN EXAScaler.
This is divided into a 6.0 PiB scratch space and a 0.5 PiB disk area for
project applications and users' personal home directories.

The peak I/O performance of Roihu scratch space is expected to be around 200
GB/s for read and 170 GB/s for write. The home and projappl will have read and
write bandwidths of 120 GB/s and 100 GB/s, respectively.

## Network

The network of Roihu is based on Infiniband NDR interconnect. Each node will be
connected to the network with 200 Gb/s links.
