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

-   Puhti: 1.4.0, 1.5.2
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
`module load gpaw/1.4.0`

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


## More information

-   [GPAW home page](https://wiki.fysik.dtu.dk/gpaw/)
