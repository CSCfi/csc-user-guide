# Getting started

CSC uses a batch job systems to execute computing tasks on our supercomputers.

This chapter goes through the basics of creating and submitting batch jobs
using the SLURM (Simple Linux Utility for Resource Management) batch job
system.

**The key concepts of the CSC batch job system:**

- Jobs do not run instantly, but are put in a queue
    - Jobs are executed when there are available resources and depending on a
      priority score
    - The priority score for a job exists to ensure fair sharing of
      computational resources between all the users of the cluster
- The start time for a job can't be predicted
    - Depends heavily on actual runtimes for all user jobs and submission of
      new jobs
- Computational resources (runtime, memory, number of cores, etc. ) are
  requested explicitly.
    - If the time or memory limits are exceeded, the job will terminated.
