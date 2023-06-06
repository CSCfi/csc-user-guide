---
title: PyTorch
tags:
  - Free
---

# PyTorch

Machine learning framework for Python.

!!! info "News" 
    **23.5.2023** Modules `pytorch/2.0` and `pytorch/1.13` have been
    updated so that [Python virtual
    environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
    should now work with them. To create a virtual environment use the
    command `python3 -m venv --system-site-packages venv`.
    
    **5.10.2022** Due to Puhti's update to Red Hat Enterprise Linux 8
    (RHEL8), **the number of fully supported PyTorch versions has been
    reduced. Previously deprecated conda-based versions have been
    removed.** Please [contact our servicedesk](../support/contact.md) if
    you really need access to older versions.

    **5.5.2022** Due to Mahti's update to Red Hat Enterprise Linux 8 (RHEL8),
    the number of fully supported PyTorch versions has been reduced. Please [contact our
    servicedesk](../support/contact.md) if you really need access to other versions.

    **4.2.2022** All old PyTorch versions which were based on direct Conda
    installations have been deprecated, and we encourage users to move to newer
    versions. Read more on our separate [Conda deprecation page](../support/tutorials/conda.md).


## Available

Currently supported PyTorch versions:

| Version | Module         | Puhti | Mahti | LUMI | Notes           |
|:--------|----------------|:-----:|:-----:|------|:----------------|
| 2.0.0   | `pytorch/2.0`  | X     | X     | X*   | default version |
| 1.13.1  | `pytorch/1.13` | -     | -     | X*   |                 |
| 1.13.0  | `pytorch/1.13` | X     | X     | -    |                 |
| 1.12.0  | `pytorch/1.12` | X     | X     | -    |                 |
| 1.11.0  | `pytorch/1.11` | X     | X     | -    |                 |
| 1.10.0  | `pytorch/1.10` | (x)   | (x)   | -    |                 |
| 1.9.0   | `pytorch/1.9`  | (x)   | (x)   | -    |                 |
| 1.8.1   | `pytorch/1.8`  | (x)   | (x)   | -    |                 |
| 1.7.1   | `pytorch/1.7`  | (x)   | -     | -    |                 |

All modules include [PyTorch](https://pytorch.org/) and related libraries with
GPU support via CUDA/ROCm.

Versions marked with "(x)" are based on old Red Hat Enterprise Linux 7
(RHEL7) images, and are no longer fully supported. In particular MPI
and Horovod are not expected to work anymore with these modules. If
you still wish to access these versions, you need to enable old RHEL7
modules by `module use /appl/soft/ai/rhel7/modulefiles/`.

**Versions in LUMI, marked as "X*" are still experimental with limited
support.** They are still subject to change at any time without notice,
and for example multi-node jobs are know not to work properly yet.

If you find that some package is missing, you can often install it yourself with
`pip install --user`. See [our Python
documentation](python.md#installing-python-packages-to-existing-modules) for
more information on how to install packages yourself. If you think that some
important PyTorch-related package should be included in the module provided by
CSC, please [contact our servicedesk](../support/contact.md).

All modules are based on containers using Apptainer (previously known
as Singularity). Wrapper scripts have been provided so that common
commands such as `python`, `python3`, `pip` and `pip3` should work as
normal. For other commands, you need to prefix them with
`apptainer_wrapper exec`, for example `apptainer_wrapper exec
huggingface-cli`. For more information, see [CSC's general
instructions on how to run Apptainer
containers](../computing/containers/run-existing.md).


!!! info "New users"

    If you are new to using machine learning on CSC's supercomputers,
    please read our new tutorial [Getting started with machine learning
    at CSC](../support/tutorials/ml-starting.md), which covers how to run
    a simple PyTorch project on Puhti using the web user interface.


## License

PyTorch is BSD-style licensed, as found in the [LICENSE
file](https://github.com/pytorch/pytorch/blob/master/LICENSE).

## Usage

To use the default version of PyTorch on Puhti or Mahti, initialize it
with:

```text
module load pytorch
```

To access PyTorch on LUMI:

```text
module use /appl/local/csc/modulefiles/
module load pytorch
```

Note that LUMI versions are still considered experimental with limited
support. They are still subject to change at any time without notice,
and for example multi-node jobs are know not to work properly yet.


If you wish to have a specific version ([see above for available
versions](#available)), use:

```text
module load pytorch/1.13
```

Please note that the module already includes CUDA and cuDNN libraries,
so **there is no need to load cuda and cudnn modules separately!**

This command will also show all available versions:

```text
module avail pytorch
```

To check the exact packages and versions included in the loaded module you can
run:

```text
list-packages
```


!!! warning 

    Note that login nodes are not intended for heavy computing, please use slurm
    batch jobs instead. See our [instructions on how to use the batch job
    system](../computing/running/getting-started.md).

### Example batch script

Example batch script for reserving one GPU and a corresponding
proportion of the available CPU cores in a single node:

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=64G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:1
        
    module load pytorch/1.13
    srun python3 myprog.py <options>
    ```

=== "Mahti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:1
    
    module load pytorch/1.13
    srun python3 myprog.py <options>
    ```

=== "LUMI"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=8
    #SBATCH --gpus-per-node=1
    #SBATCH --mem=64G
    #SBATCH --time=1:00:00
    
    export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

    module use /appl/local/csc/modulefiles/
    module load pytorch/1.13
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

For multi-GPU and multi-node jobs we recommend using the PyTorch
Distributed Data-Parallel framework. You can read more about this and
find examples of how to use PyTorch DDP on CSC's supercomputers in the
[Multi-GPU and multi-node section of our Machine learning
guide](../support/tutorials/ml-multi.md)


## More information

- [CSC's Machine learning guide](../support/tutorials/ml-guide.md)
- [PyTorch documentation](https://pytorch.org/docs/stable/index.html)
