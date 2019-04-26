## MATLAB

### Description

MATLAB is a high-level technical computing language and interactive
environment for algorithm development, data visualization, data
analysis, and numeric computation.

##### Key Features

-   High-level language for numerical computation, visualization, and
    application development.
-   Interactive environment for iterative exploration, design, and
    problem solving.
-   <span id="yui_patched_v3_11_0_1_1434006940870_520">Mathematical
    functions for linear algebra, statistics, Fourier analysis,
    filtering, optimization, numerical integration, and solving ordinary
    differential equations.</span>
-   Built-in graphics for visualizing data and tools for creating custom
    plots.
-   Development tools for improving code quality and maintainability and
    maximizing performance.
-   <span id="yui_patched_v3_11_0_1_1434006940870_496">Tools for
    building applications with custom graphical interfaces.</span>
-   Functions for integrating MATLAB based algorithms with external
    applications and languages such as C and Java.

------------------------------------------------------------------------

### Available

##### Version on CSC's Servers

Supported versions on Taito:

-   R2018a, R2018b
-   R2017b
-   R2016b
-   R2014b, R2014a

------------------------------------------------------------------------

### Usage

##### Getting Started with MATLAB Distributed Computing Server on Taito

The use of MATLAB on [Taito cluster] of CSC is possible only with the
[MATLAB Distributed Computing Server] (MDCS) product and is available
for both academic and commercial users, who have their own license of
MATLAB. The MDCS license of CSC makes possible parallel computing runs
using up to 500 (academic) or 32 (commercial) cores and allows users to
submit jobs from one's local MATLAB's GUI directly to the batch job
system of Taito.

To use MDCS, you need to have a [user account at CSC], one of the
supported MATLAB's version installed on your own computer with the
parallel computing toolbox and getting the license from your home
organization's license server.

To configure MDCS, follow the instructions on below.

1.  Make sure, you have a home directory on Taito by logging in to the
    cluster with your CSC username and password by using some ssh
    client.
2.  Download configuration scripts on below corresponding to the MATLAB
    release in use and operating system on your computer.
    -   R2017a and later: [Linux and Mac]
    -   R2017a and later: [Windows]
    -   R2016b: [Linux and Mac][1]
    -   R2016b: [Windows][2]
3.  Unzip or untar the downloaded file and place the contents into some
    directory on your computer, where you have read and write
    permissions. Make sure, this directory is set to the MATLAB's path.
    This can be done, for example, with a pathtool command.
4.  Configure your MATLAB to run parallel and serial jobs on Taito
    cluster by calling configCluster and giving your username on Taito.

<!-- -->

    >> configCluster
    Username on TAITO (e.g. joe):

**NB** If you are an user from a commercial company or Finnish research
institute, please contact CSC servicedesk for further instructions.

##### Tutorial - Configure and Test MDCS

In this tutorial, we will show, how to configure MDCS on your computer
and submit a simple test job to Taito. Hover the cursor over the video
clip to show controls.

Your browser does not support the video tag.

##### Connection to Taito

The first time you submit a job to Taito, the system will prompt whether
to supply a password or a private key for the SSH connection, as in
figure 1. By answering 'No', the password relating to CSC's username
will be used.

 

![Figure 1. The prompt for the private key.]

 

If you choose to use a private key, the location of the key file will be
asked next. The key will be stored by MATLAB so that it will not be
asked at a later time.

##### Submitting a Simple Serial Job

Start by defining a handle to the cluster on your MATLAB's command
window

    >> c = parcluster

Use the batch command to submit a batch jobs to Taito. The batch command
will return a job object which is used to access the output of the
submitted job. See an example on below and [MATLAB documentation] for
more help about batch. You can, for example, submit a simple job to test
the functionality of the MDCS.

    >> j = batch(c, @pwd, 1, 'CurrentFolder', '.')

    additionalSubmitArgs =

        '--ntasks=1 --licenses=mdcs:1'

    >> % Wait for the job to finish before fetching the results.
    >> j.wait
    >>
    >> % Now that the job has completed, fetch the results.
    >> j.fetchOutputs

Note: In the example above, j.wait has been used to ensure that the job
has completed before requesting results. In regular use, one would not
need to use wait, since a job might take an elongated period of time,
and the MATLAB session can be used for other work while the submitted
job executes.

To retrieve a list of currently running or completed jobs, call
parcluster to retrieve the cluster object. The cluster object stores an
array of jobs that were run, are running, or are queued to run. This
allows to fetch the results of completed jobs.

