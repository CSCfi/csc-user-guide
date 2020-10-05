# Billing

<iframe src="https://my.csc.fi/buc" width="100%" height="1300" frameborder="0" ></iframe>

## System specifics

### Puhti

#### Compute billing

Puhti is a heterogenous system with CPU, GPU and IO nodes and nodes with varying amounts of memory. Moreover, it is possible to use only a fraction of a node and its various resources. The billing scheme charges billing units (BU) in fair way based on the reserved amount of node resources.

In the billing scheme, the BU consumption rate of a compute job depends linearly on the number of requested cores and GPUs and the amount of requested memory (per core). More precisely:

 * Each reserved core consumes **1** BU per hour.
 * Each GiB of reserved memory consumes **0,1** BUs per hour.
 * Each reserved GiB of NVMe disk (if available) consumes **0,006** BUs per hour.
 * Each reserved GPU consumes **60** BUs per hour.

The total BU consumption per hour is the sum of the above terms:

` Total BUs = ( NCores * 1 + MemGiBs * 0,1 + NVMeGiBs * 0,006 + NGPUs * 60 ) * Walltime hours `

#### Scratch disk billing

The default 1 TiB scratch disk quota is free. Increased quota charges:

* 1 TiB consumes **50 000** BUs per year.

#### ProjAppl disk billing

The default 50 GiB projappl disk quota is free. Increased quota charges:

* 1 TiB consumes **50 000** BUs per year.

### Mahti

#### Compute billing

In contrast to Puhti, on Mahti resources are used and billed in full nodes on all normal partitions. In the interactive partition that can be used for interactive work, as well as for small scale pre- and postprocessing, the usage is billed per CPU core. In Mahti memory is not billed separately.

 * Each reserved node consumes **100** BUs per hour.
 * In interactive partition each core consumes **1** BU per hour.

#### Scratch disk billing

The default 1 TiB scratch disk quota is free. Increased quota charges:

* 1 TiB consumes **50 000** BUs per year.

#### ProjAppl disk billing

The default 50 GiB projappl disk quota is free. Increased quota charges:

* 1 TiB consumes **50 000** BUs per year.

### Allas

The Allas object storage charges:

* 1 TiB consumes **1** BUs per hour.

### cPouta and ePouta

* See [Pouta billing](../cloud/pouta/accounting.md)

### Rahti

* See [Rahti billing](/cloud/rahti/billing.md)

### Monitoring billing unit consumption

In the _My Projects_ page in [MyCSC](https://my.csc.fi) you can study the
billing unit consumption and apply for more billing units. There you can easily
check who consumed the billing units, when they were consumed and in which
service. Note that storage-related billing unit consumption (in Scratch and
Allas) is not linked to a specific user account and is reported as "unknown".
