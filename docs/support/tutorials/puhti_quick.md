# Puhti quick start guide
A quick start guide for new Puhti users. It is assumed
that you have previously used CSC cluster resources like Taito/Sisu.


### Connecting to Puhti

Connect using a normal ssh-client:
```
$ ssh <csc_username>@puhti.csc.fi
```

### Module system:

CSC uses the [Lmod](https://lmod.readthedocs.io) module system.

Modules are set up in a hierarchical fashion, meaning you need to load a compiler 
before MPI and other libraries appear.

Most commonly used module commands:


|  Module command               |  Description                                  |
|-------------------------------|-----------------------------------------------|
| module help *modulename*      | Show information about a module.              |
| module load *modulename*      | Loads the given environment module.           |
| module unload *modulename*    | Unloads the given environment module.         |
| module list                   | List the loaded modules.                      |
| module avail                  | List modules that are available to be loaded. |
| module spider *name*          | Searches the entire list of possible modules. |
| module swap *module1 module2* | Replaces a module with a second module.       |

**Note:** Some modules have the same name but are in different locations in the hierarchy. This means
that

```
module purge
module load gcc
module load boost
```
will give you a boost library without mpi support and
```
module purge
module load gcc
module load 
```
will give you a boost library with mpi support.



### Compilers
The system comes with two compiler families installed, the Intel and GCC compilers. 
We have installed both the 18 and 19 versions of the Intel compiler, and for GCC 9.1, 8.3 and 7.4 are available.
The CPUs support the AVX512 instruction set. The compilers need to be instructed to generate these instructions, 
for the Intel compiler use `-xCOMMON-AVX512` or `-xCASCADELAKE` and for the GCC compiler `-march=cascadelake` Older GCC 
compilers might not support the flags using Cascadelake, in that case just use `-mavx512f` or tell it to compile for Skylake.

**Note:** AVX512 is not necessarily faster than AVX2 and it might still be beneficial to use just AVX2. 

### MPI
Currently the system has a few different MPI implementations installed:

- hpcx-mpi
- mpich
- intel-mpi

We recommend to test using 
_hpcx-mpi_ first, this one is from the network vendor and is based on OpenMPI. If your program does not compile or run with this there is also _mpich_ available and as a last resort we have _intel-mpi_ version 18 available. Please note that currently there are no GPU-aware MPI libraries available.

 **You will need to have the MPI module loaded when submitting your jobs.**

### Python
Python is available through the _python-env_ module. This will replace the system python call with python 3.7. The anaconda environment has a lot of regularly used packages installed by default.

There are also basic machine learning libraries for Python in the module _python-data_. For deep learning applications there are also modules _tensorflow_, _pytorch_, and _mxnet_. There is also a module _tensorflow/1.13.1-hvd_ which has added Horovod support with OpenMPI and NCCL.


### Batch scripts
You have to specify your billing project in the batch script with the `--account=project_<project_<id>` 
flag. Failing to do so will cause your job to be held with the reason “_AssocMaxJobsLimit_”.
Running `srun` directly also requires the flag.

A simple script file is shown below, substitute the ID part of project_<project_<id> with your own project id and change the resource
requirement to best suit your needs.

```
#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:20:00
#SBATCH --partition=serial
#SBATCH --output output.txt
#SBATCH --error errors.txt
#SBATCH --mem-per-cpu=2G
#SBATCH --account=project_<project_id>

srun hostname
```
submit your script file with:
```
sbatch script_name
```

Most commonly used `sbatch` options

|Slurm option | Description| 
|-------------|-------------|
| --begin=time 		|	Defer job until HH:MM MM/DD/YY.|
| -c, --cpus-per-task=ncpus |	Number of cpus required per task.|
| -d, --dependency=type:jobid | 	Defer job until condition on jobid is satisfied.|
| -e, --error=err 	|	File for batch script's standard error.|
| --ntasks-per-node=n 	|	Number of tasks to per node.|
| -J, --job-name=jobname| 		Name of the job.|
| --mail-type=type 	|	Notify on state change: BEGIN, END, FAIL or ALL.|
| --mail-user=user 	|	Who to send email notification for job state changes.|
| -n, --ntasks=ntasks 	|	Number of tasks to run.|
| -N, --nodes=N 	|		Number of nodes on which to run.|
| -o, --output=out 	|	File for batch script's standard output.|
| -t, --time=minutes 	|	Time limit in format d-hh:mm:ss.|
| --mem=MB 		|	Maximum amount of real memory per node required by the job in megabytes. (Recommended for serial jobs and shared memory parallel jobs)|
| --mem-per-cpu=MB 	|	Maximum amount of real memory per allocated CPU required by the job in megabytes.(Recommended for MPI parallel jobs)|
| -p 			|	Specify queue (partition) to be used. |

To reserve GPUs you need to use the --gres flag.The new GPU name is v100 so reserving one would be done with `--gres=gpu:v100:1`


### Slurm
GPU queues are available from the normal login nodes. 


_Information about the different queues:_

|  Module command|  Time Limit   |Job node limit | Number of nodes | Memory | Cores/GPUs node   |
|----------------|---------------|---------------|-----------------|--------|-------------------|
|Serial\*\*      |  3 days       | 1 node        |     772         | 190G   | 40 cores          |
|	         |               |               |     92          | 382G   |                   |
|                |               |               |     12          | 774G   |                   |
|parallel\*\*    |  3 days       | 100 nodes     |     772         | 190G   | 40 cores          |
|                |               |               |     92          | 382G   |                   |
|                |               |               |     12          | 774G   |                   |
|hugemem         |  3 days       |  1 node       |     6           | 1532G  | 40 cores          |
|gputest         |  30 minutes   |  2 nodes      |     2           | 382G   | 40 cores + 4 GPUs |
|gpu             |  3 days       |  160 GPUs     |     78          | 382G   | 40 cores + 4 GPUs |


### Network

- Login nodes can access the internet 
- It is currently not possible to ssh to the compute nodes
- Compute nodes **do not** currently have internet access 

### Storage
The **project based** shared storage can be found under `/scratch/project_<project_id>`.
Note that this folder is shared by **all users** in a project.

The nodes do not have local storage. The local storage in the GPU nodes is not currently accessible.





