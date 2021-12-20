# Multi-GPU and multi-node machine learning

This guide explains how to utilize multiple GPUs and multiple nodes for machine
learning applications on CSC's supercomputers. It is part of our [Machine
learning guide](ml-guide.md).

## Multi-GPU, single-node jobs

Each GPU node (computer) in both Puhti and Mahti has 4 GPU cards. This means
that on a single node we can scale up to a maximum of 4 GPUs. The number of GPUs
requested is specified with the `--gres` flag. Below is an example of requesting
2 GPUs for a single Python instance:

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
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:2
    
    srun python3 myprog.py <options>
    ```

Note that on Mahti, the maximum for the `gpusmall` partition is 2 GPUs. For 4
GPUs or more you need to use the `gpumedium` partition.

!!! note 
    
    Please make sure that your code can actually take advantage of multiple GPUs as
    this typically requires some changes to the program. Simply reserving more GPUs
    isn't enough!
    
You can [monitor that your program is using all the reserved GPUs
efficiently](gpu-ml.md#gpu-utilization) with the same mechanisms described in
our GPU-accelerated machine learning guide. The only difference is that you
should now see statistics for more than one GPU.


## Multi-node jobs

For jobs requiring more than 4 GPUs one needs to scale up to using more than one
node (computer), which makes things more complicated. In particular, there needs
to be some mechanism for launching the jobs in each node and setting up the
communication between them.

We recommend using Slurm and MPI for launching the jobs, and NCCL for
interprocess communication. In particular
[Horovod](https://github.com/horovod/horovod) is a good framework for this, and
is supported in many of our TensorFlow and PyTorch modules. Many other
approaches do exist as well, such as [PyTorch
distributed](https://pytorch.org/tutorials/beginner/dist_overview.html) and
[DeepSpeed](https://www.deepspeed.ai/).

Independent of which framework you pick, pay attention what approach is used to
launch the jobs. Typically one of the two following methods are used:

- Slurm launches a single job (or task in MPI terminology) per node, and that
  job uses some other mechanism (such as launching additional Python processes)
  for using the four available GPUs,

- Slurm launches a separate job (task) *for each GPU*, i.e., four jobs per node.


### Horovod

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
use, just load the appropriate module, e.g:

```bash
module load tensorflow/2.7
```

Below are example Slurm batch scripts that use 8 GPUs across two nodes. In MPI
terminology we have 8 tasks on 2 nodes, with each task requesting one GPU and 10
CPUs. Referring back to the discussion in the previous section, here we are
using the separate-job-for-each-GPU approach.

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
    
    Note that on Mahti you have to use the `gpumedium` partition for multi-node
    jobs.
    
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```
    
### PyTorch distributed & DeepSpeed

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
