---
tags:
  - Academic
catalog:
  name: MATLAB
  description: High-level technical computing language
  license_type: Academic
  disciplines:
    - Mathematics and Statistics
  available_on:
    - web_interfaces:
        - LUMI
        - Puhti
    - LUMI
    - Puhti
---

# MATLAB
[MATLAB](https://mathworks.com/products/matlab.html) is a high-level technical computing language and interactive environment for algorithm development, data visualization, data analysis, and numeric computation.

[TOC]


## License
MATLAB is proprietary software.
We can use a network license provided by a license server or online license provided by MathWorks.
The following MATLAB functions provide information about license and the installation:

- `license` returns the license number currently in use.
- `version` return the MATLAB version.
- `ver` returns MATLAB version, license number and the names and versions of all installed toolboxes.

All toolboxes are installed to the MATLAB installations on the supercomputer, however using a specific toolbox requires that your license allows it

<!--
## Available
### Puhti - Interactive MATLAB
Puhti has MATLAB installations for interactive use and batch jobs.
The interactive MATLAB is intended for temporary, light pre- and postprocessing of data.
It is available as follows:

- License: Academic
- Versions: from R2023a to R2024b
- Toolboxes: Parallel Computing Toolbox.
  There are 2 licenses for each toolbox.

### Puhti - MATLAB Parallel Server
MATLAB Parallel Server (MPS) allows sending work as a batch job from a local MATLAB installation to Puhti.
It is available as follows:

- License: Academic
- Versions: from R2021a to R2025a
- Toolboxes: MATLAB Parallel Server.
  There is license for using upto 500 computing cores simultaneously.
  Furthermore, toolboxes that you have license on your local MATLAB license can also be used with MATLAB Parallel Server.

The academic license allows use only for the affiliates, that is staff and students, of Finnish higher education institutions.
If you are a user from a commercial company or Finnish research institute, please [contact CSC Service Desk](../support/contact.md) for further instructions.

### LUMI - Interactive MATLAB
LUMI has MATLAB an installation for interactive use.

- License: Academic
- Versions: from R2023b to R2024a
- Toolboxes: Simulink, Control System Toolbox, Curve Fitting Toolbox, Deep Learning Toolbox, Global Optimization Toolbox, Image Processing Toolbox, Optimization Toolbox, Parallel Computing Toolbox, Signal Processing Toolbox, Statistics and Machine Learning Toolbox, Wavelet Toolbox.
  There are 25 licenses of each toolbox.

The academic license allows use only for teaching and academic research at a degree-granting institute.
-->


## Overview

There are three primary ways to use MATLAB on supercomputer.

1) MATLAB web application for interactive use.
Allows users to use their own license via online license.

2) MATLAB command line interface for basic interactive and batch computing.

3) MATLAB parallel server for general batch computing.
User send workload from local MATLAB to the supercomputer's MATLAB workers.
User can use the same toolboxes that are available in their local MATLAB.
MATLAB workers on the supercomputer use license provided by the supercomputer.
Currently, only available for Puhti.


## MATLAB web application

TODO: image of web interface

