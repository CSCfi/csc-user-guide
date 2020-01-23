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
(unnecessary) communication in the system interconnect. This should be avoided. This also
fragments the system increasing queuing times for large jobs.

Instead, it is recommended to request full nodes by:
```
#SBATCH --nodes=5
#SBATCH --ntasks-per-node=40
```
If your core requirement is not a multiple of 40, you can limit the maximum spread
by combining:
```
#SBATCH --ntasks=128
#SBATCH --nodes=4
```

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
