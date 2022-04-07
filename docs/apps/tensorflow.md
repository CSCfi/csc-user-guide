# TensorFlow

Deep learning framework for Python.

!!! News

    **4.2.2022** All old TensorFlow versions which were based on direct Conda
    installations have been deprecated, and we encourage users to move to newer
    versions. Read more on our separate [Conda deprecation page](../support/deprecate-conda.md).


## Available

Currently supported TensorFlow versions:

| Version | Module                            | Puhti | Mahti-rhel7 | Environ. | Horovod | Notes                           |
|:-------:|-----------------------------------|:-----:|:-----:|----------|:-------:|---------------------------------|
| 2.8.0   | `tensorflow/2.8`                  | X     | X     | Sing.    | X       | default version                 |
| 2.7.0   | `tensorflow/2.7`                  | X     | X     | Sing.    | X       |                                 |
| 2.6.0   | `tensorflow/2.6`                  | X     | X     | Sing.    | X       |                                 |
| 2.5.0   | `tensorflow/2.5`                  | X     | X     | Sing.    | X       |                                 |
| 2.4.1   | `tensorflow/2.4`                  | X     | X     | Sing.    | X       |                                 |
| 2.4.0   | `tensorflow/2.4-hvd`              | X     | -     | Conda    | X       | *deprecated*                    |
| 2.4.0   | `tensorflow/2.4-sng`              | X     | -     | Sing.    | -       |                                 |
| 2.3.1   | `tensorflow/nvidia-20.12-tf2-py3` | X     | -     | Sing.    | -       |                                 |
| 2.3.0   | `tensorflow/2.3`                  | X     | -     | Sing.    | -       |                                 |
| 2.2.0   | `tensorflow/nvidia-20.07-tf2-py3` | X     | -     | Conda    | X       | experimental Horovod support    |
| 2.2.0   | `tensorflow/2.2-hvd`              | X     | -     | Conda    | X       | *deprecated*                    |
| 2.2.0   | `tensorflow/2.2`                  | X     | -     | Sing.    | -       |                                 |
| 2.1.0   | `tensorflow/nvidia-20.03-tf2-py3` | X     | -     | Sing.    | -       |                                 |
| 2.1.0   | `tensorflow/nvidia-20.02-tf2-py3` | X     | -     | Sing.    | -       |                                 |
| 2.0.0   | `tensorflow/nvidia-19.11-tf2-py3` | X     | -     | Sing.    | -       |                                 |
| 2.0.0:  | `tensorflow/2.0.0`                | X     | -     | Conda    | -       | *deprecated*                    |
| 2.0.0   | `tensorflow/2.0.0-hvd`            | X     | -     | Conda    | X       | *deprecated*                    |
| 1.15.5  | `tensorflow/1.15`                 | X     | -     | Sing.    | X       |                                 |
| 1.15.0  | `tensorflow/1.15-hvd`             | X     | -     | Conda    | X       | *deprecated*                    |
| 1.14.0: | `tensorflow/1.14.0`               | X     | -     | Conda    | -       | *deprecated*                    |
| 1.14.0  | `tensorflow/1.14.0-cpu`           | X     | -     | Conda    | -       | *deprecated*,<br/> optimized for CPU |
| 1.13.1: | `tensorflow/1.13.1`               | X     | -     | Conda    | -       | *deprecated*                    |
| 1.13.1  | `tensorflow/1.13.1-hvd`           | X     | -     | Conda    | X       | *deprecated*                    |

Includes [TensorFlow](https://www.tensorflow.org/) and
[Keras](https://keras.io/) with GPU support via CUDA.

Modules starting with `nvidia` are based on NVIDIA's optimized container images
from [NGC](https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow) with
some CSC specific additions. See [NVIDIA's TensorFlow container release
notes](https://docs.nvidia.com/deeplearning/frameworks/tensorflow-release-notes/index.html)
for more information on provided software versions.

If you find that some package is missing, you can often install it yourself with
`pip install --user`. If you think that some important TensorFlow-related
package should be included in a module provided by CSC, you can send an email to
[servicedesk@csc.fi](mailto:servicedesk@csc.fi).

Some modules are Singularity-based (indicated in the "Environ." column in the
table above). Wrapper scripts have been provided so that common commands such as
`python`, `python3`, `pip` and `pip3` should work as normal. For more
information, see [CSC's general instructions on how to run Singularity
containers](../computing/containers/run-existing.md).

Some modules support [Horovod](https://horovod.ai/), which is our recommended
framework for multi-node jobs, i.e., jobs needing more than 4
GPUs. Horovod can also be used with single-node jobs for 2-4 GPUs. For more
information, read the [Multi-GPU section in our machine learning
guide](../support/tutorials/ml-multi.md).


## License

TensorFlow is licensed under [Apache License
2.0](https://github.com/tensorflow/tensorflow/blob/master/LICENSE).

## Usage

To use this software on Puhti or Mahti-rhel7, initialize it with:

```text
module load tensorflow
```

to access the default version, or if you wish to have a specific version ([see
above for available versions](#available)):

```text
module load tensorflow/2.4
```

Please note that the module already includes CUDA and cuDNN libraries, so
**there is no need to load cuda and cudnn modules separately!**

This command will also show all available versions:

```text
module avail tensorflow
```

To check the exact packages and versions included in the loaded module you can
run:

```text
list-packages
```

!!! note 

    Note that Puhti login nodes are not intended for heavy computing, please use
    slurm batch jobs instead. See our [instructions on how to use the batch job
    system](../computing/running/getting-started.md).

### Example batch script

Example batch script for reserving one GPU and 1/4 of the available CPU cores in
a single node:

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=64G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:1
    
    module load tensorflow/2.8
    srun python3 myprog.py <options>
    ```
    
=== "Mahti-rhel7"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:1
    
    module load tensorflow/2.8
    srun python3 myprog.py <options>
    ```


!!! note

    Please **do not read a huge number of files from the shared file system**, use
    fast local disk or package your data into larger files instead! See the [Data
    storage section in our machine learning
    guide](../support/tutorials/ml-data.md) for more details.

### Big datasets, multi-GPU and multi-node jobs

Please see our [Machine learning guide](../support/tutorials/ml-guide.md), which
covers more advanced topics, including [efficient GPU
utilization](../support/tutorials/gpu-ml.md), [how to work with big data
sets](../support/tutorials/ml-data.md), [multi-GPU and multi-node
jobs](../support/tutorials/ml-multi.md).


## More information

- [CSC's Machine learning guide](../support/tutorials/ml-guide.md)
- [TensorFlow overview](https://www.tensorflow.org/overview/)
- [Get Started with TensorFlow](https://www.tensorflow.org/tutorials)
- [TensorFlow API documentation](https://www.tensorflow.org/api_docs/python/tf)
- [Keras documentation](https://keras.io/)
