---
tags:
  - Free
---

# Python

[Python](https://www.python.org/) is a general-purpose high-level
programming language that is widely used for scientific computing.

For learning about aspects of Python usage specific to CSC supercomputers,
please see the page on
[using Python effectively](../support/tutorials/using-python-effectively.md).

## Available

* Puhti: 3.x versions
* Mahti: 3.x versions

## License

Python packages are usually licensed under various free and open source (FOSS)
licenses. Python itself is licensed under the
[PSF License](https://docs.python.org/3/license.html), which is also open source.

## Usage

### Default environment
The basic system Python (`/usr/bin/python3`) available by default on
both Puhti and Mahti (without loading any modules) is **Python version
3.6.8**. This can be launched simply with the command `python3`, but
this environment contains only a basic set of standard Python
packages.

### Environments specific to science areas

If you need a newer version of Python, or a wider set of Python packages,
Puhti and Mahti have several pre-installed
[environment modules](../computing/modules.md) which contain
Python environments tailored to different science areas.

| Module name | Purpose |
|-|-|
| [biopythontools](./biopython.md) | bioinformatics |
| [geoconda](./geoconda.md) | geoinformatics  |
| [jax](./jax.md) | JAX ML framework |
| [python-data](./python-data.md) | data analysis and ML utilities |
| [pytorch](./pytorch.md) | PyTorch ML framework |
| [tensorflow](./tensorflow.md) | TensorFlow ML framework |

To use any of the above environments, simply load the corresponding module.
For example:

```bash
module load python-data
```

For more details about available Python versions and included libraries,
see the corresponding application documentation.

Typically, after activating a Python-based module, you can continue using the
`python3` command, but this will now point to a newer version of Python with a
wider set of Python packages available. You can always check the Python version
with the command  
`python3 --version`, and the full path of the command with
`which python3` (to see if you are using the system Python or one from the
modules listed above).

### Custom environments

While the pre-installed Python environments are by themselves sufficient for
many tasks, projects often include tasks which require additional libraries.
If this is the case, it is possible to
[extend existing environments](../../support/tutorials/using-python-effectively/#installing-python-packages-to-existing-modules)
or
[create completely new ones](../../support/tutorials/using-python-effectively/#creating-your-own-python-environments)
.

## References

* [Python Software Foundation](https://www.python.org/psf-landing/)

## More information

* [Python documentation](https://docs.python.org/3/)
* [The Python Package Index](https://pypi.org/)
