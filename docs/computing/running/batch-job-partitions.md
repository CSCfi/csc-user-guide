# Available batch job partitions

!!! Note
    The available LUMI batch job partitions are found in [the LUMI documentation](https://docs.lumi-supercomputer.eu/computing/jobs/partitions/).

## Puhti partitions

The following partitions (aka queues) are currently available in **Puhti** for
normal (CPU) nodes:


| Partition       | Time<br>limit | Max<br>tasks | Max<br>nodes             | [Node types](../systems-puhti.md)   | Max<br>memory  | Max<br>local storage<br>[(nvme)](../creating-job-scripts-puhti/#local-storage) |  
|-----------------|---------------|--------------|--------------------------|------------------------------|----------|----------|
| test            | 15 minutes    | 80           |   2                      |  M                           | 190 GiB  |          |
| [interactive](interactive-usage.md)     | 7 days        | 8            |   1                      |  IO  | 76 GiB   | 720 GiB  |
| small           | 3 days        | 40           |   1                      |  M, L, IO                    | 382 GiB  | 3600 GiB |
| large           | 3 days        | 1040         |   26                     |  M, L, IO                    | 382 Gib  | 3600 GiB | 
| longrun         | 14 days       | 40           |   1                      |  M, L, IO                    | 382 GiB  | 3600 GiB | 
| hugemem         | 3 days        | 160          |   4                      |  XL, BM                      | 1534 GiB |         |
| hugemem_longrun | 14 days       | 40           |   1                      |  XL, BM                      | 1534 GiB |         |

The following partitions are available on GPU nodes. Note that for each GPU, you should reserve at most 10 cores/task.

| Partition       | Time<br>limit | Max<br>GPUs | Max<br>nodes | [Node types](../systems-puhti.md) | Max<br>memory | Max<br>local storage (nvme) |
|-----------------|---------------|-------------|--------------|----------------------------|---------------|-----------------------------|
| gputest         | 15 minutes    | 8           | 2            | GPU                        | 382 GiB       | 3600 GiB                    |
| gpu             | 3 days        | 80          | 20           | GPU                        | 382 GiB       | 3600 GiB                    |


Information about the partition:

```
sinfo

```

or
```
scontrol show partition <partition_name>

```

!!! note "Notes on partitions"

    - ** Only request the memory you need **
        - The jobs will run sooner, since in each partition, most of the
          nodes have less memory than the maximum amount
        - Billing is based on memory requested, not on memory used
    - ** Only use longrun partitions if necessary **
        - These partitions have stricter limits and a lower priority
    - ** Only one job per user is allowed in _interactive_ partition **
        - Use this partition with the command [sinteractive](interactive-usage.md).


## Mahti partitions

The following full-node partitions (aka queues) are currently available in **Mahti** on CPU nodes. When using these partitions, your jobs use all resources available on the node and won't share the node with other jobs.

| Partition | Nodes       | Time<br>limit | Access           |
|-----------|-------------|---------------|------------------|
| test      | 1-2         | 1  hours      | all              |
| medium    | 1-20        | 36 hours      | all              |
| large     | 20-200      | 36 hours      | scalability test |
| gc          | 200-700       | 36 hours      | Grand Challenge  |

The following partition is available for allocation by resources in **Mahti** on CPU nodes. This means that you can request a sub-node allocation: you can request only part of the resources (cores and memory) available on the compute node. This also means that your job may share the node with other jobs. Each core reserved will provide 1.875 GB of memory and the only way to increase the memory reservation is to increase the number of cores reserved.

| Partition | Cores       | Time<br>limit | Max<br>memory    | Access           |
|-----------|-------------|---------------|------------------|------------------|
| interactive |  1-32      |  7 days      | 60 GiB           | all              |

The following partitions are available on GPU nodes. Note that for each GPU, you can reserve at most 32 cores/task and for each GPU the job is allocated 122.5 GiB of memory.


| Partition       | Time<br>limit | Max<br>GPUs | Max<br>nodes | [Node types](../systems-mahti.md) |  Max<br>local storage (nvme) |
|-----------------|---------------|-------------|--------------|----------------------------|-----------------------------|
| gputest         | 15 minutes    | 4           | 1            | GPU                        | 3800 GiB                    |
| gpusmall        | 36 hours      | 2           | 1            | GPU                        | 3800 GiB                    |
| gpumedium       | 36 hours      | 24          | 6            | GPU                        | 3800 GiB                    |

[Interactive partition](./interactive-usage.md#sinteractive-in-mahti), is intended for pre- and post processing tasks. 
It can be used both for interactive working and in batch jobs, where reserving a full node is not reasonable. 

The basic CPU based HPC computing should be done in _medium_, _large_ or _gc_ partitions. Only full nodes are allocated from these partitions and the jobs will have access to all cores and memory in the nodes. You may choose to run with fewer cores if that 
gives better performance. In these partitions billing is based on the allocated nodes.

The _large_ partition on Mahti is only accessible to projects that have done a
[scalability test](../../accounts/how-to-access-mahti-large-partition.md) and shown good utilisation of the resources. The partition
_gc_ is only accessible to [Grand Challenge projects](https://research.csc.fi/grand-challenge-proposals) and allows users to run extremely large simulations. 

