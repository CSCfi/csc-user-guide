# Performance Checklist

This page collects important information to enable maximum performance
for your jobs and the system. If you know how to improve job performance,
please contribute to the list!

## Limit unnecessary spreading of parallel tasks
It is important to make sure that your job can efficiently use
all the allocated resources (cores). This needs to be verified for
each new code and job type (different input) by a scaling test.
One of the limiting factors for strong scaling is the communication
between tasks. Communication within a node is faster than between
nodes. It is optimal to use as few nodes as possible.

If resources are requested simply by:
```
#SBATCH --ntasks=200
```
the queuing system may spread them on tens of nodes (just a few cores each).
This will be very bad for the performance of the job, and will cause a lot of
communication in the system interconnect. This should be avoided. Instead,
it is recommended to request full nodes by:
```
#SBATCH --nnodes=5
#SBATCH --ntasks-per-node=40
```
If your core needs are not multiples of 40, you can limit the maximum spread
by combining:
```
#SBATCH --ntasks=128
#SBATCH --nnodes=4
```

