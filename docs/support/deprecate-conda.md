# Deprecating Conda

**CSC has deprecated the use of Conda installations** on our supercomputers
Puhti and Mahti. This is due to the performance issues of Conda-based
environments on shared parallel file systems, causing long start-up delays and
system-wide slowdowns when using Python scripts. We also strongly recommend
users moving away from their own Conda-based installations.

Conda environments typically contain tens or even hundreds of thousands of
files, and starting a Conda application requires reading a large number of them.
Unfortunately all parallel file systems, which are optimized for large number of
clients, have a poor single-client performance. You notice this as a longer
initial start up time for Conda applications, and extra stress on the Lustre
metadata server.

Instead we recommend:

1. Use the existing non-Conda-based environments available through the module
   environment
    
    Check if any of the already installed environments for Python or R would
    be suitable for your project. Regular users cannot install new packages
    to the system directories, but they can install additional packages to
    their own directories, for example for Python:
    
    ```
    module load python-data
    pip install --user your-missing-package
    ```
    
    Our
    [Python](../apps/python.md#installing-python-packages-to-existing-modules)
    and [R](../apps/r-env-singularity.md#r-package-installations) pages also
    contain further details on how to install your own packages to our modules.
    

2. Use containers
    
    This is a great alternative for developing software locally on a
    workstation, and then deploying it on other workstation, cluster, or on
    cloud platforms. CSC's supercomputers support Singularity containers, which
    are are just single big files for Lustre, thus avoiding much of the
    problems. Many software projects offer Docker-containers which can often
    easily be converted to Singularity format.
    
    Read our documentation on [how to create your own Singularity
    container](../computing/containers/creating.md)
