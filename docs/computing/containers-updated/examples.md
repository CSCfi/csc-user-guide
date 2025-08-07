# Examples

This section contains examples of building and running containers on Puhti and Mahti.

## Applications

CSC has build recipes for various application in the [singularity-recipes](https://github.com/CSCfi/singularity-recipes) repository.
Here are the recipes that can be built with the fakeroot features of Puhti and Mahti:

- [Miniforge](https://github.com/CSCfi/singularity-recipes/tree/main/miniforge)
- [uv (Python)](https://github.com/CSCfi/singularity-recipes/tree/main/python-uv)
- [MATLAB](https://github.com/CSCfi/singularity-recipes/tree/main/matlab/r2024b)
- [Macaulay2](https://github.com/CSCfi/singularity-recipes/tree/main/macaulay2)
- [Open MPI with OSU micro-benchmarks](https://github.com/CSCfi/singularity-recipes/tree/main/openmpi)
- [R environment](https://github.com/CSCfi/singularity-recipes/tree/main/r-env-singularity/4.5.1-fakeroot)

## Python virtual environment

Example of simple Python container with system Python and virtual environment.

```sh title="python-venv.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:8.10

%post
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    # Install Python with system package manager
    dnf -y update
    dnf -y install python3.11 python3.11-pip
    dnf -y clean all

    # Create a Python virtual environment and install packages
    python3.11 -m venv /opt/venv
    export PATH=/opt/venv/bin:$PATH
    python3.11 -m pip install --no-cache-dir numpy

%environment
    export PATH=/opt/venv/bin:$PATH
```

```bash
apptainer build --fakeroot python-venv.sif python-venv.def
```

```bash
apptainer exec python-venv.sif python
```

## Extend an image

```sh title="python-venv-2.def"
Bootstrap: localimage
From: python-venv.sif

%post
    python3.11 -m pip install --no-cache-dir pandas
```
