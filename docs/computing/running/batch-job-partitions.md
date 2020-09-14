# Available batch job partitions

## Puhti partitions

The following partitions (aka queues) are currently available in **Puhti** for
normal (CPU) nodes:


| Partition       | Time<br>limit | Max<br>tasks | Max<br>nodes             | [Node types](../systems-puhti.md)   | Max<br>memory  | Max<br>local storage (nvme) |  
|-----------------|---------------|--------------|--------------------------|------------------------------|----------|----------|
| test            | 15 minutes    | 80           |   2                      |  M                           | 382 GiB  |          |
| interactive     | 7 days        | 1            |   1                      |  IO                          | 16 GiB   | 160 GiB  |
| small           | 3 days        | 40           |   1                      |  M, L, IO                    | 382 GiB  | 3600 GiB |
| large           | 3 days        | 4000         |   100                    |  M, L, IO                    | 382 Gib  | 3600 GiB | 
| longrun         | 14 days       | 40           |   1                      |  M, L, IO                    | 382 GiB  | 3600 GiB | 
| hugemem         | 3 days        | 160          |   4                      |  XL, BM                      | 1534 GiB |         |
| hugemem_longrun | 7 days       | 40           |   1                      |  XL, BM                      | 1534 GiB |         |

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

The following partitions (aka queues) are currently available in **Mahti**:

| Partition | Nodes       | Time<br>limit | Access           |
|-----------|-------------|---------------|------------------|
| test      | 1-2         | 1  hours      | all              |
| medium    | 1-20        | 36 hours      | all              |
| large     | 20-200      | 36 hours      | scalability test |
| gc        | 1-700       | 36 hours      | Grand Challenge  |
| interactive | 1         |  7 days       | all              |

Large partition on Mahti is only accessible to projects that have done a
[scalability test](../../accounts/how-to-access-mahti-large-partition.md) and shown good utilisation of the resources. The partition
`qc` is only accessible to Grand Challenge projects and has a higher
priority.

!!! note "Notes on partitions"

    - ** Only full nodes are allocated on Mahti **
        - Jobs will have access to all cores and memory in a node, but
		may choose to run with fewer cores if that gives better performance
        - Billing is based on the allocated nodes.


