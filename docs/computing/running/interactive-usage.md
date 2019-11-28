# Interactive usage

Login nodes should be used only for compiling, moving data, and
**light** pre- and postprocessing. **Light** means that these
**one-core-jobs** should finish in **minutes** and require **a few GiB** of memory at maximum.

All the other interactive tasks are to be done in compute nodes via
the batch job system.

Note that for graphically intensive applications it is recommended
to connect to Puhti with [NoMachine](../../support/tutorials/nomachine-usage.md).

## Starting interactive shell

A bash shell can be started by giving this directly on the command
line instead via a job script file and `sbatch`.
Note, as you may need to queue, it's convenient to ask for an email once the resources have been granted. 

```
srun --ntasks=1 --time=00:10:00 --mem=1G --x11=first --pty \
  --account=<project> --partition=small --mail-type=BEGIN \
  --mail-user=<your email address> bash
```

Once the resource has been granted, one can work normally in the shell
and launch also graphical applications. The bash promp will show the
name of the compute node:

```bash
[csc-username@r07c02 ~]$
```

Once the requested time has passed, the shell exits automatically.

## Starting interactive application with X11 graphics

In order to start application `myprog`, give this directly on the
command line instead via a job script file and `sbatch`.
Note, as you may need to queue, it's convenient to ask for an email once the resources have been granted. 

```
srun --ntasks=1 --time=00:10:00 --mem=1G --x11=first --pty \
  --account=<project> --partition=small --mail-type=BEGIN \
  --mail-user=<your email address> myprog
```

Once the requested time has passed, the application will be
automatically shutdown.



