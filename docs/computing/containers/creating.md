# Creating Singularity containers

CSC's supercomputers Puhti and Mahti support running [Singularity containers](https://sylabs.io/singularity/). If you wish to run a container-based application, first check the [application pages](../../apps/index.md) to see if a pre-installed container is already available. Also see our [documentation on how to run Singularity containers](run-existing.md).

If you cannot find a pre-built container, one option is to build your own. If a Docker container image already exists, you can often simply convert that to a Singularity container. Another option is to build your own container from scratch.  Both approaches will be discussed below. As always, if you have any problems or questions, don't hesitate to contact [CSC's Service Desk](https://www.csc.fi/en/contact-info).

## Converting a Docker container

If you already have an existing Docker container, in many cases it can easily be converted to a Singularity image. Docker container images can be found in public repositories such as [Docker Hub](https://hub.docker.com/), but **please take care to only use images uploaded from reputable sources** as these images can easily be a source of security vulnerabilities or even contain malicious code.

GPU-optimized containers can also be found in [NVIDIA's GPU cloud (NGC)](https://ngc.nvidia.com/). These containers have been prepared by NVIDIA, and should thus be safe.

Further [information about converting Docker containers to Singularity can be found in the Singularity documentation](https://sylabs.io/guides/3.6/user-guide/singularity_and_docker.html).

Here is an example of how to build a Singularity image from [NVIDIA's PyTorch Docker image](https://ngc.nvidia.com/catalog/containers/nvidia:pytorch). We'll use `sinteractive` as heavy processing should not be done in the login nodes.

```bash
# Let's start a 1 hour interactive job
sinteractive --account <project> --time 1:00:00

# Let's use the fast local drive for temporary storage
export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH

# This is just to avoid some annoying warnings
unset XDG_RUNTIME_DIR

# Change directory to where you wish to store the image
cd /projappl/<project>

# Do the actual conversion
# NOTE: the Docker image is downloaded straight from NGC
singularity build pytorch_21.03-py3.sif docker://nvcr.io/nvidia/pytorch:21.03-py3
```

Note that the Singularity image `.sif` files can easily be several GB in size, so they should not be stored in your home directory, but for example in the project application directory [projappl](/computing/disk).

Also see our [documentation on how to run Singularity containers](run-existing.md).

## Build a container from scratch

You can also build your own Singularity container from scratch. This is an option for more experienced users, and your main source of information is the [official Singularity documentation on building containers](https://sylabs.io/guides/3.6/user-guide/build_a_container.html).

You can find some help also by looking at our [tutorial on building Singularity containers from scratch](../../support/tutorials/singularity-scratch.md).
