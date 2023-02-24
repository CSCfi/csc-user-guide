---
tags:
  - Free
---

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

Packages are by default installed in the directory '~/.julia/', but the target can be changed with an environmental variable `JULIA_DEPOT_PATH`.

```bash
export JULIA_DEPOT_PATH=/your/directory
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

### Running a package as a batch job
It is a best practice to package your code instead of running standalone scripts.
The standard Julia package includes, at minimum, `src/<package>.jl` and `Project.toml` files.
Including a command line interface in your program, such as `cli.jl`, is also a good idea.
In this example, we place scripts for activating the project environment and running a batch job in the `scripts` directory.

```text
<package>.jl/      # the package directory
├── scripts/       # directory for optional scripts
│   ├── pkg.jl     # script for installing the package locally
│   ├── env.sh     # environment for running the project
│   └── batch.sh   # batch script
├── src/           # directory for source files
│   ├── <package>.jl  # package module
│   └── cli.jl     # command-line interface
└── Project.toml   # configurations and dependencies
```

The `src/<package>.jl` file must define `module` keyword with the package name.

```julia
module <package>
# your code and exports
end
```

The `Project.toml` file defines configuration and dependencies similar to the following example.

```toml
name = "<package>"
uuid = "d8317c12-93af-4873-9588-10bf4a9df297"
authors = ["author <email>"]
version = "0.1.0"
[deps]
# dependencies
[compat]
julia = "1.8"
```

In Puhti and Mahti, it is best practice to place the project under a subdirectory in Projappl.
Furthermore, to install our Julia package and its dependencies to a specific directory, we must set the `JULIA_DEPOT_PATH` environment variable.
We should also point them to a subdirectory in Projappl.
We can use the following structure:

```text
/projappl/project_<id>/<subdirectory>/
├── .julia/  # location for Julia to install packages
└── <package>.jl/  # our Julia package
```

As the subdirectory, we can use your username (`$USER`) or another name to avoid mixing your Julia dependencies with others in the project.

Now, we can write our environment as a shell script, such as `scripts/env.sh`.

```bash
# Set the environment variables.
export JULIA_DEPOT_PATH="/projappl/project_<id>/<subdirectory>/.julia"

# Create the directory path if it does not exist.
mkdir -p "/projappl/project_<id>/<subdirectory>/"

# Load the Julia module.
module load julia
```

We can use Julia's package manager to install the package and its dependencies to the location we specified using the environment variables.
It is best to write it as a Julia script, such as `scripts/pkg.jl`, as follows.

```julia
using Pkg
Pkg.activate(".")
Pkg.instantiate()
Pkg.precompile()
```

Now, we can install the application using the command line as follows.
These scripts expect that your working directory is your Julia project.

```bash
# Activate the environment.
source scripts/env.sh

# Install the package locally. We need only to do this once.
julia scripts/pkg.jl
```

We can also test the application by running it from the command line.

```bash
# Invoke the application via the command line interface..
# The argument `--project=.` activates the Julia project.
julia --project=. src/cli.jl  # <cli-arguments>
```

To run a batch job, we can write a batch script, such as `batch.sh`, as below.

```bash
#!/bin/bash
#SBATCH --job-name=julia_test
#SBATCH --account=project_<id>
#SBATCH --partition=test
#SBATCH --time=0:01:0
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=10

source scripts/env.sh
srun julia --project=. src/cli.jl  # <cli-arguments>
```

You can test it by submitting the script to the Slurm scheduler.

```bash
sbatch scripts/batch.sh
```

## More information

- [Julia home page](https://julialang.org )
- [Documentation](https://docs.julialang.org)
