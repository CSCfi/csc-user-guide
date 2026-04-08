# Getting started with Roihu

This is a quickstart guide for Roihu users. It is assumed that you have
previously used CSC supercomputing resources like Puhti, Mahti or LUMI. If not,
you can start by looking at our general
[getting started with supercomputing guide](hpc-quick.md). We also recommend
checking the
[CSC Computing Environment self-learning course materials](https://csc-training.github.io/csc-env-eff/).

To access Roihu, you need a CSC user account and a project with the Roihu service
enabled. [Read more here](../../accounts/index.md).

[TOC]

## Connecting

Connect to Roihu using either:

* [SSH client](#ssh-client)
* [Roihu web interface (available after general availability)](#roihu-web-interface)

### SSH client

Connecting to Roihu using an SSH client requires that you:

1. Set up SSH keys and add your public key to MyCSC (like on Puhti & Mahti).
2. **New:** _Sign_ your public key and download a _certificate_ for authentication.
    * Each certificate is valid for 24 hours, after which a new one must be
      generated.

**[Read detailed instructions for managing SSH keys and certificates](../../computing/connecting/ssh-keys.md).**

Once you have set up SSH keys and obtained a valid SSH certificate, connect
using an SSH client:

* [Instructions for Linux/macOS](../../computing/connecting/ssh-unix.md).
* [Instructions for Windows](../../computing/connecting/ssh-windows.md).

!!! info "Separate login nodes for CPU and GPU partitions"
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

    Please observe that software built on `roihu-cpu.csc.fi` can only be run on
    the CPU nodes, while software built on `roihu-gpu.csc.fi` can only be run
    on the GPU nodes. Importantly, this applies also to Python environments.

    **All login nodes still share the same file system, so your files are accessible from all of them.**

### Roihu web interface

The simplest way to connect to Roihu is to use the web interface.

1. Go to [www.roihu.csc.fi](https://www.roihu.csc.fi).
2. Log in using your Haka, Virtu or CSC user account.
   [Multi-factor authentication (MFA)](../../accounts/mfa.md) is required.

## Migrating research data

If you need to transfer data from Puhti or Mahti to Roihu, we require
that you:

1. Review your data carefully – **only move what you
   really need and check that you have enough space available on Roihu!**
   Note that extended disk quotas from Puhti or Mahti are not automatically transferred.
   Quota extensions on Roihu must be applied for separately.
2. Transfer data **directly** from Puhti or Mahti to Roihu.

**[Read the detailed instructions in the Roihu data migration guide](roihu-data.md).**

## Installing software

For instructions on the available compilers and preferred options, see the instructions for compiling software on:

- [Compiling on Roihu-CPU](../../computing/compiling-roihu/)
- [Compiling on Roihu-GPU](../../computing/compiling-roihu/)

## Running your first job

For more examples, see [Roihu example Slurm job scripts](../../computing/example-job-scripts-roihu.md)

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
#SBATCH --account=project_2001659
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=DD:HH:MM

srun --argos=no <your-executable>
```

## More information

* [Roihu system overview](../../computing/systems-roihu.md)
* [CSC Computing Environment self-learning materials](https://csc-training.github.io/csc-env-eff/)
