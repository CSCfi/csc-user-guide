# Performance Checklist

This page collects important information to enable maximum performance
for your jobs and the system. If you know how to improve job performance,
please contribute to the list!


## Check CPU Affinity

CPU affinity describes how a running program is placed on
the available CPU cores of a supercomputer node.
In high‑performance computing, setting affinity correctly is important for performance.
It helps programs make better use of fast processor caches and memory,
reduces unnecessary movement between cores, and leads to more stable and predictable runtimes.

Please see the [CPU affinity tutorial](../../support/tutorials/affinity.md) for
instructions how to inspect and control CPU affinity of the programs.


## Perform a scaling test

It is important to make sure that your job can efficiently use
all the allocated resources (cores). This needs to be verified for
each new code and job type (different input) by a scaling test.
Scaling tests using full nodes apply only for jobs requesting
full nodes.

If possible, run a _short_ simulation with an increasing number of resources (cores)
and evaluate how much faster your job gets. It should get at least
1.5 times faster when you double the resources (cores). Don't allocate
more resources to your job that it can use efficiently. If scaling tests are not
practical, first run your job with less resources, and note the performance.
Try increasing the resources and confirm that the job (or a similar job)
completes faster.

Note, that not all codes or job types can be run in parallel. Confirm this first
for your code.


## Mind your I/O - it can make a big difference

If your workload writes or reads a large number of small files then you may
see poor I/O performance even if the total volume is not that big. Please
consider the following items to mitigate potential bottlenecks:

* Use local storage for especially AI workloads instead of scratch. Only some
  nodes have [fast local disk](creating-job-scripts-puhti.md#local-storage),
  but we've seen 10-fold performance improvement by switching to use it. Check
  your performance: don't use the resource if it doesn't help.
  [AI batch job example](../../support/tutorials/ml-data.md#fast-local-drive-puhti-and-mahti-only)
* Investigate if you can choose how your application does I/O (e.g. OpenFoam
  can use the collated file format) and don't write unnecessary information
  on disk or do it too often (e.g. GROMACS with the `-v` flag should not be
  used at CSC).
* One way to avoid a large number of (small) files is to set up your complex
  python or R based software in a singularity container. This also helps with
  the [file number quotas](../disk.md) on projappl. Detailed examples on how
  to do this are being written.

For applications writing and reading large files, I/O performance can be often
improved by proper Lustre settings:

* If your application performs parallel I/O, set a proper stripe count
  with `lfs setstripe -c`, more details in
  [Lustre best practices](../lustre.md#best-practices).
* Use collective parallel I/O if possible.
* See also more extensive
  [I/O optimization hints](../../support/tutorials/lustre_performance.md).


