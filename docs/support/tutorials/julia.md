# Running Julia jobs
Instructions for running different Julia jobs on Puhti and Mahti.


## Prerequisites
These intructions are adapted from the general intructions of [**running jobs**](../../computing/running/getting-started.md) on Puhti and Mahti.
Furthermore, we assume general knowledge about the [**Julia Language**](../../apps/julia.md) environment.

The following Julia job use a simple project structure as follows:

```
.
├── Manifest.toml
├── Project.toml
├── batch.sh
└── script.jl
```

Furthermore, we have to instantiate the project before running the batch script.

```bash
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

Now we can explore what project files may contain.


## Serial job
A sample of a single-core Julia batch job on Puhti

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=test
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=1000

module load julia
srun julia --project=. script.jl
```

The above batch job runs the Julia script `script.jl` using one CPU core.


## Single node job with multiple threads
A sample of a multi-core Julia batch job on Puhti.
We can start Julia with multiple threads by setting the `JULIA_NUM_THREADS` environment variable.
Alternatively, we can use the `--threads` option.

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

# set the number of threads based on --cpus-per-task
export JULIA_NUM_THREADS="$SLURM_CPUS_PER_TASK"

module load julia
srun julia script.jl
```

The above batch job runs the Julia script `script.jl` using two CPU cores.

```julia
using Base.Threads

...
```


## Single node job with multiple processes

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
julia --project=. script.jl
```

```julia
using Distributed

nprocs = parse(Int, ENV["SLURM_NTASKS_PER_NODE"]) - 1
addprocs(nprocs)

@everywhere task() = (myid(), gethostname(), getpid())
futures = [@spawnat i task() for i in workers()]
outputs = fetch.(futures)

println(task())
println.(outputs)

# The Slurm resource allocation is released when all the workers have exited
rmprocs.(workers())
```

```toml
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```


## Multi-node job with MPI

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

```julia
using MPI

MPI.Init()
comm = MPI.COMM_WORLD
rank = MPI.Comm_rank(comm)
size = MPI.Comm_size(comm)
println("Hello from process $(rank) out of $(size)")
MPI.Barrier(comm)
```

```toml
[deps]
MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"

[compat]
MPI = "=0.20.8"
```


## Single node job with GPU

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

```julia
using CUDA

@show CUDA.versioninfo()
n = 2^20
x = CUDA.fill(1.0f0, n)
y = CUDA.fill(2.0f0, n)
y .+= x
println(all(Array(y) .== 3.0f0))
```

```toml
[deps]
CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"

[compat]
CUDA = "=4.0.1"
```

