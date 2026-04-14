# Inspecting and Controlling CPU Affinity

CPU affinity describes how a running program is placed on
the available CPU cores of a supercomputer node.
By controlling affinity, we decide which CPU cores a program is allowed to run on,
limiting or fixing its placement rather than leaving it entirely to the system.

In high‑performance computing, setting affinity correctly is important for performance.
It helps programs make better use of fast processor caches and memory,
reduces unnecessary movement between cores, and leads to more stable and predictable runtimes.

## Inspecting and Controlling CPU Affinity of OpenMP Applications

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

Together, these settings allow you to verify thread placement and confirm that affinity is applied as expected,
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

If we had not set `OMP_PLACES=cores; OMP_PROC_BIND=spread`, then the output would look like this:

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
which can lead to worse performance due to increased context switching and thread migration during execution, as opposed to a case where threads are bound to single cores.

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


## Inspecting CPU Affinity in General

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

Example output for a job running on two nodes with eight tasks per node and 48 cores per task (`--nodes=2 --ntasks-per-node=8 --cpus-per-task=48 --hint=nomultithread`):

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

This output shows that CSC supercomputers are configured so that, by default, each Slurm task is assigned
its own exclusive set of CPU cores from the allocation.
The number of cores reserved per task is determined by the Slurm option `cpus-per-task`.

### Advanced: Controlling CPU Affinity Manually

> Note
> This section describes **advanced, manual control of CPU affinity**.
> In practice, this is **rarely needed**, and the default Slurm configuration is best for most workloads.
> If you believe you need manual CPU binding, [**please contact us first**](../contact.md) for guidance.

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

This produces output equivalent to the default CPU binding seen above,
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
