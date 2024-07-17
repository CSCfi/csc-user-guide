# Getting started with supercomputing at CSC

You have signed up for your CSC account and first project, and are now ready to
scale up your computing! This page provides guidance for getting started with
using our HPC resources.

## Available systems

### Puhti

New users are recommended to start working on the
[Puhti supercomputer](../../computing/systems-puhti.md).
Compared to Mahti, it has much more pre-installed software, more GPU nodes, and
typically more available memory per CPU. Additionally, Puhti CPU nodes have fast
local NVMe storage, which is reserved only for GPU nodes on Mahti.

### Mahti

If you know that your computations are highly parallelizable, you should
consider running them on the
[Mahti supercomputer](../../computing/systems-mahti.md).
Compared to Puhti, Mahti has many more CPU nodes and cores per node. Mahti is
intended for computations that are able to effectively utilize at least an
entire CPU node.

Additionally, while Mahti has fewer GPU nodes than Puhti, the A100 GPUs on
Mahti are considerably more powerful than the V100 GPUs on Puhti, which
makes Mahti also suitable for machine learning applications.

### LUMI

LUMI is one of the fastest supercomputers in the world. It is intended primarily
for running computations that benefit from the large amount of high-performance
GPUs in its LUMI-G hardware partition. Whereas the GPUs on Puhti and Mahti are
manufactured by Nvidia, the LUMI GPUs are made by AMD, so make sure that your
GPU applications are able to use AMD drivers. LUMI has
[its own documentation pages](https://docs.lumi-supercomputer.eu/).

## Available interfaces

Most of the [pre-installed programs](../../apps/index.md) on CSC supercomputers
are run using the [command-line interface](#command-line-interface).
If you plan on using these programs, it is necessary to have a good
understanding of the
[basics of the Linux operating system](./env-guide/index.md).

You may also wish to develop your own scripts instead of using existing
software. It is most efficient to start writing and testing your code on your
own device, since
[running code on a shared resource](../../computing/running/getting-started.md)
inevitably introduces some overhead. You should only start running your code on
a supercomputer once you are ready for testing on a larger scale or with
specific resources like GPUs.

!!! note "On supercomputing"

    It is worth keeping in mind that running your computations on a supercomputer
    only improves performance if you play to its strengths. Supercomputers are
    powerful because they allow for
    [parallel computing](https://en.wikipedia.org/wiki/Parallel_computing).
    If your code is not written to take advantage of multiple CPUs, or one or
    more GPUs, it is the same as running it on your own workstation.

### Web interface

Puhti, Mahti and LUMI each have
[their own web interface](../../computing/webinterface/index.md), which allows
interacting with the supercomputer using a web browser. The web interface is a
good choice for interactive computing, such as developing code or exploring
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

## Available SLURM partitions

The nodes that make up a supercomputer are grouped into partitions according to
their hardware specifications. Running computations using either the web
interface or command-line interface requires you to specify a partition on which
to run your job, so it is important to be aware of their differences. Our
documentation includes a description of
[available SLURM partitions](../../computing/running/batch-job-partitions.md).
