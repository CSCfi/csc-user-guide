# GPU-accelerated machine learning

This guide explains the basics of using GPUs in CSC's supercomputers. It is part
of our [Machine learning guide](ml-guide.md).


## Puhti or Mahti?

Puhti and Mahti are CSC's two supercomputers. Puhti has the largest number of
GPUs (V100) and offers the widest selection of installed software, while Mahti
has a smaller number of faster newer generation A100 GPUs. The main GPU-related
statistics are summarized in the table below.

|       | GPU type           | GPU memory | GPU nodes | GPUs/node | Total GPUs |
|-------|--------------------|------------|-----------|-----------|------------|
| Puhti | NVIDIA Volta V100  | 32 GB      | 80        | 4         | 320        |
| Mahti | NVIDIA Ampere A100 | 40 GB      | 24        | 4         | 96         |

Please read our [usage policy for the GPU
nodes](../../computing/overview.md#gpu-nodes). Also consider that the Slurm
queuing situation may vary between Puhti and Mahti at different times. However,
note that Puhti and Mahti have distinct file systems, so you need to manually
copy your files if you wish to change the system. **In case you are unsure which
supercomputer to use, Puhti is a good default** as it has a wider set of
software supported.


## Available machine learning software

We support [a number of
applications](../../apps/index.md#data-analytics-and-machine-learning) for
GPU-accelerated machine learning on CSC's supercomputers, including
[TensorFlow](../../apps/tensorflow.md) and [PyTorch](../../apps/pytorch.md).
Please read the detailed instructions for the specific application that you are
interested in.

You need to use the [module system](../../computing/modules.md) to
load the application you want, for example:

```bash
module load tensorflow/2.7
```

Please note that our modules already include CUDA and cuDNN libraries, so there
is no need to load cuda and cudnn modules separately!

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

For more complex software requirements, we recommend using Singularity
containers. These are similar to Docker containers, and are well supported in
CSC's supercomputers, in fact many of our own modules are based on Singularity.
See our [documentation on how to run Singularity
containers](../../computing/containers/run-existing.md), and [how to create your
own containers](../../computing/containers/creating.md).


## Running GPU jobs

To submit a GPU job to the Slurm workload manager, you need to use the `gpu`
partition on Puhti or `gpusmall` or `gpumedium` on Mahti, and specify the type
and number of GPUs required using the `--gres` flag. Below are example batch
scripts for reserving one GPU and a corresponding 1/4 of the CPU cores of a
single node:

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

Mahti's `gpusmall` partition supports only jobs with 1-2 GPUs. If you need more
GPUs, use the `gpumedium` queue. You can read more about [multi-GPU and
multi-node jobs in our separate tutorial](ml-multi.md).

For more detailed information about the different partitions, see our page about
[the available batch job partitions on CSC's
supercomputers](../../computing/running/batch-job-partitions.md).

## GPU utilization

GPUs are an expensive resource compared to CPUs ([60 times more
BUs!](../../accounts/billing.md)). Hence, ideally, a GPU should be maximally
utilized once it has been reserved.

You can check the current GPU utilization of a running job by `ssh`ing to the
node where it is running and running `nvidia-smi`. You should be able to
identify your run from the process name or the process id, and check the
corresponding "GPU-Util" column. Ideally it should be above 90%.

For example, from the following excerpts we can see that on GPU 0 a `python3`
job is running which uses roughly 17 GB of GPU memory and the current GPU
utilization is 99% (i.e., very good).

```
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000000:61:00.0 Off |                    0 |
| N/A   51C    P0   247W / 300W |  17314MiB / 32510MiB |     99%      Default |
```

```
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0    122956      C   python3                                    17301MiB |
```


Alternatively, you can use `seff` which shows GPU utilization statistics for the
whole running time.

```bash
seff <job_id>
```

In this example we can see that maximum utilization is 100%, but average is 92%.

```
GPU load 
     Hostname        GPU Id      Mean (%)    stdDev (%)       Max (%) 
       r01g07             0         92.18         19.48           100 
------------------------------------------------------------------------
GPU memory 
     Hostname        GPU Id    Mean (GiB)  stdDev (GiB)     Max (GiB) 
       r01g07             0         16.72          1.74         16.91 
```

As always, don't hesitate to [contact our service desk](../contact.md) if you
need advice on how to improve you GPU utilization.

   
### Using multiple CPUs for data pre-processing

One common reason for the GPU utilization being low is when the CPU cannot load
and pre-process the data fast enough, and the GPU has to wait for the next batch
to process. It is then a common practice to reserve more CPUs to perform data
loading and pre-processing in several parallel threads or processes. A good rule
of thumb in Puhti is to **reserve 10 CPUs per GPU** (as there are 4 GPUs and 40
CPUs on each node). On Mahti you can reserve up to 32 cores, as that corresponds to
1/4 of the node. **Remember that CPUs are a much cheaper resource than the
GPU!**

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
