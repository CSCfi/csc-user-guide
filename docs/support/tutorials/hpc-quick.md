# Getting started with supercomputing at CSC

You have signed up for your CSC account and first project, and are now ready to
scale up your computing! This page provides guidance for getting started with
using our HPC resources. It is recommended that new users complete the
[CSC Computing Environment course](https://csc-training.github.io/csc-env-eff/),
which provides a more in-depth introduction to using CSC services.

## Available systems

### Puhti

New users are recommended to start working on the
[Puhti supercomputer](../../computing/systems-puhti.md).
Compared to Mahti, it has much more pre-installed software, more GPU nodes, and
typically more available memory per CPU. Additionally, GPU nodes and some of the CPU nodes
on Puhti have [fast local NVMe storage](../../computing/disk.md#temporary-local-disk-areas).

### Mahti

If you know that your computations are highly parallelizable, you should
consider running them on the
[Mahti supercomputer](../../computing/systems-mahti.md).
Compared to Puhti, Mahti has many more CPU nodes and cores per node. Mahti is
intended for computations that are able to effectively utilize at least an
entire CPU node.

Additionally, while Mahti has fewer GPU nodes than Puhti, the A100 GPUs on
Mahti are considerably more powerful than the V100 GPUs on Puhti, which
makes Mahti also suitable for machine learning applications. In contrast to Puhti,
on Mahti only GPU nodes have fast local NVMe storage available.

### LUMI

LUMI is one of the fastest supercomputers in the world. It is intended primarily
for running computations that benefit from the large amount of high-performance
GPUs in its LUMI-G hardware partition. Whereas the GPUs on Puhti and Mahti are
manufactured by Nvidia, the LUMI GPUs are made by AMD, so make sure that your
GPU applications are able to run on AMD GPUs. LUMI has
[its own documentation pages](https://docs.lumi-supercomputer.eu/).

## Available interfaces

### Web interface

Puhti, Mahti and LUMI each have
[their own web interface](../../computing/webinterface/index.md), which allows
interacting with the supercomputer using a web browser. The web interface is a
good choice for interactive computing, such as analyzing, exploring
and visualizing data. For this purpose, the web interface features multiple
interactive applications, like
[Visual Studio Code](../../computing/webinterface/vscode.md),
[Jupyter](../../computing/webinterface/jupyter.md) and
[RStudio](../../computing/webinterface/rstudio.md). For demanding computation,
like running full-scale simulations or training neural networks, you will want
to use the command-line interface, as it allows you to schedule your jobs and
allocate more resources.

### Command-line interface

Effective high-performance computing is based on using the supercomputers'
[Linux operating system](./env-guide/index.md) through a text-based interface.
Most importantly, this allows you to submit your computations as
[batch jobs](../../computing/running/creating-job-scripts-puhti.md)
directly to the SLURM job scheduler.

If you request a large amount of resources for running an interactive
application like Jupyter, you typically have to wait several hours before
manually running your code. This is both inconvenient and wasteful, as your
session may start at a time when you are unable to access your workstation,
which means that several hours of potential runtime can go unused.

When you submit a batch job to the SLURM scheduler, it is run automatically
when your requested resources become available. Running computations as batch
jobs also allows you to access resources that are not available through the
interactive applications, such as using multiple GPUs for training neural
networks.

You can access the command-line interface either by
using the [shell applications](../../computing/webinterface/shell.md)
featured in the web interface (Windows, Linux or macOS) or by
[using an SSH client on your own workstation](../../computing/connecting.md)
(Linux or macOS).

## Available resources

### Scientific software

Even if your computations are not highly parallelizable, you can benefit from
running them on CSC supercomputers if you have need for the diverse
[scientific computing software](../../apps/index.md)
installed on our systems. Puhti is especially useful in this regard, having over
a hundred pre-installed programs.

CSC systems use [environment modules](../../computing/modules.md) for
managing software environments. These modules cover everything from compilers to
workflow utilities and Python environments. Running most of our software
requires using the [command-line interface](#command-line-interface).
If you plan on using these programs, it is therefore necessary to have a good
understanding of the
[basics of the Linux operating system](./env-guide/index.md).

While the pre-installed software covers a plethora of use cases, it is not
uncommon to have to
[carry out installations of your own](../../computing/installing.md).
Luckily, we have various compilers and utilities to facilitate this.

You may also wish to develop your own scripts instead of using existing
software. It is most efficient to start writing and testing your code on your
own device, since
[running code on a shared resource](../../computing/running/getting-started.md)
inevitably introduces some overhead. You should only start running your code on
a supercomputer once you are ready for testing on a larger scale or with
specific resources like GPUs.

### Supercomputer storage

High-performance computing consumes and generates large amounts of ephemeral
data. Using CSC services for HPC thus requires a basic understanding of our
[supercomputer storage system](../../computing/disk.md). For long-term data
storage needs, we have the cloud-based
[Allas object storage service](../../data/Allas/introduction.md).

### Processing power

CSC supercomputers offer resources that, when properly used, are well-beyond
what the most sophisticated consumer devices are capable of. However, you are
not the only one using them. On your personal workstation, you have, in
principle, immediate access to resources. On a supercomputer, which is a shared
system, you must typically queue for them, since their demand tends to be higher
than their supply. Resources are allocated using the
[SLURM batch job system](../../computing/running/getting-started.md).
Jobs are submitted to
[batch job partitions](../../computing/running/batch-job-partitions.md),
which are distinct groupings of the nodes that make up a supercomputer.
Each partition has its particular resources and limitations, and it is helpful
to be aware of the differences.

!!! note "On supercomputing"

    It is worth keeping in mind that running your computations on a
    supercomputer only improves performance if you play to its strengths.
    Supercomputers are powerful because they allow for
    [parallel computing](https://en.wikipedia.org/wiki/Parallel_computing).
    If your code is not written to take advantage of multiple CPUs, or one or
    more GPUs, there is no benefit over running it on your own workstation.