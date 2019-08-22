# Serial and Thread Based Batch Jobs
Serial jobs and thread based parallel jobs (also called shared memory jobs) need to be run inside one computing node. Thus the jobs are limited by the hardware specifications of the available in nodes. In Puhti the nodes have two processors with 20 cores each, so 40 cores in total.

Sbatch option `--cpus-per-task` is used the define the number of computing cores that the batch job task will use. Option `--nodes=1` ensures that all the reserved cores will be located in the same node and `--ntasks=1` will assign all the reserved computing cores for the one same task.

In the case of threads-based jobs, the `--mem` option is recommended for memory reservation. This option defines the amount of memory needed per node. Note that if you use `--mem-per-cpu` option instead, the total memory request of the job will be memory request multiplied by the number of reserved cores (`--cpus-per-task`). Thus if you modify the number of cores to be used, you should check the memory reservation too.

Below is a sample batch job for using 6 cores in threads-based parallelization.

```
#!/bin/bash -l
#SBATCH --jobname=example
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=project_<project_id>
#SBATCH --partition=serial
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=6000
#

myprog <options>

```
Note that the command is run without `srun` command.

In most cases it is most efficient match the number of reserved cores to the number of threads or processes the application uses, but you should check the documentation for application specific details.

If the application has some command line option to set the number of threads/processes/cores to use, it should always be set to make sure the software behaves as expected. Some applications use just one core by default even if more are reserved. Some other applications may try to use all the cores in the node even if only some are reserved. Environment variable __$SLURM_CPUS_PER_TASK__ can be used instead of a number. This way the command does need to be edited if `--cpus-per-task` is changed.