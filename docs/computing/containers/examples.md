# Examples

This section contains examples of building and running containers on Roihu.

## Example: Python virtual environment

Next, we provide an example of a container with system Python and virtual environment with Python packages installed using Pip.
We can define the build definition as follows:

```sh title="python-pip.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:9.8

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
apptainer build --fakeroot --bind="$TMPDIR:/tmp" python-pip.sif python-pip.def
```

Finally, we can execute commands inside the container.
For example, we can test the container by listing the Pip installed Python packages:

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
    # The %environment section of the base image is not sourced during %post,
    # so activate the virtual environment explicitly to install into it.
    export PATH=/opt/venv/bin:$PATH

    python3.11 -m pip install --no-cache-dir pandas
```

Now, we build the container as normal:

```bash
apptainer build --fakeroot --bind="$TMPDIR:/tmp" python-pip-2.sif python-pip-2.def
```

Let's list the Pip installed packages to see the packages that we added:

```bash
apptainer exec python-pip-2.sif pip --no-cache list
```

## Example: Roihu-CPU base container with OSU micro benchmarks

This image is built for x86_64, so build and run it on Roihu-CPU (`roihu-cpu.csc.fi`).

Build definition file:

```sh title="container.def"
Bootstrap: docker
From: satama.csc.fi/r_installation_spack/core-cpu-gcc-15.2.0:v2026_03

%arguments
    NPROCS=10

%post
    # Activate module environment and load default modules.
    . /opt/activate.sh

    # Install tools
    dnf -y install wget file which
    dnf -y clean all

    # Build osu benchmarks
    cd /opt
    wget -q http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-7.4.tar.gz
    tar xf osu-micro-benchmarks-7.4.tar.gz
    cd osu-micro-benchmarks-7.4
    ./configure --prefix=/opt/osu-micro-benchmarks CC=mpicc CXX=mpicxx CFLAGS=-O3
    make -j{{ NPROCS }}
    make install
    cd ..
    rm -rf osu-micro-benchmarks-7.4 osu-micro-benchmarks-7.4.tar.gz

%runscript
    . /opt/activate.sh
    exec "$@"
```

When building the containers, set the [Apptainer cache directory](./overview.md#cache-directory) so that the base image does not fill your home directory quota (replace `<project>` with your project):

```bash
export APPTAINER_CACHEDIR=/scratch/<project>/$USER/.apptainer
apptainer build --fakeroot --bind="$TMPDIR:/tmp" container.sif container.def
```

Now, you can run commands inside the container with the environment active as follows:

!!! warning "Slurm environment variables are required for MPI to work!"
    Slurm environment variables must be propagated to the container environment for MPI to work.
    Therefore, do not use `--cleanenv`, `--contain` or similar flags.

`batch.sh`

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --mem=2G
#SBATCH --time=00:05:00

module purge
srun apptainer run container.sif /opt/osu-micro-benchmarks/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bibw
srun apptainer run container.sif /opt/osu-micro-benchmarks/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency
```

