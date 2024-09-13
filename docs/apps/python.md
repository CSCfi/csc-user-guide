---
tags:
  - Free
---

# Python

[Python](https://www.python.org/) is a general-purpose high-level
programming language that is widely used for scientific computing.
For instructions on using Python effectively on CSC supercomputers,
please see our
[Python usage guide](../support/tutorials/python-usage-guide.md).

## Available

* Puhti: 3.x versions
* Mahti: 3.x versions

## License

Python packages are usually licensed under various free and open source (FOSS)
licenses. Python itself is licensed under the
[PSF License](https://docs.python.org/3/license.html), which is also open source.

## Usage

Our
[Python usage guide](../support/tutorials/python-usage-guide.md)
contains instructions for installing packages,
using different development environments and doing parallel processing
with Python.

It is generally recommended to use one of
[pre-installed Python environments](python.md#pre-installed-python-environments)
for computing,
since these already contain the essential libraries for most uses.
If for some reason one wishes to use Python without loading an environment
module, a
basic
[system Python](python.md#system-python)
is also available.

### System Python

If using a pre-installed environment is not suitable,
the basic system Python 3.9 can be launched with:

```bash
python3.9
```

!!! warning
    It is strongly advised to explicitly launch Python version 3.9 as
    above, since **the default version launched by `python3` (3.6.8) has
    [reached end-of-life](https://devguide.python.org/versions/)**.

### Pre-installed Python environments

Puhti and Mahti have several pre-installed
[environment modules](../computing/modules.md) containing
Python environments made for different science areas.
For more details about the Python versions and libraries that are available
for a module, please see the corresponding application page by opening
one of the links in the table below.

| Module name | Purpose | Package list |
|-|-|-|
| [biopythontools](biopython.md) | bioinformatics | [open](https://a3s.fi/python-pkg-lists/biopythontools.txt) |
| [geoconda](geoconda.md) | geoinformatics | [open](https://a3s.fi/python-pkg-lists/geoconda.txt) |
| [jax](jax.md) | JAX ML framework | [open](https://a3s.fi/python-pkg-lists/jax.txt) |
| [python-data](python-data.md) | data analysis and ML utilities | [open](https://a3s.fi/python-pkg-lists/python-data.txt) |
| [pytorch](pytorch.md) | PyTorch ML framework | [open](https://a3s.fi/python-pkg-lists/pytorch.txt) |
| [qiskit](qiskit.md) | quantum computing | [open](https://a3s.fi/python-pkg-lists/qiskit.txt) |
| [tensorflow](tensorflow.md) | TensorFlow ML framework | [open](https://a3s.fi/python-pkg-lists/tensorflow.txt) |

To use any of the above environments, simply load the corresponding module
using the `module load` command.
For example:

```bash
module load python-data
```

Typically, after activating a Python-based module, the `python3` command points
to a version of Python that is newer than the default system Python and has a
wider set of available packages. You can always check the Python version
with the command `python3 --version`, and the full path of the command with
`which python3` (to see if you are using the system Python or one from the
modules listed above).

### Custom Python environments

While the pre-installed Python environments suffice for many applications,
projects often involve tasks which require additional libraries.
The following options are available in this case:

* [Installing Python packages to existing modules](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules)
* [Creating your own Python environments](../support/tutorials/python-usage-guide.md#creating-your-own-python-environments)

## References

* [Python Software Foundation](https://www.python.org/psf-landing/)

## More information

* [Python documentation](https://docs.python.org/3/)
* [The Python Package Index](https://pypi.org/)
