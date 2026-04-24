# Roihu interactive usage

!!! warning "Puhti and Mahti documentation on a separate page!"
    This page contains information on interactive usage on Roihu. 
    For information on Puhti and Mahti, see: 
    [Roihu interactive usage](./interactive-usage.md).

When you log into a CSC supercomputer, you are connected to one of its login
nodes. Login nodes are shared by all users and are **not** to be used for
heavy processing. [See our usage policy for details](../usage-policy.md). If
you need to run heavy computations interactively, you can use the `interactive` 
and `gpuinteractive` partitions.

These partitions offer fewer resources than other partitions, but
jobs submitted to them have a much higher priority in comparison, so they will
typically spend very little time queueing. The partitions can be used for
running [web interface applications](../webinterface/apps.md) and
[batch jobs](getting-started.md), but the most convenient way to use them is via
the [`salloc` command](#the-salloc-command).

## The `salloc` command

!!! info "`sinteractive` command has been deprecated on Roihu."

On Roihu the `salloc` command starts a new shell program on a compute node
with the resources specified by the user. Processes can be launched as if you
were using your own device, i.e. it is not necessary or even possible to use
Slurm commands like `srun`.

Under the hood `salloc` starts a new shell using `srun` with these default 
flags: `--interactive --preserve-env`. As such, any environmental variables 
thar are present in the launching shell should be inheritted by the interactive 
job. Once the interactive session is finished, you are returned to your original
shell program, and all temporary data written to `$TMPDIR` or any attached 
"burst buffer" storage (see [disaggregated storage](../roihu-disk.md)) are lost.

While the recommended way to use graphical applications is the
[virtual desktop](../webinterface/desktop.md), it is also possible to do this
in an interactive session launched from the command line
[using X11 forwarding](#starting-an-interactive-application-with-x11-graphics).

The easiest way to use `salloc` is by running the command:

```bash
salloc --account <project>
```

There are two interactive partitions available on Roihu; `interactive` for CPU 
resources and `gpuinteractive` for GPU resources. See the
[Roihu `interactive` partition details](./batch-job-partitions.md#roihu-partitions)
for information on the available resources. The Roihu `gpuinteractive` partition 
features GH200 superchips that are divided into a total of 48 smaller slices that 
have one-seventh of the compute capacity and one-eighth of the GPU memory capacity 
(12 GiB) of a full GH200 superchip.

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
salloc --account <project>
module load gromacs-env
orterun -n 1 gmx_mpi msd -n index.ndx -f traj.xtc -s topol.tpr
```

To use all requested cores in parallel, you need to add `--oversubscribe`.
E.g. for 4 cores, a parallel interactive job
(launched *from* the interactive session) can be run with:

```bash
salloc --account <project> --cores 4
module load gromacs-env
orterun -n 4 --oversubscribe gmx_mpi mdrun -s topol.tpr
```

## Explicit interactive shell without X11 graphics

If you do not want to use `salloc`, it is also possible to
use `srun` explicitly to launch an interactive session. Since you may
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