The point-to-point benchmarks need two MPI tasks on separate nodes, which fits the
[`test` partition](../running/batch-job-partitions.md#roihu-cpu-partitions).
For longer runs on full nodes, use the `medium` partition instead and omit `--mem`, since it allocates whole nodes.

```bash
sbatch batch.sh
```

## Example: Roihu-GPU base container with NCCL tests

This image is built for the Arm-based (aarch64) Nvidia Grace processors, so build and run them on Roihu-GPU (`roihu-gpu.csc.fi`).

Build definition file:

```sh title="container.def"
Bootstrap: docker
From: satama.csc.fi/r_installation_spack/core-gpu-gcc-14.3.0-cuda-12.9.1:v2026_03

%arguments
    NPROCS=10

%post
    # Activate module environment and load default modules.
    . /opt/activate.sh

    # Install tools
    dnf -y install wget file which
    dnf -y clean all

    # Install NCCL Tests
    module load nccl
    cd /opt
    wget https://github.com/NVIDIA/nccl-tests/archive/refs/tags/v2.18.3.tar.gz
    tar xf v2.18.3.tar.gz
    rm v2.18.3.tar.gz
    cd nccl-tests-2.18.3
    make -j{{ NPROCS }} CUDA_HOME=$CUDA_HOME NCCL_HOME=$NCCL_INSTROOT
    make -j{{ NPROCS }} CUDA_HOME=$CUDA_HOME NCCL_HOME=$NCCL_INSTROOT MPI=1 MPI_HOME=$OPENMPI_INSTROOT NAME_SUFFIX=_mpi

%runscript
    . /opt/activate.sh
    module load nccl
    exec "$@"
```

When building the containers, set the [Apptainer cache directory](./overview.md#cache-directory) so that the base image does not fill your home directory quota (replace `<project>` with your project):

```bash
export APPTAINER_CACHEDIR=/scratch/<project>/$USER/.apptainer
apptainer build --fakeroot --bind="$TMPDIR:/tmp" container.sif container.def
```

Note that the GPU base images are over 10 GB, which exceeds the 15 GiB home directory quota once the cache and the resulting image are counted together.

Now, you can run commands inside the container with the environment active as follows.
The `single` script runs the plain NCCL test over the four GPUs of one node, while the `mpi` script runs the MPI-enabled build across two nodes.
Both use the [`gputest` partition](../running/batch-job-partitions.md#roihu-gpu-partitions), which allows up to two nodes with four GPUs each.
Note that neither script sets `--mem`: on the GPU partitions the CPU memory is allocated automatically based on the number of reserved GPUs.

`batch_single.sh`

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gputest
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=72
#SBATCH --gres=gpu:gh200:4
#SBATCH --time=00:15:00

module purge
srun apptainer run --nv container.sif /opt/nccl-tests-2.18.3/build/all_reduce_perf -b 8 -e 128M -f 2 -g 4
```

```bash
sbatch batch_single.sh
```

`batch_mpi.sh`

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=gputest
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=72
#SBATCH --gres=gpu:gh200:4
#SBATCH --time=00:15:00

module purge
srun apptainer run --nv container.sif /opt/nccl-tests-2.18.3/build/all_reduce_perf_mpi -b 8 -e 128M -f 2 -g 1
```

```bash
sbatch batch_mpi.sh
```

## Example: Using Make to build containers

Makefiles are a great way to organize the logic for building containers.
If you are not familiar with how Makefiles work, we recommend reading the excellent [Makefile Tutorial](https://makefiletutorial.com/).

Here is an example of using a Makefile to build a container from a definition file named `container.def` into a SIF file named `container.sif`.

```sh title="container.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:9.8
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
make PREFIX=/projappl/<project>
```

## Example: Accelerated visualization application

Start by building the [visualization](https://github.com/CSCfi/singularity-recipes/tree/main/visualization) base image which contains VirtualGL, its dependencies, and utility scripts.
We can build the accelerated visualization applications such as [Blender](https://github.com/CSCfi/singularity-recipes/tree/main/blender) on top of the visualization base image.
Application should be executed with the `vglrun_wrapper` script installed in the base container.

## Other application containers

CSC has container build recipes for various applications in the [singularity-recipes](https://github.com/CSCfi/singularity-recipes) repository.
Here are the recipes that can be built with Apptainer using fakeroot on Roihu:

- [Miniforge](https://github.com/CSCfi/singularity-recipes/tree/main/miniforge)
- [Python with uv package manager](https://github.com/CSCfi/singularity-recipes/tree/main/python-uv)
- [Open MPI with OSU micro-benchmarks](https://github.com/CSCfi/singularity-recipes/tree/main/openmpi)
- [MATLAB](https://github.com/CSCfi/csc-env-matlab/tree/main/mathworks)
- [Macaulay2](https://github.com/CSCfi/singularity-recipes/tree/main/macaulay2)
- [R environment](https://github.com/CSCfi/singularity-recipes/tree/main/r-env-singularity/4.5.1-fakeroot)
- [PyTorch](https://github.com/CSCfi/singularity-recipes/tree/main/pytorch-fakeroot/2.6)
