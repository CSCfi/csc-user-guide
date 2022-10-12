---
tags:
  - Free
---

# JAX

JAX is Autograd and XLA, brought together for high-performance machine
learning research. 

!!! News

    **5.10.2022** Due to Puhti's update to Red Hat Enterprise Linux 8
    (RHEL8), **the number of supported JAX versions has been reduced.**
    Please [contact our servicedesk](../support/contact.md) if you really
    need access to older versions.


## Available

Currently supported JAX versions:

| Version | Module       | Puhti | Mahti |
|:-------:|--------------|:-----:|:-----:|
| 0.3.13  | `jax/0.3.13` | X     | X     |

The modules contain [JAX](https://github.com/google/jax/) for Python
with GPU support via CUDA. 

If you find that some package is missing, you can often install it
yourself with `pip install --user`. See [our Python
documentation](python.md#installing-python-packages-to-existing-modules)
for more information on how to install packages yourself. If you think
that some important JAX-related package should be included in
the modules provided by CSC, please [contact our
servicedesk](../support/contact.md).

The JAX modules are Apptainer (formerly Singularity)-based but wrapper
scripts have been provided so that common commands such as `python`,
`python3`, `pip` and `pip3` should work as normal. For more
information, see [CSC's general instructions on how to run Apptainer
containers](../computing/containers/run-existing.md).

## License

JAX is licensed under [Apache License
2.0](https://github.com/google/jax/blob/main/LICENSE).

## Usage

To use this software on Puhti or Mahti, initialize it with:

```text
module load jax
```

to access the default version. 

Please note that the JAX modules already include CUDA and cuDNN
libraries, so **there is no need to load cuda and cudnn modules
separately!** 

This will show all available versions of JAX:

```text
module avail jax
```

The JAX modules include several libraries from the JAX ecosystem
(e.g. Haiku, Flax, Trax, Objax, and Elegy). To check the exact
packages and versions included in the loaded module you can run: 

```text
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
- [JAX GitHub page](https://github.com/google/jax)
- [JAX reference documentation](https://jax.readthedocs.io/en/latest/)
