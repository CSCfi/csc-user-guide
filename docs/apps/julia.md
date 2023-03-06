---
tags:
  - Free
---

# Julia
## Description
Julia is a high-level, high-performance dynamic programming language for numerical computing.
It provides a sophisticated compiler, distributed parallel execution, numerical accuracy, and an extensive mathematical function library.

[TOC]


## License
Free and open source under [MIT license](https://github.com/JuliaLang/julia/blob/master/LICENSE.md).


## Available
- Puhti has Julia v1.8.5 with OpenBLAS
- Mahti has Julia v1.7.2 with OpenBLAS


## Usage
### Loading modules
We can load the Julia module using the following command.

```bash
module load julia
```

By default, it loads the latest stable version.


### Using Julia
After loading the Julia module, we can use Julia with the `julia` command.
Without arguments, it starts an interactive Julia REPL.

```bash
julia
```

For available command-line options, we can read the manual.

```sh
man julia
```


### Installing packages
Julia has a built-in package manager named `Pkg`.
During an interactive session, we can access it by pressing `]`.
We can load and use the package manager in scripts like other Julia packages.

We can add packages to the active environment using the `add` function.
On the Julia REPL, we can do it as follows.

```julia-repl
julia> ]
(v1.8) pkg>
(v1.8) pkg> add Example
```

The default environment is `v1.8`, as shown in the REPL.
We can do the same in a Julia script by loading `Pkg` and using the `add` function.

```julia
using Pkg
Pkg.add("Example")
```

After adding a package, we can load it in Julia.

```julia
using Example
```

Packages for one version of Julia might not work for another.
Check the required version number.

You can find more information about Julia's package manager in its [documentation](https://pkgdocs.julialang.org/v1/).


### Using environments
We can manage the dependencies of different Julia projects separately by using a different environment instead of the default environment.
The easiest way to use an environment is to use the `--project` option when starting Julia.
For example, we can use `julia --project=.` to activate an environment in the current working directory.
Alternatively, we can use the `Pkg.activate` function.

We define project metadata and dependencies in `Project.toml` file.
Adding or removing packages using the package manager manipulates the `Project.toml` file in the active environment.
Furthermore, the package manager maintains a full list of dependencies in `Manifest.toml` file.
It creates both of these files if they don't exist.

Let's consider a Julia project structured as follows.

```
.
├── my_script.jl
├── Project.toml
└── Manifest.toml
```

We can run the script using the project's environment as follows.

```bash
julia --project=. my_script.jl
```

Activating an environment does not automatically install the packages defined by `Manifest.toml` or `Project.toml`.
We can install packages using the `instantiate` function from `Pkg`.
An easy way to do it is using the following command.

```bash
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

This is a common operation when using a new Julia environment for the first time.


### Interactive job
We can request an interactive node directly on Puhti as follows.

```bash
srun --ntasks=1 --time=00:10:00 --mem=4G --pty --account=project_<id> --partition=small julia
```


### Serial batch job
A sample of a single-core Julia batch job on Puhti

```bash
#!/bin/bash 
#SBATCH --job-name=julia_serial
#SBATCH --account=project_<id>
#SBATCH --partition=small
#SBATCH --time=0:10:0
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1000

module load julia
srun julia my_script.jl
```

The above batch job runs the Julia script `my_script.jl` using one CPU core.
You can find more information about batch jobs on Puhti from the [user guide](../computing/running/getting-started.md).


### Multi-core batch job
A sample of a multi-core Julia batch job on Puhti.
We can start Julia with multiple threads using the `--threads` option.

```bash
#!/bin/bash 
#SBATCH --job-name=julia_serial
#SBATCH --account=project_<id>
#SBATCH --partition=small
#SBATCH --time=0:10:0
#SBATCH --ntasks=2
#SBATCH --mem-per-cpu=1000

module load julia
srun julia --threads 2 my_script.jl
```

The above batch job runs the Julia script `my_script.jl` using two CPU cores.


### Changing installation location
The package manager installs packages to the `$HOME/.julia` directory by default.
We can change the directory by prepending a path ending with a colon to a different directory using the `JULIA_DEPOT_PATH` environment variable.
The colon instructs Julia to automatically append the default locations to the path when running Julia.

```bash
export JULIA_DEPOT_PATH="/projappl/project_<id>/.julia:"
```

You can run `julia -E 'DEPOT_PATH` to see all the locations.


### Running a package as a batch job
It is a best practice to package your code instead of running standalone scripts.
The standard Julia package includes, at minimum, `src/<package>.jl` and `Project.toml` files.
Including a command line interface in your program, such as `cli.jl`, is also a good idea.
In this example, we place scripts for activating the project environment and running a batch job in the `scripts` directory.

```text
<package>.jl/      # the package directory
├── scripts/       # directory for optional scripts
│   ├── env.sh     # environment for running the project
│   └── batch.sh   # batch script
├── src/           # directory for source files
│   ├── <package>.jl  # package module
│   └── cli.jl     # command-line interface
└── Project.toml   # configurations and dependencies
```

The `src/<package>.jl` file must define the `module` keyword with the package name.

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
Furthermore, to install our Julia package and its dependencies to a specific directory, we must prepend a path the `JULIA_DEPOT_PATH` environment variable.
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
export JULIA_DEPOT_PATH="/projappl/project_<id>/<subdirectory>/.julia:"

# Create the directory path if it does not exist.
mkdir -p "/projappl/project_<id>/<subdirectory>/"

# Load the Julia module.
module load julia
```

We use Julia's package manager to install the package and its dependencies to the location we specified using the environment variables.
We can install the application using the command line as follows.
These scripts expect that your working directory is your Julia project.

```bash
# Activate the environment.
source scripts/env.sh

# Install the package locally. We need only to do this once.
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

We can also test the application by running it from the command line.

```bash
# Invoke the application via the command line interface..
# The argument `--project=.` activates the Julia project.
julia --project=. src/cli.jl  # <cli-arguments>
```

To run a batch job, we can write a batch script, such as `scripts/batch.sh`, as below.
We should set the `--threads` argument to the number of available threads.

```bash
#!/bin/bash
#SBATCH --job-name=julia_test
#SBATCH --account=project_<id>
#SBATCH --partition=test
#SBATCH --time=0:01:0
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=10

source scripts/env.sh
srun julia --project=. --threads 1 src/cli.jl  # <cli-arguments>
```

You can test it by submitting the script to the Slurm scheduler.

```bash
sbatch scripts/batch.sh
```


## More information
- [Julia website](https://julialang.org )
- [Julia documentation](https://docs.julialang.org)
- [Package manager documentation](https://pkgdocs.julialang.org/v1/)

See here for a [quick introduction and tutorial](https://github.com/csc-training/julia-introduction) on CSC training.
