# Getting started

CSC uses a batch job system to execute computing tasks on our supercomputers.

Typically, a batch job first loads a software environment using the
[module system](../modules.md) and then executes a program to do some
computing. A batch job has to also specify the resources needed for the
execution of the job.

This chapter goes through the basics of creating and submitting batch jobs
using the SLURM (Simple Linux Utility for Resource Management) batch job
system.

!!! Key concepts of the CSC batch job system:

    - **Jobs do not run instantly, but are put in a queue**
        - Jobs are executed when there are available resources and depending
          on a priority score
        - The priority score for a job exists to ensure fair sharing of
          computational resources between all the users of the cluster
    - **The start time for a job can't be predicted**
        - Depends heavily on actual runtimes for all user jobs and submission
          of new jobs
    - **Computational resources (runtime, memory, number of cores) are requested explicitly**
        - if the time or memory limits are exceeded, the job will terminated

To get started with running your application, you need to:

1. [Create a batch job script](creating-job-scripts.md)
2. [Submit a batch job](submitting-jobs.md)

If you are already familiar with SLURM, you can also just look at our
[example batch job scripts](example-job-scripts.md).
