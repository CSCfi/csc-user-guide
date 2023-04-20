# Running Julia jobs
Instructions for running serial, parallel, and GPU jobs with Julia on Puhti and Mahti.

[TOC]


## Prerequisites
These instructions are adapted from the general instructions of [**running jobs**](../../computing/running/getting-started.md) on Puhti and Mahti.
Furthermore, we assume general knowledge about the [**Julia environment**](../../apps/julia.md).
We use the following Julia project structure in the example jobs.
We also assume that it is our working directory when running the commands.

```
.
├── Manifest.toml  # Automatically created a list of all dependencies
├── Project.toml   # Julia environment and dependencies
├── puhti.sh       # Puhti batch script
├── mahti.sh       # Mahti batch script
└── script.jl      # Julia script
```

We have to instantiate the project before running batch scripts.

```bash
module load julia/1.8
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

Julia has some important [environment variables for parallelization](https://docs.julialang.org/en/v1/manual/environment-variables/#Parallelization).
Because we use Slurm to reserve resources on Puhti and Mahti, we need to set the `JULIA_CPU_THREADS` and `JULIA_NUM_THREADS` environment variables to the number of reserved CPU cores.
The Julia module sets these environment variables the value of `--cpus-per-task` option using the `SLURM_CPUS_PER_TASK` environment variable.
If that option is not defined, for example, on login nodes, it sets the thread count to one.
The effect is the same as sourcing the following exports in shell.

```bash
export JULIA_CPU_THREADS=${SLURM_CPUS_PER_TASK:-1}
export JULIA_NUM_THREADS=$JULIA_CPU_THREADS
```

If you need to start a julia process with different number of threads than `JULIA_NUM_THREADS` you can use the `--threads` option as follows.

```bash
julia --threads 2  # using two threads regardless of JULIA_NUM_THREADS value
```

Now we can explore project files for different types of jobs.


## Serial job
An example of a `Project.toml` project file.

```toml
[compat]
julia = "1.8"
```

An example of a `script.jl` Julia code.

```julia
println("Hello world!")
```

An example of a `puhti.sh` Puhti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1000

module load julia/1.8
srun julia --project=. script.jl
```

Mahti is intended for parallel computing; therefore, we do not include a Batch script for Mahti.


## Single node job with multiple threads
We can use the `Base.Threads` library for multithreading in Julia.
Libraries from `Base` are automatically included in the runtime.

An example of a `Project.toml` project file.

```toml
[compat]
julia = "1.8"
```

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

An example of a `puhti.sh` Puhti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=3
#SBATCH --mem-per-cpu=1000

module load julia/1.8
srun julia --project=. script.jl
```

An example of a `mahti.sh` Mahti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128

module load julia/1.8
srun julia --project=. script.jl
```


## Linear algebra backends and threading
The default `LinearAlgebra` backend on Julia is OpenBLAS.
If we want to, we can use MKL instead of OpenBLAS.
MKL is often faster than OpenBLAS, especially on Puhti, when using multiple threads.
We should load the `MKL` library before other linear algebra libraries.

```julia
using MKL
```

The Julia module sets the number of threads for OpenBLAS and MKL backends to the number of CPU threads.

```bash
export OPENBLAS_NUM_THREADS=$JULIA_CPU_THREADS
export MKL_NUM_THREADS=$JULIA_CPU_THREADS
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

There are [caveats](https://discourse.julialang.org/t/matrix-multiplication-is-slower-when-multithreading-in-julia/56227/12?u=carstenbauer) for using different numbers than one or all cores of BLAS threads on OpenBLAS and MKL.


## Single node job with multiple processes
We can use `Distributed`, a standard library for multiple processes in Julia.

An example of a `Project.toml` project file.

```toml
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

[compat]
julia = "1.8"
```

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

# We add worker processes.
addprocs(proc_num;
         env=proc_env,
         exeflags="--project=.")

# We use the `@everywhere` macro to include the task function in the worker processes.
# We must call `@everwhere` after adding worker processes; otherwise the code won't be included in the new processes.
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

An example of a `puhti.sh` Puhti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=3
#SBATCH --mem-per-cpu=1000

module load julia/1.8
srun julia --project=. script.jl
```

An example of a `mahti.sh` Mahti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128

module load julia/1.8
srun julia --project=. script.jl
```


## Multi-node job with multiple processes
The multi-node job with multiple processes is similar to the single-node example except that we use multiple nodes and we add processes to the other nodes using `SSHManager` instead of `LocalManager`.
We also do not use `srun` in the batch script, otherwise Slurm will start the Julia script on all nodes.

An example of a `Project.toml` project file.

```toml
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

[compat]
julia = "1.8"
```

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
# We must call `@everwhere` after adding worker processes; otherwise the code won't be included in the new processes.
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

An example of a `puhti.sh` Puhti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=3
#SBATCH --mem-per-cpu=1000

module load julia/1.8
julia --project=. script.jl
```

An example of a `mahti.sh` Mahti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128

module load julia/1.8
julia --project=. script.jl
```


## Multi-node job with multiple processes and threads
An example of a `Project.toml` project file.

```toml
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"

[compat]
julia = "1.8"
```

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
# We must call `@everwhere` after adding worker processes; otherwise the code won't be included in the new processes.

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

An example of a `puhti.sh` Puhti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=3
#SBATCH --mem-per-cpu=1000

module load julia/1.8
julia --project=. script.jl
```

An example of a `mahti.sh` Mahti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128

module load julia/1.8
julia --project=. script.jl
```


## Multi-node job with MPI
We can use the `MPI.jl` package to use MPI for multi-node parallelism.
In Puhti and Mahti it uses OpenMPI.
We have installed a specific version of `MPI.jl` to the shared environment.
We recommend that you use that version because it has been tested to work.
You can find the version by activating the shared environment and running `Pkg.status` as follows:

```bash
julia --project="$JULIA_CSC_ENVIRONMENT" -e 'using Pkg; Pkg.status("MPI")'
```

An example of a `Project.toml` project file.

```toml
[deps]
MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"

[compat]
julia = "1.8"
MPI = "=0.20.8"
```

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

An example of a `puhti.sh` Puhti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1000

module load julia/1.8
srun julia --project=. script.jl
```

An example of a `mahti.sh` Mahti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128
#SBATCH --cpus-per-task=1

module load julia/1.8
srun julia --project=. script.jl
```


## Single node job with one GPU
Puhti and Mahti contain NVidia GPUs.
We can use them via the `CUDA.jl` package.
We have installed a specific version of `CUDA.jl` to the shared environment.
We recommend that you use that version because it has been tested to work.
You can find the version by activating the shared environment and running `Pkg.status` as follows:

```bash
julia --project="$JULIA_CSC_ENVIRONMENT" -e 'using Pkg; Pkg.status("CUDA")'
```

An example of a `Project.toml` project file.

```toml
[deps]
CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"

[compat]
julia = "1.8"
CUDA = "=4.0.1"
```

An example of a `script.jl` Julia code.

```julia
using CUDA

@show CUDA.versioninfo()
n = 2^20
x = CUDA.fill(1.0f0, n)
y = CUDA.fill(2.0f0, n)
y .+= x
println(all(Array(y) .== 3.0f0))
```

An example of a `puhti.sh` Puhti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpu
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=4000
#SBATCH --gres=gpu:v100:1

module load julia/1.8
srun julia --project=. script.jl
```

An example of a `mahti.sh` Mahti batch script.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpusmall
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:a100:1

module load julia/1.8
srun julia --project=. script.jl
```

