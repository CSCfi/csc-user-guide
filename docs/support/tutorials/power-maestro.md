# Extended instructions for using Maestro at CSC

Please first read the actual [CSC Maestro page](/apps/maestro.md)
and then consult the power user and special case instructions below.
Further down there are steps to help solving or diagnosing issues
and to prepare data for support requests.

## Standalone jobs on Puhti

!!! Note
    All Maestro jobs must be run on compute nodes via the queuing system.
    Don't run any Maestro jobs, including the GUI on the login nodes.
    Maestro jobs on the login node may be terminated without warning.

The recommended way to run Maestro jobs on Puhti is to create
the input files on your local computer
and instead of running them, write them to disk. The procedure is
shown in [this video](/apps/maestro.md) on our main Maestro page.

Once the files have been copied to Puhti, the job is submitted to
a compute node (or several) by running the `job_name.sh` script
written out by Maestro. It will formulate the task(s) as Slurm
batch jobs and ask resources according to the selected HOST in
your `schrodinger.hosts` file on your Puhti home directory.

Another, more advanced version is to use e.g. the `pipeline` tool
which allows you to bypass some of the Schrödinger jobcontrol
machinery, but requires you to write the job script yourself.
This may be useful, in case some of your subjobs terminate
unexpectedly. In this case, please make note of those JobIds
and contact us at servicedesk@csc.fi

## Maestro `schrodinger.hosts` file

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

You can take a look at the `schrodinger.hosts` file with:

```bash
more $HOME/schrodinger.hosts
```
and you should see the HOST entries as something like:
```bash
name:        test
queue:       SLURM2.1
qargs:       -p test -t 00:10:00 --mem-per-cpu=2000 --account=project_2042424
host:        puhti-login1.csc.fi
processors:  40
```

## How to speed up simulations?

All other Maestro modules run serial jobs, except Jaguar, which can run
real parallel jobs. Don't choose the "parallel" HOST for any other job type
Instead of MPI-parallel jobs, Maestro modules typically
split the workload into multiple parts, each of which can be run independent
of the others. This is sometimes called farming. The Maestro help pages have an
excellent section on this topic. Please have a look (you'll find it like this:
Click the "help" button in the "run settings dialog", then in the first chapter
click the link named "Running Distributed Schrödinger Jobs".

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

If you're using the GUI to set up the job script, don't select the "*"
but specify a number. Bu default, you'll have this many simultaneous
jobs running (or queuing).

### Set number of subjobs

Different modules have different options. You can set some of them in
the GUI, but you may find more options with the `-h` flag:

```bash
pipeline -h
```

, where `pipeline` would be the Maestro module you want to run, like
`qsite`, `glide`, `bmin`, `ligprep`, etc.    

Your job might have a "driver" or "master" process. It needs to run
for whole duration of your work, i.e. as long as any subjobs are still
running. It might make sense to run that on a longrun HOST while the other
jobs might work on a "normal" HOST (and Slurm partition). Suitable
splitting would reduce queuing time. Asking for the longrun HOST "just
in case" is not dangerous, but may lead to unnecessary queuing.

You may be able to set the number of subjobs already in the GUI while
you set the job submission parameters. Typically, it would set the
"number of processors", which in many drivers will be equal to the
number of subjobs. Alternatively, you may be able to set also the
number of subjobs. This enables you to limit the number of simultaneous
jobs with the "processor count" (so that you and others won't run
out of licenses) but keep a single subjob at a suitable size.
Please, have a look at the help text of your driver.

### Set number of molecules per subjob

As an example, the "run settings dialog" of `Glide` offers three options:
* Recommended number of subjobs
* Exactly (fill in here) subjobs
* Subjobs with no more than (fill in here) ligands each

Aim for such numbers that an average subjob takes 1-24 hours to run, so
that the overhead per subjob remains small, but not too long so that the
job parallelizes efficiently and the time is sufficient for each subjob.
At least avoid subjobs that complete
faster than 10 minutes. You can check it afterwards with [seff](/support/faq/how-much-memory-my-job-needs.md)

`seff JOBID` 

## Optimal disk usage

The Schrödinger HOSTs in Puhti have not been configured to use
the NMVE local disk, which is available only on some of the
compute nodes. Thus, the only disk available for the jobs is the
same where your input files are. Hence, it does not make sense
to copy the files to a "temporary" location at the start of the
job.

For a desmond `multisim` workflow you would need to add this set of flags:

```bash
-LOCAL -set "stage[1].set_family.md.jlaunch_opt=["\-LOCAL\"]"
```

## Running the Maestro GUI on Puhti

This is *not recommended*. Running the GUI remotely is slow and prone
to glitches. Please run the GUI locally, and only submit the jobs
on Puhti. If this is not possible, and you have to run the GUI on
Puhti, use the [interactive partition](/computing/running/interactive-usage.md)
and [NoMachine](/apps/nomachine.md).

```bash
module load maestro
sinteractive -i
maestro
```

## Fizzled jobs

Sometimes the jobs are launched but don't finish. The state of the job as
reported by `jobcontrol`, see below, is _fizzled_. This might be due to a
number of reasons but cleaning up and restarting the jobcontrol service
might help. When you don't have any Maestro jobs running (in Puhti), give:

```bash
$SCHRODINGER/utilities/jserver -cleanall
$SCHRODINGER/utilities/jserver -shutdown
```

## Run a test job

Run one of the test jobs that come with Maestro to narrow down
potential issues. On Puhti, in your scratch directory, give:

```bash
installation_check -test test
```

If the test succeeds, the problem is likely in your input. In that case please proceed to the
_postmortem_ step below.

## Asking for support

Maestro has a tool called [postmortem](https://www.schrodinger.com/kb/1692) that can be used to create a
zip file containing the details of a failed job and the Maestro
environment. Please add that to your support request to help us analyse
your issue. On Puhti, first use 

```bash
jobcontrol -list 
```

to find the right JobId (something like `puhti-login1-0-4d34ce08`).

Then, check the right flags for `postmortem` with

```bash
$SCHRODINGER/utilities/postmortem -h
```

and create the postmortem file with

```bash
$SCHRODINGER/utilities/postmortem your-puhti-schrodinger-jobid
```

The file may be large, so instead of sending it as an email attachment, consider
using [a-flip](/data/Allas/using_allas/a_commands/#a-list) and just sending the a link instead.

Also, please have a look at these [instructions to make
support requests](/support/support-howto.md) that minimise us asking 
for more details in separate emails and thus taking it lonfer for you 
to get the issue solved.

