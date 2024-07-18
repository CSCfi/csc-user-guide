# Getting started

CSC uses a batch job system to schedule and execute computing tasks on our
supercomputers.

Typically, a batch job first loads a software environment using the
[module system](../modules.md) and then executes a program to do some
computing. Importantly, a batch job is also required to specify the resources
(runtime, memory, cores, etc.) needed for the execution of the job.

This section introduces the basics of creating and submitting batch jobs using
the SLURM batch job system at CSC.

Note that also [interactive tasks](interactive-usage.md) (other than compiling,
moving data and light pre- and post-processing) are to be done via the batch
job system. See [Usage policy](../usage-policy.md) for details.

!!! warning "Key concepts of the CSC batch job system"
    1. **Jobs do not run instantly, but are put in a queue.**
        - The jobs are executed when there are resources available. The 
          starting time also depends on your job's priority score.
        - The priority score of a job exists to ensure fair sharing of
          computational resources between all the users of the cluster. Running
          a lot of jobs will decrease the initial priority score of
          your jobs. The priority score will then increase gradually as your
          job waits in the queue.
    1. **The starting time of a job cannot be predicted accurately.**
        - It depends heavily on the actual runtimes of all other users' jobs
          and whether new jobs are submitted. See
          [FAQ](../../support/faq/when-will-my-job-run.md).
    1. **Computational resources (e.g. runtime, memory, number of cores) are
       requested explicitly.**
        - If the reserved time or memory limits are exceeded, the job will be
          terminated automatically!

To get started with running your application on CSC supercomputers:

1. [Creating a batch job script for Puhti](creating-job-scripts-puhti.md)
2. [Creating a batch job script for Mahti](creating-job-scripts-mahti.md)
3. [Submit a batch job](submitting-jobs.md)
4. [Available batch job partitions](batch-job-partitions.md)
5. [Performance checklist](performance-checklist.md)

If you are already familiar with SLURM, check out our
[example batch job scripts for Puhti](example-job-scripts-puhti.md) or
[example batch job scripts for Mahti](example-job-scripts-mahti.md).

!!! info "Getting started with LUMI"
    Please see the
    [LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/slurm-quickstart/)
    for how to get started with running jobs on the LUMI supercomputer. LUMI
    also uses the SLURM batch queue system, so the differences between running
    on CSC supercomputers and LUMI are minor.
