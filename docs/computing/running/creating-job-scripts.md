# Creating a batch job script

A batch job script will contain definitions for resources to be reserved for
the job and the commands the user wants to run.

An example of a simple batch job script.

```
#!/bin/bash -l
#SBATCH --job-name=myTest
#SBATCH --account=project_<project_id>
#SBATCH --partition=serial
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=2G

module load myprog/1.2.3

myprog -i input -o output
```
The first line with `#!/bin/bash -l` tells that the file should be interpreted
as a bash script (the `-l` flag invokes a login shell, which is needed for the
module system to work properly) .

Lines starting with `#SBATCH` are arguments to the batch system.
We are only using a small part of the options. For a list of all possible
options, see the [slurm documentation](https://slurm.schedmd.com/srun.html).

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

The partition i.e. queue needs to be set according to the job requirements.
```
#SBATCH --partition=serial
```
Different queues have different limits and available resources.


_Information about the different queues:_

| Queue          |  Time Limit   |Job node limit | Number of nodes | Memory | Cores/GPUs node   |
|----------------|---------------|---------------|-----------------|--------|-------------------|
|Serial\*\*      |  3 days       | 1 node        |     532         | 190G   | 40 cores          |
|                |               |               |     132         | 382G   |                   |
|                |               |               |     12          | 764G   |                   |
|parallel\*\*    |  3 days       | 100 nodes     |     532         | 190G   | 40 cores          |
|                |               |               |     132         | 382G   |                   |
|                |               |               |     12          | 764G   |                   |
|hugemem         |  3 days       |  1 node       |     6           | 1532G  | 40 cores          |
|gputest         |  30 minutes   |  2 nodes      |     2           | 382G   | 40 cores + 4 GPUs |
|gpu             |  3 days       |  160 GPUs     |     78          | 382G   | 40 cores + 4 GPUs |


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


After defining all the required resources in the batch job script, we define
what commands we want to run.

```
module load myprog/1.2.3
myprog -i input -o output
```

Note that for modules to be available to batch jobs, they need to be loaded in
the batch job script.

For batch jobs using multiple cores and nodes see the following sections:

- [Serial and shared memory jobs](serial-and-thread-based-batch-jobs.md)
- [MPI based jobs](mpi-batch-jobs.md)
- [Array jobs](array-jobs.md)