Once we've identified the job we want, we can retrieve the results as
we've done previously. If the job produces an error, we can call the
getDebugLog method to view the error log file. The error log can be
lengthy and is not shown here. As an example, we will retrieve the debug
log of the serial job.

    >> j.Parent.getDebugLog(j.Tasks(1))

NOTE: fetchOutputs is used to retrieve function output arguments. Data
that has been written to files on the cluster needs to be retrieved
directly from the file system.

##### Parallel Jobs

You can also submit parallel jobs with batch. Take note, the cluster
profile validation test will not completely succeed for 'taito remote'
profiles.

Let's write the following example function.

    function t = parallel_example
    t0 = tic;
    parfor idx = 1:16
        A(idx) = idx;
        pause(2)
    end
    t = toc(t0);

We'll use the batch command again, but since we're running a parallel
job, we'll also need to specify a MATLAB parallel pool.

    >> % Submitting a parallel job to 8 cores.
    >> j = batch(c, @parallel_example, 1, {}, 'pool', 8)

At first, a parallel pool with eight cores will be constructed. Note
that these jobs will always request *n*+1 CPU cores, since one core is
required to manage the batch job and pool of cores. For example, a job
that needs eight cores will consume nine CPU cores.

Once we have a handle to the cluster, we'll call the findJob method to
search for the job with the specified job ID, on example below ID = 11.
Notice the syntax of getDebugLog.

    >> j = c.findJob('ID', 11);
    >> % For debugging, retrieve the output / error log file.
    >> j.Parent.getDebugLog(j)

##### Configuring Jobs

Prior to submitting the job, along with setting the wall time, we can
also specify:

-   Email Notification (when the job is running, exiting, or aborting)
-   GPU
-   Memory Usage
-   Partition
-   Reservation
-   Working directory with a 'CurrentFolder' attribute

###### MATLAB Versions R2017a and newer

Starting in R2017a, AdditionalProperties will replace ClusterInfo. The
advantage to AdditionalProperties is that it is associated with a
cluster (whereas ClusterInfo is associated to a global MATLAB
preference). Therefore, a user can have access to multiple clusters,
each with its own set of scheduler properties.

###### Example of Setting the SLURM Scheduler Properties on Taito

Version R2017a and later releases

    c = parcluster
    c.AdditionalProperties.WallTime = '0:10:0'
    c.AdditionalProperties.MemUsage = '2g'
    c.AdditionalProperties.QueueName = 'parallel'
    c.saveProfile
    j = batch(c, @fcn, 1, {}, 'pool', 32, 'CurrentFolder', '/wrk/myworkdir')

To see the values of the current configuration options, call the
AdditionalProperties method as shown on below. To clear a value, assign
the property an empty value ('', \[\], or false), or execute
configCluster to clear all values.

    >> % See the configurations of a cluster
    >> c = parcluster
    >> c.AdditionalProperties
    >> % Save the cluster profile for further use
    >> c.saveProfile

MATLAB versions R2016b and older

    ClusterInfo.setWallTime('0:10:0')
    ClusterInfo.setMemUsage('2g')
    ClusterInfo.setQueueName('parallel')
    c = parcluster
    j = batch(c, @fcn, 1, {}, 'pool', 32, 'CurrentFolder', '/wrk/myworkdir')

Available partitions on Taito are:

-   parallel
-   serial
-   longrun
-   test
-   hugemem
-   gpu
-   gpulong
-   gputest

Notice, each partition has a default runtime of 5 minutes. Use command
AdditionalProperties.WallTime to set an appropriate run time for your
job. You can find more information about Taito partitions from [Taito
User Guide][Taito cluster].

##### An example of requesting a GPU (R2017a and newer)

Use AdditionalProperties to request a GPU, see an example on below and
<https://research.csc.fi/taito-gpu-running>.

    >> % An example of submitting a gpu job to Taito
    >> c = parcluster
    >> c.AdditionalProperties.GpuQueue = 'gpu'
    >> c.AdditionalProperties.GpuCard = 'p100'
    >> c.AdditionalProperties.GpusPerNode = 1
    >> j = batch(c, @gpuDevice, 1, {}, 'CurrentFolder', '.')

    additionalSubmitArgs =

        '--ntasks=1 -p gpu --gres=gpu:p100:1 --exclusive --licenses=mdcs:1'

The video tutorial on below will show, how to use MDCS on your computer
and submit a simple GPU job to Taito. Hover the cursor over the video
clip to show controls.

Your browser does not support the video tag.

##### Checking the Status of MDCS Licenses on Taito

You can check the status of MDCS licenses on Taito after logging in to
the cluster with scontrol command.

    $ scontrol show lic=mdcs
    LicenseName=mdcs
        Total=500 Used=320 Free=180 Remote=no

