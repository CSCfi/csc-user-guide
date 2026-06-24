# Billing

##  Roihu compute billing

Jobs in Roihu's CPU partitions consume CPU BUs, either based on the number
of reserved nodes (node-based allocation) or the number of reserved cores
(core-based allocation). Memory is not billed separately, but local
disk usage is.

On GPU partitions, the pricing is always based
on the number of reserved GPUs. CPU cores and memory are not billed separately.
Each job can reserve at most the corresponding share of the node's CPU and memory resources.

### Core based allocations

Jobs in the small, longrun, interactive, and test partitions are run on M and L nodes. These jobs are billed as follows:

`Total CPU BU = max ( 0.75 BU/coreh * cores , 0.375 BU/GiBh * mem) * runtime-hours +  0.02 BU/GiBh * reservedstorage * runtime-hours`

where `reservedstorage` is the total amount of disaggregated storage.

Jobs in the hugemem and hugemem_longrun partitions are run on XL nodes. These jobs are billed as follows:

`Total CPU BU = max ( 12 BU/coreh * cores , 0.25 BU/GiBh * mem) * runtime-hours +  0.02 BU/GiBh * reservedstorage * runtime-hours`

where `reservedstorage` is the total amount of disaggregated storage, or local storage reserved with the `gres` option in Slurm.

### Node based Slurm partitions

Jobs in the medium and large partitions are run on full M nodes. These jobs are billed as follows:

`Total CPU BU = nodes * 288 BU/nodeh * runtime-hours +  0.02 BU/GiBh * reservedstorage * runtime-hours`

where `reservedstorage` is the total amount of disaggregated storage.

### GPU partitions

The price per job in GPU partitions, including the ones for interactive visualization, are billed as follows:
 
`Total GPU BU = numOfGPUs *  200 BU/GPUh * runtime-hours + 0.02 BU/GiBh * reservedstorage * runtime-hours`

where `reservedstorage` is the total amount of disaggregated storage,
or the total amount of local storage reserved via the `gres` Slurm option on the visualization nodes.



### Storage

Storage is billed per used TiB per hour.

The pricing is 

 * Scratch: `storage BU = 6 BU  * TiB * storage-hours`
 * Home:  `storage BU = 10 BU  * TiB * storage-hours`
 * Projappl:  `storage BU = 10 BU  * TiB * storage-hours`
 * Dataset - public:  `storage BU = 6 BU  * TiB * storage-hours`
 * Dataset - shared:  `storage BU = 10 BU  * TiB * storage-hours`


## Mahti compute billing


Jobs in Mahti's CPU partitions consume CPU BUs, either based on number
of reserved nodes (node-based allocation) or number of reserved cores
(core-based allocation). Memory is not billed separately, but local
disk usage is billed separately. More precisely:

* In the partitions with node-based allocation each reserved CPU node consumes **100** CPU BU per hour.
* In the partitions with core-based allocation each core consumes **1** CPU BU per hour, and each reserved GiB of NVMe disk consumes **0.01** CPU BU per hour.


Jobs in Mahti's GPU partitions consume GPU BUs based on the number of
reserved GPUs. Memory is not billed separately, but local disk usage
is billed separately. More precisely:

* Each reserved A100 GPU consumes **100** GPU BU per hour, or in total **400** GPU BU per
  hour for a full GPU node. 
* A slice of an A100 GPU with one seventh of an A100 (a100_1g.5gb) consumes **15** GPU BU per hour
* Each reserved GiB of NVMe disk consumes **0.01** GPU BU per hour.

## Puhti compute billing

Puhti is a heterogeneous system with CPU, GPU and IO nodes and nodes with
varying amounts of memory. Moreover, it is possible to use only a fraction of a
node and its various resources. The billing scheme charges Billing Units (BU)
in a fair way based on the reserved amount of node resources. 

On Puhti's [CPU partitions](running/batch-job-partitions.md#puhti-cpu-partitions) the
jobs consume CPU Billing Units. The CPU BU consumption rate of a
compute job depends linearly on the number of requested cores, the
amount of requested local storage, and the amount of requested
memory. More precisely:

* Each reserved core consumes **1** CPU BU per hour.
* Each GiB of reserved memory consumes **0.1** CPU BU per hour.
* Each reserved GiB of NVMe disk (if available) consumes **0.006** CPU BU per hour.

```
Total CPU BU = ( NCores * 1 + MemGiBs * 0.1 + NVMeGiBs * 0.006 ) * Walltime hours
```

On Puhti's [GPU partitions](running/batch-job-partitions.md#puhti-gpu-partitions) the
jobs consume GPU Billing Units. The GPU BU consumption rate of a
compute job depends linearly on the number of requested GPUs, the number of requested cores, the
amount of requested local storage, and the amount of requested
memory. More precisely:

* Each reserved GPU consumes **60** GPU BU per hour.
* Each reserved core consumes **1** GPU BU per hour.
* Each GiB of reserved memory consumes **0.1** GPU BU per hour.
* Each reserved GiB of NVMe disk (if available) consumes **0.006** GPU BU per hour.


```
Total GPU BU = ( NCores * 1 + MemGiBs * 0.1 + NVMeGiBs * 0.006 + NGPUs * 60 ) * Walltime hours
```






## Scratch disk billing

Puhti and Mahti have the same billing for scratch storage. Usage up to 1 TiB is free of charge. 

* Excess usage beyond 1 TiB is billed: 1 TiB consumes **5** Storage BU per hour.

## ProjAppl disk billing

Puhti and Mahti have the same billing for ProjAppl storage. Usage up to 50 GiB is free of charge. 

* Excess usage beyond 50 GiB is billed: 1 TiB consumes **5** Storage BU per hour.
