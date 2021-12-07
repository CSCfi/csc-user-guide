# Multi-GPU and multi-node machine learning

## Multi-GPU, single-node jobs

Each GPU node (computer) in both Puhti and Mahti have 4 GPU cards. This means
that on a single computer we can scale up to a maximum of 4 GPUs. The number of
GPUs required is specified with the `--gres` flag. Below is an example of
requesting 2 GPUs, but running with a single Python instance:

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

Note that on Mahti, the `gpusmall` partition only supports a maximum of 2 GPUs,
for 4 GPUs or more you need to use the `gpumedium` partition. 

!!! note 
    
    Please make sure that your code can actually take advantage of multiple
    GPUs, this typically requires some changes to the program. Simply reserving
    more GPUs isn't enough!
    
You can [monitor that your program is using all the reserved GPUs
efficiently](gpu-ml.md#gpu-utilization) with the same mechanisms described in
our GPU-accelerated machine learning guide. The only difference is that you
should now see statistics for more than one GPU.


## Multi-node jobs

For jobs requiring more than 4 GPUs one needs to scale up to using more than one
node (computer), which makes things more complicated. In particular there needs
to be some mechanism for launching jobs in each node and setting up the
communication between them.

We recommend using Slurm and MPI for launching the jobs, and NCCL for
interprocess communication. In particular
[Horovod](https://github.com/horovod/horovod) is a good framework for this, and
is supported in some of our TensorFlow and PyTorch modules. Many other
approaches do exist as well, such as [PyTorch
distributed](https://pytorch.org/tutorials/beginner/dist_overview.html) and
[DeepSpeed](https://www.deepspeed.ai/).

Independent of which framework you pick, pay attention what approach is used to
launch the jobs. Typically one of two methods are used:

- Slurm launches a single job (or task in MPI terminology) per node, and that
  job uses some other mechanism (such as launching additional Python processes)
  for using the four available GPUs,

- Slurm launches a single job (task) *per GPU*, i.e., four jobs per node.


### Horovod

For large jobs requiring more than 4 GPUs we recommend using
[Horovod](https://github.com/horovod/horovod), which is supported for TensorFlow
and PyTorch. Horovod uses MPI and NCCL for interprocess communication. See also
[MPI based batch
jobs](../../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs).
Horovod can also be used with single-node jobs for 4 GPUs, and in some
benchmarks this has proved to be faster than other multi-GPU implementations.

Note that Horovod is supported only for some specific versions of TensorFlow and
PyTorch, please check the application pages to see which versions support
Horovod. To take Horovod into use, just load the appropriate module, e.g:

```bash
module load tensorflow/2.7
```

Below are example slurm batch scripts that use 8 GPUs across two computers. In
MPI terminology we have 8 tasks on 2 nodes, each task has one GPU and 10 CPUs.
Referring back to the discussion in the previous section, here we are using the
single-job-per-GPU approach.

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
    
### PyTorch distributed

PyTorch Distributed, and in particular Distributed Data-Parallel (DDP), offers a
nice way of running multi-GPU and multi-node PyTorch jobs. Unfortunately, in
this instance, the official PyTorch documentation and usage examples are sadly
out-of-date with often conflicting and confusing advice given.

To make usage of DDP on CSC's Supercomputers easier, we have created a [set of
examples on how to run simple DDP jobs on the
cluster](https://github.com/CSCfi/pytorch-ddp-examples). That repository also
has some example of DeepSpeed usage. Note that `pytorch/1.10` has experimental
support for DeepSpeed, and it does not need to be installed manually anymore.
