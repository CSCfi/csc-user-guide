# Virtual machine flavors and billing unit rates

This article lists the types (flavors) of virtual machines and their
cost in billing units.

[TOC]

The cPouta and ePouta services consume the same billing units as 
Puhti and Mahti. You can find more information in the [CSC computing environment articles].

Users can create virtual machines with larger or
smaller compute resources based on their needs. The virtual
machine *flavors* available in cPouta and ePouta are listed below in
separate tables.
Please note that the values for the memory of each flavor (in GiB) are approximated.


## About redundancy

In addition to the amount of cores, memory, and disk, the flavors we offer vary also on the level of redundancy of the nodes hosting the virtual machines.
The details on the levels of redundancy follow.

### Power redundancy

For the power provisioning of the node hosting the virtual machine, there are two possible values of redundancy.

* ![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg) **NONE** - The node is not protected from sudden power losses. **A fault in the power provisioning of the node might make the virtual machine temporarily unreachable**.
* ![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg) **FULL** - The node is protected from sudden power losses (UPS).

### Data redundancy

Within each virtual machine, the customer data is stored in a root disk (R) and possibly in an [ephemeral disk (E)](ephemeral-storage.md).
For customer data, there are three possible values of redundancy.  
We also offer the possibility to store the data in a [persistent volume (FULL)](persistent-volumes.md)

* ![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg) **NONE** - The disk is stored only in the node running the virtual machine and it is not backed up (RAID-0 or LVM striping). **A fault in one of the disks of the node might corrupt the data of the virtual machine**. Moreover, **a fault in the node hosting the virtual machine might make the virtual machine not usable until the fault is fixed**.
* ![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg) **BASIC** - The disk is stored only in the node running the virtual machine and it is mirrored within the same node (RAID-1). A fault in a single disk of the node does not compromise the data of the virtual machine. **Simultaneous faults in multiple disks of the node might corrupt the data of the virtual machine**. Moreover, **a fault in the node hosting the virtual machine might make the virtual machine not usable until the fault is fixed**.
* ![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for ephemeral disk data redundancy level FULL](../../img/circle_icons/e100.svg) **FULL** - The disk is stored using multiple nodes in a fault-tolerant fashion (Ceph), so the customer data is not tied to any specific node. In case of a fault in a node used by the customer, it is possible to re-spawn the virtual machine of the customer using an alternative node.

### Network redundancy

For the network reachability of the virtual machine, there are two possible values of redundancy.

* ![Icon for network reachability redundancy level NONE](../../img/circle_icons/n0.svg) **NONE** - The node hosting the virtual machine is connected to the cloud platform without a failover link. **A fault in the link of the node might make the virtual machine temporarily unreachable**.
* ![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg) **FULL** - The node hosting the virtual machine is connected to the cloud platform with an additional failover link.

## cPouta flavors

The following tables list the available virtual machine flavors in cPouta and their
billing unit coefficients.
Note that the default cPouta user account
allows users to launch only a subset of the available virtual machine
flavors.

### Standard flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|standard.tiny   |1|0.9 |80 |0 |80 |0.9  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)|0.25 |
|standard.small  |2|1.9  |80 |0 |80 |0.9  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)|0.5  |
|standard.medium |3|3.9 |80 |0 |80 |1.3|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)|1    |
|standard.large  |4|7.8 |80 |0 |80 |1.9|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)|2    |
|standard.xlarge |6|15 |80 |0 |80 |2.5|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)|4    |
|standard.xxlarge|8|31 |80 |0 |80 |3.8|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)|8    |
|standard.3xlarge|8|62 |80 |0 |80 |7.7|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)|16   |

### HPC flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| hpc.6.14core    | 14 | 88  | 80 | 0 | 80 | 6.2|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 23 |
| hpc.6.28core    | 28 | 176 | 80 | 0 | 80 | 6.2|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 45 |
| hpc.6.56core   | 56 | 352 | 80 | 0 | 80 | 6.2|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 90 |
| hpc.6.112core   | 112| 705 | 80 | 0 | 80 | 6.2|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 180 |
| hpc.5.16core    | 16 | 58  | 80 | 0 | 80 | 3.6|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 20 |
| hpc.5.32core    | 32 | 116 | 80 | 0 | 80 | 3.6|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 40 |
| hpc.5.64core   | 64 | 232 | 80 | 0 | 80 | 3.6|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 80 |
| hpc.5.128core   | 128| 464 | 80 | 0 | 80 | 3.6|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 160 |
| hpc.4.5core     | 5  | 21  | 80 | 0 | 80 | 4.2   |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 6   |
| hpc.4.10core    | 10 | 42  | 80 | 0 | 80 | 4.2   |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 12  |
| hpc.4.20core    | 20 | 85  | 80 | 0 | 80 | 4.2 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 25  |
| hpc.4.40core    | 40 | 171 | 80 | 0 | 80 | 4.2 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 50  |
| hpc.4.80core    | 80 | 343 | 80 | 0 | 80 | 4.2 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 100 |
| hpc-gen2.24core | 24 | 117 | 80 | 0 | 80 | 4.8 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for network reachability redundancy level NONE](../../img/circle_icons/n0.svg)    | 30  |
| hpc-gen2.48core | 48 | 234 | 80 | 0 | 80 | 4.8 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for network reachability redundancy level NONE](../../img/circle_icons/n0.svg)    | 60  |

