# How does LUMI-C differ from Mahti?

[LUMI-C](https://docs.lumi-supercomputer.eu/computing/systems/lumic/) consists of 1536 AMD CPU nodes (2x64 cores each) with a theoretical performance of 7.7 petaflops. The node count of [Mahti](systems-mahti.md) is similar, 1404 AMD CPU nodes (2x64 cores each) corresponding to a theoretical performance of 7.5 Petaflops. Although the systems are very alike based on CPU-hardware, core count and performance, there are important differences which are highlighted on this page.

## GPUs and memory

Mahti has only a few (24) GPU-nodes available, while LUMI-C will be flanked by LUMI-G and LUMI-D with a massive GPU capacity. Also, Mahti has 256 GB memory in all CPU nodes, while LUMI-C has also 512 GB and 1024 GB memory nodes (similar to Puhti).

## Accessing and SSH keys

To access LUMI, you need to first [create a LUMI-specific project](../accounts/how-to-create-new-project.md#how-to-create-finnish-lumi-projects). Note that LUMI-projects have a finite duration ([see below](lumi-vs-mahti.md#finite-time-projects)) and cannot be used for running on the national resources and vice versa.

Furthermore, accessing LUMI is only possible using SSH keys, meaning that you cannot use passwords to connect through SSH like on Mahti. For instructions on how to generate an SSH key pair and uploading the public key to [MyCSC](https://my.csc.fi/), see [Setting up SSH keys](connecting.md#setting-up-ssh-keys) and the [Get started with LUMI](https://docs.lumi-supercomputer.eu/firststeps/getstarted/) pages.

## Finite time projects

Finnish LUMI projects have a finite duration ranging from 3 months to max. 3 years depending on the access mode:

|Access mode  |Length  |Can be extended?               |
|-------------|--------|-------------------------------|
|Regular      |1 year  |No                             |
|Benchmark    |3 months|No                             |
|Extreme scale|1 year  |No                             |
|Development  |1 year  |Yes, twice = max. 3 years total|

For more details on the access modes, see the [LUMI access page on the Services for Research website](https://research.csc.fi/lumi-access). Note that LUMI users from Finland are also eligible to apply for EuroHPC Joint Undertaking (JU) resources. [See more details on European access modes here](https://www.lumi-supercomputer.eu/get-started-2021/users-in-europe/).

## Software installation policy

While Mahti offers frequently used applications as pre-installed modules, LUMI users are currently expected to compile and install the applications they intend to run on LUMI themselves.

To facilitate installing software on LUMI, the [EasyBuild tool](https://docs.lumi-supercomputer.eu/software/installing/easybuild/) is provided along with [installation recipes](https://github.com/Lumi-supercomputer/LUMI-EasyBuild-contrib) (EasyConfig files) using which you can install additional applications to your home or project directories. Additionally, a [container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container_wrapper/) identical to the [Tykky tool](containers/tykky.md) is provided as a means to wrap installations inside an Apptainer/Singularity container. This is recommended especially for Conda and pip environments to alleviate the load on the parallel filesystem.

If you have problems installing your software on LUMI-C, please [send a ticket to the LUMI user support team](https://lumi-supercomputer.eu/user-support/need-help/)!

## Programming environment and software stacks

The programming environment of LUMI-C is quite different compared to CSC supercomputers. LUMI comes with three alternative programming environments, namely Cray, GNU and AOCC. Each of the environments have their own compiler suites that become available upon loading the corresponding programming environment module. Moreover, two types of software stacks are offered, the CrayEnv and LUMI stacks. Please refer to the LUMI documentation for a detailed description of the [available collection of compiler suites](https://docs.lumi-supercomputer.eu/development/compiling/prgenv/) and [software stacks](https://docs.lumi-supercomputer.eu/computing/softwarestacks/) and how to swap between these.

!!! Note
    Irrespective of the loaded compiler suite, one noticeable difference concerning the LUMI-C programming environment is that it comes with compiler wrappers that replace commands commonly found on HPC systems such as Mahti. For example, commands for compiling MPI code like `mpicc`, `mpic++` and `mpif90` are unavailable as such. Instead, you should use the wrappers `cc`, `CC` and `ftn`, respectively. See the LUMI documentation for [more details on the available MPI wrappers](https://docs.lumi-supercomputer.eu/development/compiling/prgenv/#compile-an-mpi-program).

## Disk areas

Similar to CSC supercomputers, LUMI uses a Lustre parallel filesystem. However, there's no fast local disk on LUMI similar to the local scratch on Puhti and Mahti-AI. Instead, a fast flash-based Lustre scratch space (LUMI-F) will be made available once the installation of LUMI-G is completed. Also, the LUMI-O object storage is not available yet. [See the LUMI documentation for more details](https://docs.lumi-supercomputer.eu/storage/).

## Available partitions

LUMI-C has two types of partitions (queues): two that are allocatable by node (only full nodes can be requested, similar to Mahti) and three that are allocatable by resources (partial nodes can be requested, similar to Puhti). [See more details in the LUMI documentation](https://docs.lumi-supercomputer.eu/computing/jobs/partitions/), e.g. maximum wall-time/node count and naming of the partitions.

## Billing

Billing on LUMI differs from Mahti. The consumption of billing units (BUs) depends for example on which partition you are running on, as well as on whether you are using CPU, GPU (LUMI-G/LUMI-D) or storage resources, thus amounting to three different billing currencies. [See the LUMI documentation for more details and precise formulas](https://docs.lumi-supercomputer.eu/computing/jobs/billing/).

## Sensitive data

LUMI projects are not allowed to handle sensitive (personal) data at the moment!

## Support channels

The main channel for LUMI support is to [contact the LUMI user support team (LUST)](https://lumi-supercomputer.eu/user-support/need-help/).
