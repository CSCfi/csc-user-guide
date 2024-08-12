# Available batch job partitions

!!! info "Note"
    The available LUMI batch job partitions are found in
    [the LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/).

List all available partitions and their specifications on a system:

```
sinfo
```

Get details about a specific partition:

```
scontrol show partition <partition_name>
```

## Puhti partitions

Puhti features the following partitions for submitting jobs to CPU nodes:

| Partition         | Time<br>limit | Max<br>tasks | Max<br>nodes | [Node types](../systems-puhti.md) | Max<br>memory | Max<br>local storage<br>([NVMe]) |
|-------------------|---------------|--------------|--------------|-----------------------------------|---------------|----------------------------------|
| `test`            | 15 minutes    | 80           | 2            | M                                 | 185 GiB       | n/a                              |
| `small`           | 3 days        | 40           | 1            | M, L, IO                          | 373 GiB       | 3600 GiB                         |
| `large`           | 3 days        | 1040         | 26           | M, L, IO                          | 373 Gib       | 3600 GiB                         |
| `longrun`         | 14 days       | 40           | 1            | M, L, IO                          | 373 GiB       | 3600 GiB                         |
| `hugemem`         | 3 days        | 160          | 4            | XL, BM                            | 1496 GiB      | n/a                              |
| `hugemem_longrun` | 14 days       | 40           | 1            | XL, BM                            | 1496 GiB      | n/a                              |

The following partitions are available for submitting jobs to GPU nodes. Note
that you should reserve at most 10 cores or tasks per GPU.

| Partition | Time<br>limit | Max<br>GPUs | Max<br>nodes | [Node types](../systems-puhti.md) | Max<br>memory | Max<br>local storage ([NVMe]) |
|-----------|---------------|-------------|--------------|-----------------------------------|---------------|-------------------------------|
| `gputest` | 15 minutes    | 8           | 2            | GPU                               | 373 GiB       | 3600 GiB                      |
| `gpu`     | 3 days        | 80          | 20           | GPU                               | 373 GiB       | 3600 GiB                      |

The
[interactive partition on Puhti](./interactive-usage.md#sinteractive-in-puhti)
allows running interactive jobs on both CPU and GPU nodes. 

| Partition     | Time<br>limit | Max<br>GPUs | Max<br>nodes | [Node types](../systems-puhti.md) | Max<br>memory | Max<br>local storage ([NVMe]) |
|---------------|---------------|-------------|--------------|-----------------------------------|---------------|-------------------------------|
| `interactive` | 7 days        | 8           | 1            | IO, GPU                           | 76 GiB        | 720 GiB                       |

!!! note "Interactive GPU usage"

    To run your job on a GPU node,
    [use `sinteractive` with the `--gpu` option](./interactive-usage.md#sinteractive-in-puhti).

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

Mahti features the following partitions for submitting jobs to CPU nodes. Jobs
submitted to these partitions occupy all of the resources available on the
node and make it inaccessible to other jobs. While you need not use all
of the cores on the node, your job will nonetheless consume billing units
based on the amount of reserved nodes.

Some partitions are only available under special conditions. The `large`
partition is only accessible to projects that have completed a
[scalability test](../../accounts/how-to-access-mahti-large-partition.md) and
demonstrated good utilization of the partition resources. The `gc` partition,
which allows users to run extremely large simulations, is only accessible to
[Grand Challenge projects](https://research.csc.fi/grand-challenge-proposals).

| Partition | Nodes   | Time<br>limit | Availability               |
|-----------|---------|---------------|----------------------------|
| `test`    | 1–2     | 1 hour        | all projects               |
| `medium`  | 1–20    | 36 hours      | all projects               |
| `large`   | 20–200  | 36 hours      | requires scalability test  |
| `gc`      | 200–700 | 36 hours      | Grand Challenge projects   |

The following partitions are available for submitting jobs to GPU nodes.
Unless you specify otherwise, the job is allocated 122.5 GiB of memory for
each reserved GPU. Note that should reserve at most 32 cores or tasks per GPU.

A subset of the A100 GPUs in the `gpusmall` partition are divided into a total
of 28 smaller multi-instance GPUs (MIGs), which have one-seventh of the
compute and memory capacity of a full A100 GPU. Unless you specify otherwise,
the job is allocated 17.5 GiB of memory for each reserved MIG. Note that **you
can only reserve one MIG per job**, and that you should reserve at most 4
cores or tasks for the MIG.

| Partition   | Time<br>limit | Max<br>GPUs | Max<br>nodes | [Node types](../systems-mahti.md) | Max<br>local storage ([NVMe]) |
|-------------|---------------|-------------|--------------|-----------------------------------|-------------------------------|
| `gputest`   | 15 minutes    | 4           | 1            | GPU                               | 3800 GiB                      |
| `gpusmall`  | 36 hours      | 2           | 1            | GPU                               | 3800 GiB                      |
| `gpumedium` | 36 hours      | 24          | 6            | GPU                               | 3800 GiB                      |

!!! note "Reserving a MIG"

    You can reserve a MIG with the option `--gres=gpu:a100_1g.5bg:1`.
    For more information, see the instructions on
    [creating GPU batch jobs on Mahti](./creating-job-scripts-mahti.md#gpu-batch-jobs).

The
[interactive partition on Mahti](./interactive-usage.md#sinteractive-in-mahti)
is intended for pre- and post-processing tasks. It allows reserving CPU
resources without occupying an entire node, which means that other jobs may
also access the same node. Interactive jobs are allocated 1.875 GiB of memory
for each reserved CPU core, and the only way to reserve more memory is to
reserve more cores. The partition can be used both for jobs launched using
`sinteractive` as well as batch jobs, as long as they match the intended usage.

| Partition     | Cores       | Time<br>limit | Max<br>memory | Availability |
|---------------|-------------|---------------|---------------|--------------|
| `interactive` | 1–32        |  7 days       | 60 GiB        | all          |

<!-- Links -->
[NVMe]: ./creating-job-scripts-puhti.md#local-storage
<!---->