Note that the root disks of the hpc-gen2.24core and the hpc-gen2.48core flavors are hosted on hard disk drives (HDDs).

### I/O flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| io.70GB  | 2  | 9.7 | 20 | 70  | 90  | 4.8   |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 3  |
| io.160GB | 4  | 19 | 20 | 160 | 180 | 4.7   |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 6  |
| io.340GB | 8  | 39 | 20 | 340 | 360 | 4.8 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 12 |
| io.700GB | 16 | 78 | 20 | 700 | 720 | 4.8 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 24 |
| io.2.80GB  | 2  | 12,7 | 80 | 80  | 160  | 6.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 6  |
| io.2.240GB  | 4 | 26 | 80 | 240  | 320  | 6.6 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 12  |
| io.2.550GB  | 8  | 54 | 80 | 550  | 630  | 6.7 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 24  |
| io.2.1200GB  | 16  | 107 | 80 | 1200  | 1280  | 6.7 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 48  |

Note that both the root and the ephemeral disks of all I/O flavors are hosted on solid-state drives (SSDs).

### GPU flavors

|Flavor|Cores|GPUs|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| gpu.1.1gpu | 14 | 1 | 117 | 80 |0 | 80 | 8.3 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 60  |
| gpu.1.2gpu | 28 | 2 | 234 | 80 |0 | 80 | 8.3 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 120 |
| gpu.1.4gpu | 56 | 4 | 468 | 80 |0 | 80 | 8.3 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 240 |

Note that the root disks of all GPU flavors are hosted on solid-state drives (SSDs).

## ePouta flavors

The following tables list the available virtual machine flavors in ePouta and their
billing unit coefficients.

### Standard flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| standard.tiny    | 1 | 0.9  | 80 | 0 | 80 | 0.9   |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 0.25 |
| standard.small   | 2 | 1.9  | 80 | 0 | 80 | 0.9   |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 0.5  |
| standard.medium  | 3 | 3.9  | 80 | 0 | 80 | 1.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 1    |
| standard.large   | 4 | 7.8  | 80 | 0 | 80 | 1.9 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 2    |
| standard.xlarge  | 6 | 15 | 80 | 0 | 80 | 2.5 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 4    |
| standard.xxlarge | 8 | 31 | 80 | 0 | 80 | 3.8 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 8    |
| standard.3xlarge | 8 | 62 | 80 | 0 | 80 | 7.7 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 16   |

### HPC flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| hpc.6.14core    | 14 | 88  | 80 | 0 | 80 | 6.2|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 25 |
| hpc.6.28core    | 28 | 176 | 80 | 0 | 80 | 6.2|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 50 |
| hpc.6.56core   | 56 | 352 | 80 | 0 | 80 | 6.2|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 100 |
| hpc.6.112core   | 112| 705 | 80 | 0 | 80 | 6.2|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 200 |
| hpc.5.16core    | 16 | 58  | 80 | 0 | 80 | 3.6|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 22.5 |
| hpc.5.32core    | 32 | 116 | 80 | 0 | 80 | 3.6|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 45 |
| hpc.5.64core   | 64 | 232 | 80 | 0 | 80 | 3.6|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 90 |
| hpc.5.128core   | 128| 464 | 80 | 0 | 80 | 3.6|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 180 |
| hpc.fullnode.haswell | 46 | 242 | 80 | 0 | 80 | 5.2 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 72  |
| hpc.3.28core         | 28 | 120 | 80 | 0 | 80 | 4.2 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 48  |
| hpc.3.56core         | 56 | 240 | 80 | 0 | 80 | 4.2 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 96  |
| hpc.4.5core          | 5  | 21  | 80 | 0 | 80 | 4.2 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 8   |
| hpc.4.10core         | 10 | 43  | 80 | 0 | 80 | 4.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 15  |
| hpc.4.20core         | 20 | 87  | 80 | 0 | 80 | 4.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 30  |
| hpc.4.40core         | 40 | 175 | 80 | 0 | 80 | 4.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 60  |
| hpc.4.80core         | 80 | 351 | 80 | 0 | 80 | 4.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 120 |

