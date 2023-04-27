
tags:
  - Free
---

# Julia Language
[Julia language](https://julialang.org) is a high-performance, dynamic programming language.
Julia is excellent for scientific computing because it can compile efficient native code using LLVM and includes mathematical functions, parallel computing capabilities, and a package manager in the standard library.
Furthermore, Julia's syntax is intuitive and easy to learn, the multiple-dispatch paradigm allows writing composable code, increasing the ability to reuse existing code, and environments enable executing code in a reproducible way.

[TOC]


## License
Julia language is licensed under free and open source [MIT license](https://github.com/JuliaLang/julia/blob/master/LICENSE.md).


## Available
Julia language is available on Puhti and Mahti using the [module system](../computing/modules.md).

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


### Using Julia on the command line
After loading the Julia module, we can use Julia with the `julia` command.
Without arguments, it starts an interactive Julia REPL.

```bash
julia
```

For available command line options, we can read the manual.

```sh
man julia
```

The official [Julialang documentation](https://docs.julialang.org) or the [discourse](https://discourse.julialang.org/) can answer most questions regarding the features of the Julia language.
The Julia language includes the standard language features in Base.
Additionally, it includes various packages in the Julia installation as part of the standard library.
Julia's REPL and Pkg, the package manager, are two important packages within the standard library. Pressing ] in the Julia REPL will allow access to the package manager's REPL.
The [Pkg documentation](https://pkgdocs.julialang.org/) provides more information on how to use Julia's package manager.


### Using environments
Julia manages dependencies of projects using environments.
An environment consists of two files, `Project.toml` and `Manifest.toml`, which specify dependencies for the environment.
We define project metadata, dependencies, and compatibility constraints in `Project.toml` file.
Adding or removing packages using the package manager manipulates the `Project.toml` file in the active environment.
Furthermore, the package manager maintains a full list of dependencies in `Manifest.toml` file.
It creates both of these files if they don't exist.
Let's consider a Julia project structured as follows.

```
project
├── script.jl
├── Project.toml
└── Manifest.toml
```

We can activate an environment using the `--project` option when starting Julia or use the `Pkg.activate` function in existing Julia session.
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

Julia will activate the default environment if we don't specify an environment.
We should always use a unique environment for Julia projects instead of the default environment.
That way, we can manage the dependencies of different Julia projects separately.


### Adding packages to an environment
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

We can also set compatibility constraints to the Julia version.

```julia
Pkg.compat("julia", "1.8")
```


### Depot and load paths
The Julia constants [`Base.DEPOT_PATH`](https://docs.julialang.org/en/v1/base/constants/#Base.DEPOT_PATH) and [`Base.LOAD_PATH`](https://docs.julialang.org/en/v1/base/constants/#Base.LOAD_PATH) constants control the directories where Julia loads code.
To set them via the shell, we use the `JULIA_DEPOT_PATH` and `JULIA_LOAD_PATH` environment variables.
The Julia module automatically appends the default depot and load paths to ensure the standard library and shared depots are available.
The CSC-specific shared depots are installed in the `JULIA_CSC_DEPOT` directory, and the shared environment is in the `JULIA_CSC_ENVIRONMENT` directory.
We can look up the shared packages and their versions using the package manager as follows:

```bash
julia --project="$JULIA_CSC_ENVIRONMENT" -e 'using Pkg; Pkg.status()'
```

The first directory on the depot path controls where Julia stores installed packages, compiled files, log files, and other depots.

!!! warning "Changing the default depot directory"
    The default depot directory is `$HOME/.julia`.
    However, the home directory has a fixed quota for Puhti and Mahti.
    Therefore, we recommend changing the directory to a directory under Projappl or Scratch to avoid running out of quota because some packages install a large amounts of files.
    Afterwards, you can safely remove the default depot directory using `rm -r $HOME/.julia`.

We can change the directory by prepending the `JULIA_DEPOT_PATH` with a different directory.
For example, we can use the following by replacing the `<project>` with your CSC project.

```bash
export JULIA_DEPOT_PATH="/projappl/<project>/$USER/.julia:$JULIA_DEPOT_PATH"
```


### Creating a package with command line interface
We should package the code as a code base grows instead of running standalone scripts.
A Julia package includes a module file, such as `src/Hello.jl`, and the `Project.toml` file.
Including a command line interface in your program, such as `src/cli.jl`, is also wise.
Let's consider a project structured as below.

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
It also exports the functions and variables we want to expose in its API.
For example, the `Hello` module below defines and exports the `say` function.

```julia
module Hello

say(s) = println(s)

export say

end
```

We can use `ArgParse` package to create a command line interface `src/cli.jl` for the package.
For example, the command line interface below defines an option `--say` whose value is parsed into a string and supplied to the `say` function imported from the `Hello` module.

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

We should define and use a command line interface because it is more flexible than hard-coding values to the scripts.


### Running Julia jobs on Puhti and Mahti
We explain how to run serial, parallel and GPU jobs with Julia on Puhti and Mahti in the [**Running Julia jobs on Puhti and Mahti clusters**](../support/tutorials/julia.md) section.


### Using Julia on Jupyter and VSCode
Julia is also available on the web interface via [**Jupyter**](../computing/webinterface/julia-on-jupyter.md) and [**VSCode**](../computing/webinterface/vscode.md#julia-language).
