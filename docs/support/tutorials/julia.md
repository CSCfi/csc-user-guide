# Julia
Tutorial for running Julia code as batch jobs on Puhti and Mahti.


## Batch jobs
You can find more information about batch jobs on Puhti from the [user guide](../computing/running/getting-started.md).


## Interactive job on Puhti
We can request an interactive node directly on Puhti as follows.

```bash
srun --ntasks=1 --time=00:10:00 --mem=4G --pty --account=<project> --partition=small julia
```


## Serial batch job
A sample of a single-core Julia batch job on Puhti

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=test
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=1000

module load julia
srun julia my_script.jl
```

The above batch job runs the Julia script `my_script.jl` using one CPU core.


## Multithreading batch job
A sample of a multi-core Julia batch job on Puhti.
We can start Julia with multiple threads by setting the `JULIA_NUM_THREADS` environment variable.
Alternatively, we can use the `--threads` option.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=test
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1000

# set the number of threads based on --cpus-per-task
export JULIA_NUM_THREADS="$SLURM_CPUS_PER_TASK"

module load julia
srun julia my_script.jl
```

The above batch job runs the Julia script `my_script.jl` using two CPU cores.

