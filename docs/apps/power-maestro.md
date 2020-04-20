# Extended instructions for using Maestro at CSC

Please first read the actual [CSC Maestro page](/apps/maestro.md)
and then consult the power user and special case instructions below.

## Standalone jobs on Puhti

!!! Note
    All Maestro jobs must be run on compute nodes via the queuing system.
    Don't run any Maestro jobs, including the GUI on the login nodes.
    Maestro jobs on the login node may be terminated without warning.

There are two recommnded ways to run Maestro jobs on Puhti. In both
cases, you start by preparing the input files on your local computer
and instead of running them, write them to disk. The procedure is
shown in [this video](linkki) on our main Maestro page.

Once the files have been copied to Puhti, the job is submitted to
a compute node (or several) by running the `job_name.sh` script
written out by maestro. It will formulate the task(s) as Slurm
batch jobs and ask resources according to the selected HOST in
your `schrodinger.hosts` file on your Puhti home directory.

The recommended way is to create the input files on your local
computer, write them to disk



## Maestro schrodinger.hosts file

This file specifies the resources your jobs can get from the queuing system.
Maestro complains of the location on this file, but ignore it, it's ok.
This file must match the version of Maestro you are using (locally and in
your module command). Version match is checked at each `module load` event.
The file is created by a script (echoed on your screen when
you give `module load maestro`) that you need to run if the file does not
exist, or if the versions don't match.

As the script requests, select the computing project that will be used
for CPU usage and scratch storage. You can find the actual Slurm options
on the HOST descriptions in schrodinger.hosts file. If your jobs require
something, that's not present in the file, you can edit it.

## How to speed up simulations?

All other Maestro modules run serial jobs, except Jaguar, which can run
real parallel jobs. Instead of MPI-parallel jobs, Maestro modules typically
split the workload into multiple parts, each of which can be run independent
of the others. This is sometimes called farming.

Typically, the workload processes a lot of molecules. If you have enough
molecules, you can split the full set into smaller sets, and process each
of them as a separate job. Since this is typical, the Maestro modules have
easy-to-use options to define the number of (sub)jobs. However, you must know
in advance how many (sub)jobs to launch. In principle, this requires testing
for each different use case.

!!! Note
    When you start with a new kind of work. Don't **try** if you got the
    syntax right with 1000000 molecules and 1000 subjobs. Try with 100
    molecules and 2 subjobs. Learn how long it takes per molecule, adjust
    your parameters and scale up.

### Set number of subjobs

Different modules have different options. You can set some of them in
the GUI, but you may find more options with:

```bash
pipeline -h
```

, where `pipeline` would be the Maestro module you want to run.

Your job might have a "driver" or "master" process. It needs to run
for whole duration of your work, i.e. as long as any subjobs are still
running. It might make sense to run that on a different HOST (and hence
on a different Slurm partition).

### Set number of molecules per subjob
### Let Maestro decide

--> constraints:
too few (takes long, slurm timeout)
too many (unnecessary overhead, license runs out, mess)


## Running the Maestro GUI on Puhti

This is not recommended. Running the GUI remotely is slow and prone
to glitches. Please run the GUI locally, and only submit the jobs
on Puhti. If this is not possible, and you have to run the GUI on
Puhti, use the [interactive partition]() and 
[NoMachine](/apps/nomachine.md).

```bash
module load maestro
sinteractive -i
maestro
```