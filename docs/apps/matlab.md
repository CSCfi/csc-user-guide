---
tags:
  - Academic
system:
  - www-puhti
---

# MATLAB
[MATLAB](https://mathworks.com/products/matlab.html) is a high-level technical computing language and interactive environment for algorithm development, data visualization, data analysis, and numeric computation.

[TOC]


## License
MATLAB is proprietary software.
The academic license for MATLAB allows use only for the affiliates, that is staff and students, of Finnish higher education institutions.
If you are a user from a commercial company or Finnish research institute, please [contact CSC Service Desk](../support/contact.md) for further instructions.


## Available
CSC has MATLAB installations on Puhti for interactive use and batch jobs.
The interactive MATLAB is intended for temporary, light pre- and postprocessing of data.
It is available as follows:

- Systems: *Puhti*
- License: *Academic*
- Versions: *R2021b*, *R2023b*
- Toolboxes: *MATLAB Compiler* (2 licenses), *MATLAB Compiler SDK* (2 licenses), *Parallel Computing Toolbox* (2 licenses)

*MATLAB Parallel Server (MPS)* allows sending work as a batch job from a local MATLAB installation to Puhti.
It is available as follows:

- Systems: *Puhti*
- License: *Academic*
- Versions: *R2021b*, *R2022b*, *R2023a*, *R2023b*
- Toolboxes: *MATLAB Parallel Server* (500 licenses)

Toolboxes from the local computer can also be used with MATLAB Parallel Server.


## Using interactive MATLAB on Puhti
### Command-line interface
We can run an interactive MATLAB session on the command line.
We first need to make a reservation using Slurm:

```bash
srun --account=project_id --partition=small --time=0:15:00 --cpus-per-task=1 --mem-per-cpu=4g --pty bash
```

Then, we need to load the MATLAB module:

```bash
module load matlab
```

Now `matlab`, `mbuild`, `mex` and `mcc` commands are available.
For example, we can open the MATLAB command line interface as follows:

```bash
matlab -nodisplay
```

We can also run MATLAB scripts using the batch mode as follows:

```bash
matlab -batch <script>
```


### Web interface
We can also use the [web interface](../computing/webinterface/index.md) for interactive MATLAB sessions.
First, we need to log into [puhti.csc.fi](https://www.puhti.csc.fi) and then we can choose either the *Desktop* or the *MATLAB* application, specify the resource requirements and launch the application.
On the Desktop application, we can launch MATLAB by clicking the MATLAB icon.


## Parallel computing on MATLAB
In MATLAB, we can parallelize code using the high-level contructs from the [Parallel Computing Toolbox](https://mathworks.com/help/parallel-computing/index.html).
Consider the following serial code written in `funcSerial.m` file that pauses for one second `n` times and measures the execution time:

```matlab
function t = funcSerial(n)
t0 = tic;
for idx = 1:n
    pause(1);
end
t = toc(t0);
end
```

The following serial execution should run for around two seconds:

```matlab
funcSerial(2)
```

We can parallelize the function using the parallel for-loop construct, `parfor`, written into `funcParallel.m` file as follows:

```matlab
function t = funcParallel(n)
t0 = tic;
parfor idx = 1:n
    pause(1);
end
t = toc(t0);
end
```

To run parallel code, we need to create a parallel pool using processes or threads and then run the parallel code.
We can create a parallel pool using two processes and run the parallel code with the same argument as serial but it should only take around one second:

```matlab
pool = parpool('Processes', 2);
funcParallel(2)
delete(pool);
```

Same using parallel pool with threads:

```matlab
pool = parpool('Threads', 2);
funcParallel(2)
delete(pool);
```

With MATLAB Parallel Server we can also create parallel pools to Puhti and run parallel code there.

<!-- TODO: Constructs for using GPUs are also available. -->


## Using MATLAB Parallel Server on Puhti
### Configuring MPS on local MATLAB
Puhti's MATLAB Parallel Server (MPS) allows users to send batch jobs from a local MATLAB session to the Puhti cluster.
Using Puhti MPS requires a local MATLAB installation with a supported MATLAB version and the Parallel Computing Toolbox and access to the Puhti cluster.
We can configure MPS on a local computer using the following instructions.

1. Log in and out to Puhti via SSH client to ensure you have a home directory.
2. Download the [**MPS configuration scripts**](https://wiki.eduuni.fi/display/cscjemma/MATLAB+MPS+configuration) for Puhti.
3. Unzip the downloaded archive into a chosen directory.
   On Linux and macOS, MATLAB stores local configurations in `~/.matlab` directory.
   We can place the files there as follows:
   ```bash
   mkdir -p ~/.matlab/mps_puhti
   unzip csc.Desktop.zip -d ~/.matlab/mps_puhti
   ```
   On Windows, we can use the `%AppData%\Mathworks\MATLAB` directory to store the configurations.
4. Set the directory the MATLAB path using `addpath` and `savepath` functions in MATLAB as follows:
   ```matlab
   addpath("~/.matlab/mps_puhti")
   savepath
   ```
5. Configure your MATLAB to submit jobs to Puhti by calling `configCluster` in MATLAB and supply your username to the prompt as follows:
   ```matlab
   configCluster
   % Username on Puhti (e.g. jdoe): >>username
   ```


### Submitting serial jobs
Before submitting the batch job, we have to specify the resource reservation using `parcluster`.
Because the `parcluster` is stateful, it is safest to explicitly unset properties we don't use by setting them to the empty string `''`.
Furthermore, `CPUsPerNode` is set automatically by the `batch` command, thus we unset it.
For example, a simple CPU reservation looks as follows:

```matlab
c = parcluster;
c.AdditionalProperties.ComputingProject = 'project_<id>';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddress = '';
```

Now, we can use the [`batch`](http://se.mathworks.com/help/distcomp/batch.html) function to submit a job to Puhti.
It returns a job object which we can use to access the output of the submitted job.

The first time you submit a job, MATLAB will prompt you whether to use a password or an SSH key for authentication.

1. If you choose to use a password, MATLAB will ask your password to Puhti.
2. If you choose to use an SSH key, MATLAB will ask the path the your private key and whether the key requires a password.
   MATLAB stores the path to your key and will not ask for it later.

We can submit a simple test job that returns the current working directory as follows:

```matlab
j = batch(c, @pwd, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

In the example, we set the working directory to the home directory by setting `'CurrentFolder'` to `'.'`.
Also, we should disable MATLAB from adding the local MATLAB search path to the remote workers by setting `'AutoAddClientPath'` to `false`.


### Submitting parallel jobs
Let's create a reservation:

```matlab
c = parcluster;
c.AdditionalProperties.ComputingProject = 'project_<id>';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddress = '';
```

Now, we can use the batch command to create a parallel pool of workers by setting the `'Pool'` argument to the amount of cores we want to reserve.
For example, we can submit a parallel job to eight cores as follows:

```matlab
j = batch(c, @funcParallel, 1, {8}, 'Pool', 8, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

Note that the parallel pool will always request one additional CPU core to manage the batch job and pool of cores.
For example, a job that needs eight cores will consume nine CPU cores.


### Submitting serial GPU jobs
We can create a GPU reservation by setting the appropriate values for the `Partition`, `GpuCard`, and `GPUsPerNode` properties.
For example, a single GPU reservation looks as follows:

```matlab
c = parcluster;
c.AdditionalProperties.ComputingProject = 'project_<id>';
c.AdditionalProperties.Partition = 'gpu';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = 1;
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = 'v100';
c.AdditionalProperties.GPUsPerNode = 1;
c.AdditionalProperties.EmailAddress = '';
```

Now, we can submit a simple GPU job that queries the available GPU device as follows:

```matlab
j = batch(c, @gpuDevice, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```


### Querying jobs and output
To retrieve a list of currently running or completed jobs, use

```matlab
c = parcluster;
c.Jobs
```

Get a handle to the job with sequence number 1

```matlab
j = c.Jobs(1);
```

Once we have a handle to the cluster, we'll call the `findJob` method to search for the job with the specified job ID, on example below `ID = 11`.

```matlab
j = findJob(c, 'ID', 11);
```

Once the job has been completed, we can fetch the function outputs as follows:

```matlab
fetchOutputs(j)
```

Data that has been written to files on the cluster needs to be retrieved directly from the file system.


<!--
Once we've identified the job we want, we can retrieve the results as we've done previously.
If the job has produced an error, we can call the `getDebugLog` method to view the error log file.
The error log can be lengthy and is not shown here.

As an example, we will retrieve the debug log of the serial job.

```matlab
getDebugLog(j.Parent, j.Tasks(1))
```

For debugging, retrieve the log file.

```matlab
getDebugLog(j.Parent ,j)
```
-->


<!--
### Checking license status
You can check the status of MPS licenses on Puhti after logging in with `scontrol` command.

```bash
scontrol show lic=mdcs
```

```text
LicenseName=mdcs
    Total=500 Used=320 Free=180 Remote=no
```
-->


<!-- TODO:
## Creating and using custom MATLAB installation
It is also possible to create and use custom MATLAB installation and license.
-->
