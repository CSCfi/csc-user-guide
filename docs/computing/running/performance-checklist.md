# Performance Checklist

This page collects important information to enable maximum performance
for your jobs and the system. If you know how to improve job performance,
please contribute to the list!

## Limit unnecessary spreading of parallel tasks in Puhti
One of the limiting factors for strong scaling is the communication
between tasks. Communication within a node is faster than between
nodes. It is optimal to use as few nodes as possible.

If resources are requested simply by:
```
#SBATCH --ntasks=200
```
the queuing system may spread them on tens of nodes (just a few cores each).
This will be very bad for the performance of the job, and will cause a lot of
(unnecessary) communication in the system interconnect. If the performance of
your parallel jobs has decreased, this could be the reason.
Overall, this should be avoided. This also
fragments the system increasing queuing times for large jobs.

The best performance (fastest communication) can be achieved by requesting
full nodes:
```
#SBATCH --nodes=5
#SBATCH --ntasks-per-node=40
```
Since Puhti is currently fragmented, requesting full nodes may mean longer queuing
time, but it may be regained by faster execution. If queuing times this way seem
unacceptable, you can still limit the maximum number of nodes the job can spread on.
For example, limiting the 200 task job (which optimally fits on 5 nodes) to a maximum
of 10 nodes, you could use:

```
#SBATCH --ntasks=200
#SBATCH --nodes=5-10
```
Slurm will then allocate 200 cores from 5 to 10 nodes for your job.

### How many nodes to allow?
If full nodes or the minimum is not suitable, it is probably best to try
and monitor job performance. Choosing too many nodes will deteriorate
performance more than is gained by less queuing. Note also that overall this is lost
computer capacity.

Perhaps, a rule of thumb could be
to set the upper limit to 2 or 3 times the number which would accommodate
all tasks. With very large parallel jobs, even smaller is recommended as
communication and the likelihood of one slow node in the allocation gets
higher and poor load balancing gets more likely. Anyway, large parallel jobs
should be run in Mahti.

## Hybrid parallelization in Mahti

Many HPC applications benefit from binding OpenMP threads to CPU cores
which can be achieved by setting `export OMP_PLACES=cores` in the
batch job script.

When starting new production runs it is also good
practice to ensure correct thread affinity by adding to batch job
script
```
export OMP_AFFINITY_FORMAT="Process %P level %L thread %0.3n affinity %A"
export OMP_DISPLAY_AFFINITY=true
```
The runtime affinity will be printed to the standard error of the batch
job. If the output shows that several processes/threads are bound to
the same core, *i.e.*
```
Process 164433 level 1 thread 000 affinity 0
Process 164433 level 1 thread 001 affinity 0
```
the performance might be deteriorated and one should check the settings
in the batch script.


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
