# Running Julia batch jobs on CSC clusters
This tutorial contains examples for running various Julia batch jobs on Puhti, Mahti and LUMI clusters.

[TOC]


## Examples
These examples demonstrate the usage of the [Julia environment](../../apps/julia.md) for various batch jobs.
They are adapted from the general instructions of running jobs on [Puhti and Mahti](../../computing/running/getting-started.md) and on [LUMI](https://docs.lumi-supercomputer.eu/runjobs/).
Note that we do not use `srun` to start processes in the batch script.
Instead we use Julia for process management or call `srun` inside the Julia code.


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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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
    julia --project=. -e 'using Pkg; Pkg.instantiate()'
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


<!-- TODO: trim and move to application section
### Distributed
Distributed has two built-in cluster managers, `LocalManager` for processes that communicate using Localhost and `SSHManager` for processes that communicate via SSH.
We can add processes to the same node as the Julia job is started using `LocalManager` and the `SSHManager` to add processes to other nodes.
TODO: ClusterManagers to add processes via Slurm

```julia
using Distributed

# Adds 2 processes using LocalManager
addprocs(2)

# Adds 2 processes to node1 and 3 processes to node2 using SSHManager
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
-->


<!--
### Using environments
Julia manages dependencies of projects using environments.
An environment consists of two files, `Project.toml` and `Manifest.toml`, which specify dependencies for the environment.
We define project metadata, dependencies, and compatibility constraints in the `Project.toml` file.
Adding or removing packages using the package manager manipulates the `Project.toml` file in the active environment.
Furthermore, the package manager maintains a full list of dependencies in the `Manifest.toml` file.
It creates both of these files if they don't exist.
Let's consider a Julia project structured as follows.

```text
project/
├── script.jl
├── Project.toml
└── Manifest.toml
```

We can activate an environment using the `--project` option when starting Julia or use the `Pkg.activate` function in the existing Julia session.
For example, we can open the Julia REPL with the project's environment active as follows:

```bash
julia --project=.
```

We can call the `Base.active_project()` function to retrieve a path to the active project, that is, `Project.toml` file.

Activating an environment does not automatically install the packages defined by `Manifest.toml` or `Project.toml`.
For that, we need to instantiate the project as follows:

```julia
import Pkg
Pkg.activate(".")
Pkg.instantiate()
```

Alternatively, we can use the following one-liner:

```bash
julia --project=. -e 'import Pkg; Pkg.instantiate()'
```

Now, we can run the script using the project's environment as follows:

```bash
julia --project=. script.jl
```

Julia will activate the default environment if we don't specify an environment.
Preferably, we should use a unique environment for Julia projects instead of the default environment.
That way, we can manage the dependencies of different Julia projects separately.


### Adding packages to an environment
On the Julia REPL, we can use the package manager by importing it.

```julia
import Pkg
```

We can activate a Julia environment on the current working directory as follows.

```julia
Pkg.activate(".")
```

We can add packages to the active environment using the `Pkg.add` function.
For example, we can add the `ArgParse` package as follows.

```julia
Pkg.add("ArgParse")
```
-->


<!-- TODO: Move this section to end of julia tutorial

### Creating a package with a command line interface
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

We can use the `ArgParse` package to create a command line interface `src/cli.jl` for the package.
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
-->
