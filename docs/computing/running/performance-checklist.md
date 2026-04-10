# Performance Checklist

This page collects important information to enable maximum performance
for your jobs and the system. If you know how to improve job performance,
please contribute to the list!


## Check CPU Affinity

CPU affinity describes how a running program is placed on
the available processor cores of a supercomputer node.
By default, the operating system is free to move a program (and its processes and threads)
between CPU cores as it sees fit, which can be detrimental for performance in
a supercomputing environment.

By controlling affinity, we instead decide which CPU cores a program is allowed to run on,
limiting or fixing its placement rather than leaving it entirely to the system.
In high‑performance computing, setting affinity correctly is important for performance.
It helps programs make better use of fast processor caches and memory,
reduces unnecessary movement between cores, and leads to more stable and predictable runtimes.

### Inspecting and Controlling CPU Affinity of OpenMP Applications

Many HPC applications benefit from binding OpenMP threads to CPU cores,
which can be achieved by adding the following line to the batch job script:
```bash
# Place and bind threads to single cores
export OMP_PLACES=cores
export OMP_PROC_BIND=spread
```

It is also good practice to ensure correct thread affinity by adding the following lines to the batch job script:
```bash
export OMP_DISPLAY_AFFINITY=true
export OMP_AFFINITY_FORMAT="Process %P level %L thread %0.4n/%0.4N on node %H core %A"
```

Together, these settings allow to verify thread placement and confirm that affinity is applied as expected,
which is often a key step when diagnosing or optimizing performance on a supercomputer.

Example output for a job running on one node with two tasks and 8 cpus per task (`--nodes=1 --ntasks-per-node=2 --cpus-per-task=8 --hint=nomultithread`).
By default, the number of threads is set to match the `cpus-per-task` option:

```txt
Process 2808761 level 1 thread 0000/0004 on node rc6224 core 0
Process 2808761 level 1 thread 0001/0004 on node rc6224 core 1
Process 2808761 level 1 thread 0002/0004 on node rc6224 core 2
Process 2808761 level 1 thread 0003/0004 on node rc6224 core 3
Process 2808762 level 1 thread 0000/0004 on node rc6224 core 4
Process 2808762 level 1 thread 0001/0004 on node rc6224 core 5
Process 2808762 level 1 thread 0002/0004 on node rc6224 core 6
Process 2808762 level 1 thread 0003/0004 on node rc6224 core 7
```

This output means that each thread is bound to its own core.

If we had not set `OMP_PLACES=cores`, then the output would look like this:

```txt
Process 2808761 level 1 thread 0000/0004 on node rc6224 core 0-3
Process 2808761 level 1 thread 0001/0004 on node rc6224 core 0-3
Process 2808761 level 1 thread 0002/0004 on node rc6224 core 0-3
Process 2808761 level 1 thread 0003/0004 on node rc6224 core 0-3
Process 2808762 level 1 thread 0000/0004 on node rc6224 core 4-7
Process 2808762 level 1 thread 0001/0004 on node rc6224 core 4-7
Process 2808762 level 1 thread 0002/0004 on node rc6224 core 4-7
Process 2808762 level 1 thread 0003/0004 on node rc6224 core 4-7
```

This output means that threads of the processes are free to move between the sets of four cores (0-3 or 4-7),
which might not be optimal for performance.

If the output would show that several processes or threads are bound to the same core on the same node, for example
```txt
Process 2808761 level 1 thread 0000/0004 on node rc6224 core 0
Process 2808761 level 1 thread 0001/0004 on node rc6224 core 1
Process 2808761 level 1 thread 0002/0004 on node rc6224 core 2
Process 2808761 level 1 thread 0003/0004 on node rc6224 core 3
Process 2808762 level 1 thread 0000/0004 on node rc6224 core 0
Process 2808762 level 1 thread 0001/0004 on node rc6224 core 1
Process 2808762 level 1 thread 0002/0004 on node rc6224 core 2
Process 2808762 level 1 thread 0003/0004 on node rc6224 core 3
```
or
```txt
Process 2808761 level 1 thread 0000/0004 on node rc6224 core 0
Process 2808761 level 1 thread 0001/0004 on node rc6224 core 0
Process 2808761 level 1 thread 0002/0004 on node rc6224 core 0
Process 2808761 level 1 thread 0003/0004 on node rc6224 core 0
Process 2808762 level 1 thread 0000/0004 on node rc6224 core 0
Process 2808762 level 1 thread 0001/0004 on node rc6224 core 0
Process 2808762 level 1 thread 0002/0004 on node rc6224 core 0
Process 2808762 level 1 thread 0003/0004 on node rc6224 core 0
```
or something similar, then the performance is likely deteriorated
and the settings in the batch script should be fixed.


### Inspecting CPU Affinity in General

The `OMP_*` environment variables are specific to OpenMP and do not work with non-OpenMP applications.

The following example job script can be used for checking the CPU affinities of each Slurm task.
The job script creates a script `print_affinity.<jobid>.sh` that is then executed via `srun`:

