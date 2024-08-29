# Interactive usage

When you log into a CSC supercomputer, you are connected to one of its login
nodes. Login nodes are shared by all users and are **not** to be used for
heavy processing. [See our usage policy for details](../usage-policy.md). If
you need to run heavy computations interactively, you can use the `interactive`
partitions on Puhti and Mahti.

The `interactive` partition offers fewer resources than other partitions, but
jobs submitted to it have a much higher priority in comparison, so they will
typically spend very little time queueing. The partition can be used for
running [web interface applications](../webinterface/apps.md) and
[batch jobs](getting-started.md), but the most convenient way to use it is via
the [`sinteractive` command](#the-sinteractive-command).

## The `sinteractive` command

`sinteractive` starts a new shell program on a compute node with the resources
specified by the user. Processes can be launched as if you were using your own
device, i.e. it is not necessary or even possible to use Slurm commands like
`srun`. The shell environment differs slightly from that of the login nodes,
e.g. "heavier" text editors like Vim and Emacs are not available, so one must
use Vi or Nano instead.

Since `sinteractive` starts a new shell, any environment variables that are
not set in the user's initialization files need to be defined again manually.
Once the interactive session is finished, you are returned to your original
shell program, and all temporary data written to `$TMPDIR` and `$LOCAL_SCRATCH`
during the session are lost.

While the recommended way to use graphical applications is the
[virtual desktop](../webinterface/desktop.md), it is also possible to do this
in an interactive session launched from the command line
[using X11 forwarding](#starting-an-interactive-application-with-x11-graphics).

The easiest way to use `sinteractive` is running the command with the `-i`
option:

```bash
sinteractive -i
```

When this option is used, the user is prompted for the individual parameters
of the session (runtime, memory, cores, etc.). If you do not want to specify
the resources interactively, you can simply pass them to the command as
arguments. Note that the available options and resources are not identical on
Puhti and Mahti due to differences in hardware.

### `sinteractive` on Puhti

On Puhti, each user can have up to two active sessions on the `interactive`
partition.

If your resource requests exceed the
[limits of the Puhti `interactive` partition](./batch-job-partitions.md#puhti-interactive-partition),
or if you already have two active sessions there, you are offered the option
to submit the job to the `small` or `gpu` partitions instead. In this case,
your job does not benefit from the higher priority of the `interactive`
partition, so you will need to wait some time before the requested resources
become available and the interactive session starts. If you request GPUs using
the `-g` option, your job is automatically submitted to the `gpu` partition.

All sessions started with `sinteractive` are run on nodes that have
[fast local NVMe storage](../disk.md#compute-nodes-with-local-ssd-nvme-disks)
available. This local disk area has high I/O
capacity and is therefore the ideal location for temporary files created by
your processes. Do keep in mind that this disk area is emptied when the
interactive session ends. The `$TMPDIR` and `$LOCAL_SCRATCH` environment
variables point to the local disk area of the job.

To see the command options available on Puhti, run the following while
logged into the system:

```bash
sinteractive --help
```

### `sinteractive` on Mahti

On Mahti, each user can have up to 8 active sessions on the `interactive`
partition. See the
[Mahti `interactive` partition details](batch-job-partitions.md#mahti-interactive-partition)
for information on the available resources. It is also possible to request a
a [GPU slice](./batch-job-partitions.md#gpu-slices) for interactive work by
using the `-g` flag, which submits the job to the `gpusmall` partition. Note
that using a GPU slice restricts the amount of CPU cores and memory that is
available for your job.

As with Puhti, you can see the Mahti-specific command options by running the
following while logged into the system:

```bash
sinteractive --help
```

### Example: Running a Jupyter notebook or RStudio server via `sinteractive`

See the tutorial on
[using RStudio or Jupyter notebooks](../../support/tutorials/rstudio-or-jupyter-notebooks.md).

### Example: Running an MPI job in an interactive session

Since the shell that is started in the interactive session is already a job
step in Slurm, additional job steps cannot be created. This prevents running
e.g. GROMACS tools in the usual way, since `gmx_mpi` is a parallel program and
normally requires using `srun`. In this case, `srun` must be replaced with
`orterun -n 1` in the interactive shell. Orterun does not know of the Slurm
flags, so it needs to be told how many tasks/threads to use. The following
example will run a [GROMACS](../../apps/gromacs.md) mean square displacement
analysis for an existing trajectory:

```bash
sinteractive --account <project>
module load gromacs-env
orterun -n 1 gmx_mpi msd -n index.ndx -f traj.xtc -s topol.tpr
```

To use all requested cores in parallel, you need to add `--oversubscribe`.
E.g. for 4 cores, a parallel interactive job
(launched *from* the interactive session) can be run with:

```bash
sinteractive --account <project> --cores 4
module load gromacs-env
orterun -n 4 --oversubscribe gmx_mpi mdrun -s topol.tpr
```

## Explicit interactive shell without X11 graphics

If you do not want to use the `sinteractive` wrapper, it is also possible to
use Slurm commands explicitly to launch an interactive session. Since you may
need to queue, it is recommended to ask for an email notification once the
resources have been granted.

```bash
srun --ntasks=1 --time=00:10:00 --mem=1G --pty \
     --account=<project> --partition=small --mail-type=BEGIN \
     bash
```

Once the resources are available, you can work normally in the shell. The
Bash prompt shows the name of the compute node:

```bash
[username@r07c02 ~]$
```

Once the requested time has passed, the shell exits automatically.

## Starting an interactive application with X11 graphics

To enable X11 graphics, add `--x11=first` to the command.
The following will start the application `myprog`:

```bash
srun --ntasks=1 --time=00:10:00 --mem=1G --x11=first --pty \
     --account=<project> --partition=small --mail-type=BEGIN \
     myprog
```

Note that you can replace `myprog` with `bash`, which will launch a shell
on the compute node, which you can, in turn, use to launch graphical
applications. Once the requested time has passed, the application is
terminated automatically.
