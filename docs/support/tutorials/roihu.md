# Getting started with Roihu

This guide assumes familiarity with CSC supercomputers such as Puhti, Mahti or LUMI.

If you are new to CSC systems, start with the [getting started with supercomputing guide](hpc-quick.md).

To access Roihu, you need a CSC user account and a project with the Roihu service
enabled. [Read more about CSC accounts and projects](../../accounts/index.md).

[TOC]

!!! info "Key differences compared to Puhti and Mahti"
    Before you begin, note the following important differences:

    - **SSH authentication requires short-lived certificates (24h)**
    - **Separate login nodes for CPU and GPU environments**
    - Software built on CPU nodes cannot be used on GPU nodes (and vice versa)
    - Disk quota extensions are **not automatically transferred** from earlier projects on Puhti/Mahti

    These differences affect most workflows, so read the sections below carefully.

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
    [different CPU architectures on Roihu-CPU and Roihu-GPU](../../computing/systems-roihu.md#compute).
    Hence, there are separate login nodes for building programs and submitting
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

!!! warning "Roihu web interface availability during the pilot period"
     Roihu web interface will only be vailable after General Availability. Please connect via SSH during the pilot phase.
     

The simplest way to connect to Roihu is to use the web interface.

1. Go to [www.roihu.csc.fi](https://www.roihu.csc.fi).
2. Log in using your Haka, Virtu or CSC user account.
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

Before installing anything check if the software is already available:

- [List of pre-installed applications](../../apps/by_availability.md#roihu)
- `module spider <software name>`

If not available, choose one of the following approaches depending on your needs:

### Compiling C/C++/Fortran code

HPC software written using programming languages such as C, C++ or Fortran need to be compiled before installing.  
For instructions on the available compilers and preferred options, see the instructions for compiling software on:

- [Compiling on Roihu-CPU](../../computing/compiling-roihu.md#compiling-on-roihu-cpu)
- [Compiling on Roihu-GPU](../../computing/compiling-roihu.md#compiling-on-roihu-gpu)

### Containers

Roihu supports Apptainer/Singularity containers for container installations. 
In most cases, ready-made Docker containers can be easily converted into an Apptainer image.
Another option is to build your own container from scratch. 
You can build containers on top of Roihu base containers which have the same software stack as is available via the module system natively.
Base container are built on top of Rocky Linux 9.

!!! warning "Work in progress"
    Satama is not yet available on Roihu, so the container images
    referenced below cannot currently be accessed.
    Satama support on Roihu is expected very soon.

=== "Roihu CPU base container (~4 GB)"
    Base containers available:

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

    When building containers, set the Apptainer cache directory to `$TMPDIR` to avoid filling your home directory quota.

    ```bash
    export APPTAINER_CACHEDIR=$TMPDIR
    apptainer build --fakeroot container.sif container.def
    ```

    Now, you can run commands inside the container with clean environment and environment active as follows:

    ```bash
    apptainer run container.sif mycmd
    ```

=== "Roihu GPU base container (~16 GB)"
    Base containers available:

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

    When building the containers, set you cache directory to temporary directory to avoid filling you home directory quota.

    ```bash
    export APPTAINER_CACHEDIR=$TMPDIR
    apptainer build --fakeroot container.sif container.def
    ```

    Now, you can run commands inside the container with clean environment and environment active as follows:

    ```bash
    apptainer run --nv container.sif mycmd
    ```

=== "Roihu ML/AI GPU base container (~8 GB)"
    Base containers for machine learning/AI available.
    
    Built on Rocky Linux 9.7 with Python 3, MPI and CUDA installed traditionally via RPMs.
    *This approach gives a container that is not identical to Roihu's host system, but may be easier to extend in some cases.*
    

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

    When building the containers, set you cache directory to temporary directory to avoid filling you home directory quota.

    ```bash
    export APPTAINER_CACHEDIR=$TMPDIR
    apptainer build --fakeroot container.sif container.def
    ```

    Now, you can run commands inside the container. For example to launch python3:

    ```bash
    apptainer exec --nv --bind=$(csc-common-bind) container.sif python3
    ```

More details on working with containers in CSC's computing environment can be found from the links below:

- [Overview of containers](../../computing/containers/overview.md)
- [Running containers](../../computing/containers/overview.md#running-containers)
- [Creating containers](../../computing/containers/overview.md#building-container-images)
- [Tykky container wrapper](../../computing/containers/tykky.md)

### Spack

Spack is a flexible package manager that can be used to install software on supercomputers and Linux and macOS systems. The basic module tree including compilers, MPI libraries and many of the available software on CSC supercomputers have been installed using Spack. Spack is similar to the EasyBuild package manager extensively used on LUMI.

CSC provides user Spack modules on Roihu, that can be used to build software on top of the available compilers and libraries. It is also possible to install different customized versions of packages available in the module tree for special use cases.

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
2. Submit your batch job into the queuing system
3. Wait for the job to finish, and look for its output

See the relevant documentation below for detailed information:

1. [Available batch job partitions](../../computing/running/batch-job-partitions.md)
1. [Creating a batch job script](../../computing/running/creating-job-scripts-roihu.md)
1. [Example job scripts](../../computing/running/example-job-scripts-roihu.md)
1. [Submit a batch job](../../computing/running/submitting-jobs.md)
1. [Performance checklist](../../computing/running/performance-checklist.md)

For common Slurm error messages, see our FAQ on [Why does my batch job fail?](../faq/why-does-my-batch-job-fail.md).

### Known issues (pilot phase)

#### Argos errors

During the pilot phase, you may encounter multiple warnings or errors related to *Argos* in your Slurm job output, for example:

```
error: argos:slurm_spank_task_init: get_env_var: cannot get SLURM_ARGOS_SPANK_OPT from job(22474) environment (No such environment variable)
```

These messages are **harmless** and do not affect your job execution.
Your job will continue normally with Argos disabled.

If your job completes successfully, you can safely ignore these messages.

To suppress most of the Argos related warnings and errors, you can pass the `--argos=no` flag option to srun in the following manner:

```bash
#!/bin/bash
#SBATCH --account=<project_id>
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=DD:HH:MM

srun --argos=no <your-executable>
```

The same option can also be passed as an `#SBATCH` input.

## More information

* [Roihu system overview](../../computing/systems-roihu.md)
* [CSC Computing Environment self-learning materials](https://csc-training.github.io/csc-env-eff/)
* [Contact our service desk](../contact.md)
