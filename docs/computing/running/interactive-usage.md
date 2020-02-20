# Interactive usage

Login nodes should be used only for compiling and moving data.
They can also be used for **light** pre- and postprocessing. **Light** means that these
**one-core-jobs** should finish in **minutes** and require **a few GiB** of memory at maximum.

All the other interactive tasks are to be done in compute nodes either via the `sinteractive`
command or explicitly via the batch job system. Puhti has an interactive partition, where each
user can run one job using one core at maximum, but this resource should always be immediately
available without queuing.

`sinteractive` allows running graphical applications, but note that for graphically intensive
applications it is recommended to connect to Puhti with 
[NoMachine](../../support/tutorials/nomachine-usage.md).

## Easy interactive work: sinteractive command

You can request a single core from a compute node simply with `sinteractive`.
This command will open a shell on a compute node and you can use it as your own
laptop without additional Slurm commands for starting jobs or applications.
The default resources cover typical use cases, but you can also request more
from the command line.

_Default and maximum resources for `sinteractive`_
|Resource |Flag to request |Default  |Maximum |
|Time     |--time=HH:MM:SS |24:00:00 |168:00:00|
|Memory   |--mem=<X>       |18G      |50G    |
|Local Disk|--gres:nvme=<X>|100G     |500G    |
|Cores    |-               |1        |1       |
|Partition|--partition=<X> |interative| any   |

In an `sinterative` job the environment variable $TMDPIR (FIXME?) points to the
[NVMe fast local disk](/computing/running/creating-job-scripts/#local-storage).

### Example: Running a notebooks server via sinteractive
FIXME
### Example: RStudio?
FIXME

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

