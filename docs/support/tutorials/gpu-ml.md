---
title: GPU-accelerated machine learning
---

# GPU-accelerated machine learning

This guide explains the basics of using GPUs in CSC's supercomputers. It is part
of our [Machine learning guide](ml-guide.md).


## Puhti, Mahti or LUMI?

Puhti and Mahti are CSC's two national supercomputers. Of the two,
Puhti has the larger number of GPUs (NVIDIA V100) and offers the
widest selection of installed software, while Mahti has a smaller
number of faster newer generation NVIDIA A100 GPUs. The CSC-hosted
European supercomputer
[LUMI](https://docs.lumi-supercomputer.eu/hardware/) provides a
massive GPU resource based on AMD GPUs.

The main GPU-related statistics are summarized in the table below.

|       | GPU type           | GPU memory  | GPU nodes | GPUs/node | Total GPUs    |
|-------|--------------------|-------------|-----------|-----------|---------------|
| Puhti | NVIDIA Volta V100  | 32 GB       | 80        | 4         | 320           |
| Mahti | NVIDIA Ampere A100 | 40 GB       | 24        | 4         | 96            |
| LUMI  | AMD MI250x         | 64 (128) GB | 2978      | 8 (4)     | 23824 (11912) |

!!! info "Note"

    Each LUMI node has 4 MI250x GPUs, however 8 GPUs will be available
    through Slurm as the MI250x card features 2 GPU dies (GCDs). The table
    above shows the GPU die specific numbers, MI250x card specific numbers
    are shown in parenthesis.

Please read our [usage policy for the GPU
nodes](../../computing/usage-policy.md#gpu-nodes). Also consider that
the Slurm queuing situation may vary between the different
supercomputers at different times, so it may be worth checking out all
the options. For example LUMI has a huge number of GPUs available, and
queuing times are very short (as of summer 2023).

Note that all supercomputers have distinct file systems, so you need
to manually copy your files if you wish to change the system. **In
case you are unsure which supercomputer to use, Puhti is a good
default** as it has a wider set of software supported.


## Available machine learning software

We support [a number of
applications](../../apps/by_discipline.md#data-analytics-and-machine-learning)
for GPU-accelerated machine learning on CSC's supercomputers,
including [TensorFlow](../../apps/tensorflow.md) and
[PyTorch](../../apps/pytorch.md).  Please read the detailed
instructions for the specific application that you are interested in.

You need to use the [module system](../../computing/modules.md) to
load the application you want, for example:

```bash
module load tensorflow/2.12
```

Please note that our modules already include CUDA and cuDNN libraries, so there
is no need to load cuda and cudnn modules separately!

On LUMI you need to first enable the module repository for CSC's installations:

```bash
module use /appl/local/csc/modulefiles/
```

Finally, on Puhti, we provide some special applications which are not shown by
default in the module system. These have been made available due to user
requests, but with limited support. You can enable them by running:

```bash
module use /appl/soft/ai/singularity/modulefiles/
```

### Installing your own software

In many cases, our existing modules provide the required framework, but some
packages are missing. In this case you can often load the appropriate module and
then [install additional packages for personal use with the `pip` package
manager](../../apps/python.md#installing-python-packages-to-existing-modules).

For more complex software requirements, we recommend using
[tykky](../../computing/containers/tykky.md) or [creating your own
Apptainer container](../../computing/containers/creating.md).


## Running GPU jobs

To submit a GPU job to the Slurm workload manager, you need to use the `gpu`
partition on Puhti or `gpusmall` or `gpumedium` on Mahti, and specify the type
and number of GPUs required using the `--gres` flag. 

On LUMI you need to use one of the GPU-partitions such as `dev-g`,
`small-g` or `standard-g`.

Below are example batch scripts for reserving one GPU and a
corresponding proportion of the CPU cores and memory of a single node:

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
    
    srun python3 myprog.py <options>
    ```


Mahti's `gpusmall` partition supports only jobs with 1-2 GPUs. If you need more
GPUs, use the `gpumedium` queue. You can read more about [multi-GPU and
multi-node jobs in our separate tutorial](ml-multi.md).

For more detailed information about the different partitions, see our page about
[the available batch job partitions on CSC's
supercomputers](../../computing/running/batch-job-partitions.md) and [Slurm partitions on LUMI](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/).

## GPU utilization

GPUs are a very expensive resource compared to CPUs, hence, GPUs
should be maximally utilized once they have been allocated. We provide
some tools to monitor the utilization of GPU jobs on different
supercomputers. The GPU utilization, should ideally be close to
100%. If your utilization is consistently low (for example under 50%)
it might because of several reasons:

- You may have have a processing bottle-neck, for example you should
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

#### `seff` command for a completed job (Puhti and Mahti)

The easiest way to check the GPU utilization on a completed job is to
use the `seff` command:

```bash
seff <job_id>
```

In this example we can see that maximum utilization is 100%, but
average is 92% (this is a good level):

```
GPU load 
     Hostname        GPU Id      Mean (%)    stdDev (%)       Max (%) 
       r01g07             0         92.18         19.48           100 
------------------------------------------------------------------------
GPU memory 
     Hostname        GPU Id    Mean (GiB)  stdDev (GiB)     Max (GiB) 
       r01g07             0         16.72          1.74         16.91 
```

#### `nvidia-smi` for a running job (Puhti and Mahti)

When the job is running you can run `nvidia-smi` over `ssh` on the
node where it is running. You can check the node's hostname with the
`squeue --me` command. The output can look something like this:

```
   JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
17273947       gpu puhti-gp mvsjober  R       0:07      1 r01g06
```

You can see the node's hostname from the `NODELIST` column, in this
case it's `r01g06`. You can now check the GPU utilization with
(replace `<nodename>` with the actual node's hostname in your case):

```bash
ssh <nodename> nvidia-smi
```

The output will look something like this:

```
Wed Jun 14 09:53:11 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 515.105.01   Driver Version: 515.105.01   CUDA Version: 11.7     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000000:89:00.0 Off |                    0 |
| N/A   57C    P0   232W / 300W |   5222MiB / 32768MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A   2312753      C   /appl/soft/ai/bin/python3        5219MiB |
+-----------------------------------------------------------------------------+
```

From this we can see that our process is using around 5GB (out of 32GB) of GPU memory, and the current GPU utilization is 100% (which is very good).


If you want a continually updating view:

```bash
ssh r01g06 -t watch nvidia-smi
```

This will update every 2 seconds, press Ctrl-C to exit.


#### `rocm-smi` for a running job (LUMI)

The LUMI supercomputer uses AMD GPUs, and hence the command is a bit
different: `rocm-smi`. On [LUMI you need to use `srun` to log in to a node where you have a running job](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/interactive/#using-srun-to-check-running-jobs):

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
several parallel threads or processes. A good rule of thumb in Puhti
is to **reserve 10 CPUs per GPU** (as there are 4 GPUs and 40 CPUs on
each node). On Mahti you can reserve up to 32 cores, as that
corresponds to 1/4 of the node. On LUMI we recommend using 7 CPU
cores, as there are 63 cores for 8 GPUs. **Remember that CPUs are a
much cheaper resource than the GPU!**

You might have noticed that we have already followed this advice in our example
job scripts:

```bash
#SBATCH --cpus-per-task=10
```

Your code also has to support parallel pre-processing. However, most high-level
machine learning frameworks support this out of the box. For example in
[TensorFlow you can use `tf.data`](https://www.tensorflow.org/guide/data) and
set `num_parallel_calls` to the number of CPUs reserved and utilize `prefetch`:

```python
dataset = dataset.map(..., num_parallel_calls=10)
dataset = dataset.prefetch(buffer_size)
```

In [PyTorch, you can use
`torch.utils.DataLoader`](https://pytorch.org/docs/stable/data.html), which
supports data loading with multiple processes:

```python
train_loader = torch.utils.data.DataLoader(..., num_workers=10)
```

If you are using multiple data loaders, but data loading is still slow, it is
also possible that you are using the shared file system inefficiently. A common
error is to read a huge number of small files. You can read more about [how to
store and load data in the most efficient way for machine learning in our
separate tutorial](ml-data.md).

### Profilers

[TensorFlow Profiler](https://www.tensorflow.org/guide/profiler) and
[PyTorch
Profiler](https://pytorch.org/tutorials/intermediate/tensorboard_profiler_tutorial.html)
are available as TensorBoard plugins. The profilers can be found at
the *PROFILE* and *PYTORCH_PROFILER* tabs in TensorBoard,
respectively. Note that the tabs may not be visible by default but can
be found at the pull-down menu on the right-hand side of the
interface.  The profilers can be used to identify resource consumption
and to resolve performance bottlenecks, in particular the data input
pipeline.

See also:

- [How to launch TensorBoard using the Puhti web interface](../../computing/webinterface/apps.md)
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

#### `seff` command for a completed job (Puhti and Mahti)

On Puhti and Mahti you can use the `seff` tool for a completed job:

```bash
seff <job_id>
```

Note that the GPU energy usage is counted only after the job has
completed, so there is no intermediate value printed while it's
running.

Example output where we have used a single node with 4 GPUs:

```
GPU energy
      Hostname        GPU Id   Energy (Wh)
        r01g01             0         58.30
        r01g01             1         56.63
        r01g01             2         44.87
        r01g01             3         62.21
```


### `gpu-energy` tool (LUMI)

LUMI does not have the `seff` command, but there is a preliminary tool
that can be used to read the GPU energy counters found in the AMD GPU
card. The tool and its documentation can be found here:
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

