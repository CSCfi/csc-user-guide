# Multi-GPU and multi-node machine learning

This guide explains how to utilize multiple GPUs and multiple nodes for machine
learning applications on CSC's supercomputers. It is part of our [Machine
learning guide](ml-guide.md).

## Nodes and tasks

### GPU Nodes

Each separate GPU computer, or GPU **node**, has a small number of
GPUs. Puhti and Mahti have 4 GPUs per node, and LUMI has 8 GPUs. The
supercomputer may have tens or even thousands of GPU nodes. See
[GPU-accelerated machine learning](gpu-ml.md) for more details.  If
you need 1-4 GPUs (or 1-8 in LUMI) you should always reserve a
**single node job**. If you need more than 4 GPUs (or 8 in LUMI) you
need to reserve a **multi-node job**. You can then only reserve full
nodes, i.e., the number of GPUs will be a multiple of 4 (or 8).

### MPI tasks

When parallelizing to multiple GPUs it is common to allocate a
separate CPU process for handling the communication to each GPU. This
per GPU task division may be handled by the program itself, for
example using [Python's multiprocessing
library](https://docs.python.org/3/library/multiprocessing.html) to
launch separate processes, or one can use Slurm's MPI facility to
launch **multiple MPI tasks**. Whether MPI tasks are used or not
depends on the software framework used.

### Slurm examples

Below are Slurm batch script examples for launching single- or multi-node jobs, with or without MPI.

!!! warning "Note"
    
    Please make sure that your code can actually take advantage of multiple GPUs as
    this typically requires some changes to the program. **Simply reserving more GPUs
    isn't enough!**
    
You can [monitor that your program is using all the reserved GPUs
efficiently](gpu-ml.md#gpu-utilization) with the same mechanisms described in
our GPU-accelerated machine learning guide. The only difference is that you
should now see statistics for more than one GPU.


#### Single node run using 2 GPUs, no MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=20
    #SBATCH --mem=64G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:2
        
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=10
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:2
    
    srun python3 myprog.py <options>
    ```
    
    Note that on Mahti, the maximum for the `gpusmall` partition is 2
    GPUs. For 3 or 4 GPUs or more you need to use the `gpumedium`
    partition.

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=16
    #SBATCH --gpus-per-task=2
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 myprog.py <options>
    ```

The example above can be easily changed to more than 2 GPUs by
changing the number specified in the `--gres` option (Puhti and Mahti)
or `--gpus-per-task` option (LUMI). The maximum for a single node job
is 4 GPUs or 8 (LUMI).

#### Single node using all GPUs, using MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=8
    #SBATCH --gpus-per-task=1
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 myprog.py <options>
    ```


#### Multi-node with 2 full nodes, no MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=64
    #SBATCH --gpus-per-task=8
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 myprog.py <options>
    ```


#### Multi-node with 2 full nodes, using MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=64G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=10
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=8
    #SBATCH --gpus-per-task=1
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 myprog.py <options>
    ```


## Available frameworks

Independent of which framework you pick, pay attention what approach is used to
launch the jobs. Typically one of the two following methods are used:

- Slurm launches a single job (or task in MPI terminology) per node, and that
  job uses some other mechanism (such as launching additional Python processes)
  for using the four available GPUs,

- Slurm launches a separate job (task) *for each GPU*, i.e., four jobs per node.


### Pytorch DDP

[PyTorch distributed](https://pytorch.org/tutorials/beginner/dist_overview.html)

PyTorch Distributed, and in particular Distributed Data-Parallel (DDP), offers a
nice way of running multi-GPU and multi-node PyTorch jobs. Unfortunately, here,
the official PyTorch documentation and usage examples are sadly out-of-date with
often conflicting and confusing advice given.

To make usage of DDP on CSC's supercomputers easier, we have created a [set of
examples on how to run simple DDP jobs in the
cluster](https://github.com/CSCfi/pytorch-ddp-examples). That repository also
contains some examples of DeepSpeed usage. Note that `pytorch/1.10` has
experimental support for DeepSpeed, and it does not need to be installed
manually anymore.


### DeepSpeed

[DeepSpeed](https://www.deepspeed.ai/)

### Horovod

[Horovod](https://github.com/horovod/horovod) uses MPI for launching jobs.

For large jobs requiring more than 4 GPUs we recommend using
[Horovod](https://github.com/horovod/horovod), which at CSC is supported for
TensorFlow and PyTorch. Horovod uses MPI and NCCL for interprocess
communication. See also [MPI based batch
jobs](../../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs).
Horovod can also be used with single-node jobs for 4 GPUs, and in some
benchmarks this has proved to be faster than other multi-GPU implementations.

Note that Horovod is supported only for some specific versions of
[TensorFlow](../../apps/tensorflow.md) and [PyTorch](../../apps/pytorch.md).
Please check the application pages for further information. To take Horovod into
use, just load the appropriate module.


### TF multistrategies

Some text here.
