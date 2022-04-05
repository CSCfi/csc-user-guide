# Interactive usage

When you login to CSC supercomputers, you end up in one of the login nodes of the computer. These login nodes are shared by all users and they are **not** intended for heavy computing. See our [Usage policy](../overview.md#usage-policy) for details.
If you need to do heavy computing interactively, you should use interactive batch jobs.

In an interactive batch job, a user submits a batch job that starts an interactive shell session in a computing node. For heavy interactive tasks users can also request specific resources (time, memory, cores, disk). You can also use tools with graphical user interfaces in this interactive shell session, but in this case you need to have enabled X11 forwarding. An even better option for remote graphics is to use the [Puhti web interface](../webinterface/index.md).

Please notice that the interactive batch jobs run in the computing nodes, where the environment differs 
slightly from the login nodes. For example, not all the same text editors are available. Furthermore, when you log out from an interactive batch job, the session with all the processes will be terminated, and data in the job specific `$TMPDIR` and `$LOCAL_SCRATCH` areas will be removed. 


## Easy interactive work: sinteractive command

Puhti and Mahti have an `interactive` partition which enables immediate access to an interactive batch job session. The easiest way to use this resource is to use the `sinteractive` command:
```text
sinteractive -i
```
The command above asks what computing project will be used and how much resources the job will need. After that it opens a shell session that runs on a compute node. You can use this session as a normal bash shell without additional Slurm commands for starting jobs and applications.

You can define the resource requests in command line too if you don't want to specify them interactively. Note that the _sinteractive_ commands
in Puhti and Mahti are not identical. There is some differences in both command line options and in the way how the command works.


### sinteractive in Puhti

In Puhti, each user can have two active sessions open in the `interactive` partition.
In the interactive partition you can reserve in maximum 8 cores, with max 76 GB of memory,
up to 7 days of time, and 720 GB of local scratch space. GPUs cannot be reserved.

If your requests exceed these limits or you already have two sessions in the
interactive partition, `sinteractive` can submit the session request to `small` or `gpu`
partitions instead. However, in these cases your session starts queuing just like normal batch job and
you may need to wait some time before the requested resources become available and the interactive session 
starts.

All the `sinterative` sessions are executed in nodes that have [NVMe fast local disk area](/computing/running/creating-job-scripts-puhti/#local-storage) available. The environment variable `$TMPDIR` points to the local disk area of the job. This local disk area has high I/O capacity and thus it is the ideal location for temporary files created by the application. Note however, that this disk area is erased when the interactive batch job session ends.

For example, an interactive session with 2 cores, 8 GiB  of memory, 48 h running time and 100 GiB local scratch using project _project_2001234_
can be launched with command:

```text
sinteractive --account project_2001234 --cores 2 --time 48:00:00 --mem 8000 --tmp 100
```

Available options for `sinteractive` in Puhti are:

| Option        | Function                                                 | Default              | Max |
| ------------- | -------------------------------------------------------- | -------------------- |-----|
| -i, --interactive | Set resource requests for the job interactively.      |                      | |
| -t, --time    | Run time reservation in minutes or in format d-hh:mm:ss. | 24:00:00             | 7-00:00:00 |
| -m, --mem     | Memory reservation in MB.                                | 2000                 | 76000|
| -j, --jobname | Job name.                                                | interactive          | |
| -c, --cores   | Number of cores.                                         | 1                    | 8 |
| -A, --account | Accounting project.                                      |                      | |
| -d, --tmp     | Size of job specific $TMPDIR disk (in GiB).              | 32                   |720  |
| -g, --gpu     | Number of GPU:s to reserve (max 4)                       | 0                    | 0 |

### sinteractive in Mahti

In Mahti, users can have up to 8 interactive batch job sessions in the `interactive` partition. Other partitions don't support interactive batch jobs. Each interactive session can reserve 1-32 cores, but the total number of reserved cores shared with all user sessions cannot exceed 32. Thus a user can have for example 4 interactive sessions with 8 cores or one 32 core session. Each core reserved will provide 1.875 GB of memory and the only way to increase the memory reservation is to increase the number of cores reserved. The maximum memory, provided by 32 cores, is 60 GB.

For example, an interactive session with 6 cores, 11,25 GiB of memory and 48 h running time using project _project_2001234_
can be launched with command:

```text
sinteractive --account project_2001234 --time 48:00:00 --cores 6
```

Available options for `sinteractive` in Mahti are:

| Option        | Function                                                 | Default              |
| ------------- | -------------------------------------------------------- | -------------------- |
| -i, --interactive | Set resource requests for the job interactively       |                      |
| -t, --time    | Run time reservation in minutes or in format d-hh:mm:ss. | 24:00:00             |
| -j, --jobname | Job name.                                                | interactive          |
| -c, --cores   | Number of cores ( + 1.875 GB of memory/core)             | 2                    |
| -A, --account | Accounting project.                                      |                      |





### Example: Running a Jupyter notebook or RStudio server via sinteractive
See the [Using RStudio or Jupyter notebook tutorial](../../support/tutorials/rstudio-or-jupyter-notebooks.md).

### Example: Running an MPI job in an interactive session

Since the shell started in the interactive session is already a job step in Slurm, more job steps can't be started.
This will disable, e.g. running Gromacs tools, as `gmx_mpi` is a parallel program and normally needs `srun`.
In this case, in the interactive shell, `srun` must be replaced with `orterun -n 1`. Orterun does not know of the
Slurm flags, so it needs to be told how many tasks/threads to use. The following example will run a
[Gromacs](../../apps/gromacs.md) mean square displacement analysis for an existing trajectory.

```bash
sinteractive --account <project>
module load gromacs-env
orterun -n 1 gmx_mpi msd -n index.ndx -f traj.xtc -s topol.tpr
```
To use all requested cores in parallel, you need to add `--oversubscribe`.
E.g. for 4 cores, a parallel interactive job
(launched *from* the interactive session) can be run with

```bash
sinteractive --account <project> -c 4
module load gromacs-env
orterun -n 4 --oversubscribe gmx_mpi mdrun -s topol.tpr
```

## Explicit interactive shell without X11 graphics

If you don't want to use the `sinteractive` wrapper, it's possible
to use Slurm commands explicitly.
Note, as you may need to queue, it's convenient to ask for an email once the resources have been granted. 

```
srun --ntasks=1 --time=00:10:00 --mem=1G --pty \
  --account=<project> --partition=small --mail-type=BEGIN \
   bash
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
   myprog
```

Note, that you can replace `myprog` with `bash`, which will launch a terminal
on the compute node. From that terminal you can launch also graphical applications.
Once the requested time has passed, the application will be
automatically shutdown.
