# Containers

In this section, we provide instructions on how to build and run containers using [Apptainer](https://apptainer.org/) with fakeroot enabled in HPC clusters without unprivileged user namespaces.
We explain the special aspects of building and running containers on Puhti and Mahti clusters including how to set up the build environment, how to invoke the build commands, how to write container definition files and how to run containers.
For general instructions about building and running containers, we recommend that users read the official [Apptainer documentation](https://apptainer.org/docs/user/main/index.html).

Some reasons for using containers on HPC clusters are:

- Containers improve startup times and avoid I/O bottlenecks with the parallel file system, that is Lustre in Puhti and Mahti, for applications that consist of a large number of files or load many shared libraries on startup such as Python, R, and MATLAB.
  This is because Apptainer uses the Singularity Image Format (SIF) which packs the container files into a single SquashFS file.

- Running containerized software is reproducible because the container image is immutable.

- Container build definitions capture more comprehensively what is installed into the container and how it is installed.

Limitations of containers:

- Containers are not composable and they are not a substitute for package managers.
  That is, having a container with Python installed and another container with R installed, will not provide you with a container with both Python and R installed.

## Running containers

Assume we have a container image called `container.sif`.
We can execute an arbitrary command (replace `mycommand`) inside the container using the `apptainer exec` command as follows:

```bash
apptainer exec container.sif mycommand
```

We can make directories from the host available inside the container by using bind mounts.
Specific directories that we may want to bind mount on Puhti and Mahti are the user home, projappl, scratch, and local disk spaces.
Here is an example:

```bash
apptainer exec --bind="/users,/projappl,/scratch,$TMPDIR,$LOCAL_SCRATCH" container.sif mycommand
```

We can add (Nvidia) GPU support with the `--nv` flag as follows:

```bash
apptainer exec --nv container.sif mycommand
```

We can use the same flags with `apptainer run` and `apptainer shell` commands.

## Building container images

We can build containers with Apptainer as follows:

```bash
apptainer build <options>
```

In this section, we explain how to use the command to convert existing Docker and OCI images to Singularity Image format (SIF) images, build new SIF images from definition files or develop containers interactively as modifiable (ch)root directory using a sandbox.
Also, we cover how to set the appropriate build environment and resources like memory for building on Puhti and Mahti.

### Build location

We can build containers on any node that has local disk available.
Login nodes have local disk by default.
To build on a compute node, we can reserve a job with local disk (NVMe).
Here is an example of an interactive job for building containers (change the `project_id` to your project ID):

```bash
srun \
    --account=project_id \
    --partition=interactive \
    --cpus-per-task=8 \
    --mem=16G \
    --gres=nvme:20 \
    --time=01:00:00 \
    --pty bash
```

### Temporary directory

The `TMPDIR` environment variable must point to the local disk.
Apptainer will use it to identify the directory as its temporary directory when building a container.
Puhti and Mahti cluster set the `TMPDIR` environment variable automatically on login nodes which have local disk by default and compute nodes when local disk is reserved.
Parallel file systems such as Lustre cannot (and should not) be used as the temporary directory.

### Cache directory

Apptainer caches layers and blobs such as base images to the cache directory.
The default location is in the home directory (`$HOME/.apptainer`) which on Puhti and Mahti has a limited quota.
Thus, we may want to change the cache location to projappl to avoid filling our home directory (modify the `project_id` to your project ID).

```bash
export APPTAINER_CACHEDIR=/projappl/project_id/$USER/.apptainer
```

We can also clean the cache directory if necessary:

```bash
apptainer cache clean
```

### Virtual memory limit

Virtual memory is limited on Puhti and Mahti login nodes is quite small and should be increased to the hard limit.
Exceeding the virtual memory limit causes memory errors during build.
You can query the current virtual memory limit using `ulimit -v` and the hard limit using `ulimit -Hv`.
On Puhti and Mahti login nodes, we can set the virtual memory limit to the hard limit as follows:

```bash
ulimit -v $(ulimit -Hv)
```

If your build runs out of memory, virtual memory or local disk space during the build on the login node, you should use an interactive job where virtual memory is unlimited and memory and local disk size can be configured.

### Building SIF image from existing Docker or OCI image

We can obtain existing container images from a container registry by pulling them.
Apptainer will convert them from Docker or OCI format into the Singularity Image Format (SIF).

```bash
apptainer build rockylinux.sif docker://docker.io/rockylinux/rockylinux:8
```

You can authenticate to a private registry using `apptainer registry login` command.

### Building SIF image from definition file

When building containers with fakeroot in an environment that does not have unprivileged usernamespaces available, many commands that assume higher privileges such as `useradd` and `groupadd` will fail.
These commands are typically executed as part of pre- or post-installation scripts of DEB and RPM packages.
We can work around many of these problems by using a host-compatible base image and replacing problematic commands with dummies that always succeed.

We can query information about the host system by reading the `/etc/os-release` file.

```bash
cat /etc/os-release
```

```text title="stdout"
NAME="Rocky Linux"
VERSION="8.10 (Green Obsidian)"
ID="rocky"
ID_LIKE="rhel centos fedora"
VERSION_ID="8.10"
...
```

Apptainer definition files are written using the `.def` file extension.
Here is a simple example of container definition that uses compatible base image and replaces the failing commands with the succeeding dummies:

```sh title="container.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:8.10

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

By default Apptainer bind mounts the host's `/tmp` to `/tmp` in the build environment.
However, the size of `/tmp` is limited on Puhti and Mahti, thus, we bind mount the local disk (`$TMPDIR`) to `/tmp` to avoid running out of memory.

### Developing with interactive sandbox

We can also build Apptainer sandboxes with fakeroot.
Sandboxes are useful for interactive development of containers.
The sandbox must be created on the local disk (`$TMPDIR`), not on the parallel file system (Lustre).

We can initialize a sandbox from a base image as follows:

```bash
apptainer build --fakeroot --sandbox "$TMPDIR/rockylinux" docker://docker.io/rockylinux/rockylinux:8.10
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

### Operating systems and package managers

Sometimes it may be necessary to build a container that uses a different Linux operating system than the host as the base image, for example, if software is developed and packaged only for that Linux operating system and it would require an unreasonable amount of effort to try to port to a different operating system.
The ability to build containers of a different Linux operating system than the host is limited when using fakeroot without unprivileged usernamespaces and the only way to figure out is to attempt to build the container.
Here are base images for some common Linux operating systems:

- RHEL compatible operating systems with DNF package manager:
    - [RedHat Universal Base Images (UBI)](https://catalog.redhat.com/en/software/base-images): [redhat/ubi8](https://hub.docker.com/r/redhat/ubi8), [redhat/ubi9](https://hub.docker.com/r/redhat/ubi9) 
    - [rockylinux](https://hub.docker.com/r/rockylinux/rockylinux)
    - [almalinux](https://hub.docker.com/_/almalinux)
- SUSE compatible operating systems with Zypper package manager:
    - [opensuse/leap](https://hub.docker.com/r/opensuse/leap)
- Debian compatible operating systems with APT package manager:
    - [debian](https://hub.docker.com/_/debian)
    - [ubuntu](https://hub.docker.com/_/ubuntu)

### Installing software into container

The typical pattern of installing software into a container is to start by using the system package manager such as DNF, APT or Zypper to install "system" software to `/usr` and then install software using a user-space package manager such as PIP, Conda or Spack or install software manually to `/usr/local` or in a unique directory under `/opt`.
Our container [Examples](./examples.md) demonstrates this pattern with different kinds of containerized software installations.

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
