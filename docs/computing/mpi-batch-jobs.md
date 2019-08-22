# MPI Based Batch Jobs
In MPI jobs each task has its own memory allocation and thus the tasks can be distributed between nodes.

Below is a sample batch job for a MPI based job using 50 cores

```
#!/bin/bash -l
#SBATCH --jobname=example
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=project_<project_id>
#SBATCH --partition=parallel
#SBATCH --time=02:00:00
#SBATCH --ntasks=50
#SBATCH --mem-per-cpu=4000

srun myprog <options>

```
Note that the command is run with `srun`.