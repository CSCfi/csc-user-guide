# Building Singularity containers from scratch

On CSC platforms, there are two ways to use [Singularity containers](https://sylabs.io/singularity/) that you have built yourself. You may: 

* [Convert Docker containers to Singularity image files](../../computing/containers/creating.md#converting-a-docker-container), or 
* Build a Singularity image entirely from scratch.

This tutorial focuses on the latter scenario, with further information available on the [Singularity website](https://sylabs.io/guides/3.6/user-guide/build_a_container.html).

## Containers as distinct environments

One can think of Singularity containers as distinct environments of their own. For example, the Linux distribution used in the container may differ from that of the host environment where the container is executed. Singularity images also have an internal file system that is not visible outside of the container. Likewise, most of the host environment will not be visible to a container unless explicitly specified. Selected folders can be exposed to the container by using [bind mounts](https://sylabs.io/guides/3.0/user-guide/bind_paths_and_mounts.html).

When planning the contents and configuration of a Singularity container, a decision needs to be made on whether specific installations should be done within the container or added as bind mounts. For example, certain dependencies may already be present on the host. The container Linux distribution will naturally affect this decision.

Frequently the environment variables used within a container *versus* the host environment will also differ (more on that below). 

## Preparing a definition file

A definition file (with the extension .def) is a file containing the commands required to build a Singularity container. Examples of Singularity definition files used on CSC computing environments can be found in our [singularity-recipes repository](https://github.com/CSCfi/singularity-recipes). 

A definition file is split into sections serving different purposes ([see here for details](https://sylabs.io/guides/3.5/user-guide/definition_files.html)). At the very top of the file, one must provide a header specifying a bootstrap keyword and a Linux distribution. For example, to create a header for a CentOS 7.7 container, one would type:

```
Bootstrap: library
From: centos:7.7
```

The choice of Linux distribution defines the types of commands used in the definition file. For example, a CentOS container would use commands such as `yum -y install`, whereas an Ubuntu container would use commands such as `apt-get -y install`.

Other sections one can use include the following. Note that different sections can be added or left out, depending on your needs (e.g. if you have no external files to include in the container, there is no need for a `%files` section).

* `%labels` (e.g. name and contact of the image maintainer)
* `%files` (commands for copying external files into a specific location in the container)
* `%post` (section for software installation commands)
* `%environment` (environment variables defined upon launching the container)

#### A few words on environment variables

Environment variables can be defined in both the `%post` and `%environment` sections. Those specified in the former may be useful during software installations, but unlike variables specified under the `%environment` section, will not be visible upon launching the container.

If you wish to specify environment variables on the host environment in a way that is visible to the container, these must be preceded by `SINGULARITYENV_`. Variables without this prefix will not be passed onto the container.

## Building a container

Building a Singularity container requires root (`sudo`) access. As such, this cannot be directly done on CSC's supercomputers. Instead you can use your own computer or, for example, the [Sylabs Remote Builder](https://cloud.sylabs.io/builder) to build the container image.

Another option is to use a [Pouta virtual machine](../../cloud/pouta/index.md). This enables one to specify the type of environment used to build the image. Most of the time, the Linux distribution of the environment used to build the container will matter relatively little. However, certain installations (e.g. [NVIDIA CUDA drivers](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)) have strict version requirements with regard to kernel headers, meaning that the distribution must effectively be matched between the environment for container building, the container and the host.

To build a container using a definition file, one can simply run:

```
sudo singularity build container.sif recipe.def
```

If everything is successful, this results in a container image (.sif file) that can be moved onto your computing environment of choice. The image file is *immutable*, meaning that it can not be modified after the build step. It is also possible to create [writable sandbox directories](https://sylabs.io/guides/3.6/user-guide/build_a_container.html?highlight=sandbox#creating-writable-sandbox-directories) that can be used for testing (and can be subsequently converted into Singularity images).

## Running a container

There are a couple of ways to run Singularity containers on CSC computing environments. For detailed instructions, visit our documentation on [running containers](../../computing/containers/run-existing.md).

The options include using:

* `singularity exec`
* `singularity_wrapper exec` (wrapper script binding local folders, e.g. `TMPDIR`)

Many of the Singularity containers available on CSC environments come with wrappers for selected commands, enabling them to be executed without a need for the above. It is also possible to prepare wrappers for containers built from scratch, although this requires some familiarity with writing bash scripts.

## Moving containers onto CSC computing environments

#### Puhti and Mahti
Singularity image files can be transferred onto Puhti or Mahti [using `scp`, `rsync` or a graphical file transfer tool](../../data/moving/index.md). 

#### CSC Sensitive Data Desktop
If wishing to use a custom-built container on the [CSC Sensitive Data Desktop](../../data/sensitive-data/sd_desktop.md), first transfer the image file to Puhti. Then follow our guidelines on [using Allas to move containers to the SD Desktop](../../data/sensitive-data/sd-desktop-singularity.md).
