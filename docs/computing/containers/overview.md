---
description: Instructions for building and running Apptainer containers in CSC supercomputers.
---

# Apptainer containers

This section provides instructions for building and running containers with [Apptainer](https://apptainer.org/) on CSC supercomputers.
While we focus on CSC-specific usage and best practices, the official [Apptainer documentation](https://apptainer.org/docs/user/main/index.html) serves as a comprehensive reference for general usage.
For hands-on guidance, see the [Examples](./examples.md) section, which provides concrete examples tailored to CSC systems.

Note that Apptainer was formerly known as Singularity, and you may still encounter the old name in the software internals and old documentation.
The project was renamed when it transitioned from Sylabs to the Linux Foundation, but the core functionality remains the same.
Sylabs maintains a fork of the project called SingularityCE.

## Motivation

An Apptainer container image is a single, compressed file that packages everything needed to run an application.
This immutable file contains the complete root filesystem, including all applications, libraries, and dependencies, along with metadata such as environment variables and runtime configurations.
Apptainer uses the Singularity Image Format (SIF) for its images, which are identified by the `.sif` file extension.

Apptainer containers enable you to select any Linux distribution as your base image, such as Ubuntu, Rocky Linux, or OpenSUSE, and leverage its native package manager to install software within that environment.
However, building containers on CSC supercomputers has certain limitations, especially, when your chosen base image differs from the host's Linux distribution.
These issues and their solutions are covered in detail later.

Running software from an Apptainer container can significantly improve startup times and reduce I/O bottlenecks on the [Lustre](../lustre.md) parallel file system.
This is particularly beneficial for applications that contain many files or load numerous shared libraries during startup.
Python environments, for instance, are notorious for this issue due to their extensive module dependencies and dynamic loading behavior.

Apptainer containers ensure reproducible execution because their images are immutable.
Once built, a container image remains unchanged, guaranteeing consistent behavior across different systems and over time.
Additionally, Apptainer build definitions document the exact steps, packages, and configurations used to create the container, making the entire build process transparent and repeatable.

Container images have an important limitation: they are not composable.
Unlike traditional package managers that allow you to incrementally add software to a system, you cannot simply combine existing containers to create a new one.
For example, having one container with Python and another with R does not give you access to both environments simultaneously.
To use both tools together, you must create a new container image that includes both Python and R installations from the start.

## Running containers

### Using Apptainer directly

Assume we have a container image called `container.sif`.
We can execute an arbitrary command (replace `mycommand`) inside the container using the `apptainer exec` command as follows:

```bash
apptainer exec container.sif mycommand
```

We can make directories from the host available inside the container by using bind mounts.
On Roihu, we can bind mount the different [Disk Areas](../disk.md) to the container manually as follows:

```bash
apptainer exec --bind="/users,/projappl,/scratch,$TMPDIR,$LOCAL_SCRATCH" container.sif mycommand
```

Alternatively, we can use `csc-common-bind` command to bind mounts the common disk areas:

```bash
apptainer exec --bind="$(csc-common-bind)" container.sif mycommand
```

On Roihu-GPU, we can add Nvidia GPU support with the `--nv` flag as follows:

```bash
apptainer exec --nv container.sif mycommand
```

We can use the same flags with `apptainer run` and `apptainer shell` commands.

## Building container images

This section explain how to use Apptainer to convert existing Docker and OCI images to SIF images, how to build new SIF images from definition files or how to develop containers interactively as modifiable (ch)root directory using a sandbox.
Also, we cover how to set the appropriate build environment and resources like memory for building on Roihu.

### Choosing a Linux distribution as a base image

When selecting a base image for your container, you can choose from several Linux distributions, each with its own package manager.
For Red Hat Enterprise Linux (RHEL) based distributions that use the DNF package manager, popular options include [RedHat Universal Base Images (UBI)](https://catalog.redhat.com/en/software/base-images) available as [redhat/ubi8](https://hub.docker.com/r/redhat/ubi8) and [redhat/ubi9](https://hub.docker.com/r/redhat/ubi9), as well as community alternatives like [rockylinux](https://hub.docker.com/r/rockylinux/rockylinux) and [almalinux](https://hub.docker.com/_/almalinux).
If you prefer SUSE-based systems with the Zypper package manager, [opensuse/leap](https://hub.docker.com/r/opensuse/leap) provides a stable foundation. For Debian-based distributions using the APT package manager, both [debian](https://hub.docker.com/_/debian) and [ubuntu](https://hub.docker.com/_/ubuntu) offer well-maintained base images with extensive package repositories.

While Apptainer allows you to build containers using any Linux distribution as the base image, building on CSC supercomputers has some limitations due to using Apptainer fakeroot mode without unprivileged user namespaces.
In this environment, certain privileged commands that are commonly executed during package installation will fail.
For example, package managers often run privileged commands, such as `useradd` and `groupadd`, as part of their installation scripts and these will fail in the fakeroot environment.

By using a base image from the same family as the host system we will decrease the number of problems stemming from using fakeroot mode for building containers.
If you are using a base image that is not from the same family as the host system, expect that there are more packages that can't be installed successfully.
The best way to find out is to try to build the container.

You can identify your host system's Linux distribution as follows:

```bash
cat /etc/os-release
```

```text title="stdout"
NAME="Red Hat Enterprise Linux"
VERSION="9.8 (Plow)"
ID="rhel"
ID_LIKE="fedora"
VERSION_ID="9.8"
...
```

Furthermore, we can replace the problematic commands with dummy versions that always succeed:

```bash
cp /usr/bin/true /usr/sbin/useradd
cp /usr/bin/true /usr/sbin/groupadd
```

This approach allows package installations to complete successfully while bypassing the permission-related failures.

### Installing software into the container

The typical pattern of installing software into a container is to start by using the system package manager such as DNF, APT or Zypper to install "system" software to `/usr` and then install software using a user-space package manager such as Pip, Conda or Spack or install software manually to `/usr/local` or in a unique directory under `/opt`.

### Build location

On Roihu, we can build containers on login nodes and compute nodes.
Local disk is available automatically.
To build on a compute node, we can reserve an interactive Slurm job as follows:

```bash
sinteractive --cores 4 --mem 4000 --time 0:15:00
```

### Temporary directory

The `TMPDIR` environment variable must point to the local disk.
Apptainer will use it to identify the directory as its temporary directory when building a container.
Roihu cluster sets the `TMPDIR` environment variable automatically on login nodes which have local disk by default and compute nodes when local disk is reserved.
Lustre parallel file system cannot (and should not) be used as the temporary directory.

### Cache directory

Apptainer caches layers and blobs such as base images to the cache directory.
The default location is in the home directory (`$HOME/.apptainer`) which on Roihu has a limited quota.
Thus, we may want to change the cache location to scratch to avoid filling our home directory (modify the `project_id` to your project ID).

```bash
export APPTAINER_CACHEDIR=/scratch/project_id/$USER/.apptainer
```

We can also clean the cache directory if necessary:

```bash
apptainer cache clean
```

### Bind mounting temporary directory

By default Apptainer bind mounts the host's `/tmp` to `/tmp` in the build environment.
However, the size of `/tmp` is limited on Roihu, thus, we bind mount the local disk (`$TMPDIR`) to `/tmp` to avoid running out of disk space as follows: `--bind="$TMPDIR:/tmp"`.

### Building SIF image from existing Docker or OCI image

We can obtain existing container images from a container registry by pulling them.
Apptainer will convert them from Docker or OCI format into the Singularity Image Format (SIF).

```bash
apptainer build rockylinux.sif docker://docker.io/rockylinux/rockylinux:9.8
```

### Building SIF image from definition file

Apptainer definition files are written using the `.def` file extension.
Here is a simple example of container definition:

```sh title="container.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:9.8

%post
    # Replace the failing commands with always succeeding dummies.
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    # Continue to install software into the container normally.
    dnf -y update  # would fail without the dummies
```

We can invoke Apptainer to build the container (`container.sif`) from the definition file (`container.def`) using fakeroot as follows:

```bash
apptainer build --fakeroot --bind="$TMPDIR:/tmp" container.sif container.def
```

See the [Examples](./examples.md) section for more examples of Apptainer definition files.

### Developing with interactive sandbox

We can also build Apptainer sandboxes with fakeroot.
Sandboxes are useful for interactive development of containers.
The sandbox must be created on the local disk (`$TMPDIR`), not on the Lustre parallel file system.

We can initialize a sandbox from a base image as follows:

```bash
apptainer build --fakeroot --sandbox "$TMPDIR/rockylinux" docker://docker.io/rockylinux/rockylinux:9.8
```

Then we can run a shell in the sandbox to install software into it:

```bash
apptainer shell --fakeroot --writable --contain --cleanenv --bind="$TMPDIR:/tmp" "$TMPDIR/rockylinux"
```

We can use the same tricks to replace the failing commands in the sandbox:

```bash
cp /usr/bin/true /usr/sbin/useradd
cp /usr/bin/true /usr/sbin/groupadd
```

Now, we can install software normally:

```bash
dnf -y update
```

## Roihu base images

CSC provides dedicated base images for both Roihu CPU and Roihu GPU.
These base images are built on top of Rocky Linux 9 images.
Each image contains one of the Spack-built software stacks, along with its dependencies and modulefiles to activate the environment.
The software versions match those of the system software.

Base images allow you to build containers with a software stack identical to the platform's, such as optimized MPI containers.
The resulting container images are self-contained and do not require bind-mounting any binaries to run.
However, these containers are not portable to other machines.
Container images are available in the OCI format on Satama.

See examples in the [Examples](./examples.md) section.

## Reading datasets from SquashFS file

We can also avoid I/O bottlenecks with datasets that consist of large amounts of small files by reducing them to a single SquashFS file.
The SquashFS file can be bind mounted inside the container and accessed in a read-only manner.
The following example extracts the dataset to the local disk, creates a SquashFS file from the dataset and then moves it back to scratch:

```bash
# Extract individual files to local drive
cd $TMPDIR
tar xf /scratch/project_id/mydataset.tar

# Create squashfs file
mksquashfs mydataset mydataset.sqfs -processors 4

# Move the resulting squashfs file back to the shared drive
mv mydataset.sqfs /scratch/project_id/
```

Now, we can bind mount the dataset as follows:

```bash
apptainer exec --bind=/scratch/project_id/mydataset.sqfs:/data:image-src=/ container.sif mycommand
```

The data will be available under the path `/data` inside the container.

## Container wrappers

[Tykky](./tykky.md) container wrapper is available for creating containerized Pip and Conda installations with wrappers scripts.
If you are familiar with Tykky you can keep using it, but we recommend building and running containers directly as explained in the previous sections.
