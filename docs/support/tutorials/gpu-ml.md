# GPU-accelerated machine learning

## What CSC service to use?

If you need GPU-accelerated machine learning, CSC's supercomputer Puhti is usually the way to go.  First, please read the [instructions on how to access Puhti](../../computing/overview.md), and [how to submit computing jobs to Puhti's queuing system](../../computing/running/getting-started.md).

In some special cases, a virtual server on [**Pouta**](../../cloud/pouta/index.md) might make sense as it also offers GPUs.  This gives you more control over the computing environment, but may not be suitable for very heavy computing tasks.  For model deployment, the [**Rahti**](../../cloud/rahti/index.md) contained cloud service might be used, however, it currently doesn't offer GPU support. See some examples of [how to deploy machine learning models on Rahti](https://github.com/CSCfi/rahti-ml-examples).

## Using Puhti

For GPU-accelerated machine learning on Puhti, we support [TensorFlow](../../apps/tensorflow.md), [PyTorch](../../apps/pytorch.md), [MXNET](../../apps/mxnet.md), and [RAPIDS](../../apps/rapids.md).  Please read the detailed instructions for the specific application that you are interested in.  In brief, you need to use the [module system](../../computing/modules.md) to load the application you want, for example:

```bash
module load tensorflow/2.0.0
```

To submit a job to the slurm queue using GPUs, you need to use the `gpu` partition and also specify the type and number of GPUs using the `--gres` flag. An example batch script for reserving one GPU and 10 CPUs in a single node:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1

srun python3 myprog.py <options>
```

### Data storage

It is recommended to store big datasets in [Allas](../../data/Allas/index.md), and download them to your project's [scratch directory](../../computing/disk.md) prior to starting your computation.  Example:

```bash
module load allas
allas-conf
cd /scratch/<your-project>
swift download <bucket-name> your-dataset.tar
```

Many machine learning tasks, such as training a model, require reading a huge number of relatively small files from the drive.  Unfortunately the Lustre-shared file system (e.g. `/scratch`, `/projappl` and users' home directories) does not perform very well when opening a lot of files, and it also causes noticable slowdowns for all users of Puhti.  Instead, consider taking into use the [NVME fast local storage](../../computing/running/creating-job-scripts.md#local-storage) on the GPU nodes.

!!! note

    Please **do not read a huge number of small from the shared file system**, use the fast local NVME drive instead!


In brief, you just need to add `nvme:<number-of-GB>` to the `--gres` flag in your submission script, and then the fast local storage will be available in the location specified by the environment variable `$LOCAL_SCRATCH`.  Here is an example run that reserves 100 GB of the fast local drive and extracts the dataset tar-package on that drive before launching the computation:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1,nvme:100

tar xf /scratch/<your-project>/your-dataset.tar -C $LOCAL_SCRATCH

srun python3 myprog.py --input_data=$LOCAL_SCRATCH <options>
```

Note that you need to communicate somehow to your own program where to find the dataset, for example with a command line argument.  Also see our [general instructions on how to take the fast local storage into use](../../computing/running/creating-job-scripts.md#local-storage).

### Multi-GPU and multi-node jobs

Multi-GPU jobs are also supported by specifying the number of GPUs required in the `--gres` flag, for example to have 4 GPUs (which is the maximum for a single node in Puhti): `--gres=gpu:v100:4`.  Please also make sure that your code can take advantage of multiple GPUs, this typically requires some changes to the program.

For large jobs requiring more than 4 GPUs we recommend using [Horovod](https://github.com/horovod/horovod), which is supported for TensorFlow and PyTorch on Puhti.  Horovod uses MPI and NCCL for interprocess communication. See also [MPI based batch jobs](../../computing/running/creating-job-scripts.md#mpi-based-batch-jobs).  Modules that support Horovod have the `-hvd` suffix in their name.  Note that Horovod is supported only for some specific versions of TensorFlow and PyTorch.  You can run `module avail hvd` to see all Horovod-enabled modules.  To take Horovod into use, just load the appropriate module, e.g:

```bash
module load tensorflow/2.0.0-hvd
```

Below is an example slurm batch script that uses 8 GPUs across two computers.  In MPI terminology we have 8 tasks on 2 nodes, each task has one GPU and 10 CPUs.

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=10
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:4
#SBATCH --time=1:00:00
#SBATCH --mem=32G
#SBATCH --account=<project>

# uncomment the following line if you want to see some debug info from NCCL
# export NCCL_DEBUG=INFO

srun python3 myprog.py <options>
```

### Singularity

We also provide GPU-enabled applications via Singularity containers.  For example very recent NVIDIA-optimized version of TensorFlow and PyTorch are available.  See our [general instructions for using Singularity on Puhti](../../computing/containers/run-existing.md).

A specific image can be activated via the module system:


```bash
module use /appl/soft/ai/singularity/modulefiles/
module avail nvidia  # to see existing images
module load nvidia-pytorch/19.11-py3  # to activate a specific image
```

Here is an example submission script.  Note that the `singularity_wrapper` command is essential, otherwise the program will not run inside the image.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1

srun singularity_wrapper exec python3 myprog <options>
```
