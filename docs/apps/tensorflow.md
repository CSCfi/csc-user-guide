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

Alternatively you can also run TensorFlow via [Singularity images](/computing/containers/run-existing/), see [here for a usage example](../support/tutorials/gpu-ml.md#singularity).

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

!!! note

    Please **do not read a huge number of files from the shared file system**, use fast local disk or package your data into larger files instead!  See the [GPU-accelerated machine learning guide](../support/tutorials/gpu-ml.md#data-storage) for more details.

### Big datasets, multi-GPU and multi-node jobs

Please see our tutorial for [GPU-accelerated machine learning](../support/tutorials/gpu-ml.md), which covers how to work with big data sets, multi-GPU and multi-node jobs among other things.


## More information

- CSC's guide for [GPU-accelerated machine learning](../support/tutorials/gpu-ml.md)
- [TensorFlow overview](https://www.tensorflow.org/overview/)
- [Get Started with TensorFlow](https://www.tensorflow.org/tutorials)
- [TensorFlow API documentation](https://www.tensorflow.org/api_docs/python/tf)
- [Keras documentation](https://keras.io/)
