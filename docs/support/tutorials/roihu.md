# Getting started with Roihu

This is a quickstart guide for Roihu users. It is assumed that you have
previously used CSC supercomputing resources like Puhti, Mahti or LUMI. If not,
you can start by looking at our general
[getting started with supercomputing guide](../hpc-quick.md). We also recommend
checking the
[CSC Computing Environment self-learning course materials](https://csc-training.github.io/csc-env-eff/).

To access Roihu, you need a CSC user account and project that has Roihu service
enabled. [Read more here](../../accounts/index.md).

[TOC]

## Connecting

Connect to Roihu using either:

* [SSH client](#ssh-client)
* [Roihu web interface](#roihu-web-interface)

### SSH client

Connecting to Roihu using an SSH client requires that you have:

1. Set up SSH keys and added your public key to MyCSC (like on Puhti & Mahti).
2. **New:** _Signed_ your public key and downloaded a _certificate_ that allows
   authenticating.
    * Each certificate is valid for 24 hours, after which a new one must be
      generated.

Read the detailed
[instructions for managing SSH keys and certificates](../../computing/connecting/ssh-keys.md).

Once you have set up SSH keys and obtained a valid SSH certificate, connect
using an SSH client:

* [Instructions for Linux/macOS](../../computing/connecting/ssh-unix.md).
* [Instructions for Windows](../../computing/connecting/ssh-windows.md).

!!! info "Note: Roihu has separate login nodes for CPU and GPU partitions"
    Roihu has
    [different CPU architectures on the CPU and GPU nodes](../../computing/systems-roihu.md#compute).
    Hence, there are separate login nodes for building and running programs on
    the respective nodes: `roihu-cpu.csc.fi` and `roihu-gpu.csc.fi`. For
    example, connect to one of the CPU login nodes using a command-line SSH
    client like this:

    ```bash
    # Replace <username> with the name of your CSC user account.

    ssh <username>@roihu-cpu.csc.fi
    ```

    Please observe that software built on `roihu-cpu.csc.fi` can only be run on
    the CPU nodes, while software built on `roihu-gpu.csc.fi` can only be run
    on the GPU nodes. Importantly, this applies also to Python environments.

### Roihu web interface

The simplest way to connect to Roihu is to use the web interface.

1. Go to [www.roihu.csc.fi](https://www.roihu.csc.fi).
2. Log in using your Haka, Virtu or CSC user account.
   [Multi-factor authentication (MFA)](../../accounts/mfa.md) is required.

## Migrating research data

If you need to transfer research data from Puhti or Mahti to Roihu, we
recommend that you:

1. Carefully review your data before transferring it – **only move what you
   really need!** Notably, previous extended disk quotas on Puhti or Mahti will
   not be automatically moved to Roihu. Quota extensions on Roihu must be
   separately applied for and properly motivated.
2. Move your data _directly_ from Puhti or Mahti to Roihu for performance and
   capacity management reasons.

[Read our separate Roihu data migration guide here](data-migration.md).

## Installing software

Document: compilers, MPI, HPC libraries, pre-installed applications, CPU/GPU
architecture considerations

## Running your first job

Document: module system, Slurm queues, performance considerations, link to
examples

## More information

* [Roihu system overview](../../computing/systems-roihu.md)
* [CSC Computing Environment self-learning materials](https://csc-training.github.io/csc-env-eff/)
