# Working with large language models on supercomputers

This guide gives some examples and hints on how to work with large
language models (LLMs) on CSC's supercomputers.

## LLMs and GPU memory

If you are doing inference (using a model, rather than training), you
can in some cases do without a GPU, for example if the model is small
enough or has been reduced by quantization. However, in most other
cases you will need to use a GPU.

In order to use an LLM (or any neural network) with a GPU, the model
needs to be loaded into the GPU memory (VRAM). LLMs can be very large
and here the size of the GPU memory becomes critical. You can refer to
[our table of GPU stats](gpu-ml.md#puhti-mahti-or-lumi) for the full
details, but our GPUs have VRAM memory as follows:

- 32 GB on Puhti (NVIDIA V100)
- 40 GB on Mahti (NVIDIA A100)
- 64 GB on LUMI (single GCD of an AMD MI250x)

The model size in memory depends on how the weights are
stored. Typically a regular floating point value in a computer is
stored in a format called fp32, which uses 32 bits of memory, or 4
bytes (remember 8 bits = 1 byte). In deep learning, 16 bit floating
point formats (fp16 of bf16) have been used for a long time to speed
up part of the computation. These use 2 bytes of memory per
weight. Recently, as model sizes have grown, even lower-precision
formats, going down to 8 or even 4 bits, have become more
common. Common quantization methods include
[GPTQ](https://arxiv.org/abs/2210.17323),
[SpQR](https://arxiv.org/abs/2306.03078) and
[GGML/GGUF](https://huggingface.co/docs/hub/en/gguf). If you are
unfamiliar with quantization, see for example [this online guide on
quantization for
LLMs](https://www.datacamp.com/tutorial/quantization-for-large-language-models).

The model size in memory is then the number of parameters times the
number of bytes needed for storing a single weight. For example a 30
billion parameter model with fp16 takes up 60 GB of memory. In
practice [for inference there's up to 20% overhead][1] so you might
actually need around 70 GB of memory, and thus even a single GCD in
LUMI might not be enough for our example model. If you would instead
store that model with 4 bit quantization, it would be about 0.5 bytes
per parameter, so around 15 GB for our example (or around 18 GB with
overhead).

For training a lot more memory is needed as not only the model, but
also the optimizer states, gradients and activations need to be
stored. As a *very* rough estimate, around 4-6x the model size (in GB)
is needed for fine-tuning a model, but this depends a lot on the
details. So for our example 30B parameter fp16 model, it might require
60 GB x 6 = 360 GB of GPU memory for training! We'll discuss ways to
solve this problem in the sections below. See the [Transformer Math
101 blog post by EleutherAI for more details][1].

## Fine-tuning LLMs

We have a [git repository with some example scripts for doing LLM
fine-tuning on Puhti, Mahti or LUMI][2]. The example uses the [Hugging
Face (HF) libraries][3] and in particular the HF Trainer to train a
given model (taken from the HF model repositories) with the IMDb movie
review dataset. The task itself might not make much sense, it's just
used to demonstrate the technical task of fine-tuning a model with a
given dataset.

The examples, by default, use the [EleutherAI/gpt-neo-1.3B][4] model,
as it will fit into the memory of a single GPU in Puhti. Given that
it's a 1.37 billion parameter model with 32 bit weights, according to
our rule-of-thumb, mentioned above, it might require up to 1.37x4x6 =
32 GB of memory for training, so it should just fit into the 32 GB
maximum of Puhti's V100 (if we're lucky).

The repository has basic launch scripts for Puhti, Mahti and LUMI for
a single GPU, a full node (4 GPUs or Puhti/Mahti and 8 GPUs on LUMI)
and two full nodes (8 respectively 16 GPUs). The Slurm scripts are
essentially the same as for any PyTorch DDP runs, see our [Multi-GPU
and multi-node ML guide](ml-multi.md#pytorch-ddp) for examples, or
just take a look at [the scripts in the GitHub repository][2]:

- [`run-finetuning-puhti-gpu1.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu1.sh) - fine-tuning on Puhti with 1 GPU
- [`run-finetuning-puhti-gpu4.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu4.sh) - fine-tuning on Puhti with one full node (4 GPUs)
- [`run-finetuning-puhti-gpu8.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu8.sh) - fine-tuning on Puhti with two full nodes (8 GPUs in total)

(The repository also has scripts for Mahti and LUMI if you check the
[file listing][2].)

The basic multi-GPU versions are all using PyTorch Distributed Data
Parallel (DDP) mode, in which each GPU has a full copy of the
model. Only the training data is distributed across the different
GPUs. This means that the full model must fit into a single GPU.

If your model doesn't fit into a single GPU on Puhti, it might work on
Mahti or LUMI, but first check with the rule-of-thumb calculation
mentioned above if there's even a chance of that! If not, read on for
PEFT and FSDP approaches.

### Using PEFT and LoRA

If your model would fit into the GPU memory, it is still possible that
all the extra memory needed by the overhead of the fine-tuning process
will not fit (you will notice this quickly as the program crashes with
a CUDA or ROCm out-of-memory error!). Then the solution may be to use
the [Parameter Efficient Fine-Tuning (PEFT)][5] library which trains a
smaller number of extra parameters, which reduces the training
overhead a substantially. PEFT supports many methods including
[LoRA](https://arxiv.org/abs/2106.09685) and
[QLoRA](https://arxiv.org/abs/2305.14314).

PEFT will typically have about 10% of the original number of
parameters, but the amount of GPU memory saved varies depending on the
situation. We have seen savings from 5% to 60%.

PEFT is very easy to enable, see the [PEFT quicktour][6] for an
example. PEFT can be enabled in the example above simply by adding the
flag `--peft`. It might pay to [dig a bit deeper into the best
parameters for using LoRA for example][8].


### Using Accelerate and FSDP

For larger models that do not fit into the GPU memory (even for
inference), you need to use an approach that splits the actual model
(and the training overhead) over multiple GPUs. We can no longer
retain a full copy of the model in each GPU.

A good approach, which is supported natively in PyTorch is [Fully
Sharded Data Parallel (FSDP)][7]. In FSDP the model parameters,
gradients and optimizer states are not stored completely in each GPU,
but are split up (sharded) between all GPUs and only gathered together
as needed in the current stage of the training.

Perhaps the easiest way to take FSDP into use for large language models
is to use Hugging Face's Accelerate framework. No changes are needed
to the PyTorch script, one only needs to change to the `accelerate`
launcher. [Our GitHub repository][2] has example scripts for launching
on one or two full nodes on Puhti:

- [`run-finetuning-puhti-gpu4-accelerate.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu4-accelerate.sh) - fine-tuning on Puhti with one full node using Accelerate
- [`run-finetuning-puhti-gpu8-accelerate.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu8-accelerate.sh) - fine-tuning on Puhti with two full nodes using Accelerate

(The repository also has scripts for Mahti and LUMI if you check the
[file listing][2].)

Our [Multi-GPU and multi-node ML guide](ml-multi.md#accelerate) also
has Slurm script examples for using Accelerate with FSDP.

There are two things to note when using Accelerate: 

1. The `accelerate` launcher expects to have a configuration YAML
   file. We have provided two examples in the GitHub repository,
   `accelerate_config.yaml` for a basic example and
   `accelerate_config_fsdp.yaml` for using FSDP. These configs use
   reasonable default parameters, but it might be useful to tweak
   those, especially [take a look at FSDP's parameters][9].

2. For multi-node runs you need to launch the `accelerate` launcher
   separately on each node with the `--machine_rank` argument set
   according to the rank of the node (0=first node, 1=second node
   etc). We can use the `$SLURM_NODEID` variable to set this, but we
   need to use a shell trick so that it isn't evaluated until it
   actually runs in the specific node. (See the script
   [`run-finetuning-puhti-gpu8-accelerate.sh`](https://github.com/CSCfi/llm-fine-tuning-examples/blob/master/run-finetuning-puhti-gpu8-accelerate.sh)
   for an example of how this can be done.)

You can also use PEFT (LoRA) with Accelerate with the `--peft` in our
example script.

### Alternative trainers

An alternative to the standard Hugging Face Trainer for fine-tuning
LLMs is the
[SFTTrainer](https://huggingface.co/docs/trl/main/en/sft_trainer) from
the [TRL](https://huggingface.co/docs/trl/index) library. These are
not covered in this guide. We recommend checking for example [this
fine-tuning guide from Hugging
Face](https://huggingface.co/blog/mlabonne/sft-llama3), which also
covers the [Unsloth library](https://github.com/unslothai/unsloth).


## Quantization

Quantization is a process that converts the weights and activations within an LLM from high-precision values, such as 32-bit floating-point, to lower-precision ones, such as an 8-bit integer. This leads to a significant decrease in overall model size, leading to smaller memory needs with a slight drop in accuracy.

Quantization can be done during inference or training phase. Post-Training Quantization (PTQ) involves quantizing a pre-trained model during the inference phase. Quantization-Aware Training (QAT) is applied during training to simulate the effects of quantization, resulting in a model more robust to quantization noise. You can learn more about quantization for example in [this tutorial](https://www.datacamp.com/tutorial/quantization-for-large-language-models).

It can take hours to quantize very large models, but luckily many models already have a quantized version available, for example in Hugging Face. You can look for quantized models by a suffix in the model name indicating a quantization method, such as **AWQ, GPTQ, or GGUF**, or alternatively, model precision, such as **8bit** or **4bit**.

### Using BitsandBytes Quantization

The [BitsAndBytes library from Hugging Face Transformers] (https://huggingface.co/docs/transformers/en/quantization/bitsandbytes) offers runtime quantization, which compresses weights to 8-bit or 4-bit on-the-fly during inference to save memory.

```python
from transformers import BitsAndBytesConfig, AutoModelForCausalLM

bnb_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_quant_type="nf4",
   bnb_4bit_compute_dtype=torch.bfloat16,
   bnb_4bit_use_double_quant=True,
   bnb_4bit_quant_storage=torch.bfloat16,
)

model = AutoModelForCausalLM.from_pretrained(
   args.model,
   quantization_config=bnb_config,
   ...
)
```
You can use it in our fine-tuning LLMs example (see above) with the --4bit argument. Alternatively, see [our Github repository](link) for an example to quantize a model using bitsandbytes and running inference with the quantized model using Puhti, Mahti or LUMI.

### Using GPTQ Quantization

In addition to **bitsandbytes**, Hugging Face Transformers has also integrated [**Gradient Post-Training Quantization (GPTQ)**](https://huggingface.co/docs/transformers/en/quantization/gptq). 
GPTQ performs **row-wise quantization of weight matrices**, optimizing each row individually so that the quantized weights closely approximate the original values with minimal reconstruction error.  

Unlike runtime quantization libraries such as bitsandbytes, GPTQ performs a **one-time compression step** using a calibration dataset, resulting in a new quantized model that can be saved and loaded without requiring the original full-precision weights.

```python
from transformers import GPTQConfig, AutoModelForCausalLM

gptq_config = GPTQConfig(
    bits=4,               # Use 4-bit quantization
    dataset="c4",         # Calibration dataset
    group_size=128,       # Optional: grouped quantization
    sym=False,            # Optional: asymmetric quantization
)

model = AutoModelForCausalLM.from_pretrained(
    args.model,
    quantization_config=gptq_config,
    ...
)
```

GPTQ supports different backends for faster inference such as **Marlin** (optimized for A100) and **ExLlamaV2** (optimized for LLaMA models on consumer GPUs). To enable a specific backend, pass `backend="marlin"` or `exllama_config={"version": 2}` to `GPTQConfig`.

A [blog post by Hugging Face](https://huggingface.co/blog/overview-quantization-transformers) compares bitsandbytes and GPTQ features which can be helpful in deciding which one is more suitable for your use case. See also our [Github repository](link) for an example to quantize a model using GPTQ with Hugging Face Transformers on Puhti, Mahti or LUMI.

### Using GPTQ Quantization via LLM Compressor

There is another way you can do quantization using GPTQ modifier from [**LLM Compressor**](https://github.com/vllm-project/llm-compressor). LLM Compressor is a post-training compression toolkit for Hugging Face models. It applies a *recipe* (e.g., GPTQ quantization) to an already-trained model and saves a compressed checkpoint that loads back into `transformers`. At runtime, it swaps the model’s linear layers for compressed kernels so generation uses quantized matmuls without changing your inference code. GPTQModifier is the quantization recipe component that runs **GPTQ** and quantizes weights to for example W4A16 (4-bit weights, 16-bit activations) using a small calibration set and lets you quantize target layers (e.g., `Linear`) and ignore heads (e.g., `lm_head`) to preserve output quality. 

```python
from llmcompressor.entrypoints.oneshot import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier

# Define a GPTQ recipe: 4-bit weights (W4A16), target Linear layers, skip the LM head
recipe = GPTQModifier(targets="Linear", scheme="W4A16", ignore=["lm_head"])

# Apply GPTQ using a small calibration dataset (internally sampled by your script/flags)
oneshot(model=model, dataset="HuggingFaceH4/ultrachat_200k", recipe=recipe)
```
See an example to quantize a model using GPTQ via LLM Compressor on Puhti, Mahti or LUMI in [our Github repository](link).

### Using AWQ Quantization via LLM Compressor

Using the LLM Compressor library, you can also quantize a model with [**Activation-Aware Weight Quantization**](https://arxiv.org/pdf/2306.00978) (AWQ). AWQ observes that not all weights in an LLM contribute equally to model performance. By protecting only \~1% of the most salient weight channels, quantization error can be significantly reduced. These salient channels are identified based on activation distributions rather than raw weight values.

```python 
from llmcompressor.entrypoints.oneshot import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier

# Define AWQ recipe: 4-bit weights (W4A16_ASYM), target Linear layers, skip LM head
recipe = [AWQModifier(targets=["Linear"], scheme="W4A16_ASYM", ignore=["lm_head"])]

# Apply AWQ with a small calibration set (dataset can be your own or a public one)
oneshot(  
    model=model,  
    dataset="mit-han-lab/pile-val-backup",  # uses 'validation' split by default inside your script/flags
    recipe=recipe,
)
```
See an example to quantize a model using AWQ via LLM Compressor on Puhti, Mahti or LUMI in [our Github repository](link).

## Retrieval-augmented generation (RAG)

[Retrieval-augmented generation (RAG)][RAG] is a way of using a
pre-trained large language model together with the user's own dataset
without needing any computationally expensive fine-tuning or
retraining of the model.  In brief, this works by performing a search
on the dataset and using the top results as additional context for the
language model.

In RAG the search is a critical part of the system, as a failed search
will give the LLM the wrong context, which easily causes the LLM to
generate irrelevant information. For efficient search one can utilize
embedding models and fast vector search methods. See our [RAG-60K
repository][RAG-60K] for an example of how to utilize supercomputers
to prepare a Faiss vector store using state-of-the-art embedding
models.

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

### Inference with Ollama

[Ollama](https://ollama.com/) is a popular tool for using LLMs, as it
supports [several state-of-the-art models](https://ollama.com/library)
which can be accessed via an API. Ollama has been designed to run as a
service, and is thus not directly suited to running as a batch job on
supercomputers. However, it can be run as part of a batch job by
starting the service at the start of the job, and stopping when the
job ends.

First, you can install Ollama into your project folder like this:

```bash
cd /projappl/project_2001234  # replace with the appropriate path for you
mkdir ollama
cd ollama
wget https://ollama.com/download/ollama-linux-amd64.tgz
tar xzf ollama-linux-amd64.tgz
rm ollama-linux-amd64.tgz
```

On LUMI you have to do this additionally (in the same directory as
above). Note that with the additional ROCm files, the installation
takes 14 GB of disk space!

```bash
wget https://ollama.com/download/ollama-linux-amd64-rocm.tgz
tar xzf ollama-linux-amd64-rocm.tgz
rm ollama-linux-amd64-rocm.tgz
```

In your batch job you then just need to start the service with `ollama
serve`. After that your job can access the API in `localhost` at port
`11434`.  It's also a good idea to setup the environment variable
`OLLAMA_MODELS` to point to the project scratch, as it will otherwise
download huge model files to your home directory.  See our [example
Slurm script `run-ollama.sh` for running with Ollama][11].

The [`ai-inference-examples`][14] repository also has some examples of
running Ollama on a full node with 4 GPUs on Puhti and 8 GPUs on LUMI.

### Inference with vLLM

[vLLM][12] is another library for running LLM inference. vLLM supports
[offline batched inference][13] which is the mode most suitable for
running in a supercomputer. This runs just as a normal Python batch
job.

Here is a user-contributed example for processing a big dataset with
vLLM efficiently: <https://github.com/TurkuNLP/ECCO-ocr-large-run>.

In some situations there's still a need for an OpenAI-compatible
server, for example when interfacing with other programs. [Example
scripts for running vLLM on Puhti, Mahti and LUMI can be found in our
`ai-inference-examples` repository][14]. There's also an example of
running on multiple nodes using Ray.


[1]: https://blog.eleuther.ai/transformer-math/
[2]: https://github.com/CSCfi/llm-fine-tuning-examples
[3]: https://huggingface.co/docs/transformers/en/index
[4]: https://huggingface.co/EleutherAI/gpt-neo-1.3B
[5]: https://huggingface.co/docs/peft/index
[6]: https://huggingface.co/docs/peft/quicktour
[7]: https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/
[8]: https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms
[9]: https://huggingface.co/docs/transformers/fsdp
[10]: https://huggingface.co/docs/peft/en/accelerate/fsdp#the-important-parts
[11]: https://github.com/CSCfi/machine-learning-scripts/blob/master/slurm/run-ollama.sh
[12]: https://docs.vllm.ai/en/latest/
[13]: https://docs.vllm.ai/en/latest/getting_started/quickstart.html#offline-batched-inference
[14]: https://github.com/CSCfi/ai-inference-examples
[RAG]: https://en.wikipedia.org/wiki/Retrieval-augmented_generation
[RAG-60K]: https://github.com/CSCfi/RAG-60K/tree/main
