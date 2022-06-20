# Woking with containers at CSC 

## Containers: A non-technical description 

As a beginner-friendly introduction of containers to non-IT professionals, let's use the analogy of packaging a pet 
in a cage before traveling. A pet essentially needs a living environment (food, water, etc) and a cage to contain the
living environment. Once a pet is packaged, a traveler can take it (e.g, by car, train, flight, etc...) wherever he/she goes 
without affecting the function of the pet by the external environment. Similarly, imagine how a developer (like a 
traveler) would ensure the same functionality of an application (pet) independent of the host environment. One 
solution is to run the application in an isolated environment (just like caging).  In other words, packaging 
up the whole application (process) along with its dependencies ensures the same runtime environment for the 
application independent of the host computing environment. This is essentially the basic idea behind the containers.

Let's now understand how an application runs in an isolated environment in a bit technical way. The Linux
kernel process controls access to the computer hardware. All other processes rely on the kernel to interact with the 
environment, memory, discs, network, etc. One could say that all processes, except the kernel, live inside bubble 
(i.e, host environment), created by the kernel. Normally, when you start new processes, the kernel copies the environment 
from the parent process to the new child processes. The child processes live inside the same bubble. However, when 
starting a new process, you can ask the kernel to show a completely different environment to the child process. This 
is called "running the application in a container." In particular, you can ask the kernel to show a completely different
root file system to the new process. The file system can come from a single file, "a container image", that the kernel 
just shows to the new process as a regular file system. This file system image can contain completely different files 
from the parent process' file system. Effectively this allows packing all the necessary components from a given Linux 
distribution and all the software dependencies for an application into a single file, which can be run in any Linux 
machine with suitable kernel and virtualisation support. In cloud environments, this makes it possible to run applications
transparent irrespective of the Linux distribution.  In HPC environments this can also avoid some parallel file system
performance issues.

## Why to use containers in HPC systems?

The use of containers in HPC environment is increasing with advances in HPC-friendly containers such as singularity which 
can be launched from [Lustre parallel file system](https://docs.csc.fi/computing/lustre/) without privileged root access. 
Here are a few benefits that one can get by using containerised applications:

- Shorter startup times: As containers have less overhead (no need to load OS !), they can be launched quite quickly. 
  You can easily see the differences in start-up times between a containerised application and the application installed 
  directly from conda especially when run at scale. 
- File I/O throughput:  This is one of the biggest issues for Lustre file systems when I/O intensive jobs are deployed in 
  HPC systems. Containers may not solve this issue, but at least when containerised application starts from a single image file, 
  the number of requests for Lustre server node (OSS and MDS) are lesser as compared to conda-based installations where an 
  excessive number of files needs to be loaded when an application is launched.
- Ease of portability: containerised applications can be deployed easily in different computing environments.
- Reproducibility: Containerised applications run the same way regardless of where they are deployed.
- Greater efficiency: As containers are lightweight in nature, CPU and Memory Utilization is not an issue. Thus, containerised
  applications are easy to scale up across the cluster.
- Ease of installation: Once you have singularity image, launching a container from the image is very easy. No real installation
  is needed for it.

## Usage of containers in CSC HPC systems

- [Creating HPC-friendly container](creating.md)
- [Running existing containers](run-existing.md)
- [Container wrapper tool at CSC](https://docs.csc.fi/computing/containers/tykky)


