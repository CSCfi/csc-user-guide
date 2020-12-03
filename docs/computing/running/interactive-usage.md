# Interactive usage

When you login to CSC supercomputers, you end up in one of the login nodes of the computer. These login nodes are shared by all users and they are **not** intended for heavy computing. See our [Usage policy](../overview.md#usage-policy) for details.
If you need to do heavy computing interactively, you should use interactive batch jobs.

In an interactive batch job, a user submits a batch job that starts an interactive shell session in a computing node. For heavy interactive tasks user can also request specific resources (time, memory, cores, disk). You can also use tools with graphical user interfaces in this interactive shell session, but in this case it is recommended that you do the initial connection to a login node of the supercomputer with [NoMachine](../../support/tutorials/nomachine-usage.md) virtual desktop.

Please notice that the interactive batch jobs run in the computing nodes, where the environment differs 
slightly from the login nodes. For example, not all the same text editors are available. Furthermore, when you log out from an interactive batch job, the session with all the processes will be terminated, and data in the job specific `$TMPDIR` area will be removed. 


## Easy interactive work: sinteractive command

Puhti and Mahti have an `interactive` partition which enables immediate access to an interactive batch job session. The easiest way to use this resource is to use the `sinteractive` command:
```text
sinteractive -i
```
The command above asks what computing project will be used and how much resources the job will need. After that it opens a shell session that runs on a compute node. You can use this session as a normal bash shell without additional Slurm commands for starting jobs and applications.

You can define the resource requests in command line too if you don't want to specify them interactively. Note that the _sinteractive_ commands
in Puhti and Mahti are not identical. There is some differences in both command line options and in the way how the command works.


### sinteractive in Puhti

In Puhti, each user can have only one active session open in the `interactive` partition. In the interactive partition you can reserve in maximum 1 core, with max 16 GB of memory, up to 7 days of time, and 160 GB of local scratch space.  GPUs cannot be reserved.

If your requests exceed these limits or you already have a session in the
interactive partition, `sinteractive` can submit the session request to `small` or `gpu`
partitions instead. However, in these cases your session starts queuing just like normal batch job and
you may need to wait some time before the requested resources become available and the interactive session 
starts.

All the `sinterative` sessions are executed in nodes that have [NVMe fast local disk area](/computing/running/creating-job-scripts-puhti/#local-storage) available. The environment variable `$TMPDIR` points to the local disk area of the job. This local disk area has high I/O capacity and thus it is the ideal location for temporary files created by the application. Note however, that this disk area is erased when the interactive batch job session ends.

For example, an interactive session with 8 GiB  of memory, 48 h running time and 100 GiB local scratch using project _project_2001234_
can be launched with command:

```text
sinteractive --account project_2001234 --time 48:00:00 --mem 8000 --tmp 100
```

Available options for `sinteractive` in Puhti are:

| Option        | Function                                                 | Default              |
| ------------- | -------------------------------------------------------- | -------------------- |
| -i, --interactive | Set resource requests for the job interactively       |                      |
| -t, --time    | Run time reservation in minutes or in format d-hh:mm:ss. | 24:00:00             |
| -m, --mem     | Memory reservation in MB.                                | 1000                 |
| -j, --jobname | Job name.                                                | interactive          |
| -c, --cores   | Number of cores.                                         | 1                    |
| -A, --account | Accounting project.                                      |                      |
| -d, --tmp     | Size of job specific $TMPDIR disk (in GiB).             | 32                   |
| -g, --gpu     | Number of GPU:s to reserve (max 4)                       | 0                    |

### sinteractive in Mahti

In Mahti, users can have several interactive batch job sessions in the `interactive` partition. Other partitions don't support interactive batch jobs. Each interactive session can reserve 1-8 cores, but the total number of reserved cores shared with all user sessions cannot exceed 8. Thus a user can have for example 4 interactive sessions with 2 cores or one 8 core session. Each core reserved will provide 1.875 GB of memory and the only way to increase the memory reservation is to increase the number of cores reserved. The maximum memory, provided by 8 cores, is 15 GB.

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





### Example: Running a Jupyter notebook server via sinteractive

You can start a Jupyter notebook server on a Puhti compute node,
and access it with your local web browser. In this case there is no
need to start NoMachine. In the Puhti terminal session, run the command:

```text
sinteractive --account <project> start-jupyter-server
```

This command will start the server, and it will then print out a web
address and a ssh command. Execute the ssh command (copy-paste) in
another linux terminal on your local machine to form a tunnel between
your machine and the compute node. Note that you need to set up
[passwordless access using ssh keys](/computing/connecting/#setting-up-ssh-keys) to do so. After this you can access
the Jupyter server by copy-pasting the web address into your local web browser.

### Example: RStudio Server in sinteractive session

RStudio Server can also be launched on a Puhti compute node and accessed through a local web browser.
The process is similar to starting a Jupyter notebook server:

```text
sinteractive --account <project> --mem 8000 --tmp 100
module load r-env-singularity 
start-rstudio-server
```
For a detailed guide to launching RStudio Server, see our documentation on the [`r-env-singularity module`](../../apps/r-env-singularity.md).

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
