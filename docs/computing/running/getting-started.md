# Getting started

CSC uses a batch job system to execute computing tasks on our supercomputers.

Typically, a batch job first loads a software environment using the
[module system](../modules.md) and then executes a program to do some
computing. A batch job is also required to specify the resources needed for the
execution of the job.

This chapter introduces the basics of creating and submitting batch jobs
using the SLURM (Simple Linux Utility for Resource Management) batch job
system.

Note that also [interactive tasks](interactive-usage.md) (other than
compiling, moving data and light  pre- and postprocessing) are to be
done via batch job system. 

!!! note "Key concepts of the CSC batch job system"

    - **Jobs do not run instantly but are put in a queue**
        - The jobs are executed when there are resources available. The 
          timing also depends on the priority score.
        - The priority score for a job exists to ensure fair sharing of
          computational resources between all the users of the cluster.
    - **The starting time for a job cannot be predicted**
        - It depends heavily on the actual runtimes for all user jobs and 
          whether new jobs are submitted, see [FAQ](../../support/faq/when-will-my-job-run.md).
    - **Computational resources (runtime, memory, number of cores) are requested explicitly**
        - If the time or memory limits are exceeded, the job will be terminated.

To get started with running your application on Puhti:

1. [Create a batch job script for Puhti](creating-job-scripts-puhti.md)
2. [Submit a batch job](submitting-jobs.md)

If you are already familiar with SLURM, check out our
[example batch job scripts for Puhti](example-job-scripts-puhti.md) or
[example batch job scripts for Mahti](example-job-scripts-mahti.md).
