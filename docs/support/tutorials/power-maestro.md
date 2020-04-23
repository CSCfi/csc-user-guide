# Extended instructions for using Maestro at CSC

Please first read the actual [CSC Maestro page](../../apps/maestro.md)
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
shown in [this video](/apps/maestro/) on our main Maestro page.

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

This file specifies the resources your jobs can get either locally 
or from the queuing system. To use the recommended procedure 
you need to edit the local (on your computer) `schrodinger.hosts` file to
include the same HOSTs that you want to use on Puhti. On Windows, this will
require admin privileges.

On Puhti, Maestro complains about the location on this file, but ignore it, it's ok.
This file must match the version of Maestro you are using (locally and in
your module command). Version match is checked at each `module load` event.
The file is created by a script (echoed on your screen when
you give `module load maestro`) that you need to run if the file does not
exist, or if the versions don't match.

As the script requests, select the computing project that will be used
for CPU usage and scratch storage. You can find the actual Slurm options
on the HOST descriptions in schrodinger.hosts file. If your jobs require
something, that's not present in the file, you can edit it.

On Puhti, Linux and Mac, you can take a look at the `schrodinger.hosts` file with:

```bash
more $HOME/schrodinger.hosts
```

and on Windows you should find it in `C:\Program Files\Schrodinger-version\schrodinger.hosts`

After the longish header and the `localhost` entry , you should see the 
Puhti  HOST entries as something like:
```bash
name:        test
queue:       SLURM2.1
qargs:       -p test -t 00:10:00 --mem-per-cpu=2000 --account=project_2042424
host:        puhti-login1.csc.fi
processors:  40
```

If your `schrodinger.hosts` file does not have the --account=**something** defined
on Puhti delete the file and rerun the script to create it (`module load maestro` will
print out which one). You don't need to have the `--account=` option set in your **local**
`schrodinger.hosts` file. In your local file, it's enough that the different HOST
entries exist (and the gpu-ones have GPU's specified). 

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

If you're using the GUI to set up the job script, don't select * (ampersand)
but specify a number. By default, you'll have this many simultaneous
jobs running (or queuing).

The 'default' submit script will work "as is" for small jobs, but for
large workflows, you'll need to edit it, see below.

### Additional flags for Maestro modules

Different modules have different options. You can set some of them in
the GUI, but you may find more options with the `-h` flag:

```bash
glide -h
```

, where `glide` would be the Maestro module you want to run, like
`qsite`, `pipeline`, `bmin`, `ligprep`, etc.    

The Maestro help has a nice summary of the different options for
different modules: in Maestro help select: "Job Control Guide"
-> "Running jobs" -> "Running Jobs from the Command Line" -> 
"The HOST, DRIVERHOST, and SUBHOST Options"

Set the "driver" or "master" to run on "localhost:1" as it needs to run
for whole duration of your workflow, i.e. as long as any subjobs are still
running. Alternatively, if it needs a lot of resources,
run that on a "longrun" HOST and the others on a "normal" HOST 
(i.e. "small" Slurm partition). Suitable
splitting would reduce your queuing time. Asking for the longrun HOST "just
in case" is not dangerous, but may lead to unnecessary queuing.

!!! Note
    For any jobs in Puhti, never allocate more than one
    core from `localhost` and even that, only for a driver process.

You may be able to set the number of subjobs already in the GUI.
Typically, it would set the
"number of processors", which in many drivers will be equal to the
number of subjobs. Alternatively, you may be able to set also the
number of subjobs. This enables you to limit the number of simultaneous
jobs with the "processor count" (so that you and others won't run
out of licenses) but keep a single subjob at a suitable size.
Please, have a look at the help text of your driver, via the Help
path described above.

In summary, for a large workflow edit the GUI generated script along
the lines:
`-HOST "serial"` to `-DRIVERHOST longrun -SUBHOST serial` 
or
`-HOST "serial"` to `-DRIVERHOST localhost -SUBHOST serial` 

### Set number of subjobs or molecules per subjob

As an example, the "run settings dialog" of `Glide` offers three options:
* Recommended number of subjobs
* Exactly (fill in here) subjobs
* Subjobs with no more than (fill in here) ligands each

Aim for such numbers that an average subjob takes 1-24 hours to run, so
that the overhead per subjob remains small, but not too long so that the
job parallelizes efficiently and each subjob has time to finish.
At least avoid subjobs that complete
faster than 10 minutes. You can check it afterwards with 
[seff](../faq/how-much-memory-my-job-needs.md)

`seff JOBID` 

If time runs out for a subjob, search for "restart" in the 
[Schrödinger Knowledge Base](https://www.schrodinger.com/support)
for yor module, and/or look again for the options of your driver with
the `-h` flag. Most jobs are restartable, so you don't lose
completed work or used resources.

## Optimal disk usage

The Schrödinger HOSTs in Puhti have not been configured to use
the [NMVE local disk](../../../computing/running/creating-job-scripts/#local-storage),
which is available only on some of the
compute nodes. Since most jobs don't gain speed advantage of NVME disk, you'll
likely queue less, when not asking for it. If your job will require a lot or random I/O,
please contact us at [servicedesk@csc.fi](mailto:servicedesk@csc.fi)
Thus, the only disk available for the jobs is the
same where your input files already are. Hence, it does not make sense
to copy the files to a "temporary" location at the start of the
job.

For a desmond `multisim` workflow you would need to add this set of flags
to the submit script (all in one line):

```bash
-LOCAL -set "stage[1].set_family.md.jlaunch_opt=["\-LOCAL\"]"
```

## Running the Maestro GUI on Puhti

This is *not recommended*. Running the GUI remotely is slow and prone
to glitches. Please run the GUI locally, and only submit the jobs
on Puhti. If this is not possible, and you have to run the GUI on
Puhti, use the [interactive partition](../../computing/running/interactive-usage.md)
and [NoMachine](../../apps/nomachine.md).

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

Maestro has a tool called [postmortem](https://www.schrodinger.com/kb/1692) 
that can be used to create a
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
Also, see above the recommendation to [try with small systems](#how-to-speed-up-simulations) - 
it will also enable you to use the test HOST and avoid queueing.

Also, please have a look at these [instructions to make
support requests](../support-howto.md) that minimise us asking 
for more details in separate emails and thus taking it lonfer for you 
to get the issue solved.

## Recap for Maestro usage on Puhti

* Test your workflow with a small sample first
* Don't run the Maestro GUI on the login node (use `sinteractive -i`)
* Don't specify too many subjobs - an optimal subjob takes 1-24 hours
* Don't specify too many subjobs - there are many researchers using the same license
* Don't run a heavy "driver process" on the login node (if it's heavy use `-DRIVERHOST longrun -SUBHOST serial`)
* Never run anything in parallel on the login node (localhost should not be your only HOST in the script, and it should not have a number bigger than 1
* Submit all jobs from your /scratch area
* If your local computer is Windows, edit \ to / in your script
* Use the same version of Maestro locally and on Puhti
* Use the `-LOCAL` option to minimize unnecessary copying of files
