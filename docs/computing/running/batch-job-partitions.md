# Available batch job partitions

!!! info "Note"
    The available LUMI batch job partitions are found in [the LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/).

List all available partitions and their specifications on a system:

```
sinfo
```

Get details about a specific partition:

```
scontrol show partition <partition_name>
```

## Puhti partitions

The following partitions (aka queues) are currently available in **Puhti** for
normal (CPU) nodes:


| Partition       | Time<br>limit | Max<br>tasks | Max<br>nodes             | [Node types](../systems-puhti.md)   | Max<br>memory  | Max<br>local storage<br>[(NVMe)](../creating-job-scripts-puhti/#local-storage) |
|-----------------|---------------|--------------|--------------------------|------------------------------|----------|----------|
| test            | 15 minutes    | 80           |   2                      |  M                           | 185 GiB  |          |
| [interactive](interactive-usage.md)     | 7 days        | 8            |   1                      |  IO  | 76 GiB   | 720 GiB  |
| small           | 3 days        | 40           |   1                      |  M, L, IO                    | 373 GiB  | 3600 GiB |
| large           | 3 days        | 1040         |   26                     |  M, L, IO                    | 373 Gib  | 3600 GiB | 
| longrun         | 14 days       | 40           |   1                      |  M, L, IO                    | 373 GiB  | 3600 GiB | 
| hugemem         | 3 days        | 160          |   4                      |  XL, BM                      | 1496 GiB |         |
| hugemem_longrun | 14 days       | 40           |   1                      |  XL, BM                      | 1496 GiB |         |

The following partitions are available on GPU nodes. Note that for each GPU, you should reserve at most 10 cores/tasks.

| Partition       | Time<br>limit | Max<br>GPUs | Max<br>nodes | [Node types](../systems-puhti.md) | Max<br>memory | Max<br>local storage (NVMe) |
|-----------------|---------------|-------------|--------------|----------------------------|---------------|-----------------------------|
| gputest         | 15 minutes    | 8           | 2            | GPU                        | 373 GiB       | 3600 GiB                    |
| gpu             | 3 days        | 80          | 20           | GPU                        | 373 GiB       | 3600 GiB                    |


!!! info "Notes on partitions"
    1. **Use the `test` and `gputest` partitions for testing code**
        - The available resources are limited, but the queuing times are short
    2. **Only use the `gputest` and `gpu` partitions if you are sure your code
       uses GPUs**
        - There are more CPU nodes than GPU nodes, so your job will run sooner
          if using CPUs
    3. **Only request multiple CPU cores if you are sure your tool or code can
       use them**
        - Reserving more cores does nothing by itself, except make you queue
          for longer
    4. **Only request the memory you need**
        - Memory may become a bottleneck for resource requests; requesting less
          memory will decrease your time in queue
        - Billing is based on memory requested, not on memory used
    5. **Only use the `longrun` partitions if necessary**
        - These partitions have stricter limits and a lower priority
    6. **Only two jobs per user are allowed in the `interactive` partition**
        - Use through apps in the web interface or with the command
          [sinteractive](interactive-usage.md)

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
| [interactive](interactive-usage.md#sinteractive-in-mahti)  |  1-32      |  7 days      | 60 GiB           | all              |

The following partitions are available on GPU nodes. Note that for each full A100 GPU, you can reserve at most 32 cores/tasks and for each GPU the job is allocated 122.5 GiB of memory. 
A subset of the A100 GPUs are sliced into smaller a100_1g.5gb GPUs with one seventh of the compute and memory capacity of a full A100 GPU. For each small GPU you can reserve at most 
4 cores/tasks and for each GPU the job is allocated 17.5 GiB of memory. Also note that you can reserve at most one small GPU per job.


| Partition       | Time<br>limit | Max<br>GPUs | Max<br>nodes | [Node types](../systems-mahti.md) |  Max<br>local storage (NVMe) |
|-----------------|---------------|-------------|--------------|----------------------------|-----------------------------|
| gputest         | 15 minutes    | 4           | 1            | GPU                        | 3800 GiB                    |
| gpusmall        | 36 hours      | 2           | 1            | GPU                        | 3800 GiB                    |
| gpumedium       | 36 hours      | 24          | 6            | GPU                        | 3800 GiB                    |

[Interactive partition](./interactive-usage.md#sinteractive-in-mahti), is intended for pre- and post processing tasks. 
It can be used both for interactive working and in batch jobs, where reserving a full node is not reasonable. 

The basic CPU based HPC computing should be done in _medium_, _large_ or _gc_ partitions. Only full nodes are allocated from these partitions and the jobs will have access to all cores and memory in the nodes. You may choose to run with fewer cores if that 
gives better performance. In these partitions billing is based on the allocated nodes.

The _large_ partition on Mahti is only accessible to projects that have done a
[scalability test](../../accounts/how-to-access-mahti-large-partition.md) and shown good utilization of the resources. The partition
_gc_ is only accessible to [Grand Challenge projects](https://research.csc.fi/grand-challenge-proposals) and allows users to run extremely large simulations. 

