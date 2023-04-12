# Running Julia jobs
Instructions for running different Julia jobs on Puhti and Mahti.


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
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

Now we can explore project files for different types of jobs.

Julia has some important [environment variables for parallelization](https://docs.julialang.org/en/v1/manual/environment-variables/#Parallelization).
Because we use Slurm to reserve resources on Puhti and Mahti, we need to set the `JULIA_CPU_THREADS` and `JULIA_NUM_THREADS` environment variables to the number of reserved CPU cores.
The Julia module sets these environment variables the value of `--cpus-per-task` option using the `SLURM_CPUS_PER_TASK` environment variable.
If that option is not defined, for example, on login nodes, it sets the thread count to one.


## Serial job
`Project.toml`

```toml
# empty
```

An example of `puhti.sh` batch script contains the following:

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

module load julia
srun julia --project=. script.jl
```

`script.jl`

```julia
println("Hello world!")
```


## Single node job with multiple threads
We can use the `Base.Threads` library for multithreading in Julia.

We don't need to include libraries in `Base` to `Project.toml`.

```toml
# empty
```

`puhti.sh`

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

module load julia
srun julia --project=. script.jl
```

`mahti.sh`

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128

module load julia
srun julia --project=. script.jl
```

`script.jl`

```julia
using Base.Threads

# Number of threads
n = nthreads()

# Lets fill the id of each thread to the ids array.
ids = zeros(Int, 10*n)
@threads for i in eachindex(ids)
    ids[i] = threadid()
end

# Print the outputs.
println(n)
println(ids)
```

!!! note
    `LinearAlgebra` backend such as OpenBlas and MKL have their own threading support which controlled by `BLAS.set_num_threads` not `Base.Threads`.


## Single node job with multiple processes
We can use `Distributed`, a standard library for multiple processes in Julia.
When we add `Distributed`, the `Project.toml` file will look as follows.

```toml
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

`puhti.sh`

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

module load julia
srun julia --project=. script.jl
```

`mahti.sh`

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128

module load julia
srun julia --project=. script.jl
```

`script.jl`

```julia
using Distributed

# Add new workers before using @everywhere macros, otherwise the code won't be included to the new processes.
addprocs(Sys.CPU_THREADS)

# We must use @everywhere macro to include the task function to the worker processes.
@everywhere function task()
    return (myid(), gethostname(), getpid())
end

# We run the task function in each worker process.
futures = [@spawnat id task() for id in workers()]

# Then, we fetch the output from the processes.
outputs = fetch.(futures)

# Remove processes after we are done.
rmprocs.(workers())

# Print the outputs.
println(task())
println.(outputs)
```


## Multi-node job with MPI

`Project.toml`

```toml
[deps]
MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"

[compat]
MPI = "=0.20.8"
```

`puhti.sh`

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

module load julia
srun julia --project=. script.jl
```

`mahti.sh`

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128
#SBATCH --cpus-per-task=1

module load julia
srun julia --project=. script.jl
```

`script.jl`

```julia
using MPI

MPI.Init()
comm = MPI.COMM_WORLD
rank = MPI.Comm_rank(comm)
size = MPI.Comm_size(comm)
println("Hello from rank $(rank) out of $(size) from host $(gethostname()) and process $(getpid()).")
MPI.Barrier(comm)
```


## GPU job

`Project.toml`

```toml
[deps]
CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"

[compat]
CUDA = "=4.0.1"
```

`puhti.sh`

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

module load julia
srun julia --project=. script.jl
```

`mahti.sh`

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

module load julia
srun julia --project=. script.jl
```

`script.jl`

```julia
using CUDA

@show CUDA.versioninfo()
n = 2^20
x = CUDA.fill(1.0f0, n)
y = CUDA.fill(2.0f0, n)
y .+= x
println(all(Array(y) .== 3.0f0))
```

