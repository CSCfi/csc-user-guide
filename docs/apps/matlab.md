# MATLAB

MATLAB is a high-level technical computing language and interactive environment for algorithm development, data visualization, data analysis, and numeric computation.

- High-level language for numerical computation, visualization, and application development.
- Interactive environment for iterative exploration, design, and problem solving.
- Mathematical functions for linear algebra, statistics, Fourier analysis, filtering, optimization, numerical integration, and solving ordinary differential equations.
- Built-in graphics for visualizing data and tools for creating custom plots.
- Development tools for improving code quality and maintainability and maximizing performance.
- Tools for building applications with custom graphical interfaces.
- Functions for integrating MATLAB based algorithms with external applications and languages such as C and Java.

[TOC]

## Available

- Puhti: R2021b, R2021a, R2020b,R2020a, R2019b, R2019a, R2018b, R2018a, R2017b

## License

Proprietary software. The terms of use of this software allow its use for only the affiliates (staff and students) of Finnish higher education institutions. **NB** If you are an user from a commercial company or Finnish research institute, please contact CSC servicedesk for further instructions.

## Usage

At CSC, MATLAB is available both interactive and batch jobs. The interactive sessions are intended for light pre- and postprocessing of data, whereas larger parallel jobs should be run via batch job system of Puhti using MATLAB Parallel Server (MPS) tool.

### Interactive MATLAB Sessions on Puhti
<div id="interactive-matlab" />

There are four interactive MATLAB licenses with **two Parallel Computing Toolbox** and **two Compiler SDK** licenses available for temporary interactive academic use. We recommend to use [the Puhti web interface remote desktop](../computing/webinterface/desktop.md) for the sessions. After logging in to the web interface, MATLAB can be launched as follows:

* Select "Desktop" from the "Apps"-view and specify your resource requirements
* To only run the MATLAB app, select the `Desktop > single application` and `App > MATLAB` settings. 
* To launch the full desktop, select either `mate` or `xfce` and run MATLAB from the host terminal or by clicking the desktop icon. If using the host terminal, open MATLAB with:

```bash
module load matlab/r2021b
matlab
```

### Getting Started with MATLAB Parallel Server on Puhti

The use of MATLAB on Puhti is possible with the MATLAB Parallel Server product and is available for both academic and commercial users, who have their own license of MATLAB. CSC's MPS license makes possible parallel computing runs using up to 500 (academic) or 32 (commercial) cores. With MPS, users can submit jobs from their local MATLAB's GUI directly to the batch job system of Puhti. Before starting using MPS, it is strongly recommend to read the 'Computing' section in [Puhti User Guide](/computing/overview).

#### Installing the Tool Scripts

To use MPS, you need to have an user account at CSC, one of the supported MATLAB's version installed on your own computer with the parallel computing toolbox and getting the license from your home organization's license server.

To configure MPS, follow the instructions on below.

