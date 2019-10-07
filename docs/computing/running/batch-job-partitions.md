# Available batch job partitions

## Puhti partitions

The following partitions (aka queues) are currently available in **Puhti** for normal (CPU) nodes:

| Partition       | Time<br>limit | Max<br>tasks | Max<br>nodes             | [Node types](../system.md)   | Max<br>memory  | Max<br>local storage (nvme) |  
|-----------------|---------------|--------------|--------------------------|------------------------------|----------|----------|
| test            | 0,5 hours     | 160          |   4                      |  M                           | 382 GiB  |          |
| small           | 3 days        | 40           |   1                      |  M, L, IO                    | 382 GiB  | 3600 GiB |
| large           | 3 days        | 4000         |   100                    |  M, L, IO                    | 382 Gib  | 3600 GiB | 
| longrun         | 14 days       | 40           |   1                      |  M, L, IO                    | 382 GiB  | 3600 GiB | 
| hugemem         | 3 days        | 160          |   4                      |  XL, BM                      | 1534 GiB |         |
| hugemem_longrun | 7 days       | 40           |   1                      |  XL, BM                      | 1534 GiB |         |


The following partitions are available on GPU nodes. Note that for each GPU, you should reserve at most 10 cores/task.

| Partition       | Time<br>limit | Max<br>GPUs | Max<br>nodes             | [Node types](../system.md)   | Max<br>memory  | Max<br>local storage (nvme) |  
|-----------------|---------------|-------------|--------------|------------------------------|----------|-------------|
| gputest         | 0,5 hours     | 8           |   2          |   GPU                        | 382 GiB  | 3600 GiB    |
| gpu             | 3 days        | 80          |   20         |   GPU                        | 382 GiB  | 3600 GiB    |


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
