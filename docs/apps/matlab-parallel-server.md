# MATLAB Parallel Server

MATLAB Parallel Server (MPS) allows users to send batch jobs from MATLAB on the user's computer to the Roihu cluster's MATLAB workers.
The examples on this page use the functions `funcSerial`, `funcParallel` and `funcThreads` defined on the [MATLAB](matlab.md#computational-threads-and-parallel-computing-toolbox) page.
For licensing, see [MATLAB license](matlab.md#license).

[TOC]


## Local configuration

Using MPS requires the following configuration on the user's computer: MATLAB installation with a supported MATLAB version, the Parallel Computing Toolbox, [SSH access](../computing/connecting/ssh-keys.md) to the Roihu cluster, and a user-side configuration.
Install the user-side configuration files by running the following MATLAB script:

```matlab title="mps_csc.m"
% Define local MATLAB configuration directory.
if ispc()
    % Windows
    confroot = fullfile(getenv("APPDATA"), "Mathworks", "MATLAB");
elseif isunix() || ismac()
    % Unix (Linux) or MacOS
    confroot = fullfile(getenv("HOME"), ".matlab");
else
     % Operating system not supported
     exit();
end

% Path to where the ZIP file is downloaded.
confzip = fullfile(confroot, "mps_csc.zip");

% Remove previous zipfile if exists
if exist(confzip, "file") == 2
    delete(confzip);
end

% Path to the directory where configuration files are extracted.
confdir = fullfile(confroot, "mps_csc");

% Remove previous zipdir if exists
if exist(confdir, "dir") == 7
    rmdir(confdir, 's');
end

% Download the configuration files as a ZIP file.
websave(confzip, "https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/csc.Desktop.zip");

% Extract the configuration files to the configuration directory.
unzip(confzip, confdir);

% Persist path to the configuration files.
addpath(confdir);
savepath();
```

Next, let's configure a cluster profile that allows your MATLAB to submit jobs to Roihu.
Supply your Roihu username to the prompt.

```matlab title="configCluster.m"
configCluster();
```

Finally, we can test the connection from MATLAB to Roihu.
The first time you connect, MATLAB will prompt you to choose between password or SSH key authentication.
You **must** select the SSH key authentication, provide the path to your private key and enter the password for the private key if one exists.
Password authentication is not supported on Roihu.
MATLAB will store the path to your key and will not request it again in future sessions.

```matlab title="testConnection.m"
c = parcluster();
cscWorkspaces(c);
```

!!! error
    If you are using PuTTY to generate SSH keys, you **must** export the private key as an **OpenSSH key** and use it with MATLAB Parallel Server.
    The PuTTY Private Key format (`.ppk`) will **not** work.


## Single node serial and parallel
We define the resource reservation using [`parcluster`](https://www.mathworks.com/help/parallel-computing/parcluster.html) and submit the function or script to the cluster using [`batch`](http://www.mathworks.com/help/distcomp/batch.html).
The `parcluster` object is stateful, thus we explicitly unset properties when they are unused, such as GPUs for CPU-only jobs.
You can use the following examples; just replace `<project>` with your project, such as `project_2001234`, and modify the resource reservation to suit your needs.

=== "Serial"

    ```matlab title="serial.m"
    c = parcluster();
    c.AdditionalProperties.ComputingProject = '<project>';  % --account=<ComputingProject>
    c.AdditionalProperties.Partition = 'small';             % --partition=<Partition>
    c.AdditionalProperties.WallTime = '00:15:00';           % --time=<WallTime>
    c.NumThreads = 1;                                       % --cpus-per-task=<NumThreads>
    c.AdditionalProperties.MemPerCPU = '4g';                % --mem-per-cpu=<MemPerCPU>
    c.AdditionalProperties.GPUCard = '';                    % --gres=gpu:<GPUCard>:<GPUsPerNode>
    c.AdditionalProperties.GPUsPerNode = 0;
    j = batch(c, @funcSerial, 1, {2}, 'CurrentFolder', '.', 'AutoAddClientPath', false);
    ```

=== "Parallel"

    ```matlab title="parallel.m"
    c = parcluster();
    c.AdditionalProperties.ComputingProject = '<project>';  % --account=<ComputingProject>
    c.AdditionalProperties.Partition = 'small';             % --partition=<Partition>
    c.AdditionalProperties.WallTime = '00:15:00';           % --time=<WallTime>
    c.NumThreads = 2;                                       % --cpus-per-task=<NumThreads>
    c.AdditionalProperties.MemPerCPU = '4g';                % --mem-per-cpu=<MemPerCPU>
    c.AdditionalProperties.GPUCard = '';                    % --gres=gpu:<GPUCard>:<GPUsPerNode>
    c.AdditionalProperties.GPUsPerNode = 0;
    j = batch(c, @funcThreads, 1, {2}, 'CurrentFolder', '.', 'AutoAddClientPath', false);
    ```

<!-- === "GPU" -->
<!---->
<!--     ```matlab title="gpu.m" -->
<!--     c = parcluster(); -->
<!--     c.AdditionalProperties.ComputingProject = '<project>';  % --account=<ComputingProject> -->
<!--     c.AdditionalProperties.Partition = 'gpu';               % --partition=<Partition> -->
<!--     c.AdditionalProperties.WallTime = '00:15:00';           % --time=<WallTime> -->
<!--     c.NumThreads = 1;                                       % --cpus-per-task=<NumThreads> -->
<!--     c.AdditionalProperties.MemPerCPU = '4g';                % --mem-per-cpu=<MemPerCPU> -->
<!--     c.AdditionalProperties.GPUCard = 'gh200';                % --gres=gpu:<GPUCard>:<GPUsPerNode> -->
<!--     c.AdditionalProperties.GPUsPerNode = 1; -->
<!--     j = batch(c, @funcGPU, 1, {1000}, 'CurrentFolder', '.', 'AutoAddClientPath', false); -->
<!--     ``` -->

In the example, we set the working directory to the home directory in the cluster by setting `'CurrentFolder'` to `'.'`.
Also, we should disable MATLAB from adding the local MATLAB search path to the remote workers by setting `'AutoAddClientPath'` to `false`.
These examples reserve 1 MATLAB Parallel Server license on the cluster for the duration of the job.


## Multinode jobs

!!! warning
    Multinode jobs do not seem to work in R2025a.

We can also create a parallel pool of workers by setting the `'Pool'` argument to the number of workers we want to reserve (translates to `--ntasks=<PoolSize>` in the Slurm reservation).
The `parcluster` resources specify how many resources are reserved per worker.
**We should reserve a pool in this way when we need more workers than can fit into a single node; otherwise, we can reserve a parallel job as was described in the previous section and reserve a pool with threads or processes.**

Here is an example of a parallel pool with 50 workers:

```matlab title="pool.m"
c = parcluster();
c.AdditionalProperties.ComputingProject = '<project>';  % --account=<ComputingProject>
c.AdditionalProperties.Partition = 'large';             % --partition=<Partition>
c.AdditionalProperties.WallTime = '00:15:00';           % --time=<WallTime>
c.NumThreads = 1;                                       % --cpus-per-task=<NumThreads>
c.AdditionalProperties.MemPerCPU = '4g';                % --mem-per-cpu=<MemPerCPU>
c.AdditionalProperties.GPUCard = '';                    % --gres=gpu:<GPUCard>:<GPUsPerNode>
c.AdditionalProperties.GPUsPerNode = '';
j = batch(c, @funcParallel, 1, {50}, 'Pool', 50, 'CurrentFolder', '.', 'AutoAddClientPath', false);
```

Note that the parallel pool will always request one additional process to manage the pool of workers.
This example reserves 51 MATLAB Parallel Server licenses on the cluster for the duration of the job.
Roihu has 500 MATLAB Parallel Server licenses shared by all users.


## Querying jobs and output

Get a handle on the parcluster object:

```matlab
c = parcluster();
```

Retrieve the last 5 jobs:

```matlab
c.Jobs(end-4:end)
```

Retrieve a job by its identifier:

```matlab
j = c.findJob('ID', 11);
```

We can fetch the function outputs of a completed job as follows:

```matlab
result = j.fetchOutputs()
```

We can read the output of the job as follows:

```matlab
diary(j)
```

We can also query the efficiency of a job:

```matlab
seff(j)
```

Data that has been written to files on the cluster needs to be retrieved directly from the file system, for example, using `scp`.


<!--
## Checking license status
You can check the status of MPS licenses on Roihu after logging in with `scontrol` command.

```bash
scontrol show lic=mdcs
```

```text
LicenseName=mdcs
    Total=500 Used=320 Free=180 Remote=no
```
-->