### I/O flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| io.haswell.2core  | 2  | 9.7  | 20 | 70   | 90   | 4.8   |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 4.5 |
| io.haswell.4core  | 4  | 19  | 20 | 160  | 180  | 4.7   |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 9   |
| io.haswell.8core  | 8  | 39  | 20 | 350  | 370  | 4.8 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 18  |
| io.haswell.16core | 16 | 78  | 20 | 700  | 720  | 4.8 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 36  |
| io.haswell.32core | 32 | 156 | 20 | 1400 | 1420 | 4.8 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 72  |
| io.haswell.46core | 46 | 242 | 20 | 2100 | 2120 | 5.2  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 108 |
| io.2.80GB         | 2  | 12,7 | 80 | 80  | 160  | 6.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 6  |
| io.2.240GB        | 4  | 26  | 80 | 240  | 320  | 6.6 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 12  |
| io.2.550GB        | 8  | 54  | 80 | 550  | 630  | 6.7 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 24  |
| io.2.1200GB       | 16 | 107 | 80 | 1200 | 1280 | 6.7 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 48  |

### High memory flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| tb.3.480RAM  | 56 | 480  | 20 | 1650 | 1730 | 8.5  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 110 |
| tb.3.1470RAM | 80 | 1470 | 80 | 2500 | 2580 | 18 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 320 |

Note that the root disks of all high memory flavors are hosted on solid-state drives (SSDs), while the ephemeral disks are hosted using NVM Express (NVMe).

### GPU flavors

|Flavor|Cores|GPUs|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Total<br/>disk<br/>(GB)|Memory/<br/>core<br/>(GiB)|Redundancy|Billing<br/>Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| gpu.1.1gpu | 14 | 1 | 117 | 80 |    0 |   80 |   8.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 60  |
| gpu.1.2gpu | 28 | 2 | 234 | 80 |    0 |   80 |   8.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 120 |
| gpu.1.4gpu | 56 | 4 | 468 | 80 |    0 |   80 |   8.3 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 240 |
| gpu.2.1gpu | 20 | 1 | 180 | 80 | 1000 | 1080 | 9 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 100 |
| gpu.3.1gpu | 12 | 1 | 219 | 80 | 1500 | 1580 | 18 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg)![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg)![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg)![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg)| 150  |

Note that both the root and the ephemeral disks of the GPU flavors are hosted on solid-state drives (SSDs).

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

**hpc.6.\*:**

-   Redundant power
-   CPU:  AMD EPYC 9734 112-Core Processor,
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node failure may cause downtime, but instances
    are recoverable.

**hpc.5.\*:**

-   Redundant power
-   CPU:  AMD EPYC 7702 64-Core Processor,
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node failure may cause downtime, but instances
    are recoverable.

**hpc.4.\*:**

-   No redundant power
-   CPU: Intel(R)    Xeon(R)   Gold    6148   CPU    @   2.40GHz,
    ***hyper-threading***
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node or disk failures may cause downtime, but instances
    are recoverable.

**hpc-gen2.\*:**

-   No redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Single 40 Gb/s
-   Flavor disk: Local SATA disk, RAID-0
-   Instances can be lost due to a single-node or disk failure.

**ePouta HPC flavor characteristics:**

**hpc.6.\*:**

-   Redundant power
-   CPU:  AMD EPYC 9734 112-Core Processor,
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node failure may cause downtime, but instances
    are recoverable.

**hpc.5.\*:**

-   Redundant power
-   CPU:  AMD EPYC 7702 64-Core Processor,
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored in the central storage
-   Single-node failure may cause downtime, but instances
    are recoverable.

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
virtual machine root and ephemeral disks. 

As these instances are also tightly tied to the hardware, you may
expect downtime of instances during the maintenance of the hardware.

The bulk of the storage is available as an ephemeral disk, typically
in /dev/vdb.

Often you want to create clusters of servers with the io.\*
flavors. In these cases, you probably want to have your virtual
machines land on different physical servers. This cannot currently be
done in the web interface. To do this, please refer to the
anti-affinity group commands in our [command line instructions].

