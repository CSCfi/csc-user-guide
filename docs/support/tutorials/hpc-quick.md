# Getting started with supercomputing at CSC

You have signed up for your [CSC account](../../accounts/how-to-create-new-user-account.md)
and first [project](../../accounts/how-to-create-new-project.md), and are now ready to
scale up your computing! This page provides guidance for getting started with
using our HPC resources.

It is recommended that new users complete the *CSC Computing Environment* course,
which provides an in-depth introduction to CSC services. The next live teaching
instance can be found in the
[CSC training calendar](https://csc.fi/en/trainings/training-calendar/).
A [self-learning implementation](https://csc.fi/en/training-calendar/csc-computing-environment-self-learning/)
is also available. The
[practical exercises](https://csc-training.github.io/csc-env-eff/) are
accessible without having to sign up, and quite useful by themselves.

## Which system should I use?


### Puhti

New users are recommended to start working on the
[Puhti supercomputer](../../computing/available-systems.md#puhti).
Compared to Mahti, it has much more [pre-installed software](../../apps/by_system.md#puhti), more GPU nodes, and
typically more available memory per CPU core. Additionally, GPU nodes and some CPU nodes
on Puhti have [fast local NVMe storage](../../computing/disk.md#temporary-local-disk-areas).

### Mahti

If you know that your computations are highly parallelizable, you should
consider running them on the
[Mahti supercomputer](../../computing/available-systems.md#mahti).
Compared to Puhti, Mahti has many more CPU nodes and cores per node. Mahti is
intended for computations that are able to effectively utilize at least an
entire CPU node.

Additionally, while Mahti has fewer GPU nodes than Puhti, the A100 GPUs on Mahti
are considerably more powerful than the V100 GPUs on Puhti, which makes Mahti
also suitable for large-scale machine learning applications. In contrast to Puhti,
only GPU nodes have fast local NVMe storage available on Mahti.

### LUMI

The [LUMI supercomputer](../../computing/available-systems.md#lumi)
is one of the fastest in the world. It is intended primarily
for running computations that benefit from the large amount of high-performance
GPUs in its LUMI-G hardware partition. Whereas the GPUs on Puhti and Mahti are
manufactured by Nvidia, the LUMI GPUs are made by AMD, so make sure that your
GPU applications are able to run on AMD GPUs. LUMI has
[its own documentation pages](https://docs.lumi-supercomputer.eu/).

## Available interfaces

### Web interface

Puhti, Mahti and LUMI each have
[their own web interface](../../computing/webinterface/index.md), which allows
interacting with the supercomputer through a web browser. The web interface is a
good choice for interactive computing, such as analyzing, exploring
and visualizing data. For this purpose, the web interface features multiple
interactive applications, like
[Visual Studio Code](../../computing/webinterface/vscode.md),
[Jupyter](../../computing/webinterface/jupyter.md) and
[RStudio](../../computing/webinterface/rstudio.md). In addition, it provides a
[desktop environment](../../computing/webinterface/desktop.md) featuring
software with graphical user interfaces (GUIs), as well as an
[accelerated visualization app](../../computing/webinterface/accelerated-visualization.md)
for GPU-accelerated visualization and rendering. For demanding computation,
like running full-scale simulations or training neural networks, you should use
the command-line interface, since it allows you to access more resources and
schedule your jobs.

### Command-line interface

While many of the interactive applications in the web interface, such as
Jupyter and RStudio, are easy to use and thus a good starting point for using
CSC supercomputers, their computing capacity is limited to relatively
low-resource interactive usage. If you need access to more resources (e.g.
multiple CPU nodes or GPUs) or if your work requires efficiency over
interactivity, it is a good idea to switch to using the text-based command-line
interface to interact directly with the supercomputer's
[Linux operating system](./env-guide/index.md). While this way of working may
seem archaic, it is truly powerful once you get used to it.

The CLI allows you to 
[submit your computations as batch jobs](../../computing/running/getting-started.md)
to the SLURM job scheduler, which runs them as soon as the requested resources
are available. In practice, this means that getting work done does not
necessitate being tied to your workstation. While setting up this automation
can require some more planning on your part, in the long run it makes it more
reproducible both to yourself and other parties, such as reviewers and collaborators.

You can access the command-line interface either by
using the [shell applications](../../computing/webinterface/shell.md)
featured in the web interface (Windows, Linux or macOS) or by
[using an SSH client on your own workstation](../../computing/connecting.md)
(Linux or macOS).

## Available resources

### Scientific software

Even if your computations are not highly parallelizable, you can benefit from
running them on a CSC supercomputer by making use of the variety of useful
[scientific computing software](../../apps/index.md) that is available.
Puhti is especially distinguished in this regard, having over a hundred
pre-installed programs.

CSC systems use [environment modules](../../computing/modules.md) for
managing software environments. These modules cover everything from
[compilers](../../computing/installing.md#compiling) to
[programming languages](../../apps/by_discipline.md#mathematics-and-statistics)
to workflow utilities like
[Nextflow](../../apps/nextflow.md) and [Snakemake](../../apps/snakemake.md).
Effectively running most of the installed software requires using the
[command-line interface](#command-line-interface), so it is extremely useful to
have a solid grasp of the
[basics of the Linux operating system](./env-guide/index.md).

While the pre-installed software covers a wide variety of use cases, it is not
uncommon to need to
[carry out installations of your own](../../computing/installing.md).
Luckily, we have various
compilers,
[high-performance libraries](../../computing/hpc-libraries.md) and
other utilities to facilitate this.

You may also wish to develop your own scripts instead of using existing
software. It is most efficient to start writing and testing your code on your
own device, since running it on a shared system (which supercomputers
invariably are) inevitably introduces some overhead. You should only start
running your scripts on a supercomputer once you are ready for testing them on a
larger scale or using specific resources like GPUs.

!!! note "Checking for availability"
    If you have a piece of scientific software in mind, it is quite probable
    that we have it installed on Puhti. You can search for software using the
    command `module spider <module-name>`. Most often the name of the software
    module is simply the name of the software, and even if your search query
    does not match the module name exactly, the search is case-insensitive and
    supports partial matches.

### Supercomputer storage

High-performance computing consumes and generates large amounts of data.
Using CSC services for HPC thus requires a basic understanding of the
[supercomputer disk areas](../../computing/disk.md) as well as the principles
of [managing data on them](./clean-up-data.md). Note that the none of the
disk areas are intended for long-term preservation of datasets or experimental
results. For that purpose, we offer the cloud-based
[Allas object storage service](../../data/Allas/introduction.md). Allas supports
multiple options for
[transferring your data to and from object storage](../../data/Allas/accessing_allas.md).

[Moving data](../../data/moving/index.md) between a supercomputer and a local
workstation is made easy by using the
[web interface file browser](../../data/moving/web-interface.md) or a
text-based file transfer tool like [scp](../../data/moving/scp.md) or
[rsync](../../data/moving/rsync.md). You can also use the
[Linux wget utility](../../data/moving/wget.md) to download data to
a supercomputer directly from a website or FTP server.

### Powerful processing

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
