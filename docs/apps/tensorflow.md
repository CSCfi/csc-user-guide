---
tags:
  - Free
catalog:
  name: TensorFlow
  description: Deep learning library for Python
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  available_on:
    - LUMI
    - Puhti
    - Mahti
    - Roihu
---

# TensorFlow

Deep learning framework for Python.

!!! info "News"

    **16.6.2026** TensorFlow is now available on Roihu-GPU, the module has been 
    renamed `python-tensorflow`.

**5.10.2022** Due to Puhti's update to Red Hat Enterprise Linux 8
    (RHEL8), **the number of fully supported TensorFlow versions has been
    reduced. Previously deprecated conda-based versions have been
    removed.** Please [contact our servicedesk](../support/contact.md) if
    you really need access to older versions.

    **5.5.2022** Due to Mahti's update to Red Hat Enterprise Linux 8 (RHEL8),
    the number of fully supported TensorFlow versions has been reduced. Please [contact our
    servicedesk](../support/contact.md) if you really need access to other versions.

    **4.2.2022** All old TensorFlow versions which were based on direct Conda
    installations have been deprecated, and we encourage users to move to newer
    versions. Read more on our separate [Conda deprecation page](../support/tutorials/conda.md).


## Available

Currently supported TensorFlow versions:

| Version | Module                   | Roihu-GPU | Puhti | Mahti | LUMI | Notes                   |
|:--------|:-------------------------|-----------|:-----:|:-----:|:----:|-------------------------|
| 2.21.0  | `python-tensorflow/2.21` | X         | -     | -     | -    | Default on Roihu-GPU    |
| 2.18.0  | `tensorflow/2.18`        |           | X     | X     | -    | Default on Puhti, Mahti |
| 2.17.0  | `tensorflow/2.17`        |           | X     | X     | -    |                         |
| 2.16.1  | `tensorflow/2.16`        |           | -     | -     | X    | Default on LUMI         |
| 2.15.0  | `tensorflow/2.15`        |           | X     | X     | -    |                         |
| 2.14.0  | `tensorflow/2.14`        |           | X     | X     | -    |                         |
| 2.13.0  | `tensorflow/2.13`        |           | X     | X     | -    |                         |
| 2.12.0  | `tensorflow/2.12`        |           | X     | X     | X    |                         |
| 2.11.0  | `tensorflow/2.11`        |           | X     | X     | X    |                         |
| 2.10.0  | `tensorflow/2.10`        |           | X     | X     | X    |                         |
| 2.9.0   | `tensorflow/2.9`         |           | X     | X     | X    |                         |
| 2.8.0   | `tensorflow/2.8`         |           | X     | X     | X    |                         |

Includes [TensorFlow](https://www.tensorflow.org/) and
[Keras](https://keras.io/) with GPU support via CUDA/ROCm.

If you find that some package is missing, you can often install it
yourself using `pip install`. It is recommended to use Python virtual
environments. See [our Python documentation for more information on
how to install packages
yourself](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).
If you think that some important package should be included in the
module provided by CSC, please [contact our
servicedesk](../support/contact.md).

All modules are based on containers using Apptainer (previously known
as Singularity). Wrapper scripts have been provided so that common
commands such as `python`, `python3`, `pip` and `pip3` should work as
normal. For other commands, you need to prefix them with
`apptainer_wrapper exec`, for example `apptainer_wrapper exec
huggingface-cli`. For more information, see [CSC's general
instructions on how to run Apptainer
containers](../computing/containers/overview.md#running-containers).

Some modules support [Horovod](https://horovod.ai/), which is our
recommended framework for multi-node jobs, i.e., jobs needing more
than 4 GPUs on Puhti and Mahti. Horovod can also be used with
single-node jobs for 2-4 GPUs. For more information, read the
[Multi-GPU section in our machine learning
guide](../support/tutorials/ml-multi.md).


## License

TensorFlow is licensed under [Apache License
2.0](https://github.com/tensorflow/tensorflow/blob/master/LICENSE).

## Usage

To use the default version of TensorFlow on Roihu-GPU, initialize it with:

```text
module load python-tensorflow
```

To access PyTorch on Puhti or Mahti:

```text
module load tensorflow
```

To access TensorFlow on LUMI:

```text
module use /appl/local/csc/modulefiles/
module load tensorflow
```

If you wish to have a specific version ([see above for available
versions](#available)), use:

```text
module load python-tensorflow/2.21  # on Roihu-GPU
module load tensorflow/2.12         # on other systems
```

Please note that the modules already include CUDA/ROCm libraries, so
**there is no need to load cuda or rocm modules separately!**

This command will also show all available versions:

```text
module avail python-tensorflow  # on Roihu-GPU
module avail tensorflow         # on other systems
```

To check the exact packages and versions included in the loaded module you can
run:

```text
pip list
```

!!! warning 

    Note that login nodes are not intended for heavy computing, please use
    slurm batch jobs instead. See our [instructions on how to use the batch job
    system](../computing/running/getting-started.md).

### Example batch script

Example batch script for reserving one GPU and 1/4 (1/8 on LUMI) of
the available CPU cores in a single node:


=== "Roihu-GPU"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=72
    #SBATCH --mem=120G
    #SBATCH --gres=gpu:gh200:1
    #SBATCH --time=1:00:00
    
    module load python-tensorflow/2.21
    srun python3 myprog.py <options>
    ```

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
    
    module load tensorflow/2.14
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
    #SBATCH --gres=gpu:a100:1
    
    module load tensorflow/2.14
    srun python3 myprog.py <options>
    ```

=== "LUMI"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=1
    #SBATCH --mem=60G
    #SBATCH --time=1:00:00
    
    module use /appl/local/csc/modulefiles/
    module load tensorflow/2.12
    srun python3 myprog.py <options>
    ```

Please read the section on [Efficient GPU utilization in our Machine
learning guide](../support/tutorials/gpu-ml.md) to learn how to use
the GPU efficiently.


### Big datasets, multi-GPU and multi-node jobs

If you are working with big datasets, or datasets that contain a lot
of files, please read [the data section of our Machine learning
guide](../support/tutorials/ml-data.md). In particular, please **do
not read a huge number of files from the shared file system**, use
fast local disk or package your data into larger files instead!

For multi-GPU and multi-node please read the [Multi-GPU and multi-node
section of our Machine learning
guide](../support/tutorials/ml-multi.md)


## More information

- [CSC's Machine learning guide](../support/tutorials/ml-guide.md)
- [TensorFlow overview](https://www.tensorflow.org/overview/)
- [Get Started with TensorFlow](https://www.tensorflow.org/tutorials)
- [TensorFlow API documentation](https://www.tensorflow.org/api_docs/python/tf)
- [Keras documentation](https://keras.io/)
