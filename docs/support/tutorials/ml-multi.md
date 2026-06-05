# Multi-GPU and multi-node machine learning

This guide explains how to utilize multiple GPUs and multiple nodes
for machine learning applications on CSC's supercomputers. It is part
of our [Machine learning guide](ml-guide.md).

First we will explain the general principles, such as single- and
multi-node jobs and mechanisms for launching multiple processes. After
that we discuss some common software frameworks how to use them on
CSC's supercomputers: [PyTorch DDP](#pytorch-ddp),
[DeepSpeed](#deepspeed) and briefly [Horovod](#horovod) and
[TensorFlow's
`tf.distribute.Strategy`](#tensorflows-tfdistributestrategy).

## Multiple GPUs and multiple nodes

Each separate GPU node (i.e., a single computer in the cluster), has a
fixed number of GPUs. Puhti, Mahti and Roihu have 4 GPUs per node, and
LUMI has 8 GPUs per node.  (Technically a LUMI node has 4 dual-chip
GPU cards, but from the software point-of-view this looks the same as 8
GPUs.) The entire supercomputer may have tens or even thousands of GPU
nodes. See [GPU-accelerated machine learning](gpu-ml.md) for more
details.

If you need 1-4 GPUs (or 1-8 in LUMI) you should always reserve a
**single node job**. If you need more than 4 GPUs (or 8 in LUMI) you
need to reserve a **multi-node job**. While it is technically possible
to reserve, e.g., two GPUs in one node and two in another, this is not
recommended except for testing purposes, as the communication across
nodes is always slower than inside a node.

To reserve a single node with N=1-4 GPUs on Puhti, Mahti or 1-8 GPUs
on LUMI you need the following options (**change N for the actual
number of GPUs**):

=== "Puhti"

    ```bash
    #SBATCH --partition=gpu
    #SBATCH --gres=gpu:v100:N
    ```

=== "Mahti"

    ```bash
    #SBATCH --partition=gpusmall 
    #SBATCH --gres=gpu:a100:N
    ```

    Note: on Mahti use `gpusmall` partition for 1 or 2 GPUs, `gpumedium`
    for 3 or 4 GPUs.

=== "LUMI"

    ```bash
    #SBATCH --partition=small-g
    #SBATCH --gpus-per-node=N
    ```

    Note: on LUMI, you can use `standard-g` partition if you ask for the full node (8 GPUs).


For multi-node jobs you always reserve full nodes, so you will have a
multiple of 4 GPUs (or 8 in LUMI). For example with two nodes on
Mahti, you'll have 2*4=8 GPUs.

=== "Puhti"

    ```bash
    #SBATCH --partition=gpu
    #SBATCH --gres=gpu:v100:4
    #SBATCH --nodes=2
    ```

=== "Mahti"

    ```bash
    #SBATCH --partition=gpumedium
    #SBATCH --gres=gpu:a100:4
    #SBATCH --nodes=2
    ```

=== "LUMI"

    ```bash
    #SBATCH --partition=standard-g
    #SBATCH --gpus-per-node=8
    #SBATCH --nodes=2
    ```

Note that the `--gres` (or `--gpus-per-node` on LUMI) option always
specifies the number of GPUs *per node*, even in the multi-node
case. So if we are reserving 8 GPUs across 2 nodes in Puhti, that is 4
GPUs on each node, i.e, `--gres=gpu:v100:4`.


### Allocation of non-GPU resources

The other resources (CPU cores and CPU memory) should be reserved
according to the proportion of GPUs reserved in the node. For example
if you reserve 1 GPU out of 4, the other resources should be reserved
(at most) to 1/4 of the total resource of the node.

In Puhti this amounts to 10 CPU cores and roughly 95G of memory (for
memory we round down a bit as the units are not so exact). On Mahti
the maximum is 32 CPU cores, the memory should be automatically
allocated.

On [LUMI use a maximum of 7 CPU cores and 60GB per reserved
GPU](https://lumi-supercomputer.github.io/LUMI-training-materials/User-Updates/Update-202308/responsible-use/#core-and-memory-use-on-small-g-and-dev-g).


Note that the GPU memory is fixed according to the number of GPUs, you
cannot allocate more (or less) of this.


## Monitoring GPU utilization

!!! warning "Note"
    
    Please make sure that your code can actually take advantage of multiple GPUs as
    this typically requires some changes to the program. **Simply reserving more GPUs
    is not enough!**
    
You can [monitor that your program is using all the reserved
GPUs](gpu-ml.md#gpu-utilization) with the same mechanisms described in
our GPU-accelerated machine learning guide. The only difference is
that you should now see statistics for more than one GPU.

Example output using `nvidia-smi` for a 2 GPU job on Puhti (single node):

```
Tue Mar 17 13:36:42 2026       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.288.01             Driver Version: 535.288.01   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Tesla V100-SXM2-32GB           On  | 00000000:61:00.0 Off |                    0 |
| N/A   44C    P0             259W / 300W |   3973MiB / 32768MiB |     97%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
|   1  Tesla V100-SXM2-32GB           On  | 00000000:62:00.0 Off |                    0 |
| N/A   43C    P0             257W / 300W |   3973MiB / 32768MiB |     98%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A   2047858      C   ...oft/ai/wrap/pytorch-2.9/bin/python3     3968MiB |
|    1   N/A  N/A   2047859      C   ...oft/ai/wrap/pytorch-2.9/bin/python3     3968MiB |
+---------------------------------------------------------------------------------------+
```

Here we have two CPU processes, each using a GPU close to 100%
utilization (GPU-Util column). If either GPU instead shows 0% it is
not used at all. If the GPUs show rather low percentages, it might
mean that you don't need multiple GPUs at least for the computational
power. For large language models, you might need them for the GPU
memory however, so check also the GPU memory usage (Memory-Usage column).

## Launching multiple processes

The typical approach in multi-GPU processing in deep learning is to
launch one _CPU_ control process for each GPU. Launching these
processes may be handled either by the deep learning framework itself
(such as with PyTorch's `torchrun`) or by using Slurm's MPI facility
to launch **multiple MPI tasks**.

## Available frameworks

There are many frameworks for doing multi-GPU and multi-node machine
learning. Some frameworks are tightly coupled to a specific framework,
such as PyTorch `DistributedDataParallel` (DDP), DeepSpeed or
TensorFlow's `tf.distribute.Strategy`, while others are more general,
for example Horovod.

Independent of which framework you pick, pay attention to the approach
used to launch jobs. For example with Horovod it is common to use MPI,
while DeepSpeed can be configured to use MPI or its own parallel
launcher. In some frameworks, the launching mechanism may also vary
depending on if you are running a single- or multi-node job.

All frameworks should use
[NCCL](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html)
(NVIDIA) or [RCCL](https://github.com/ROCmSoftwarePlatform/rccl) (AMD)
for fast inter-GPU communication, even if MPI is used to set up the
connections.


### PyTorch DDP

[PyTorch
distributed](https://pytorch.org/tutorials/beginner/dist_overview.html),
and in particular `DistributedDataParallel` (DDP), offers a nice way
of running multi-GPU and multi-node PyTorch jobs.


Hence, to make usage
of DDP on CSC's supercomputers easier, we have created a [set of
examples on how to run simple DDP jobs in the
cluster](https://github.com/CSCfi/pytorch-ddp-examples). In the
examples we use the
[rendezvous](https://pytorch.org/docs/stable/elastic/rendezvous.html)
mechanism to set up communications across nodes, not MPI.

Example Slurm batch job for running PyTorch DDP on a single full node:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch
    
    srun torchrun --standalone --nnodes=1 --nproc_per_node=4 myprog.py <options>
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

    srun torchrun --standalone --nnodes=1 --nproc_per_node=4 myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=56
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    module purge
    module use /appl/local/laifs/modules
    module load lumi-aif-singularity-bindings
    
    export SIF=/appl/local/laifs/containers/lumi-multitorch-latest.sif

    srun singularity run $SIF \
      torchrun --standalone --nnodes=1 --nproc_per_node=$SLURM_GPUS_PER_NODE myprog.py <options>
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
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400
    
    module purge
    module load pytorch

    srun torchrun \
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

    srun torchrun \
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
    #SBATCH --partition=small-g
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=56
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    export RDZV_HOST=$(hostname)
    export RDZV_PORT=29400
    
    module purge
    module use /appl/local/laifs/modules
    module load lumi-aif-singularity-bindings

    export SIF=/appl/local/laifs/containers/lumi-multitorch-latest.sif

    srun singularity run $SIF torchrun \
        --nnodes=$SLURM_JOB_NUM_NODES \
        --nproc_per_node=$SLURM_GPUS_PER_NODE \
        --rdzv_id=$SLURM_JOB_ID \
        --rdzv_backend=c10d \
        --rdzv_endpoint="$RDZV_HOST:$RDZV_PORT" \
        myprog.py <options>
    ```

The LUMI examples are using the [LUMI AI Factory PyTorch
installation](https://docs.lumi-supercomputer.eu/laif/software/ai-environment/).

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


### PyTorch Lightning with DDP

[PyTorch Lightning](https://lightning.ai/) is a popular higher-level
framework designed to make using PyTorch easier. Running multi-GPU and
multi-node jobs with Lightning is quite easy. If you wish to convert
your existing PyTorch script to Lightning, we will refer you to the
[official PyTorch Lightning
documentation](https://lightning.ai/docs/pytorch/stable/).


We recommend using DistributedDataParallel (DDP) for multi-GPU and
multi-node usage. You just need to add these options to your Lightning
Trainer:

```python
trainer = pl.Trainer(devices=args.gpus,
                     num_nodes=args.nodes,
                     accelerator='gpu',
                     strategy='ddp',
                     ...)
```

You need to give appropriate values for `devices` (number of GPUs *per
node*) and `num_nodes`. We suggest giving these are command line arguments:

```python
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--gpus', default=1, type=int,
                        help='number of GPUs per node')
    parser.add_argument('--nodes', default=1, type=int,
                        help='number of nodes')
    # any other command line arguments here
    args = parser.parse_args()
```

PyTorch Lightning Slurm script for single node using all GPUs:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch

    srun python3 myprog.py --gpus=4 --nodes=1 <options>
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

    module purge
    module load pytorch
    
    srun python3 myprog.py --gpus=4 --nodes=1 <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00

    module purge
    module use /appl/local/laifs/modules
    module load lumi-aif-singularity-bindings
    
    export SIF=/appl/local/laifs/containers/lumi-multitorch-latest.sif

    srun singularity run $SIF \
      python3 myprog.py --gpus=8 --nodes=1 <options>
    ```

<br/>
PyTorch Lightning Slurm script for two full nodes using all GPUs:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch
    
    srun python3 myprog.py --gpus=4 --nodes=2 <options>
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

    srun python3 myprog.py --gpus=4 --nodes=2 <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00

    module purge
    module use /appl/local/laifs/modules
    module load lumi-aif-singularity-bindings
    
    export SIF=/appl/local/laifs/containers/lumi-multitorch-latest.sif

    srun singularity run $SIF \
      python3 myprog.py --gpus=8 --nodes=2 <options>
    ```


### Accelerate

Hugging Face's
[Accelerate](https://huggingface.co/docs/transformers/accelerate) is a
popular framework for large language model training, and it makes
using more advanced training algorithms like FSDP very easy. Launching
a job with accelerate it similar to PyTorch DDP, except we need to use
the accelerate launcher and also provide an Accelerate config file.

A working [example for LLM fine-tuning can be found in this GitHub
repository](https://github.com/CSCfi/llm-fine-tuning-examples)
(check the files ending with `-accelerate.sh`). Also check our [guide
on using LLMs on supercomputers](ml-llm.md).

Example using Accelerate on all GPUs on a single node:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch

    srun accelerate launch \
     --config_file=accelerate_config.yaml \
     --num_processes=4 \
     --num_machines=1 \
     --machine_rank=0 \
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

    srun accelerate launch \
     --config_file=accelerate_config.yaml \
     --num_processes=4 \
     --num_machines=1 \
     --machine_rank=0 \
     myprog.py <options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=56
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    #SBATCH --gpus-per-node=8

    module purge
    module use /appl/local/laifs/modules
    module load lumi-aif-singularity-bindings
    
    export SIF=/appl/local/laifs/containers/lumi-multitorch-latest.sif

    srun singularity run $SIF accelerate launch \
     --config_file=accelerate_config.yaml \
     --num_processes=8 \
     --num_machines=1 \
     --machine_rank=0 \
     myprog.py <options>
    ```


Example of running Accelerate on 2 full nodes (8 GPUs).

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch

    GPUS_PER_NODE=4
    NUM_PROCESSES=$(expr $SLURM_NNODES \* $GPUS_PER_NODE)
    MAIN_PROCESS_IP=$(hostname -i)
    
    RUN_CMD="accelerate launch \
                        --config_file=accelerate_config.yaml \
                        --num_processes=$NUM_PROCESSES \
                        --num_machines=$SLURM_NNODES \
                        --machine_rank=\$SLURM_NODEID \
                        --main_process_ip=$MAIN_PROCESS_IP \
                        myprog.py <options>"
    
    srun bash -c "$RUN_CMD"
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
    
    module purge
    module load pytorch

    GPUS_PER_NODE=4
    NUM_PROCESSES=$(expr $SLURM_NNODES \* $GPUS_PER_NODE)
    MAIN_PROCESS_IP=$(hostname -i)
    
    RUN_CMD="accelerate launch \
                        --config_file=accelerate_config.yaml \
                        --num_processes=$NUM_PROCESSES \
                        --num_machines=$SLURM_NNODES \
                        --machine_rank=\$SLURM_NODEID \
                        --main_process_ip=$MAIN_PROCESS_IP \
                        myprog.py <options>"
    
    srun bash -c "$RUN_CMD"
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=56
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00
    
    module purge
    module use /appl/local/laifs/modules
    module load lumi-aif-singularity-bindings
    
    export SIF=/appl/local/laifs/containers/lumi-multitorch-latest.sif

    NUM_PROCESSES=$(expr $SLURM_NNODES \* $SLURM_GPUS_PER_NODE)
    MAIN_PROCESS_IP=$(hostname -i)
    
    RUN_CMD="accelerate launch \
                        --config_file=accelerate_config.yaml \
                        --num_processes=$NUM_PROCESSES \
                        --num_machines=$SLURM_NNODES \
                        --machine_rank=\$SLURM_NODEID \
                        --main_process_ip=$MAIN_PROCESS_IP \
                        myprog.py <options>"
    
    srun singularity run $SIF bash -c "$RUN_CMD"
    ```


Note the somewhat cumbersome way of defining the command with the
`$SLURM_NODEID` variable escaped so that is only evaluated on the
actual node where it is running. Normally all the variables are
evaluated on the first node, but `$SLURM_NODEID` should be different
on each node to get the distributed setup working correctly.


Both examples use this `accelerate_config.yaml` file:

```yaml
compute_environment: LOCAL_MACHINE
debug: false
distributed_type: MULTI_GPU
downcast_bf16: 'no'
gpu_ids: all
main_training_function: main
main_process_port: 29500
mixed_precision: bf16
num_processes: 1
rdzv_backend: static
same_network: true
tpu_env: []
tpu_use_cluster: false
tpu_use_sudo: false
use_cpu: false
```


If you want to use FSDP, simply use an Accelerate config similar to this:

```yaml
compute_environment: LOCAL_MACHINE
debug: false
distributed_type: FSDP
downcast_bf16: 'no'
fsdp_config:
  fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
  fsdp_backward_prefetch_policy: BACKWARD_PRE
  fsdp_forward_prefetch: false
  fsdp_cpu_ram_efficient_loading: true
  fsdp_offload_params: false
  fsdp_sharding_strategy: FULL_SHARD
  fsdp_state_dict_type: SHARDED_STATE_DICT
  fsdp_sync_module_states: true
  fsdp_use_orig_params: true
gpu_ids: all
main_training_function: main
main_process_port: 29500
mixed_precision: bf16
num_processes: 1
rdzv_backend: static
same_network: true
tpu_env: []
tpu_use_cluster: false
tpu_use_sudo: false
use_cpu: false
```

See our [GitHub repository for more
examples](https://github.com/CSCfi/llm-fine-tuning-examples).



### DeepSpeed

[DeepSpeed](https://www.deepspeed.ai/) is an optimization software
suite for PyTorch that helps in scaling both training and inference
for large deep learning models.

Example of running DeepSpeed on a single full node using the
`deepspeed` launcher:

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=320G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:4
    
    module purge
    module load pytorch
    
    srun apptainer_wrapper exec deepspeed myprog.py \
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

    srun apptainer_wrapper exec deepspeed myprog.py \
        --deepspeed --deepspeed_config my_ds_config.json \
        <further options>
    ```

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=56
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00

    module purge
    module use /appl/local/laifs/modules
    module load lumi-aif-singularity-bindings
    
    export SIF=/appl/local/laifs/containers/lumi-multitorch-latest.sif

    srun singularity run $SIF \
      deepspeed myprog.py \
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
    #SBATCH --mem=320G
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

=== "LUMI"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=8
    #SBATCH --mem=480G
    #SBATCH --time=1:00:00

    module purge
    module use /appl/local/laifs/modules
    module load lumi-aif-singularity-bindings
    
    export SIF=/appl/local/laifs/containers/lumi-multitorch-latest.sif

    srun singularity run $SIF python3 myprog.py \
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



