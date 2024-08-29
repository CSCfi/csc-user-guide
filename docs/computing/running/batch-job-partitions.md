# Available batch job partitions

On CSC supercomputers, programs are run by submitting them to partitions,
which are logical sets of nodes managed by the SLURM workload manager.
This page lists the available SLURM partitions on the Puhti and Mahti
supercomputers, as well as explains their intended uses. Below are the general
guidelines for using the SLURM partitions on our systems:

1. **Use the `test` and `gputest` partitions for testing your code, not production.**
   These partitions provide access to fewer resources than other partitions,
   but jobs submitted to them have a higher priority and are thus granted
   resources before other jobs.
2. **Only request multiple CPU cores if you know your program supports
   parallel processing.** Reserving multiple cores does not automatically
   speed up your job. Your program must be written in a way that the
   computations can be done in multiple threads or processes. Reserving more
   cores does nothing by itself, except make you queue for longer.
3. **Only use the GPU partitions if you know your program can utilize GPUs.**
   Running your computations using one or more GPUs is a very effective
   parallelization method for certain applications, but your program must be
   configured to use the CUDA platform. If you are unsure whether this is the
   case, it is better to submit it to a CPU partition, since you will be
   allocated resources sooner. You may also always
   [consult CSC Service Desk](../../support/contact.md) when in doubt.

The following commands can be used to show information about available
partitions:

```bash
# Display a summary of available partitions
$ sinfo --summarize

# Display details about a specific partition:
$ scontrol show partition <partition_name>
```

!!! info "LUMI partitions"
    The available LUMI batch job partitions are found in the
    [LUMI documentation].

## Puhti partitions

The following guidelines apply to the SLURM partitions on Puhti:

1. **Only request the memory you need.** Memory can easily end up being a
   bottleneck in resource allocation. Even if the desired amount of GPUs
   and/or CPU cores is continuously available, your job will sit in the queue
   for as long as it takes for the requested amount of memory to become
   free. It is thus recommended to only request the amount of memory that is
   necessary for running your job. Additionally, the amount of billing units
   consumed by your job is affected by the amount of memory requested, not
   the amount which was actually used. See
   [how to estimate your memory requirements](../../support/faq/how-much-memory-my-job-needs.md).
2. **Only use the `longrun` partitions if necessary.** The `longrun` and
   `hugemem_longrun` partitions provide access to fewer resources and have a
   lower priority than the other partitions, so it is recommended to use them
   only for jobs that *really* require a very long runtime (e.g. if there is no
   way to checkpoint and restart a computation).

### Puhti CPU partitions

Puhti features the following partitions for submitting jobs to CPU nodes:

| Partition         | Time<br>limit | Max CPU<br>cores | Max<br>nodes | [Node types](../systems-puhti.md) | Max memory<br>per node | Max local storage<br>([NVMe]) per node |
|-------------------|---------------|------------------|--------------|-----------------------------------|------------------------|----------------------------------------|
| `test`            | 15 minutes    | 80               | 2            | M                                 | 185 GiB                | n/a                                    |
| `small`           | 3 days        | 40               | 1            | M, L, IO                          | 373 GiB                | 3600 GiB                               |
| `large`           | 3 days        | 1040             | 26           | M, L, IO                          | 373 GiB                | 3600 GiB                               |
| `longrun`         | 14 days       | 40               | 1            | M, L, IO                          | 373 GiB                | 3600 GiB                               |
| `hugemem`         | 3 days        | 160              | 4            | XL, BM                            | 1496 GiB               | n/a                                    |
| `hugemem_longrun` | 14 days       | 40               | 1            | XL, BM                            | 1496 GiB               | n/a                                    |

### Puhti GPU partitions

Puhti features the following partitions for submitting jobs to GPU nodes:

| Partition | Time<br>limit | Max<br>GPUs | Max CPU<br>cores | Max<br>nodes | [Node types](../systems-puhti.md) | Max memory<br>per node | Max local storage<br>([NVMe]) per node |
|-----------|---------------|-------------|------------------|--------------|-----------------------------------|------------------------|----------------------------------------|
| `gputest` | 15 minutes    | 8           | 80               | 2            | GPU                               | 373 GiB                | 3600 GiB                               |
| `gpu`     | 3 days        | 80          | 800              | 20           | GPU                               | 373 GiB                | 3600 GiB                               |

!!! info "Fair use of GPU nodes on Puhti" 
    You should reserve **no more than 10 CPU cores per GPU**.

### Puhti `interactive` partition

