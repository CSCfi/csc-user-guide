# TensorFlow

Deep learning framework for Python.

## Available

The `tensorflow` module is available on Puhti only.  Currently supported TensorFlow versions:

- 2.0.0
- 2.0.0-hvd (with [Horovod](https://github.com/horovod/horovod) support)
- 1.14.0
- 1.14.0-cpu (optimized for CPU usage, no GPU support)
- 1.13.1
- 1.13.1-hvd (with [Horovod](https://github.com/horovod/horovod) support)

Includes [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/) with GPU support via CUDA.  Also includes all the packages from [Python Data](python-data.md).

If you find that some package is missing, you can often install it yourself with `pip install --user`.

If you think that some important TensorFlow-related package should be included in a module provided by CSC, you can send an email to <servicedesk@csc.fi>.

Alternatively you can also run TensorFlow via [Singularity images](/computing/containers/run-existing/), [see below for a usage example](#singularity).

## License

TensorFlow is licensed under [Apache License 2.0](https://github.com/tensorflow/tensorflow/blob/master/LICENSE).

## Usage

To use this software on Puhti, initialize it with:

```text
module load tensorflow
```

to access the default version.

This will show all available versions:

```text
module avail tensorflow
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

module load tensorflow/1.14.0
srun python3 myprog.py <options>
```

### Local storage

The GPU nodes in Puhti have fast local storage which is useful for IO-intensive applications.  See our [general instructions on how to take the fast local storage into use](../computing/running/creating-job-scripts.md#local-storage).  For example to use 100 GB of local storage, just change the `gres` line in the above batch script example to:

```bash
#SBATCH --gres=gpu:v100:1,nvme:100
```

### Horovod

[Horovod](https://github.com/horovod/horovod) is a supported method for running multi-GPU and multi-node jobs with TensorFlow. Horovod uses MPI and NCCL for interprocess communication. See also [MPI based batch jobs](../computing/running/creating-job-scripts.md#mpi-based-batch-jobs).

Modules that support Horovod have the `-hvd` postfix in their name.  Note that we might not support Horovod for all TensorFlow versions. (To see all modules try `module avail tensorflow`).  To take TensorFlow with Horovod support into use, you can run for example:

```text
module load tensorflow/1.13.1-hvd
```

Below is an example slurm batch script that uses 8 tasks across two nodes.  Each task has one GPU and 10 CPUs.

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

module load tensorflow/1.13.1-hvd

export NCCL_DEBUG=INFO

srun python3 myprog.py <options>
```

### Singularity

TensorFlow can also be run via Singularity, either using pre-installed images on Puhti, or by converting a Docker image yourself.  See our [general instructions for using Singularity on Puhti](/computing/containers/run-existing/).

A specific image can be activated via the module system:


```bash
module use /appl/soft/ai/singularity/modulefiles/
module avail nvidia-tensorflow  # to see existing images
module load nvidia-tensorflow/19.11-tf2-py3  # to activate a specific image
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


## More information

- [TensorFlow overview](https://www.tensorflow.org/overview/)
- [Get Started with TensorFlow](https://www.tensorflow.org/tutorials)
- [TensorFlow API documentation](https://www.tensorflow.org/api_docs/python/tf)
- [Keras documentation](https://keras.io/)
