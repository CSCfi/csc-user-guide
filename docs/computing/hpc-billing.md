# Billing

CSC resource usage is measured in Billing Units (BU). Billing Units are granted
to CSC projects and are consumed when you use CSC services.

This page explains how BUs are consumed on CSC supercomputers.

There are different types of Billing Units:

| BU type    | Consumed by |
|:-----------|:------------|
| CPU BU     | CPU jobs on supercomputers |
| GPU BU     | GPU jobs on supercomputers |
| Storage BU | Data stored in supercomputer storage |
| Cloud BU   | Cloud services |

The BU types are separate from each other. CPU jobs consume CPU BUs,
GPU jobs consume GPU BUs, and data stored in the supercomputer storage consumes Storage BUs.

You can check the BU usage and quotas of your project in [MyCSC](https://my.csc.fi/).
In MyCSC, open **Projects**, select your project, and see the **Resources** section.

You can also check your project's BU balance on a given supercomputer
from the command line with:

```bash
csc-projects
```

## Roihu compute billing

Jobs in Roihu's CPU partitions consume CPU BUs based on either the CPU resource allocation
(per node price for node-based allocation or per core price for core-based allocation) or
the memory allocation, whichever consumes the most BUs, but not both.

On GPU partitions the pricing is always based on the amount of reserved GPUs. CPU cores
and memory are not billed separately, each job will at most be able to reserve a corresponding
share of CPU and memory resources of the node.

For all partitions local disk usage is billed additionally to the above BUs.

See details of the different [CPU and GPU partitions on Roihu](running/batch-job-partitions.md#roihu-partitions).

### Core-based allocations

Jobs in the small, longrun, interactive, and test partitions are run on M and L nodes. These jobs are billed as follows:

`Total CPU BU = max ( 0.75 BU/coreh * cores , 0.375 BU/GiBh * mem) * runtime-hours +  0.02 BU/GiBh * reservedstorage * runtime-hours`

where `reservedstorage` is the total amount of disaggregated storage.

Jobs in the hugemem and hugemem_longrun partitions are run on XL nodes. These jobs are billed as follows:

`Total CPU BU = max ( 12 BU/coreh * cores , 0.25 BU/GiBh * mem) * runtime-hours +  0.02 BU/GiBh * reservedstorage * runtime-hours`

where `reservedstorage` is the total amount of disaggregated storage, or local storage reserved with the `gres` option in Slurm.

??? info "Core-based allocation example"
     A job in the `small` partition reserves 4 CPU cores, 16 GiB of memory,
     and runs for 2 hours with no additional reserved storage.

     ```text
     max(0.75 * 4, 0.375 * 16) * 2
     = max(3, 6) * 2
     = 12 CPU BU
     ```

     Although the job reserved only 4 cores, the memory
     reservation determines the price in this example.

### Node-based Slurm partitions

Jobs in the medium and large partitions are run on full M nodes. These jobs are billed as follows:

`Total CPU BU = nodes * 288 BU/nodeh * runtime-hours +  0.02 BU/GiBh * reservedstorage * runtime-hours`

where `reservedstorage` is the total amount of disaggregated storage.

### GPU partitions

Jobs in GPU partitions, including interactive visualization partitions, are billed as follows:
 
`Total GPU BU = numOfGPUs *  200 BU/GPUh * runtime-hours + 0.02 BU/GiBh * reservedstorage * runtime-hours`

where `reservedstorage` is the total amount of disaggregated storage,
or the total amount of local storage reserved via the `gres` Slurm option on the visualization nodes.

??? info "GPU allocation example"
     A job in a GPU partition reserves 2 GPUs and runs for 5 hours with no
     additional reserved storage.

     ```text
     2 * 200 * 5
     = 2000 GPU BU
     ```

     CPU cores (72 per GPU) and memory (217G per GPU) are not billed separately.

### Storage

Storage is billed in Storage BUs per used TiB per hour. The price depends on
the storage area where the data is kept.

The pricing for different storage areas is:

| Storage area     | Billing                       |
|:-----------------|:-----------------------------:|
| Scratch          | `6 BU * TiB * storage-hours`  |
| Home             | `10 BU * TiB * storage-hours` |
| Projappl         | `10 BU * TiB * storage-hours` |
| Dataset — public | `6 BU * TiB * storage-hours`  |
| Dataset — shared | `10 BU * TiB * storage-hours` |

Note that using local scratch on hugemem and visualization nodes **does not** consume storage BUs.
Instead, it is included in compute BU billing.

??? info "Storage BU example"
     A project stores 1 TiB of data in scratch for 180 days.

     ```text
     6 * 1 * 24 * 180
     = 25920 Storage BU
     ```

     Storage BU billing depends on the amount of data stored, the storage area,
     and the time the data is kept there.

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

## Additional information

* [What happens when I run out of billing units?](usage-policy/#running-out-of-billing-units)
* [How to apply for more billing units](../accounts/how-to-apply-for-billing-units/)