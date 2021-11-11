# Multi-GPU and multi-node machine learning jobs

Multi-GPU jobs are also supported by specifying the number of GPUs required in
the `--gres` flag, for example to have 4 GPUs on Puhti (which is the maximum for
a single node): `--gres=gpu:v100:4`. On Mahti the flag would be:
`--gres=gpu:a100:4`. Note that on Mahti, the `gpusmall` partition only supports
a maximum of 2 GPUs, for 4 GPUs or more you need to use the `gpumedium` partition.
**Please also make sure that your code can take advantage of
multiple GPUs, this typically requires some changes to the program**.

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
module load tensorflow/2.4
```

Below are example slurm batch scripts that use 8 GPUs across two computers. In
MPI terminology we have 8 tasks on 2 nodes, each task has one GPU and 10 CPUs.

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
    