The `interactive` partition on Puhti allows running
[interactive jobs](./interactive-usage.md) on CPU nodes. To run an
interactive job on a GPU node, use `sinteractive` command
[with the `-g` option](./interactive-usage.md#sinteractive-on-puhti),
which submits the job to the `gpu` partition instead. Note that you can only
run two simultaneous jobs on the Puhti `interactive` partition.

| Partition     | Time<br>limit | Max CPU<br>cores | Max<br>nodes | [Node types](../systems-puhti.md) | Max memory<br>per node | Max local storage<br>([NVMe]) per node |
|---------------|---------------|------------------|--------------|-----------------------------------|------------------------|----------------------------------------|
| `interactive` | 7 days        | 8                | 1            | IO                                | 76 GiB                 | 720 GiB                                |

## Mahti partitions

### Mahti CPU partitions

Mahti features the following partitions for submitting jobs to CPU nodes. Jobs
submitted to these partitions occupy
[all of the resources available on a node](../systems-mahti.md#compute-nodes)
and make it inaccessible to other jobs. Thus, your job should ideally be able
to utilize all 128 cores available on each reserved node efficiently. Although
in certain situations it may be worthwhile to
[undersubscribe nodes](creating-job-scripts-mahti.md#undersubscribing-nodes),
note that your job will still consume billing units based on the amount of
reserved *nodes*, not CPU cores.

Some partitions are only available under special conditions. The `large`
partition is only accessible to projects that have
[completed a scalability test](../../accounts/how-to-access-mahti-large-partition.md)
and demonstrated good utilization of the partition resources. The `gc`
partition, which allows users to run extremely large simulations, is only
accessible to
[Grand Challenge projects](https://research.csc.fi/grand-challenge-proposals).

| Partition | Time<br>limit | CPU cores<br>per node | Nodes<br>per job | [Node types](../systems-mahti.md) | Memory<br>per node | Max local storage<br>([NVMe]) per node | Requirements                    |
|-----------|---------------|-----------------------|------------------|-----------------------------------|--------------------|----------------------------------------|---------------------------------|
| `test`    | 1 hour        | 128                   | 1–2              | CPU                               | 256 GiB            | n/a                                    | n/a                             |
| `medium`  | 36 hours      | 128                   | 1–20             | CPU                               | 256 GiB            | n/a                                    | n/a                             |
| `large`   | 36 hours      | 128                   | 20–200           | CPU                               | 256 GiB            | n/a                                    | [scalability test]              |
| `gc`      | 36 hours      | 128                   | 200–700          | CPU                               | 256 GiB            | n/a                                    | [Grand Challenge project]       |

### Mahti GPU partitions

Mahti features the following partitions for submitting jobs to GPU nodes.
Unless otherwise specified, the job is allocated 122.5 GiB of memory for
each reserved GPU.

| Partition   | Time<br>limit | Max<br>GPUs | Max CPU<br>cores | Max<br>nodes | [Node types](../systems-mahti.md) | Max memory<br>per node | Max local storage<br>([NVMe]) per node |
|-------------|---------------|-------------|------------------|--------------|-----------------------------------|------------------------|----------------------------------------|
| `gputest`   | 15 minutes    | 4           | 128              | 1            | GPU                               | 490 GiB                | 3800 GiB                               |
| `gpusmall`  | 36 hours      | 2           | 64               | 1            | GPU                               | 490 GiB                | 3800 GiB                               |
| `gpumedium` | 36 hours      | 24          | 768              | 6            | GPU                               | 490 GiB                | 3800 GiB                               |

!!! info "Fair use of GPU nodes on Mahti"
    You should reserve **no more than 32 CPU cores per GPU**.

#### GPU slices

A subset of the Nvidia A100 GPUs on the Mahti `gpusmall` partition are divided
into a total of 28 smaller GPU slices, which have one-seventh of the
compute and memory capacity of a full A100 GPU. You are able to reserve at
most 4 CPU cores when using a GPU slice. Additionally, the job is allocated
17.5 GiB of memory, and there is no way to request a different amount. Finally,
you are only able to reserve one GPU slice per job. The GPU slices are intended
especially for interactive use that requires GPU capacity.

To reserve a GPU slice, use `sinteractive` with the `-g` option, or include the
`--gres=gpu:a100_1g.5gb:1` option together with specifying the `gpusmall`
partition in your batch script. For more information, see the instructions on
[creating GPU batch jobs on Mahti](creating-job-scripts-mahti.md#gpu-batch-jobs).

### Mahti `interactive` partition

The `interactive` partition on Mahti is intended for
[interactive pre- and post-processing tasks](./interactive-usage.md). It
allows reserving CPU resources without occupying an entire node, which means
that other jobs may also access the same node. You can run up to 8
simultaneous jobs on the `interactive` partition and reserve at most 32 cores,
i.e. you may have one job using 32 cores, 8 jobs using 4 cores each, or
anything in between. Mahti interactive jobs are allocated 1.875 GiB of memory
for each reserved CPU core, and the only way to reserve more memory is to
reserve more cores.

| Partition     | Time<br>limit | Max CPU<br>cores | Max<br>nodes | [Node types](../systems-mahti.md) | Max memory<br>per node | Max local storage<br>([NVMe]) per node |
|---------------|---------------|------------------|--------------|-----------------------------------|------------------------|----------------------------------------|
| `interactive` | 7 days        | 32               | 1            | CPU                               | 60 GiB                 | n/a                                    |

<!-- Links -->
[Grand Challenge project]: https://research.csc.fi/grand-challenge-proposals
[LUMI documentation]: https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/
[NVMe]: ../disk.md#compute-nodes-with-local-ssd-nvme-disks
[scalability test]: ../../accounts/how-to-access-mahti-large-partition.md
<!-- Links -->
