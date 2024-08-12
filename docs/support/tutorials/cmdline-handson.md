# Hands-on batch jobs in Puhti tutorial

The next few exercises take you through submitting your first batch jobs on Puhti.
We've used R and HMMER as examples, but the principles are the same for other
applications as well. However, please always consult the [application specific
page](../../apps/index.md) if it exists. It may have a tailored template for you.

## Get the exercise files
### a) Log in to Puhti from a terminal

`ssh your-username@puhti.csc.fi` or if you don't have an ssh client available, you can log in via the [Puhti web interface](../../computing/webinterface/index.md) using your web browser and open a terminal there.

### b) Go to scratch directory and download the exercises file

`csc-workspaces` command will show you which projects you're a member of.
```
csc-workspaces
...
Project: project_20001234 "Great science with HPC tools"

/projappl/project_20001234        16G/54G         38K/100K
/scratch/project_20001234         56G/1.1T       107K/1.0M
------------------------------------------------------------
```
Make note of the project name (here: _project_20001234_). Select the one you want 
to work with and change to the scratch directory (don't work in the `$HOME` folder!):

```
cd /scratch/project_20001234
```

and download the input files with `wget`:

```
wget https://a3s.fi/docs-files/input-data.tar
```

### c) Uncompress the exercises file

```
tar xvf input-data.tar
``` 

!!! Note
    Text in *italics* is not a command and
    you can choose what to put there (but you need to be consistent later).

## A simple batch job script

### a) Create a batch job script that prints the compute node on which it is running.

Using nano editor (use whichever editor you like):

```
nano test_hostname.sh
```

Put this into the file.

```
#!/bin/bash -l
#SBATCH --job-name=print_hostname
#SBATCH --time=00:01:00
#SBATCH --partition=test
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1G
#SBATCH --account=project_20001234

sleep 30
echo "This job runs on the host: "; hostname
```

To exit from the nano editor:

`CTRL+O (enter); CTRL+X (confirm save)`

Submit the batch script to Puhti

```
sbatch test_hostname.sh
```

### b) Check the job status.

In the following command replace _<your username\>_ with your
CSC username - or which ever you used to log in to Puhti. If
you are not sure which it is, you can check it with `whoami` or with
this command `echo $USER`).

```
squeue -u your_username
```

### c) What and where did the job print out?

!!! Note 
    Here you need to replace the *JOBID* with the ID your job was given.

```
less slurm-JOBID.out (type q to quit)
```

If the job failed, please check which project you had in the batch script `--account=???`
[Typical reasons for a failed batch in our FAQ](../faq/why-does-my-batch-job-fail.md)

##Simple R job 

Run a simple R job from a script. The script will fit a straight line
through a file containing some x,y value pairs. More info on
[running R in the CSC environment](../../apps/r-env.md)

### a) Set up an interactive batch job and initialize R environment

As we now plan to run an application interactively, we'll ask for an interactive
batch job and work there, instead of the login node. The following
command will set it up (use the same _project_ as in the batch script above):

```
sinteractive --account <project> --mem 4000 --tmp 10 --time 2:00:00
```

Give `module load r-env` to initialize the R environment.

- **How do you know if it is already loaded?**

Go to the directory `r-job`, where you have the data (a file called
`data.csv`) and launch R:

```
start-r
```

You should get some introductory text and your prompt should now look like this:


```
...
Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

>
```
Now, interactively, fit a line through data points in the file _data.csv_.
Write (or copy/paste) the following commands in the prompt (press enter after each line,
watch for errors):
```
mydata <- read.csv("data.csv")
fit <- lm(y~x,mydata)
fit$coefficients
```
You should see something like this:
```
(Intercept)           x
  0.8289352   3.1440282
```
Then quit from the R-command prompt with
```
q()
```

### b) Create a script to run the same works.

In the "r-job" directory, create an R script file (R
commands to be executed) with the same commands as you pasted
in the R command prompt. Name the file `fit.R`

