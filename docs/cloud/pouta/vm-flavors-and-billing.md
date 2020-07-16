# Virtual machine flavors and billing unit rates

This article lists the types (flavors) of virtual machines and their
cost in billing units.

[TOC]

The cPouta and ePouta services consume the same billing units as 
Puhti and Mahti. You can find more information in the [CSC computing
environment articles].

Users can create virtual machines with larger or
smaller compute resources based on their needs. The virtual
machine *flavors* available in cPouta and ePouta are listed below in
separate tables.

**New prices from 18.3.2019 onwards. The prices before 18.3.2019
are shown in parentheses.**

## cPouta flavors

The following tables list the available virtual machine flavors in cPouta and their
billing unit coefficients.
Note that the default cPouta user account
allows users to launch only a subset of the available virtual machine
flavors.

### Standard flavors

|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|standard.tiny   |1|1 |80 |0 |80 |1  |0.25 (0.5)|
|standard.small  |2|2 |80 |0 |80 |1  |0.5 (1)|
|standard.medium |3|4 |80 |0 |80 |1.3|1 (2)|
|standard.large  |4|8 |80 |0 |80 |2  |2 (4)|
|standard.xlarge |6|16|80 |0 |80 |2.6|4 (8)|
|standard.xxlarge|8|32|80 |0 |80 |4  |8 (16)|
|standard.3xlarge|8|64|80 |0 |80 |8  |16|

**\*** Because not all memory amounts round exactly to GiB, the closest value
has been used. This applies to all tables.

### HPC flavors

|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| hpc.4.5core     | 5  | 22  | 80          | 0 | 80 | 4.3 | 6 (10)    |
| hpc.4.10core    | 10 | 43  | 80          | 0 | 80 | 4.3 | 12 (20)   |
| hpc.4.20core    | 20 | 86  | 80          | 0 | 80 | 4.3 | 25 (40)   |
| hpc.4.40core    | 40 | 172 | 80          | 0 | 80 | 4.3 | 50 (80)   |
| hpc.4.80core    | 80 | 344 | 80          | 0 | 80 | 4.3 | 100 (160) |
| hpc-gen2.24core | 24 | 120 | 80  (RAID0) | 0 | 80 | 5   | 30 (45)   |
| hpc-gen2.48core | 48 | 240 | 80  (RAID0) | 0 | 80 | 5   | 60 (90)   |

### I/O flavors

|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| io.70GB  | 2  | 10 | 20 (SSD/RAID0) | 70 (SSD/RAID0)  | 90  | 5 | 3 (5)   |
| io.160GB | 4  | 20 | 20 (SSD/RAID0) | 160 (SSD/RAID0) | 180 | 5 | 6 (19)  |
| io.340GB | 8  | 40 | 20 (SSD/RAID0) | 340 (SSD/RAID0) | 360 | 5 | 12 (20) |
| io.700GB | 16 | 80 | 20 (SSD/RAID0) | 700 (SSD/RAID0) | 720 | 5 | 24 (40) |

### GPU flavors

|Flavor|Cores|GPUs |Memory <br/>(* GiB)|Disk (root) GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| gpu.1.1gpu | 14 | 1 | 120 | 80 (SSD/RAID1) | 80 | 8.5 | 60  |
| gpu.1.2gpu | 28 | 2 | 240 | 80 (SSD/RAID1) | 80 | 8.5 | 120 |
| gpu.1.4gpu | 56 | 4 | 480 | 80 (SSD/RAID1) | 80 | 8.5 | 240 |

## ePouta flavors

The following tables list the available virtual machine flavors in ePouta and their
billing unit coefficients.

### Standard flavors

|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| standard.tiny    | 1 | 1  | 80 | 0 | 80 | 1   | 0.25 (0.5) |
| standard.small   | 2 | 2  | 80 | 0 | 80 | 1   | 0.5 (1)    |
| standard.medium  | 3 | 4  | 80 | 0 | 80 | 1.3 | 1 (2)      |
| standard.large   | 4 | 8  | 80 | 0 | 80 | 2   | 2 (4)      |
| standard.xlarge  | 6 | 16 | 80 | 0 | 80 | 2.6 | 4 (8)      |
| standard.xxlarge | 8 | 32 | 80 | 0 | 80 | 4   | 8 (16)     |
| standard.3xlarge | 8 | 64 | 80 | 0 | 80 | 8   | 16         |

### HPC flavors

