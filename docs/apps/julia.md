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
- Mahti has Julia v1.8.5 with OpenBLAS


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

For available command line options, we can read the manual.

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

Instantiating an environment is a common operation when using a new Julia environment for the first time.


### Interactive job on Puhti
We can request an interactive node directly on Puhti as follows.

```bash
srun --ntasks=1 --time=00:10:00 --mem=4G --pty --account=<project> --partition=small julia
```


### Serial batch job on Puhti
A sample of a single-core Julia batch job on Puhti

```bash
#!/bin/bash 
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1000

module load julia
srun julia my_script.jl
```

The above batch job runs the Julia script `my_script.jl` using one CPU core.
You can find more information about batch jobs on Puhti from the [user guide](../computing/running/getting-started.md).


### Multi-core batch job on Puhti
A sample of a multi-core Julia batch job on Puhti.
We can start Julia with multiple threads by setting the `JULIA_NUM_THREADS` environment variable.
Alternatively, we can use the `--threads` option.

```bash
#!/bin/bash 
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1000

# set the number of threads based on --cpus-per-task
export JULIA_NUM_THREADS="$SLURM_CPUS_PER_TASK"

module load julia
srun julia my_script.jl
```

The above batch job runs the Julia script `my_script.jl` using two CPU cores.


### Changing installation location
The package manager installs packages to the `$HOME/.julia` directory by default.
We can change the directory by prepending the `JULIA_DEPOT_PATH` environment variable with a different directory.
In Puhti and Mahti, it is best practice to point the directory to Projappl as follows.

```bash
export JULIA_DEPOT_PATH="/projappl/<project>/.julia:$JULIA_DEPOT_PATH"
```

Julia automatically appends the default locations to the path when colon `:` is present in the path while running Julia.
You can run `julia -E 'DEPOT_PATH` to see the full path used at runtime.
In the future, the default paths are required for using shared packages specific to Puhti and Mahti.
You can read more from the documentation [`JULIA_DEPOT_PATH`](https://docs.julialang.org/en/v1/manual/environment-variables/#JULIA_DEPOT_PATH) and [`DEPOT_PATH`](https://docs.julialang.org/en/v1/base/constants/#Base.DEPOT_PATH).


### Packaging code
Packaging your code instead of running standalone scripts is a best practice.
The standard Julia package includes the module file, such as `src/Hello.jl`, and the `Project.toml` file.
Including a command line interface in your program, such as `src/cli.jl`, is also a good idea.

```text
Hello.jl/         # the package directory
├── src/          # directory for source files
│   ├── Hello.jl  # package module
│   └── cli.jl    # command line interface
└── Project.toml  # configurations and dependencies
```

The `Project.toml` file defines configuration and dependencies like the following example.

```toml
name = "Hello"
uuid = "d39f8c29-790d-4dca-9a6b-e0bca2099731"
authors = ["author <email>"]
version = "0.1.0"

[deps]
ArgParse = "c7e460c6-2fb9-53a9-8c5b-16f535851c63"

[compat]
julia = "1.8"
ArgParse = "1.1"
```

The `src/Hello.jl` file must define the `module` keyword with the package name.

```julia
module Hello

say(s) = println(s)
export say

end
```

We can use `ArgParse` package to create a command line interface `src/cli.jl` for the package.

```julia
using ArgParse
using Hello

s = ArgParseSettings()
@add_arg_table! s begin
    "--say"
        help = "say something"
end
args = parse_args(s)

say(args["say"])
```

We can also test the application by running it from the command line.

```bash
julia --project=. src/cli.jl --say "Hello world"
```


## More information
- [Julia website](https://julialang.org )
- [Julia documentation](https://docs.julialang.org)
- [Package manager documentation](https://pkgdocs.julialang.org/v1/)

See here for a [quick introduction and tutorial](https://github.com/csc-training/julia-introduction) on CSC training.
