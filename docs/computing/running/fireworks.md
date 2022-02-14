# FireWorks workflow tool

[FireWorks](https://materialsproject.github.io/fireworks/) is a free, open-source tool for defining, managing and executing workflows with multiple steps and potentially complex dependencies. Workflows are flexibly defined using YAML, JSON or through a Python API and stored in a MongoDB database. This page describes how to define and execute FireWorks workflows in CSC's computing environment using a MongoDB running in the Rahti container cloud.

## Installing FireWorks

FireWorks is easy to install. We recommend using `pip` to install FireWorks, either in a virtual environment or to your Python user install directory. For further instructions, see [how to install Python packages to existing modules](../../apps/python#installing-python-packages-to-existing-modules.md).

## Setting up MongoDB in Rahti

The process of setting up and connecting to a MongoDB database in Rahti is detailed in a separate tutorial, see [Accessing databases on Rahti from CSC supercomputers](../../cloud/rahti/tutorials/connect-database-hpc.md).

## Defining and executing workflows with FireWorks

The basic components of FireWorks are the 

- LaunchPad (manages workflows and metadata)
- FireTask (computing job to be performed)
- Firework (list of multiple FireTasks)
- Workflow (set of Fireworks including their dependencies and metadata)

A FireWorker (e.g. your laptop or in this case either of CSC's supercomputers) fetches a workflow from the LaunchPad and executes it. To appropriately run FireWorks in CSC's computing environment, you need to additionally configure a QueueAdapter for running jobs through the queueing system. The content of the files used to configure these is described below.

### Step 1. Setting up the LaunchPad

!!! Note
    This page focuses on the usage of YAML files and the FireWorks command-line interface to define and execute workflows. For instructions on using the FireWorks Python API, see the [official FireWorks documentation](https://materialsproject.github.io/fireworks/).

Before configuring the LaunchPad, make sure that you have opened a connection to your MongoDB database in Rahti using WebSocat as outlined in [Accessing databases on Rahti from CSC supercomputers](../../cloud/rahti/tutorials/connect-database-hpc.md). Note that `websocat` should be launched in an interactive session to avoid stressing the login nodes. With the obtained target port, database username and password, run `lpad init` to interactively configure the LaunchPad:

```
$ lpad init

Please supply the following configuration values
(press Enter if you want to accept the defaults)

Enter host parameter. (default: localhost). Example: 'localhost' or 'mongodb+srv://CLUSTERNAME.mongodb.net': localhost
Enter port parameter. (default: 27017). : <target port>
Enter name parameter. (default: fireworks). Database under which to store the fireworks collections: <database name>
Enter username parameter. (default: None). Username for MongoDB authentication: <username>
Enter password parameter. (default: None). Password for MongoDB authentication: <password>
Enter ssl_ca_file parameter. (default: None). Path to any client certificate to be used for Mongodb connection: None
Enter authsource parameter. (default: None). Database used for authentication, if not connection db. e.g., for MongoDB Atlas this is sometimes 'admin'.: None

Configuration written to my_launchpad.yaml!
```

!!! Note
    Upon configuration, WebSocat may complain `websocat: Connection reset by peer (os error 104)`. This warning is due to minor timing issues based on the Python global interpreter lock (GIL) and can be safely ignored.

### Step 2. Setting up the QueueAdapter for submission through SLURM

To run FireWorks through the batch queue system a file `my_qadapter.yaml` is required where the queue parameters and any commands to be run prior to or after the workflow (e.g. module loads, export environment variables) are written. An example `my_qadapater.yaml` file compatible with Puhti is provided below

```yaml
_fw_name: CommonAdapter
_fw_q_type: SLURM
rocket_launch: rlaunch multi 1
nodes: 1
cpus_per_task: 1
ntasks_per_node: 40
mem_per_cpu: 1000
walltime: '00:05:00'
queue: small
account: <billing project>
job_name: example
pre_rocket: |
         module load <my module>
         export PATH=$PATH:/path/to/websocat
         websocat -b tcp-l:127.0.0.1:<port> wss://websocat-<database name>.rahtiapp.fi -E &
post_rocket: null
```

In addition to queue parameters (resource requests, billing project), the QueueAdapter contains the `rocket_launch` key which specifies how the Fireworks should be launched within the batch job (this will be explained further in [Step 3](fireworks.md#step-3-executing-a-fireworks-workflow)). Additionally, the batch queue system (SLURM) is specified with the `_fw_q_type` key, and any commands to be run before and/or after the workflow are provided using the `pre_rocket` and `post_rocket` keys.

!!! Note
    To open a TCP tunnel to your MongoDB in Rahti from the compute side, `websocat` should in addition to the interactive session also be launched in the `pre_rocket`. Here, the previously obtained target port can be used. See [Accessing databases on Rahti from CSC supercomputers](../../cloud/rahti/tutorials/connect-database-hpc.md#step-2-running-websocat-on-csc-supercomputers) for further details.

For all possible SLURM flags that can be specified in the QueueAdapter, see the [SLURM template file](https://github.com/materialsproject/fireworks/blob/main/fireworks/user_objects/queue_adapters/SLURM_template.txt) distributed with FireWorks. Note the usage of underscores instead of dashes compared to the common SLURM options, e.g. `cpus_per_task` vs. `--cpus-per-task`, as well as the keys `walltime` and `queue` in contrast to `time` and `partition` used by SLURM. If the existing SLURM template does not suit your needs, please consult the [official FireWorks documentation on programming custom QueueAdapters](https://materialsproject.github.io/fireworks/qadapter_programming.html).

### Step 3. Defining and executing a simple FireWorks workflow

A FireTask describes the computation to be performed and combining multiple FireTasks yields Fireworks and Workflows. Similar to the LaunchPad and QueueAdapter, these are specified using YAML files. A simple `hello_wf.yaml` example is provided below.

```yaml
fws:
- fw_id: 1
  spec:
    _tasks:
    - _fw_name: ScriptTask
      script: srun /path/to/hello_mpi.x >> first-hello.out
    - _fw_name: FileTransferTask
      files:
      - src: first-hello.out
        dest: $HOME/first-hello.out
      mode: move
- fw_id: 2
  spec:
    _tasks:
    - _fw_name: ScriptTask
      script: srun /path/to/hello_mpi.x >> second-hello.out
    - _fw_name: FileTransferTask
      files:
      - src: second-hello.out
        dest: $HOME/second-hello.out
      mode: move
links:
  1:
  - 2
metadata: {}
```

This toy workflow demonstrates the usage of the built-in `ScriptTask` FireTask to execute an [MPI parallelized `hello_mpi.x` program](https://a3s.fi/hello_mpi.x/hello_mpi.x) through the shell. After this, the output is moved to the user's home directory using a `FileTransferTask`. For illustrative purposes, the Workflow is composed of two identical Fireworks with these two FireTasks. A dependence is defined using the `links` keyword so that the second Firework is launched only after the first one has completed. For a more in depth description on how to design FireWorks workflows, see the official FireWorks documentation.

The steps to execute this example workflow through the batch queue system consist of resetting the LaunchPad, adding the workflow YAML file and, finally, launching the workflow.

```bash
$ lpad reset
Are you sure? This will RESET 1 workflows and all data. (Y/N)
2022-02-14 11:42:59,323 INFO Performing db tune-up
2022-02-14 11:42:59,496 INFO LaunchPad was RESET.

$ lpad add hello_wf.yaml
2022-02-14 11:43:32,144 INFO Added a workflow. id_map: {1: 1, 2: 2}

$ qlaunch singleshot
2022-02-14 11:44:09,835 INFO moving to launch_dir /path/to/launch_dir
2022-02-14 11:44:09,847 INFO submitting queue script
```

!!! Note
    The `qlaunch` command is used to launch the workflow through the batch queue system instead of the basic `rlaunch` command that is normally used in absence of a batch queue system. However, `rlaunch` is still used inside the `my_qadapter.yaml` file where FireWorks is instructed how the workflow should be run *within* the batch job. In the above case, the `multi 1` option is used to run a single parallel job using all the requested resources. For further details on running parallel jobs using FireWorks, see the [official documenation on the multi job launcher](https://materialsproject.github.io/fireworks/multi_job.html).

!!! Note
    If not using the default names `my_launchpad.yaml` and `my_qadapter.yaml` for the LaunchPad and QueueAdapter files, you need to specify the file names using the `-l` and `-q` flags of the `qlaunch` and `rlaunch` (only `-l`) commands. If the files are neither in the current working directory, the full paths should be given or a configuration directory specified with the `-c` flag. A good idea is also to leverage a `FW_config.yaml` configuration file in which several default parameters can be set. The official FireWorks documentation gives further instructions on [how to modify the FW config file](https://materialsproject.github.io/fireworks/config_tutorial.html).

Based on the content of the `my_qadapter.yaml` file, FireWorks creates a submission script `FW_submit.script` and automatically submits it when `qlaunch` is run. You will see that the job has been submitted to the queue, and using the `lpad get_fws` command you're able to query the current state of your workflow. Before the job starts running, the command will show that the first Firework is marked as `READY` to be run, while the second one is `WAITING` because we told FireWorks to not launch it before the first one has completed. For further instructions on querying workflows, see the [official FireWorks documentation](https://materialsproject.github.io/fireworks/query_tutorial.html).

```bash
$ lpad get_fws
[
    {
        "fw_id": 1,
        "created_on": "2022-02-14T09:43:31.941934",
        "updated_on": "2022-02-14T09:45:27.533414",
        "state": "READY",
        "name": "Unnamed FW"
    },
    {
        "fw_id": 2,
        "created_on": "2022-02-14T09:43:31.942114",
        "updated_on": "2022-02-14T09:43:31.942114",
        "name": "Unnamed FW",
        "state": "WAITING"
    }
]
```

The `singleshot` option was used above to launch a single job. If you have multiple workflows in your LaunchPad ready to be executed, you can use the `rapidfire` option to execute them all in separate batch jobs. 

!!! Note
    The `rapidfire` mode is designed such that it will continuously pull jobs from the LaunchPad that are marked as `READY`. This state applies also for jobs that have already been submitted, but are still queueing. Consequently, too many workflows can accidentally be submitted! To control this, the `-m` and `--nlaunches` flags can be used to limit the number of simultaneous jobs in the queue and the total number of jobs to be submitted, respectively. For further details, see the [official FireWorks documentation on launching jobs through a queue](https://materialsproject.github.io/fireworks/queue_tutorial.html).
  
When the batch job starts, a launch directory is created for each Firework within which the particular job is run. So if your workflow consists of two Fireworks such as in this example, two `launcher_*` directories are created by default. This can, however, be altered and controlled as described in the [official FireWorks documentation](https://materialsproject.github.io/fireworks/controlworker.html). 