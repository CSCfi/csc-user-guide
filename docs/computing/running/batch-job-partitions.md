# Available batch job partitions

On CSC supercomputers, programs are run by submitting them to partitions,
which are logical sets of nodes managed by the Slurm workload manager.
This page lists the available Slurm partitions on the Roihu, Puhti, and Mahti
supercomputers and explains their intended uses. Below are the general
guidelines for using the Slurm partitions on our systems:

1. **Use the `test` and `gputest` partitions for testing your code, not production.**
   These partitions provide access to fewer resources than other partitions,
   but jobs submitted to them have a higher priority and are thus granted
   resources before other jobs.
2. **Only request multiple CPU cores if you know your program supports
   parallel processing.** Reserving multiple cores does not automatically
   speed up your job. Your program must be written in a way that the
   computations can be performed in multiple threads or processes. Reserving more
   cores does nothing by itself if your code is not parallelized,
   except making you queue for longer.
3. **Only use the GPU partitions if you know your program can utilize GPUs.**
   Running your computations using one or more GPUs is a very effective
   parallelization method for certain applications, but your program must be
   configured to use the CUDA platform. If you are unsure whether this is the
   case, it is better to submit your job to a CPU partition, since you will be
   allocated resources sooner. If unsure, contact the
   [CSC Service Desk](../../support/contact.md).

The following commands can be used to show information about available
partitions:

```bash
# Display a summary of available partitions
sinfo --summarize
```

```bash
# Display details about a specific partition:
scontrol show partition <partition_name>
```

!!! info "LUMI partitions"
    The available LUMI batch job partitions are found in the
    [LUMI documentation].

## Roihu partitions

Roihu partitions use different allocation types that cater to varying use cases
and resource requirements. These are explained in the table below.

| Allocation type | Resource request                                                          |
|:---------------:|---------------------------------------------------------------------------|
| R               | Memory and CPU resources can be changed independently                     |
| N               | Full-node requests only                                                   |
| C               | Memory allocation is fixed based on the requested number of CPU cores     |
| G               | CPU and memory allocation is fixed based on the requested number of GPUs  |

### Roihu CPU partitions

Roihu provides the following partitions for submitting jobs to CPU nodes:

| Partition         | Allocation type | Time limit | Nodes  | Max CPUs      | [Node types](../systems-roihu.md#nodes) | Max memory            | Requirements       |
|-------------------|-----------------|------------|--------|---------------|-----------------------------------------|-----------------------|--------------------|
| `test`            | R               | 15 minutes | 1 - 2  | 384 per node  | M                                       | 744 GiB per node      |                    |
| `small`           | R               | 72 hours   | 1      | 384 per job   | M, L                                    | 1500 GiB per job      |                    |
| `medium`          | N               | 36 hours   | 1 - 6  | 384 per node  | M                                       | 744 GiB per node      |                    |
| `large`           | N               | 36 hours   | 6 - 60 | 384 per node  | M                                       | 744 GiB per node      | [scalability test](../../accounts/how-to-access-roihu-large-partition.md) |
| `longrun`         | R               | 10 days    | 1      | 192 per job   | M, L                                    | 1500 GiB per job      |                    |
| `hugemem`         | C               | 36 hours   | 1      | 128 per job   | XL                                      | 6037 GiB per job      |                    |
| `hugemem_longrun` | C               | 10 days    | 1      | 128 per job   | XL                                      | 6037 GiB per job      |                    |

### Roihu GPU partitions

Roihu provides the following partitions for submitting jobs to GPU nodes:

| Partition        | Allocation type | Time limit | Nodes  | Min GPUs | Max GPUs      | [Node types](../systems-roihu.md#nodes) | Max memory       | Requirements       |
|------------------|-----------------|------------|--------|----------|---------------|-----------------------------------------|------------------|--------------------|
| `gputest`        | G               | 15 minutes | 1 - 2  | 1        | 4 per node    | GPU                                     | 217 GiB per reserved GPU |                    |
| `gpumedium`      | G               | 36 hours   | 1 - 4  | 1        | 4 per job     | GPU                                     | 217 GiB per reserved GPU |                    |
| `gpularge`       | G               | 36 hours   | 1 - 10 | 4        | 4 per node    | GPU                                     | 217 GiB per reserved GPU | [scalability test](../../accounts/how-to-access-roihu-large-partition.md) |

Each full GPU node has 4 GH200 GPUs. Each reserved GPU grants access to up to **72 CPU cores**, and
95 GiB of HBM3 memory + 122 GiB of LPDDR5 memory, for a total of **217G available memory** per reserved GPU.

The memory amounts listed here are the allocatable amounts available to jobs;
some memory is reserved for system use.

### Roihu interactive partitions

Roihu has several partitions reserved for interactive use and for data visualization.

#### Roihu-CPU interactive use

The `interactive` partition on Roihu allows running
[interactive jobs](./interactive-usage.md) on CPU nodes, through the `sinteractive` command.

The `sinteractive` command selects the correct partition based on your resource request
and automatically provides Roihu-CPU resources when run from a Roihu-CPU login node.

| Partition         | Allocation type | Time limit | Nodes  | Max CPUs      | [Node types](../systems-roihu.md#nodes) | Max memory            |
|-------------------|-----------------|------------|--------|---------------|-----------------------------------------|-----------------------|
| `interactive`     | R               | 36 hours   | 1      | 32 per job    | M                                       | 64 GiB per job        |

#### Roihu-GPU interactive use

The `gpuinteractive` partition on Roihu allows running
[interactive jobs](./interactive-usage.md) on GPU nodes, through the `sinteractive` command.

The `sinteractive` command selects the correct partition based on your resource request
and automatically provides a GPU slice when run from a Roihu-GPU login node.

| Partition         | Allocation type | Time limit | Nodes  | Max CPUs  | Max GPU slices | [Node types](../systems-roihu.md#nodes) |
|-------------------|-----------------|------------|--------|-----------|----------------|-----------------------------------------|
| `gpuinteractive`  | G               | 12 hours   | 1      | TBA       | TBA            | GPU (slice)                             |

!!! info "What is a GPU slice?"
    The Roihu gpuinteractive partition consists of two nodes, each containing four GH200 GPUs.
    Each GPU can be divided into up to seven 1g.12gb MIG slices, providing up to 56 GPU slices across the partition.
    Each slice provides one-seventh of the GPU compute capacity and one-eighth of the GPU memory capacity (12 GiB) of a full GH200 GPU.

!!! note "GPU slices not yet fully configured"
    GPU slices are not yet configured on the system, and reserving GPUs through `sinteractive`, or through Slurm on the partition
    will instead provide full GPUs.

#### Vizinteractive

Roihu also features the following partition for interactive use and data visualization with specialized hardware:

| Partition        | Allocation type | Time limit | Nodes | Max GPUs  | [Node types](../systems-roihu.md#nodes) |
|------------------|-----------------|------------|-------|-----------|-----------------------------------------|
| `vizinteractive` | G               | 12 hours   | 1     | 2 per job | V                                       |

Each node in the partition has 2 Nvidia L40 GPUs with 48 GB of memory and two 32-core AMD Turin 9335 CPUs.
Each reserved GPU grants access to up to 32 CPU cores and 183 GiB of CPU memory.

### Local storage on Roihu nodes

Local storage on Roihu M, L, and GPU nodes is meant for storing temporary files only, not high-performance I/O.

High-performance local storage is available on Roihu XL and V nodes, which is ideal for I/O-intensive jobs.

There are two kinds of node-local storage: **automatic temporary storage**
(`$TMPDIR`), available in every job without a reservation and free of charge,
and **reservable local scratch** (`$LOCAL_SCRATCH`), which is only available
on the XL and V nodes, is reserved through Slurm with the `--gres=nvme`
option, and consumes billing units.

The amount of local storage available to a single user depends on the [partition](#roihu-partitions) used:

=== "Automatic (`$TMPDIR`)"

    | Allocation type         | Available per user | Read / Write speeds |
    |:------------------------|-------------------:|---------------------|
    | R (shared nodes)        | 20 GiB             | 5000 / 1400 MB/s    |
    | N (full nodes)          | 600 GiB            | 5000 / 1400 MB/s    |
    | G (GPU nodes)           | 150 GiB            | 5000 / 1400 MB/s    |
    | Hugemem (XL) nodes      | 578 GiB            | 6700 / 4000 MB/s    |
    | V (visualization nodes) | 14 TiB             | 6700 / 4000 MB/s    |

    Reservable local scratch has not yet been implemented on visualization nodes (V).
    Until it is available, jobs on these nodes can use the full `$TMPDIR` allocation shown above.

    Once reservable local scratch is implemented, the amount of `$TMPDIR` available per user on visualization nodes will be reduced.

=== "Reservable (`$LOCAL_SCRATCH`)"

    | Node type               | Maximum reservable | Read / Write speeds |
    |:------------------------|-------------------:|---------------------|
    | Hugemem (XL) nodes      | 13 TiB             | 6700 / 4000 MB/s    |
    | V (visualization nodes) | 6.5 TiB per user   | 6700 / 4000 MB/s    |

    Reserving local scratch on the visualization nodes is not yet
    implemented; use `$TMPDIR` on these nodes until this feature is added.

Read more about: [Local storage on Roihu nodes](../roihu-disk.md#temporary-local-disk-areas)

<!-- Links -->
[LUMI documentation]: https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/
<!-- Links -->
