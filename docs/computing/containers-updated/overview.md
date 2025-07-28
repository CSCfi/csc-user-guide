# Containers (updated)

In this section, we provide instructions on how to build and run containers using Apptainer with fakeroot enabled in a HPC enviroment without unprivileged usernamespaces.
Puhti and Mahti clusters are examples of such environments.


## Building containers
Building container requires setting appropriate build environment, using appropriate build commands and writing one or more container definition files.

### Temporary directory and local disk
We can build containers on the login node or compute node, as long as the node has local disk available.
The `TMPDIR` environment variable must point to the local disk.
Apptainer will use it to identify the directory as its temporary directory when building a container.
Puhti and Mahti cluster set `TMPDIR` automatically on login nodes and compute nodes when local disk (NVMe) is reserved.
Parallel file systems such as Lustre cannot and should not be used as the temporary dirctory.

### Virtual memory
Virtual memory is limited on the login nodes and exceeding it causes memory errors.
You can check and modify virtual memory limits as follows:

```bash
# Current virtual memory limit in kB
ulimit -v
```

```bash
# Hard limit for virtual memory in kB
ulimit -Hv
```

```bash
# Set virtual memory limit to the hard limit
ulimit -v $(ulimit -Hv)
```

### Increase resources using an interactive job
If your build runs out of memory, virtual memory or local disk space during the build on the login node, you should use an interactive job.
Virtual memory has no limit in interactive job and memory and local disk size can be configured:

```bash
srun \
    --account=project_2001659 \
    --partition=interactive \
    --cpus-per-task=8 \
    --mem=16G \
    --gres=nvme:20 \
    --time=01:00:00 \
    --pty bash
```

### Binding temporary directory during build
In HPC clusters the `/tmp` directory may have limited size.
In the build script we should bind mount the local disk to `/tmp` to avoid running out of memory if the container build process writes data to it.

```bash
apptainer build \
    --fakeroot \
    --bind="$TMPDIR:/tmp" \
    --env="TMPDIR=/tmp" \
    container.sif container.def
```

### Build definition



## Running containers

