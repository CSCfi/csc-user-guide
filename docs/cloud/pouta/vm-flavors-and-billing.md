# Virtual machine flavors and Billing Unit rates

Currently, Pouta will bill for the use of 3 resources: storage volumes, floating IPs and virtual machines. The account of use of resources is done in increments of one hour. A good way to estimate usage cost is the [Billing Unit calculator](https://research.csc.fi/resources/#buc) utility. All these resources consume Cloud Billing Units, for more information about Billing in CSC, visit the [Billing](../../accounts/billing.md) page.

- **Storage volumes**: 3,6 Cloud BU / TiB hour for standard volume and 1,8 Cloud BU / TiB hour for capacity volume. In the [Volumes](https://pouta.csc.fi/dashboard/project/volumes/) page of your project, you can see the existing volumes. The total size of the volume is billed, and it consumes Cloud BUs even if they are not attached to virtual machines. This is because the data is still stored on our systems, and the total size of the volume is reserved for the volume.
- **Floating IPs**: 0,2 Cloud BU / hour. Every floating IP reserved to the project (even if it is not in use) is billed. See the list of reserved [Floating IPs](https://pouta.csc.fi/dashboard/project/floating_ips/) of your project. Any extra routers you create and connect to the external network will be also billed for one floating IP. The default router included in the project does not consume Cloud Billing Units.
- **Virtual machines**: see below the list of [cPouta](#cpouta-flavors) and [ePouta](#epouta-flavors) flavors (The values for the memory of each flavor (in GiB) are approximated). Virtual machines consume Cloud BUs regardless whether you are using them or not. This means that a **shut down or suspended virtual machine still consumes Cloud BUs**, and it is because the resources are still reserved and cannot be used by other users. You can find more information about the different states of virtual machines and their Cloud BU consumption in [Virtual machine lifecycle](vm-lifecycle.md).

\* **Cloud BU**: Cloud Billing Units

## Quotas

Each Pouta project has this initial default quota:

| Resource | Default |
|--------------:|:--------|
| Instances | 8 |
| Cores | 8 |
| Memory | 32 GB |
| Floating IPs | 2 |
| Storage | 1 TB |


Additional quota can be requested by sending an email to [csc service desk](../../support/contact.md) and explaining your use case. Every request is evaluated based on user needs versus available resources. We always aim to have enough free resources for every quota granted, but please note that there is no warranty. In some cases specific hardware, linked to specific virtual machine flavors may be full, so you would not be able to provision them even if you have the quota to do so.

## cPouta flavors

The following tables list the available virtual machine flavors in cPouta and their Cloud Billing Unit coefficients. Note that the default cPouta user account allows users to launch only a subset of the available virtual machine flavors.

### Standard flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Billing<br/>Units<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|
|standard.tiny   |1|0.9 |80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")|0.26 |
|standard.small  |2|1.9  |80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")|0.52  |
|standard.medium |3|3.9 |80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")|1.05    |
|standard.large  |4|7.8 |80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")|2.10    |
|standard.xlarge |6|15 |80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")|4.20    |
|standard.xxlarge|8|31 |80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")|8.40    |
|standard.3xlarge|8|62 |80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")|16.80   |

See more details on the [Standard flavors](#cpouta) section.

### HPC flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Cloud<br/>Billing<br/>Units<br/>/h|
|-:|:-:|:-:|:-:|:-:|:-:|
| hpc.6.14core    | 14 | 88  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 23 |
| hpc.6.28core    | 28 | 176 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 45 |
| hpc.6.56core   | 56 | 352 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 90 |
| hpc.6.112core   | 112| 705 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 180 |
| hpc.5.16core    | 16 | 58  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 20 |
| hpc.5.32core    | 32 | 116 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 40 |
| hpc.5.64core   | 64 | 232 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 80 |
| hpc.5.128core   | 128| 464 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 160 |
| hpc.4.5core     | 5  | 21  | 80 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 6   |
| hpc.4.10core    | 10 | 42  | 80 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 12  |
| hpc.4.20core    | 20 | 85  | 80 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 25  |
| hpc.4.40core    | 40 | 171 | 80 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 50  |
| hpc.4.80core    | 80 | 343 | 80 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 100 |

See more details on the [HPC flavors](#cpouta_1) section.

### I/O flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Billing<br/>Units<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|
| io.70GB  | 2  | 9.7 | 20 | 70  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 3.15  |
| io.160GB | 4  | 19 | 20 | 160 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 6.30  |
| io.340GB | 8  | 39 | 20 | 340 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 12.60 |
| io.700GB | 16 | 78 | 20 | 700 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 25.20 |
| io.2.80GB  | 2  | 12,7 | 80 | 80  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 6  |
| io.2.240GB  | 4 | 26 | 80 | 240  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 12  |
| io.2.550GB  | 8  | 54 | 80 | 550  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 24  |
| io.2.1200GB  | 16  | 107 | 80 | 1200  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 48  |

Note that both the root and the ephemeral disks of all I/O flavors are hosted on solid-state drives (SSDs).

See more details on the [I/O flavors](#cpouta_2) section.

### GPU flavors

|Flavor|Cores|GPUs|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Cloud<br/>Billing<br/>Units<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|
| gpu.1.1gpu | 14 | 1 | 117 | 80 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 60  |
| gpu.1.2gpu | 28 | 2 | 234 | 80 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 120 |
| gpu.1.4gpu | 56 | 4 | 468 | 80 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 240 |

Note that the root disks of all GPU flavors are hosted on solid-state drives (SSDs).

See more details on the [GPU flavors](#cpouta_3) section.

## ePouta flavors

The following tables list the available virtual machine flavors in ePouta and their
Billing Unit coefficients.

### Standard flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Billing<br/>Units<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|
| standard.tiny    | 1 | 0.9  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 0.26 |
| standard.small   | 2 | 1.9  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 0.52  |
| standard.medium  | 3 | 3.9  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 1.05    |
| standard.large   | 4 | 7.8  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 2.10     |
| standard.xlarge  | 6 | 15 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 4.20    |
| standard.xxlarge | 8 | 31 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 8.40    |
| standard.3xlarge | 8 | 62 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 16.80   |

See more details on the [Standard flavors](#epouta) section.

### HPC flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Cloud<br/>Billing<br/>Units<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|
| hpc.6.14core    | 14 | 88  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 25 |
| hpc.6.28core    | 28 | 176 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 50 |
| hpc.6.56core   | 56 | 352 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 100 |
| hpc.6.112core   | 112| 705 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 200 |
| hpc.5.16core    | 16 | 58  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 22.5 |
| hpc.5.32core    | 32 | 116 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 45 |
| hpc.5.64core   | 64 | 232 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 90 |
| hpc.5.128core   | 128| 464 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 180 |
| hpc.4.5core          | 5  | 21  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 8   |
| hpc.4.10core         | 10 | 43  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 15  |
| hpc.4.20core         | 20 | 87  | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 30  |
| hpc.4.40core         | 40 | 175 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 60  |
| hpc.4.80core         | 80 | 351 | 80 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 120 |

See more details on the [HPC flavors](#epouta_1) section.

### I/O flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Billing<br/>Units<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|
| io.2.80GB         | 2  | 12,7 | 80 | 80  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 6.30  |
| io.2.240GB        | 4  | 26  | 80 | 240  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 12.60  |
| io.2.550GB        | 8  | 54  | 80 | 550  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 25  |
| io.2.1200GB       | 16 | 107 | 80 | 1200 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 50  |

See more details on the [I/O flavors](#epouta_2) section.

### High memory flavors

|Flavor|Cores|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Cloud<br/>Billing<br/>Units<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|
| tb.3.480RAM  | 56 | 480  | 20 | 1650 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 110 |
| tb.3.1470RAM | 80 | 1470 | 80 | 2500 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 320 |

Note that the root disks of all high memory flavors are hosted on solid-state drives (SSDs), while the ephemeral disks are hosted using NVM Express (NVMe).

See more details on the [High memory flavors](#epouta_4) section.

### GPU flavors

|Flavor|Cores|GPUs|Memory<br/>(GiB)|Root<br/>disk<br/>(GB)|Ephemeral<br/>disk<br/>(GB)|Redundancy<br/>([notation](#flavor-notation))|Cloud<br/>Billing<br/>Units<br/>/h<br/>|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| gpu.1.1gpu | 14 | 1 | 117 | 80 |    0 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 60  |
| gpu.1.2gpu | 28 | 2 | 234 | 80 |    0 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 120 |
| gpu.1.4gpu | 56 | 4 | 468 | 80 |    0 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 240 |
| gpu.2.1gpu | 20 | 1 | 180 | 80 | 1000 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 100 |
| gpu.3.1gpu | 12 | 1 | 219 | 80 | 1500 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 150  |

Note that both the root and the ephemeral disks of the GPU flavors are hosted on solid-state drives (SSDs).

See more details on the [GPU flavors](#epouta_3) section.

## Flavor notation

We use symbols to describe some of the features of the flavors we offer.
A short description of the notation used follows.

- **Power redundancy**, For the power provisioning of the node hosting the virtual machine, there are two possible values of redundancy (none or full), see below.
- **Data redundancy**, Within each virtual machine, the customer data is stored in a root disk (R) and possibly in an [ephemeral disk (E)](ephemeral-storage.md).
For customer data, there are three possible values of redundancy.
We also offer the possibility to store the data in a [persistent volume (FULL)](persistent-volumes.md)
- **Network redundancy**, For the network reachability of the virtual machine, there are two possible values of redundancy (none or full), see below.

|Type|Icon||Description|
|-:|:-:|:-:|:-|
|Power|![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")|**NONE**|The node is not protected from sudden power losses. **A fault in the power provisioning of the node might make the virtual machine temporarily unreachable**.|
|Power|![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")|**FULL**|The node is protected from sudden power losses by a Uninterruptible power supply (UPS).|
|Data|![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")|**NONE**|The disk is stored only in the node running the virtual machine and it is not backed up (RAID-0 or LVM striping). **A fault in one of the disks of the node might corrupt the data of the virtual machine**. Moreover, **a fault in the node hosting the virtual machine might make the virtual machine not usable until the fault is fixed**.|
|Data|![Icon for root disk data redundancy level BASIC](../../img/circle_icons/r50.svg "Root disk BASIC")![Icon for ephemeral disk data redundancy level BASIC](../../img/circle_icons/e50.svg "Ephemeral disk BASIC")|**BASIC**|The disk is stored only in the node running the virtual machine and it is mirrored within the same node (RAID-1). A fault in a single disk of the node does not compromise the data of the virtual machine. **Simultaneous faults in multiple disks of the node might corrupt the data of the virtual machine**. Moreover, **a fault in the node hosting the virtual machine might make the virtual machine not usable until the fault is fixed**.|
|Data|![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for ephemeral disk data redundancy level FULL](../../img/circle_icons/e100.svg "Ephemeral Disk")|**FULL**|The disk is stored using multiple nodes in a fault-tolerant fashion ([CEPH](https://ceph.io/en/)), so the customer data is not tied to any specific node. In case of a fault in a node used by the customer, it is possible to re-spawn the virtual machine of the customer using an alternative node.|
|Network|![Icon for network reachability redundancy level NONE](../../img/circle_icons/n0.svg "Network")|**NONE**|The node hosting the virtual machine is connected to the cloud platform without a failover link. **A fault in the link of the node might make the virtual machine temporarily unreachable**.|
|Network|![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")|**FULL**|The node hosting the virtual machine is connected to the cloud platform with an additional failover link.|
|Other|![New VMs with this flavor cannot be currently launched](../../img/risk-icon.svg)||Launching new virtual machines with this flavor is temporarily not possible. Existing virtual machines are not affected.|

* [RAID 0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0) spreads the data across two or more disks. It is used for an increased I/O performance. It provides no fault tolerance or redundancy, the failure of one drive will cause the entire array to fail.

* [RAID 1](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1) mirrors the data across two or more disks. Reads are usually fast operations, but writes are as fast as the slowest disk. The failure of one drive does not lose any data.

## Which type of flavor should I use?

### **Standard flavors**

These are generic flavors that are useful for running regular computation tasks like a web service or software development. If you are unsure on what to use, this is the recommended choice for you. You can later [resize the instance](../../support/faq/how-to-resize-in-pouta.md) to a more suitable flavor afterwards when your application's are clearer.

They provide better availability compared to the
HPC flavors. This is because cloud administrators can move these virtual machines from one host machine to another without causing a break in service. This means that
you are likely less affected by maintenance.

These flavors are not suitable for computationally intensive
workloads. The virtual CPUs used in these instances are
**overcommitted**, which means 32 hyperthreaded CPU cores are used to
provide more than 32 virtual cores. For these kind of tasks we recommend [HPC flavors](#hpc-flavors_2)

#### cPouta

|Flavor<br/>family|Redundant<br/>power|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|
|standard.\*|Yes|Various|Redundant 25 Gb/s|Stored in the central storage|Single-node or disk failures may cause downtime, but instances are recoverable.|

#### ePouta

|Flavor<br/>family|Redundant<br/>power|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|
|standard.\*|Yes|Various|Redundant 25 Gb/s|Stored in the central storage|Single-node or disk failures may cause downtime, but instances are recoverable.|

### **HPC flavors**

If your use case is computationally intensive, you should use one of
the HPC flavors. The availability of these instances is not as high
as the standard flavors, but you get better performance. The HPC
flavors have faster CPUs models and **no overcommitment of CPU cores**.

#### cPouta

|Flavor<br/>family|Redundant<br/>power|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**hpc.6.\***|Yes|AMD EPYC 9734 112-Core|Redundant 25 Gb/s|Stored in the central storage|Single-node failure may cause downtime, but instances are recoverable.|
|**hpc.5.\***|Yes|AMD EPYC 7702 64-Core|Redundant 25 Gb/s|Stored in the central storage|Single-node failure may cause downtime, but instances are recoverable.|
|**hpc.4.\***|No|Intel(R)    Xeon(R)   Gold    6148   CPU@2.40GHz ***hyper-threading***|Redundant 25 Gb/s|Stored in the central storage|Single-node or disk failures may cause downtime, but instances are recoverable.|

#### ePouta

|Flavor<br/>family|Redundant<br/>power|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**hpc.6.\***|Yes|AMD EPYC 9734 112-Core Processor|Redundant 25 Gb/s|Stored in the central storage|Single-node failure may cause downtime, but instances are recoverable.|
|**hpc.5.\***|Yes|AMD EPYC 7702 64-Core Processor|Redundant 25 Gb/s|Stored in the central storage|Single-node failure may cause downtime, but instances are recoverable.|
|**hpc.4\***|Yes|Intel(R) Xeon(R) CPU Gold 6148, with hyper-threading|Redundant 25 Gb/s|Stored in the central storage|Single-node or disk failures may cause downtime, but instances are recoverable.|

### **I/O flavors**

Typical use cases:

-   Hadoop/Spark
-   Non-critical centralized databases
-   Clustered databases

I/O flavors are intended to provide the best I/O performance on the
virtual machine root and ephemeral local disks. Typical use cases are the ones that will read from and/or write to intensely the disk.   

The availability of these instances is not as high as the standard flavors, but the I/O performance is significantly better.
This is why, the instances of this flavor are tightly tied to the hardware, because of this you may
expect downtime of instances during the maintenance of the hardware that runs them.

The bulk of the storage is available as an ephemeral disk, typically
in /dev/vdb.

Often you want to create clusters of servers with the io.\*
flavors. In these cases, you probably want to have your virtual
machines land on different physical servers. To do this, please follow the
[Server Groups](launch-vm-from-web-gui.md#server-groups) documentation.

#### cPouta

|Flavor family|Redundant<br/>power|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**io.70GB-700GB**|No|Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading|Redundant 10 Gb/s or 40 Gb/s|Local SSD disks, RAID-1|- Instances can be lost due to a single-node or multiple simultaneous disk failures.<br/>- Instances can not be migrated nor resized to a different family flavor.|
|**io.2.\***|Yes|AMD EPYC 7282 16-Core Processor|Redundant 25 Gb/s|Local NVMe disk, RAID-1|- Instance can be lost due to a single-node or multiple simultaneous disk failures.<br/>- Instances can not be resized to a different family flavor.|

#### ePouta

|Flavor family|Redundant<br/>power|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**io.2.\***|Yes|AMD EPYC 7313 16-Core Processor|Redundant 25 Gb/s|Local NVMe disk, RAID-1|Instance can be lost due to a single-node or multiple simultaneous disk failures.<br/>These virtual machines can not be resized to a different family flavor.|

### GPU flavors

The GPU flavors are intended to provide high performance computing using
GPGPU (General Purpose computing on Graphical Processing
Units). GPGPUs can significantly speed up certain algorithms and
applications.
The GPGPUs are suitable for machine and deep learning like Large Language Models (LLMs), scientific computing, rendering or visualization.

The GPGPU
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
Also remember that the GPU flavor is the most demanded one on our platform,
so if you are not using your GPU flavor VM, consider shelving or deleting it so others can use it. 

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
batch system [Puhti](../../computing/systems-puhti.md).

#### cPouta

|Flavor family|Redundant<br/>power|GPU|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**gpu.1.\***|No|NVIDIA Tesla P100 (16 GB)|Intel(R) Xeon(R) CPU E5-2680 v4, with hyper-threading|Redundant 10 Gb/s|Local SSD disks, RAID-1|Instance can be lost due to a single-node or multiple simultaneous disk failures.|

#### ePouta

|Flavor family|Redundant<br/>power|GPU|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**gpu.1.\***|Yes|NVIDIA Tesla P100 (16 GB)|Intel(R) Xeon(R) CPU E5-2680 v4, with hyper-threading|Redundant 10 Gb/s|Local SSD disks, RAID-1|Instance can be lost due to a single-node or disk failure.|
|**gpu.2.\***|Yes|NVIDIA Tesla V100 (16 GB)|Intel(R) Xeon(R) Gold 6148, with hyper-threading|Redundant 10 Gb/s|Local SSD disks, RAID-0|NUMA Aware: yes (CPU &lt;&gt; memory, not PCI devices)<br/>Instance can be lost due to a single-node or disk failure.|
|**gpu.3.\***|Yes|NVIDIA A100 (40 GB)|AMD EPYC 7402 24-Core Processor|Redundant 10 Gb/s|Local NVMe disks|Instance can be lost due to a single-node or disk failure.<br/>Multi-Instance GPU (MIG) functionality supported|

### High memory flavors

!!! info "High memory flavors are only in ePouta"
    High memory flavors are only available in ePouta.

These flavors have large amounts of memory and are meant for use cases
which require and can utilize such amounts of memory. Typical use cases
of these flavors include genome sequencing and analysis applications.

The resize/migration functionalities do not work for these instances. 
If you need to resize one VM of this flavor you will need to, either create a new VM and move all data and install all applications manually
on the new VM, either create a snapshot of the source VM, and then
create a new VM with that snapshot. More information at the [resize the instance](../../support/faq/how-to-resize-in-pouta.md) article.
**Please note** that all ephemeral disk data will be lost in the process and will not be stored
in the snapshot because only the VM's root disk is stored in the snapshot.
Never store on the ephemeral disk any valuable data that you have no a second safe copy.

#### ePouta

|Flavor family|Redundant<br/>power|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**tb.3.\***|Yes|Intel(R) Xeon(R) CPU  E5-2680 v4, with hyper-threading<br/>**or**<br/>Intel(R) Xeon(R) CPU E5-2698 v4, with hyper-threading|Redundant 25 Gb/s|Local SSD disks, RAID-0|Instances can be lost due to a single-node or disk failure.|

### Deprecated flavors

This is the set of original flavors that has been available
since the launch. **You should not launch any new virtual machines using
any of these flavors. Existing
virtual machines that use these flavors will continue to
work.** We will maintain these flavors for a period of time,
but they will be removed at some point in the near future.

|Flavor|Cores|Memory <br/>(GiB)|Root<br/> disk <br/>(GB)|Ephemeral<br/> disk <br/>(GB)|Redundancy|Cloud<br/>Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|
| hpc-gen1.1core  | 1  | 3.7 | 80 (RAID0)  | 0            |  | 2  |
| hpc-gen1.4core  | 4  | 15  | 80 (RAID0)  | 0            |  | 8  |
| hpc-gen1.8core  | 8  | 30  | 80 (RAID0)  | 0            |  | 16 |
| hpc-gen1.16core | 16 | 60  | 80 (RAID0)  | 0            |  | 32 |
| hpc-gen2.2core  | 2  | 10  | 80 (RAID0)  | 0            |  | 4  |
| hpc-gen2.8core  | 8  | 40  | 80 (RAID0)  | 0            |  | 15 |
| hpc-gen2.16core | 16 | 80  | 80 (RAID0)  | 0            |  | 30 |
| hpc-gen2.24core | 24 | 117 | 80 | 0 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for network reachability redundancy level NONE](../../img/circle_icons/n0.svg "Network")    | 30  |
| hpc-gen2.48core | 48 | 234 | 80 | 0 |![Icon for power redundancy level NONE](../../img/circle_icons/p0.svg "Power NONE")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for network reachability redundancy level NONE](../../img/circle_icons/n0.svg "Network")    | 60  |
| tiny            | 1  | 1   | 10  (RAID0) | 110 (RAID0)  |  | 2  |
| mini            | 1  | 3.5 | 10  (RAID0) | 110 (RAID0)  |  | 2  |
| small           | 4  | 15  | 10  (RAID0) | 220  (RAID0) |  | 8  |
| medium          | 8  | 30  | 10  (RAID0) | 440  (RAID0) |  | 16 |
| large           | 12 | 45  | 10  (RAID0) | 660  (RAID0) |  | 24 |
| fullnode        | 16 | 60  | 10  (RAID0) | 900  (RAID0) |  | 32 |
| hpc.mini        | 2  | 3.5 | 80         | 0            |  | 5   |
| hpc.small             | 4  | 7   | 80         | 0            | | 10  |
| hpc.medium.haswell    | 8  | 40  | 80         | 0            | | 20  |
| hpc.large.haswell     | 16 | 80  | 80         | 0            | | 40  |
| hpc.xlarge.haswell    | 32 | 156 | 80         | 0            | | 80  |
| hpc.fullnode.haswell | 46 | 242 | 80 | 0 | 80 | 5.2 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 72  |
| hpc.medium.westmere   | 8  | 14  | 80         | 0            |  | 8   |
| hpc.large.westmere    | 16 | 28  | 80         | 0            |  | 16  |
| hpc.xlarge.westmere   | 23 | 41  | 80         | 0            |  | 24  |
| hpc.largemem.westmere | 23 | 90  | 80         | 0            |  | 36  |
| hpc.3.28core         | 28 | 120 | 80 | 0 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 48  |
| hpc.3.56core         | 56 | 240 | 80 | 0 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level FULL](../../img/circle_icons/r100.svg "Root disk FULL")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 96  |
| io.haswell.2core  | 2  | 9.7  | 20 | 70  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 4.5 |
| io.haswell.4core  | 4  | 19  | 20 | 160  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 9   |
| io.haswell.8core  | 8  | 39  | 20 | 350  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 18  |
| io.haswell.16core | 16 | 78  | 20 | 700  |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 36  |
| io.haswell.32core | 32 | 156 | 20 | 1400 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 72  |
| io.haswell.46core | 46 | 242 | 20 | 2100 |![Icon for power redundancy level FULL](../../img/circle_icons/p100.svg "Power FULL")![Icon for root disk data redundancy level NONE](../../img/circle_icons/r0.svg "Root disk NONE")![Icon for ephemeral disk data redundancy level NONE](../../img/circle_icons/e0.svg "Ephemeral disk NONE")![Icon for network reachability redundancy level FULL](../../img/circle_icons/n100.svg "Network FULL")| 108 |
| tb.4.735RAM  | 80 | 735  | 80 (SSD/RAID0) | 3300 (SSD/RAID0) || 220 (350) |
| tb.westmere.32core    | 32 | 488 | 80 (RAID6) | 3250 (RAID6) || 200 |
| tb.westmere.64core    | 64 | 976 | 80 (RAID6) | 6500 (RAID6) || 400 |

  [CSC computing environment articles]: https://research.csc.fi/computing
  [command line instructions]: command-line-tools.md
  [TensorFlow]: https://www.tensorflow.org
  [optimization service]: https://research.csc.fi/optimization-service
  [Terms of Use]: https://research.csc.fi/pouta-user-policy
