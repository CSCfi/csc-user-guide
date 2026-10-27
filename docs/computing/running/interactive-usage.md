# Interactive usage

When you log into a CSC supercomputer, you are connected to one of its login
nodes. Login nodes are shared by all users and are **not** to be used for
heavy processing. [See our usage policy for details](../usage-policy.md). If
you need to run heavy computations interactively, you can use the `interactive`
partitions on Roihu.

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
of the session (runtime, cores, etc.). If you do not want to specify
the resources interactively, you can simply pass them to the command as
arguments.

### `sinteractive` on Roihu

There are two interactive partitions available on Roihu; `interactive` for CPU 
resources and `gpuinteractive` for GPU resources. See the
[Roihu `interactive` partition details](./batch-job-partitions.md#roihu-partitions)
for information on the available resources.

Once GPU slicing is implemented, the GH200 GPUs in the `gpuinteractive` partition
will be divided into smaller Multi-Instance GPU (MIG) slices. Each slice will provide
one-seventh of the GPU compute capacity and one-eighth of the GPU memory capacity
of a full GH200 GPU, giving each slice 12 GiB of GPU memory. With two nodes, four
GPUs per node, and up to seven slices per GPU, the partition can provide up to
56 GPU slices in total.

`sinteractive` selects the partition from your request. On the CPU login node
(`roihu-cpu.csc.fi`), it starts a session on the `interactive` partition by
default, or on the `gpuinteractive` partition if you add the `-g` option. On the
GPU login node (`roihu-gpu.csc.fi`), it always starts a GPU session.

!!! info "GPU sessions started from `roihu-cpu.csc.fi` get a fresh environment"
     The CPU nodes are x86 and the GPU nodes are ARM, so software loaded on the CPU
     login node does not work on the GPU nodes. When you start a GPU session from
     `roihu-cpu.csc.fi`, `sinteractive` therefore starts it with a fresh login
     environment. Modules you have loaded on the login node are not carried over,
     so load them again in the session. If you want the session to inherit your
     login node environment, start GPU sessions from `roihu-gpu.csc.fi` instead. See
     [submitting jobs across architectures](submitting-jobs-across-architectures.md).

!!! info "`gpuinteractive` currently gives full GPUs"
     The GPU slicing in the `gpuinteractive` partition is not yet implemented, so
     users are currently allocated a full GPU when using sinteractive on Roihu-GPU.

To see the command options available on Roihu, run the following while
logged into the system:

```bash
sinteractive --help
```

Note that memory can not be specified in a sinteractive session, and
you are allocated 2 GiB memory per each reserved CPU on Roihu-CPU.
Only way to get extra memory in your job is to increase the amount of resources you request.

GPU sessions always get 212 GiB of memory.

To reserve fast [disaggregated storage](../disk.md#disaggregated-storage) for the
session, give the amount in GB with the `-d` (`--tmp`) option, up to 2048 GB. The
storage is mounted at `/sbf/data`:

```bash
sinteractive --account <project> --cores 4 -d 100
```

Copy any results you need from `/sbf/data` before the session ends.

### Example: Running a Jupyter notebook or RStudio server via `sinteractive`

See the tutorial on
[using RStudio or Jupyter notebooks](../../support/tutorials/rstudio-or-jupyter-notebooks.md).

### Example: Running an MPI job in an interactive session

Since the shell that is started in the interactive session is already a job
step in Slurm, additional job steps cannot be created. This prevents running
e.g. GROMACS tools in the usual way, since `gmx_mpi` is a parallel program and
normally requires using `srun`. In this case, `srun` must be replaced with
`prterun -n 1` in the interactive shell. Prterun does not know of the Slurm
flags, so it needs to be told how many tasks/threads to use. The following
example will run a [GROMACS](../../apps/gromacs.md) mean square displacement
analysis for an existing trajectory:

```bash
sinteractive --account <project>
module load gromacs-env
prterun -n 1 gmx_mpi msd -n index.ndx -f traj.xtc -s topol.tpr
```

To use all requested cores in parallel, you need to add `--oversubscribe`.
E.g. for 4 cores, a parallel interactive job
(launched *from* the interactive session) can be run with:

```bash
sinteractive --account <project> --cores 4
module load gromacs-env
prterun -n 4 --oversubscribe gmx_mpi mdrun -s topol.tpr
```

## Connecting to a compute node of a running job

Sometimes (e.g. for debugging purposes) it is useful to login to a compute 
node where a Slurm job is currently running. Bash shell can be started in the master
node of a job (i.e. the first node in your allocation and the one on which 
your batch script is executed) as follows:
```bash
srun --jobid=<jobid> --overlap --pty bash
```
(`--overlap` allows to run multiple job steps at the same time, and `--pty` enables normal
terminal behaviour).
For jobs spanning multiple nodes it is also possible to connect to a specific
node with the `--nodelist=` option:
```bash
srun --jobid=<jobid> --overlap --nodelist=rcXXXX --pty bash
```
where `rcXXXX` is the name of a node as shown e.g. by the `squeue` command.
(Note that the format of the node names varies between different systems).


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
[username@rc4105 ~]$
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
