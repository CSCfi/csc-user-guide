# Interactive usage

When you login to CSC supercomputers, you end up to one of the login nodes of the computer. These login nodes are shared by all users, and they should be used only for compiling, manging batch jobs and moving data. Login nodes can be used for **light** pre- and postprocessing, but they are not intended for heavy computing.  **Light** means that these
**one-core-jobs** should finish in **minutes** and require **a few GiB** of memory at maximum.
All the other tasks are to be done in compute nodes either as normal batch jobs or as _interactive batch_ jobs.

In intercative batch job, user submits a batch job, that provides interactive shell session running in the
requested computing resources in the computing nodes. Heavy interactive tasks can now be run in the limits of requested resources (time, memory, cores, disk). You can also use tools with craphical user interfaces in interactive batch jobs, but in that case it is recommended that you do the initial connection to a login node of the supercomputer with [NoMachine](../../support/tutorials/nomachine-usage.md) virtual desktop.

You should notice that interactive bach jobs run in the computing nodes, where the environment differs 
slightly from the login nodes. For example, not all the text editors are available. Futher, when you log out from an interactive batch job, the session, including all the processes running in the session and data in the node spcific local scratch area, will be terminated. 


## Easy interactive work: sinteractive command

Puhti has an _interactive_ partition to enable immediate access to an interactive batch job session. The easiest way to use this resource is to execute commmand:

```text
sinteractive -p <project_name> 
```
This command will open a shell on a compute node and you can use it as normal bash shell without additional Slurm commands for starting jobs and applications.

_sinteractive options_

|Option| Function | Default |
| --- | --- | --- |
|-t, --time | Run time reservation in minutes or in format d-hh:mm:ss. | 24:00:00 |
|-m, --mem | Memory reservation in MB. | 1000 |
|-j, --jobname | Job name. | interactive |
|-c, --cores | Number of cores. |  1 |
|-p, --project | Accounting project.|  $CSC_PRIMARY_PROJECT |
|-d, --tmp  | Size of job specifinc /tmp or $LOCAL_SCRATCH disk (in GiB). | 32 |
|-g, --gpu  | Number of GPU:s to reserve (max 2) | 0 |

The default sinteractive resources cover typical use cases, but you can also request more
from the command line. For example to have an interactive session with 8 GiB 
of memory, 48 h runnig time and 100 GiB local scratch using project _project_2011234_
could be lauched with command:

```text
sinteractive -p project_2011234 --time 48:00:00 --mem 8000 --tmp 100
```

Note that each user can have only one active session open in the _interactive_ partition. Furher
in interactive partition you can reserve in maximum 1 core, 16 GB of 
memory, 7 days of time, 160 GB of local scratch space and 0 gpus.

If your requests exceed these limits or you already have a session in
intercative partition, then sinteractive can submit the session request to _small_ or _gpu_
partitions in stead. However, in these cases your session will start queueing just like a normal batch jobs.
Thus you may need wait some time before the requested resources become available and the interactive session 
starts.

In an `sinterative` job the environment variable $TMDPIR (FIXME?) points to the
[NVMe fast local disk](/computing/running/creating-job-scripts/#local-storage).

### Example: Running a notebooks server via sinteractive
FIXME
### Example: RStudio in sinteractive session

Open connection to Puhti with NoMachine.
In the Puhti terminal session, run commands:

```text
sinteractive -p <project> --mem 8000 --tmp 100
module load r-env 
module load rstudio
export XDG_RUNTIME_DIR=$LOCAL_SCRATCH
rstudio
```


## Explicit interactive shell without X11 graphics

If you don't want to use the `sinteractive`wrapper, it's possible
to use Slurm commands explicitly.
Note, as you may need to queue, it's convenient to ask for an email once the resources have been granted. 

```
srun --ntasks=1 --time=00:10:00 --mem=1G --pty \
  --account=<project> --partition=small --mail-type=BEGIN \
  --mail-user=<your email address> bash
```

Once the resource has been granted, you can work normally in the shell.
The bash prompt will show the
name of the compute node:

```bash
[csc-username@r07c02 ~]$
```

Once the requested time has passed, the shell exits automatically.

## Starting an interactive application with X11 graphics

To enable X11 graphics, add `--x11=first` to the command.
The following will start the application `myprog`: 

```
srun --ntasks=1 --time=00:10:00 --mem=1G --x11=first --pty \
  --account=<project> --partition=small --mail-type=BEGIN \
  --mail-user=<your email address> myprog
```

Note, that you can replace `myprog` with `bash`, which will launch a terminal
on the compute node. From that terminal you can launch also graphical applications.
Once the requested time has passed, the application will be
automatically shutdown.