##### Interactive MATLAB sessions on Taito-shell

There are four interactive MATLAB licenses with two Parallel Computing
Toolbox and one Compiler license available on Taito-shell for temporary
interactive academic use. We recommend to use [NoMachine] client for the
sessions. After logging in to Taito-shell, MATLAB can be launched as
follows:

    $ module load matlab/R2018b
    $ matlab

------------------------------------------------------------------------

### Discipline

Mathematics and Statistics  

------------------------------------------------------------------------

### References

-   <span class="citation book">Gilat, Amos (2004). *MATLAB: An
    Introduction with Applications 2nd Edition*. John Wiley & Sons. ISBN
    978-0-471-69420-5</span>
-   <span class="citation book">Lynch, Stephen (2004). *Dynamical
    Systems with Applications using MATLAB*. Birkhäuser.
    ISBN978-0-8176-4321-8</span>
-   <span class="citation book">Quarteroni, Alfio; Fausto Saleri (2006).
    *Scientific Computing with MATLAB and Octave*. Springer. ISBN
    978-3-540-32612-0</span>
-   <span id="yui_patched_v3_11_0_1_1433833348523_714"><span
    class="citation book"><span class="citation book">Ferreira, A.J.M.
    (2009). *MATLAB Codes for Finite Element Analysis*. Springer. ISBN
    978-1-4020-9199-5</span></span></span>

------------------------------------------------------------------------

### Support

servicedesk@csc.fi

------------------------------------------------------------------------

### Manual

Documentation and manuals for MATLAB and related products is available
via the [Documentation site] of MathWorks. To learn more about the
MATLAB Parallel Computing Toolbox, check out these resources:

-   [Parallel Computing Coding Examples]
-   [Parallel Computing Documentation]
-   [Parallel Computing Tutorials]
-   [Parallel Computing Videos]
-   [Parallel Computing Webinars]

 

Other documentation relating to using MATLAB on Taito cluister

-   [Manual page of MATLAB's batch command]
-   [Useful SLURM commands for monitoring jobs]
-   [How to estimate how much memory my batch job needs?]
-   [Mounting your CSC directories as a part of your local file system]

 

------------------------------------------------------------------------

  [Taito cluster]: https://research.csc.fi/taito-user-guide
  [MATLAB Distributed Computing Server]: https://se.mathworks.com/products/distriben.html
  [user account at CSC]: https://research.csc.fi/accounts-and-projects
  [Linux and Mac]: https://research.csc.fi/documents/48467/244245/csc.remote.R2018b.tar.gz/a705c3a8-e042-47df-9258-cdeecd35696c
  [Windows]: https://research.csc.fi/documents/48467/244245/csc.remote.R2018b.zip/4bb23b04-21b2-4cdc-ad50-ffde0652612c
  [1]: https://research.csc.fi/documents/48467/244245/csc.remote.tar/666694a1-a0e5-469c-9226-213f17c45a99
  [2]: https://research.csc.fi/documents/48467/244245/csc.remote.zip/2d123e9e-6a70-4e37-a74f-6d7004ad89ec
  [Figure 1. The prompt for the private key.]: https://research.csc.fi/documents/48467/171595/figure_2.png/76c5efcc-5cad-4998-943f-0701fc5080ea?t=1414058565490
  [MATLAB documentation]: http://se.mathworks.com/help/distcomp/batch.html
  [NoMachine]: https://research.csc.fi/-/nomachine
  [Documentation site]: http://se.mathworks.com/help/index.html
  [Parallel Computing Coding Examples]: http://www.mathworks.com/products/parallel-computing/code-examples.html
  [Parallel Computing Documentation]: http://www.mathworks.com/help/distcomp/index.html
  [Parallel Computing Tutorials]: http://www.mathworks.com/products/parallel-computing/tutorials.html
  [Parallel Computing Videos]: http://www.mathworks.com/products/parallel-computing/videos.html
  [Parallel Computing Webinars]: http://www.mathworks.com/products/parallel-computing/webinars.html
  [Manual page of MATLAB's batch command]: https://se.mathworks.com/help/distcomp/batch.html
  [Useful SLURM commands for monitoring jobs]: https://research.csc.fi/taito-using-slurm-commands-to-execute-batch-jobs
  [How to estimate how much memory my batch job needs?]: https://research.csc.fi/faq-details/-/asset_publisher/YcvLTywwhutL/content/a?_101_INSTANCE_YcvLTywwhutL_redirect=%2Ffaq-details
  [Mounting your CSC directories as a part of your local file system]: https://research.csc.fi/csc-guide-remote-disk-mounts
