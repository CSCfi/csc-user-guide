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
    * See our instructions for managing certificates: [Signing public SSH keys](https://csc-guide-preview.2.rahtiapp.fi/origin/roihu-quickstart/computing/connecting/ssh-keys/#signing-public-key)

For platform-specific instructions, see:

* [Instructions for Linux/macOS](../../computing/connecting/ssh-unix.md).
* [Instructions for Windows](../../computing/connecting/ssh-windows.md).

**[Read detailed instructions for creating and managing SSH keys and certificates](../../computing/connecting/ssh-keys.md).**

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

    **Importantly:**
    - Software compiled on Roihu-CPU nodes only works on Roihu-CPU nodes
    - Software compiled on Roihu-GPU nodes only works on Roihu-GPU nodes
    - This also applies to Python environments

    **All login nodes still share the same file system, so your files are accessible from all of them.**

### Roihu web interface (available after general availability)

The simplest way to connect to Roihu is to use the web interface.

1. Go to [www.roihu.csc.fi](https://www.roihu.csc.fi).
2. Log in using your Haka, Virtu or CSC user account.
   [Multi-factor authentication (MFA)](../../accounts/mfa.md) is required.

## Migrating research data

If you need to transfer data from Puhti or Mahti to Roihu, we require
that you:

1. Review your data carefully – **only move what you
   really need**
2. Check your available disk space on Roihu (for example, using the `csc-workspaces` command)
3. Transfer data **directly** from Puhti or Mahti to Roihu.

Note that previous extended disk quotas on Puhti or Mahti will not be automatically moved to Roihu. Quota extensions on Roihu must be separately applied for and properly motivated.

**[Read the detailed instructions in the Roihu data migration guide](roihu-data.md).**

## Installing software

Before installing anything:

1. Check if the software is already available:
   - [List of pre-installed applications](../apps/index.md)
   - `module spider <module name>`

If not available, choose one of the following approaches depending on your needs:

### Compiling C/C++/Fortran code

HPC software written using programming languages such as C, C++ or Fortran need to be compiled before installing.  
For instructions on the available compilers and preferred options, see the instructions for compiling software on:

- [Compiling on Roihu-CPU](../../computing/compiling-roihu.md#building-mpi-applications)
- [Compiling on Roihu-GPU](../../computing/compiling-roihu.md#building-gpu-applications)

### Containers

Roihu supports Apptainer/Singularity containers for container installations. 
In most cases, ready-made Docker containers can be easily converted into an Apptainer image.
Another option is to build your own container from scratch. 

More details on working with containers in CSC's computing environment can be found from the links below:

- [Overview of containers](containers/overview.md)
- [Running containers](containers/overview.md#running-containers)
- [Creating containers](containers/overview.md#building-container-images)
- [Tykky container wrapper](containers/tykky.md)

### Python/R environments

Best practice guidelines on installing your own Python and R packages can be found in the Python, R and Tykky container wrapper pages below.

- [Installing Python packages and environments](../support/tutorials/python-usage-guide.md)
- [Containerizing Conda and pip environments with Tykky](containers/tykky.md)
- [R package installations](../apps/r-env.md#r-package-installations)

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

1. [Available batch job partitions](batch-job-partitions.md)
2. [Creating a batch job script](creating-job-scripts-roihu.md)
3. [Submit a batch job](submitting-jobs.md)
4. [Performance checklist](performance-checklist.md)

For common Slurm error messages, see our FAQ on [Why does my batch job fail?](../faq/why-does-my-batch-job-fail.md).

### Known issues (pilot phase)

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

## More information

* [Roihu system overview](../../computing/systems-roihu.md)
* [CSC Computing Environment self-learning materials](https://csc-training.github.io/csc-env-eff/)
* [Contact our service desk](https://docs.csc.fi/support/contact/)