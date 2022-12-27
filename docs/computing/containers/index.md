# Working with containers in CSC's computing environment

The use of containers in HPC environments is increasing due to advances in HPC-friendly
technologies such as [Singularity/Apptainer](https://apptainer.org/), which can be
launched from a [Lustre parallel file system](../lustre.md) without root privileges.
Here are a few benefits that one can get by using containerized applications:

- **Shorter startup times:** As containers have less overhead (no need to load OS!),
  they can be launched quite quickly. For example, when working with large Python
  environments, you can easily see a difference in start-up times between a containerized
  environment and the application installed directly on the shared file system using
  Conda. This applies especially when running at scale on an HPC system.
- **File I/O throughput:**  Deploying I/O intensive jobs on HPC systems is a major
  issue for Lustre file systems. While containers might not provide a full solution,
  the fact that containerized applications start from a single image file results in
  significantly fewer requests to the Lustre server nodes (OSS and MDS) compared to
  Conda-based installations, which read an excessive number of files each time an
  application is launched. [SquashFS images](run-existing.md#mounting-datasets-with-squashfs)
  can also be used together with Apptainer containers to create compact images
  of your dataset that are interpreted as a single file by Lustre.
- **Portability and reproducibility:** Containerized applications can be deployed
  easily in different computing environments and they run the same way regardless
  of where they are deployed.
- **Greater efficiency:** As containers are lightweight in nature, CPU and memory
  utilization is not an issue. Thus, containerized applications are easy to scale
  up across the cluster.
- **Easy installation:** Once you have an apptainer image, launching a container
  from the image is very easy. No real installation is needed.

To make working with containers in CSC's environment as transparent and easy as
possible, a [container wrapper tool](tykky.md) for packaging installations has
been made available.

## A non-technical description

As a beginner-friendly introduction to containers, let's use the analogy of packaging
a pet in a cage before traveling. A pet essentially needs a living environment (food,
water, etc.) and a cage to contain the living environment. Once a pet is packaged,
a traveler can take it (e.g. by car, train, flight, etc...) wherever without affecting
the function of the pet by the external environment. Similarly, imagine how a developer
could ensure the same functionality of an application independent of the host environment.
One solution is to run the application in an isolated environment (just like caging).
In other words, packaging up the whole application (process) along with its dependencies
ensures the same runtime environment for the application independent of the host
computing environment. This is essentially the basic idea behind containers.

Let's now understand how an application runs in an isolated environment at a slightly
more technical level. The Linux kernel process controls access to the computer hardware.
All other processes rely on the kernel to interact with the environment, memory, disks,
network, etc. One could say that all processes, except the kernel, live inside a bubble
(i.e, host environment), created by the kernel. Normally, when you start new processes,
the kernel copies the environment from the parent process to the new child processes.
The child processes live inside the same bubble. However, when starting a new process,
you can ask the kernel to show a completely different environment to the child process.
This is called "running the application in a container". In particular, you can ask the
kernel to show a completely different root file system to the new process. The file
system can come from a single file, "a container image", that the kernel just shows
to the new process as a regular file system. This file system image can contain
completely different files from the file system of the parent process. Effectively,
this allows packaging all the necessary components of a given Linux distribution and
all the software dependencies for an application into a single file, which can be run
in any Linux machine with a suitable kernel and virtualization support. In cloud
environments, this makes it possible to run applications transparently irrespective
of the Linux distribution. In HPC environments this can also mitigate the above outlined
parallel file system performance issues.

## More information on creating and running containers at CSC

- [Creating HPC-friendly containers](creating.md)
- [Running existing containers](run-existing.md)
- [Easy-to-use container wrapper tool](tykky.md)
