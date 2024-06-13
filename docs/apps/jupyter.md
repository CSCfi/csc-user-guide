---
tags:
  - Free
system:
  - www-mahti
  - www-puhti
---

# Jupyter

[Project Jupyter](https://jupyter.org/) develops and maintains interactive
computational environments, including the ever-popular
[computational notebooks](https://docs.jupyter.org/en/latest/#what-is-a-notebook).

Jupyter interfaces such as Jupyter Notebook and JupyterLab come pre-installed
with the [IPython](https://ipython.readthedocs.io/en/stable/index.html)
kernel, which allows working on notebooks using the
[Python programming language](./python.md). Our web interface also includes an
[interactive Julia-Jupyter app](../computing/webinterface/julia-on-jupyter.md)
using the [IJulia](https://github.com/JuliaLang/IJulia.jl)
kernel for working with the [Julia language](./julia.md). 

## Available

  - Mahti
  - Puhti

## License

Jupyter is released under the [modified BSD
license](https://opensource.org/licenses/BSD-3-Clause).

## Usage

There are two ways of running Jupyter notebooks on CSC supercomputers:

1. As an interactive app on our web
interface **(recommended)**
	1. [Using the IPython kernel](../computing/webinterface/jupyter.md)
	2. [Using the IJulia kernel](../computing/webinterface/julia-on-jupyter.md)
2. Remotely using SSH tunneling
	1. [Using the IPython
kernel](../support/tutorials/rstudio-or-jupyter-notebooks.md#instructions-for-ssh-tunneling)

!!! note
	SSH tunneling requires [setting up SSH
	keys](../../computing/connecting.mdsetting-up-ssh-keys).

## References

- [Project Jupyter](https://jupyter.org/)

## More information

- [About Project Jupyter](https://jupyter.org/about)
- [Project Jupyter Documentation](https://docs.jupyter.org/en/latest/)
