# Getting started with Roihu

This guide assumes familiarity with CSC supercomputers such as Puhti, Mahti or LUMI.

If you are new to CSC systems, start with the [getting started with supercomputing guide](hpc-quick.md).

To access Roihu, you need a CSC user account and a project with the Roihu service
enabled. [Read more about CSC accounts and projects](../../accounts/index.md).

[TOC]

!!! info "Key differences compared to Puhti and Mahti"
    Before you begin, note the following important differences:

    - **SSH authentication requires short-lived certificates (24h)**
    - **Separate login nodes and CPU architectures for CPU (x86) and GPU (ARM) environments**
    - Software built on CPU nodes cannot be used on GPU nodes (and vice versa)
    - Disk quota extensions are **not automatically transferred** from earlier projects on Puhti/Mahti

    These differences affect most workflows, so read the sections below carefully.

## Add Roihu as a service

Before you start using Roihu, you need to enable it as a service for your project in MyCSC.

### Project managers

If you already have a computational project, for example for Mahti or Puhti,
you can add Roihu there as a service.

If you do not have a computing project yet, apply for one in MyCSC following the instructions
for [creating a new project](../../accounts/how-to-create-new-project.md).

Adding Roihu as a service:

1. Go to my.csc.fi and log in e.g. with your HAKA identification
2. Go to the "Profile" section, and in the bottom right corner, check that your Level of identity assurance (LoA) is **medium** or **high**
    - If your LoA is **low**, you need to raise it to access Roihu. See the [instructions for raising LoA](../../accounts/strong-identification.md).
3. Go to the "Projects" section, and open your project.
4. In the right-side Services tab, click the "+ Add services" option.
5. Choose Roihu, click Next and confirm this option.

Note that it may take a few minutes for Roihu to become accessible for you,
and the other project members.

??? info "What if I need more disk quota on Roihu?"
     The default disk quotas are more restrictive on Roihu, than on Mahti and Puhti.

     |            |Capacity|Number of files|
     |------------|--------|---------------|
     |**home**    |15 GiB  |150 000 files  |
     |**projappl**|15 GiB  |150 000 files  |
     |**scratch** |250 GiB |500 000 files  |

     After adding the Roihu service for your project, you can apply for a disk quota increase for the project in MyCSC.

     1. In MyCSC, go to your project where you have Roihu enabled.
     2. In the "Services" tab, find Roihu and click **Configure**.
     3. In "Quota settings", specify how much quota you require, and justify your request in the text box.

     See the ["increasing disk quotas" section](../../accounts/how-to-increase-disk-quotas.md) for
     details and the maximum disk quotas you can apply for.

### Project members

After your project manager has applied for the Roihu service,
you will get an email titled "Roihu supercomputer for your use".

Next, accept the terms of service for Roihu, with the following instructions:

1. Go to my.csc.fi and log in e.g. with your HAKA identification
2. Go to the "Profile" section, and in the bottom right corner, check that your Level of identity assurance (LoA) is **medium** or **high**
    - If your LoA is **low**, you need to raise it to access Roihu. See the [instructions for raising LoA](../../accounts/strong-identification.md).
3. Go to the "Projects" section, and open your project.
4. In the right-side Services tab, click open Roihu
5. Accept the terms of service.

After adding Roihu to your project, you can connect to the system.
Note that there may be a short delay of a few minutes before you can connect.

## Connecting

Connect to Roihu using either:

