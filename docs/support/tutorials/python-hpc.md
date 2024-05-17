# Using Python on CSC supercomputers

Some basic aspects of using Python are very different on a CSC
supercomputer compared to usage on a personal device.
To make the most of the computational resources offered by CSC,
it is good to be aware of the differences.

## Pre-installed software

Because of the parallel nature of the **Lustre** file system used by CSC
supercomputers, it is not possible for users to do
system-level software installations, as one would on a personal device.
Fortunately, a diverse collection of essential software for scientific
computing is already installed, including several
Python environments tailored to different science areas.

Pre-installed software environments on CSC supercomputers are implemented as
**Lmod** environment modules. For learning more about environment modules,
please visit the [module system Docs page](../../computing/modules.md).
The following Python environments are available as modules:

| Module name | Purpose | Contents |
|-|-|-|
| biopythontools | bioinformatics | [pip](https://a3s.fi/python-recipes/biopythontools_3.10.6.txt) |
| geoconda | geoinformatics | [conda](https://a3s.fi/python-recipes/geoconda_3.10.9.yml) |
| jax | ML framework | [pip](https://a3s.fi/python-recipes/jax0.4.23_python3.9_cuda12.2_csc_fix1.txt) |
| python-data | data analytics and ML utilities | [conda](https://a3s.fi/python-recipes/python-data-2023-11.yaml) |
| pytorch | ML framework | [pip](https://a3s.fi/python-recipes/pytorch_2.2.1_csc_fix2.txt) |
| tensorflow | ML framework | [pip](https://a3s.fi/python-recipes/tensorflow_2.15.0_rocky3.txt) |

## Installing additional software

While the pre-existing Python environments are quite extensive, every so often
a project requires additional software not present in an environment.

### Complementing a pre-existing environment

In most cases, it is easiest to complement one of the pre-existing Python
environments. There are several ways to do this.

#### Virtual environments

The Python standard library includes the
[venv](https://docs.python.org/3/library/venv.html) module, which supports the
creation of virtual environments. Python virtual environments are generally
very useful for managing packages for multiple projects with their individual
dependencies. On CSC supercomputers, this is very helpful, since system-level
installations are not possible.

While it is possible to install all required packages inside the virtual
environment, it is typically more convenient to use them as extensions of
pre-existing environments. In most cases, this is as simple as loading a module
and then sourcing the virtual environment.

```bash
module load <some-module>
source <my-env>/bin/activate
```

#### User installations 

- Conda environments

	- Recipes for modules for tweaking
- Ways to complement modules

### Build your own environment

- Modules and environments are not the same

### Project-level installation

## Serial and parallel computing

## Interactive computing with Jupyter notebooks


