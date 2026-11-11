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
    GPAW calculations are run with the `gpaw python` command.

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

## More information

- [GPAW home page](https://gpaw.readthedocs.io/)