* [SSH client](#ssh-client)
* [Roihu web interface (available after general availability)](#roihu-web-interface)

### SSH client

To connect via SSH:

1. Set up SSH keys (same as Puhti/Mahti)
2. **New:** _Sign_ your public key and download a _certificate_
    * Certificates are valid for **24 hours**
    * See our instructions for managing certificates: [Signing public SSH keys](../../computing/connecting/ssh-keys.md#signing-public-key)

For platform-specific instructions, see:

* [Instructions for Linux/macOS](../../computing/connecting/ssh-unix.md).
* [Instructions for Windows](../../computing/connecting/ssh-windows.md).

**[Read detailed instructions for managing SSH keys and certificates](../../computing/connecting/ssh-keys.md).**

!!! warning "Separate CPU and GPU environments"
    Roihu has
    [different CPU architectures on Roihu-CPU (x86) and Roihu-GPU (ARM)](../../computing/systems-roihu.md#compute).
    Therefore, there are separate login nodes for building programs and submitting
    jobs to their respective nodes:
    
    1. **`roihu-cpu.csc.fi`**
    2. **`roihu-gpu.csc.fi`**
    
    Connecting example (Roihu-CPU):

    ```bash
    # Replace <username> with the name of your CSC user account.

    ssh <username>@roihu-cpu.csc.fi
    ```

    **Importantly:**<br>
    - Software compiled on Roihu-CPU nodes only works on Roihu-CPU nodes<br>
    - Software compiled on Roihu-GPU nodes only works on Roihu-GPU nodes<br>
    - This also applies to Python environments<br>

    **All login nodes still share the same file system, so your files are accessible from all of them.**

### Roihu web interface

The simplest way to connect to Roihu is to use the web interface.

1. Go to [www.roihu.csc.fi](https://www.roihu.csc.fi).
2. Log in using your HAKA, Virtu or CSC user account.
   [Multi-factor authentication (MFA)](../../accounts/mfa.md) is required.

## Migrating research data

If you need to transfer data from Puhti or Mahti to Roihu, we require
that you:

1. Review your data carefully – **only move what you really need**
2. Check your available disk space on Roihu (for example, using the `csc-workspaces` command)
3. Transfer data **directly** from Puhti or Mahti to Roihu.

Note that previous extended disk quotas on Puhti or Mahti will not be automatically moved to Roihu.
Quota extensions on Roihu must be separately applied for and properly motivated.

**[Read the detailed instructions in the Roihu data migration guide](roihu-data.md).**

## Installing software

Before installing anything, check if the software is already available:

- [List of pre-installed applications](../../apps/by_availability.md#roihu)
- `module spider <software name>`

If the software is not available as a module, choose one of the following approaches depending on your needs:

### Compiling C/C++/Fortran code

HPC software written using programming languages, such as C, C++, or Fortran need to be compiled before installing.

For instructions on the available compilers and preferred options, see the instructions for compiling software on:

- [Compiling on Roihu-CPU](../../computing/compiling-roihu.md#compiling-on-roihu-cpu)
- [Compiling on Roihu-GPU](../../computing/compiling-roihu.md#compiling-on-roihu-gpu)

### Containers

Roihu supports Apptainer/Singularity containers for container installations. 
In most cases, ready-made Docker containers can be easily converted into an Apptainer image.
Another option is to build your own container from scratch. 
You can build containers on top of Roihu base containers, which have the same software stack as is available via the module system natively.
Base containers are built on top of Rocky Linux 9.

---

=== "Roihu CPU base container (~4 GB)"
    Base containers are available:

    - `satama.csc.fi/r_installation_spack/core-cpu-gcc-15.2.0:v2026_03`

    Build definition file:

    ```sh title="container.def"
    Bootstrap: docker
    From: satama.csc.fi/r_installation_spack/core-cpu-gcc-15.2.0:v2026_03

    %post
        # Activate module environment and load default modules.
        . /opt/activate.sh
        # Build your application here:

    %runscript
        . /opt/activate.sh
        exec "$@"
    ```

    When building the containers, set the Apptainer cache directory to `$TMPDIR` to avoid filling your home directory quota.

    ```bash
    export APPTAINER_CACHEDIR=$TMPDIR
    apptainer build --fakeroot container.sif container.def
    ```

    Now, you can run commands inside the container with the environment active as follows:

    ```bash
    apptainer run container.sif mycmd
    ```

=== "Roihu GPU base container (~16 GB)"
    Base containers are available:

    - `satama.csc.fi/r_installation_spack/core-gpu-gcc-15.2.0-cuda-13.1.1:v2026_03`
    - `satama.csc.fi/r_installation_spack/core-gpu-gcc-14.3.0-cuda-12.9.1:v2026_03`
    - `satama.csc.fi/r_installation_spack/core-gpu-gcc-13.4.0-cuda-12.6.3:v2026_03`

    Build definition file:

    ```sh title="container.def"
    Bootstrap: docker
    From: satama.csc.fi/r_installation_spack/core-gpu-gcc-14.3.0-cuda-12.9.1:v2026_03

    %post
        # Activate module environment and load default modules.
        . /opt/activate.sh
        # Build your application here:

    %runscript
        . /opt/activate.sh
        exec "$@"
    ```

    When building the containers, set the Apptainer cache directory to `$TMPDIR` to avoid filling your home directory quota.

    ```bash
    export APPTAINER_CACHEDIR=$TMPDIR
    apptainer build --fakeroot container.sif container.def
    ```

    Now, you can run commands inside the container with the environment active as follows:

    ```bash
    apptainer run --nv container.sif mycmd
    ```

=== "Roihu ML/AI GPU base containers"
    Base containers for machine learning/AI are available.
    
    These containers are built on Rocky Linux 9.7 with Python 3, MPI and CUDA installed via RPM packages.
    *This approach produces a container that is not identical to Roihu's host system, but may be easier to extend in some cases than the normal base containers.*
    
    - `satama.csc.fi/r_installation_aida/ml-base:rocky9.7_gcc12_py3.12_cuda12.9`
    - `satama.csc.fi/r_installation_aida/ml-base:rocky9.7_gcc12_py3.12_cuda13`
    - `satama.csc.fi/r_installation_aida/pytorch-base:2.10_cuda13_roihu` - `ml-base` image with basic PyTorch 2.10 packages added
    - `satama.csc.fi/r_installation_aida/pytorch:2.10_cuda13_roihu` - full PyTorch installation (same as CSC module)
    - `satama.csc.fi/r_installation_aida/vllm:0.19.1_cuda12.9_roihu` - vLLM container (same as CSC module)

    Build definition file:

    ```sh title="container.def"
    Bootstrap: docker
    From: satama.csc.fi/r_installation_aida/ml-base:rocky9.7_gcc12_py3.12_cuda13

    %post
        # Build your application here:
    ```

    When building the containers, set the Apptainer cache directory to `$TMPDIR` to avoid filling your home directory quota.

    ```bash
    export APPTAINER_CACHEDIR=$TMPDIR
    apptainer build --fakeroot container.sif container.def
    ```

    Now, you can run commands inside the container. For example, to launch python3:

    ```bash
    apptainer exec --nv --bind=$(csc-common-bind) container.sif python3
    ```

---

More details on working with containers in CSC's computing environment can be found from the links below:

- [Overview of containers](../../computing/containers/overview.md)
- [Running containers](../../computing/containers/overview.md#running-containers)
- [Creating containers](../../computing/containers/overview.md#building-container-images)
- [Tykky container wrapper](../../computing/containers/tykky.md)

### Spack

Spack is a flexible package manager that can be used to install software on supercomputers and Linux and macOS systems.
The basic module tree including compilers, MPI libraries and many of the available software on CSC supercomputers have been installed using Spack.
Spack is similar to the EasyBuild package manager extensively used on LUMI.

CSC provides user Spack modules on Roihu, that can be used to build software on top of the available compilers and libraries.
It is also possible to install different customized versions of packages available in the module tree for special use cases.

[See here for a short tutorial on how to install software on Roihu using Spack.](roihu-user-spack.md)

### Python/R environments

Best practice guidelines on installing your own Python and R packages can be found in the Python, R and Tykky container wrapper pages below.

- [Installing Python packages and environments](../tutorials/python-usage-guide.md)
- [Containerizing Conda and pip environments with Tykky](../../computing/containers/tykky.md)
- [R package installations](../../apps/r-env.md#r-package-installations)

## Running your first job

Roihu uses Slurm, similarly to Puhti and Mahti.

Basic workflow:

1. Create a job script where you
    * Define the resources for your job (time, memory, cores)
    * Load the required modules
    * Launch your executable
2. Submit your batch job to the queuing system
3. Wait for the job to finish, and look for its output

See the relevant documentation below for detailed information:

1. [Available batch job partitions](../../computing/running/batch-job-partitions.md)
1. [Creating a batch job script](../../computing/running/creating-job-scripts-roihu.md)
1. [Example job scripts](../../computing/running/example-job-scripts-roihu.md)
1. [Submit a batch job](../../computing/running/submitting-jobs.md)
1. [Performance checklist](../../computing/running/performance-checklist.md)

For common Slurm error messages, see our FAQ on [Why does my batch job fail?](../faq/why-does-my-batch-job-fail.md).

## More information

* [Roihu system overview](../../computing/systems-roihu.md)
* [CSC Computing Environment self-learning materials](https://csc-training.github.io/csc-env-eff/)
* [Contact our service desk](../contact.md)