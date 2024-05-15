# Creating containers

CSC's supercomputers Puhti and Mahti support running [Apptainer containers](https://apptainer.org/) (formerly known as Singularity). If you wish to run a container-based application, first check the [application pages](../../apps/index.md) to see if a pre-installed container is already available. Also see our [documentation on how to run containers](run-existing.md).

If you cannot find a pre-built container, one option is to build your own. If a Docker container image already exists, you can often simply convert that to an Apptainer container. Another option is to build your own container from scratch.  Both approaches will be discussed below. As always, if you have any problems or questions, don't hesitate to contact [CSC's Service Desk](https://www.csc.fi/en/contact-info).

## Converting a Docker container

If you already have an existing Docker container, in many cases it can easily be converted to an Apptainer image. Docker container images can be found in public repositories such as [Docker Hub](https://hub.docker.com/), but **please take care to only use images uploaded from reputable sources** as these images can easily be a source of security vulnerabilities or even contain malicious code.

GPU-optimized containers can also be found in [NVIDIA's GPU cloud (NGC)](https://catalog.ngc.nvidia.com/). These containers have been prepared by NVIDIA, and should thus be safe.

Further [information about converting Docker containers can be found in the Apptainer documentation](https://apptainer.org/docs/user/main/docker_and_oci.html).

Here is an example of how to build an Apptainer image on Puhti from [NVIDIA's PyTorch Docker image](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch). We'll use `sinteractive` as heavy processing should not be done in the login nodes.

```bash
# Let's start a 1 hour interactive job with enough memory and local scratch space
sinteractive --account <project> --time 1:00:00 -m 16G --tmp 64

# Let's use the fast local drive for temporary storage
export APPTAINER_TMPDIR=$LOCAL_SCRATCH
export APPTAINER_CACHEDIR=$LOCAL_SCRATCH

# This is just to avoid some annoying warnings
unset XDG_RUNTIME_DIR

# Change directory to where you wish to store the image
cd /projappl/<project>

# Do the actual conversion
# NOTE: the Docker image is downloaded straight from NGC
apptainer build pytorch_22.09-py3.sif docker://nvcr.io/nvidia/pytorch:22.09-py3
```

Note that the Apptainer image `.sif` files can easily be several GB in size, so they should not be stored in your home directory, but for example in the project application directory [projappl](/computing/disk).

Also see our [documentation on how to run containers](run-existing.md).

## Build a container from scratch

You can also build your own container from scratch. This is an option for more experienced users, and your main source of information is the [official Apptainer documentation on building containers](https://apptainer.org/docs/user/main/build_a_container.html).

You can find some help also by looking at our [tutorial on building Apptainer containers from scratch](../../support/tutorials/singularity-scratch.md).

## Building a container without sudo access on Puhti and Mahti

Root access into Puhti and Mahti is not permitted. Namespaces have also been disabled due to security issues involved. However, with a few restrictions, Apptainer can still be used by an unprivileged user to build a container using the [fakeroot](https://apptainer.org/docs/user/main/fakeroot.html) feature.

Apptainer enables `--fakeroot` flag by default when building containers if `sudo` or namespaces are not available, this makes the user appear as `root:root` while building the container, thus enabling them to build images that require root file permissions e.g. to install packages via `apt`.
However, this only makes the user *appear* as the root user, in the host system a user still has no additional permissions. By itself, fakeroot is not always sufficient, and building some containers may fail due to various reasons. For more details see the [official Apptainer documentation](https://apptainer.org/docs/user/main/fakeroot.html).

The following simple example definition file (saved as `ubuntu.def`) creates an image based on Ubuntu 22.04 with one package installed.

```text title="ubuntu.def"
Bootstrap: docker
From: ubuntu:22.04
%post
	apt-get update
	apt-get install -y cowsay
```

The image can be built with `apptainer build ubuntu.sif ubuntu.def` and ran as `apptainer shell ubuntu.sif`. Now, the installed package can be accessed in the shell opened by typing `echo hello | /usr/games/cowsay`. Note that `sudo` is not required to run these commands.

Below is a table of common docker base images and whether installing simple packages with the distribution's default package manager works on them in Puhti and Mahti:

|Image|Tag|Works|
|-----|---|-----|
|alpine|3.6-3.19|no|
|almalinux|8-9|yes|
|debian|buster-trixie|yes|
|centos|7|yes|
|opensuse/leap|15.0,15.6|no|
|opensuse/leap|15.1-15.5|yes|
|redhat/ubi|8-9|yes|
|ubuntu|16.04-22.04|yes|

Some issues related to, for example, glibc, fakeroot, file permissions and old remote repos are often difficult to solve, so trying out a few different base images can be a good idea before spending a lot of time debugging.
