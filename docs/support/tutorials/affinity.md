# Inspecting and Controlling CPU Affinity

This tutorial describes how CPU affinities can be inspected and controlled in job scripts on CSC supercomputers.
The tutorial scripts are written for the Roihu supercomputer, but are generally also applicable on Puhti, Mahti and LUMI.


## What is CPU Affinity?

CPU affinity describes how a running program is placed on
the available CPU cores of a supercomputer node.
By controlling affinity, we decide which CPU cores a program is allowed to run on,
limiting or fixing its placement rather than leaving it entirely to the system.

In high‑performance computing, setting affinity correctly is important for performance.
It helps programs make better use of fast processor caches and memory,
reduces unnecessary movement between cores, and leads to more stable and predictable runtimes.


## Inspecting CPU Affinity in Slurm Jobs

The following example job script can be used for checking the CPU affinities of each Slurm task.
The job script creates a script `print_affinity.<jobid>.sh` that is then executed via `srun`:

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8 --cpus-per-task=48  # The product should be 384
#SBATCH --hint=nomultithread

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

Example output for this job:

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


## Advanced: Controlling CPU Affinity Manually in Slurm Jobs

!!! warning "Advanced topic"
    This section describes **advanced, manual control of CPU affinity**.
    In practice, this is **rarely needed**, and the default Slurm configuration is best for most workloads.
    If you believe you need manual CPU binding, [**please contact us first**](../contact.md) for guidance.

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

!!! warning "Script for full nodes"
    This script works correctly only on full nodes.

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8 --cpus-per-task=48  # The product should be 384
#SBATCH --hint=nomultithread

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


## Inspecting and Controlling CPU Affinity of MPI+OpenMP Applications

Many HPC applications benefit from binding OpenMP threads to CPU cores.
This does not happen automatically but need to be enabled with the following lines in the batch job script:

```bash
# Place and bind threads to single cores
export OMP_PLACES=cores
export OMP_PROC_BIND=spread
```

This tutorial illustrates the meaning of these settings.

First, let's check the default behaviour in the case when threads are not bound.
The following job script exemplifies the use of `OMP_*` for checking the CPU affinities of each process and OpenMP thread:

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=1000M
#SBATCH --hint=nomultithread

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Print thread affinities
export OMP_DISPLAY_AFFINITY=true
export OMP_AFFINITY_FORMAT="Process %P level %L thread %0.4n/%0.4N on node %H core %A"

# Run the program
srun <my_openmp_program>
```

Example output for this job:

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

This output means that the threads of the processes are free to move between the sets of four cores (0-3 or 4-7),
which can lead to worse performance due to increased context switching and thread migration during execution,
as opposed to a case where threads are bound to single cores.

In the following example job script, we have enabled thread binding:

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=1000M
#SBATCH --hint=nomultithread

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Print thread affinities
export OMP_DISPLAY_AFFINITY=true
export OMP_AFFINITY_FORMAT="Process %P level %L thread %0.4n/%0.4N on node %H core %A"

# Run the program
srun <my_openmp_program>
```

Now the output looks like this:

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

This output means that each thread is bound to its own core, which is often desired for best performance.

In general, when starting to use a new application or configuration,
it is essential to use these settings to verify thread placement and confirm that affinity is applied as expected,
which is often a key step when diagnosing or optimizing performance on a supercomputer.

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

Please do not hesitate to [**contact us**](../contact.md) if you need help with ensuring good
performance for your application.
