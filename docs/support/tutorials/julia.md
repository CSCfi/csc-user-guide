# Running Julia batch jobs on CSC clusters
This tutorial contains examples for running various Julia batch jobs on Puhti, Mahti and LUMI clusters.

[TOC]


## Examples
These examples demonstrate the usage of the [Julia environment](../../apps/julia.md) for various batch jobs.
They are adapted from the general instructions of running jobs on [Puhti and Mahti](../../computing/running/getting-started.md) and on [LUMI](https://docs.lumi-supercomputer.eu/runjobs/).
Note that we do not use `srun` to start processes in the batch script.
Instead we use Julia for process management or call `srun` inside the Julia code.

Before running the examples, we need to instantiate the Julia project on the login node.
That is, run the following command in the directory with your Julia environment where `Project.toml` file is located.


=== "Puhti"
```bash
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

An example of a `script.jl` code.

```julia
println("Hello world!")
```

=== "Puhti"
    An example of a `batch.sh` batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `batch.sh` batch script.

    ```bash
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
    An example of a `batch.sh` batch script.

    ```bash
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

An example of a `script.jl` code.

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
    An example of a `batch.sh` batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `batch.sh` batch script.

    ```bash
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
    An example of a `batch.sh` batch script.

    ```bash
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

An example of a `Project.toml` project file.

```toml
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

An example of a `script.jl` code.

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

=== "Puhti"
    An example of a `batch.sh` batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `batch.sh` batch script.

    ```bash
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
    An example of a `batch.sh` batch script.

    ```bash
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

An example of a `Project.toml` project file.

```toml
[deps]
ClusterManagers = "34f1f09b-3a8b-5176-ab39-66d58a4d544e"
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

An example of a `script.jl` code.

```julia
using Distributed
using ClusterManagers

# We set one worker process per core.
proc_num = parse(Int, ENV["SLURM_NTASKS"])

# Environment variables that we pass to the worker processes.
# We set the thread count to one since each process uses one core.
n = Threads.nthreads()
proc_env = [
    "JULIA_NUM_THREADS"=>"$n",
    "JULIA_CPU_THREADS"=>"$n",
    "OPENBLAS_NUM_THREADS"=>"$n",
]

# We add worker processes to the local node using SlurmManager
addprocs(SlurmManager(proc_num); env=proc_env, exeflags="--project=.")

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

=== "Puhti"
    An example of a `batch.sh` batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=2
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `batch.sh` batch script.

    ```bash
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
    An example of a `batch.sh` batch script.

    ```bash
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
The command is `srun` in Puhti, Mahti, and LUMI.
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

An example of a `Project.toml` project file.

```toml
[deps]
MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"
```

An example of a `script.jl` code.

```julia
using MPI
mpiexec(mpirun -> run(`$mpirun julia --project=. prog.jl`))
```

An example of a `prog.jl` Julia MPI code.

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
    An example of a `batch.sh` batch script.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=2
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia
    module load julia-mpi
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `batch.sh` batch script.

    ```bash
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
    An example of a `batch.sh` batch script.

    ```bash
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

=== "Puhti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"
    ```

    An example of a `script.jl` code.

    ```julia
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = A_d * A_d
    ```

    An example of a `batch.sh` batch script.

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

    module load julia
    module load julia-cuda
    julia --project=. script.jl
    ```

=== "Mahti"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"
    ```

    An example of a `script.jl` code.

    ```julia
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = A_d * A_d
    ```

    An example of a `batch.sh` batch script.

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

    module load julia
    module load julia-cuda
    julia --project=. script.jl
    ```

=== "LUMI"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    AMDGPU = "21141c5a-9bdb-4563-92ae-f87d6854732e"
    ```

    An example of a `script.jl` code.

    ```julia
    using AMDGPU

    A = rand(2^9, 2^9)
    A_d = ROCArray(A)
    B_d = A_d * A_d
    ```

    An example of a `batch.sh` batch script.

    ```bash
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


### Multi GPU with MPI
We use the following directory structure and assume it is our working directory.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
├── prog.jl       # Julia GPU-aware MPI program
└── script.jl     # Julia script
```

An example of a `script.jl` code.

```julia
using MPI
mpiexec(mpirun -> run(`$mpirun julia --project=. prog.jl`))
```

=== "LUMI"
    An example of a `Project.toml` project file.

    ```toml
    [deps]
    AMDGPU = "21141c5a-9bdb-4563-92ae-f87d6854732e"
    MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"
    ```

    An example of a `prog.jl` code. ([source](https://gist.github.com/luraess/a47931d7fb668bd4348a2c730d5489f4))

    ```julia
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
    fill!(send_mesg, Float64(rank))
    AMDGPU.synchronize()
    rank==0 && println("start sending...")
    MPI.Sendrecv!(send_mesg, dst, 0, recv_mesg, src, 0, comm)
    println("recv_mesg on proc $rank: $recv_mesg")
    rank==0 && println("done.")
    ```

    An example of a `batch.sh` batch script.

    ```bash
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
