---
tags:
  - Free
---

# JAX

JAX is Autograd and XLA, brought together for high-performance machine
learning research.


## Available

Currently supported JAX versions:

| Version | Module             | Puhti | Mahti | LUMI | Notes           |
|:-------:|--------------------|:-----:|:-----:|:----:|-----------------|
| 0.4.23  | `jax/0.4.23-py3.9` | X     | X     | X*   | default version |
| 0.4.20  | `jax/0.4.20`       | X     | X     | X*   |                 |
| 0.4.18  | `jax/0.4.18`       | -     | -     | X*   |                 |
| 0.4.14  | `jax/0.4.14`       | X     | X     | -    |                 |
| 0.4.13  | `jax/0.4.13`       | X     | X     | -    |                 |
| 0.4.1   | `jax/0.4.1`        | X     | X     | -    |                 |
| 0.3.13  | `jax/0.3.13`       | X     | X     | -    |                 |

The modules contain [JAX](https://github.com/google/jax/) for Python 9
with GPU support via CUDA/ROCm as well as a large list of additional python packages commonly used together with JAX.

**Versions in LUMI, marked as "X*" are still experimental with limited
support.** Some of the features described below might not work for them.
They are subject to change at any time without notice. Note that JAX is
also available in the [LUMI Software Library](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/j/jax/).

!!! note

    Since JAX releases new versions on a somewhat irregular schedule
    we will not make all new versions immediately available.
    Instead we endeavour to update the JAX version available on our systems approximately once every quarter, targeting February, May, August and November, on a best effort basis.

All modules are based on containers using Apptainer (previously known
as Singularity). Wrapper scripts have been provided so that common
commands such as `python`, `python3`, `pip` and `pip3` should work as
normal. For other commands, you need to prefix them with
`apptainer_wrapper exec`. For more information, see [CSC's general
instructions on how to run Apptainer
containers](../computing/containers/run-existing.md).


## Additional packages

If you find that some package is missing, you can often install it
yourself with `pip install --user`. See [our Python
documentation](python.md#installing-python-packages-to-existing-modules)
for more information on how to install packages yourself. If you think
that some important JAX-related package should be included in
the modules provided by CSC, please [contact our
servicedesk](../support/contact.md).


With recent modules it is also possible to use [Python virtual
environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment). To
create a virtual environment use the command
`python3 -m venv --system-site-packages venv`.

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

The JAX modules include several libraries from the JAX ecosystem
(e.g. Haiku, Flax, and Objax). To check the exact packages and
versions included in the loaded module you can run:

```bash
list-packages
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
