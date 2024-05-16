# Using Python on CSC supercomputers

Some aspects of using Python on a supercomputer differ crucially from usage
on a personal device. To make the most of the computational resources available
to you, it is good to know about these differences.

## Pre-installed software

Because of the parallel nature of the Lustre file system that CSC
supercomputers utilize, it is not possible for regular users to do
system-level software installations as one would on a personal device.
Fortunately, a diverse collection of useful software for scientific computing
is already installed on CSC supercomputers, including several Python
environments.

- All software needs to be loaded as lua modules
	- Link to instructions for using them
- List available Python envs, their purpose and contents

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