We recommend using the [web interface](../computing/webinterface/index.md) for interactive MATLAB sessions.
The web interface allows you to use your own license such as campus license and all the toolboxes associated with the license.
Start by logging into the web interface of the cluster you want to use, that is, [www.puhti.csc.fi](https://www.puhti.csc.fi), [www.mahti.csc.fi](https://www.mahti.csc.fi) or [www.lumi.csc.fi](https://www.lumi.csc.fi).
Then press the MATLAB icon to choose the MATLAB web application.

In the submit form, select appropriate resources for your session.
We recommend atleast 8 GB of memory before launching the MATLAB application.
The MATLAB web application by itself consumes around 4 GB of memory.

TODO: image of license gui

You will be presented with MATLAB web application license GUI.
Login with your MathWorks credentials.

TODO: image of matlab web application

Loading MATLAB web interface takes couple of minutes.


## MATLAB command-line interface

=== "Puhti and Mahti"

    On Puhti and Mahti, we can load the MATLAB module as follows:

    ```bash
    module load matlab
    ```

=== "LUMI"

    On LUMI, we must add the module files under CSC's local directory to the module path before loading the module as follows:

    ```bash
    module use /appl/local/csc/modulefiles
    module load matlab
    ```

We can open the MATLAB command line interface as follows:

```bash
matlab -nodisplay
```

We can also run MATLAB scripts using the batch mode as follows:

```bash
matlab -batch <script>
```

Use a different license:

```bash
export MLM_LICENSE_FILE="license-file-or-server"
```


## Parallel computing
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


## MATLAB Parallel Server
### Local configuration
Puhti's MATLAB Parallel Server (MPS) allows users to send batch jobs from a local MATLAB session to the Puhti cluster.
Using Puhti MPS requires a local MATLAB installation with a supported MATLAB version and the Parallel Computing Toolbox and access to the Puhti cluster.
We can configure MPS on a local computer using the following instructions.

1. Log in and out to Puhti via SSH client to ensure you have a home directory.
2. Download the configuration script archive [**mps_puhti.zip**](https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip) for Puhti.
3. Create a local MATLAB configuration directory.
4. Extract the configurations to the configuration directory.
5. Add the directory to the unzipped configuration files to MATLAB's path using `addpath` and `savepath` functions in MATLAB.
6. Configure your MATLAB to submit jobs to Puhti by calling `configCluster` in MATLAB and supply your username to the prompt.


#### Linux and MacOS
Step 1: Run in shell:

```bash
ssh <username>@puhti.csc.fi exit
```

Step 2: Run in shell:

```bash
curl --location --output "$HOME/Downloads/mps_puhti.zip" https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip
```

Step 3: Run in shell:

```bash
mkdir -p "$HOME/.matlab"
```

Step 4: Run in shell:
```bash
unzip "$HOME/Downloads/mps_puhti.zip" -d "$HOME/.matlab/mps_puhti"
```

Step 5: Run in MATLAB:
```matlab
addpath(fullfile(getenv("HOME"), ".matlab", "mps_puhti"))
savepath
```

Step 6: Run in MATLAB:
```matlab
configCluster
```

#### Windows
Step 1: Run in Windows Powershell:

```bash
ssh <username>@puhti.csc.fi exit
```

Step 2: Run in Windows Powershell:

```powershell
Invoke-WebRequest -Uri "https://github.com/CSCfi/csc-env-matlab/raw/refs/heads/main/config/mps_puhti.zip" -OutFile "$env:USERPROFILE\Downloads\mps_puhti.zip"
```

Step 3: Run in Windows Powershell:

```powershell
New-Item -Path "$env:APPDATA\Mathworks\MATLAB" -ItemType Directory -Force 
```

Step 4: Run in Windows Powershell:
```powershell
Expand-Archive -Path "$env:USERPROFILE\Downloads\mps_puhti.zip" -DestinationPath "$env:APPDATA\Mathworks\MATLAB\mps_puhti"
```

Step 5: Run in MATLAB:
```matlab
addpath(fullfile(getenv("APPDATA"), "Mathworks", "MATLAB", "mps_puhti"))
savepath
```

Step 6: Run in MATLAB:
```matlab
configCluster
```


### Submitting single and multithreaded jobs
Before submitting the batch job, we have to specify the resource reservation using `parcluster`.
Because the `parcluster` is stateful, it is safest to explicitly unset properties we don't use by setting them to the empty string `''`.
Furthermore, `CPUsPerNode` is set automatically by the `batch` command, thus we unset it.
For example, a simple CPU reservation looks as follows:

```matlab
c = parcluster;
% Replace 'project_id' to your project identifier, otherwise the script will fail.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddress = '';
% You can reserve multiple threads by increasing the NumThreads value.
c.NumThreads = 1;
```

Now, we can use the [`batch`](http://se.mathworks.com/help/distcomp/batch.html) function to submit a job to Puhti.
It returns a job object which we can use to access the output of the submitted job.

The first time you submit a job, MATLAB will prompt you to choose between password or SSH key authentication.
Password authentication is no longer supported on Puhti, so you must select SSH key authentication.
Provide the path to your private key and enter the password for the private key if one exists.
MATLAB will store the path to your key and will not request it again in future sessions.

We can submit a simple test job that returns the current working directory as follows:

```matlab
j = batch(c, @pwd, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

In the example, we set the working directory to the home directory by setting `'CurrentFolder'` to `'.'`.
Also, we should disable MATLAB from adding the local MATLAB search path to the remote workers by setting `'AutoAddClientPath'` to `false`.


### Submitting GPU jobs
We can create a GPU reservation by setting the appropriate values for the `Partition`, `GpuCard`, and `GPUsPerNode` properties.
For example, a single GPU reservation looks as follows:

```matlab
c = parcluster;
% Replace 'project_id' to your project identifier, otherwise the script will fail.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'gpu';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = 1;
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = 'v100';
c.AdditionalProperties.GPUsPerNode = 1;
c.AdditionalProperties.EmailAddress = '';
% You can reserve multiple threads by increasing the NumThreads value.
c.NumThreads = 10;
```

Now, we can submit a simple GPU job that queries the available GPU device as follows:

```matlab
j = batch(c, @gpuDevice, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```


### Submitting parallel pool
Let's create a reservation:

```matlab
c = parcluster;
% Replace 'project_id' to your project identifier, otherwise the script will fail.
c.AdditionalProperties.ComputingProject = 'project_id';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '4g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddress = '';
% You can reserve multiple threads per worker by increasing the NumThreads value.
c.NumThreads = 1;
```

Now, we can use the batch command to create a parallel pool of workers by setting the `'Pool'` argument to the amount of cores we want to reserve.
For example, we can submit a parallel job to eight cores as follows:

```matlab
j = batch(c, @funcParallel, 1, {8}, 'Pool', 8, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

Note that the parallel pool will always request one additional CPU core to manage the batch job and pool of cores.
For example, a job that needs eight cores will consume nine CPU cores.


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
