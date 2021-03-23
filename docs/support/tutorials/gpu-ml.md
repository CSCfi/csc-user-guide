# GPU-accelerated machine learning

## What CSC service to use?

If you need GPU-accelerated machine learning, CSC's supercomputers, Puhti and Mahti, are usually the way to go.  First, please read the [instructions on how to access Puhti and Mahti](../../computing/overview.md), and [how to submit computing jobs](../../computing/running/getting-started.md).

In some special cases, a virtual server on [**Pouta**](../../cloud/pouta/index.md) might make sense as it also offers GPUs.  This gives you more control over the computing environment, but may not be suitable for very heavy computing tasks.  For model deployment, the [**Rahti**](../../cloud/rahti/index.md) contained cloud service might be used, however, it currently doesn't offer GPU support. See some examples of [how to deploy machine learning models on Rahti](https://github.com/CSCfi/rahti-ml-examples).

## Using CSC's supercomputers

For GPU-accelerated machine learning on CSC's supercomputers, we support [TensorFlow](../../apps/tensorflow.md), [PyTorch](../../apps/pytorch.md), [MXNET](../../apps/mxnet.md), and [RAPIDS](../../apps/rapids.md).  Please read the detailed instructions for the specific application that you are interested in.  In brief, you need to use the [module system](../../computing/modules.md) to load the application you want, for example:

```bash
module load tensorflow/2.0.0
```

Please note that our modules already include CUDA and cuDNN libraries, so **there is no need to load cuda and cudnn modules separately!**

To submit a job to the slurm queue using GPUs, you need to use the `gpu` partition and also specify the type and number of GPUs using the `--gres` flag. An example batch script for reserving one GPU and 10 CPUs in a single node:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1

srun python3 myprog.py <options>
```

### Data storage

It is recommended to store big datasets in [Allas](../../data/Allas/index.md), and download them to your project's [scratch directory](../../computing/disk.md) prior to starting your computation.  Example:

```bash
module load allas
allas-conf
cd /scratch/<your-project>
swift download <bucket-name> your-dataset.tar
```

!!! note

    Please **do not read a huge number of files from the shared file system**, use fast local disk or package your data into larger files instead!


Many machine learning tasks, such as training a model, require reading a huge number of relatively small files from the drive.  Unfortunately the Lustre-shared file systems (e.g. `/scratch`, `/projappl` and users' home directories) do not perform very well when opening a lot of files, and it also causes noticeable slowdowns for all users of the supercomputer.  Instead, consider more efficient approaches, including:

- packaging your dataset into larger files 
- taking into use the [NVME fast local storage](../../computing/running/creating-job-scripts-puhti.md#local-storage) on the GPU nodes.

#### More efficient data format

Many machine learning frameworks support formats for packaging your data more efficiently.  For example [TensorFlow's TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord) format.  Other examples include using [HDF5](https://towardsdatascience.com/hdf5-datasets-for-pytorch-631ff1d750f5), or [LMDB](http://deepdish.io/2015/04/28/creating-lmdb-in-python/) formats, or even humble ZIP-files, e.g., via Python's [zipfile](https://docs.python.org/3/library/zipfile.html) library.  The main point with all of these is that instead of many thousands of small files you have one, or a few bigger files, which are much more efficient to access and read linearly.  Don't hesitate to [contact our service desk](https://www.csc.fi/contact-info) if you need advice about how to access your data more efficiently.


#### Fast local drive

If you really need to access the individual small files, you can use the fast local drive that is present in every GPU node.  In brief, you just need to add `nvme:<number-of-GB>` to the `--gres` flag in your submission script, and then the fast local storage will be available in the location specified by the environment variable `$LOCAL_SCRATCH`.  Here is an example run that reserves 100 GB of the fast local drive and extracts the dataset tar-package on that drive before launching the computation:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --gres=gpu:v100:1,nvme:100

tar xf /scratch/<your-project>/your-dataset.tar -C $LOCAL_SCRATCH

srun python3 myprog.py --input_data=$LOCAL_SCRATCH <options>
```

