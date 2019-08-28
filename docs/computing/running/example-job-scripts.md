# Example batch job scripts

## OpenMP

```
#!/bin/bash -l
#SBATCH --jobname=example
#SBATCH --account=project_<project_id>
#SBATCH --partition=serial
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=6000

srun myprog <options>
```

## MPI

```
#!/bin/bash -l
#SBATCH --jobname=example
#SBATCH --account=project_<project_id>
#SBATCH --partition=parallel
#SBATCH --time=02:00:00
#SBATCH --ntasks=50
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```
