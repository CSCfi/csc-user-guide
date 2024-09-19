---
tags:
  - Free
---

# JAX

JAX is Autograd and XLA, brought together for high-performance machine
learning research.


## Available

Currently supported JAX versions:

| Version | Module             | Puhti   | Mahti   | LUMI       | Notes          |
|:-------:|--------------------|:-------:|:-------:|:----------:|----------------|
| 0.4.30  | `jax/0.4.30`       | default | default | -          | all packages   |
| 0.4.30  | `jax/0.4.30-small` | X       | X       | -          | framework only |
| 0.4.23  | `jax/0.4.23-py3.9` | X       | X       | default*   |                |
| 0.4.20  | `jax/0.4.20`       | X       | X       | X*         |                |
| 0.4.18  | `jax/0.4.18`       | -       | -       | X*         |                |
| 0.4.14  | `jax/0.4.14`       | X       | X       | -          |                |
| 0.4.13  | `jax/0.4.13`       | X       | X       | -          |                |
| 0.4.1   | `jax/0.4.1`        | X       | X       | -          |                |
| 0.3.13  | `jax/0.3.13`       | X       | X       | -          |                |

The modules contain [JAX](https://github.com/google/jax/) for Python 3.9
with GPU support via CUDA/ROCm as well as a large list of additional python packages commonly used together with JAX.

**Versions in LUMI, marked as "*" are still experimental with limited
support.** Some of the features described below might not work for them.
They are subject to change at any time without notice. Note that JAX is
also available in the [LUMI Software Library](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/j/jax/).

Since version 0.4.30, the JAX module comes in two flavours:

- A "small" flavour that includes JAX with CUDA 12.2 GPU support, as well as cpu-only versions of
  PyTorch and Tensorflow to allow using their data loading utilities. These follow the naming scheme
  `jax/<version>-small`, or you can use `jax/small` to load the default (latest) version.
- A "full" flavour that includes many commonly used machine learning packages building on JAX -- you can
  check `pip list` for a full list of all included packages. These follow the naming scheme `jax/<version>`,
  or you can simply use `jax` to load the default (latest) version.

!!! note

    Since JAX releases new versions on a somewhat irregular schedule
    we will not make all new versions immediately available.
    Instead we endeavour to update the JAX version available on our systems approximately every six months, targeting February and August, on a best effort basis.

All modules are based on containers using Apptainer (previously known
as Singularity). Wrapper scripts have been provided via [tykky](../computing/containers/tykky.md)
so that common commands such as `python`, `python3`, `pip` and `pip3` and
those provided by installed packages should work as normal.
For other commands, you may need to prefix them with
`apptainer_wrapper exec`. For more information, see [CSC's general
instructions on how to run Apptainer
containers](../computing/containers/run-existing.md).


## Additional packages

If you find that some package is missing, you can often install it
yourself using `pip install`. It is recommended to use Python virtual
environments. See [our Python documentation for more information on
how to install packages
yourself](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).
If you think that some important package should be included in the
module provided by CSC, please [contact our
servicedesk](../support/contact.md).

## License

JAX is licensed under [Apache License
2.0](https://github.com/google/jax/blob/main/LICENSE).

## Usage

To use the default version (most-recent) on Puhti or Mahti, initialize it with:

```bash
module load jax
```

To access CSC-installed JAX on LUMI:

```bash
module use /appl/local/csc/modulefiles/
module load jax
```

!!! note

    In your scripts we recommend to fix the version so that
    changes in future upgrades do not break scripts, e.g.,:
    `module load jax/0.4.23-py3.9`

Please note that the JAX modules already include the corresponding
CUDA and cuDNN or ROCm libraries, so **there is no need to load any
cuda, cudnn, or rocm modules separately!**

This will show all available versions of JAX:

```bash
module avail jax
```

!!! note

    Note that the login nodes are not intended for heavy computing,
    please use slurm batch jobs instead. See our [instructions on how
    to use the batch job
    system](../computing/running/getting-started.md).

!!! note

    Please **do not read a huge number of files from the shared file system**, use
    fast local disk or package your data into larger files instead! See the [Data
    storage section in our machine learning
    guide](../support/tutorials/ml-data.md) for more details.

## More information

- [CSC's Machine learning guide](../support/tutorials/ml-guide.md)
- [JAX in LUMI Software Library](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/j/jax/)
- [JAX GitHub page](https://github.com/google/jax)
- [JAX reference documentation](https://jax.readthedocs.io/en/latest/)
