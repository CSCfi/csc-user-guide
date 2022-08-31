# Multi-GPU and multi-node machine learning

This guide explains how to utilize multiple GPUs and multiple nodes for machine
learning applications on CSC's supercomputers. It is part of our [Machine
learning guide](ml-guide.md).

First we will explain the general principles, such as single- and
multi-node jobs and mechanisms for launching multiple processes. After
that we discuss some common software frameworks how to use them on
CSC's supercomputers.

## Nodes and tasks

### GPU Nodes

Each separate GPU computer, or GPU **node**, has a small number of
GPUs. Puhti and Mahti have 4 GPUs per node, and LUMI has 8 GPUs. The
supercomputer may have tens or even thousands of GPU nodes. See
[GPU-accelerated machine learning](gpu-ml.md) for more details, in
particular the table of GPUs in CSC's different supercomputers might
be of interest.  If you need 1-4 GPUs (or 1-8 in LUMI) you should
always reserve a **single node job**. If you need more than 4 GPUs (or
8 in LUMI) you need to reserve a **multi-node job**.

### MPI tasks

When parallelizing to multiple GPUs it is common to allocate a
separate CPU process for handling the communication to each GPU. This
per GPU task division may be handled by the program itself, for
example using [Python's multiprocessing
library](https://docs.python.org/3/library/multiprocessing.html) to
launch separate processes, or one can use Slurm's MPI facility to
launch **multiple MPI tasks**. Whether MPI tasks are used or not
depends on the software framework used.

### Slurm examples

Below are Slurm batch script examples for launching single- or multi-node jobs, with or without MPI.

!!! warning "Note"
    
    Please make sure that your code can actually take advantage of multiple GPUs as
    this typically requires some changes to the program. **Simply reserving more GPUs
    isn't enough!**
    
You can [monitor that your program is using all the reserved GPUs
efficiently](gpu-ml.md#gpu-utilization) with the same mechanisms described in
our GPU-accelerated machine learning guide. The only difference is that you
should now see statistics for more than one GPU.


#### Single node run using 2 GPUs, no MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=20
    #SBATCH --mem=64G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:2
        
    srun python3 myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=10
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:2
    
    srun python3 myprog.py <options>
    ```
    
    Note that on Mahti, the maximum for the `gpusmall` partition is 2
    GPUs. For 3 or 4 GPUs or more you need to use the `gpumedium`
    partition.

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=16
    #SBATCH --gpus-per-task=2
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 myprog.py <options>
    ```

The example above can be easily changed to more than 2 GPUs by
changing the number specified in the `--gres` option (Puhti and Mahti)
or `--gpus-per-task` option (LUMI). The maximum for a single node job
is 4 GPUs or 8 (LUMI).

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
    #SBATCH --cpus-per-task=10
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=8
    #SBATCH --gpus-per-task=1
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 myprog.py <options>
    ```


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
    #SBATCH --cpus-per-task=40
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=64
    #SBATCH --gpus-per-task=8
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 myprog.py <options>
    ```


#### Multi-node with 2 full nodes, using MPI

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=64G
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
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=10
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    srun python3 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=8
    #SBATCH --gpus-per-task=1
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 myprog.py <options>
    ```


## Available frameworks

There are many frameworks for doing multi-GPU and multi-node
computing. Some frameworks are tightly coupled to a specific machine
learning framework, such as PyTorch `DistributedDataParallel`,
DeepSpeed or TensorFlow's `tf.distribute.Strategy`, while others are
more general like Horovod.

Independent of which framework you pick, pay attention to what
approach is used to launch the jobs. For example Horovod always uses
MPI, while DeepSpeed can be configured to use MPI or its own parallel
launcher.

In many frameworks, the launching mechanism may also vary depending on
if you are running a single- or multi-node job. All frameworks should
use
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
examples found online can often be out-of-date.

To make usage of DDP on CSC's supercomputers easier, we have created a
[set of examples on how to run simple DDP jobs in the
cluster](https://github.com/CSCfi/pytorch-ddp-examples). In the
examples we use the
[rendezvous](https://pytorch.org/docs/stable/elastic/rendezvous.html)
mechanism to communcate across nodes, not MPI.

Example of running PyTorch DDP on a single full node:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module load pytorch
    
    srun python3 -m torch.distributed.run --standalone --nnodes=1 --nproc_per_node=4 \
        myprog.py <options>
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    module load pytorch

    srun python3 -m torch.distributed.run --standalone --nnodes=1 --nproc_per_node=4 \
        myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=128
    #SBATCH --gpus-per-task=8
    #SBATCH --time=1:00:00

    module use /projappl/project_462000007/ai/modulefiles/
    module load pytorch

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    srun python3 -m torch.distributed.run --standalone --nnodes=1 --nproc_per_node=8 \
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
    #SBATCH --cpus-per-task=40
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400
    
    module load pytorch

    srun python3 -m torch.distributed.run \
        --nnodes=$SLURM_JOB_NUM_NODES \
        --nproc_per_node=4 \
        --rdzv_id=$SLURM_JOB_ID \
        --rdzv_backend=c10d \
        --rdzv_endpoint="$RDZV_HOST:$RDZV_PORT" \
        myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=eap
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --gpus-per-task=8
    #SBATCH --time=1:00:00
    
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400

    module use /projappl/project_462000007/ai/modulefiles/
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

1. Initialize with `dist.init_process_group()`, for example:

    ```python
    import torch.distributed as dist
    import os

    local_rank = int(os.environ['LOCAL_RANK'])

    dist.init_process_group(backend='nccl')
    world_size = dist.get_world_size()
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


A fully working example can be found in our [`pytorch-ddp-examples`
repository](https://github.com/CSCfi/pytorch-ddp-examples):

- [run-gpu4-benchmark-ddp-puhti.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-gpu4-benchmark-ddp-puhti.sh) shows a benchmark run (including copying of a training set to NVME) on
Puhti with a full node of 4 GPUs
- [run-gpu8-benchmark-ddp-puhti.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-gpu8-benchmark-ddp-puhti.sh) shows the same for two full nodes
- [benchmark_ddp.py](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/benchmark_ddp.py) shows the Python code for the actual benchmark run utilizing DDP.




### DeepSpeed

[DeepSpeed](https://www.deepspeed.ai/) is an optimization software
suite for PyTorch that helps with scaling training and inference for
large deep learning models. DeepSpeed is supported in the newest
`pytorch` modules in Puhti and Mahti.

Example of running DeepSpeed on a single full node using the
`deepspeed` launcher:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
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
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4

    module load pytorch

    srun singularity_wrapper exec deepspeed myprog.py \
        --deepspeed --deepspeed_config my_ds_config.json \
        <further options>
    ```

Example of running DeepSpeed on 2 full nodes using MPI for launching a
task for each GPU:

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
    #SBATCH --cpus-per-task=10
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:4
    
    module load pytorch

    srun python3 myprog.py \
        --deepspeed --deepspeed_config my_ds_config.json \
        <further options>
    ```

If you are converting an old PyTorch script there are a few steps that you need to do:

1. Initialize distributed environment, for example:

    ```python
    import deepspeed

    deepspeed.init_distributed()
    ```
    
2. Initialize DeepSpeed engine:

    ```python
    model_engine, optimizer, train_loader, __ = deepspeed.initialize(
        args=args, model=model, model_parameters=model.parameters(),
        training_data=train_dataset)
    ```
    
3. Modify training loop to use the DeepSpeed engine:

    ```python
    data = data[0].to(model_engine.local_rank)
    labels = data[1].to(model_engine.local_rank)

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
    
A fully working example can be found in our
[`pytorch-ddp-examples`
repository](https://github.com/CSCfi/pytorch-ddp-examples):

- [run-gpu4-benchmark-deepspeed.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-gpu4-benchmark-deepspeed.sh) shows a benchmark run (including copying of a training set to NVME) on
Mahti with a full node of 4 GPUs
- [run-gpu8-benchmark-deepspeed.sh](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/run-gpu8-benchmark-deepspeed.sh) shows the same for two full nodes
- [benchmark_deepspeed.py](https://github.com/CSCfi/pytorch-ddp-examples/blob/master/benchmark_deepspeed.py) shows the Python code for the actual benchmark run utilizing DeepSpeed.


### Horovod

[Horovod](https://horovod.ai/) is a general framework that supports
PyTorch and TensorFlow among other frameworks. Horovod always uses MPI
for launching jobs.  Horovod can be used both with single- and
multi-node jobs.

In CSC's supercomputers Horovod is supported only for some specific
versions of [TensorFlow](../../apps/tensorflow.md) and
[PyTorch](../../apps/pytorch.md).  Please check the application pages
for further information. To take Horovod into use, just load the
appropriate module, and modify your program according to the
instructions in [Horovod's
documentation](https://horovod.readthedocs.io/), for example:

* [Horovod with PyTorch](https://horovod.readthedocs.io/en/latest/pytorch.html)
* [Horovod with TensorFlow](https://horovod.readthedocs.io/en/stable/tensorflow.html) and [Keras](https://horovod.readthedocs.io/en/stable/keras.html)


### TensorFlow's `tf.distribute.Strategy`

TensorFlow also has its own [built-in mechanisms for distributed
training](https://www.tensorflow.org/guide/distributed_training) in
the [`tf.distribute.Strategy`
API](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy).



