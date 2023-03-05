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

By default it loads the latest stable version.


### Interactive use
After loading the Julia module, we can run it interactively with the following command.

```bash
julia
```

If we need more resources, we can request an interactive node directly on Puhti as follows.

```bash
srun --ntasks=1 --time=00:10:00 --mem=4G --pty --account=project_id --partition=small julia
```


### Installing packages
Julia has an built-in package manager called `Pkg`.
During an interactive session, we can access it by pressing `]`.
In scripts, we can use the package manager in the same way as other Julia packages.

The packages are added to the project with an `add` command.
On julia REPL we can do it as follows.

```julia-repl
julia> ]
(v1.8) pkg>
(v1.8) pkg> add Example
```

The package is added to the active environment, in this case, the default environemnt `(v1.8)`.
By default, Julia's package manager installs packages to the `$HOME/.julia` directory.

We can do the same in a Julia script.

```julia
using Pkg
Pkg.add("Example")
```

After adding a package, we can load it in Julia.

```julia
using Example
```

**NOTE:** Packages that work for one version of Julia might not work at all for another. Check the required version number.

More information about Julia's package manager you can be found in its [documentation](https://julialang.github.io/Pkg.jl/v1/).


## Using a custom environment
We can manage dependencies of Julia project by using a custom environment instead of the default environment.
The easiest way to use an environment is to use the `--project=<path>` option when starting julia to active an environment in the `<path>`.
For example, we can use the command `julia --project=.` to start an environemnt in the current working directory.
If we now add new package, they will be written to the `Project.toml` file.
Furhermore, the full list of all dependencies will be written to the `Manifest.toml` file.
Both of these files are created automatically if they don't exist.

Let's consider a Julia project structured as follows.

```
.
├── script.jl
├── Project.toml
└── Manifest.toml
```

We can run the script using the project's environment as follows.

```bash
julia --project=. script.jl
```

Activating an environment does not automatically install the packages defined by `Manifest.toml` or `Project.toml`.
We can install packages using the `instantiate` function from `Pkg` as follows.

```bash
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

This is common operation when using a Julia environment for the first time.


### Serial batch job
Sample single-processor Julia batch job on Puhti

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

This runs the script `my_script.jl` one time using one CPU-core.
You can find more information about batch jobs on Puhti from the [user guide](../computing/running/getting-started.md).


### Multi-core batch job
Sample of multi-core Julia batch job on Puhti.
We can start julia with multiple threads using the `--threads` option.

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


## Changing installation location
We can change the directory by prepending a path ending with a colon to a different directory using the `JULIA_DEPOT_PATH` environment variable.
The colon instructs Julia to automatically append the default locations to the path when running Julia.

```bash
export JULIA_DEPOT_PATH="/projappl/project_id/.julia:"
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
