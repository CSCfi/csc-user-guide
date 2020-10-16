# Billing

See the [Billing unit and price calculator](https://research.csc.fi/billing-and-monitoring#buc)
at research.csc.fi.

## Puhti

### Compute billing

Puhti is a heterogeneous system with CPU, GPU and IO nodes and nodes with
varying amounts of memory. Moreover, it is possible to use only a fraction of a
node and its various resources. The billing scheme charges billing units (BU)
in a fair way based on the reserved amount of node resources.

In the billing scheme, the BU consumption rate of a compute job depends
linearly on the number of requested cores, the number of requested GPUs and the
amount of requested memory. More precisely:

 * Each reserved core consumes **1** BU per hour.
 * Each GiB of reserved memory consumes **0,1** BU per hour.
 * Each reserved GiB of NVMe disk (if available) consumes **0,006** BU per hour.
 * Each reserved GPU consumes **60** BU per hour.

The total BU consumption per hour is the sum of the above terms:

` Total BU = ( NCores * 1 + MemGiBs * 0,1 + NVMeGiBs * 0,006 + NGPUs * 60 ) * Walltime hours `

### Scratch disk billing

The default 1 TiB scratch disk quota is free. Increased quota is charged:

* 1 TiB consumes **50 000** BU per year.

### ProjAppl disk billing

The default 50 GiB projappl disk quota is free. Increased quota is charged:

* 1 TiB consumes **50 000** BU per year.

## Mahti

### Compute billing

In contrast to Puhti, on Mahti resources are used and billed per node in all
normal partitions. In the interactive partition, which can be used for
interactive work, as well as for small scale pre- and postprocessing, the usage
is billed per CPU core. Memory is not billed separately.

 * Each reserved node consumes **100** BU per hour.
 * In interactive partition each core consumes **1** BU per hour.

### Scratch disk billing

The default 1 TiB scratch disk quota is free. Increased quota is charged:

* 1 TiB consumes **50 000** BU per year.

### ProjAppl disk billing

The default 50 GiB projappl disk quota is free. Increased quota is charged:

* 1 TiB consumes **50 000** BU per year.

## Allas

The Allas object storage is charged:

* 1 TiB consumes **1** BU per hour.

## cPouta and ePouta

* See [Pouta billing](../cloud/pouta/accounting.md).

## Rahti

* See [Rahti billing](../cloud/rahti/billing.md).

## Monitoring billing unit consumption

In the _My Projects_ page in [MyCSC](https://my.csc.fi) you can study the
billing unit consumption and apply for more billing units. There you can easily
check who consumed the billing units, when they were consumed and in which
service. Note that storage-related billing unit consumption (in Scratch and
Allas) is not linked to a specific user account and is reported as "other".
