# Billing

For Puhti a new billing scheme is introduced. Taito and cloud billing is not changed.

## Puhti 

### Compute billing

Puhti is a heterogenous system with CPU, GPU and IO nodes and nodes with varying amount of memory. Moreover, it is possible to use only a fraction of a node and its various resources. The billing scheme tries to charge the billing units (BUs) in fair way based on the reserved amount of node resources.

In the billing scheme the BU consumption rate of a compute job depends linearly on the number of requested cores and GPUs and the amount of requested memory (per core). More precisely,

 * each reserved core consumes **1** BU per hour,
 * each GiB of reserved memory consumes **0.1** BUs per hour,
 * each reserved GiB of NVMe disk (if available) consumes **0.006** BUs per hour.
 * each reserved GPU consumes **60** BUs per hour.

and the total BU consumption per hour is the sum of the above terms. Thus a job uses BUs as follows:

` Total BUs = ( NCores * 1 + MemGiBs * 0.1 + NVMeGiBs * 0.006 + NGPUs * 60 ) * Walltime hours `

### Lustre scratch disk billing

The default 1 TiB scratch disk quota is free. Increased quota is charged as follows:

   * 1 TiB consumes **50 000** BUs per year.

## Allas 

Allas object storage is charged based on usage as follows:

* 1 TiB consumes **3.5** BUs per hour.

## Estimating the billing units

To make it easier for customers to estimate how much billing units
they need, there is a [billing unit
calculator](https://research.csc.fi/billing-and-monitoring) available for all CSC compute and storage services.
