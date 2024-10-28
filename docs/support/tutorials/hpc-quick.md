# Getting started with supercomputing at CSC

You have signed up for your
[user account](../../accounts/how-to-create-new-user-account.md)
and first [CSC project](../../accounts/how-to-create-new-project.md), and are
now ready to scale up your computing! This page provides guidance for getting
started with using our HPC resources.

It is recommended that new users complete the *CSC Computing Environment*
course, which provides an in-depth introduction to CSC services. The next live
teaching instance can be found in the
[CSC training calendar](https://csc.fi/en/trainings/training-calendar/).
A
[self-learning implementation](https://csc.fi/en/training-calendar/csc-computing-environment-self-learning/)
is also available. The
[course materials](https://csc-training.github.io/csc-env-eff/) are accessible
without having to sign up, and are very useful by themselves.

For a more general introduction to HPC, we recommend the
[*Elements of Supercomputing*](https://edukamu.fi/elements-of-supercomputing/)
online course.

!!! note "Need support?"

    Do not hesitate to [contact the CSC Service Desk](../contact.md) if you
    have any questions about using CSC services. We are happy to help!

## Which system should I use?

### Puhti

New users are recommended to start working on the
[Puhti supercomputer](../../computing/available-systems.md#puhti).
Compared to Mahti, it has much more
[pre-installed software](../../apps/by_system.md#puhti), more GPU nodes, and
typically more available memory per CPU core. Additionally, GPU nodes and some
CPU nodes on Puhti have
[fast local NVMe storage](../../computing/disk.md#temporary-local-disk-areas).

### Mahti

If you know that your computations are highly parallelizable, you should
consider running them on the
[Mahti supercomputer](../../computing/available-systems.md#mahti).
Compared to Puhti, Mahti has many more CPU nodes and cores per node. Mahti is
intended for computations that are able to effectively utilize at least an
entire CPU node.

Additionally, while Mahti has fewer GPU nodes than Puhti, the A100 GPUs on Mahti
are considerably more powerful than the V100 GPUs on Puhti, which makes Mahti
also suitable for demanding [machine learning](ml-guide.md) applications.
In contrast to Puhti, only the GPU nodes on Mahti have fast local NVMe storage
available.

### LUMI

The [LUMI supercomputer](../../computing/available-systems.md#lumi)
is one of the fastest in the world. It is intended primarily
for running computations that benefit from the large amount of high-performance
GPUs in its LUMI-G hardware partition. Whereas the GPUs on Puhti and Mahti are
manufactured by Nvidia, the LUMI GPUs are made by AMD, so make sure that your
GPU applications are able to run on AMD GPUs. LUMI has
[its own documentation pages](https://docs.lumi-supercomputer.eu/).

!!! note "On supercomputing"

    CSC supercomputers offer resources that, when properly used, are well-beyond
    what the most sophisticated consumer devices are capable of. However, *you are
    not the only one using them*. On your personal workstation, you have, in
    principle, immediate access to resources. On a supercomputer, which is a shared
    system, you must typically queue for them, since their demand tends to be higher
    than their supply. See our [usage policy](../../computing/usage-policy.md)
    for more information.

    It is also worth keeping in mind that running your computations on a
    supercomputer only improves performance if you play to its strengths.
    Supercomputers are powerful because they allow for
    [parallel computing](https://en.wikipedia.org/wiki/Parallel_computing).
    If your code is not written to take advantage of multiple CPU cores, or one or
    more GPUs, there might be no benefit over running it on your own workstation.
    However, high memory and/or storage requirements, as well as availability of
    pre-installed software and licenses are other factors which may make using
    CSC supercomputers attractive for you.

## How to access CSC supercomputers?

### Web interface

Puhti, Mahti and LUMI each have
[their own web interface](../../computing/webinterface/index.md), which allows
interacting with the supercomputer through a web browser. The web interface is a
good choice for interactive computing, such as analyzing, exploring and
visualizing data. For this purpose, the web interface features multiple
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

- [Puhti web interface](https://www.puhti.csc.fi)
- [Mahti web interface](https://www.mahti.csc.fi)
- [LUMI web interface](https://www.lumi.csc.fi)

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
are available. Importantly, the batch job system ensures that your jobs are run
on the *compute nodes* opposed to the *login nodes*,
which are [**not** intended for heavy computing](../../computing/usage-policy.md).
Another benefit of batch jobs is that running computations does not necessitate
being tied to your workstation. While setting up this automation can require
some more planning on your part, in the long run it makes your work more
efficient as well as more reproducible both to yourself and other parties, such
as reviewers and collaborators.

You can access the command-line interface either by
using the [shell applications](../../computing/webinterface/shell.md)
featured in the web interfaces or by
[using an SSH client on your own workstation](../../computing/connecting/index.md).

## How to work with software and data?

### Software

A variety of useful [scientific computing software](../../apps/index.md) is
available on CSC supercomputers. Puhti is especially distinguished in this
regard, having over a hundred pre-installed programs. Our application pages
include batch job script examples and guidelines for running the software
efficiently on CSC supercomputers. We highly recommend using them as a
starting point!

CSC supercomputers use [environment modules](../../computing/modules.md) for
managing software environments. These modules cover everything from
[compilers](../../computing/installing.md#compiling) and
[programming languages](../../apps/by_discipline.md#mathematics-and-statistics)
to workflow utilities like
[Nextflow](../../apps/nextflow.md) and [Snakemake](../../apps/snakemake.md).
Running most of the installed software efficiently requires using the
[command-line interface](#command-line-interface), so it is extremely useful to
have a working knowledge of the
[basics of the Linux operating system](./env-guide/index.md).

While the pre-installed software covers a wide variety of use cases, it is also
possible to install your own applications on CSC supercomputers. The process
often differs from carrying out installations on your own computer, so make
sure to familiarize yourself with our
[installation instructions](../../computing/installing.md). For compiling HPC
applications we have various
[compilers](../../computing/installing.md#compiling),
[high-performance libraries](../../computing/hpc-libraries.md) and other
utilities available to facilitate this. Note that some installations, such as
complex Python environments, benefit from
[containerization](../../computing/containers/overview.md).

You may also wish to develop your own scripts and programs instead of using existing
software. It is most efficient to start writing and testing your code on your
own device, since running it on a shared system (which supercomputers are)
inevitably introduces some overhead. You should only start running your scripts
on a supercomputer once you are ready for testing them on a larger scale or
using specific resources like GPUs.

!!! note "Checking availability"

    If you have a piece of scientific software in mind, it is quite probable
    that we have it installed on Puhti. Besides browsing Docs CSC, you can search
    for software on the command-line using the command
    `module spider <search-pattern>`. Most often the name of the software module
    is simply the name of the software itself, and even if your search pattern
    does not match the module name exactly, the search is case-insensitive and
    supports partial matches.

### Data storage

CSC supercomputers provide distinct [disk areas](../../computing/disk.md) for
different data storage purposes. The *project-based* shared storage can be found
under `/scratch/<project>`. This folder is shared by *all users* in a project
and has a default quota of 1 TB.

Please note that the **scratch disk is not meant for long-term data storage**
and, on Puhti, files that have not been used for 180 days will be automatically
removed. We recommend the
[Allas object storage service](../../data/Allas/introduction.md) for storing
research data that is not actively used on the supercomputers. See
[guidelines for managing data on Puhti and Mahti scratch disks](clean-up-data.md)
for more information. Also note that sensitive data must not be processed or
stored on CSC supercomputers. For this purpose we have separate
[sensitive data services](../../data/sensitive-data/index.md).

CSC supercomputers also have a persistent project-based storage with a default
quota of 50 GB. It is located under  
`/projappl/<project>` and recommended, for example, for custom software
installations. Additionally, each user can store up to 10 GB of data in their
personal home directory (`$HOME`).

[Moving data](../../data/moving/index.md) between a supercomputer and a local
workstation is easy using the
[web interface file browser](../../data/moving/web-interface.md) or
command-line file transfer tools like [scp](../../data/moving/scp.md) and
[rsync](../../data/moving/rsync.md). You can also use the
[Linux wget utility](../../data/moving/wget.md) to download data to
a supercomputer directly from a website or FTP server.

!!! note "CSC does not back up your data!"
    None of the disk areas are automatically backed up by CSC. This means that
    data accidentally deleted by the user cannot be recovered in any way. To
    avoid unintended data loss, make sure to regularly back up your data, for
    example to Allas or your own organization's storage systems.

## Useful links

You can use the navigation sidebar or the search function to find more
information about using CSC HPC services. Here we have included links to pages
that we think are particularly useful when getting started with supercomputing
at CSC.

=== "User accounts and projects"
    - [Creating a new user account](../../accounts/how-to-create-new-user-account.md)
    - [Creating a new project](../../accounts/how-to-create-new-project.md) and
      [adding members to an existing one](../../accounts/how-to-add-members-to-project.md)
    - [Adding service access for a project](../../accounts/how-to-add-service-access-for-project.md)
    - [Billing](../../accounts/billing.md) and
      [applying for billing units](../../accounts/how-to-apply-for-billing-units.md)
    - [Changing your password](../../accounts/how-to-change-password.md)
    - [MyCSC customer portal](https://my.csc.fi)

=== "Computing"
    - [Overview](../../computing/index.md)
    - [Usage policy](../../computing/usage-policy.md)
    - [Connecting to supercomputers](../../computing/connecting/index.md)
    - [Running batch jobs](../../computing/running/getting-started.md) and
      [available batch job partitions](../../computing/running/batch-job-partitions.md)
    - [Pre-installed applications](../../apps/index.md) and
      [how to install custom software](../../computing/installing.md)
    - [LUMI user guide](https://docs.lumi-supercomputer.eu/)

=== "Training materials and tutorials"
    - [*CSC Computing Environment* course materials](https://csc-training.github.io/csc-env-eff/)
    - [Linux basics tutorial](../tutorials/env-guide/index.md)
    - [Machine learning guide](ml-guide.md)
    - [Using Python on CSC supercomputers](python-usage-guide.md)
    - [Managing data on Puhti and Mahti scratch disks](clean-up-data.md)
    - Other [tutorials](index.md) and
      [training materials](../training-material.md)

=== "Support"
    - [Frequently asked questions](../faq/index.md)
    - [CSC Service Desk](../contact.md)
