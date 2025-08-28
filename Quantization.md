
# Quantization

Quantization is a process that converts the weights and activations within an LLM from high-precision values, such as 32-bit floating-point, to lower-precision ones, such as an 8-bit integer. This leads to a significant decrease in overall model size, leading to smaller memory needs with a slight drop in accuracy.

Quantization can be done during inference or training phase. **Post-Training Quantization (PTQ)** involves quantizing a pre-trained model during the inference phase. **Quantization-Aware Training (QAT)** is applied during training to simulate the effects of quantization, resulting in a model more robust to quantization noise.  
(Source: [Datacamp – Quantization for Large Language Models](https://www.datacamp.com/tutorial/quantization-for-large-language-models))

It can take hours to quantize very large models, but luckily many models already have a quantized version available, for example in Hugging Face. You can look for quantized models by a suffix in the model name indicating a quantization method, such as **AWQ, GPTQ, or GGUF**, or alternatively, model precision, such as **8bit** or **4bit**.

---

## Using quantization

Using the **bitsandbytes** library, you can also use 4-bit quantization.  
[Quantization has been integrated into Hugging Face Transformers as well](https://huggingface.co/blog/4bit-transformers-bitsandbytes).

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


## Using GPTQ Quantization

In addition to **bitsandbytes**, you can also use **Gradient Post-Training Quantization (GPTQ)**.  
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

A blog post by Hugging Face compares bitsandbytes and GPTQ features which can be helpful in deciding which one is more suitable for your use case. https://huggingface.co/blog/overview-quantization-transformers

Source: [https://huggingface.co/and adocs/transformers/en/quantization/gptq](https://huggingface.co/docs/transformers/en/quantization/gptq)  
[https://github.com/ModelCloud/GPTQModel/tree/main](https://github.com/ModelCloud/GPTQModel/tree/main)


## Using GPTQ via LLM Compressor


There is another way you can do quantization using GPTQ modifier from llmcompressor. **LLM Compressor** is a post-training compression toolkit for Hugging Face models. It applies a *recipe* (e.g., quantization) to an already-trained model and saves a compressed checkpoint that loads back into `transformers`. At runtime, it swaps the model’s linear layers for compressed kernels so generation uses quantized matmuls without changing your inference code. GPTQModifier is the quantization recipe component that runs **GPTQ** and quantizes weights to 4-bit (commonly W4A16: 4-bit weights, 16-bit activations) using a small calibration set and lets you quantize target layers (e.g., `Linear`) and ignore heads (e.g., `lm_head`) to preserve output quality. 

```python
# Load the base model 
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Define a GPTQ recipe: 4-bit weights (W4A16), target Linear layers, skip the LM head
recipe = GPTQModifier(targets="Linear", scheme="W4A16", ignore=["lm_head"])

# Apply GPTQ using a small calibration dataset (internally sampled by your script/flags)
oneshot(model=model, dataset="HuggingFaceH4/ultrachat_200k", recipe=recipe)

# Save the compressed checkpoint
save_dir = "Meta-Llama-3-8B-Instruct-W4A16-G128"
model.save_pretrained(save_dir, save_compressed=True) 
tokenizer.save_pretrained(save_dir)
```

## Using AWQ Quantization

Using the `llmcompressor` library, you can quantize a model with Activation-Aware Weight Quantization (AWQ). AWQ observes that not all weights in an LLM contribute equally to model performance. By protecting only \~1% of the most salient weight channels, quantization error can be significantly reduced. These salient channels are identified based on activation distributions rather than raw weight values. It selectively quantizes weights to 4-bit (commonly `W4A16_ASYM`: 4-bit weights, 16-bit activations, asymmetric quantization) by calibrating with sample activations and it allows you to quantize target layers (e.g., `Linear`) while ignoring sensitive ones (e.g., `lm_head`) to keep generation quality intact.

```python 
# Load model and tokenizer
MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)

# Define AWQ recipe: 4-bit weights (W4A16_ASYM), target Linear layers, skip LM head
recipe = [AWQModifier(targets=["Linear"], scheme="W4A16_ASYM", ignore=["lm_head"])]

# Apply AWQ with a small calibration set (dataset can be your own or a public one)
oneshot(  
    model=model,  
    dataset="mit-han-lab/pile-val-backup",  # uses 'validation' split by default inside your script/flags
    recipe=recipe,
)

# Save compressed checkpoint
SAVE_DIR = "Meta-Llama-3-8B-Instruct-awq-asym"
model.save_pretrained(SAVE_DIR, save_compressed=True)
tokenizer.save_pretrained(SAVE_DIR)
```
A practical example of how to implement quantization in your model is given at: https://github.com/mahnoormahnoorr/Quantization 

(source and more info: [https://github.com/vllm-project/llm-compressor/tree/main](https://github.com/vllm-project/llm-compressor/tree/main)  
[https://arxiv.org/pdf/2306.00978](https://arxiv.org/pdf/2306.00978)) 
