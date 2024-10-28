---
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
Julia language is available on Puhti, Mahti, and LUMI from the command line using the [module system](../computing/modules.md).
It is also available on the web interface via [Jupyter](../computing/webinterface/julia-on-jupyter.md) and [VSCode](../computing/webinterface/vscode.md#julia-language).

If you find issues in using Julia on the cluster, you should [contact the servicedesk](../support/contact.md).


## Usage
### Using the Julia module
Julia language is available from the `julia` module.

=== "Puhti and Mahti"

    On Puhti and Mahti, we can load the module as follows:

    ```bash
    module load julia
    ```

=== "LUMI"

    On LUMI, we must add the module files under CSC's local directory to the module path before loading the module.

    ```bash
    module use /appl/local/csc/modulefiles
    module load julia
    ```

After loading the Julia module, we can use Julia with the `julia` command.
Without arguments, it starts an interactive Julia REPL.

```bash
julia
```

For available command line options, we can run `julia --help` or read the manual `man julia`.
For questions about the features of Julia language, we refer we recommend the official [documentation](https://docs.julialang.org) and the [discourse](https://discourse.julialang.org/) channel.


### Using the package manager
The standard method for installing Julia packages is to use the package manager, `Pkg`, from the standard library.
In Julia, we can import it as follows:

```julia
import Pkg
```

The common functions we use are `Pkg.add` to add packages, `Pkg.activate` to activate environments, and `Pkg.instantiate` to install all packages defined in the active environment.
The [Pkg documentation](https://pkgdocs.julialang.org/) provides more information on how to use Julia's package manager.


### Placing the Julia depot directory
The first directory on the Julia depot path controls where Julia stores installed packages, compiled files, log files, and other depots.
It is `$HOME/.julia` by default.
The home directory has a relatively small quota on Puhti, Mahti, and LUMI.
If you install large packages, we recommend placing the depot directory under Projappl to avoid running out of quota.
We can change the depot directory by prepending a new directory to `JULIA_DEPOT_PATH` environment variable.

For example, we can use the following by replacing the `<project>` with a CSC project.

```bash
export JULIA_DEPOT_PATH="/projappl/<project>/$USER/.julia:$JULIA_DEPOT_PATH"
```

Afterward, you can safely remove the default depot directory using `rm -r $HOME/.julia`.
For more information, you can read more about the [depot path documentation](https://docs.julialang.org/en/v1/base/constants/#Base.DEPOT_PATH).


### Multi-threading
Julia provides the `Threads` library for multi-threading.
It is included in the base library and imported by default in a Julia session.
We can start Julia with multiple threads by setting the `JULIA_NUM_THREADS` environment variable or starting Julia with the `--threads` option which overrides the value in the environment variable.
If Julia module is loaded within a Slurm job and the environment variable is not set, it is set to the amount of requested CPU cores (`--cpus-per-task`).
The default thread count is one.
We recommend reading the [multi-threading](https://docs.julialang.org/en/v1/manual/multi-threading/) section in Julia's manual for more details.


### Multi-processing and distributed computing
#### Distributed and ClusterManagers.jl
For multiprocessing and distributed computing, Julia provides the `Distributed` standard library.
We use it for multi-processing on the local node.
We can extend `Distributed` by installing the `ClusterManagers.jl` package, which allows us to add workers' processes to multiple nodes via Slurm using `SlurmManager`.
We recommend reading the [multi-processing and distributed computing](https://docs.julialang.org/en/v1/manual/distributed-computing/) section in Julia manual for more details.


#### MPI.jl
We can use MPI for distributed computing, especially over multiple nodes, in Julia on Puhti, Mahti, and LUMI using the `MPI.jl` package.
We can install it using the package manager as follows:

```julia
import Pkg
Pkg.add("MPI")
```

We can load the `julia-mpi` module which sets global preferences to the environment such that MPI.jl uses to use the system MPI installation and the correct command to start MPI processes.

```bash
module load julia-mpi
```

For more information, we recommend reading the [MPI.jl documentation](https://juliaparallel.org/MPI.jl/stable/).


### GPU programming
#### CUDA.jl
The GPU nodes on Puhti and Mahti contain NVidia GPUs which can be programmed using CUDA.
We can install the `CUDA.jl` package for CUDA programming in Julia using the package manager as follows:

```julia
import Pkg
Pkg.add("CUDA")
```

We can load the `julia-cuda` module which sets global preferences to the environment such that CUDA.jl uses the system CUDA installation.

```bash
module load julia-cuda
```

For information, we recommend reading the [CUDA.jl documentation](https://cuda.juliagpu.org/stable/).


#### AMDGPU.jl
The GPU nodes on LUMI contain AMD GPUs.
We can install the `AMDGPU.jl` package for programming AMD GPUs in Julia using the package manager as follows:

```julia
import Pkg
Pkg.add("AMDGPU")
```

We can load the `julia-amdgpu` module which sets global preferences to the environment such that AMDGPU.jl to use the system ROCm installation.

```bash
module load julia-amdgpu
```

For information, we recommend reading the [AMDGPU.jl documentation](https://amdgpu.juliagpu.org/stable/).


### Running Julia batch jobs on CSC clusters
[Running Julia batch jobs on CSC clusters](../support/tutorials/julia.md) section explains how to run serial, parallel, and GPU batch jobs with Julia on Puhti, Mahti, and LUMI.


### Further reading
For further reading about parallel and high-performance computing with Julia, we recommend the [Julia for high-performance scientific computing](https://enccs.github.io/julia-for-hpc/) from ENCCS and the [A brief tour of Julia for high-performance computing](https://forem.julialang.org/wikfeldt/a-brief-tour-of-julia-for-high-performance-computing-5deb) by Kjartan Thor Wikfeldt.
HLRS's training material for the [Julia for High-Performance Computing](https://github.com/carstenbauer/JuliaHLRS23) course offers a deep dive into programming high-performance code with Julia.
Finally, the [Julia on HPC Clusters](https://juliahpc.github.io) lists general notes about using and installing Julia on an HPC cluster.
