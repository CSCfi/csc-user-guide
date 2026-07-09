---
tags:
  - Free
catalog:
  name: Julia Language
  description:  High-level, high-performance dynamic programming language for numerical computing
  license_type: Free
  disciplines:
    - Mathematics and Statistics
  available_on:
    - LUMI
    - Roihu
    - Mahti
---

# Julia Language
[Julia language](https://julialang.org) is a high-performance, dynamic programming language.
Julia is excellent for scientific computing because it can compile efficient native code using LLVM and includes mathematical functions, parallel computing capabilities, and a package manager in the standard library.
Furthermore, Julia's syntax is intuitive and easy to learn, the multiple-dispatch paradigm allows writing composable code, increasing the ability to reuse existing code, and environments enable executing code in a reproducible way.

[TOC]


## License
Julia language is licensed under free and open source [MIT license](https://github.com/JuliaLang/julia/blob/master/LICENSE.md).


## Citation
If you use Julia in your research, please cite the following paper:

> Jeff Bezanson, Alan Edelman, Stefan Karpinski, and Viral B. Shah (2017).
> Julia: A Fresh Approach to Numerical Computing.
> SIAM Review, 59(1), 65–98.
> DOI: [10.1137/141000671](https://doi.org/10.1137/141000671)

To find the correct citation for a specific Julia package, you can use the `pkg> status` command or consult the package's documentation and repository.


## Available
Julia language is available on Roihu-CPU, Roihu-GPU, Mahti, and LUMI from the command line using the [module system](../computing/modules.md).
It is also available on the web interface via [Jupyter](../computing/webinterface/julia-on-jupyter.md) and [VSCode](../computing/webinterface/vscode.md#julia-language).

If you find issues in using Julia on the cluster, you should [contact the servicedesk](../support/contact.md).


## Usage
### Using the Julia module
Julia language is available from the `julia` module.

=== "Roihu-CPU, Roihu-GPU and Mahti"

    On Roihu-CPU, Roihu-GPU and Mahti, we can load the module as follows:

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
For questions about the features of Julia language, we recommend the official [documentation](https://docs.julialang.org) and the [discourse](https://discourse.julialang.org/) channel.


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
The home directory has a relatively small quota on Roihu, Mahti, and LUMI.
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
#### Distributed and SlurmClusterManager.jl
For multiprocessing and distributed computing, Julia provides the `Distributed` standard library.
We use it for multi-processing on the local node.
We can extend `Distributed` by installing the `SlurmClusterManager.jl` package, which allows us to add workers' processes to multiple nodes via Slurm using `SlurmManager`.
We recommend reading the [multi-processing and distributed computing](https://docs.julialang.org/en/v1/manual/distributed-computing/) section in Julia manual for more details.


#### MPI.jl
We can use MPI for distributed computing, especially over multiple nodes, in Julia on Roihu-CPU, Roihu-GPU, Mahti, and LUMI using the `MPI.jl` package.
We can install it using the package manager as follows:

```julia
import Pkg
Pkg.add("MPI")
```

We can load the `julia-mpi` module which sets global preferences to the environment such that MPI.jl uses the system MPI installation and the correct command to start MPI processes.

```bash
module load julia-mpi
```

For more information, we recommend reading the [MPI.jl documentation](https://juliaparallel.org/MPI.jl/stable/).


### GPU programming
#### CUDA.jl
The GPU nodes on Roihu-GPU and Mahti contain NVidia GPUs which can be programmed using CUDA.
We can install the `CUDA.jl` package for CUDA programming in Julia using the package manager as follows:

```julia
import Pkg
Pkg.add("CUDA")
```

We can load the `julia-cuda` module which sets global preferences to the environment such that CUDA.jl uses the system CUDA installation.

```bash
module load julia-cuda
```

For more information, we recommend reading the [CUDA.jl documentation](https://cuda.juliagpu.org/stable/).


#### AMDGPU.jl
The GPU nodes on LUMI contain AMD GPUs.
We can install the `AMDGPU.jl` package for programming AMD GPUs in Julia using the package manager as follows:

```julia
import Pkg
Pkg.add("AMDGPU")
```

We can load the `julia-amdgpu` module which sets global preferences to the environment such that AMDGPU.jl uses the system ROCm installation.

```bash
module load julia-amdgpu
```

For more information, we recommend reading the [AMDGPU.jl documentation](https://amdgpu.juliagpu.org/stable/).


### Further reading
For further reading about parallel and high-performance computing with Julia, we recommend the [Julia for high-performance scientific computing](https://enccs.github.io/julia-for-hpc/) from ENCCS and the [A brief tour of Julia for high-performance computing](https://forem.julialang.org/wikfeldt/a-brief-tour-of-julia-for-high-performance-computing-5deb) by Kjartan Thor Wikfeldt.
HLRS's training material for the [Julia for High-Performance Computing](https://github.com/carstenbauer/JuliaHLRS23) course offers a deep dive into programming high-performance code with Julia.
Finally, the [Julia on HPC Clusters](https://juliahpc.github.io) lists general notes about using and installing Julia on an HPC cluster.


## Running Julia batch jobs on CSC clusters
This section contains examples for running various Julia batch jobs on Roihu-CPU, Roihu-GPU, Mahti and LUMI clusters.
They demonstrate the usage of the Julia environment described [above](#usage) for various batch jobs.
They are adapted from the general instructions of running jobs on [Roihu and Mahti](../computing/running/getting-started.md) and on [LUMI](https://docs.lumi-supercomputer.eu/runjobs/).
Note that we do not use `srun` to start processes in the batch script.
Instead we use Julia for process management or call `srun` inside the Julia code.

Before running the examples, we need to instantiate the Julia project on the login node.
That is, run the following command in the directory with your Julia environment where `Project.toml` file is located.


=== "Roihu-CPU and Roihu-GPU"
    ```bash
    module purge
    module load julia
    julia --project=. --threads=1 -e 'using Pkg; Pkg.instantiate()'
    ```

=== "Mahti"
    ```bash
    module load julia
    julia --project=. --threads=1 -e 'using Pkg; Pkg.instantiate()'
    ```

=== "LUMI"
    ```bash
    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. --threads=1 -e 'using Pkg; Pkg.instantiate()'
    ```

You can use multiple threads `--threads=10` which will speed up the precompilation.


### Serial program
We use the following directory structure and assume it is our working directory.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

```julia title="script.jl"
println("Hello world!")
```

=== "Roihu-CPU"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module purge
    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=interactive
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1875

    module load julia
    julia --project=. script.jl
    ```


=== "LUMI"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. script.jl
    ```


### Multi-threading on single node
We use the following directory structure and assume it is our working directory.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

```julia title="script.jl"
# Number of threads
n = Threads.nthreads()
println(n)

# Lets fill the id of each thread to the ids array.
ids = zeros(Int, n)
Threads.@threads for i in eachindex(ids)
    ids[i] = Threads.threadid()
end
println(ids)

# Alternatively, we can use the @spawn macro to run task on threads.
ids = zeros(Int, n)
@sync for i in eachindex(ids)
    Threads.@spawn ids[i] = Threads.threadid()
end
println(ids)
```

=== "Roihu-CPU"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module purge
    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --mem-per-cpu=0

    module load julia
    julia --project=. script.jl
    ```

=== "LUMI"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. script.jl
    ```


### Multi-processing on single node
We use the following directory structure and assume it is our working directory.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

```toml title="Project.toml"
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

```julia title="script.jl"
using Distributed

# We set one worker process per core.
proc_num = Sys.CPU_THREADS

# Environment variables that we pass to the worker processes.
# We set the thread count to one since each process uses one core.
proc_env = [
    "JULIA_NUM_THREADS"=>"1",
    "JULIA_CPU_THREADS"=>"1",
    "OPENBLAS_NUM_THREADS"=>"1",
]

# We add worker processes to the local node using LocalManager.
addprocs(proc_num; env=proc_env, exeflags="--project=.")

# We use the `@everywhere` macro to include the task function in the worker processes.
# We must call `@everywhere` after adding worker processes; otherwise the code won't be included in the new processes.
@everywhere function task()
    return (worker=myid(), hostname=gethostname(), pid=getpid())
end

# We run the task function in each worker process.
futures = [@spawnat worker task() for worker in workers()]

# Then, we fetch the output from the processes.
outputs = fetch.(futures)

# Remove processes after we are done.
rmprocs.(workers())

# Print the outputs of master and worker processes.
println(task())
println.(outputs)
```

=== "Roihu-CPU"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module purge
    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --mem-per-cpu=0

    module load julia
    julia --project=. script.jl
    ```

=== "LUMI"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. script.jl
    ```


### Multi-processing on multiple nodes
We use the following directory structure and assume it is our working directory.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

```toml title="Project.toml"
[deps]
SlurmClusterManager = "c82cd089-7bf7-41d7-976b-6b5d413cbe0a"
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

```julia title="script.jl"
using Distributed
using SlurmClusterManager

# Environment variables that we pass to the worker processes.
# We set the thread count to one since each process uses one core.
n = get(ENV, "SLURM_CPUS_PER_TASK", "1")
proc_env = [
    "JULIA_NUM_THREADS"=>"$n",
    "JULIA_CPU_THREADS"=>"$n",
    "OPENBLAS_NUM_THREADS"=>"$n",
]

# We add worker processes across the allocated nodes using SlurmManager
manager = SlurmManager(; launch_timeout=300)
addprocs(manager; env=proc_env, exeflags="--project=.")

# We use the `@everywhere` macro to include the task function in the worker processes.
# We must call `@everywhere` after adding worker processes; otherwise the code won't be included in the new processes.
@everywhere function task()
    return (worker=myid(), hostname=gethostname(), pid=getpid())
end

# We run the task function in each worker process.
futures = [@spawnat worker task() for worker in workers()]

# Then, we fetch the output from the processes.
outputs = fetch.(futures)

# Remove processes after we are done.
rmprocs.(workers())

# Print the outputs of master and worker processes.
println(task())
println.(outputs)
```

=== "Roihu-CPU"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=384
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module purge
    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module load julia
    julia --project=. script.jl
    ```

=== "LUMI"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. script.jl
    ```


### MPI program
We launch the MPI program using Julia's `mpiexec` wrapper function.
The wrapper function substitutes the correct command from local preferences to the `mpirun` variable to run the MPI program.
The command is `srun` in Roihu, Mahti, and LUMI.
The wrapper allows us to write more flexible code, such as mixing MPI and non-MPI code, and more portable code because the command to run MPI programs can vary across platforms.
We note that for large-scale Julia MPI jobs with thousands of ranks, we have to distribute the [depot directory to local node storage or memory](https://juliahpc.github.io/user_faq/#how_to_cope_with_a_large_number_of_mpi_processes_accessing_the_same_julia_depot) and modify the depot paths accordingly.
Otherwise, package loading will become extremely slow.


We use the following directory structure and assume it is our working directory.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
├── prog.jl       # Julia MPI program
└── script.jl     # Julia script
```

```toml title="Project.toml"
[deps]
MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"
```

```julia title="script.jl"
using MPI
mpiexec(mpirun -> run(`$mpirun julia --project=. prog.jl`))
```

```julia title="prog.jl"
using MPI

MPI.Init()
comm = MPI.COMM_WORLD
rank = MPI.Comm_rank(comm)
size = MPI.Comm_size(comm)
println("Hello from rank $(rank) out of $(size) from host $(gethostname()) and process $(getpid()).")
MPI.Barrier(comm)
```

=== "Roihu-CPU"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=384
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=1000

    module purge
    module load julia
    module load julia-mpi
    julia --project=. script.jl
    ```

=== "Mahti"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module load julia
    module load julia-mpi
    julia --project=. script.jl
    ```

=== "LUMI"
    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module use /appl/local/csc/modulefiles
    module load julia
    module load julia-mpi
    julia --project=. script.jl
    ```


### Single GPU
We use the following directory structure and assume it is our working directory.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

=== "Roihu-GPU"
    ```toml title="Project.toml"
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"
    ```

    ```julia title="script.jl"
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = A_d * A_d
    ```

    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=72
    #SBATCH --gres=gpu:gh200:1

    module purge
    module load julia
    module load julia-cuda
    julia --project=. script.jl
    ```

=== "Mahti"
    ```toml title="Project.toml"
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"

    [compat]
    CUDA = "< 5.9"
    ```

    ```julia title="script.jl"
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = A_d * A_d
    ```

    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=32
    #SBATCH --gres=gpu:a100:1

    module load julia
    module load julia-cuda
    julia --project=. script.jl
    ```

=== "LUMI"
    ```toml title="Project.toml"
    [deps]
    AMDGPU = "21141c5a-9bdb-4563-92ae-f87d6854732e"
    ```

    ```julia title="script.jl"
    using AMDGPU

    A = rand(2^9, 2^9)
    A_d = ROCArray(A)
    B_d = A_d * A_d
    ```

    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --gpus-per-node=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=8
    #SBATCH --mem-per-cpu=1750

    module use /appl/local/csc/modulefiles
    module load julia
    module load julia-amdgpu
    julia --project=. script.jl
    ```


### GPU-aware MPI
We use the following directory structure and assume it is our working directory.
The `prog.jl` code is adapted from this [source](https://gist.github.com/luraess/a47931d7fb668bd4348a2c730d5489f4).


```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
├── prog.jl       # Julia GPU-aware MPI program
└── script.jl     # Julia script
```

```julia title="script.jl"
using MPI
mpiexec(mpirun -> run(`$mpirun julia --project=. prog.jl`))
```

=== "Roihu-GPU"
    ```toml title="Project.toml"
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"
    MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"
    ```

    ```julia title="prog.jl"
    using MPI
    using CUDA

    const gpu_devices = CUDA.devices()
    const num_devices = length(gpu_devices)

    MPI.Init()
    comm = MPI.COMM_WORLD
    rank = MPI.Comm_rank(comm)
    # select device
    comm_l = MPI.Comm_split_type(comm, MPI.COMM_TYPE_SHARED, rank)
    rank_l = MPI.Comm_rank(comm_l)
    device = CUDA.device!(mod(rank_l, num_devices))
    gpu_id = CUDA.deviceid(CUDA.device())
    # select device
    size = MPI.Comm_size(comm)
    dst  = mod(rank+1, size)
    src  = mod(rank-1, size)
    println("rank=$rank rank_loc=$rank_l (gpu_id=$gpu_id - $device), size=$size, dst=$dst, src=$src")
    N = 2^16  # Minimum array size for gdrcopy to work.
    send_mesg = CuArray{Float64}(undef, N)
    recv_mesg = CuArray{Float64}(undef, N)
    fill!(send_mesg, Float64(rank))
    CUDA.synchronize()
    rank==0 && println("start sending...")
    MPI.Sendrecv!(send_mesg, dst, 0, recv_mesg, src, 0, comm)
    println("sum(recv_mesg) on proc $rank: $(sum(recv_mesg))")
    rank==0 && println("done.")
    MPI.Finalize()
    ```

    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpumedium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=72
    #SBATCH --gres=gpu:gh200:4

    module purge
    module load julia
    module load julia-mpi
    module load julia-cuda
    julia --project=. script.jl
    ```

=== "LUMI"
    ```toml title="Project.toml"
    [deps]
    AMDGPU = "21141c5a-9bdb-4563-92ae-f87d6854732e"
    MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"
    ```

    ```julia title="prog.jl"
    using MPI
    using AMDGPU
    MPI.Init()
    comm = MPI.COMM_WORLD
    rank = MPI.Comm_rank(comm)
    # select device
    comm_l = MPI.Comm_split_type(comm, MPI.COMM_TYPE_SHARED, rank)
    rank_l = MPI.Comm_rank(comm_l)
    device = AMDGPU.device_id!(rank_l+1)
    gpu_id = AMDGPU.device_id(AMDGPU.device())
    # select device
    size = MPI.Comm_size(comm)
    dst  = mod(rank+1, size)
    src  = mod(rank-1, size)
    println("rank=$rank rank_loc=$rank_l (gpu_id=$gpu_id - $device), size=$size, dst=$dst, src=$src")
    N = 4
    send_mesg = ROCArray{Float64}(undef, N)
    recv_mesg = ROCArray{Float64}(undef, N)
    AMDGPU.synchronize()
    rank==0 && println("start sending...")
    MPI.Sendrecv!(send_mesg, dst, 0, recv_mesg, src, 0, comm)
    println("recv_mesg on proc $rank: $recv_mesg")
    rank==0 && println("done.")
    ```

    ```bash title="batch.sh"
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --gpus-per-node=8
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=8
    #SBATCH --mem-per-cpu=0

    module use /appl/local/csc/modulefiles
    module load julia
    module load julia-mpi
    module load julia-amdgpu
    julia --project=. script.jl
    ```


## Notes
### Multi-threading in linear algebra
Julia uses OpenBLAS as the default `LinearAlgebra` backend.
External linear algebra backends such as OpenBLAS use internal threading.
We can set their thread counts using environment variables.
The `julia` module sets them to the number of CPU threads.

```bash
export OPENBLAS_NUM_THREADS=$JULIA_CPU_THREADS
```

We must be careful not to oversubscribe cores when using BLAS operations within Julia threads or processes.
We can change the amount of BLAS threads at runtime using the `BLAS.set_num_threads` function.

```julia
using LinearAlgebra

# Number of threads
n = Threads.nthreads()

# Define a matrix
X = rand(1000, 1000)

# Set the number of threads to one before performing BLAS operations of multiple Julia threads.
BLAS.set_num_threads(1)
Y = zeros(n)
Threads.@threads for i in 1:n  # uses n Julia threads
    Y[i] = sum(X * X)          # uses one BLAS thread
end

# Set the number of threads back to the default when performing BLAS operation on a single Julia Thread.
BLAS.set_num_threads(n)
Z = zeros(n)
for i in 1:n                   # uses one Julia thread
    Z[i] = sum(X * X)          # uses n BLAS threads
end
```

There are [caveats](https://discourse.julialang.org/t/matrix-multiplication-is-slower-when-multithreading-in-julia/56227/12?u=carstenbauer) for using different numbers than one or all cores of BLAS threads on OpenBLAS.
