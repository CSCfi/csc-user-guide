# Available batch job partitions

## Puhti partitions

Currently, the following partitions (aka queues) are available in **Puhti**
for normal (CPU) nodes:

| Partition       | Time<br>Limit | Max<br>Tasks | Max<br>Nodes             | [Node-types](../system.md)   | Max<br> Mem  | Max<br> Local storage (nvme) |  
|-----------------|---------------|--------------|--------------------------|------------------------------|----------|----------|
| test            | 0.5 hour      | 160          |   4                      |  M                           | 382 GiB  |          |
| small           | 3 days        | 40           |   1                      |  M, L, IO                    | 382 GiB  | 3600 GiB |
| large           | 3 days        | 4000         |   100                    |  M, L, IO                    | 382 Gib  | 3600 GiB | 
| longrun         | 14 days       | 40           |   1                      |  M, L, IO                    | 382 GiB  | 3600 GiB | 
| hugemem         | 3 days        | 160          |   4                      |  XL, BM                      | 1534 GiB |         |
| hugemem_longrun | 14 days       | 40           |   1                      |  XL, BM                      | 1534 GiB |          |


For GPU nodes, the following partitions exist. Note that for each GPU one should reserve at most 10 cores/tasks.

| Partition       | Time<br>Limit | Max<br>GPUs | Max<br>Nodes             | [Node-types](../system.md)   | Max<br> Mem  | Max<br> Local storage (nvme) |  
|-----------------|---------------|-------------|--------------|------------------------------|----------|-------------|
| gputest        | 0.5 hour      | 8           |   2          |   GPU                        | 382 GiB  | 3600 GiB |
| gpu             | 3 days        | 80          |   20         |   GPU                        |382 GiB   | 3600 GiB |


You can also get information about the partition with the commands:

```
sinfo

```

or
```
scontrol show partition <partition_name>

```


!!! note "Notes on partitions"

    - ** Only request the memory you need **
        - jobs will be able to run sooner, since in each partition most of the
          nodes have less memory than the maximum amount
        - billing is based on requested memory, not on used memory
    - ** Only use longrun partitions if you have to **
        - these partitions have stricter limits and lower priority
