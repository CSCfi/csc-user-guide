---
tags:
  - Free
catalog:
  name: GPAW
  description: Versatile DFT package
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
    - Roihu
---

# GPAW

GPAW is a density-functional theory (DFT) and beyond code based on the projector-augmented wave (PAW) method and
the atomic simulation environment (ASE). The wave functions can be described with
plane waves, uniform real-space grids, and atom-centered basis functions.

Some features of the software include:

- total energy calculations
- structural optimizations
- different boundary conditions (finite, wire, slab, bulk)
- efficient parallelization
- excited state properties within time-dependent density-functional theory

## Available

### Roihu

- Roihu-CPU: 25.7.0
- Check all available versions (and default version) with `module avail gpaw`
- The installation includes the following libraries: MPI, OpenMP, ScaLAPACK, ELPA, FFTW, libxc, libvdwxc, DFT-D3, DFT-D4
- See [GPAW documentation on parallel runs](https://gpaw.readthedocs.io/documentation/parallel_runs/parallel_runs.html#parallelization-options)
  for instructions on how to enable high-performance libraries in the input script
- The PAW setups are installed through `gpaw_data` package
- Use `gpaw info` for detailed version information


### Puhti and Mahti

- Puhti: 20.10.0, 21.1.0, 21.6.0, 22.1.0, 22.8.0, 24.6.0
- Mahti: 20.10.0, 21.1.0, 21.6.0, 22.1.0, 22.8.0, 23.9.1, 24.1.0, 24.6.0, 25.1.0, 25.7.0
- Check all available versions (and default version) with
    `module avail gpaw`
- Modules ending with `-omp` have the optional OpenMP parallelization enabled,
    see [GPAW documentation about parallel runs](https://wiki.fysik.dtu.dk/gpaw/documentation/parallel_runs/parallel_runs.html?highlight=openmp#manual-openmp)
    for more details.
- All installations before 24.1.0 use version **0.9.20000** of GPAW's PAW Setups.

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
    GPAW calculations are run with the `gpaw-python` command on Puhti and Mahti and with the `gpaw python` command on Roihu.

### Batch script examples

=== "Roihu-CPU (partial node)"

    ```bash
    #!/bin/bash
    #SBATCH --job-name=gpaw
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:30:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=2
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000M

    # Set the number of threads based on cpus-per-task
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

    # Place and bind threads to single cores
    # Comment the following lines if binding is not desired
    export OMP_PLACES=cores
    export OMP_PROC_BIND=spread

    # Run GPAW
    srun gpaw python input.py
    ```

=== "Roihu-CPU (full nodes)"

    ```bash
    #!/bin/bash
    #SBATCH --job-name=gpaw
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    ##SBATCH --partition=large  # uncomment if using 6 or more nodes
    #SBATCH --time=00:30:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=192 --cpus-per-task=2  # The product should be 384

    # Test different values of
    # --ntasks-per-node and --cpus-per-task above
    # for your use case and use the values that give the best performance

    # Set the number of threads based on cpus-per-task
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

    # Place and bind threads to single cores
    # Comment the following lines if binding is not desired
    export OMP_PLACES=cores
    export OMP_PROC_BIND=spread

    # Run GPAW
    srun gpaw python input.py
    ```

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

- [GPAW home page](https://gpaw.readthedocs.io/)
