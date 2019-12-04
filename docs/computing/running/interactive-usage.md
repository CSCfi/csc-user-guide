# Interactive usage

Login nodes should be used only for compiling, moving data, and
**light** pre- and postprocessing. **Light** means that these
**one-core-jobs** should finish in **minutes** and require **a few GiB** of memory at maximum.

All the other interactive tasks are to be done in compute nodes via
the batch job system.

Note, that for graphically intensive applications it is recommended
to connect to Puhti with [NoMachine](../../support/tutorials/nomachine-usage.md).

## Starting an interactive shell without X11 graphics

A bash shell can be started directly from the command
line with `srun` instead via a job script file and `sbatch`.
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

