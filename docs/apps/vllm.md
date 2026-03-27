---
tags:
  - Free
catalog:
  name: vLLM
  description: A fast and easy-to-use library for LLM inference and serving
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  available_on:
    - Roihu
---

# vLLM

A fast and easy-to-use library for LLM inference and serving.

!!! info "News" 

    **7.4..2026** vLLM now available as a separate module on Roihu


## Available

Currently supported PyTorch versions:

| Version | Module               |
|:--------|----------------------|
| 0.18.0  | `python-vllm/0.18.0` |

Includes [vLLM](), [PyTorch](https://pytorch.org/) and related
libraries with GPU support via CUDA/ROCm.

!!! note "<span id="roihu-vllm">vLLM on Roihu</span>"
    If you don't particularly need vLLM, we recommend using the [full PyTorch module](pytorch.md) instead, which includes more packages.


If you find that some package is missing, you can often install it
yourself using `pip install`. It is recommended to use Python virtual
environments. See [our Python documentation for more information on
how to install packages
yourself](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).
If you think that some important package should be included in the
module provided by CSC, please [contact our
servicedesk](../support/contact.md).

All modules are based on containers using Apptainer (previously known
as Singularity). Wrapper scripts have been provided so that common
commands such as `python`, `python3`, `pip` and `pip3` should work as
normal. 

## License

vLLM is covered by the [Apache License
2.0](https://github.com/vllm-project/vllm/blob/main/LICENSE).

## Usage

To load the default version on Roihu:

```text
module load python-vllm
```

If you wish to have a specific version ([see above for available
versions](#available)), use:

```text
module load python-vllm/0.18.0
```

To check the exact packages and versions included in the loaded module you can
run:

```text
pip list
```

### Example script for usage

See the [vLLM section in CSC's Machine learning
guide](../support/tutorials/ml-llm.md#inference-with-vllm), which has
links to example script for using vLLM on Roihu.

The full [Machine learning guide](../support/tutorials/ml-guide.md)
might also be of use.

[vLLM]: https://docs.vllm.ai/en/latest/
