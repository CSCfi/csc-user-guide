# Building Apptainer containers from scratch

On CSC platforms, there are two ways to create
[Apptainer containers](https://apptainer.org/) (formerly known as Singularity).
You may:

1. [Convert Docker containers to Apptainer image files](../../computing/containers/creating.md#converting-a-docker-container),
   or
2. Build an Apptainer image entirely from scratch.

This tutorial focuses on the latter scenario, with further information
available on the
[Apptainer website](https://apptainer.org/docs/user/main/build_a_container.html).

## Containers as distinct environments

One can think of containers as distinct environments of their own. For example,
the Linux distribution used in the container may differ from that of the host
environment where the container is executed. Apptainer images also have an
internal file system that is not visible outside the container. Likewise, most
of the host environment will not be visible to a container unless explicitly
specified. Selected folders on the host can be exposed to the container by
using
[bind mounts](https://apptainer.org/docs/user/main/bind_paths_and_mounts.html).

When planning the contents and configuration of an Apptainer container, a
decision needs to be made on whether specific installations should be done
within the container or added as bind mounts. For example, certain dependencies
may already be present on the host. The container Linux distribution will
naturally affect this decision.

Frequently, the environment variables used within a container *versus* the host
environment will also differ (more on that below).

## Preparing a definition file

A definition file (with the extension `.def`) is a file containing the commands
required to build the container. Examples of definition files used in CSC's
computing environment can be found in our
[singularity-recipes repository](https://github.com/CSCfi/singularity-recipes).

A definition file is split into sections serving different purposes
([see here for details](https://apptainer.org/docs/user/main/definition_files.html)).
At the very top of the file, one must provide a header specifying a bootstrap
keyword and a Linux distribution. For example, to create a header for an Ubuntu
22.04 container, one would type:

```dockerfile
Bootstrap: docker
From: ubuntu:22.04
```

The choice of Linux distribution defines the types of commands used in the
definition file. For example, a CentOS container would use commands such as
`yum -y install`, whereas an Ubuntu container would use commands such as
`apt-get -y install`.

Other sections one can use include the following:

* `%labels` (e.g. name and contact of the image maintainer).
* `%files` (commands for copying external files into a specific location in the
  container).
* `%post` (section for software installation commands).
* `%environment` (environment variables defined upon launching the container).

Note that different sections can be added or left out depending on your needs.
For example, if you have no external files to include in the container, there
is no need for a `%files` section.

### A few words on environment variables

Environment variables can be defined in both the `%post` and `%environment`
sections. Those specified in the former may be useful during software
installations, but unlike variables specified under the `%environment` section,
they will not be visible upon launching the container.

If you wish to specify environment variables on the host environment in a way
that is visible to the container, these must be preceded by `APPTAINERENV_`.
Variables without this prefix will not be passed to the container.

## Building a container

Building an Apptainer container requires root (`sudo`) access. However, on CSC
supercomputers, where users do not have root privileges, you may use the
[fakeroot](https://apptainer.org/docs/user/main/fakeroot.html) feature to
circumvent this requirement (with a few restrictions).
[See our documentation on creating containers for more details](../../computing/containers/creating.md#building-a-container-without-sudo-access-on-puhti-and-mahti).

Alternatively, you may use your own computer, or a virtual machine where you
have root access, to build a container image. One option is to use a
[Pouta virtual machine](../../cloud/pouta/index.md). This enables one to
specify the type of environment used to build the image. Most of the time, the
Linux distribution of the environment used to build the container will matter
relatively little. However, certain installations (e.g.
[Nvidia CUDA drivers](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html))
have strict version requirements with regard to kernel headers, meaning that
the distribution must effectively be matched between the environment for
container building, the container and the host.

To build a container using a definition file, one can simply run:

```bash
sudo apptainer build container.sif recipe.def
```

or without `sudo` using the `--fakeroot` option:

```bash
apptainer build --fakeroot container.sif recipe.def
```

!!! info "Note"
    In older versions of Linux the command may be `singularity` instead of
    `apptainer`.

If everything is successful, this results in a container image (`.sif` file)
that can be moved to your computing environment of choice. The image file is
*immutable*, meaning that it can not be modified after the build step. It is
also possible to create
[writable sandbox directories](https://apptainer.org/docs/user/main/build_a_container.html#creating-writable-sandbox-directories)
that can be used for testing (and can be subsequently converted into Apptainer
images).

## Running a container

There are a couple of ways to run Apptainer containers in CSC's computing
environment. For detailed instructions, visit our documentation on
[running containers](../../computing/containers/run-existing.md).

The options include using:

* `apptainer exec`
* `apptainer_wrapper exec` (wrapper script that binds commonly used local
  folders, e.g. `$TMPDIR`)

Many of the containers available in CSC's computing environment come with
wrappers for selected commands, enabling them to be executed without a need for
the above. It is also possible to prepare wrappers for containers built from
scratch, although this requires some familiarity with writing Bash scripts. We
do also provide a
[container wrapper tool "Tykky"](../../computing/containers/tykky.md) that can
be used to easily containerize and create wrappers for Python environments.

## Moving containers to CSC's computing environment

### Puhti, Mahti and LUMI

Apptainer image files can be transferred to Puhti, Mahti or LUMI using e.g.
[`scp`, `rsync` or a graphical file transfer tool](../../data/moving/index.md).

### CSC Sensitive Data Desktop

If you wish to use a custom-built container on the
[CSC Sensitive Data Desktop](../../data/sensitive-data/sd_desktop.md), first
transfer the image file to Puhti. Then, follow our guidelines on
[using Allas to move containers to the SD Desktop](../../data/sensitive-data/sd-desktop-singularity.md).

## More information

* [Working with containers in CSC's computing environment](../../computing/containers/overview.md)
* [Creating containers with Tykky](../../computing/containers/tykky.md)
