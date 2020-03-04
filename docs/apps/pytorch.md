# PyTorch

Machine learning framework for Python.

## Available

The `pytorch` module is available on Puhti only.  Current versions:

- 1.4 (currently corresponds to 1.4.0, may be upgraded to newer point release later if needed)
- 1.3.1
- 1.3.1-hvd (with [Horovod](https://github.com/horovod/horovod) support using hpcx-mpi)
- 1.3.1-hvd-mpich (with [Horovod](https://github.com/horovod/horovod) support using mpich MPI)
- 1.3.0
- 1.2.0
- 1.1.0
- 1.0.1

Includes [PyTorch](https://pytorch.org/) and related libraries with GPU support via CUDA.  Also includes all the packages from [Python Data](python-data.md).

If you find that some package is missing, you can often install it yourself with `pip install --user`.

If you think that some important PyTorch-related package should be included in the module provided by CSC, you can send an email to <servicedesk@csc.fi>.

Alternatively you can also run PyTorch via [Singularity images](../computing/containers/run-existing.md), see [here for a usage example](../support/tutorials/gpu-ml.md#singularity).

## License

PyTorch is BSD-style licensed, as found in the [LICENSE file](https://github.com/pytorch/pytorch/blob/master/LICENSE).

## Usage

To use this software on Puhti, initialize it with:

```text
module load pytorch
```

to access the default version.

This will show all available versions:

```text
module avail pytorch
```

To check the exact packages and versions included in the loaded module you can run:

```text
list-packages
```


!!! note 

    Note that Puhti login nodes are not intended for heavy computing, please use slurm batch jobs instead. See our [instructions on how to use the batch job system](../computing/running/getting-started.md).

### Example batch script

Example batch script for reserving one GPU and 10 CPUs in a single node:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1

module load pytorch/1.4
srun python3 myprog.py <options>
```

!!! note

    Please **do not read a huge number of files from the shared file system**, use fast local disk or package your data into larger files instead!  See the [GPU-accelerated machine learning guide](../support/tutorials/gpu-ml.md#data-storage) for more details.

### Big datasets, multi-GPU and multi-node jobs

Please see our tutorial for [GPU-accelerated machine learning](../support/tutorials/gpu-ml.md), which covers more advanced topics, including how to work with big data sets, multi-GPU and multi-node jobs.


## More information

- CSC's guide for [GPU-accelerated machine learning](../support/tutorials/gpu-ml.md)
- [PyTorch documentation](https://pytorch.org/docs/stable/index.html)
- [Horovod with PyTorch example](https://github.com/horovod/horovod/blob/master/docs/pytorch.rst)
