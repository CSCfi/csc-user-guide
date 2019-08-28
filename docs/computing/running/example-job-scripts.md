# Example batch job scripts

Below are example job scripts for running different types of programs:

[TOC]

!!! note
    If you copy them (please do!), remember to change at least the resources
    (time, tasks etc.) to match your needs and to replace `myprog <options>`
    with the executable (and options) of the program you wish to run as well
    as `<project_id>` with your project ID.

## OpenMP

```
#!/bin/bash -l
#SBATCH --job-name=example
#SBATCH --account=project_<project_id>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=4000

# set the number of threads based on the --cpus-per-task above
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## MPI

```
#!/bin/bash -l
#SBATCH --job-name=example
#SBATCH --account=project_<project_id>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --ntasks=80
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```
