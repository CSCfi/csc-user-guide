# GPAW

GPAW is an efficient program package for electronic structure
calculations. It is based on the density-functional theory (DFT)
implemented within the projector augmented wave (PAW), and it can utilize
various basis sets (uniform real-space grids, plane waves, localized
atomic orbital basis).

Some features of the software:

-   total energy calculations
-   structural optimizations
-   different boundary conditions (finite, wire, slab, bulk)
-   efficient parallelization
-   excited state properties within time-dependent density-functional
    theory

[TOC]

## Available

-   Puhti: 1.4.0, 1.5.2, 20.1.0
-   Mahti: 20.1.0
-   Check all available versions (and default version) with
    `module avail gpaw`

### PAW Setups

All installations use version **0.9.20000** of GPAW's PAW Setups.

## License
GPAW is free software available under GPL, version 3+

## Usage

Initialize default version:

```bash
$ module load gpaw
```

A specific version can be initialized with `module load gpaw/version`, e.g.
`module load gpaw/20.1.0`

**Example parallel batch script for Puhti**

```
#!/bin/bash -l
#SBATCH --time=00:30:00
#SBATCH --partition=large
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=2
#SBATCH --mem-per-cpu=2GB
#SBATCH --account=<project>
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 80 core (2 full nodes) gpaw job, requesting
# 30 minutes time and 2 GB of memory for each core

module load gpaw

srun gpaw-python input.py
```

**Example batch script for Mahti with hybrid MPI/OpenMP parallelization**

```
#!/bin/bash -l
#SBATCH --time=00:30:00
#SBATCH --partition=medium
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=4
#SBATCH --account=<project>
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 1280 core (10 full nodes) gpaw job, using hybrid
# MPI/OpenMP parallelization with 4 OpenMP threads per node,
# requesting 30 minutes time.
# Please experiment with optimum MPI task / OpenMP thread ratio with
# your particular input

module load gpaw  # Note: only the default 20.1.0-omp version supports OpenMP

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun gpaw-python input.py
```

**Example batch script for Mahti with pure MPI parallelization**

```
#!/bin/bash -l
#SBATCH --time=00:30:00
#SBATCH --partition=medium
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=128
#SBATCH --account=<project>
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 1280 core (10 full nodes) gpaw job, using pure
# MPI parallelization requesting 30 minutes time.

module load gpaw

export OMP_NUM_THREADS=1

srun gpaw-python input.py
```


## More information

-   [GPAW home page](https://wiki.fysik.dtu.dk/gpaw/)
