---
tags:
  - Free
---

# GPAW

GPAW is an efficient program package for electronic structure
calculations. It is based on the density-functional theory (DFT)
implemented within the projector augmented wave (PAW), and it can utilize
various basis sets (uniform real-space grids, plane waves, localized
atomic orbital basis).

Some features of the software include:

- total energy calculations
- structural optimizations
- different boundary conditions (finite, wire, slab, bulk)
- efficient parallelization
- excited state properties within time-dependent density-functional
    theory

[TOC]

## Available

- Puhti: 20.10.0, 21.1.0, 21.6.0, 22.1.0, 22.8.0
- Mahti: 20.10.0, 21.1.0, 21.6.0, 22.1.0, 22.8.0, 23.9.1, 24.1.0
- Check all available versions (and default version) with
    `module avail gpaw`
- Modules ending with `-omp` have the optional OpenMP parallelization enabled,
    see [GPAW documentation about parallel runs](https://wiki.fysik.dtu.dk/gpaw/documentation/parallel_runs/parallel_runs.html?highlight=openmp#manual-openmp)
    for more details.

### PAW Setups

All installations (except 24.1.0) use version **0.9.20000** of GPAW's PAW Setups.

## License

GPAW is free software available under GPL, version 3+.

## Usage

Since the default version, that is available with `module load gpaw`, is
subject to change when new versions are installed, we recommend to always load
a specific GPAW version:

```bash
module load gpaw/version
```

!!! warning "Note"
    In CSC environment, GPAW calculations are run with the `gpaw-python` command.

### Enabling ELPA

On Mahti, GPAW can use the ELPA library to speed up the diagonalization step. Especially with LCAO calculations, ELPA can improve
the performance. In order to use ELPA, the `'use_elpa' : True` setting needs to be included in the parallelization options in GPAW input
(see [GPAW documentation](https://wiki.fysik.dtu.dk/gpaw/documentation/lcao/lcao.html#notes-on-performance) for more information).

### Batch script examples

=== "Puhti"

    ```bash
    #!/bin/bash -l
    #SBATCH --time=00:30:00
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40
    #SBATCH --mem-per-cpu=2GB
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END #uncomment to get mail

    # this script runs a 80 core (2 full nodes) gpaw job, requesting
    # 30 minutes time and 2 GB of memory for each core

    module load gpaw/21.1.0

    srun gpaw-python input.py
    ```

=== "Mahti (hybrid MPI/OpenMP parallelization)"

    ```bash
    #!/bin/bash -l
    #SBATCH --time=00:30:00
    #SBATCH --partition=medium
    #SBATCH --nodes=10
    #SBATCH --ntasks-per-node=32
    #SBATCH --cpus-per-task=4
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END #uncomment to get mail

    # this script runs a 1280 core (10 full nodes) gpaw job, using hybrid
    # MPI/OpenMP parallelization with 4 OpenMP threads per node,
    # requesting 30 minutes time.
    # Please experiment with optimum MPI task / OpenMP thread ratio with
    # your particular input

    # Note: only the modules with "-omp" ending supports OpenMP
    # (default version in Mahti is OpenMP enabled)

    module load gpaw/21.1.0-omp

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

    srun gpaw-python input.py
    ```

=== "Mahti (pure MPI parallelization)"

    ```bash
    #!/bin/bash -l
    #SBATCH --time=00:30:00
    #SBATCH --partition=medium
    #SBATCH --nodes=10
    #SBATCH --ntasks-per-node=128
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END #uncomment to get mail

    # this script runs a 1280 core (10 full nodes) gpaw job, using pure
    # MPI parallelization requesting 30 minutes time.

    module load gpaw/21.1.0

    export OMP_NUM_THREADS=1

    srun gpaw-python input.py
    ```

## More information

- [GPAW home page](https://wiki.fysik.dtu.dk/gpaw/)
