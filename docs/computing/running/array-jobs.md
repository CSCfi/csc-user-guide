# Array jobs

In many cases, a computational analysis job contains a number of similar independent subtasks.
A user may have several datasets that are analyzed in the same way, or the same simulation code
is executed with a number of different parameters. These kinds of tasks are often called
_embarrassingly parallel_ jobs, or collectively _task farming_, since they can, in principle,
be distributed to as many processors as there are tasks to run.

Array jobs may be a suitable approach if:

1. The runtime of each independent job is long enough for the SLURM batch system
    overhead to be irrelevant.
    * Individual runtimes are longer than about 30 minutes.
2. The total number of independent jobs is not excessively large.
    * A user can only have up to 400 jobs either running or queuing on the batch
      system.

!!! note "Other options"
    When the runtimes are very short or the number of individual jobs is very large,
    there are more suitable options for running high-throughput calculations.
    The recommended tool for these use cases is [HyperQueue](../../apps/hyperqueue.md).
    Alternatives include the
    [Linux `xargs` utility](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html)
    (see [this batch script](https://a3s.fi/pub/xargsjob.sh) for a usage example)
    and the [GNU Parallel shell tool](../../support/tutorials/many.md).

## Defining an array job

In Slurm, an array job is defined using the option `--array` or `-a`, e.g.

```bash
#SBATCH --array=1-100
```

will launch not just one batch job, but 100 batch jobs where the subjob specific environment
variable `$SLURM_ARRAY_TASK_ID` has a value ranging from 1 to 100. This variable can then
be utilized in the actual job launching commands so that each subtask gets processed. All
subjobs are launched in the batch job system at once, and they are executed using as many
processors as are available.

In addition to defining a job range, you can also provide a list of job index values, e.g.

```bash
#SBATCH --array=4,7,22
```

would launch three jobs with `$SLURM_ARRAY_TASK_ID` values 4, 7 and 22.

You can also include step size in the job range definition. The array job definition

```bash
#SBATCH --array=1-100:20
```

would run five jobs with `$SLURM_ARRAY_TASK_ID` values: 1, 21, 41, 61 and 81.

In some cases, it may be reasonable to limit the number of simultaneously running processes.
This is done with the notation `%max_number_of_jobs`. For example, in a case were you have
100 jobs but a license for only five simultaneous processes, you could ensure that you will
not run out of license using the definition

```bash
#SBATCH --array=1-100%5
```

## A simple array job example

As a first array job example, let's assume that we have 50 datasets (`data_1.inp`, `data_2.inp`
... `data_50.inp`) that we would like to analyze using the program `my_prog` that uses the syntax

```bash
my_prog inputfile outputfile
```

Each of the subtasks requires less than two hours of computing time and less than 4 GB of memory.
We can perform all 50 analysis tasks with the following batch job script:

```bash
#!/bin/bash -l
#SBATCH --job-name=array_job
#SBATCH --output=array_job_out_%A_%a.txt
#SBATCH --error=array_job_err_%A_%a.txt
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000
#SBATCH --array=1-50

# run the analysis command
my_prog data_${SLURM_ARRAY_TASK_ID}.inp data_${SLURM_ARRAY_TASK_ID}.out
```

In the batch job script, the line `#SBATCH --array=1-50` defines that 50 subjobs will be submitted.
The other `#SBATCH` lines refer to individual subjobs. In this case, one subjob uses at most one
processor (`--ntasks=1`), 4 GB of memory (`--mem-per-cpu=4000`), and can last up to two hours
(`--time=02:00:00`). However, the total wall clock time needed to process all 50 tasks is not
limited.

In the job execution commands, the script utilizes the `$SLURM_ARRAY_TASK_ID` variable in
the definition of the input and output files so that the first subjob will run the command

```bash
my_prog data_1.inp data_1.out
```

the second one will run the command

```bash
my_prog data_2.inp data_2.out
```

and so forth.

The job can be now launched using the command

```bash
sbatch job_script.sh
```

Typically, not all jobs are executed at once. However, after a while, a large number of jobs may
be running simultaneously. When the batch job is finished, the `data_dir` directory contains 50
output files.

After submitting an array job, the command

```bash
squeue -l -u <username>
```

reveals that you have one pending job and possibly several other jobs running in the batch job
system. All these jobs have a `jobid` that contains two parts: the `jobid` number of the array
job and the subjob number. Directing the output of each subjob into a separate file is recommended
as the file system may fail if several dozens of processes try to write into the same file at
the same time. If the output files need to be merged into one file, it can often be easily done
after the array job has finished. For example in the case above, we could collect the results
into one file using the command

```bash
cat data_*.out > all_data.out
```

In the case of standard output and error files, defined in the `#SBATCH` lines,  you can use the
definitions `%A` and `%a` to give unique names to the output files of each subjob. In the file
names, `%A` will be replaced by the ID of the array job and `%a` will be replaced by the
`$SLURM_ARRAY_TASK_ID`.

## Using a file name list in an array job

In the example above, we were able to use `$SLURM_ARRAY_TASK_ID` to refer to the order numbers
in the input files. If this type of approach is not possible, a list of files or commands created
before the submission of the batch job can be used. Let's assume that we have a similar task as
defined above but the file names do not contain numbers but are in the format `data_aa.inp`,
`data_ab.inp`, `data_ac.inp` and so forth. Now, we first need to make a list of the files to
be analyzed. In this case, we could collect the file names into the file `namelist` using the
command

```bash
ls data_*.inp > namelist
```

The command

```bash
sed -n <row_number>p inputfile
```

reads a certain line from the name list file. In this case, the actual command script could be

```bash
#!/bin/bash -l
#SBATCH --job-name=array_job
#SBATCH --output=array_job_out_%A_%a.txt
#SBATCH --error=array_job_err_%A_%a.txt
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000
#SBATCH --array=1-50

# set the input file to process
name=$(sed -n ${SLURM_ARRAY_TASK_ID}p namelist)
# run the analysis
my_prog ${name} ${name}.out
```

This example is otherwise similar to the first one except that it reads the name of the file to
analyze from the file `namelist`. This value is stored in the variable `${name}`, which is used in
the job execution command. As the row number to read is defined by the `$SLURM_ARRAY_TASK_ID`,
each data file listed in the file `namelist` is processed as a different subjob. Note that as
we now also use `${name}` in the output definition, the output file name will be in the format
`data_aa.inp.out`, `data_ab.inp.out`, `data_ac.inp.out` and so forth.

## Using array jobs in workflows with sbatch_commandlist

!!! info "sbatch-hq"
    A more efficient alternative to `sbatch_commandlist` is the CSC utility tool `sbatch-hq`,
    which is essentially a wrapper for [HyperQueue](../../apps/hyperqueue.md). `sbatch-hq`
    allows you to submit an ensemble of similar independent non-MPI parallel tasks from a
    command list, i.e. a file in which each line corresponds to an individual subtask to be
    executed. [See the HyperQueue page for more details](../../apps/hyperqueue.md#task-farming-with-sbatch-hq-tool).

In Puhti, you can use the command `sbatch_commandlist` to execute a list of commands as an
array job. This command takes as an input a text file. The command list is split into several
pieces that are executed as an independent sub-task of a array batch job, automatically
generated by the `sbatch_commandlist`. Thus, one subtask of an array job may process several
commands from the command list.

The syntax of this command is:

```bash
sbatch_commandlist -commands commandlist
```

Options `-t` and `-mem` can be used to modify the time and memory reservation of the subjobs
(default 12 h, 8 GB). By default, the billing project is set based on the name of the scratch
directory where this command is executed, but if needed, it can be assigned using option
`-project`. The command list is split into maximum 200 subtasks. If individual tasks are
very short you could use the option `--max_jobs` to decrease the splitting so that each array
job task would take at least around half an hour to process.

After submitting an array job, `sbatch_commandlist` starts monitoring the progress of the
job. If you use `sbatch_commandlist` interactively in the login nodes, you normally don't
want to keep the monitor running for hours. In these cases, you can just close the monitoring
process by pressing `Ctrl-c`. The actual array job is not deleted, but it stays active in the
batch job system and you can manage it with normal Slurm commands.

In addition to interactive usage, `sbatch_commandlist` can be utilized in batch jobs and
automatic workflows, where only certain steps of the workflow can utilize array jobs based
parallel computing. As an example, let's assume we have a gzip compressed tar-archive file
`my_data.tgz` containing a directory with a large number of files. To create a new compressed
archive, that includes also a md5 checksum file for each file we would need to:

1. un-compress and un-pack `my_data.tgz`
2. execute `md5sum` for each file and finally
3. pack and compress the `my_data` directory again.

The second step of the workflow could be executed using a for-loop, but we could also use the
loop just to generate a list of `md5sum` commands, that can be processed with `sbatch_commandlist` .

```bash
#!/bin/bash -l
#SBATCH --job-name=workfow
#SBATCH --output=workflow_out_%j.txt
#SBATCH --error=workflow_err_%j.txt
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --mem=4000
#SBATCH --ntasks=1
#SBATCH --partition=small

#open the tgz file
tar zxf my_data.tgz
cd my_data

#generate a list of md5sum commands
for my_file in *
do
  echo "md5sum $my_file > $my_file.md5" >> md5commands.txt
done

#execute the md5commands as an array job
sbatch_commandlist -commands md5commands.txt

#remove the command file and compress the directory
rm -f md5commands.txt
cd ..
tar zcf my_data_with_md5.tgz my_data
rm -rf my_data
```

Note that the batch job script above is not an array job, but it launches another batch job
that is an array job.
