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

=== "Roihu-CPU"

    | Version | Module            | Notes |
    |:------- |:----------------- |:----- |
    | 25.7.0  | `gpaw/25.7.0`     | Plain installation. Same as `gpaw/pilot-25.7.0`. |
    | 26.7.0  | `gpaw/26.7.0`     | Containerized installation. |

    The installations include the following libraries: MPI, OpenMP, ScaLAPACK, ELPA, FFTW, libxc, libvdwxc, DFT-D3, DFT-D4.

=== "Roihu-GPU"

    | Version | Module            | Notes |
    |:------- |:----------------- |:----- |
    | 26.7.0  | `gpaw/26.7.0`     | Containerized installation. |

    The installations include the following libraries: MPI, OpenMP, ScaLAPACK, FFTW, libxc, libvdwxc, DFT-D3, DFT-D4.

=== "LUMI"

    GPAW is available as [a user-installable module](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/g/GPAW/).
    See [the LUMI installation instructions in GPAW documentation](https://gpaw.readthedocs.io/platforms/Cray/lumi.html)
    for detailed instructions.

## License

GPAW is free software available under GPL, version 3+.

## Usage

Since the default version, that is available with `module load gpaw`, is
subject to change when new versions are installed, we recommend to always load
a specific GPAW version:

```bash
module load gpaw/version
```

Use `gpaw info` to check the GPAW version and the included libraries.

See [GPAW documentation on parallel runs](https://gpaw.readthedocs.io/documentation/parallel_runs/parallel_runs.html#parallelization-options)
for instructions on how to enable high-performance libraries in the input script

!!! warning "Note"
    GPAW calculations are run with the `gpaw python` command.

### Batch script examples

=== "Roihu-CPU (partial node)"

    ```bash
    #!/bin/bash
    #SBATCH --job-name=gpaw
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=2 --cpus-per-task=1
    #SBATCH --mem-per-cpu=1G
    #SBATCH --time=00:30:00

    # Load gpaw module
    module load gpaw/version

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
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=192 --cpus-per-task=2  # The product should be 384
    #SBATCH --time=00:30:00

    # Test different values of
    # --ntasks-per-node and --cpus-per-task above
    # for your use case and use the values that give the best performance

    # Load gpaw module
    module load gpaw/version

    # Set the number of threads based on cpus-per-task
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

    # Place and bind threads to single cores
    # Comment the following lines if binding is not desired
    export OMP_PLACES=cores
    export OMP_PROC_BIND=spread

    # Run GPAW
    srun gpaw python input.py
    ```

## Custom GPAW environment on Roihu

It is possible to create a Python virtual environment on top of the GPAW module.
This is useful for installing additional Python packages alongside GPAW
and/or installing a development version of GPAW.

!!! info "Roihu-CPU and Roihu-GPU"
    The instructions below work for both Roihu-CPU and Roihu-GPU, but it is
    recommended to include the target platform in the environment name (like
    `venv-gpaw-cpu`), because binaries compiled for
    Roihu-CPU and Roihu-GPU are not compatible.


### Creating and using a Python virtual environment

Use the gpaw module to create a new virtual environment:

```bash
module load gpaw/26.7.0
python -m venv --system-site-packages venv-gpaw-cpu
module unload gpaw/26.7.0
```

To load this environment, use the activate script:
```bash
source venv-gpaw-cpu/bin/activate
```

!!! warning "Entrypoint scripts with virtual environment"

    Note that so-called entrypoint scripts like `gpaw` and `ase`
    are short-hands for `python -m gpaw` and `python -m ase`, respectively,
    but the difference is that `gpaw`/`ase` run in **the installation-time environment**
    whereas `python -m <module>` runs in **the currently active environment**,
    which is often desired.

    The entrypoint scripts get created in the virtual environment only
    when installing the corresponding packages in the environment.
    Therefore, when you load the newly created environment, the `gpaw`
    executable is not available, but you can execute it with `python -m gpaw` instead.


### Installing additional Python packages

Load the environment and install extra packages with pip:

```bash
# Load gpaw venv
source venv-gpaw-cpu/bin/activate

# Install a python package
# Note:
# - The constraint ensures that the provided high-performance numpy and scipy
#   are not reinstalled by pip with less-optimal versions
pip install --constraint /gpaw_container/config/constraints.txt <package>
```

### Installing a development version of GPAW

Load the environment, clone the gpaw code, and install it with pip:

```bash
# Load gpaw venv
source venv-gpaw-cpu/bin/activate

# Clone the gpaw development repository
git clone https://gitlab.com/gpaw/gpaw.git
cd gpaw

# Install GPAW
# Note:
# - The constraint ensures that the provided high-performance numpy and scipy
#   are not reinstalled by pip with less-optimal versions
# - The GPAW config is set to the siteconfig file tailored for Roihu
# - This installs in editable mode (leave the '-e' out if you don't want an editable install)
rm -rf build _build _gpaw.*.so gpaw.egg-info
GPAW_BUILD_JOBS=8 GPAW_CONFIG=/gpaw_container/config/siteconfig.py pip install --constraint /gpaw_container/config/constraints.txt --no-build-isolation -v --log build-cpu.log --config-settings editable_mode=compat -e .

# Check the installed gpaw
gpaw info
```

## More information

- [GPAW home page](https://gpaw.readthedocs.io/)