|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| hpc.fullnode.haswell | 46 | 242 | 80 | 0 | 80 | 5.4 | 72 (120)  |
| hpc.3.28core         | 28 | 120 | 80 | 0 | 80 | 4.4 | 48 (70)   |
| hpc.3.56core         | 56 | 240 | 80 | 0 | 80 | 4.4 | 96 (140)  |
| hpc.4.5core          | 5  | 22  | 80 | 0 | 80 | 4.4 | 8 (12)    |
| hpc.4.10core         | 10 | 45  | 80 | 0 | 80 | 4.5 | 15 (23)   |
| hpc.4.20core         | 20 | 90  | 80 | 0 | 80 | 4.4 | 30 (45)   |
| hpc.4.40core         | 40 | 180 | 80 | 0 | 80 | 4.4 | 60 (90)   |
| hpc.4.80core         | 80 | 360 | 80 | 0 | 80 | 4.4 | 120 (180) |

### I/O flavors

|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| io.haswell.2core  | 2  | 10  | 20 | 70   | 90   | 5   | 4.5 (7)   |
| io.haswell.4core  | 4  | 20  | 20 | 160  | 180  | 5   | 9 (13)    |
| io.haswell.8core  | 8  | 40  | 20 | 350  | 370  | 5   | 18 (25)   |
| io.haswell.16core | 16 | 80  | 20 | 700  | 720  | 5   | 36 (50)   |
| io.haswell.32core | 32 | 160 | 20 | 1400 | 1420 | 5   | 72 (100)  |
| io.haswell.46core | 46 | 242 | 20 | 2100 | 2120 | 5.4 | 108 (150) |

### High memory flavors

|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| tb.3.480RAM  | 56 | 480  | 20 (SSD/RAID0) | 1650 (NVMe/RAID0) | 1730 | 8.5  | 110 (240) |
| tb.3.1470RAM | 80 | 1470 | 80 (SSD/RAID0) | 2500 (NVMe/RAID0) | 2580 | 18.3 | 320 (600) |

### GPU flavors

|Flavor|Cores|GPUs|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| gpu.1.1gpu | 14 | 1 | 120 | 80 (SSD/RAID1) | 0 | 80 | 8.5 | 60  |
| gpu.1.2gpu | 28 | 2 | 240 | 80 (SSD/RAID1) | 0 | 80 | 8.5 | 120 |
| gpu.1.4gpu | 56 | 4 | 480 | 80 (SSD/RAID1) | 0 | 80 | 8.5 | 240 |
| gpu.2.1gpu | 20 | 1 | 180 | 80 (SSD/RAID0) | 1000 (SSD/RAID0) | 1080 | 9 | 100 (140) |

**\*** Because not all memory amounts round exactly to GiB, the closest value
has been used.

Please note: The flavors in the two tables are slightly different.
This is because
different hardware is used in the two clouds. Any storage with a
comment in parentheses such as (SSD/RAID0) 
is local to the compute node. In ePouta, the HPC root disks
and standalone volumes are hosted in the centralized Ceph block
storage system.

## Which type of flavor should I use?

### **Standard flavors**

Typical use cases:

-   Web services (non-HPC)
-   Software development

These are generic flavors that are useful for running regular web
services such as a web server with a database backend. 
They provide better availability compared to the
HPC flavors.

Cloud administrators can move these virtual machines from one host
machine to another without causing a break in service. This means that
you are likely less affected by maintenance.

These flavors are not suitable for computationally intensive
workloads. The virtual CPUs used in these instances are
overcommitted, which means 32 hyperthreaded CPU cores are used to
provide more than 32 virtual cores.

**Flavor characteristics:**

-   Redundant power
-   CPU: Varies
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node or disk failures may cause downtime, but instances
    are recoverable.

### **HPC flavors**

Typical use cases:

-   Scientific applications

If your use case is computationally intensive, you should use one of
the HPC flavors. The availability of these instances is not as high
as the standard flavors, but you get better performance. The HPC
flavors have faster CPUs and no overcommitment of CPU cores.

**cPouta HPC flavor characteristics:**

**hpc.4.\*:**

-   Not redundant power
-      CPU:   Intel(R)    Xeon(R)   Gold    6148   CPU    @   2.40GHz,
    ***hyper-threading***
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node or disk failures may cause downtime, but instances
    are recoverable.

**hpc-gen2.\*:**

-   No redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Single 40 Gb/s
-   Flavor disk: Local SATA disk, no RAID
-   Instances can be lost due to a single-node or disk failure.

**ePouta HPC flavor characteristics:**

**hpc.4\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU Gold 6148, with hyper-threading
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node or disk failures may cause downtime, but instances
    are recoverable.

**hpc.3\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v4, with hyper-threading
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node or disk failures may cause downtime, but instances
    are recoverable.

