# Using arcrunner to run large job sets in FGCI

Grid computing can be very effective in cases where the analysis task
can be split into numerous independent sub-tasks. This kind of tasks are
generally referred to as *embarrassingly parallel* computing tasks.
Typical examples are cases where the same simulation task is executed
several times with different parameter settings. Another common
embarrassingly parallel job type are cases where the same analysis is
performed to a large set of input files.

Running embarrassingly parallel computing tasks in the grid environment
is in principle straight forward: the user just creates the grid job
files, described in chapter 2.2, submits all the jobs to grid and, once
the jobs are ready, the collects the results and merges them together.
However, this kind of straight forward seeming approach is not always
the most efficient way.

In this chapter we describe a grid job manager tool, called *arcrunner*,
that can be used to run large embarrassingly parallel computing tasks
easily and effectively in the FGI environment. You can use *arcrunner*
at CSC on [Puhti](../../computing/overview.md) or you can download it to your local Linux or MacOSX
computer.

## Installing arcrunner

Arcrunner is installed on Puhti where it can be launched with the
command:

    arcrunner

To use *arcrunner* in your local computer, you need to have the ARC
middleware client and python installed on your computer. You can
download the *arcrunner* tool from the [Web site of FGI](https://confluence.csc.fi/download/attachments/10782989/arcrunner_29.11.13.tgz)

Once you have downloaded the installation file, unpack it with the
command:

`tar zxf arcrunner.tgz`

Next go to the *arcrunner/bin* directory:

`cd arcrunner/bin`

The next step is to modify the fifth row of the *arcrunner* file so that
the *jobmanagerpath* variable corresponds to the location of your
*arcrunner* installation. For example if you have downloaded and
unpacked *arcrunner* installation package to directory */opt/grid* the
jobmanagerpath defining line should be:

`set jobmanagerpath=("/opt/grid/arcrunner")`

After this the only thing left to do is to add the *arcrunner/bin*
directory to your command path.

## Using arcrunner

The minimum input for the *arcrunner* command is:

`arcrunner -xrsl job_descriptionfile.xrsl`

When *arcrunner* is launched, it first checks all the sub-directories of
the current directory. If a job description file, defined with the
option *-xrsl*, is found in sub-directory, arcrunner tries to execute
the task in the FGCI environment.

In cases where there are a large number of grid jobs to be executed, all
jobs are not submitted at once. In these cases *arcrunner* tries to
optimize the usage of the grid environment. It follows the number jobs
that are queuing in the clusters and sends more jobs only when there are
free resources available. The command also keeps a track of the executed
grid jobs and starts sending more jobs to those clusters that execute
the jobs most efficiently. If you don't want to use all the FGI
clusters, you can use the cluster list file and option *-R* to define
what clusters will be used.

The maximum number of jobs, waiting to be executed, can be defined with
the option *-W*. If some job stays in a queue for too long a time, it is
withdrawn from this queue and submitted to another cluster. The maximum
queuing time (in seconds) can be set with the option *-Q*

Sometimes, some FGI cluster may not work properly and the jobs may fail
due to technical reasons. If this happens, the failed grid jobs are
re-submitted to other clusters three times before they are considered as
failed sub-jobs.

During execution *arcrunner* checks the status of the sub-jobs once a
minute and prints the status of each active sub-job. Finally it writes
out a summary table about the sub-jobs.

When a job finishes successfully, the job-manager retrieves the
resultant files from the grid to the grid job directory.

**Table 3.** *arcrunner* options

|                    |                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------|
| **Option**         | **Description**                                                                               |
| -xrsl *file\_name* | The common xrsl file name that defines the jobs.                                              |
| -R *file\_name*    | Text file containing the names of the clusters to be used.                                    |
| -W *integer*       | Maximum number of jobs in the grid waiting to run. (Default 200).                             |
| -Q *integer*       | The maximum time a jobs stays in a queue before being resubmitted. (Default 3600s).           |
| -S *integer*       | The maximum time a jobs stays in a submitted state before being resubmitted. (Default 3600s). |
| -J *integer*       | Maximum number of simultaneous jobs running in the grid. (Default 1000 jobs).                 |


## An arcrunner example

The following simple example demonstrates the usage of the arcrunner
command. First we assume that we have a set of files which we wish to
analyse. In this example we have 100 files named *file\_1*, *file\_2*,
*file\_3*, ...,*file\_100* , each containing 100 integer numbers in one
column. We would like to calculate the average for the values in each
file using FGI.

To run the analysis in FGI using *arcrunner* we first need to create a
sub-folder for each of the input files and copy the input files there.
This could be done, for example, with a shell script like the following
bash script:

```bash
for number in `seq 1 100`
do
  mkdir subjob_$number
  mv file_$number subjob_$number/inputfile.txt
done
```

Now your directory should contain 100 subfolders, each containing one of
the files to be analysed. Note that the name of the input file is now
the same (*inputfile.txt*) in all the sub-job directories. The average
of the numbers in a file called *inputfile.txt* can be calculated with
the following script. The script is created with a text editor and saved
as file *calc\_average.csh*

```bash
#!/bin/bash
awk '{ a = (a + $1)} END{ print a/NR }' inputfile.txt > output.txt 
```

To run this script in FGI we need to create a job description file. In
this case we will name the file *average.xrsl*. The content of the job
description file would then be:

```
&(executable=calc_average.csh)
(jobname=arc_example)
(stdout=std.out)
(stderr=std.err)
(cpuTime="2 minutes")
(memory="1000")
(inputfiles=
("inputfile.txt" "inputfile.txt" )
)
(outputfiles=
("output.txt" "" )
) 
```


Next we need to copy the command script and the job description files to
all the sub-job folders. This is done with another small shell script
containing the following loop:

```bash
for number in `seq 1 100`
do
  cp calc_average.csh subjob_$number/
  cp average.xrsl subjob_$number/
done
```

Now we have 100 sub-directories each containing a grid job description
file and the corresponding job script and input files. We can now launch
the analysis task with *arcrunner*

`arcrunner -xrsl average.xrsl`

When the command is executed, *arcrunner* starts sending the 100 jobs,
one by one, to FGI. Sending the jobs will take some time. If some of the
FGCI servers are down, *arcrunner* will give error messages about
unsuccessful job submission. These messages can however be ignored as
the jobs will be re-submitted during the next job status checking cycle.
The job submission log that *<span
style="text-decoration: none">arcrunner </span>* prints to standard
output (i.e your screen) looks like the following:

```
/home/csc/kkmattil/.arc/clusters_for_arcrunner
2012-08-08 15:50:26 INFO Job subjob_1 submitted with gid gsiftp://electra-grid.chem.jyu.fi:2811/jobs/vH2LDmdtKJgna2baVq8oAPWnABFKDmABFKDmcHNKDmABFKDmd56JWm
2012-08-08 15:50:26 INFO Job subjob_1 changing state from new to submitted
2012-08-08 15:50:48 INFO Job subjob_10 submitted with gid gsiftp://taygeta-grid.oulu.fi:2811/jobs/MbFLDmztKJgnhWNBSqWNI3hmABFKDmABFKDmv7KKDmABFKDmGprtIn
2012-08-08 15:50:48 INFO Job subjob_10 changing state from new to submitted
2012-08-08 15:50:50 INFO Job subjob_100 submitted with gid gsiftp://maia-grid.uef.fi:2811/jobs/hG5KDm1tKJgn9NOVEmGrhjGmABFKDmABFKDmeBMKDmABFKDmT8QnTo
2012-08-08 15:50:50 INFO Job subjob_100 changing state from new to submitted
2012-08-08 15:50:52 INFO Job subjob_11 submitted with gid gsiftp://aesyle-grid.fgi.csc.fi:2811/jobs/c9sLDm3tKJgnKazeGptluZemABFKDmABFKDmydNKDmABFKDmrS5hJn
2012-08-08 15:50:52 INFO Job subjob_11 changing state from new to submitted 
```

When all the jobs are submitted or the number of the submitted job
reaches the limit of simultaneously submitted jobs ( default 200 ),
*arcrunner* writes out a summary about the computing task it is
executing. For example, the following summary tells that of the 100
sub-jobs, 71 jobs have already finished, two are running, 25 are queuing
and 2 are being submitted to the clusters.

```
2012-08-08 16:08:21 INFO host                        new submitted queuing running finished failed success failure
2012-08-08 16:08:21 INFO merope-grid.cc.tut.fi         0         0       9       0        0      0       0       0
2012-08-08 16:08:21 INFO asterope-grid.abo.fi          0         0       0       0        9      0       0       0
2012-08-08 16:08:21 INFO electra-grid.chem.jyu.fi      0         0       1       0        9      0       0       0
2012-08-08 16:08:21 INFO taygeta-grid.oulu.fi          0         0       0       1        8      0       0       0
2012-08-08 16:08:21 INFO maia-grid.uef.fi              0         0       0       1        8      0       0       0
2012-08-08 16:08:21 INFO grid.triton.aalto.fi          0         0       5       0        4      0       0       0
2012-08-08 16:08:21 INFO aesyle-grid.fgi.csc.fi        0         0       0       0        9      0       0       0
2012-08-08 16:08:21 INFalcyone-grid.grid.helsinki.fi   0         0       1       0        8      0       0       0
2012-08-08 16:08:21 INFO celaeno-grid.lut.fi           0         0       9       0        0      0       0       0
2012-08-08 16:08:21 INFO usva.fgi.csc.fi               0         1       0       0        8      0       0       0
2012-08-08 16:08:21 INFO pleione-grid.utu.fi           0         1       0       0        8      0       0       0
2012-08-08 16:08:21 INFO TOTAL                         0         2      25       2       71      0       0       0 
```

The *arcrunner* command should be kept running until all the jobs have
reached the state of *success* or failure and the command stops. For the
case of large analysis tasks this can mean that *arcrunner* will be
running for several days. In these kind of situations we recommend that
*arcrunner* is launched inside a *screen* virtual session. If the
*arcrunner* command stops for some reason before all the sub-jobs are
ready, you can continue the jobs by running the same *arcrunner* command
again.

When all the sub-jobs are processed, all the sub-job directories contain
a new directory called *results.*This directory now contains the output
files defined in the job description files and the standard output and
input files. In this case the results directory contains files
*output.txt*, *std.err* and *std.out*. All the results can now be
collected into one file, for example, with the command:

```bash
cat subjob_*/results/output.txt > results.txt
```
