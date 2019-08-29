# Creating a batch job script

A batch job script will contain definitions for resources to be reserved for
the job and the commands the user wants to run.

An example of a simple batch job script.
```
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=project_<project_id>
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=2G
#SBATCH --partition=small

module load myprog/1.2.3

srun myprog -i input -o output
```
The first line with `#!/bin/bash` tells that the file should be interpreted
as a bash script.

Lines starting with `#SBATCH` are arguments to the batch system.
We are only using a small part of the options. For a list of all possible
options, see the [Slurm documentation](https://slurm.schedmd.com/sbatch.html).

The general syntax for a `#SBATCH` option is:

```
#SBATCH option_name argument
```

In our example:

```
#SBATCH --jobname=myTest
```

sets the name of the job. It can be used to identify a job in the queue and
other listings.

```
#SBATCH --account=project_<project_id>
```

sets the billing project for the job. **This argument is mandatory, failing to
set it will cause your job to be held with the reason "_AssocMaxJobsLimit_"**
You can check you projects in [My CSC](https://my.csc.fi) in the "My Projects"
tab.

Time reservation is set with option `--time`

```
#SBATCH --time=10:00:00
```

Time is given in the format __hh:mm:ss__ (optionally __d-hh:mm:ss__, where
__d__ is days). Maximum time depends on the queue selected. When time
reservation ends, the job is terminated whether it is finished or not, so time
reservations should be sufficient. Job will consume billing units according to
it's actual runtime.

```
#SBATCH --mem-per-cpu=2G
```

sets the required memory per requested cpu-core. If you go over the requested
memory, your job will be terminated.

The partition needs to be set according to the job requirements.
```
#SBATCH --partition=small
```

!!! Note "Available partitions"
    The currently available batch job partitions can be found [here](batch-job-partitions.md).


After defining all the required resources in the batch job script, we set up our 
environment. Note that for modules to be available to batch jobs, they need to be loaded in
the batch job script.

```
module load myprog/1.2.3
```

Finally we launch our program using the `srun` command

```
srun myprog -i input -o output
```


## Serial and shared memory batch jobs

Serial jobs and shared memory jobs need to be run inside one computing node. Thus the jobs are limited by the hardware specifications of the available in nodes. In Puhti each node has two processors with 20 cores each, so 40 cores in total.

Sbatch option `--cpus-per-task` is used the define the number of computing cores that the batch job task will use. Option `--nodes=1` ensures that all the reserved cores will be located in the same node and `--ntasks=1` will assign all the reserved computing cores for the one same task.

In the case of threads-based jobs, the `--mem` option is recommended for memory reservation. This option defines the amount of memory needed per node. Note that if you use `--mem-per-cpu` option instead, the total memory request of the job will be memory request multiplied by the number of reserved cores (`--cpus-per-task`). Thus if you modify the number of cores to be used, you should check the memory reservation too.


In most cases it is most efficient match the number of reserved cores to the number of threads or processes an application uses, but you should check the documentation for application specific details.

If the application has some command line option to set the number of threads/processes/cores to use, it should always be set to make sure the software behaves as expected. Some applications use just one core by default even if more are reserved. Some other applications may try to use all the cores in the node even if only some are reserved. Environment variable __$SLURM_CPUS_PER_TASK__ can be used instead of a number. This way the command does need to be edited if `--cpus-per-task` is changed.




## MPI Based Batch Jobs

 In MPI jobs each task has its own memory allocation and thus the tasks can be distributed between nodes.
 
 The number of MPI tasks to launch is set with:
``` 
 --ntasks=<number_of_mpi_tasks>
```
 
 If more fine tuned control is needed, the exact number of nodes and number of tasks per node can be specified with
`--nodes` and `--ntasks-per-node` respectively.

To request more cores per MPI task, you can use the argument `--cpus-per-task`.The default value is one core per task. 
It is recommended to request memory using the `--mem-per-cpu` option.


!!! Note
    - MPI programs can **not** be started with mpirun or mpiexec, `srun` has to be used
    - A MPI module has to be loaded in the batch job script for the submisson to work properly.


