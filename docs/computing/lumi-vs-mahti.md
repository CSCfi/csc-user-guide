# How does LUMI-C differ from Mahti?

[LUMI-C](https://docs.lumi-supercomputer.eu/computing/systems/lumic/) consists of 1536 AMD CPU nodes (2x64 cores each) with a performance of 5.6 petaflops. The node count of [Mahti](systems-mahti.md) is similar, 1404 AMD CPU nodes (2x64 cores each) corresponding to a performance of 7.5 Petaflops. Although the systems are very alike based on core count and performance, there are important differences related to access and use which are highlighted on this page.

## Accessing and SSH keys

To access LUMI, you need to first [create a LUMI-specific project](../accounts/how-to-create-new-project.md#creating-a-lumi-project-and-applying-for-resources). Furthermore, accessing LUMI is only possible using SSH keys, meaning that you cannot use passwords to connect through SSH like on Mahti. For instructions on how to generate an SSH key pair and upload the public key, see [Setting up SSH keys](https://docs.csc.fi/computing/connecting/#setting-up-ssh-keys) and the [Get started with LUMI](https://docs.lumi-supercomputer.eu/firststeps/getstarted/) pages.

## Finite time projects

LUMI projects have a finite length ranging from 3 months to 3 years depending on the access mode:

|Access mode  |Length  |Can be extended?               |
|-------------|--------|-------------------------------|
|Regular      |1 year  |No                             |
|Benchmark    |3 months|No                             |
|Extreme scale|1 year  |No                             |
|Development  |1 year  |Yes, twice = max. 3 years total|

For more details on the access modes, see the [LUMI access page](https://research.csc.fi/lumi-access).

## Software installation policy

While Mahti offers frequently used applications as pre-installed modules, users are expected to compile and install the applications they intend to run on LUMI themselves. This is due to the fact that LUMI is a pan-European system with significantly more users than the national systems. Maintaining a pre-installed collection of software and licenses that would meet all users' needs on a European level would thus require excessive administration efforts. Moreover, neither the local organizations such as CSC nor the LUMI user support team (LUST) have root access to the system.

To facilitate installing software on LUMI, the [EasyBuild tool](https://docs.lumi-supercomputer.eu/software/installing/easybuild/) is provided along with [installation recipes](https://github.com/Lumi-supercomputer/LUMI-EasyBuild-contrib) (EasyConfig files) using which you can install additional applications to your home or project directories. Additionally, a [container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container_wrapper/) identical to the [Tykky tool](containers/tykky.md) is provided as a means to wrap installations inside an Apptainer/Singularity container. This is recommended especially for Conda and pip environments to alleviate the load on the parallel filesystem.

If you have problems installing your software on LUMI-C, please [send a ticket to the LUMI user support team](https://lumi-supercomputer.eu/user-support/need-help/)!

## Programming environment and software stacks

The programming environment of LUMI-C is quite different compared to CSC supercomputers. LUMI comes with three alternative programming environments, namely Cray, GNU and AOCC. Each of the environments have their own compiler suites that become available upon loading the corresponding programming environment module. Moreover, two types of software stacks are offered, the CrayEnv and LUMI stacks. Please refer to the LUMI documentation for a detailed description of the [available collection of compiler suites](https://docs.lumi-supercomputer.eu/development/compiling/prgenv/) and [software stacks](https://docs.lumi-supercomputer.eu/computing/softwarestacks/) and how to swap between these.

One noticable difference about the Cray programming environments is that it comes with compiler wrappers that replace commands commonly found on HPC systems. For example, commands for compiling MPI code such as `mpicc`, `mpic++` and `mpif90` are unavailable as such. Instead, you should use the wrappers `cc`, `CC` and `ftn`, respectively. See the LUMI documentation for [more details on the Cray MPI wrappers](https://docs.lumi-supercomputer.eu/development/compiling/prgenv/#compile-an-mpi-program).

## Disk areas

Similar to CSC supercomputers, LUMI uses the Lustre parallel filesystem. However, there's currently no fast local disk such as on Puhti and Mahti-AI. The fast flash-based scratch space (LUMI-F) will be made available once the installation of LUMI-G is completed. Also, the object storage (LUMI-O) is not available yet. [See the LUMI documentation for more details](https://docs.lumi-supercomputer.eu/storage/).

## Available partitions

LUMI-C has two types of partitions (queues): two that are allocatable by node (only full nodes can be requested, similar to Mahti) and three that are allocatable by resources (partial nodes can be requested, similar to Puhti). [See more details in the LUMI documentation](https://docs.lumi-supercomputer.eu/computing/jobs/partitions/), e.g. maximum wall-time/node count and naming of the partitions.

## Billing

Billing on LUMI-C differs from Mahti, as well as depending on which partition you are using. Notably, the standard partition on LUMI-C is billed based on allocated CPU-core hours (1 billing unit per CPUh), while on Mahti reserving one node (128 physical cores) consumes 100 BUs per hour. The small partition on LUMI-C is on the other hand billed per allocated core if you are above a certain threshold per chunk of 2 GB of memory. [See the LUMI documentation for more details and precise formulas](https://docs.lumi-supercomputer.eu/computing/jobs/billing/).

## Sensitive data

LUMI projects are not allowed to handle sensitive (personal) data at the moment!

## Support channels

The main channel for LUMI support is to [contact the LUMI user support team (LUST)](https://lumi-supercomputer.eu/user-support/need-help/).