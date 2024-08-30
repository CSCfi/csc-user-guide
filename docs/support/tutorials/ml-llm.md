# Working with large language models on supercomputers

This guide gives some examples and hints on how to work with large
language models on CSC's supercomputers.

## GPUs and GPU memory

If you are doing inference (using a model, rather than training), you
can in some cases do without a GPU, for example if the model is small
enough or has been reduced by quantization. In most other cases you
will need to use a GPU.

In order to use an LLM (or any neural network) with a GPU, the model
needs to be loaded into the GPU memory (VRAM). LLMs can be very large
and here the size of the GPU memory becomes critical. You can refer to
[our table of GPU stats](gpu-ml.md#puhti-mahti-or-lumi) for the full
details, but our GPUs have VRAM memory as follows:

- 32 GB on Puhti (NVIDIA V100)
- 40 GB on Mahti (NVIDIA A100)
- 64 GB on LUMI (single GCD of an AMD MI250x)

The model size is the number of parameters times 2 bytes (for 16 bit
weights) or times 4 bytes (32 bit). For example a 30 billion parameter
model with fp16, takes up 60 GB of memory. In practice [for inference
there's up to 20% overhead][1] so you might need around 70 GB of
memory, and thus even a single GCD in LUMI might not be enough.

For training a lot more memory is needed as not only the model, but
also the optimizer states, gradients and activations need to be
stored. As a *very* rough estimate, around 5x the model size is needed
for fine-tuning a model, but this depends a lot on the details. We'll
discuss to ways to solve this problem in the sections below.

## Fine-tuning LLMs

We have a [git repository with some example scripts for doing LLM
fine-tuning on Puhti][2]. The example uses the [Hugging Face (HF)
libraries][3] and in particular the Hugging Face Trainer to train a
given model (taken from the HF model repositories) with the IMDb movie
review dataset. The task itself might not make much sense, but it's
just used to demonstrate the technical task of fine-tuning a model
with a given dataset.

The examples, by default, use the [EleutherAI/gpt-neo-1.3B][4] model,
as it will fit into the memory of a single GPU in Puhti. Given that
it's a 1.37 billion parameter model with 32 bit weights, according to
our rule-of-thumb, mentioned above, it would require 1.37*4*5 = 27.4
GB of memory for training which is less than the 32 GB maximum of
Puhti's V100.

The repository has basic launch scripts for Puhti for 1 GPU, 4 GPUs (a
full node) and 8 GPUs (two full nodes). The Slurm scripts are
essentially the same as for any PyTorch DDP runs, see our [Multi-GPU
and multi-node ML guide](ml-multi.md#pytorch-ddp) for examples, or
just take a look at [the scripts in the GitHub repository][2]:

- `run-finetuning-puhti-gpu1.sh` - fine-tuning on Puhti with 1 GPU
- `run-finetuning-puhti-gpu4.sh` - fine-tuning on Puhti with one full node (4 GPUs)
- `run-finetuning-puhti-gpu8.sh` - fine-tuning on Puhti with two full nodes (8 GPUs in total)

The basic multi-GPU versions are all using PyTorch Distributed Data
Parallel (DDP) mode, in which each GPU has a full copy of the
model. Only the training data is distributed across the different
GPUs. This means that the full model must fit into a single GPU.

### Using PEFT and LoRA

If your model would fit into the GPU memory, but cannot handle all the
extra memory needed by the overhead of the fine-tuning process, the
solution may be to use [Parameter Efficient Fine-Tuning (PEFT)][5]
which adaptively trains a smaller number of parameters, which reduces
the training overhead a substantially. PEFT is very easy to enable,
see the [PEFT quicktour][6]
for an example. PEFT can be enabled in the example above by adding the
flag `--peft`.

### Using Accelerate and FSDP

For larger models, that might not fit into the GPU memory or the
training overhead is too big for a single GPU, you need to use an
approach that splits the actual model (and related training
parameters) over multiple GPUs. We can no longer retain a full copy of
the model in each GPU.

One approach, which is supported natively by PyTorch is [Fully Sharded
Data Parallel (FSDP)][7]. In FSDP the model parameters, gradients and
optimizer states are not stored completely in each GPU, but are split
up (sharded) between all GPUs and only gathered together as needed in
the current stage of the training.

Perhaps to easiest way to take that into use is to use Hugging Face's
Accelerate framework. No changes are needed to the PyTorch script and
[the GitHub repository][2] has example scripts for launching on one or
two full nodes on Puhti:

- `run-finetuning-puhti-gpu4-accelerate.sh` - fine-tuning on Puhti with one full node using Accelerate
- `run-finetuning-puhti-gpu8-accelerate.sh` - fine-tuning on Puhti with two full nodes using Accelerate

Our [Multi-GPU and multi-node ML guide](ml-multi.md#accelerate) has
Slurm script examples for using Accelerate with FSDP.

[1]: https://blog.eleuther.ai/transformer-math/
[2]: https://github.com/mvsjober/fine-tuning-examples
[3]: https://huggingface.co/docs/transformers/en/index
[4]: https://huggingface.co/EleutherAI/gpt-neo-1.3B
[5]: https://huggingface.co/docs/peft/index
[6]: https://huggingface.co/docs/peft/quicktour
[7]: https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/

## Inference

Inference, that is using the model rather than training it, is usually
much simpler. Our [example git repository][2] has an inference example
in `inference-demo.py` and `run-inference-puhti.sh`. If your model
doesn't fit into a single GPU, you can simple reserve more GPUs and
then let Hugging Face sort it out by setting `device_map='auto'` when
loading the model, for example:

```python
model = AutoModelForCausalLM.from_pretrained(args.model, device_map='auto')
```
