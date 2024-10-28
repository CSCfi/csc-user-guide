# Conda best practices for CSC supercomputers

!!! warning "Do not install Conda environments directly on the parallel file system of CSC supercomputers!"
    [CSC has deprecated the use of Conda environments](../../computing/usage-policy.md#conda-installations)
    that are installed _directly_ on the parallel file system of CSC supercomputers
    (e.g. `/scratch`, `/projappl`, `$HOME`). This is due to performance issues of
    Conda-based environments on shared file systems, causing long start-up delays
    and system-wide slowdowns when running Python scripts.

Conda environments typically contain tens or even hundreds of thousands of
files, and starting a Conda application requires reading a large number of them.
Unfortunately, all parallel file systems, which are optimized for a large number of
clients, have a poor single-client performance. You will notice this as longer
initial start up times for Conda applications and extra stress on the Lustre
metadata server.

**Conda can still be used indirectly**. As an alternative to direct Conda usage,
we recommend:

1. **Use CSC's pre-installed environments available through the module system**

    Check if any of
    [CSC's pre-installed environments](../../apps/python.md#pre-installed-python-environments)
    would be suitable for your project. If the existing environment is missing a few
    critical packages, you can often install the missing packages on your own.

    Our [Python usage guide](python-usage-guide.md#installing-python-packages-to-existing-modules)
    and [R application page](../../apps/r-env.md#r-package-installations) contain further
    details on how to install your own packages on top of our modules. You can also
    [contact CSC Service Desk](../contact.md) with requests for missing packages.

2. **Create a containerized Conda or pip environment using CSC's Tykky tool**

    CSC has developed
    [a tool for wrapping Conda or pip installations](../../computing/containers/tykky.md)
    into a smaller set of files using Apptainer and SquashFS technologies. The tool is
    available as a pre-installed module and is also used for CSC's own installations.

3. **Use your own custom containers**

    This is a great alternative for developing software locally on a workstation,
    and then deploying it on another workstation, cluster, or on cloud platforms.
    CSC's supercomputers support Apptainer containers, which are are just single
    large files for Lustre, thus avoiding much of the problems. Many software
    projects offer Docker containers which can often be easily converted into
    Apptainer format. Inside the container you can naturally use for example
    Conda to manage the packages without causing any file system issues.

    Use [Tykky](../../computing/containers/tykky.md) to convert an existing Docker
    container to Apptainer or read our documentation on
    [how to create your own Apptainer container](../../computing/containers/creating.md).
