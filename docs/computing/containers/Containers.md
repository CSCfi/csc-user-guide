# Woking with containers at CSC 

## Containers: A non-technical description 

As a beginner-friendly introduction of containers to non-IT professionals, let's use the analogy of packaging a pet 
in a cage before traveling. A pet essentially needs a living environment (food, water, etc) and a cage to contain the
living environment. Travelers can now take the caged pet (e.g, by car, train, flight, etc...) wherever he/she goes 
without affecting the function of the pet by the external environment. Similarly, imagine how a developer (like a 
traveler) would ensure the same functionality of an application (pet) independent of the host environment. One 
solution is to run the application in an isolated environment (just like caging).  In other words, packaging 
up the whole application (process) along with its dependencies ensures the same runtime environment for the 
application independent of the host computing environment. 

Let's now understand how an application runs in an isolated run time environment in a bit technical way. The Linux
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

## Advantages of using containers in HPC systems

The use of containers in HPC environment is increasing with advances in HPC-friendly containers such as singularity which 
can be launched from [Lustre parallel file system](https://docs.csc.fi/computing/lustre/) without privileged root access. 
Here are a few benefits that one can get by using containerised applications:
   - Lesser startup times: As containers have less overhead (no need to load OS !) containerised applications have faster 
      start-up times. You can easily the differences in start-up time between a containerised application and modularised 
      application based on conda. 
   - File I/O Throughput:  This is one of the biggest issues for Lustre file systems when I/O intensive jobs are deployed. 
    Containers may not solve this issue, but at least when containerised application starts from a single image file, the 
    number requests for Lustre server node (OSS and MDS) are less as compared to conda-based installation where an excessive
    number of files needs to be loaded.
   - Ease of portability: containerised applications can be deployed easily in different computing environments.
   - Reproducibility: DevOps teams know applications in containers will run the same, regardless of where they are deployed.
   - Greater efficiency: As containers are lightweight in nature, CPU and Memory Utilization is not an issue. Thus, containerised
     applications facilitate  faster scale-up across the cluster

## Usage of containers in CSC HPC systems

- [Creating HPC-friendly container](https://docs.csc.fi/computing/containers/creating/)
- [Running existing containers](https://docs.csc.fi/computing/containers/run-existing/)
- [Container wrapper tool at CSC](https://docs.csc.fi/computing/containers/tykky)