```bash
#!/bin/bash
#SBATCH ...

# Create a script for printing affinity
PRINT_AFFINITY="./print_affinity.$SLURM_JOB_ID.sh"
cat << 'EOF' > $PRINT_AFFINITY
#!/bin/bash
printf "Task %4d running on node %s core %s\n" \
  "$SLURM_PROCID" \
  "$SLURMD_NODENAME" \
  "$(grep Cpus_allowed_list /proc/self/status | cut -f2)"
EOF
chmod +x $PRINT_AFFINITY

# Remove script on exit
trap "rm -f $PRINT_AFFINITY" EXIT

# Run the program
srun $PRINT_AFFINITY
```

Example output for a job running on two nodes with eight task per node and 48 cores per task (`--nodes=2 --ntasks-per-node=8 --cpus-per-task=48 --hint=nomultithread`):

```txt
Task   10 running on node rc6284 core 96-143
Task   11 running on node rc6284 core 144-191
Task    9 running on node rc6284 core 48-95
Task   15 running on node rc6284 core 336-383
Task   12 running on node rc6284 core 192-239
Task   13 running on node rc6284 core 240-287
Task   14 running on node rc6284 core 288-335
Task    8 running on node rc6284 core 0-47
Task    7 running on node rc6283 core 336-383
Task    1 running on node rc6283 core 48-95
Task    3 running on node rc6283 core 144-191
Task    6 running on node rc6283 core 288-335
Task    4 running on node rc6283 core 192-239
Task    2 running on node rc6283 core 96-143
Task    5 running on node rc6283 core 240-287
Task    0 running on node rc6283 core 0-47
```

This output shows that CSC supercomputers are configured so that by default each Slurm task is assigned
its own exclusive set of CPU cores from the allocation.
The number of cores reserved per task is determined by the Slurm option `cpus-per-task`.

### Advanced: Controlling CPU Affinity Manually

> Note
> This section describes **advanced, manual control of CPU affinity**.
> In practice, this is **rarely needed**, and the default Slurm configuration is best for most workloads.
> If you believe you need manual CPU binding, **please contact us first** for guidance.

If a different placement strategy is needed, the default CPU binding can be disabled by `srun --cpu-bind=none`.
This removes all CPU affinity restrictions, allowing processes to run on **any allocated core on the node**.
This is **generally undesirable for performance** unless combined with explicit manual binding,
which can be done using tools such as numactl.

The following job script provides an example for setting CPU binding manually.
The job script creates two scripts: `print_affinity.<jobid>.sh` and `cpu_bind.<jobid>.sh`.
The first script is the same script used above for checking affinities and the second script
uses numactl for binding tasks to CPU cores in the same way as done by default:
each task is assined a contiguous block of CPU cores based on the task's local ID and
the number of CPUs per task:

```bash
#!/bin/bash
#SBATCH ...

# Create a script for printing affinity
PRINT_AFFINITY="./print_affinity.$SLURM_JOB_ID.sh"
cat << 'EOF' > $PRINT_AFFINITY
#!/bin/bash
printf "Task %4d running on node %s core %s\n" \
  "$SLURM_PROCID" \
  "$SLURMD_NODENAME" \
  "$(grep Cpus_allowed_list /proc/self/status | cut -f2)"
EOF
chmod +x $PRINT_AFFINITY

# Create a script for binding tasks to CPU cores
BIND_CPU="./bind_cpu.$SLURM_JOB_ID.sh"
cat << 'EOF' > $BIND_CPU
#!/bin/bash
cpus_per_task=${SLURM_CPUS_PER_TASK:-1}
start_core=$((SLURM_LOCALID * cpus_per_task))
end_core=$((SLURM_LOCALID * cpus_per_task + cpus_per_task - 1))
numactl --physcpubind ${start_core}-${end_core} "$@"
EOF
chmod +x $BIND_CPU

# Remove scripts on exit
trap "rm -f $PRINT_AFFINITY $BIND_CPU" EXIT

# Run the program with manual binding
srun --cpu-bind=none $BIND_CPU $PRINT_AFFINITY
```

This produces output equivalent to the default CPU binding,
confirming that the manual placement reproduces the standard behaviour:

```txt
Task    4 running on node rc6283 core 192-239
Task    6 running on node rc6283 core 288-335
Task    7 running on node rc6283 core 336-383
Task    5 running on node rc6283 core 240-287
Task    0 running on node rc6283 core 0-47
Task    1 running on node rc6283 core 48-95
Task    2 running on node rc6283 core 96-143
Task    3 running on node rc6283 core 144-191
Task   15 running on node rc6284 core 336-383
Task    8 running on node rc6284 core 0-47
Task    9 running on node rc6284 core 48-95
Task   10 running on node rc6284 core 96-143
Task   11 running on node rc6284 core 144-191
Task   12 running on node rc6284 core 192-239
Task   13 running on node rc6284 core 240-287
Task   14 running on node rc6284 core 288-335
```

If needed, the logic in the binding script can be modified to bind CPU cores according to the needs of your application.


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


