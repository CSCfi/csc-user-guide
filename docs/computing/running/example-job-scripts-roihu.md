# Example batch job scripts for Roihu

Example job scripts for running different types of programs:

[TOC]

!!! note
    If you use the scripts (please do!), do not forget to change the resources
    (time, tasks etc.) to match your needs and to replace `myprog <options>`
    with the executable (and options) of the program you wish to run as well
    as `<project>` with the name of your project.

## Pilot projects

During the pilot period, pilot users will have access to separate `pilot` and `gpupilot` partitions. 
These partitions allow you to run larger test cases on both Roihu-CPU (up to 200 nodes) and Roihu-GPU (up to 60 nodes).

See [job time and node limits in the pilot partitions.](batch-job-partitions.md#roihu-pilot-partitions)

Pilot partitions will provide you with full nodes and may experience long queue times during peak use.
Normal partitions (see examples below) are still available during the pilot projects, and are
recommended to use especially for smaller scale and routine runs. 

### Example pilot project CPU job script (MPI+OpenMP)

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=pilot
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=384 --cpus-per-task=1  # The product should be 384
###SBATCH --ntasks-per-node=192 --cpus-per-task=2  # The product should be 384
###SBATCH --ntasks-per-node=96 --cpus-per-task=4  # The product should be 384
#SBATCH --hint=nomultithread
#SBATCH --mem=744G  # Ensure we use all available memory on the nodes

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single hardware threads
# Comment the following lines if binding is not desired
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

In the above, set the MPI task (`--ntasks`) and OpenMP thread (`--cpus-per-task`) counts to best
fit your program, while ensuring that the total cpu count is using all 384 cores
on your nodes.

### Example pilot project GPU job script

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpupilot
#SBATCH --time=00:30:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=4 --cpus-per-task=72  # The product should be 288
#SBATCH --gres=gpu:gh200:4  # 4 GPUs per node

# Set the number of CPU threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind CPU threads to single CPU cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Serial CPU

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1000M
#SBATCH --hint=nomultithread

# Run the program
srun myprog <options>
```

## Partial CPU node: MPI

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --mem-per-cpu=1000M
#SBATCH --hint=nomultithread

# Run the program
srun myprog <options>
```

## Partial CPU node: OpenMP

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=1000M
#SBATCH --hint=nomultithread

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Partial CPU node: MPI+OpenMP

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=1000M
#SBATCH --hint=nomultithread

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Partial CPU node: MPI+OpenMP with simultaneous multithreading

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=4
#SBATCH --hint=multithread

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single hardware threads
# Comment the following lines if binding is not desired
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Full CPU nodes: MPI

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
##SBATCH --partition=large  # uncomment if using 6 or more nodes
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=384 --cpus-per-task=1  # The product should be 384
#SBATCH --hint=nomultithread
#SBATCH --mem=744G

# Run the program
srun myprog <options>
```

## Full CPU nodes: OpenMP

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
##SBATCH --partition=large  # uncomment if using 6 or more nodes
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1 --cpus-per-task=384  # The product should be 384
#SBATCH --hint=nomultithread
#SBATCH --mem=744G

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Full CPU nodes: MPI+OpenMP

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
##SBATCH --partition=large  # uncomment if using 6 or more nodes
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=192 --cpus-per-task=2  # The product should be 384
#SBATCH --ntasks-per-node=96  --cpus-per-task=4  # The product should be 384
#SBATCH --hint=nomultithread
#SBATCH --mem=744G

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Full CPU nodes: MPI+OpenMP with simultaneous multithreading

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
##SBATCH --partition=large  # uncomment if using 6 or more nodes
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=384 --cpus-per-task=2  # The product should be 768
#SBATCH --ntasks-per-node=192 --cpus-per-task=4  # The product should be 768
#SBATCH --hint=multithread
#SBATCH --mem=744G

# Set the number of CPU threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind CPU threads to single CPU cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## GPU slices

!!! info "Work in progress"
    This section is work in progress.


## Partial GPU nodes: 1-16 GPUs

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpumedium
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1 --cpus-per-task=72  # The product should be 72 if requesting 1 GPU per node
#SBATCH --gres=gpu:gh200:1  # Corresponds to 1 GPU per node

# Set the number of CPU threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind CPU threads to single CPU cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Full GPU nodes: 16 or more GPUs

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=gpularge
#SBATCH --time=00:30:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=4 --cpus-per-task=72  # The product should be 288
#SBATCH --gres=gpu:gh200:4  # 4 GPUs per node

# Set the number of CPU threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind CPU threads to single CPU cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Fast disk (NVMe over Fabric)

!!! info "Work in progress"
    This section is work in progress.
