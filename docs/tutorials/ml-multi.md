# Multi-GPU and multi-node machine learning

This guide explains how to utilize multiple GPUs and multiple nodes for machine
learning applications on CSC's supercomputers. It is part of our [Machine
learning guide](ml-guide.md).

First we will explain the general principles, such as single- and
multi-node jobs and mechanisms for launching multiple processes. After
that we discuss some common software frameworks how to use them on
CSC's supercomputers: [PyTorch DDP](#pytorch-ddp),
[DeepSpeed](#deepspeed) and briefly [Horovod](#horovod) and
[TensorFlow's
`tf.distribute.Strategy`](#tensorflows-tfdistributestrategy).

## Nodes and tasks

### GPU Nodes

Each separate GPU node (i.e., a single computer in the cluster), has a
fixed number of GPUs. Puhti and Mahti have 4 GPUs per node, and LUMI
has 8 GPUs per node.  (Technically a LUMI node has 4 GPUs cards, but 8
GPU dies.) The entire supercomputer may have tens or even thousands of
GPU nodes. See [GPU-accelerated machine learning](gpu-ml.md) for more
details, in particular the table describing the different GPUs in
CSC's various supercomputers might be of interest.

If you need 1-4 GPUs (or 1-8 in LUMI) you should always reserve a
**single node job**. If you need more than 4 GPUs (or 8 in LUMI) you
need to reserve a **multi-node job**. While it is technically possible
to reserve, e.g., two GPUs in one node and two in another, this is not
recommended except for testing purposes, as the communication across
nodes is always slower than inside a node.


### MPI tasks

When parallelizing to multiple GPUs it is common to allocate a
separate CPU process for handling the communication to each GPU. This
per GPU task division may be handled by the program itself, for
example using [Python's multiprocessing
library](https://docs.python.org/3/library/multiprocessing.html) to
launch separate processes. Another method is to use Slurm's MPI
facility to launch **multiple MPI tasks**. Whether MPI tasks are used
or not often depends on the software framework used.

### Slurm examples

In this section we provide Slurm batch script examples for launching
single- or multi-node jobs, with or without MPI.

!!! warning "Note"
    
    Please make sure that your code can actually take advantage of multiple GPUs as
    this typically requires some changes to the program. **Simply reserving more GPUs
    is not enough!**
    
You can [monitor that your program is using all the reserved
GPUs](gpu-ml.md#gpu-utilization) with the same mechanisms described in
our GPU-accelerated machine learning guide. The only difference is
that you should now see statistics for more than one GPU.


#### Single node run using 2 GPUs, no MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=20
    #SBATCH --mem=190G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:2
        
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=64
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:2
    
    srun python3 myprog.py <options>
    ```
    
    Note that on Mahti, the maximum for the `gpusmall` partition is 2
    GPUs. For 3 or 4 GPUs or more you need to use the `gpumedium`
    partition.

=== "LUMI"

    LUMI example coming soon!


The example above can be easily changed to more than 2 GPUs by
changing the number specified in the `--gres` option (Puhti and Mahti)
or `--gpus-per-node` option (LUMI). The maximum for a single node job
is 4 GPUs (Puhti and Mahti) or 8 GPUs (LUMI). 

If you increase the number of GPUs you may also wish to increase the
number of CPU cores and the amount of memory reserved. In our
examples, we have used **as a rule of thumb to reserve CPU cores and
memory in the same proportion as the number of GPUs**. For example in
Puhti there are 4 GPUs, 40 CPU cores, and 384 GBs of memory per
node. For each GPU we would then reserve 10 CPU cores, and roughly 95G
of memory (for memory we round down a bit as the units are not so
exact).

#### Single node using all GPUs, using MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    LUMI example coming soon!


The option `--mem=0` means to reserve all memory in that node.


#### Multi-node with 2 full nodes, no MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    LUMI example coming soon!


Note that the `--gres` option always specifies the number of GPUs on a
*single-node*, even in the multi-node case. So if we are reserving 8
GPUs across 2 nodes in Puhti, that is 4 GPUs on each node, i.e,
`--gres=gpu:v100:4`.


#### Multi-node with 2 full nodes, using MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    LUMI example coming soon!


## Available frameworks

There are many frameworks for doing multi-GPU and multi-node machine
learning. Some frameworks are tightly coupled to a specific framework,
such as PyTorch `DistributedDataParallel`, DeepSpeed or TensorFlow's
`tf.distribute.Strategy`, while others are more general, for example
Horovod.

Independent of which framework you pick, pay attention to the approach
used to launch jobs. For example with Horovod it is common to use MPI,
while DeepSpeed can be configured to use MPI or its own parallel
launcher. In some frameworks, the launching mechanism may also vary
depending on if you are running a single- or multi-node job.

All frameworks should use
[NCCL](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html)
(or [RCCL](https://github.com/ROCmSoftwarePlatform/rccl) for AMD) for
fast inter-GPU communication, even if MPI is used to set up the
connections.


### PyTorch DDP

[PyTorch
distributed](https://pytorch.org/tutorials/beginner/dist_overview.html),
and in particular `DistributedDataParallel` (DDP), offers a nice way
of running multi-GPU and multi-node PyTorch jobs. Unfortunately, the
PyTorch documentation has been a bit lacking in this area, and
examples found online can often be out-of-date. Hence, to make usage
of DDP on CSC's supercomputers easier, we have created a [set of
examples on how to run simple DDP jobs in the
cluster](https://github.com/CSCfi/pytorch-ddp-examples). In the
examples we use the
[rendezvous](https://pytorch.org/docs/stable/elastic/rendezvous.html)
mechanism to set up communcations across nodes, not MPI.

Example Slurm batch job for running PyTorch DDP on a single full node:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch
    
    srun python3 -m torch.distributed.run --standalone --nnodes=1 --nproc_per_node=4 \
        myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=128
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    module purge
    module load pytorch

    srun python3 -m torch.distributed.run --standalone --nnodes=1 --nproc_per_node=4 \
        myprog.py <options>
    ```


Example of running PyTorch DDP on 2 full nodes:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400
    
    module purge
    module load pytorch

    srun python3 -m torch.distributed.run \
        --nnodes=$SLURM_JOB_NUM_NODES \
        --nproc_per_node=4 \
        --rdzv_id=$SLURM_JOB_ID \
        --rdzv_backend=c10d \
        --rdzv_endpoint="$RDZV_HOST:$RDZV_PORT" \
        myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400
    
    module purge
    module load pytorch

    srun python3 -m torch.distributed.run \
        --nnodes=$SLURM_JOB_NUM_NODES \
        --nproc_per_node=4 \
        --rdzv_id=$SLURM_JOB_ID \
        --rdzv_backend=c10d \
        --rdzv_endpoint="$RDZV_HOST:$RDZV_PORT" \
        myprog.py <options>
    ```


If you are converting an old PyTorch script there are a few steps that you need to do:

1. Initialize with `init_process_group()`, for example:

    ```python
    import torch.distributed as dist

    dist.init_process_group(backend='nccl')

    local_rank = int(os.environ['LOCAL_RANK'])
    torch.cuda.set_device(local_rank)
    ```

2. Wrap your model with `DistributedDataParallel`:

    ```python
    from torch.nn.parallel import DistributedDataParallel

    model = DistributedDataParallel(model, device_ids=[local_rank])
    ```

3. Use `DistributedSampler` in your `DataLoader`:

    ```python
    from torch.utils.data.distributed import DistributedSampler

    train_sampler = DistributedSampler(train_dataset)
    train_loader = DataLoader(dataset=train_dataset, sampler=train_sampler, ...)
    ```


A fully working example for Puhti can be found in our [`pytorch-ddp-examples`
repository](https://github.com/CSCfi/pytorch-ddp-examples):

- [mnist_ddp.py](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_ddp.py)
  shows the Python code for training a simple CNN model on MNIST data
  using PyTorch DDP
- [run-ddp-gpu4.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-ddp-gpu4.sh)
  contains the Slurm script to run the training on 4 GPUs on a single
  node
- [run-ddp-gpu8.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-ddp-gpu8.sh)
  shows the same for two full nodes, with a total of 8 GPUs


### DeepSpeed

[DeepSpeed](https://www.deepspeed.ai/) is an optimization software
suite for PyTorch that helps in scaling both training and inference
for large deep learning models. DeepSpeed is supported in the [PyTorch
modules in Puhti and Mahti](../apps/pytorch.md) since version
1.10. DeepSpeed is not yet fully supported on LUMI.

Example of running DeepSpeed on a single full node using the
`deepspeed` launcher:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch
    
    srun singularity_wrapper exec deepspeed myprog.py \
        --deepspeed --deepspeed_config my_ds_config.json \
        <further options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=128
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4

    module purge
    module load pytorch

    srun singularity_wrapper exec deepspeed myprog.py \
        --deepspeed --deepspeed_config my_ds_config.json \
        <further options>
    ```
   
<br/>

Example of running DeepSpeed on 2 full nodes using MPI for launching a
separate task for each GPU:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch

    srun python3 myprog.py \
        --deepspeed --deepspeed_config my_ds_config.json \
        <further options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    module purge
    module load pytorch

    srun python3 myprog.py \
        --deepspeed --deepspeed_config my_ds_config.json \
        <further options>
    ```

If you are converting an old PyTorch script there are a few steps that
you need to do:

1. Make sure it handles the DeepSpeed command line arguments, for example:

    ```python
    import argparse
    
    parser = argparse.ArgumentParser()
    # handle any own command line arguments here
    parser = deepspeed.add_config_arguments(parser)
    
    args = parser.parse_args()
    ```

2. Initialize the distributed environment, for example:

    ```python
    import deepspeed

    deepspeed.init_distributed()
    ```
    
3. Initialize the DeepSpeed engine:

    ```python
    model = # defined in normal way
    train_dataset = # defined normally
    
    model_engine, optimizer, train_loader, __ = deepspeed.initialize(
        args=args, model=model, model_parameters=model.parameters(),
        training_data=train_dataset)
    ```
    
4. Modify the training loop to use the DeepSpeed engine:

    ```python
    for batch in train_loader:
        data = batch[0].to(model_engine.local_rank)
        labels = batch[1].to(model_engine.local_rank)

        outputs = model_engine(data)
        loss = criterion(outputs, labels)

        model_engine.backward(loss)
        model_engine.step()
    ```


See the [DeepSpeed Getting started
guide](https://www.deepspeed.ai/getting-started/) for the full
details. In particular you also need to create a [DeepSpeed
configuration
file](https://www.deepspeed.ai/getting-started/#deepspeed-configuration).

A fully working example can be found in our [`pytorch-ddp-examples`
repository](https://github.com/CSCfi/pytorch-ddp-examples):

- [mnist_deepspeed.py](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_deepspeed.py)
  shows the Python code for training a simple CNN model on MNIST data
  using PyTorch DeepSpeed
- [run-deepspeed-gpu4.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-deepspeed-gpu4.sh)
  contains the Slurm script to run the training on 4 GPUs on a single
  node
- [run-deepspeed-gpu8.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-deepspeed-gpu8.sh)
  shows the same for two full nodes, with a total of 8 GPUs
- [ds_config.json](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/ds_config.json)
  shows the DeepSpeed configuration file used for this example


### Horovod

[Horovod](https://horovod.ai/) is a general library that supports
PyTorch and TensorFlow among other frameworks. With Horovod you should
use MPI for launching jobs.  Horovod can be used both with single- and
multi-node jobs.

In CSC's supercomputers Horovod is supported only for some specific
versions of [TensorFlow](../apps/tensorflow.md) and
[PyTorch](../apps/pytorch.md).  Please check the application pages
for further information. To take Horovod into use, just load the
appropriate module, and modify your program according to the
instructions in [Horovod's
documentation](https://horovod.readthedocs.io/), for example:

* [Horovod with PyTorch](https://horovod.readthedocs.../latest/pytorch.html)
* [Horovod with TensorFlow](https://horovod.readthedocs.../stable/tensorflow.html) and [Keras](https://horovod.readthedocs.../stable/keras.html)


### TensorFlow's `tf.distribute.Strategy`

TensorFlow also has its own [built-in mechanisms for distributed
training](https://www.tensorflow.org/guide/distributed_training) in
the [`tf.distribute.Strategy`
API](https://www.tensorflow.org/api_docs/pyth../distribute/Strategy).



