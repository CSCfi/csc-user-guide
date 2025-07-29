# Containers (updated)

In this section, we provide instructions on how to build and run containers using [Apptainer](https://apptainer.org/) with fakeroot enabled in HPC clusters without unprivileged usernamespaces.
We explain the special aspects of building and running containers on Puhti and Mahti clusters including how to set up the build environment, how to invoke the build commands, how to write container definition files and how to run containers on the clusters.
For general instructions about building and running containers, we recommend that users read the official [Apptainer documentation](https://apptainer.org/docs/user/main/index.html).

## Running containers

We can obtain a container by either pulling an existing container or by building a container.

Assume we have `container.sif`

```bash
apptainer exec container.sif bash
```

```bash
apptainer exec --bind="/users,/projappl,/scratch,$TMPDIR,$LOCAL_SCRATCH" container.sif bash
```

## Building containers

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
Puhti and Mahti cluster set the `TMPDIR` enviroment variable automatically on login nodes and compute nodes when local disk is reserved.
Parallel file systems such as Lustre cannot (and should not) be used as the temporary directory.

### Cache directory

Apptainer caches layers and blobs such as base images to the cache directory.
The default location is in the home directory which on Puhti and Mahti has a limit quota.
Thus, we may want to change the cache location to projappl or temporary directory.

```bash
# Change to temporary directory
export APPTAINER_CACHEDIR=$TMPDIR

# Change to projappl
export APPTAINER_CACHEDIR=/projappl/project_id/$USER
```

We can also clean the cache directory if necessary:

```bash
apptainer cache clean
```

### Virtual memory limit

If the virtual memory is limited, exceeding it memory causes memory errors during build.
Virtual memory is limit on Puhti and Mahti login nodes is quite small and should be increased to the hard limit.
You can check and modify virtual memory limits as follows:

```bash
# Query the current virtual memory limit in kB
ulimit -v
```

```bash
# Query the hard limit for virtual memory in kB
ulimit -Hv
```

```bash
# Set virtual memory limit to the hard limit
ulimit -v $(ulimit -Hv)
```

If your build runs out of memory, virtual memory or local disk space during the build on the login node, you should use an interactive job.
Virtual memory has no limit in interactive job and memory and local disk size can be configured.

### Build definition file and invoking the build command

When building containers on environment that does not have unprivileged usernamespaces available, many commands that assume higher privileges such as `useradd` and `groupadd` will fail.
These command are typically executed as part of pre or post installation scripts of DEB and RPM packages.
We can workaround many of these problems by using host compatible base image and replacing problematic commands with dummies that always succeed.

We can query information about the host system by reading the `/etc/os-release` file.

```text
$ cat /etc/os-release
NAME="Rocky Linux"
VERSION="8.10 (Green Obsidian)"
ID="rocky"
ID_LIKE="rhel centos fedora"
VERSION_ID="8.10"
...
```

Container definition file named `container.def`:

```sh
# Use host compatible base image.
Bootstrap: docker
From: rockylinux/rockylinux:8.10

%post
    # Replace the failing commands with always succeeding dummies.
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd
    # Install software with the system package manager.
    dnf -y update
```

We can invoke Apptainer to build the container (`container.sif`) from the definition file (`container.def`) using fakeroot as follows:

```bash
apptainer build \
    --fakeroot \
    --bind="$TMPDIR:/tmp" \
    container.sif container.def
```

By default Apptainer bind mounts the host's `/tmp` to `/tmp` in the build environment.
However, the size of `/tmp` is limited on Puhti and Mahti, thus, we bind mount the local disk (`$TMPDIR`) to `/tmp` to avoid running out of memory.

## Complete example of building and running a container

Here is a complete example of building and running a container on Puhti or Mahti.

```sh
#TODO
```