1. Make sure, you have a home directory on Puhti by logging in to the cluster with your CSC username and password by using some ssh client.
2. [Download](https://wiki.eduuni.fi/display/cscjemma/MATLAB+MPS+configuration) MPS tool scripts corresponding to the operating system on your computer.
3. Unzip or untar the downloaded file and place the contents into some directory on your computer, where you have read and write permissions. Make sure, this directory is set to the MATLAB's path. This can be done, for example, with a `pathtool` command.
4. Configure your MATLAB to submit jobs to Puhti by calling `configCluster` and giving your CSC username.

```bash
>> configCluster
Username on Puhti (e.g. joe):
```

#### Configuring Jobs

Prior to submitting the batch job, we have to specify at least

- Wall time (WallTime)
- Memory reservation (MemUsage)
- Billing project (AccountName)
- [Partition on Puhti](/computing/running/batch-job-partitions/) (QueueName)

Optionally, we can configure also
- Email Notification (when the job is running, exiting, or aborting)
- GPU
- Working directory with a 'CurrentFolder' attribute

```bash
>> c = parcluster
>> c.AdditionalProperties.WallTime = '0:10:0'
>> c.AdditionalProperties.MemUsage = '2g'
>> c.AdditionalProperties.QueueName = 'small'
>> c.AdditionalProperties.AccountName = 'project_<id>'
>> % Check configured values
>> c.AdditionalProperties
>> c.saveProfile
```

To clear a value of a property, assign an empty value ('', [], or false), or execute `configCluster` to clear all values. For example, to turn off email notifications
```bash
>> c.AdditionalProperties.EmailAddress = ''
```

#### Submitting a Simple Serial Job

We start by defining a handle to the cluster on your MATLAB's command window

```bash
>> c = parcluster
```
The first time you submit a job to Puhti, the system will prompt whether to use your CSC password or a ssh-key pair for authentication on the computing server. By answering 'No', the CSC's username and password will be asked. If you choose to use a ssh-key pair instead, the location of the key file will be asked next. The key will be stored by MPS, so that it will not be asked at a later time.

Use the `batch` command to submit a batch jobs to Puhti. The command will return a job object which is used to access the output of the submitted job. See an example on below and [MATLAB documentation](http://se.mathworks.com/help/distcomp/batch.html) for more help about `batch`. You can, for example, submit a simple job to test the functionality of the MPS.

```bash
>> j = batch(c, @pwd, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath', false)

additionalSubmitArgs =

    '--ntasks=1 --licenses=mdcs:1'

>> % Wait for the job to finish before fetching the results.
>> j.wait
>>
>> % Now that the job has completed, fetch the results.
>> j.fetchOutputs
```

**NB** In the example above, `j.wait` has been used to ensure that the job has completed before requesting results. In regular use, you would not need to use `wait`, since a job might take an elongated period of time, and the MATLAB session can be used for other work while the submitted job executes.

To retrieve a list of currently running or completed jobs, use
```bash
>> jobs = c.Jobs
>> % Get a handle to the job with sequence number 2
>> j2 = c.Jobs(2)
>> % Fetch results
>> fetchOutputs(j2)
```

Once we've identified the job we want, we can retrieve the results as we've done previously. If the job has produced an error, we can call the `getDebugLog` method to view the error log file. The error log can be lengthy and is not shown here. As an example, we will retrieve the debug log of the serial job.

```bash
>> j.Parent.getDebugLog(j.Tasks(1))
```

**NB** `fetchOutputs` is used to retrieve function output arguments. Data that has been written to files on the cluster needs to be retrieved directly from the file system.

#### Parallel Jobs

You can also submit parallel jobs with `batch`. **NB** The cluster profile validation test will not completely succeed for 'puhti 201xa/b' profiles.

Let's write the following example function.

```batch
function t = parallel_example
t0 = tic;
parfor idx = 1:16
	A(idx) = idx;
	pause(2)
end
t = toc(t0);
```

We'll use the batch command again, but since we're running a parallel job, we'll also need to specify a MATLAB parallel pool.

```bash
>> % Submitting a parallel job to 8 cores.
>> j = batch(c, @parallel_example, 1, {}, 'pool', 8, CurrentFolder','.', 'AutoAddClientPath',false)
```

At first, a parallel pool with eight cores will be constructed. Note that these jobs will always request n+1 CPU cores, since one core is required to manage the batch job and pool of cores. For example, a job that needs eight cores will consume nine CPU cores in total.

Once we have a handle to the cluster, we'll call the `findJob` method to search for the job with the specified job ID, on example below `ID = 11`. Notice the syntax of `getDebugLog`.

```bash
>> j = c.findJob('ID', 11);
>> % For debugging, retrieve the output / error log file.
>> j.Parent.getDebugLog(j)
```

#### Using GPUs

```bash
>> c = parcluster
>> c.AdditionalProperties.QueueName = 'gpu'
>> c.AdditionalProperties.GpuCard = 'v100'
>> c.AdditionalProperties.GpusPerNode = 1
>> j = batch(c, @gpuDevice, 1, {}, 'CurrentFolder', '.', 'AutoAddClientPath',false)
```

#### Checking the Status of MPS Licenses on Puhti

You can check the status of MPS licenses on Puhti after logging in with `scontrol` command.

```bash
$ scontrol show lic=mdcs
LicenseName=mdcs
    Total=500 Used=320 Free=180 Remote=no
```

## More information

Documentation and manuals for MATLAB and related products is available via the Documentation site of MathWorks. To learn more about the MATLAB Parallel Computing Toolbox, check out these resources:

- [Parallel Computing Documentation](http://www.mathworks.com/help/distcomp/index.html)
- [Parallel Computing Tutorials](http://www.mathworks.com/products/parallel-computing/tutorials.html)
- [Parallel Computing Videos](http://www.mathworks.com/products/parallel-computing/videos.html)
- [Parallel Computing Webinars](http://www.mathworks.com/products/parallel-computing/webinars.html)
- [Puhti User Guide](/computing/overview/)



