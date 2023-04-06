# Running Julia jobs
Instructions for running different Julia jobs on Puhti and Mahti.


## Prerequisites
These intructions are adapted from the general intructions of [**running jobs**](../../computing/running/getting-started.md) on Puhti and Mahti.
Furthermore, we assume general knowledge about the [**Julia environment**](../../apps/julia.md).
We use the following Julia project structure in the example jobs.
We also assume that it is our working directory when running the commands.

```
.
├── Manifest.toml  # Automatically created list of all dependencies
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


## Serial job
An example of a single-core Julia batch job on Puhti
An example of `puhti.sh` batch script contains the following:

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=test
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1000

module load julia
srun julia --project=. script.jl
```

The `script.jl` prints "Hello world!" text.

```julia
println("Hello world!")
```


## Job with multiple threads
An example of a multi-core Julia batch job on Puhti.

We can use the `Base.Threads` library for multithreading in Julia.
We don't need to include libraries in `Base` to `Project.toml`.
We can start Julia with multiple threads by setting the `JULIA_NUM_THREADS` environment variable or use the `--threads` option.
Julia's thread count should equal to the value of `--cpus-per-task` which sets the amount of CPU cores on Slurm.
We can access the value using the `SLURM_CPUS_PER_TASK` enviroment variable.

`puhti.sh`

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=test
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1000

export JULIA_NUM_THREADS="$SLURM_CPUS_PER_TASK"
module load julia
srun julia --project=. script.jl
```

`script.jl`

```julia
using Base.Threads

println(nthreads())
...
```


## Single node job with multiple processes
We can use `Distributed` which is a standard library for using multiple processes in Julia.
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
#SBATCH --partition=test
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=3
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1000

module load julia
# We don't use srun here!
julia --project=. script.jl
```

`script.jl`

```julia
using Distributed

nprocs = parse(Int, ENV["SLURM_NTASKS_PER_NODE"]) - 1
addprocs(nprocs)

@everywhere function task()
    return (myid(), gethostname(), getpid())
end

futures = [@spawnat i task() for i in workers()]
outputs = fetch.(futures)

println(task())
println.(outputs)

rmprocs.(workers())
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
#SBATCH --partition=test
#SBATCH --time=00:15:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1000

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
println("Hello from process $(rank) out of $(size)")
MPI.Barrier(comm)
```


## Job with GPU

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
#SBATCH --partition=gputest
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4000
#SBATCH --gres=gpu:v100:1

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


## Hybrid Jobs
What we can combine?