Note that you need to communicate somehow to your own program where to find the dataset, for example with a command line argument.  Also see our [general instructions on how to take the fast local storage into use](../../computing/running/creating-job-scripts-puhti.md#local-storage).

If you are running a multi-node job (see next section), you need to modify the `tar` line so that it is performed on each node separately:

```bash
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 \
    tar xf /scratch/<your-project>/your-dataset.tar -C $LOCAL_SCRATCH
```

### GPU utilization

GPUs are an expensive resource compared to CPUs ([60 times more BUs!](../../accounts/billing.md)).  Hence, ideally, a GPU should be maximally utilized when it has been reserved.

You can check the GPU utilization of a running job by `ssh`ing to the node where it is running and running `nvidia-smi`.  You should be able to identify your run from the process name or the process id, and check the corresponding "GPU-Util" column.  Ideally it should be above 90%.

For example, from the following excerpts we can see that on GPU 0 a `python3` job is running which uses roughly 17 GB of GPU memory and the current GPU utilization is 99% (i.e., very good).

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


Alternatively, you can use `seff` which shows GPU utilisation statistics for the whole running time.

```bash
seff <job_id>
```

In this example we can see that maximum utilization is 100%, but average is 92%.  If the average improves over time it is probably due to slow startup time, e.g., initial startup processing where the GPU is not used at all.

```
GPU load 
     Hostname        GPU Id      Mean (%)    stdDev (%)       Max (%) 
       r01g07             0         92.18         19.48           100 
------------------------------------------------------------------------
GPU memory 
     Hostname        GPU Id    Mean (GiB)  stdDev (GiB)     Max (GiB) 
       r01g07             0         16.72          1.74         16.91 
```

As always, don't hesitate to [contact our service desk](https://www.csc.fi/contact-info) if you need advice on how to improve you GPU utilization.

   
#### Using multiple CPUs for data pre-processing

One common reason for the GPU utilization being low is when the CPU cannot load and pre-process the training data fast enough, and the GPU has to wait for the next batch to process.  It is then a common practice to reserve more CPUs to perform data loading and pre-processing in several parallel threads or processes.  A good rule of thumb in Puhti is to **reserve 10 CPUs per GPU** (as there are 4 GPUs and 40 CPUs per node).  *Remember that CPUs are a much cheaper resource than the GPU!*

You might have noticed that we have already followed this advice in our example job scripts:

```bash
#SBATCH --cpus-per-task=10
```

Remember that your code also has to support parallel pre-processing.  However, most high-level machine learning frameworks support this out of the box.  For example in [TensorFlow you can use `tf.data`](https://www.tensorflow.org/guide/data) and set `num_parallel_calls` to the number of CPUs reserved and utilize `prefetch`:

```python
dataset = dataset.map(..., num_parallel_calls=10)
dataset = dataset.prefetch(buffer_size)
```

In [PyTorch, you can use `torch.utils.DataLoader`](https://pytorch.org/docs/stable/data.html), which supports loading with multiple processes:

```python
train_loader = torch.utils.data.DataLoader(..., num_workers=10)
```

### Multi-GPU and multi-node jobs

Multi-GPU jobs are also supported by specifying the number of GPUs required in the `--gres` flag, for example to have 4 GPUs (which is the maximum for a single node in Puhti): `--gres=gpu:v100:4`.  Please also make sure that your code can take advantage of multiple GPUs, this typically requires some changes to the program.

For large jobs requiring more than 4 GPUs we recommend using [Horovod](https://github.com/horovod/horovod), which is supported for TensorFlow and PyTorch on Puhti.  Horovod uses MPI and NCCL for interprocess communication. See also [MPI based batch jobs](../../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs).  Modules that support Horovod have the `-hvd` suffix in their name.  Note that Horovod is supported only for some specific versions of TensorFlow and PyTorch.  You can run `module avail hvd` to see all Horovod-enabled modules.  To take Horovod into use, just load the appropriate module, e.g:

```bash
module load tensorflow/2.0.0-hvd
```

Below is an example slurm batch script that uses 8 GPUs across two computers.  In MPI terminology we have 8 tasks on 2 nodes, each task has one GPU and 10 CPUs.

```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=10
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:4
#SBATCH --time=1:00:00
#SBATCH --mem=32G
#SBATCH --account=<project>

# uncomment the following line if you want to see some debug info from NCCL
# export NCCL_DEBUG=INFO

srun python3 myprog.py <options>
```

### Singularity

Our machine learning modules are increasingly being built using [Singularity containers](https://en.wikipedia.org/wiki/Singularity_(software)). If you are familiar with [Docker containers](https://en.wikipedia.org/wiki/Docker_(software)), Singularity containers as essentially the same thing, but are better suited for multi-user systems such as CSC's supercomputers. Containers provide an isolated software environment for each application, which has several benefits, including typically a much shorter start-up time.

In most cases, Singularity-based modules can be used in the same way as other modules as we have provided wrapper scripts so that common commands such as `python`, `python3`, `pip` and `pip3` should work as normal. Common paths such as `/projappl`, `/scratch` and users' home directories should be visible from inside the container.

However, if you need to run something else inside the container, you need to prefix that command with `singularity_wrapper exec`, for example `singularity_wrapper exec ps`. Another useful command is `singularity_wrapper shell` which starts a shell session inside the container.

Also check our [general instructions for using Singularity on Puhti](../../computing/containers/run-existing.md).


#### Special Singularity-based applications

Finally, we provide some special Singularity-based applications which are not shown by default in the module system.  You can enable them by running:

```bash
module use /appl/soft/ai/singularity/modulefiles/
```

##### Intel TensorFlow

Intel CPU-optimized version of tensorflow in the module `intel-tensorflow/2.3-cpu-sng`.

##### DeepLabCut

[DeepLabCut](http://www.mackenziemathislab.org/deeplabcut/) is a software package for animal pose estimation, available in the module `deeplabcut/2.1.9`.

##### Turku neural parser

[Turku neural parser](http://turkunlp.org/Turku-neural-parser-pipeline/) is a pipeline for segmentation, morphological tagging, dependency parsing and lemmatization created by the [Turku NLP group](http://turkunlp.org/).

    module use /appl/soft/ai/singularity/modulefiles/
    module load turku-neural-parser/fi-en-sv-cpu
    echo "Minulla on koira." | singularity_wrapper run stream fi_tdt parse_plaintext

There is also a GPU-version `turku-neural-parser/fi-en-sv-gpu`.
