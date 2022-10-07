# Julia

## Description

Julia is a high-level, high-performance dynamic programming language for
numerical computing. It provides a sophisticated compiler, distributed
parallel execution, numerical accuracy, and an extensive mathematical
function library.

See here for a [quick introduction and tutorial](https://github.com/csc-training/julia-introduction).

[TOC]

## Available

- Puhti: 1.8.1 compiled with Intel Math Kernel Library (MKL)
- Mahti: 1.7.2 compiled with OpenBLAS

## License

Free and open source under [MIT license](https://github.com/JuliaLang/julia/blob/master/LICENSE.md).

## Usage

### Loading Modules

To load a module for a stable version of Julia, use the following command

```bash
module load julia
```

### Interactive use

After loading the Julia module, it can be run interactively simply by
typing

```bash
julia
```

If more resources are required, one can request an interactive node
directly on Puhti with

```bash
srun --ntasks=1 --time=00:10:00 --mem=4G --pty --account=project_id --partition=small julia
```

### Installing packages

You can access to the package manager by pressing "]" during the interactive session. The packages are added to the project with an 'add' command.

```bash
julia> ]
(v1.8) pkg>
(v1.8) pkg> add Example
```

After adding a package, it can be loaded in Julia:

```bash
julia> using Example
```

Packages are by default installed in the directory '~/.julia/', but the target can be changed with an environmental variable 'JULIA_PKGDIR'.

```bash
export JULIA_PKGDIR=/your/directory
```

**NOTE:** Packages that work for one version of Julia might not work at all for another. Check the required version number.

More information about Julia's package manager you can found from its [documentation](https://julialang.github.io/Pkg.jl/v1/).

### Serial batch job

Sample single-processor Julia batch job on Puhti

```bash
#!/bin/bash 
#SBATCH --job-name=julia_serial
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=0:10:0
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1000

module load julia
srun julia my_script.jl
```

This runs the script `my_script.jl` one time using one cpu-core. You can find more information about batch jobs on Puhti from the [user guide](../computing/running/getting-started.md).

## More information

- [Julia home page](https://julialang.org )
- [Documentation](https://docs.julialang.org)