**hpc.\*.haswell:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2690 v3, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node or disk failures may cause downtime, but instances
    are recoverable.

### **I/O flavors**

Typical use cases:

-   Hadoop/Spark
-   Non-critical centralized databases
-   Clustered databases

I/O flavors are intended to provide the best I/O performance on the
virtual machine root and ephemeral disks. They are backed by local
SSDs on the servers they run on. The SSDs are configured in a RAID-0
configuration for maximal performance. This means there is an
increased risk of loss of a virtual machine in case of hardware
problems. The risk of disk failure is larger than in the other
flavors, so it is especially important to be aware of the risks of
data loss with these flavors.

As these instances are also tightly tied to the hardware, you may
expect downtime of instances during the maintenance of the hardware.
Resize/migration functionality neither works for these instances.
The bulk of the storage is available as an ephemeral disk, typically
in /dev/vdb.

Often you want to create clusters of servers with the io.\*
flavors. In these cases, you probably want to have your virtual
machines land on different physical servers. This cannot currently be
done in the web interface. To do this, please refer to the
anti-affinity group commands in our [command line instructions].

The availability of these instances is not as high as the
standard flavors, but the I/O
performance is significantly better. Maintenance work can cause a larger disruption, and the
resize functionality does not work.

**cPouta IO flavor characteristics:**

**io.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Redundant 10 Gb/s or 40 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Instances can be lost due to a single-node or disk failure.

**ePouta IO flavor characteristics:**

**io.haswell.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Instances can be lost due to a single-node or disk failure.

### GPU flavors

Typical use cases:

-   High performance compute applications leveraging GPUs
-   Machine and deep learning, e.g. [TensorFlow]
-   Rendering

The GPU flavors are intended to provide high performance computing using
GPGPU (General Purpose computing on Graphical Processing
Units). GPGPUs can significantly speed up certain algorithms and
applications. The gpu.1. flavors have NVIDIA Tesla P100 GPGPUs.
The gpu.2.1gpu in ePouta have a NVIDIA Tesla V100 GPGPU.

The GPGPUs are suitable for deep learning, scientific computing as
well as for remote desktops, rendering or visualization. The GPGPU
flavors are backed by local SSD on the servers. The SSDs in gpu.1 flavors
are configured in RAID-1. This is where the OS root disk is stored. With
gpu.2 flavors, the SSDs are bigger and he SSDs are configured in RAID-0
for faster staging of datasets. You can use the volumes for storing larger
data sets and persistent data. If you need to read and write a lot of data
between the disk and GPGPU, using volumes might affect performance when
compared to local SSD disk.

To take advantage of the acceleration which GPGPUs provide, the
applications you run must support them. If you write
your own applications, the [optimization service] helps in
leveraging the GPGPUs.

GPGPUs can be used for a lot of cool and interesting things,
but please remember the resource usage must comply with the [Terms of
use].

Limitations and caveats: 

-   As we use PCI passthrough to get the whole GPGPU into the
    instance. The administrators are not able to access the GPGPU and
    check its health. Please report any errors or problems with the GPGPUs
    to CSC (and attach the output of the command "nvidia-smi -q").
-   The applications must be able to utilize the GPU to get a speedup.

These instances are also tightly tied to the hardware. You may expect
downtime of instances during the maintenance of the hardware.

Users also have the possibility to use NVIDIA Volta V100 GPGPUs in the
batch system on Puhti-AI: <https://research.csc.fi/techspecs>.

**cPouta flavor characteristics:**

**gpu.1.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v4, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-1
-   Instance can be lost due to a single-node or disk failure.

**ePouta flavor characteristics:**

**gpu.1.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v4, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-1
-   Instance can be lost due to a single-node or disk failure.

**gpu.2.\*:**

-   Only available via request to servicedesk@csc.fi
-   Redundant power
-   CPU: Intel(R) Xeon(R) Gold 6148, with hyper-threading
-   NUMA Aware: yes (CPU &lt;&gt; memory, not PCI devices)
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Instance can be lost due to a single-node or disk failure.

### Installation and configuration of GPU Flavors

We have specific CUDA images available for the GPU nodes.
These images come pre-installed with the freshest CUDA version. Note
that the CUDA images are not configured with auto update. You can use
any other images with the GPU flavors, but you have
to install the required libraries yourself.
[How CSC customizes the images](adding-images.md).

### High memory flavors (only in ePouta)

Typical use cases:

-   Scientific applications requiring large amounts of memory

