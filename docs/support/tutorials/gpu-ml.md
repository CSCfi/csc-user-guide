# GPU-accelerated machine learning

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
nodes](../../computing/overview.md#gpu-nodes). In particular, the policy favors
machine learning and AI workloads for Mahti's GPU partition (Mahti-AI). Another
thing to consider is that the Slurm queuing situation may vary between Puhti and
Mahti at different times. However, note that Puhti and Mahti have different file
systems, so you need to manually copy your files if you wish to change the
system. **In case you are unsure which supercomputer to use, Puhti is a good
default** as it has a wider set of software supported.


## Available machine learning software

We support many applications for GPU-accelerated machine learning on CSC's supercomputers:
[list of supported applications](../../apps/index.md#data-analytics-and-machine-learning). 
Please read the detailed instructions for the specific application that you are interested
in, for example [TensorFlow](../../apps/tensorflow.md), [PyTorch](../../apps/pytorch.md),
[MXNET](../../apps/mxnet.md), and [RAPIDS](../../apps/rapids.md).

In brief, you need to use the [module system](../../computing/modules.md) to
load the application you want, for example:

```bash
module load tensorflow/2.4
```

Please note that our modules already include CUDA and cuDNN libraries, so
**there is no need to load cuda and cudnn modules separately!**

Finally, on Puhti, we provide some special applications which are not shown by
default in the module system. These have been made available due to user
requests, but with limited support. You can enable them by running:

```bash
module use /appl/soft/ai/singularity/modulefiles/
```

<!-- ##### Intel TensorFlow -->

<!-- Intel CPU-optimized version of tensorflow in the module -->
<!-- `intel-tensorflow/2.3-cpu-sng`. -->

<!-- ##### DeepLabCut -->

<!-- [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut/) is a software -->
<!-- package for animal pose estimation, available in the module `deeplabcut/2.1.9`. -->

<!-- ##### Turku neural parser -->

<!-- [Turku neural parser](http://turkunlp.org/Turku-neural-parser-pipeline/) is a -->
<!-- pipeline for segmentation, morphological tagging, dependency parsing and -->
<!-- lemmatization created by the [Turku NLP group](http://turkunlp.org/). -->

<!--     module use /appl/soft/ai/singularity/modulefiles/ -->
<!--     module load turku-neural-parser/fi-en-sv-cpu -->
<!--     echo "Minulla on koira." | singularity_wrapper run stream fi_tdt parse_plaintext -->

<!-- There is also a GPU-version `turku-neural-parser/fi-en-sv-gpu`. -->

<!-- **NOTE:** running the command requires at least 4GB of RAM, so you need to run it -->
<!-- in an [interactive session](../../computing/running/interactive-usage.md) or a -->
<!-- batch job. -->


To submit a job to the slurm queue using GPUs, you need to use the `gpu`
partition on Puhti or `gpusmall` or `gpumedium` on Mahti, and also specify the
type and number of GPUs using the `--gres` flag. Below are example batch scripts
for reserving one GPU and a corresponding 1/4 of the CPU cores of a single node:

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
GPUs, use the `gpumedium` queue. You can [read more about multi-GPU and
multi-node jobs](#multi-gpu-and-multi-node-jobs) below.

For more detailed information about the different partitions, see our page about
[the available batch job partitions on CSC's
supercomputers](../../computing/running/batch-job-partitions.md).

## GPU utilization

GPUs are an expensive resource compared to CPUs ([60 times more
BUs!](../../accounts/billing.md)). Hence, ideally, a GPU should be maximally
utilized when it has been reserved.

You can check the GPU utilization of a running job by `ssh`ing to the node where
it is running and running `nvidia-smi`. You should be able to identify your run
from the process name or the process id, and check the corresponding "GPU-Util"
column. Ideally it should be above 90%.

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


Alternatively, you can use `seff` which shows GPU utilisation statistics for the
whole running time. (NOTE: this works only on Puhti at the moment.)

```bash
seff <job_id>
```

In this example we can see that maximum utilization is 100%, but average is 92%.
If the average improves over time it is probably due to slow startup time, e.g.,
initial startup processing where the GPU is not used at all.

```
GPU load 
     Hostname        GPU Id      Mean (%)    stdDev (%)       Max (%) 
       r01g07             0         92.18         19.48           100 
------------------------------------------------------------------------
GPU memory 
     Hostname        GPU Id    Mean (GiB)  stdDev (GiB)     Max (GiB) 
       r01g07             0         16.72          1.74         16.91 
```

As always, don't hesitate to [contact our service
desk](https://www.csc.fi/contact-info) if you need advice on how to improve you
GPU utilization.

   
### Using multiple CPUs for data pre-processing

One common reason for the GPU utilization being low is when the CPU cannot load
and pre-process the training data fast enough, and the GPU has to wait for the
next batch to process. It is then a common practice to reserve more CPUs to
perform data loading and pre-processing in several parallel threads or
processes. A good rule of thumb in Puhti is to **reserve 10 CPUs per GPU** (as
there are 4 GPUs and 40 CPUs per node). On Mahti you can reserve up to 32 cores,
as that corresponds to 1/4 of the node. **Remember that CPUs are a much cheaper
resource than the GPU!**

You might have noticed that we have already followed this advice in our example
job scripts:

```bash
#SBATCH --cpus-per-task=10
```

Remember that your code also has to support parallel pre-processing. However,
most high-level machine learning frameworks support this out of the box. For
example in [TensorFlow you can use
`tf.data`](https://www.tensorflow.org/guide/data) and set `num_parallel_calls`
to the number of CPUs reserved and utilize `prefetch`:

```python
dataset = dataset.map(..., num_parallel_calls=10)
dataset = dataset.prefetch(buffer_size)
```

In [PyTorch, you can use
`torch.utils.DataLoader`](https://pytorch.org/docs/stable/data.html), which
supports loading with multiple processes:

```python
train_loader = torch.utils.data.DataLoader(..., num_workers=10)
```