You can use e.g. `nano` editor, which you need to initialize first
with `module load nano` (in the interactive node, in the login node,
it is available without the module load command).

Make sure the file is ok with:
```
cat fit.R
```
You should see three lines with the R commands.

### c) Run the script interactively

```
apptainer_wrapper exec Rscript --no-save --no-restore -f fit.R
```

### d) Results
- **Did the job succeed?**
- **What are the fit coefficients?**

## Simple R job as a batch job 

Now run the previous R script as a batch job.

### a) Create a batch job script, which will submit the job to the queue.

Copy the *serial batch script* template from [CSC's R-env page](../../../apps/r-env/#serial-batch-jobs)
into a file called _batch.sh_

In addition to setting up the computing requirements, this script
also resets some additional R environment variables. These won't
be necessary, if you run some other application. Always check first
if there's a template batch script for your application, and use that
as the base for your own script.

For this example, you'll need to make three changes. Replace the _<project>_ 
placeholder in the `--account` and `echo "TMPDIR=/scratch/...`
lines with your own computing project. And finally, at the end of the script, 
replace (`myscript.R`) i.e. the R-script to be executed to `fit.R`.

### b) Submit the batch script with

```
sbatch batch.sh
```

### c) Did the job succeed? Where are the fit constants?


## Run tens of R batch jobs as an array job

In this example, we will repeat the previous fitting job for 20 datasets 
using the array job functionality of SLURM. Note, that for such short 
jobs it would not make sense to run them as separate batch jobs, but 
you could loop over them in one job or better inside the R script.

### a) Prepare a list of files to process.

Go to the folder named `r-array`. Create there a file called
`datanames.txt`. This file will contain the names of all those files
that will be used as input to the fitting. Run the following commands to
create it.

``` 
cd data_dir
ls 
ls > ../datanames.txt
```

### b) Write the R script, that will do the fitting.

Go back to the r-array folder, create a script named `modelscript.R`
and put the following commands to it (you can copy the previous script
and edit that, or start from scratch).

```
dataname <- commandArgs(trailingOnly = TRUE)
mydata <- read.csv(paste0("data_dir/",dataname))
fit <- lm(y~x,mydata)
write(fit$coefficients,
file=paste0("result_dir/",dataname,"_result.txt"))
```

The first line will extract from the batch command the name of the
dataset to be fitted. The next line reads that data into the variable
mydata. Then we fit, like in the previous example, and finally write the
coefficients into a file.

### c) Create a batch script to submit the job.

Name it `R_array.sh`. Copy the contents from the previous example.
Add the following line among the other lines starting #SBATCH:

```
#SBATCH --array=1-20
```

It will ask SLURM to run an array of 20 jobs. Edit the output and error
files to go to their own *directories* and files by editing/adding
(`%a` will be replaced with the number of the array job):

```
#SBATCH --output=out/output%a.txt
#SBATCH --error=err/errors%a.txt
```

Change the SLURM partition to be used (`--partition=`) from _test_ to _small_.

Before the line with `srun apptainer_wrapper...`, add the following line

```
dataname=$(sed -n "$SLURM_ARRAY_TASK_ID"p datanames.txt)

```
and edit the line to run the R command into:

```
srun apptainer_wrapper exec Rscript --no-save modelscript.R $dataname
```

You should now have:

   1. `datanames.txt`, which has the names of your datafiles
   1. `modelscript.R`, which contains the R code to do the fitting
   1. `R_array.sh`, which is the batch script to submit the job
   1. (and the folders `out, err, data_dir, result_dir` which were there already)

### d) run the batch script with

```
sbatch R_array.sh
```
Since you're now running 20 jobs, they might take a moment in the queue.
You should get the fit coefficients in separate files in the
`result_dir`. Let's now use interactive R to look at the results.

### e) Collect the results and plot them.

Note, plotting will work only if you have 
[remote X11 forwarding](../../computing/connecting/index.md#graphical-connection).
Actually, for R, there is even a tailored remote setup using 
[RStudio Server](../../apps/r-env.md),
and you're welcome to use that, but in this tutorial, the key point is to 
demonstrate the general approach.

In the folder containing `analyse.R` start the interactive R shell with
```
start-x
```

In the R shell that opens, write `source("analyse.R")`. This will 
run (source) the script contents. The original data was
created by calculating the y values by y=2x + some random noise.
The plot will appear in a separate window.

### f) How do the fit coefficients match that?

## Batch job with thread parallelization

Some applications can be run in parallel to speed them up. In this
example you run the [HMMER software](../../apps/hmmer.md) to describe 
and analyze related or similar protein sequence areas both in serial 
and parallel to see if the jobs speed up.

HMMER uses a database that is already installed, but the protein
sequences you want to study need to be copied first to be used as input:

```
wget https://a3s.fi/docs-files/example.fasta
```

### a) Serial HMMER job

Let's first run the job with just one core. Copy one of the old batch
scripts to current directory, and change / add the following items in
it (or take a look at [these examples](../../computing/running//example-job-scripts-puhti.md)):

1. Output to `out_%j.txt`
1. error to `err_%j.txt`
1. run time 10 minutes
1. load the `hmmer` -module
1. remove the R specific environment settings
1. run command:

```
hmmscan $PFAMDB/pfam_a.hmm example.fasta > example_1.result
```

Submit the job with: `sbatch your-jobscript-name.sh`

Submitting the job echoes the SLURM JOBID number to the screen, but
that is also shown in the output and error filenames
(`out_<SLURM_JOBID>.out`). Check if the job is running with

`squeue -u <your username>` (use *your* username)

Or

`squeue -j <SLURM_JOBID>` (replace with the JOBID of your job)

Once the job is finished you can check how much memory and time it used:

```
sacct -j <SLURM_JOBID> -o elapsed,reqmem,maxrss
```

- **Did you reserve a good amount of memory? (not excessively too much, but
enough to not be close to memory running out and terminating the job).**
Another way to get a quick summary of used resources is:

```
seff <SLURM_JOBID>
```

### b) Parallel HMMER job

Now, let's try with 4 cores. At this point we'll also switch to using
the environment variable `$SLURM_CPUS_PER_TASK` to avoid mistakes
and the need to change that in many places. Add this line to the batch
script:

```
#SBATCH --cpus-per-task=4
```

Note that this only asks the _queuing_system_ for more resources. You need to tell it also
to the application you're running (how, depends on the application). Change the run command to:

```
hmmscan --cpu $SLURM_CPUS_PER_TASK $HMMERDB/Pfam-A.hmm example.fasta > example_$SLURM_CPUS_PER_TASK.result
```

As you've asked for 4 cpus per task, the environment variable
`$SLURM_CPUS_PER_TASK` evaluates to 4 when the script is run, and
you only need to change the number on the #SBATCH line if you want to try other
numbers as well.

Submit the job and check with the `sacct` command how long it took to
run the hmmer job and how did the memory usage change and try to answer
these questions:

- **Does it make sense to use 4 cores instead of 1?**
- **Was the memory reservation ok?**
- **Does it make sense to use more than 4 cores?**
- **How to speed up the job?**

## Batch job memory consumption

### a) Exceed memory allocation on purpose

Create a new _R-script_ (like in the previous exercise) named `mem-test.R`. It
should have the following contents:

```
dim=10
dim_end=1000
while (dim < dim_end) {
mat <- matrix(rnorm(dim*dim), dim)
print("passed dimension")
print(dim)
dim=dim*2
}
print("all done")
```

Variable `dim` is the dimension of the square matrix, which will be
filled with normal distributed random numbers. The script doubles
`dim` until it exceeds `dim_end`. Make a new _batch script_ to run your
R-script `mem-test.R`. In addition to the resource requests your
script needs to load the R-environment and then run the R-script (as in
previous exercise). Submit the script with `sbatch`.

Once the job has been completed (how can you check if it is running or
queuing?), check with `sacct` or `seff` how much memory was used as
in the previous exercise. If the job completed successfully, increase
the `dim_end` variable in your script *i.e.* make a bigger matrix and
rerun the job. Note also the time it takes to run the job. How does the
time and memory needed by the job depend on the number of elements in
the array?

  max(dim) |  # of elements  | Time [s] (Elapsed) |  Memory used (MaxRSS)
  ----------|----------------|--------------------|----------------------
  | | | 
  | | |  
  | | |  
  | | |  

- **How big matrix is needed to exceed the default allowed memory of the batch job?**

## Scaling test for an MPI parallel job

Before running parallel jobs it is important to determine how the job
scales. It does not make sense to use many cores, if this does not speed
up the job. The speedup depends on the application but also input. In
this tutorial we'll use CP2K which can use thousands of cores for
certain job types and model systems (but not for this one). Therefore,
it is important to test the scaling for each different job type (or
model system type). The idea is not to run production simulations, but
quick short simulations (*i.e.* using the actual production system) but
only for like 1-5 minutes, which will be enough to reveal the
performance.

### a) Prepare a CP2k job

First copy the input file to your working directory:

```
module load cp2k`
cp $CP2K_DATA_DIR/tests/QS/benchmark/H2O-32.inp .
```

Then create a batch script and submit it with `sbatch`
!!! Tip
    Remember to check the CSC software pages for [application specific
    examples for batch jobs:](../../apps/index.md)

For the first job, ask minimal resources (copy the rest of the
batch script contents from CSC's CP2k page):

```
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

# submit the job
srun cp2k.popt H2O-32.inp > H2O-32_$SLURM_NPROCS.out
```

### b) Run the same job with increasing resources and note performance

After running the job with one core, edit the batch script to use more
cores/mpitasks (*e.g.* 2,4,8,16, ... this is the `--ntasks` or `--ntasks-per-node` flag)
and rerun
the job. The output files will be named with the number of cores used to
run them (`$SLURM_NPROCS`). Instead of the small partition you can
also use the `test` partition. If you ask for more than 40 cores (in Puhti), you
need to switch to `large` partition. In multinode jobs, always 
limit the number of *Nodes*, so that the job is not spread onto
more nodes than necessary as it
[creates unwanted communication overhead and fragments the allocations on the system](../../computing/running/performance-checklist.md).

With the following command you can sum the time spent at different steps
for each job.

`grep "CPU TIME" H2O-32_1.out | awk '{a+=$5;print a}'`

Check with `seff JOBID` how much memory the simulation used (compare
`sacct` and `seff` output!) and fill in the data in the following
table. If your code does not print out either the performance or used
time, you can use the `sacct` command (`sacct -j <JOBID> -o
elapsed,alloc,maxrss`)

A rule of thumb for acceptable scaling is that when you double the resources,
the job should speed up at least 1.5 fold. Ideally it would speed up
linearly with resources *i.e.* 2 fold, so often you're better off running many
smaller simulations at the same time, rather than few with very many cores - if
you have this option.

The speedup at some core counts may be off the trend. There may be
variation due to load on the system or because the code/system does not
parallelize well or be able to distribute the computational load for
that particular core count. Sometimes rerun helps to sort out an
outlier. If you know the code parallelizes well, there is no point to
start testing from 1 core, but from where you think the code runs well.
You'll notice bad speedup anyway.

  # cores | Time [s] (Elapsed) | Speedup | Ideal speedup | Memory used
  ----------|----------------------|---------|---------------|-------------
 | | | | 
 | | | | 


### c) Scaling test results

- **How many cores can you use efficiently? (i.e. how far does the job scale)**
- **How does the required memory depend on the number of cores?**
- **Why are the elapsed times reported by sacct slightly different to the sum of "CPU TIME" lines?**
- **Are all nodes similar? Should we limit which resources SLURM may give us?**
- **If we want to run a different cp2k system do we need to rerun the scaling test?**
