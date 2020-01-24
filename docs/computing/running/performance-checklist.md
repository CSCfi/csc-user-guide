# Performance Checklist

This page collects important information to enable maximum performance
for your jobs and the system. If you know how to improve job performance,
please contribute to the list!

## Limit unnecessary spreading of parallel tasks
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
Since, Puhti is currently fragmented, requesting full nodes may mean longer queuing
time, but it may be regained by faster execution. If queuing times this way seem
unaccecptable, you can still limit the maximum number of nodes the job can spread on.
For example, limiting the 200 task job (which optimally fits on 4 nodes) to a maximum
of 10 nodes, you could use:

```
#SBATCH --ntasks=200
#SBATCH --nodes=4-10
```
Slurm will then allocate 200 cores from 4 to 10 nodes for your job.


## Perform a scaling test
It is important to make sure that your job can efficiently use
all the allocated resources (cores). This needs to be verified for
each new code and job type (different input) by a scaling test.

Run a _short_ simulation with an increasing number of resources (cores)
and evaluate how much faster your job gets. It should get at least
1.5 times faster when you double the resources (cores). Don't allocate
more resources to your job that it can use efficiently.

Note, that not all codes or job types can be run in parallel. Confirm this first
for your code.
