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
shown in [this video](../../apps/maestro.md) on our main Maestro page.

Once the files have been copied to Puhti, the job is submitted to
a compute node(s) by running the `job_name.sh` script
written out by Maestro. It will formulate the task(s) as Slurm
batch job(s) and ask resources according to the selected HOST in
your `schrodinger.hosts` file on your Puhti home directory.

Another, more advanced version is to use e.g. the `pipeline` tool
which allows you to bypass some of the Schrödinger jobcontrol
machinery, but requires you to write the job script yourself.
This may be useful, in case some of your subjobs terminate
unexpectedly. In this case, please make note of those JobIds
and contact us at servicedesk@csc.fi

This article explains some implementation details on Puhti
and helps setting up efficient simulation workflows.

## Maestro `schrodinger.hosts` file

This file specifies the resources your jobs can get either locally 
or from the queuing system. To use the recommended procedure 
you need to edit the local (on your computer) `schrodinger.hosts` file to
include the same HOSTs that you want to use on Puhti. On Windows, this will
require admin privileges.

On Puhti, Maestro complains about the location on this file, but ignore it, it's ok.
This file must match the version of Maestro you are using (locally and in
Puhti). Version match is checked at each `module load` event.
The file is created by a script (echoed on your screen when
you give `module load maestro`) that you need to run if the file does not
exist, or if the versions don't match.

As the script requests, select the computing project that will be used
for CPU usage and scratch storage. You can find the actual Slurm options
on the HOST descriptions in schrodinger.hosts file. If your jobs require
something, that's not present in the file, you can edit it.

On Puhti you can take a look at the `schrodinger.hosts` file with:

```bash
more $HOME/schrodinger.hosts
```

On your local computer this file will be in the Maestro installation direcctory,
e.g. on Windows in `C:\Program Files\Schrodinger-version\schrodinger.hosts`

After the longish header and the `localhost` entry , you should see the 
Puhti HOST entries as something like:
```bash
name:        test
queue:       SLURM2.1
qargs:       -p test -t 00:10:00 --mem-per-cpu=2000 --account=project_2042424
host:        puhti-login1.csc.fi
processors:  4
```

For example, this HOST entry, available for Schrödinger jobs as  _test_ (from `name: test`),
 will use the Slurm partition _test_ (from `-p test`), allocate a maximum of 10 minutes of time, 2 GB
of memory and consume resources from Project_2042424. If you need different
resources you can edit this file, e.g. by adding a new entry. 
The requests must be within the [partition limits](../../computing/running/batch-job-partitions.md).

