# Example batch job scripts

## OpenMP

```
#!/bin/bash -l
#SBATCH --jobname=example
#SBATCH --account=project_<project_id>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```

## MPI

```
#!/bin/bash -l
#SBATCH --jobname=example
#SBATCH --account=project_<project_id>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --ntasks=80
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```
