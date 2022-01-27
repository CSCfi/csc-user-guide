# Deprecating Conda

**CSC has deprecated the direct usage of Conda installations on our
supercomputers' (Puhti and Mahti) shared file systems**. This is due to the
performance issues of Conda-based environments on parallel file systems, causing
long start-up delays and system-wide slowdowns when using Python scripts. We
strongly recommend users moving away from their own installations which use
Conda directly on a shared drive (such as `/projappl`, `/scratch` on user's home
directory). We are also gradually deprecating CSC-installed modules that are
based directly on Conda. Conda can still be used indirectly, for example wrapped
as a Singularity container.

Conda environments typically contain tens or even hundreds of thousands of
files, and starting a Conda application requires reading a large number of them.
Unfortunately all parallel file systems, which are optimized for large number of
clients, have a poor single-client performance. You notice this as a longer
initial start up time for Conda applications, and extra stress on the Lustre
metadata server.

As an alternative to direct Conda usage we recommend:

1. **Use CSC's pre-installed environments available through the module system**
    
    Check if any of [CSC's pre-installed environments](../apps/index.md) would
    be suitable for your project. If the existing environment is missing a few
    critical packages, you can often install the missing packages on your own.
    
    Our
    [Python](../apps/python.md#installing-python-packages-to-existing-modules)
    and [R](../apps/r-env-singularity.md#r-package-installations) pages also
    contain further details on how to install your own packages to our modules.
    You can also [contact CSC's servicedesk](contact.md) with requests for
    missing packages.
    
2. **Wrap your Conda or pip environment using CSC's tool**

    CSC is currently developing [a tool for wrapping existing Conda or pip
    installations](https://github.com/CSCfi/hpc-container-wrapper) into a
    smaller set of files using Singularity and squashfs technologies. The tool
    is still being developed, but is already being used internally for CSC's own
    installations.

3. **Use your own custom containers**
    
    This is a great alternative for developing software locally on a
    workstation, and then deploying it on other workstation, cluster, or on
    cloud platforms. CSC's supercomputers support Singularity containers, which
    are are just single big files for Lustre, thus avoiding much of the
    problems. Many software projects offer Docker-containers which can often
    easily be converted to Singularity format. Inside of the container you can
    naturally use for example Conda to manage the packages without causing any
    file system issues.
    
    Read our documentation on [how to create your own Singularity
    container](../computing/containers/creating.md)
