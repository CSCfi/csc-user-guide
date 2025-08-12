# Examples

This section contains examples of building and running containers on Puhti and Mahti.

## Example: Python virtual environment

Next, we provide an example of a container with system Python and virtual environment with Python packages installed using pip.
We can define the build definition as follows:

```sh title="python-pip.def"
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
apptainer build --fakeroot python-pip.sif python-pip.def
```

Finally, we can execute commands inside the container.
For example, we can test the container by listing the pip installed Python packages:

```bash
apptainer exec python-pip.sif pip --no-cache list
```

## Example: Extending a local image

We can also extend existing SIF images.
In this example, we extend the `python-pip.sif` container image by adding another Python library to it as follows:

```sh title="python-pip-2.def"
Bootstrap: localimage
From: python-pip.sif

%post
    python3.11 -m pip install --no-cache-dir pandas
```

Now, we build the container as normal:

```bash
apptainer build --fakeroot python-pip-2.sif python-pip-2.def
```

Let's list the pip installed packages to see the packages that we added:

```bash
apptainer exec python-pip.sif pip --no-cache list
```

## Example: Using Make to build containers

Makefiles are a great way to organize the logic for building containers.
If you are not familiar with how Makefiles work, we recommend reading the excellent [Makefile Tutorial](https://makefiletutorial.com/).

Here is an example of using a Makefile to build a container from a definition file named `container.def` into a SIF file named `container.sif`.

```sh title="container.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:8.10
```

```Makefile title="Makefile"
TMPDIR ?= /tmp
PREFIX := .

CONTAINER_SIF := $(PREFIX)/container.sif
CONTAINER_DEF := container.def

.PHONY: all
all: $(CONTAINER_SIF)

$(CONTAINER_SIF): $(CONTAINER_DEF)
	apptainer build --fakeroot --bind=$(TMPDIR):/tmp $@ $<

.PHONY: clean
clean:
	rm -f $(CONTAINER_SIF)
```

Let's invoke Make to build the container:

```bash
make
```

We can also invoke make with arguments such as `PREFIX` to build the container into a different directory:

```bash
make PREFIX=/projappl/project_id
```

## Example: Accelerated visualization application

- [VirtualGL](https://github.com/CSCfi/singularity-recipes/tree/main/visualization)
- [Blender](https://github.com/CSCfi/singularity-recipes/tree/main/blender)

## Other application containers

CSC has container build recipes for various applications in the [singularity-recipes](https://github.com/CSCfi/singularity-recipes) repository.
Here are the recipes that can be built with Apptainer using fakeroot on Puhti and Mahti:

- [Miniforge](https://github.com/CSCfi/singularity-recipes/tree/main/miniforge)
- [Python with uv](https://github.com/CSCfi/singularity-recipes/tree/main/python-uv)
- [MATLAB](https://github.com/CSCfi/singularity-recipes/tree/main/matlab/r2024b)
- [Macaulay2](https://github.com/CSCfi/singularity-recipes/tree/main/macaulay2)
- [Open MPI with OSU micro-benchmarks](https://github.com/CSCfi/singularity-recipes/tree/main/openmpi)
- [R environment](https://github.com/CSCfi/singularity-recipes/tree/main/r-env-singularity/4.5.1-fakeroot)
