# TensorFlow

Deep learning framework for Python.

## Available

Available on Puhti only.  Currently supported TensorFlow versions and corresponding modules to load:

- 2.3.0 using [Singularity](../support/tutorials/gpu-ml.md#singularity): `tensorflow/2.3-sng`
- 2.2.0 with *preliminary* [Horovod](../support/tutorials/gpu-ml.md#multi-gpu-and-multi-node-jobs) support using [Singularity](../support/tutorials/gpu-ml.md#singularity): `tensorflow/nvidia-20.07-tf2-py3`
- 2.2.0 with [Horovod](../support/tutorials/gpu-ml.md#multi-gpu-and-multi-node-jobs) support: `tensorflow/2.2-hvd`
- 2.2.0 using [Singularity](../support/tutorials/gpu-ml.md#singularity): `tensorflow/2.2-sng`
- 2.1.0 using [Singularity](../support/tutorials/gpu-ml.md#singularity): `tensorflow/nvidia-20.03-tf2-py3`
- 2.1.0 using [Singularity](../support/tutorials/gpu-ml.md#singularity): `tensorflow/nvidia-20.02-tf2-py3`
- 2.0.0 using [Singularity](../support/tutorials/gpu-ml.md#singularity): `tensorflow/nvidia-19.11-tf2-py3`
- 2.0.0: `tensorflow/2.0.0`
- 2.0.0 with [Horovod](../support/tutorials/gpu-ml.md#multi-gpu-and-multi-node-jobs) support: `tensorflow/2.0.0-hvd`
- 1.15.0 with [Horovod](../support/tutorials/gpu-ml.md#multi-gpu-and-multi-node-jobs) support: `tensorflow/1.15-hvd`
- 1.14.0: `tensorflow/1.14.0`
- 1.14.0 optimized for CPU usage, no GPU support: `tensorflow/1.14.0-cpu`
- 1.13.1: `tensorflow/1.13.1`
- 1.13.1 with [Horovod](../support/tutorials/gpu-ml.md#multi-gpu-and-multi-node-jobs) support: `tensorflow/1.13.1-hvd`

Includes [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/) with GPU support via CUDA.

Modules starting with `nvidia` are based on NVIDIA's optimized
container images from
[NGC](https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow) with
some CSC specific additions. See [NVIDIA's TensorFlow container
release
notes](https://docs.nvidia.com/deeplearning/frameworks/tensorflow-release-notes/index.html)
for more information on provided software versions.


!!! note 

    In Singularity-based modules you need to launch Python with `singularity_wrapper`, see [here for a usage example](../support/tutorials/gpu-ml.md#singularity).

If you find that some package is missing, you can often install it yourself with `pip install --user`, or `singularity_wrapper exec pip install --user` in Singularity-based modules. If you think that some important TensorFlow-related package should be included in a module provided by CSC, you can send an email to <servicedesk@csc.fi>.

## License

TensorFlow is licensed under [Apache License 2.0](https://github.com/tensorflow/tensorflow/blob/master/LICENSE).

## Usage

To use this software on Puhti, initialize it with:

```text
module load tensorflow
```

to access the default version, or if you wish to have a specific version (see [above for available versions](#available)):

```text
module load tensorflow/2.0.0
```

Please note that the module already includes CUDA and cuDNN libraries, so **there is no need to load cuda and cudnn modules separately!**

This command will also show all available versions:

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

For Singularity-based modules the last two lines would instead look like:

```
module load tensorflow/nvidia-20.02-tf2-py3
srun singularity_wrapper exec python3 myprog.py <options>
```

!!! note

    Please **do not read a huge number of files from the shared file system**, use fast local disk or package your data into larger files instead!  See the [GPU-accelerated machine learning guide](../support/tutorials/gpu-ml.md#data-storage) for more details.

### Big datasets, multi-GPU and multi-node jobs

Please see our tutorial for [GPU-accelerated machine learning](../support/tutorials/gpu-ml.md), which covers more advanced topics, including how to work with big data sets, multi-GPU and multi-node jobs.


## More information

- CSC's guide for [GPU-accelerated machine learning](../support/tutorials/gpu-ml.md)
- [TensorFlow overview](https://www.tensorflow.org/overview/)
- [Get Started with TensorFlow](https://www.tensorflow.org/tutorials)
- [TensorFlow API documentation](https://www.tensorflow.org/api_docs/python/tf)
- [Keras documentation](https://keras.io/)