These flavors have large amounts of memory and are meant for use cases
which require and can utilize such amounts of memory. Typical use cases
of these flavors include scientific applications with huge memory
requirements, for example Gnome sequencing and analysis applications.

The resize/migration functionality does not work for these instances.

If you need to move a workload from another type of VM to a TB
instance, either move all data and install all applications manually
on the new TB VM or create a snapshot of the source VM. Then
convert that snapshot to a volume and use the volume to create the
new TB-flavor VM.

If you need to move a workload from a TB instance to another instance,
either move all data and install all applications manually on a new
VM or create a snapshot of the source VM. **Please note** that all
ephemeral disk data will be lost in the process and will not be stored
in the snapshot, only the TB VM root disk.

**Flavor characteristics:**

**tb.3.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU  E5-2680 v4, with hyper-threading **or**
    Intel(R) Xeon(R) CPU E5-2698 v4, with hyper-threading
-   Network: Redundant 25 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Instances can be lost due to a single-node or disk failure.

## Deprecated flavors

This is the set of original flavors that has been available
since the launch. **You should not launch any new virtual machines using
any of these flavors. Existing
virtual machines that use these flavors will continue to
work.** We will maintain these flavors for a period of time,
but they will be removed at some point in the near future.

|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| hpc-gen1.1core  | 1  | 3.7 | 80 (RAID0)  | 0            | 80  | 3.7 | 2  |
| hpc-gen1.4core  | 4  | 15  | 80 (RAID0)  | 0            | 80  | 3.7 | 8  |
| hpc-gen1.8core  | 8  | 30  | 80 (RAID0)  | 0            | 80  | 3.7 | 16 |
| hpc-gen1.16core | 16 | 60  | 80 (RAID0)  | 0            | 80  | 3.7 | 32 |
| hpc-gen2.2core  | 2  | 10  | 80 (RAID0)  | 0            | 80  | 5   | 4  |
| hpc-gen2.8core  | 8  | 40  | 80 (RAID0)  | 0            | 80  | 5   | 15 |
| hpc-gen2.16core | 16 | 80  | 80 (RAID0)  | 0            | 80  | 5   | 30 |
| tiny            | 1  | 1   | 10  (RAID0) | 110 (RAID0)  | 120 | 1   | 2  |
| mini            | 1  | 3.5 | 10  (RAID0) | 110 (RAID0)  | 120 | 1.7 | 2  |
| small           | 4  | 15  | 10  (RAID0) | 220  (RAID0) | 230 | 3.8 | 8  |
| medium          | 8  | 30  | 10  (RAID0) | 440  (RAID0) | 450 | 3.8 | 16 |
| large           | 12 | 45  | 10  (RAID0) | 660  (RAID0) | 670 | 3.8 | 24 |
| fullnode        | 16 | 60  | 10  (RAID0) | 900  (RAID0) | 910 | 3.8 | 32 |
| hpc.mini              | 2  | 3.5 | 80         | 0            | 80   | 1.8  | 5   |
| hpc.small             | 4  | 7   | 80         | 0            | 80   | 1.8  | 10  |
| hpc.medium.haswell    | 8  | 40  | 80         | 0            | 80   | 5    | 20  |
| hpc.large.haswell     | 16 | 80  | 80         | 0            | 80   | 5    | 40  |
| hpc.xlarge.haswell    | 32 | 156 | 80         | 0            | 80   | 5    | 80  |
| hpc.medium.westmere   | 8  | 14  | 80         | 0            | 80   | 1.8  | 8   |
| hpc.large.westmere    | 16 | 28  | 80         | 0            | 80   | 1.8  | 16  |
| hpc.xlarge.westmere   | 23 | 41  | 80         | 0            | 80   | 1.8  | 24  |
| hpc.largemem.westmere | 23 | 90  | 80         | 0            | 80   | 4    | 36  |
| tb.4.735RAM  | 80 | 735  | 80 (SSD/RAID0) | 3300 (SSD/RAID0)  | 3380 | 9.2  | 220 (350) |
| tb.westmere.32core    | 32 | 488 | 80 (RAID6) | 3250 (RAID6) | 3330 | 15.2 | 200 |
| tb.westmere.64core    | 64 | 976 | 80 (RAID6) | 6500 (RAID6) | 6580 | 15.2 | 400 |

  [CSC computing environment articles]: https://research.csc.fi/computing
  [command line instructions]: command-line-tools.md
  [TensorFlow]: https://www.tensorflow.org
  [Optimization service]: https://research.csc.fi/optimization-service
  [Terms of Use]: https://https://research.csc.fi/pouta-user-policy
  [https://research.csc.fi/pouta-adding-images]: 
