# Advanced batch jobs
## Hyper-threading
In Puhti one can use Hyper-threading so that the number of simultaneous processes in a node can exceed the number of physical cores. In this approach, the operating system executes the program through virtual cores. As each physical core can run two virtual cores, one Puhti node can have 48 virtual cores, when hyper-threading is used.

The efficiency of hyper-threading depends strongly of the program used. You should always first test if using hyper-threading really improves the execution times before launching larger hyper-threading utilizing jobs.

In practice, hyper-threading is taken in use by using <var>aprun</var> with option <var>-j</var> 2 (assigning 2 compute units per core). You can also use aprun option <var>-N</var> 48 to define that the job should be executed with 48 processing elements per node.

```
!/bin/bash -l
## MPI parallel job script example, HyperTreading mode
#SBATCH -J HT_job
#SBATCH -e my_output_err_%j
#SBATCH -o my_output_%j
#SBATCH -t 00:11:00
#SBATCH -N 4
#SBATCH -p test

## 4x24=96 cores reserved
## run my MPI executable using hyperthreading (2x96=192 compute units)
aprun -j 2 -n 192 -N 48 ./test2
```