The availability of these instances is not as high as the
standard flavors, but the I/O
performance is significantly better.

**cPouta IO flavor characteristics:**

**io.70GB-700GB:**

!!! Note  
    These servers have non-redundant disks, and you may expect data loss in case of disk failure.  
    These virtual machines can not be migrated nor resized to a different family flavor.

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Redundant 10 Gb/s or 40 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Instances can be lost due to a single-node or disk failure.

**io.2.\*:**

!!! Note  
    These virtual machines can not be resized to a different family flavor.

-   Redundant power
-   CPU: AMD EPYC 7282 16-Core Processor
-   Network: Redundant 25 Gb/s
-   Flavor disk: Local NVMe disk, RAID-1
-   Instance can be lost due to a single-node or multiple simultaneous disk failures.


**ePouta IO flavor characteristics:**

**io.haswell.\*:**

!!! Note  
    These servers have non-redundant disks, and you may expect data loss in case of disk failure.  
    These virtual machines can not be migrated nor resized to a different family flavor.

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Instances can be lost due to a single-node or disk failure.

**io.2.\*:**

!!! Note  
    These virtual machines can not be resized to a different family flavor.

-   Redundant power
-   CPU: AMD EPYC 7313 16-Core Processor
-   Network: Redundant 25 Gb/s
-   Flavor disk: Local NVMe disk, RAID-1
-   Instance can be lost due to a single-node or multiple simultaneous disk failures.

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
gpu.2 flavors, the SSDs are bigger and the SSDs are configured in RAID-0
for faster staging of datasets. You can use the volumes for storing larger
data sets and persistent data. If you need to read and write a lot of data
between the disk and GPGPU, using volumes might affect performance when
compared to local SSD disk.

To take advantage of the acceleration which GPGPUs provide, the
applications you run must support them. If you write
your own applications, the [optimization service] helps in
leveraging the GPGPUs.

GPGPUs can be used for a lot of cool and interesting things,
but please remember the resource usage must comply with the [Terms of Use].

Limitations and caveats: 

-   As we use PCI passthrough to get the whole GPGPU into the
    instance. The administrators are not able to access the GPGPU and
    check its health. Please report any errors or problems with the GPGPUs
    to CSC (and attach the output of the command "nvidia-smi -q").
-   The applications must be able to utilize the GPU to get a speedup. Even
    though there is no specific speedup target to be met to enable GPU usage
    on Pouta, it is best to aim for higher speedups to compensate for the
    relatively higher prices per hour associated with GPUs and their relative
    scarcity.
-   As the majority of computing resources in Pouta are CPU-based and GPU
    resources are relatively limited, most likely, you will need to specify
    your need for GPU resources in your application or make an additional
    request via <servicedesk@csc.fi> to enable their usage on your existing
    Pouta application.

These instances are also tightly tied to the hardware. You may expect
downtime of instances during the maintenance of the hardware.

Users also have the possibility to use NVIDIA Volta V100 GPGPUs in the
batch system on [Technical details about Puhti](../../computing/systems-puhti.md).

**cPouta flavor characteristics:**

**gpu.1.\*:**

-   No redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v4, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-1
-   Instance can be lost due to a single-node or multiple simultaneous disk failures.

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

**gpu.3.\*:**

-   Redundant power
-   CPU: AMD EPYC 7402 24-Core Processor
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local NVMe disks
-   Instance can be lost due to a single-node or disk failure.
-   Multi-Instance GPU (MIG) is supported

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
of these flavors include genome sequencing and analysis applications.

The resize/migration functionalities do not work for these instances.

If you need to move a workload from another type of VM to an instance with a high memory flavor, i.e., a TB instance, either move all data and install all applications manually
on the new TB instance or create a snapshot of the source VM. Then
convert that snapshot to a volume and use the volume to create the
new TB-flavor VM.

If you need to move a workload from a TB instance to another instance,
either move all data and install all applications manually on a new
VM or create a snapshot of the source VM. **Please note** that all
ephemeral disk data will be lost in the process and will not be stored
in the snapshot because only the TB VM root disk is stored in the snapshot.

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

|Flavor|Cores|Memory <br/>(GiB)|Root<br/> disk <br/>(GB)|Ephemeral<br/> disk <br/>(GB)|Total<br/> disk <br/>(GB)|Memory/<br/> core <br/>(GiB)|Billing<br/> Units<br/>/h|
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
  [optimization service]: https://research.csc.fi/optimization-service
  [Terms of Use]: https://research.csc.fi/pouta-user-policy