If your `schrodinger.hosts` file **on Puhti** does not have the --account=**something** defined
delete the file and rerun the script to create it (`module load maestro` will
print out the path to the script, copy/paste it on the command line).
You don't need to have the `--account=` option set in your **local**
`schrodinger.hosts` file. In your local file, it's enough that the different HOST
entries exist (and the gpu-ones have GPU's specified). 

Note that the HOST entries and Slurm partitions (or queues) are two
different things. The HOST entries define resources using Slurm partitions.

## How to speed up simulations?

All other Maestro modules run serial jobs, except Jaguar and Quantum Espresso, which can run
"real" parallel jobs. Don't choose a "parallel" HOST for any other job type.
Instead of MPI-parallel jobs, Maestro modules typically
split the workload into multiple parts, each of which can be run independent
of the others. The Maestro help pages have an
excellent section on this topic. Please have a look (you'll find it like this:
Click the "help" button in the "run settings dialog", then in the first chapter
click the link named "Running Distributed Schrödinger Jobs".

Typically, the workload processes a lot of molecules. If you have enough
molecules, you can split the full set into smaller sets, and process each
of the sets as a separate job. Since this is typical, the Maestro modules have
easy-to-use options to define the number of (sub)jobs. However, you must know
in advance how many (sub)jobs to launch. In principle, this requires 
knowing how long one molecule takes, or testing for each different use case.

!!! Note
    When you start with a new kind of work. Don't **try** if you got the
    syntax right with 1000000 molecules and 1000 subjobs. Try with 50
    molecules and 2 subjobs. Learn how long it takes per molecule,
    confirm your submit syntax is correct, adjust
    your parameters if needed and then scale up.

If you're using the GUI to set up the job script, specify how many (sub)jobs
(processors) you want to use. (You can easily edit this later in the submit
script if you change your mind)

The 'default' submit script will work "as is" for small jobs. Just make
sure you don't ask for too many (sub)jobs. Each subjob should take longer
than, say one hour to complete, for very large jobs rather 24 hours.
Running a lot of very short jobs is inefficient in many ways.
For large workflows, you'll need to edit it, see below.

## Additional flags for Maestro modules

Different modules have different options. You can set some of them in
the GUI, but you may find more options with the `-h` flag:

```bash
glide -h
```

, where `glide` would be the Maestro module you want to run, like
`qsite`, `pipeline`, `bmin`, `ligprep`, etc.    

The Maestro help has a nice summary of the different options for
different modules: in Maestro help select: "Installation and jobs"
-> "Running Distributed Schrödinger Jobs".

### Simple HOST selection

For jobs that finish within about two days, and 10 subjobs just use:

```
-HOST normal_72h:10
```

or if they all finish within 7 days, use:
```
-HOST longrun:10
```

If you have a workflow that will last longer, read on.

### Advanced HOST selection

The general aim is to have the "driver process" running on a "HOST"
that will be alive for the whole duration of the workflow. Good
options are _interactive_ and _longrun_, if you estimate the complete
workflow to take more than 3 days (queuing included). A "driver process"
that is not using a lot of CPU is also allowed on a login node, but
a subjob is not. Never submit jobs on Puhti _login nodes_ with
`-HOST localhost`. (It's ok if you create your own batch script _and_
use localhost on a computenode, but that's for special cases only 
and not discussed on this page.)

Set the "driver" or "master" to run on a HOST that allows for long
run times (if it's a big calculation). The driver needs to be alive
for the whole duration of the workflow (otherwise, your subjob
likely ends up fizzled). You can use "interactive"
which allows for 7 days for one core. If you need to run multiple
workflows at the same time, choose "longrun" for the next drivers.
In both cases select some "normal" HOST 
(i.e. "small" Slurm partition) for the (sub)jobs. Suitable
splitting will reduce your queuing time. Asking for the longrun HOST "just
in case" is not dangerous, but may lead to unnecessary queuing.

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
`-HOST "normal_72h:10"` to `-HOST "longrun:1 normal_72h:9"`
or e.g.
`-HOST "normal_72h"` to `-HOST "interactive:1 normal_72h:9"`

Note, that you can have only one single core job running in the
interactive HOST. 

Desmond jobs can have the `-HOST gpu` flag as set by the GUI, but
Windows users need to change the forward slash "/" to backward slash
"\" in the binary name.

### Authoritative job control instructions from the manual

A more detailed discussion for advanced jobs can be found in Maestro help via
(from the GUI or via login in [Schrödinger website](https://www.schrodinger.com/documentation)): 

*  "Job Control Guide" -> "Running jobs" -> "Running Jobs from the Command Line" -> 
"The HOST, DRIVERHOST, and SUBHOST Options" 

and a table for driver process conventions from 

* "Installation and Jobs" -> "Running Distributed Schrödinger Jobs"


## Set number of subjobs or molecules per subjob

!!! Tip
    If you don't know how long your full workflow will take, don't ask
    for more than 10 subjobs and/or `NJOBS`. More is not always better.
    If you have very large cases, don't exceed 50 simultaneous (sub)jobs.

As an example, the "run settings dialog" of `Glide` offers three options:

* Recommended number of subjobs
* Exactly (fill in here) subjobs
* Subjobs with no more than (fill in here) ligands each

Aim for such numbers that an average subjob takes 2-24 hours to run, so
that the overhead per subjob remains small, but not too long so that the
job parallelizes efficiently i.e. you get your results quikcly and each 
subjob has time to finish (and that the master job has time to finish).
At least avoid subjobs that complete faster than 15 minutes. You can check 
subjob duration afterwards with [seff](../faq/how-much-memory-my-job-needs.md)
and use this info in your new jobs:

`seff JOBID` 

If time runs out for a subjob, search for "restart" in the 
[Schrödinger Knowledge Base](https://www.schrodinger.com/support)
for yor module, and/or look again for the options of your driver with
the `-h` flag. Most jobs are restartable, so you don't lose
completed work or used resources.

If you choose too many subjobs, Maestro will get confused on the Slurm
messages and sorting out the issue can be difficult. Also, running too
many subjobs at a time can lead to the [license running out](#availability-of-licenses),
and waiting in the queue have been in for nothing.

## Optimal disk usage

The Schrödinger HOSTs in Puhti have not been configured to use
the [NMVE local disk](../../../computing/running/creating-job-scripts-puhti/#local-storage),
which is available only on some of the
compute nodes. Since most jobs don't gain speed advantage of NVME disk, you'll
likely queue less, when not asking for it. If your job will require a lot or random I/O,
please contact us at [servicedesk@csc.fi](mailto:servicedesk@csc.fi) on how to request it.
The only disk available for the jobs is the
same where your input files already are. Hence, it does not make sense
to copy the files to a "temporary" location at the start of the
job. However, at the moment there doesn't seem to be a way to prevent that
in latest versions (2020.1 onwards).

## Copying files to and from local computer

There is a [detailed tutorial](/data/moving/) on how to accomplish
this. Below, is an efficient alternative in the command line, which
works even in Windows power shell:

In Windows, start the Power Shell by searching for it in the bottom left menu.
In Linux or Mac, open a terminal.  `cd` to the
directory that has the _directory_ of input files recently written out by the GUI
(here named `glide-dock_1`)

`scp -r glide-dock_1 your-username@puhti.csc.fi:/scratch/project_123456/`

will copy the whole directory (note `-r`) into your Puhti scratch folder.
In a terminal in Puhti, run the job, and once it has completed, you can copy it back
(give the command on your local computer):

`scp -r your-username@puhti.csc.fi:/scratch/project_123456/glide-dock_1 .`

You might be interested in some [additional ssh tips](../../../computing/connecting/#setting-up-ssh-keys),
which will release you from typing your password every time.

## Running the Maestro GUI on Puhti

This is **not recommended**. Running the GUI remotely is slow and prone
to glitches. Please run the GUI locally, and only submit the jobs
(run the script) on Puhti. If this is not possible, and you _have_ _to_ run the GUI on
Puhti, use the [interactive partition](../../computing/running/interactive-usage.md)
and [NoMachine](../../apps/nomachine.md).

```bash
module load maestro
sinteractive -i
maestro
```

## Availability of licenses

The CSC Maestro license has a fixed amount of tokens that are available for everyone. 
First, Maestro uses _module specific_ tokens, of which there are many for each module. 
If they run out, then more jobs (of that same type) can be run with "general tokens", 
but when they run out, no more jobs of that type (or any new jobs which need a 
general token) can't be run by anyone. Therefore, this should be avoided. 
Once a job ends, the tokens are released, and are available for everyone.

You can check the currently available licenses with:
```
$SCHRODINGER/utilities/licutil -avail
```
and currently used licenses with:
```
$SCHRODINGER/utilities/licutil -used
```

Note, that some Maestro tools or workflows use multiple modules and hence licenses
or tokens from multiple modules. Typically, one running instance of a module (a job or
a subjob) requires several tokens. For example, Desmond and Glide jobs take 8 tokes each.

CPU time is a different resource and has nothing to do with license tokens.
When CPU-time runs out, you or your project manager can apply for more via [my.csc.fi](https://my.csc.fi).

## Fizzled jobs

Sometimes the jobs are launched but don't finish. The state of the job as
reported by `jobcontrol`, see below, is _fizzled_. This might be due to a
number of reasons but cleaning up and restarting the jobcontrol service
might help. When you don't have any Maestro jobs running (in Puhti), give:

```bash
$SCHRODINGER/utilities/jserver -cleanall
$SCHRODINGER/utilities/jserver -shutdown
```

Another reason is too many simultaeous jobs. Please have a look at the
error files for suggestions, and if this is the case, ask for less subjobs.

## Run a test job to help problem diagnostics

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
     * Note, that you can have only one job running at a time in the `test` and `interactive` partitions.
* Don't run the Maestro GUI on the login node (use `sinteractive -i` if you _must_ run the GUI on Puhti)
* Don't specify too many subjobs - an optimal subjob takes 2-24 hours
* Don't specify too many subjobs - there are many researchers using the same license
* Don't run a heavy "driver process" on the login node (if it's heavy, for 10 simultaneous jobs use `-HOST "longrun:1 normal_72h:9"`)
* Never run anything in parallel on the login node (localhost should not be in your script)
* Submit all jobs from your /scratch area
* If your local computer is Windows, edit `\` to `/` in your script
* Use the same version of Maestro locally and on Puhti

If you have suggestions on how to improve this text, e.g. to give examples of efficient workflows,
fork a copy (top right pen icon), edit and propose merge, or send your suggestion to servicedesk@csc.fi.
