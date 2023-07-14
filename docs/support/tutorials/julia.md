# Using Julia on Puhti, Mahti, and LUMI clusters
Instructions for running serial, parallel, and GPU jobs with Julia on Puhti, Mahti, and LUMI clusters.

[TOC]


## Introduction
These instructions are adapted from the general instructions of running jobs on [Puhti and Mahti](../../computing/running/getting-started.md) and on [LUMI](https://docs.lumi-supercomputer.eu/runjobs/).
Furthermore, we assume general knowledge about the [**Julia Language**](../../apps/julia.md) environment.
For further reading about parallel and high-performance computing with Julia, we recommend the [Julia for high-performance scientific computing](https://enccs.github.io/Julia-for-HPC) from ENCCS and the [A brief tour of Julia for high-performance computing](https://forem.julialang.org/wikfeldt/a-brief-tour-of-julia-for-high-performance-computing-5deb) written by Kjartan Thor Wikfeldt.
CSC training also has a [quick introduction and tutorial](https://github.com/csc-training/julia-introduction) to Julia.


### Project structure
We use the following Julia project structure in the example jobs.
We also assume that it is our working directory when running the commands.

```
.
├── Manifest.toml  # Automatically created a list of all dependencies
├── Project.toml   # Julia environment and dependencies
├── batch.sh       # Slurm batch script
└── script.jl      # Julia script
```

The example jobs demonstrate project files for different single and multi-node jobs.


### Slurm
TODO: Julia, MPI and `srun` in batch jobs, local preferences and Julia's mpiexec function, environment variables, remove srun from MPI examples, use Julia to create new processes


### Environment variables
The `julia` module sets the [`JULIA_CPU_THREADS`](https://docs.julialang.org/en/v1/manual/environment-variables/#JULIA_CPU_THREADS) and [`JULIA_NUM_THREADS`](https://docs.julialang.org/en/v1/manual/environment-variables/#JULIA_NUM_THREADS) environment variables to the number of reserved CPU cores when loaded in a Slurm job; otherwise, the module sets them to one.
We use the value of the `--cpus-per-task` option, which populates the `SLURM_CPUS_PER_TASK` environment variable, to detect the number of CPU cores.
The effect is the same as setting the following environment variables in a shell.

```bash
# Sets the value to SLURM_CPUS_PER_TASK if defined, otherwise 1
export JULIA_CPU_THREADS=${SLURM_CPUS_PER_TASK:-1}
export JULIA_NUM_THREADS=$JULIA_CPU_THREADS
```

We can start a Julia process with a different number of threads than `JULIA_NUM_THREADS` using the `--threads` option as follows:

```bash
julia --threads 2  # using two threads regardless of JULIA_NUM_THREADS value
```

We can interact with environment variables in the Julia session using the [`ENV`](https://docs.julialang.org/en/v1/base/base/#Base.ENV) constant.


### Multi-threading
We can use the `Base.Threads` library for multi-threading in Julia.
It is automatically loaded and available as `Threads` in the Julia session.
The Julia manual contains more detailed information about [multi-threading](https://docs.julialang.org/en/v1/manual/multi-threading/).

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

Alternatively, we can use the MKL backend via [MKL.jl](https://github.com/JuliaLinearAlgebra/MKL.jl) as a linear algebra backend.
MKL is often faster than OpenBLAS when using multiple threads on Intel CPUs, such as those on Puhti.
We can set the MKL thread count as follows.

```bash
export MKL_NUM_THREADS=$JULIA_CPU_THREADS
```

If we use MKL, we should load it before other linear algebra libraries.

```julia
using MKL
using LinearAlgebra
# your code ...
```

There are [caveats](https://discourse.julialang.org/t/matrix-multiplication-is-slower-when-multithreading-in-julia/56227/12?u=carstenbauer) for using different numbers than one or all cores of BLAS threads on OpenBLAS and MKL.


### Distributed
We can use `Distributed`, a standard library for multiple processes in Julia.
The Julia manual has a section about  [distributed computing](https://docs.julialang.org/en/v1/manual/distributed-computing/) explaining Julia's distributed programming.
Later we also discuss how to use MPI.
Distributed has two built-in cluster managers, `LocalManager` for processes that communicate using Localhost and `SSHManager` for processes that communicate via SSH.
We can add processes to the same node as the Julia job is started using `LocalManager` and the `SSHManager` to add processes to other nodes.

```julia
using Distributed

# Implicitly adds 2 processes using LocalManager
addprocs(2)

# Implicitly adds 2 processes to node1 and 3 processes to node2 using SSHManager
addprocs([(2, "node1"), (3, "node2")])
```

When adding processes, we can also pass various key values, such as environment variables and options for Julia.
We demonstrate them in the examples.

We can find the node name in the Julia process using the following:

```julia
local_node = first(split(gethostname(), '.'; limit=2))
```

We can read the names of the nodes that slurm allocated for a job using `SLURM_JOB_NODELIST` environment variable and expanding it using `scontrol show hostnames <nodelist>` command as follows:

```julia
nodes = readlines(`scontrol show hostnames $(ENV["SLURM_JOB_NODELIST"])`)
```

We can use these nodenames when adding processes using `SSHManager`.

!!! info "LUMI does not have SSH between compute nodes."
    Currently, LUMI does not have SSH between compute notes.
    Hence we cannot add processes to other nodes via SSHManager.


### MPI.jl
We can use MPI for multi-node parallel computing in Julia on Puhti, Mahti and LUMI using the `MPI.jl` package.
For programming, we recommend reading the [MPI.jl documentation](https://juliaparallel.org/MPI.jl/stable/).
We have installed MPI.jl, which uses the local MPI installation, in the shared environment.
We recommend you use the version in the shared environment because we have tested it.
You can find the version by activating the shared environment and running `Pkg.status` as follows:

```bash
julia --project="$CSC_JULIA_ENVIRONMENT_DIR" -e 'using Pkg; Pkg.status("MPI")'
```

Furthermore, the `julia` module automatically loads the correct MPI module.


### CUDA.jl
The GPU nodes on Puhti and Mahti contain GPUs for NVidia.
We can use them with `CUDA.jl` package in Julia.
For programming, we recommend reading the [CUDA.jl documentation](https://cuda.juliagpu.org/stable/).
We have installed CUDA.jl, which uses the local CUDA installation, in the shared environment.
We recommend you use the version in the shared environment because we have tested it.
You can find the version by activating the shared environment and running `Pkg.status` as follows:

```bash
julia --project="$CSC_JULIA_ENVIRONMENT_DIR" -e 'using Pkg; Pkg.status("CUDA")'
```

Furthermore, the `julia-cuda` module automatically loads the correct CUDA module.


### AMDGPU.jl
The GPU nodes on LUMI contain GPUs for AMD.
We can use them with `AMDGPU.jl` package in Julia.
For programming, we recommend reading the [AMDGPU.jl documentation](https://amdgpu.juliagpu.org/stable/).
We have installed AMDGPU.jl, which uses the local ROCm installation, in the shared environment.
We recommend you use the version in the shared environment because we have tested it.
You can find the version by activating the shared environment and running `Pkg.status` as follows:

```bash
julia --project="$CSC_JULIA_ENVIRONMENT_DIR" -e 'using Pkg; Pkg.status("AMDGPU")'
```

Furthermore, the `julia-amdgpu` module automatically loads the correct AMD programming environment and ROCm module.


## Single node jobs
### Serial
An example of a `script.jl` Julia code.

```julia
println("Hello world!")
```

=== "Puhti"
    An example of a `Project.toml` project file.

    ```toml
    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Puhti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `Project.toml` project file.

    ```toml
    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Mahti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=interactive
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1875

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```


=== "LUMI"
    An example of a `Project.toml` project file.

    ```toml
    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` LUMI batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```


### Multiple threads
An example of a `script.jl` Julia code.

```julia
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

=== "Puhti"
    An example of a `Project.toml` project file.

    ```toml
    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Puhti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `Project.toml` project file.

    ```toml
    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Mahti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --mem-per-cpu=0

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "LUMI"
    An example of a `Project.toml` project file.

    ```toml
    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` LUMI batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```


### Multiple processes
An example of a `script.jl` Julia code.

```julia
using Distributed

# We set one worker process per core.
proc_num = Sys.CPU_THREADS

# Environment variables that we pass to the worker processes.
# We set the thread count to one since each process uses one core.
proc_env = [
    "JULIA_NUM_THREADS"=>"1",
    "JULIA_CPU_THREADS"=>"1",
    "OPENBLAS_NUM_THREADS"=>"1",
    "MKL_NUM_THREADS"=>"1",
]

# We add worker processes to the local node using LocalManager.
addprocs(proc_num;
         env=proc_env,
         exeflags="--project=.")

# We use the `@everywhere` macro to include the task function in the worker processes.
# We must call `@everywhere` after adding worker processes; otherwise the code won't be included in the new processes.
@everywhere function task()
    (
        id=myid(),
        hostname=gethostname(),
        pid=getpid(),
        nthreads=Threads.nthreads(),
        cputhreads=Sys.CPU_THREADS
    )
end

# We run the task function in each worker process.
futures = [@spawnat id task() for id in workers()]

# Then, we fetch the output from the processes.
outputs = fetch.(futures)

# Remove processes after we are done.
rmprocs.(workers())

# Print the outputs of master and worker processes.
println(task())
println.(outputs)
```

=== "Puhti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Puhti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Mahti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --mem-per-cpu=0

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "LUMI"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` LUMI batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```


### Single GPU
=== "CUDA.jl"
    An example of a `script.jl` Julia code.

    ```julia
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = $A_d * $A_d
    ```

=== "AMDGPU.jl"
    An example of a `script.jl` Julia code.

    ```julia
    using AMDGPU

    A = rand(2^9, 2^9)
    A_d = ROCArray(A)
    B_d = $A_d * $A_d
    ```

---

=== "Puhti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"

    [compat]
    julia = "1.9"
    CUDA = "=4.0.1"
    ```

    An example of a `batch.sh` Puhti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=10
    #SBATCH --gres=gpu:v100:1
    #SBATCH --mem-per-cpu=8000

    module load julia-cuda/1.8
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"

    [compat]
    julia = "1.9"
    CUDA = "=4.0.1"
    ```

    An example of a `batch.sh` Mahti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=32
    #SBATCH --gres=gpu:a100:1
    #

    module load julia-cuda/1.8
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "LUMI"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    AMDGPU = "21141c5a-9bdb-4563-92ae-f87d6854732e"

    [compat]
    julia = "1.9"
    AMDGPU = "=0.4.13"
    ```

    An example of a `batch.sh` LUMI batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=16
    #SBATCH --gpus-per-node=1
    #SBATCH --mem-per-cpu=1750

    module load julia-amdgpu/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```


## Multi-node jobs
### MPI
An example of a `script.jl` Julia code.

```julia
using MPI

MPI.Init()
comm = MPI.COMM_WORLD
rank = MPI.Comm_rank(comm)
size = MPI.Comm_size(comm)
println("Hello from rank $(rank) out of $(size) from host $(gethostname()) and process $(getpid()).")
MPI.Barrier(comm)
```

=== "Puhti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"

    [compat]
    julia = "1.9"
    MPI = "=0.20.8"
    ```

    An example of a `batch.sh` Puhti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=2
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    srun julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"

    [compat]
    julia = "1.9"
    MPI = "=0.20.8"
    ```

    An example of a `batch.sh` Mahti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    srun julia --project=. script.jl
    ```

=== "LUMI"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"

    [compat]
    julia = "1.9"
    MPI = "=0.20.8"
    ```

    An example of a `batch.sh` LUMI batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    srun julia --project=. script.jl
    ```


### Multiple processes
An example of a `script.jl` Julia code.

```julia
using Distributed

# We set one worker process per core.
proc_num = Sys.CPU_THREADS

# Environment variables that we pass to the worker processes.
# We set the thread count to one since each process uses one core.
proc_env = [
    "JULIA_NUM_THREADS"=>"1",
    "JULIA_CPU_THREADS"=>"1",
    "OPENBLAS_NUM_THREADS"=>"1",
    "MKL_NUM_THREADS"=>"1",
]

# Read the list of nodenames allocated by Slurm.
nodes = readlines(`scontrol show hostnames $(ENV["SLURM_JOB_NODELIST"])`)

# Retrieve the node name of the master process.
local_node = first(split(gethostname(), '.'; limit=2))

# We add worker processes to the local node using LocalManager.
addprocs(proc_num;
         env=proc_env,
         exeflags="--project=.")

# We add worker processes to the other nodes with SSHManager.
addprocs([(node, proc_num) for node in nodes if node != local_node];
         tunnel=true,
         env=proc_env,
         exeflags="--project=.")

# We use the `@everywhere` macro to include the task function in the worker processes.
# We must call `@everywhere` after adding worker processes; otherwise the code won't be included in the new processes.
@everywhere function task()
    (
        id=myid(),
        hostname=gethostname(),
        pid=getpid(),
        nthreads=Threads.nthreads(),
        cputhreads=Sys.CPU_THREADS
    )
end

# We run the task function in each worker process.
futures = [@spawnat id task() for id in workers()]

# Then, we fetch the output from the processes.
outputs = fetch.(futures)

# Remove processes after we are done.
rmprocs.(workers())

# Print the outputs of master and worker processes.
println(task())
println.(outputs)
```

=== "Puhti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Puhti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Mahti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --mem-per-cpu=0

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```


### Multiple processes and threads
An example of a `script.jl` Julia code.

```julia
using Distributed

# We set one worker process per node.
proc_num = 1

# Environment variables that we pass to the worker processes.
# We set the thread count to CPU_THREADS such that each worker uses all reserved cores in the node.
proc_env = [
    "JULIA_NUM_THREADS"=>"$(Sys.CPU_THREADS)",
    "JULIA_CPU_THREADS"=>"$(Sys.CPU_THREADS)",
    "OPENBLAS_NUM_THREADS"=>"$(Sys.CPU_THREADS)",
    "MKL_NUM_THREADS"=>"$(Sys.CPU_THREADS)",
]

# Read the list of nodenames allocated by Slurm.
nodes = readlines(`scontrol show hostnames $(ENV["SLURM_JOB_NODELIST"])`)

# Retrieve the node name of the master process.
local_node = first(split(gethostname(), '.'; limit=2))

# We add worker processes to the local node using LocalManager.
addprocs(proc_num;
         env=proc_env,
         exeflags="--project=.",
         enable_threaded_blas=true)

# We add worker processes to the other nodes with SSHManager.
addprocs([(node, proc_num) for node in nodes if node != local_node];
         tunnel=true,
         env=proc_env,
         exeflags="--project=.",
         enable_threaded_blas=true)

# We use the `@everywhere` macro to include the task function in the worker processes.
# We must call `@everywhere` after adding worker processes; otherwise the code won't be included in the new processes.

@everywhere function task_threads()
    ids = zeros(Int, Threads.nthreads())
    Threads.@threads for i in eachindex(ids)
        ids[i] = Threads.threadid()
    end
    return ids
end

@everywhere function task_proc()
    (
        id=myid(),
        hostname=gethostname(),
        pid=getpid(),
        nthreads=Threads.nthreads(),
        cputhreads=Sys.CPU_THREADS,
        thread_ids=task_threads()
    )
end

# We run the task function in each worker process.
futures = [@spawnat id task_proc() for id in workers()]

# Then, we fetch the output from the processes.
outputs = fetch.(futures)

# Remove processes after we are done.
rmprocs.(workers())

# Print the outputs of master and worker processes.
println(task_proc())
println.(outputs)
```

=== "Puhti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Puhti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

    [compat]
    julia = "1.9"
    ```

    An example of a `batch.sh` Mahti batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --mem-per-cpu=0

    module load julia/1.9
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
    julia --project=. script.jl
    ```
