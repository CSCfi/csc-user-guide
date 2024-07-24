# Example batch job scripts for Puhti

Example batch job scripts for running different types of applications/programs
on Puhti.

[TOC]

!!! info "Edit placeholders as needed"
    When using these scripts, remember to change the resources (runtime, tasks,
    etc.) to match your needs, and to replace `myprog <options>` with the
    executable (and options) of the program you intend to run. Also, do not
    forget to replace `<project>` with the name of your billing project (see
    [My CSC](https://my.csc.fi) or `csc-projects` command).

## Serial

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```

## OpenMP

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=4000

# set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## MPI

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=40
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```

## Large MPI

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=40
#SBATCH --mem-per-cpu=4000

srun myprog <options>
```

## MPI + OpenMP

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=02:00:00
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=4000

# set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun myprog <options>
```

## Single GPU

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=8000
#SBATCH --gres=gpu:v100:1

srun myprog <options>
```

## Multiple GPUs

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --time=02:00:00
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=8000
#SBATCH --gres=gpu:v100:4

srun myprog <options>
```

## Interactive with X11 graphics
 
Give this directly on the command-line instead of using a batch job script and
`sbatch`. Note, as you may need to queue, it's convenient to ask for an email
notification once the resources have been granted (`--mail-type=BEGIN`).

```bash
srun --ntasks=1 --time=00:10:00 --mem=1G --x11=first --pty \
     --account=<project> --partition=small --mail-type=BEGIN \
     myprog
```

See also [Interactive usage](interactive-usage.md).

## Local storage

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000
#SBATCH --gres=nvme:10

# access the local storage using $LOCAL_SCRATCH environment variable, e.g.
cd $LOCAL_SCRATCH

srun myprog <options>

# move important data to the directory from which the job was submitted, e.g.
mv mydata $SLURM_SUBMIT_DIR
```

!!! warning "Remember to recover your data"
    The local storage is purged after each batch job. Do not forget to move
    the data you want to preserve from the local disk back to a shared disk
    area (e.g. `/scratch`).
