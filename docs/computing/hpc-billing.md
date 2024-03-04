# Billing

## Puhti compute billing

Puhti is a heterogeneous system with CPU, GPU and IO nodes and nodes with
varying amounts of memory. Moreover, it is possible to use only a fraction of a
node and its various resources. The billing scheme charges billing units (BU)
in a fair way based on the reserved amount of node resources.

In the billing scheme, the BU consumption rate of a compute job depends
linearly on the number of requested cores, the number of requested GPUs and the
amount of requested memory. More precisely:

* Each reserved core consumes **1** BU per hour.
* Each GiB of reserved memory consumes **0.1** BU per hour.
* Each reserved GiB of NVMe disk (if available) consumes **0.006** BU per hour.
* Each reserved GPU consumes **60** BU per hour.

The total BU consumption per hour is the sum of the above terms:

```
Total BU = ( NCores * 1 + MemGiBs * 0.1 + NVMeGiBs * 0.006 + NGPUs * 60 ) * Walltime hours
```

## Mahti compute billing

In contrast to Puhti, in Mahti resources are used and billed per node in all
normal partitions. In the interactive partition, which can be used for
interactive work, as well as for small scale pre- and postprocessing, the usage
is billed per CPU core. The GPU nodes in Mahti are billed according to the number
of reserved GPUs. Memory is not billed separately.

* Each reserved CPU node consumes **100** BU per hour.
* In interactive partition each core consumes **1** BU per hour.
* Each reserved A100 GPU consumes **100** BU per hour, or in total **400** BU per
  hour for a full GPU node.
* A slice of an A100 GPU with one seventh of an A100 (a100_1g.5gb) consumes **15** BU per hour 

## Scratch disk billing

Puhti and Mahti have the same billing for scratch storage. Usage up to 1 TiB is free of charge. 

* Excess usage beyond 1 TiB is billed: 1 TiB consumes **5** BU per hour.

## ProjAppl disk billing

Puhti and Mahti have the same billing for scratch storage. Usage up to 50 GiB is free of charge. 

* Excess usage beyond 50 GiB is billed: 1 TiB consumes **5** BU per hour.
