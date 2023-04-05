---
tags:
  - Free
---

# Julia Language
[Julia language](https://julialang.org) is a high-level, high-performance dynamic programming language for numerical computing.
It provides a sophisticated compiler, distributed parallel execution, numerical accuracy, and an extensive mathematical function library.

[TOC]


## License
Free and open source under [MIT license](https://github.com/JuliaLang/julia/blob/master/LICENSE.md).


## Available
Julia is available on Puhti and Mahti.

```bash
module avail julia
```


## Usage
### Loading the Julia module
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

You can find answers to most questions relating the Julia language's features from the official [Julialang documentation](https://docs.julialang.org) or the [discourse](https://discourse.julialang.org/).
The `Base` contains the features that are included in the Julia language.
The standard library contains various packages that are included in the Julia installation.
Two important packages from the standard library are the Julia REPL and Julia's package manager named Pkg.
The package manager also has a REPL which we can access from the Julia REPL by pressing `]`.
You can find more information about how to use Julia's package manager from the [Pkg documentation](https://pkgdocs.julialang.org/v1/).


### Using environments
Julia manages dependecies of projects using environments.
An environment consists of two files, `Project.toml` and `Manifest.toml`, which specify dependecies for the environment.
We define project metadata, dependencies and compatibility constraints in `Project.toml` file.
Adding or removing packages using the package manager manipulates the `Project.toml` file in the active environment.
Furthermore, the package manager maintains a full list of dependencies in `Manifest.toml` file.
It creates both of these files if they don't exist.

Let's consider a Julia project structured as follows.

```
MyProject.jl
├── script.jl
├── Project.toml
└── Manifest.toml
```

We can activate an environment using the `--project` option when starting Julia or we can use the `Pkg.activate` function.
For example, we can open the Julia REPL with the project's environment active as follows:

```bash
julia --project=.
```

Activating an environment does not automatically install the packages defined by `Manifest.toml` or `Project.toml`.
For that, we need to invoke the `Pkg.instantiate` function with the project's environment active as follows:

```bash
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

Now, we can run the script using the project's environment as follows:

```bash
julia --project=. script.jl
```

If we don't specify an environment, Julia will activate the default environment.
We should always use unique environment for Julia projects instead of using the default environment.
That way, we can manage the dependencies of different Julia projects separately.


### Adding packages and compatibilities
On the Julia REPL, we can use the package manager by importing it.

```julia
using Pkg
```

We can add packages to the active environment using the `Pkg.add` function.
For example, we can add `ArgParse` package as follows.

```julia
Pkg.add("ArgParse")
```

Furthermore, we can set compatibility constraints to a package version.
For example, we can add compatibility to `ArgParse` as follows.

```julia
Pkg.compat("ArgParse", "1.1")
```

We can also set compatibility constraint to Julia version.

```julia
Pkg.compat("julia", "1.8")
```


### Depot and load paths
The package manager installs packages to the `$HOME/.julia` directory by default.
On Puhti and Mahti, the home directory has a fixed quota.
To avoid running out of quota, we recommend changing the directory to a directory under Projappl.
We can change the directory by prepending the `JULIA_DEPOT_PATH` environment variable with a different directory.
For example, we can use the following:

```bash
export JULIA_DEPOT_PATH="/projappl/<project>/$USER/.julia:$JULIA_DEPOT_PATH"
```

You can read more from the documentation [`DEPOT_PATH`](https://docs.julialang.org/en/v1/base/constants/#Base.DEPOT_PATH) and [`LOAD_PATH`](https://docs.julialang.org/en/v1/base/constants/#Base.LOAD_PATH).


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

We can use the command line interface as follows.

```bash
julia --project=. src/cli.jl --say "Hello world"
```

Creating and using a command line interface with batch scripts is the best practice compared to hard-coding values to the scripts.


### Running jobs
We explain how to run jobs on Puhti and Mahti in the [**Running Julia jobs**](../support/tutorials/julia.md) tutorial.


## Resources
For further reading about parallel and high-performance computing with Julia, we recommend the [Julia for high-performance scientific computing](https://enccs.github.io/Julia-for-HPC) from ENCCS and the [A brief tour of Julia for high-performance computing](https://forem.julialang.org/wikfeldt/a-brief-tour-of-julia-for-high-performance-computing-5deb) written by Kjartan Thor Wikfeldt.
CSC training also has a [quick introduction and tutorial](https://github.com/csc-training/julia-introduction) to Julia.
