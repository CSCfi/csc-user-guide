# Shared memory and hybrid parallelization

Each compute node on CSC servers (like Puhti) have many Cpu cores. Puhti has two processors, code name Intel Cascade Lake, with 20 cores. That is altogether 40 cores per compute node. Hence, it is possible to run shared memory parallel (OpenMP, Intel TBB) programs efficiently within a node with forty threads at maximum. 

## How to compile

All Programming environments (Gnu and Intel) support OpenMP. Following compiler flags will enable OpenMP support. Same flags are valid for hybrid OpenMP/MPI compiling.

| Compiler  | Flag |
| :------------- |:-------------|
| Gnu | -fopenmp |
|  Intel | -qopenmp |

Here are examples for OpenMP compiling (upper line: Intel compiler, second line: GNU-compiler, third line: Gnu OpenMPI warpper):

```
ifort -qopenmp -o my_openmp_exe my_openmp.f95
gfortran -fopenmp -o my_openmp_exe my_openmp.f95
mpifort -fopenmp -o my_hybrid_exe my_hybrid.f95
```
See [OpenMP web site](https://www.openmp.org/) for more information including standards and tutorials.

## Include files

For Fortran 77 use following line:
```
include 'omp_lib.h'
```
For Fortran 90 (and later) use:

```
use omp_lib
```

For C/C++ use:

```
#include <omp.h>
```

For parallel C++ programs that will utilize Threading Building Blocks technology see TBB documentation [community site](https://www.threadingbuildingblocks.org/) and [Intel Threading Building Blocks Documentation](https://software.intel.com/en-us/tbb-documentation). 

## Running OpenMP programs

The number of OpenMP threads is specified with an environment variable OMP_NUM_THREADS. Running a shared memory program typically requires requesting a whole node. Thus, a forty thread OpenMP job can be run as shown in a following example.

```
#!/bin/bash -l
#SBATCH -J my_openmp
#SBATCH -e my_output_err_%j
#SBATCH -o my_output_%j
#SBATCH --account=project_<project_id>
#SBATCH --mem=2000
#SBATCH -t 01:00:00
# Thread parallel code will need one task (process)
#SBATCH -n 1
# How many threads is needed? an example 40 threads per task (40 is the maximum)
#SBATCH --cpus-per-task=40
## if code is compiled by an Intel compiler then remove # from the line below 
#export KMP_AFFINITY=compact
## if code is compiled by a Gnu compiler then remove # from the line below
#export OMP_PROC_BIND=TRUE
## export the OMP_NUM_THREADS variable using correct number of OpenMP threads
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASKS
## exucute an OpenMP binary
srun ./my_openmp_exe

```
## Binding threads to cores

The compilers support thread/core affinity which binds threads to cores for better performance. This is enabled with compiler-specific environment variables as follows:

Intel:

```
export KMP_AFFINITY=compact
```

Gnu:

```
export OMP_PROC_BIND=TRUE
```
If these variables and values are not set all threads in a compute node might run in a same core.
Learn more about [Intel thread affinity interface](https://software.intel.com/en-us/cpp-compiler-developer-guide-and-reference-thread-affinity-interface-linux-and-windows). Support information for GNU compilers for tread affinity can be found [here](https://gcc.gnu.org/onlinedocs/libgomp/GOMP_005fCPU_005fAFFINITY.html#GOMP_005fCPU_005fAFFINITY).

## Hybrid parallelization
In many cases it is beneficial to combine MPI and OpenMP parallelization. More precisely, the inter-node communication is handled with MPI and for communication within the nodes OpenMP is used. For example, on Puhti, an eight-node job in which there is one MPI task per node and each MPI task has forty OpenMP threads, resulting in a total core (and thread) count of 320.

Running a hybrid job can be done as above with the exception that more nodes are specified and for each node one MPI task is requested. The parallel partition must be requested to run the program because there are more than one node. That is, for a 8 x 40 job the following flags are needed.

```
#!/bin/bash -l
# Hybrid MPI/OpenMP example. Please read carefully and do necessary changes.
# Job layout: one mpi process per compute node and 40 openmp threads per mpi task
#SBATCH -J my_hybrid
#SBATCH -e my_output_err_%j
#SBATCH -o my_output_%j
#SBATCH --account=project_<project_id>
#SBATCH --mem-per-cpu=1000
#SBATCH -t 02:00:00
# Number of compute nodes
#SBATCH -N 8
# Number of mpi tasks per compute node
#SBATCH -n 8
# 40 threads per mpi task
#SBATCH --cpus-per-task=40
# Choose a suitable queue <parallel>
#SBATCH -p parallel

## if code is compiled by an Intel compiler then remove # from the line below 
#export KMP_AFFINITY=compact
## if code is compiled by a Gnu compiler then remove # from the line below
#export OMP_PROC_BIND=TRUE
## export the OMP_NUM_THREADS variable using correct number of OpenMP threads
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASKS
## execute a hybrid binary
srun ./my_hybrid_exe

```

Because each compute node on Puhti contains two 20-core processors it might be useful to try hybrid MPI/OpenMP job that has 2 mpi processes per compute node. In the next batch job example one MPI process is allocated per socket (each compute node has two sockets and one socket has one 20-core processor). Total core (and thread) count is 320 (16 mpi process and each mpi process has 20 OpenMP threads).
 
```
#!/bin/bash -l
## Hybrid MPI/OpenMP example. Please read carefully and do necessary changes.
## 
## The number of compute nodes for a 8 node MPI/OpenMP job (16*20=320)
## Job layout: two mpi process per compute node, 
## 1 mpi task per socket + 20 openmp threads per mpi task
## 
## 8 nodes
#SBATCH --nodes=8
## 16 MPI tasks (total number of mpi tasks)
#SBATCH --ntasks=16
## 2 MPI task per compute node
#SBATCH --ntasks-per-node=2
## 1 MPI task per socket
#SBATCH --ntasks-per-socket=1
## 20 threads per mpi task
#SBATCH --cpus-per-task=20
## Memory for each mpi process
#SBATCH --mem-per-cpu=1000
## Choose a suitable queue <parallel>
## How to check queue limits: scontrol show part <queue name>
## for example: scontrol show part parallel
#SBATCH -p parallel
#SBATCH -J jobname
#SBATCH -o jobname_%j.out
#SBATCH -e jobname_%j.err
#SBATCH --account=project_<project_id>
#SBATCH -t 01:01:00
## export the OMP_NUM_THREADS variable using correct number of OpenMP threads 
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
## if code is compiled by an Intel compiler then remove # from the line below 
#export KMP_AFFINITY="compact,1"
## if code is compiled by a Gnu compiler then remove # from the line below
#export OMP_PROC_BIND=TRUE
## execute a hybrid binary
srun ./my_hybrid_exe

```

