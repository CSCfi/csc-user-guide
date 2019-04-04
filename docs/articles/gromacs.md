# Gromacs

## Gromacs is a fast and versatile classical molecular dynamics code

Initialise use on Taito like this:

```bash
$ module load gromacs-env
```

which will initialise the default module.

This will show all available versions:
```bash
$ module avail gromacs-env
```

!!! tip
    This is a tip of high importance

!!! warning
    This is a warning of high importance

!!! note
    This is a note of high importance
    With two lines


## Example batch script

```
#!/bin/bash -l
#SBATCH -t 00:30:00
#SBATCH -p parallel
#SBATCH --constraint=snb
#SBATCH --ntasks-per-node=16
#SBATCH --nodes=8
#SBATCH -J GMX
#SBATCH -o ogmx.%j
#SBATCH -e egmx.%j
#SBATCH --mem-per-cpu=512
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 128 core (8 full Sandy Bridge nodes) gromacs job, requesting 30 minutes time

export OMP_NUM_THREADS=1

# module load gromacs-env/5.1.x-snb # change x to the latest version
# un/comment to use the older 5.1.x version
module load gromacs-env/2016.x-snb # change x to the latest version
```
