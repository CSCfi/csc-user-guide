# Examples

This section contains examples of building and running containers on Puhti and Mahti.

## Applications

CSC has build recipes for various application in the [singularity-recipes](https://github.com/CSCfi/singularity-recipes) repository.
Here are the recipes that can be built with Apptainer using fakeroot on Puhti and Mahti:

- [Miniforge](https://github.com/CSCfi/singularity-recipes/tree/main/miniforge)
- [uv (Python)](https://github.com/CSCfi/singularity-recipes/tree/main/python-uv)
- [MATLAB](https://github.com/CSCfi/singularity-recipes/tree/main/matlab/r2024b)
- [Macaulay2](https://github.com/CSCfi/singularity-recipes/tree/main/macaulay2)
- [Open MPI with OSU micro-benchmarks](https://github.com/CSCfi/singularity-recipes/tree/main/openmpi)
- [R environment](https://github.com/CSCfi/singularity-recipes/tree/main/r-env-singularity/4.5.1-fakeroot)

## Python virtual environment

Next, we provide an example of simple Python container with system Python and virtual environment.
We can define the build definition as follows:

```sh title="python-venv.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:8.10

%post
    # Replace the failing commands with always succeeding dummies.
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    # Install Python with system package manager.
    dnf -y update
    dnf -y install python3.11 python3.11-pip
    dnf -y clean all

    # Create a Python virtual environment and install packages using pip.
    python3.11 -m venv /opt/venv
    export PATH=/opt/venv/bin:$PATH
    python3.11 -m pip install --no-cache-dir numpy

%environment
    export PATH=/opt/venv/bin:$PATH
```

Now, we can build the container image as follows:

```bash
apptainer build --fakeroot python-venv.sif python-venv.def
```

Finally, we can execute commands inside the container.
For example, we can test the container by listing the PIP installed Python packages:

```bash
apptainer exec python-venv.sif pip --no-cache list
```

## Extend an image

We can also extend existing SIF images.
In this example, we extend the `python-venv.sif` container image by adding a new python library to it as follows:

```sh title="python-venv-2.def"
Bootstrap: localimage
From: python-venv.sif

%post
    python3.11 -m pip install --no-cache-dir pandas
```

Now, we build the container as normal:

```bash
apptainer build --fakeroot python-venv-2.sif python-venv-2.def
```

Let's list the PIP installed packages to see the packages that we added:

```bash
apptainer exec python-venv.sif pip --no-cache list
```
