# PyTorch

Machine learning framework for Python.

!!! News

    **5.5.2022** Due to Mahti's update to Red Hat Enterprise Linux 8 (RHEL8),
    the number of fully supported PyTorch versions has been reduced. Please [contact our
    servicedesk](../support/contact.md) if you really need access to other versions.

    **4.2.2022** All old PyTorch versions which were based on direct Conda
    installations have been deprecated, and we encourage users to move to newer
    versions. Read more on our separate [Conda deprecation page](../support/deprecate-conda.md).


## Available

Currently supported PyTorch versions:

| Version | Module              | Puhti | Mahti | Environ. | Horovod | Notes           |
|:-------:|---------------------|:-----:|:-----:|----------|:-------:|-----------------|
| 1.11.0  | `pytorch/1.11`      | X     | X     | Sing.    | X       | default version |
| 1.10.0  | `pytorch/1.10`      | X     | (X)   | Sing.    | X       |                 |
| 1.9.0   | `pytorch/1.9`       | X     | (X)   | Sing.    | X       |                 |
| 1.8.1   | `pytorch/1.8`       | X     | (X)   | Sing.    | X       |                 |
| 1.7.1   | `pytorch/1.7`       | X     | -     | Sing.    | X       |                 |
| 1.6.0   | `pytorch/1.6`       | X     | -     | Conda    | -       | *deprecated*    |
| 1.4.0   | `pytorch/1.4`       | X     | -     | Conda    | -       | *deprecated*    |
| 1.3.1   | `pytorch/1.3.1`     | X     | -     | Conda    | -       | *deprecated*    |
| 1.3.1   | `pytorch/1.3.1-hvd` | X     | -     | Conda    | X       | *deprecated*    |
| 1.3.0   | `pytorch/1.3.0`     | X     | -     | Conda    | -       | *deprecated*    |
| 1.2.0   | `pytorch/1.2.0`     | X     | -     | Conda    | -       | *deprecated*    |
| 1.1.0   | `pytorch/1.1.0`     | X     | -     | Conda    | -       | *deprecated*    |
| 1.0.1   | `pytorch/1.0.1`     | X     | -     | Conda    | -       | *deprecated*    |
| 0.4.1   | `pytorch/0.4.1`     | X     | -     | Conda    | -       | *deprecated*    |

Versions marked with "(X)" on Mahti are based on old Red Hat Enterprise Linux 7
(RHEL7) images, and are no longer fully supported. In particular MPI and Horovod
do not work anymore on Mahti with these modules. If you still wish to access
these versions, you need to enable old RHEL7 modules by `module use
/appl/soft/ai/rhel7/modulefiles/`.

All modules include [PyTorch](https://pytorch.org/) and related libraries with
GPU support via CUDA.

If you find that some package is missing, you can often install it yourself with
`pip install --user`. See [our Python
documentation](python.md#installing-python-packages-to-existing-modules) for
more information on how to install packages yourself. If you think that some
important PyTorch-related package should be included in the module provided by
CSC, please [contact our servicedesk](../support/contact.md).

Some modules are Singularity-based (indicated in the "Environ." column in the
table above). Wrapper scripts have been provided so that common commands such as
`python`, `python3`, `pip` and `pip3` should work as normal. For more
information, see [CSC's general instructions on how to run Singularity
containers](../computing/containers/run-existing.md).

Some modules support [Horovod](https://horovod.ai/), which is our recommended
framework for multi-node jobs, i.e., jobs needing more than 4 GPUs. For more
information, read the [Multi-GPU section in our machine learning
guide](../support/tutorials/ml-multi.md).


### NVIDIA's containers

For convenience, we also offer modules based on NVIDIA's optimized container
images from [NGC](https://ngc.nvidia.com/catalog/containers/nvidia:pytorch) with
some CSC specific additions. For these, the included PyTorch versions are
typically not the release versions, but the newest git commit at the time of
creation. See [NVIDIA's PyTorch container release
notes](https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/index.html)
for more information on provided software versions. Currently, these are
available on **Puhti only**.

- 1.8.0a0 using Singularity: `pytorch/nvidia-20.11-py3`
- 1.7.0a0 with *experimental* [Horovod](../support/tutorials/ml-multi.md) support using Singularity: `pytorch/nvidia-20.08-py3`
- 1.6.0a0 using Singularity: `pytorch/nvidia-20.07-py3`
- 1.5.0a0 using Singularity: `pytorch/nvidia-20.03-py3`
- 1.5.0a0 using Singularity: `pytorch/nvidia-20.02-py3`
- 1.4.0a0 using Singularity: `pytorch/nvidia-19.11-py3`


## License

PyTorch is BSD-style licensed, as found in the [LICENSE
file](https://github.com/pytorch/pytorch/blob/master/LICENSE).

## Usage

To use this software on Puhti or Mahti, initialize it with:

```text
module load pytorch
```

to access the default version, or if you wish to have a specific version ([see
above for available versions](#available)):

```text
module load pytorch/1.11
```

Please note that the module already includes CUDA and cuDNN libraries, so
**there is no need to load cuda and cudnn modules separately!**

This command will also show all available versions:

```text
module avail pytorch
```

To check the exact packages and versions included in the loaded module you can
run:

```text
list-packages
```


!!! note 

    Note that login nodes are not intended for heavy computing, please use slurm
    batch jobs instead. See our [instructions on how to use the batch job
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
        
    module load pytorch/1.11
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
    
    module load pytorch/1.11
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
- [PyTorch documentation](https://pytorch.org/docs/stable/index.html)
- [Horovod with PyTorch example](https://github.com/horovod/horovod/blob/master/docs/pytorch.rst)
