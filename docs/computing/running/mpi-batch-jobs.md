# MPI Based Batch Jobs
In MPI jobs each task has its own memory allocation and thus the tasks can be distributed between nodes.

Below is a sample batch job for a MPI based job using 50 cores

```
#!/bin/bash -l
#SBATCH --jobname=example
#SBATCH --account=project_<project_id>
#SBATCH --partition=parallel
#SBATCH --time=02:00:00
#SBATCH --ntasks=50
#SBATCH --mem-per-cpu=4000

srun myprog <options>

```
Note that the command needs to be run with `srun`.
MPI program can **not** be started with mpirun or mpiexec.

- To request more cores per MPI task, you can use the argument `--cpus-per-task`.The default value is one core per task. 
- It is recommended to request memory using the `--mem-per-cpu` option.
- If more fine tuned control is needed, the exact number of nodes and number of tasks per node can be specified with
`--nodes` and `--ntasks-per-node` respectively.


Multiple `srun` commands can be run in the same batch script and the command accepts the same options as `#SBATCH`. Options given to `srun`
will override the options given using `#SBATCH`, assuming that they fit inside the original `#SBATCH` resource allocation.


