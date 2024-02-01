---
tags:
  - Academic
system:
  - www-puhti
---

# MATLAB
MATLAB is a high-level technical computing language and interactive environment for algorithm development, data visualization, data analysis, and numeric computation.

</--
- High-level language for numerical computation, visualization, and application development.
- Interactive environment for iterative exploration, design, and problem solving.
- Mathematical functions for linear algebra, statistics, Fourier analysis, filtering, optimization, numerical integration, and solving ordinary differential equations.
- Built-in graphics for visualizing data and tools for creating custom plots.
- Development tools for improving code quality and maintainability and maximizing performance.
- Tools for building applications with custom graphical interfaces.
- Functions for integrating MATLAB based algorithms with external applications and languages such as C and Java.
-->

[TOC]


## License
MATLAB is proprietary software.
The academic license for MATLAB allows use only for the affiliates, that is staff and students, of Finnish higher education institutions.
If you are an user from a commercial company or Finnish research institute, please [contact CSC Service Desk](../support/contact.md) for further instructions.


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
### Command line interface
We can run an interactive MATLAB sessions on the command line.
We first need to make a reservation using Slurm:

```bash
srun <reservation> --pty bash
```

Then, we need to load the matlab module:

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
First, we need to log into [puhti.csc.fi](https://www.puhti.csc.fi) and then we can choose either the *Desktop* or the *MATLAB* application, specify the resouces requirements and launch the application.
On the Desktop application, we can launch MATLAB by clicking the MATLAB icon.


## Using MATLAB Parallel Server on Puhti
### Configuring MPS on local MATLAB
MATLAB Parallel Server allows users to submit jobs from their local MATLAB session to the batch job system of Puhti.
Before starting using MPS, it is strongly recommend to read the 'Computing' section in [Puhti User Guide](../computing/index.md).
To use MPS, you need to have an user account at CSC, one of the supported MATLAB's version installed on your own computer with the parallel computing toolbox and getting the license from your home organization's license server.

To configure MPS, follow the instructions on below.

1. Make sure, you have a home directory on Puhti by logging in to the cluster with your CSC username and password by using some ssh client.
2. [Download](https://wiki.eduuni.fi/display/cscjemma/MATLAB+MPS+configuration) MPS tool scripts corresponding to the operating system on your computer.
3. Unzip or untar the downloaded file and place the contents into some directory on your computer, where you have read and write permissions. Make sure, this directory is set to the MATLAB's path. This can be done, for example, with a `pathtool` command.
4. Configure your MATLAB to submit jobs to Puhti by calling `configCluster` and giving your CSC username.

```matlab
configCluster
% Username on Puhti (e.g. joe):
```


### Submitting jobs
Prior to submitting the batch job, we have to specify the resource reservation using `parcluster`.
An empty string `''` means that we have not set a value for the attribute.
For example, a simple CPU reservation looks as follows:

```matlab
c = parcluster;
c.AdditionalProperties.ComputingProject = 'project_<id>';
c.AdditionalProperties.Partition = 'small';
c.AdditionalProperties.WallTime = '00:15:00';
c.AdditionalProperties.CPUsPerNode = '';
c.AdditionalProperties.MemPerCPU = '2g';
c.AdditionalProperties.GpuCard = '';
c.AdditionalProperties.GPUsPerNode = '';
c.AdditionalProperties.EmailAddres = '';
```

See available [partitions on Puhti](/computing/running/batch-job-partitions/).
To clear a value of a property, assign an empty value ('', [], or false), or execute `configCluster` to clear all values.

The first time you submit a job to Puhti, the system will prompt whether to use your CSC password or a ssh-key pair for authentication on the computing server.
By answering 'No', the CSC's username and password will be asked.
If you choose to use a ssh-key pair instead, the location of the key file will be asked next.
The key will be stored by MPS, so that it will not be asked at a later time.

Use the `batch` command to submit a batch jobs to Puhti.
The command will return a job object which is used to access the output of the submitted job.
See an example on below and [MATLAB documentation](http://se.mathworks.com/help/distcomp/batch.html) for more help about `batch`.
You can, for example, submit a simple job to test the functionality of the MPS.


```matlab
j = batch(c, @pwd, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)
```

We can set the working directory using the 'CurrentFolder' attribute.
When the job has completed, we can fetch the results.

```matlab
j.fetchOutputs
```

To retrieve a list of currently running or completed jobs, use

```matlab
jobs = c.Jobs;
% Get a handle to the job with sequence number 2
j2 = c.Jobs(2);
% Fetch results
fetchOutputs(j2)
```

Once we've identified the job we want, we can retrieve the results as we've done previously. If the job has produced an error, we can call the `getDebugLog` method to view the error log file. The error log can be lengthy and is not shown here. As an example, we will retrieve the debug log of the serial job.

```matlab
j.Parent.getDebugLog(j.Tasks(1))
```

**NB** `fetchOutputs` is used to retrieve function output arguments. Data that has been written to files on the cluster needs to be retrieved directly from the file system.


### Parallel jobs
You can also submit parallel jobs with `batch`. **NB** The cluster profile validation test will not completely succeed for 'puhti 201xa/b' profiles.

Let's write the following example function.

```matlab
function t = parallel_example()
t0 = tic;
parfor idx = 1:16
    A(idx) = idx;
    pause(2)
end
t = toc(t0);
end
```

We'll use the batch command again, but since we're running a parallel job, we'll also need to specify a MATLAB parallel pool.

```matlab
% Submitting a parallel job to 8 cores.
j = batch(c, @parallel_example, 1, {}, 'Pool', 8, CurrentFolder','.', 'AutoAddClientPath',false)
```

At first, a parallel pool with eight cores will be constructed. Note that these jobs will always request n+1 CPU cores, since one core is required to manage the batch job and pool of cores. For example, a job that needs eight cores will consume nine CPU cores in total.

Once we have a handle to the cluster, we'll call the `findJob` method to search for the job with the specified job ID, on example below `ID = 11`. Notice the syntax of `getDebugLog`.

```matlab
j = c.findJob('ID', 11);
% For debugging, retrieve the output / error log file.
j.Parent.getDebugLog(j)
```

### Using GPUs

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

```matlab
j = batch(c, @gpuDevice, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath',false)
```

### Checking license status

You can check the status of MPS licenses on Puhti after logging in with `scontrol` command.

```bash
scontrol show lic=mdcs
```

```text
LicenseName=mdcs
    Total=500 Used=320 Free=180 Remote=no
```


## Creating and using custom MATLAB installation
TODO: It is also possible to create and use custom matlab installation and license.


## More information

Documentation and manuals for MATLAB and related products is available via the Documentation site of MathWorks. To learn more about the MATLAB Parallel Computing Toolbox, check out these resources:

- [Parallel Computing Documentation](http://www.mathworks.com/help/distcomp/index.html)
- [Parallel Computing Tutorials](http://www.mathworks.com/products/parallel-computing/tutorials.html)
- [Parallel Computing Videos](http://www.mathworks.com/products/parallel-computing/videos.html)
- [Parallel Computing Webinars](http://www.mathworks.com/products/parallel-computing/webinars.html)
- [Puhti User Guide](../computing/index.md)
