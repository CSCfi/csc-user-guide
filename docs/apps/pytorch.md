---
title: PyTorch
tags:
  - Free
---

# PyTorch

Machine learning framework for Python.

!!! info "News" 

    **19.9.2024** PyTorch 2.4.1 with ROCm 6.1 added to LUMI. The LUMI
    PyTorch module now includes [vLLM version
    0.5.5](https://docs.vllm.ai/en/latest/) in addition to
    FlashAttention-2, bitsandbytes and many other frequently requested
    packages already added included in earlier installations. The LUMI
    module still uses old-style wrappers (not the tykky-based wrappers
    as in Puhti and Mahti).

    **21.8.2024** PyTorch 2.4 added to Puhti and Mahti. The LUMI
    installation will be delayed until after the current service
    break. The torchtext package is no longer included as it has been
    deprecated and no longer works with PyTorch 2.4.

    **13.6.2024** PyTorch 2.3 added to Puhti and Mahti. The LUMI
    installation will be delayed until early autumn due to an incompatible
    ROCm driver version. This version has also updated how Python commands
    are wrapped, as this solves several problems with using virtual
    environments and Jupyter Notebooks. Due to this `apptainer` and
    `apptainer_wrapper` commands will no longer work, but otherwise the
    change should be invisible to users.

    **1.3.2024** PyTorch 2.2 added to Puhti, Mahti and LUMI. The LUMI
    module includes ROCm versions of 
    [FlashAttention-2](https://github.com/ROCm/flash-attention) 
    and [bitsandbytes](https://github.com/ROCm/bitsandbytes) as these are
    difficult for users to add themselves. 
    [xFormers](https://github.com/facebookresearch/xformers) has been added 
    to all three systems.

    **17.11.2023** PyTorch 2.1 added to Puhti, Mahti and LUMI. Horovod has
    been removed, we recommend using [PyTorch DDP](../support/tutorials/ml-multi.md) 
    instead. [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/) 
    was added to the Puhti and Mahti version.
    
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

| Version | Module         | Puhti | Mahti | LUMI | Notes                      |
|:--------|----------------|:-----:|:-----:|------|:---------------------------|
| 2.4.1   | `pytorch/2.4`  | -     | -     | X    | default version            |
| 2.4.0   | `pytorch/2.4`  | X     | X     | -    | New tykky-based wrappers   |
| 2.3.1   | `pytorch/2.3`  | X     | X     | -    | New tykky-based wrappers   |
| 2.2.2   | `pytorch/2.2`  | -     | -     | X    | default version            |
| 2.2.1   | `pytorch/2.2`  | X     | X     | -    |                            |
| 2.1.2   | `pytorch/2.1`  | -     | -     | X    |                            |
| 2.1.0   | `pytorch/2.1`  | X     | X     | -    |                            |
| 2.0.1   | `pytorch/2.0`  | -     | -     | X    |                            |
| 2.0.0   | `pytorch/2.0`  | X     | X     | -    |                            |
| 1.13.1  | `pytorch/1.13` | -     | -     | X    | limited multi-node support |
| 1.13.0  | `pytorch/1.13` | X     | X     | -    |                            |
| 1.12.0  | `pytorch/1.12` | X     | X     | -    |                            |
| 1.11.0  | `pytorch/1.11` | X     | X     | -    |                            |
| 1.10.0  | `pytorch/1.10` | (x)   | (x)   | -    |                            |
| 1.9.0   | `pytorch/1.9`  | (x)   | (x)   | -    |                            |
| 1.8.1   | `pytorch/1.8`  | (x)   | (x)   | -    |                            |
| 1.7.1   | `pytorch/1.7`  | (x)   | -     | -    |                            |

Includes [PyTorch](https://pytorch.org/) and related libraries with
GPU support via CUDA/ROCm.

Versions marked with "(x)" are based on old Red Hat Enterprise Linux 7
(RHEL7) images, and are no longer fully supported. In particular MPI
and Horovod are not expected to work anymore with these modules. If
you still wish to access these versions, you need to enable old RHEL7
modules by `module use /appl/soft/ai/rhel7/modulefiles/`.

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
normal. 

For **PyTorch version 2.2 and earlier**, other commands need to be
prefixed with `apptainer_wrapper exec`, for example `apptainer_wrapper
exec huggingface-cli`. For more information, see [CSC's general
instructions on how to run Apptainer
containers](../computing/containers/run-existing.md). 

For **PyTorch version 2.3 and later on Puhti or Mahti**, we have used
wrappers created with [the tykky
tool](../computing/containers/tykky.md), and all commands provided by
pre-installed Python packages are wrapped and can be used directly. In
case you really need to run something inside the container you can
prefix with `_debug_exec` or run `_debug_shell` to open a shell
session.


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

If you wish to have a specific version ([see above for available
versions](#available)), use:

```text
module load pytorch/2.4
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
    #SBATCH --mem=80G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:1
        
    module load pytorch/2.4
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
    
    module load pytorch/2.4
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
    module load pytorch/2.4
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


### PyTorch profiler

If your PyTorch program is slow, or you notice that it has a [low GPU
utilization](../support/tutorials/gpu-ml.md#gpu-utilization) you can
use the [PyTorch
profiler](https://pytorch.org/tutorials/intermediate/tensorboard_profiler_tutorial.html)
to analyze the time and memory consumption of your program.

The PyTorch profiler can be taken into use by adding a few lines of
code to your existing PyTorch program:

```python
from torch.profiler import profile, ProfilerActivity

prof = profile(
    schedule=torch.profiler.schedule(
        skip_first=10,
        wait=5,
        warmup=1,
        active=3, 
        repeat=1)
    on_trace_ready=torch.profiler.tensorboard_trace_handler('./logs/profiler'),
    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
    record_shapes=True,   # record shapes of operator inputs
    profile_memory=True,  # track tensor memory allocation/deallocation
    with_stack=True       # record source code information
)
```

In this example we opt to skip the first 10 batches and record only a
few batches for profiling. The profiling trace is saved into
TensorBoard format into the directory `logs/profiler`. To see all the
options, check the [PyTorch API documentation for
profiler](https://pytorch.org/docs/stable/profiler.html#torch.profiler.profile).

Next you need to start and stop the profiler, and record the
individual steps (typically the batches). This would typically be
around your training loop:

```python
prof.start()

for batch in train_loader:
    # normal forward and backprop stuff here
    prof.step()

prof.stop()
```

In our [GitHub
repository](https://github.com/CSCfi/pytorch-ddp-examples/) we gave a
full example with profiling:
[`mnist_ddp_profiler.py`](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_ddp_profiler.py)
with a corresponding [Slurm batch job
script](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-ddp-gpu1-profiler.sh).

After running the job you can view the output of the profiler using
TensorBoard.  Start a TensorBoard session in the [web interface of the
supercomputer](../computing/webinterface/apps.md) you are using. If
the PyTorch profiler isn't opened automatically you may be able to
find it as *PYTORCH_PROFILER* in the tab bar. If the tab isn't visible
by default, it can be found at the pull-down menu on the right-hand
side of the interface.

A particularly useful view is the Trace view (select "Trace" from the
"Views" pull-down menu). Below is an example screenshot of a run of
the example linked to above.

![Screenshot of PyTorch profiler in TensorBoard](../img/pytorch-profiler1.png)

The Trace view can be zoomed in and panned using the small toolbar to
the upper right, or using the 'a' and 'd' keys to pan, and 'w' and 's'
for zooming in and out.

In the screenshot we can see:

- Area 1, marked with red, shows the data loading (can be seen by
  zooming in and reading the function names shown. This is run
  entirely in the CPU as it's only colored in the top part of the
  screen under regular python CPU threads.
- Area 2, marked with blue, shows the forward and back propagation
  steps. Part of this is done on the GPU, as seen by the coloring in
  the bottom part, in the "GPU 0" area.
  
Clearly this job is not utilizing the GPU well as a majority of the
time is used in CPU processing. In general one could try adding more
CPU cores to handle the data loading more efficiently, and increase
the batch size to increase the GPU processing load.  In this
particular case, however, the problem is that the network is so small
that it cannot really utilize the GPU fully.

More hints on how to view and interpret the output of the profiler can
be found in the [PyTorch profiler with TensorBoard
tutorial](https://pytorch.org/tutorials/intermediate/tensorboard_profiler_tutorial.html#use-tensorboard-to-view-results-and-analyze-model-performance).


## More information

- [CSC's Machine learning guide](../support/tutorials/ml-guide.md)
- [PyTorch documentation](https://pytorch.org/docs/stable/index.html)
