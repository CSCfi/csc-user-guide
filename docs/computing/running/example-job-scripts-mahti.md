# Example batch job scripts for Mahti

Example job scripts for running different types of programs:

[TOC]

!!! note
    If you use the scripts (please do!), do not forget to change the resources
    (time, tasks etc.) to match your needs and to replace `myprog <options>`
    with the executable (and options) of the program you wish to run as well
    as `<project>` with the name of your project.

## MPI

```
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=02:00:00
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=128

srun myprog <options>
```

## Large MPI

```
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=100
#SBATCH --ntasks-per-node=128

srun myprog <options>

```
## MPI + OpenMP

```
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=100
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8

# Set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## MPI + OpenMP with thread binding

```
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=100
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8

# Set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores

srun myprog <options>
```


## MPI + OpenMP with simultaneous multithreading

```
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=100
#SBATCH --hint=multithread
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=16

# Note that the ntasks-per-node * cpus-per-task = 256

# Set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## MPI with one task per NUMA domain

```
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=02:00:00
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

# A compute node has 8 NUMA domains, each containing 16 cores
# Slurm places the MPI tasks --cpus-per-task apart

srun myprog <options>
```


## OpenMP

```
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=128

# set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## 1-2 GPU job i.e. `gpusmall` partition

```
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpusmall
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:a100:1
## if local fast disk on a node is also needed, replace above line with:
#SBATCH --gres=gpu:a100:1,nvme:900
#
## Please remember to load the environment your application may need.
## And use the variable $LOCAL_SCRATCH in your batch job script 
## to access the local fast storage on each node.

srun myprog <options>
```

## 4 GPUs per node and multinode GPU job i.e. `gpumedium` partition

```
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpumedium
#SBATCH --time=02:00:00
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:a100:4
## if local fast disk on nodes is also needed, replace above line with: 
#SBATCH --gres=gpu:a100:4,nvme:3600
#
## Please remember to load the environment your application may need.
## And use the variable $LOCAL_SCRATCH in your batch job script 
## to access the local fast storage on each node.

srun myprog <options>
```
