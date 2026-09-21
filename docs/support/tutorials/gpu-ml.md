---
title: GPU-accelerated machine learning
---

# GPU-accelerated machine learning

This guide explains the basics of using GPUs in CSC's supercomputers. It is part
of our [Machine learning guide](ml-guide.md).


## Roihu-GPU or LUMI?

Roihu is CSC's national supercomputer, meant mainly for researchers
based in Finland, opened in June 2026. Roihu-GPU, which refers to the
GPU side of Roihu, has 528 GPUs (NVIDIA GH200) and aims to provide a
wide and easy-to-use software stack for researchers.

CSC also hosts the European supercomputer
[LUMI](https://docs.lumi-supercomputer.eu/hardware/), which provides a
massive GPU resource based on AMD GPUs.

Roihu-GPU has a wide set of software for different fields of science and
getting access is very easy for Finnish-affiliated researchers. LUMI,
on the other hand provides a massive GPU resource, and enables much
larger jobs.

The main GPU-related statistics are summarized in the table below.

|           | GPU type            | GPU memory  | GPU nodes | GPUs/node | Total GPUs    |
|-----------|---------------------|-------------|-----------|-----------|---------------|
| Roihu-GPU | NVIDIA Hopper GH200 | 96 GB       | 132       | 4         | 528           |
| LUMI      | AMD MI250x          | 64 (128) GB | 2978      | 8 (4)     | 23824 (11912) |

!!! info "Note"

    Each LUMI node has 4 MI250x GPUs, however 8 GPUs will be available
    through Slurm as the MI250x card features 2 GPU dies (GCDs). The table
    above shows the GPU die specific numbers, MI250x card specific numbers
    are shown in parenthesis.

Please read our [usage policy for the GPU
nodes](../../computing/usage-policy.md#gpu-nodes). Also consider that
the Slurm queuing situation may vary between the different
supercomputers at different times, so it may be worth checking out all
the options.

Note that all supercomputers have distinct file systems, so you need
to manually copy your files if you wish to change the system. 


## Available machine learning software

We support [a number of
applications](../../apps/by_discipline.md#data-analytics-and-machine-learning)
for GPU-accelerated machine learning on CSC's supercomputers,
including [PyTorch](../../apps/pytorch.md), [JAX](../../apps/jax.md)
and [TensorFlow](../../apps/tensorflow.md).  Please read the detailed
instructions for the specific application that you are interested in.

You need to use the [module system](../../computing/modules.md) to
load the application you want, for example:

```bash
module load python-pytorch/2.10
```

Please note that our modules already include CUDA and cuDNN libraries, so there
is no need to load cuda and cudnn modules separately!

On LUMI, we recommend that you use the [AI Software Environment
provided by the LUMI AI Factory](https://docs.lumi-supercomputer.eu/laif/software/ai-environment/).


### Installing your own software

In many cases, our existing modules provide the required framework, but some
packages are missing. In this case you can often load the appropriate module and
then [install additional packages for personal use with the `pip` package
manager](./python-usage-guide.md#installing-python-packages-to-existing-modules).

For more complex software requirements, we recommend using
[tykky](../../computing/containers/tykky.md) or [creating your own
Apptainer container](../../computing/containers/overview.md#building-container-images).


## Running GPU jobs

To submit a GPU job to the Slurm workload manager, you need to use the
`gpumedium` partition on Roihu-GPU, and specify the type and number of
GPUs required using the `--gres` flag.

On LUMI you need to use one of the GPU-partitions such as `dev-g`,
`small-g` or `standard-g`.

Below are example batch scripts for reserving one GPU and a
corresponding proportion of the CPU cores and memory of a single node:

=== "Roihu-GPU"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=72
    #SBATCH --gres=gpu:gh200:1
    #SBATCH --time=1:00:00
    
    # load any modules and run your program here
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
    
    # load any modules and run your program here
    ```

Roihu-GPU also has a [`gpularge` partition which requires a scalability
test for
access](../../accounts/how-to-access-roihu-large-partition.md)

For more detailed information about the different partitions, see our page about
[the available batch job partitions on CSC's
supercomputers](../../computing/running/batch-job-partitions.md) and [Slurm partitions on LUMI](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/).

## GPU utilization

GPUs are a very expensive resource compared to CPUs, hence, GPUs
should be maximally utilized once they have been allocated. We provide
some tools to monitor the utilization of GPU jobs on different
supercomputers. The GPU utilization, should ideally be close to
100%. If your utilization is consistently low (for example under 50%)
it might be because of several reasons:

- You may have a processing bottleneck, for example you should
  use a data loading framework (and reserve enough CPU cores for it)
  to be able to feed the GPU with data fast enough. [See our
  documentation on using multiple CPU cores for data
  loading](#using-multiple-cpus-for-data-pre-processing).
  
- Alternatively, it might simply be the case that the computational
  problem is "too small" for the GPU, for example if the neural
  network is relatively simple. This is not a problem as such, but if
  your utilization is really low, you might consider if using CPUs
  would be more cost efficient.

As always, don't hesitate to [contact our service desk](../contact.md)
if you have any questions regarding GPU utilization.

### Tools for monitoring GPU utilization

#### `nvidia-smi` for a running job (Roihu-GPU)

When the job is running you can run `nvidia-smi` over `ssh` on the
node where it is running. You can check the node's hostname with the
`squeue --me` command. The output can look something like this:

```
  JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
1341095   gputest roihu-gp mvsjober  R       0:24      1 rg2101
```

You can see the node's hostname from the `NODELIST` column, in this
case it's `rg2101`. You can now check the GPU utilization with
(replace `<nodename>` with the actual node's hostname in your case):

```bash
ssh <nodename> nvidia-smi
```

The output will look something like this:

```
Tue Sep 15 16:04:42 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.71.05              Driver Version: 595.71.05      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GH200 120GB             On  |   00000019:01:00.0 Off |                    0 |
| N/A   51C    P0            396W /  680W |    4964MiB /  97871MiB |     96%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A         1753915      C   ...rch/wrappers/2.13/bin/python3       4950MiB |
+-----------------------------------------------------------------------------------------+
```

From this we can see that our process is using around 5GB (out of
96GB) of GPU memory, and the current GPU utilization is 96% (which is
quite good).


If you want a continually updating view:

```bash
ssh <nodename> -t watch nvidia-smi
```

This will update every 2 seconds, press Ctrl-C to exit.


#### `rocm-smi` for a running job (LUMI)

The LUMI supercomputer uses AMD GPUs, and hence the command is a bit
different: `rocm-smi`. On [LUMI you need to use `srun` to log in to a
node where you have a running
job](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/interactive/#using-srun-to-check-running-jobs):

```bash
srun --interactive --pty --jobid=<jobid> rocm-smi
```

Replace `<jobid>` with the actual Slurm job ID. You can also use
`watch rocm-smi` to get the continually updated view.

   
### Using multiple CPUs for data pre-processing

One common reason for the GPU utilization being low is when the CPU
cannot load and pre-process the data fast enough, and the GPU has to
wait for the next batch to process. It is then a common practice to
reserve more CPUs to perform data loading and pre-processing in
several parallel threads or processes. For example on Roihu-GPU for each
GPU you can reserve a maximum of 72 CPU cores.

On LUMI we recommend using 7 CPU cores, as there are 63 cores for 8
GPUs.

You might have noticed that we have already followed this advice in
our example job scripts.

Your code also has to support parallel pre-processing. However, most
high-level machine learning frameworks support this out of the
box. For example in [PyTorch, you can use
`torch.utils.DataLoader`](https://pytorch.org/docs/stable/data.html),
which supports data loading with multiple processes:

```python
train_loader = torch.utils.data.DataLoader(..., num_workers=10)
```

The optimal number of workers depends on the dataset and other
factors. On Roihu-GPU, using all 72 cores is probably too much in most
cases, but 10 can be a good starting point.

If you are using multiple data loaders, but data loading is still slow, it is
also possible that you are using the shared file system inefficiently. A common
error is to read a huge number of small files. You can read more about [how to
store and load data in the most efficient way for machine learning in our
separate tutorial](ml-data.md).

### Profilers

[PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)
and [TensorFlow Profiler](https://www.tensorflow.org/guide/profiler)
are available as TensorBoard plugins. The profilers can be found at
the *PROFILE* and *PYTORCH_PROFILER* tabs in TensorBoard,
respectively. Note that the tabs may not be visible by default but can
be found at the pull-down menu on the right-hand side of the
interface.  The profilers can be used to identify resource consumption
and to resolve performance bottlenecks, in particular the data input
pipeline.

See also:

- [How to launch TensorBoard using the Roihu web interface](../../computing/webinterface/apps.md)
- [PyTorch profiler tutorial](../../apps/pytorch.md#pytorch-profiler)

## GPU energy usage

For ecological and economical reasons it is often needed to monitor
the energy usage of machine learning jobs. Measuring the full energy
usage of a single job, including CPU and GPU processing, networking
and cooling is quite difficult to do in the general case as those
resources are shared over many jobs and can depend on various factors
independent of the monitored job. Fortunately, measuring the energy
usage of just the GPUs is easier, as they are typically not shared
among many jobs. As the GPU is by far the biggest energy user it
provides a good approximation of the total energy usage.

### Tools for monitoring GPU energy usage

Roihu-GPU doesn't yet have any built-in support for monitoring the GPU
energy usage. In the meantime users can use the 
[NVIDIA Management Library](http://developer.nvidia.com/nvidia-management-library-nvml) 
or the corresponding [Python bindings in pyNVML](https://pypi.org/project/nvidia-ml-py/) 
to fetch GPU energy information.

### `gpu-energy` tool (LUMI)

For LUMI there is a simple tool that can be used to read the GPU
energy counters found in the AMD GPU card. The tool and its
documentation can be found here:
<https://github.com/mvsjober/gpu-energy-amd>.

It has been pre-installed on LUMI in the path `/appl/local/csc/soft/ai/bin/gpu-energy`.

Typical usage in a Slurm script:

```
gpu-energy --save

# run job here

gpu-energy --diff
```

Example output:

```
GPU 0: 46.64 Wh, avg power: 377.81 W (444.43 s)
GPU 2: 46.47 Wh, avg power: 376.46 W (444.43 s)
GPU 4: 46.18 Wh, avg power: 374.04 W (444.43 s)
GPU 6: 46.62 Wh, avg power: 377.62 W (444.43 s)
TOTAL: 185.91 Wh
```

Note that it prints the energy only for even-numbered GCDs, this is because the AMD GPU energy counter only produces a single value for the whole MI250x card.

!!! warning "Always measure GPU usage for a full node on LUMI!"

    Measuring the GPU energy on LUMI has to be done on a full node to get
    accurate results. The reason is that the MI250x GPU has 2 GPU dies
    (GCDs), but the energy counter gives a single number for the whole
    MI250x. If you reserve a single GCD, another run may be using the
    other GCD. Reserving 2 GCDs, it's not possible to guarantee that you
    get them from the same card.

See the [README.md file for more usage examples](https://github.com/mvsjober/gpu-energy-amd/blob/master/README.md).

