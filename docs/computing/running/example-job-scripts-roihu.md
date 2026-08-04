# Example batch job scripts for Roihu

Example job scripts for running different types of programs:

[TOC]

!!! note
    If you use the scripts (please do!), do not forget to change the resources
    (time, tasks etc.) to match your needs and to replace `myprog <options>`
    with the executable (and options) of the program you wish to run as well
    as `<project>` with the name of your project.

## Roihu-CPU

### Serial CPU

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1000M

# Run the program
srun myprog <options>
```

### Partial CPU node: MPI

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --mem-per-cpu=1000M

# Run the program
srun myprog <options>
```

### Partial CPU node: OpenMP

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

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

### Partial CPU node: MPI+OpenMP

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

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

### Full CPU nodes: MPI

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
##SBATCH --partition=large  # uncomment if using 6 or more nodes
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=384 --cpus-per-task=1  # The product should be 384

# Run the program
srun myprog <options>
```

### Full CPU nodes: OpenMP

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
##SBATCH --partition=large  # uncomment if using 6 or more nodes
#SBATCH --time=00:30:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1 --cpus-per-task=384  # The product should be 384

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

### Full CPU nodes: MPI+OpenMP

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

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

## Roihu-GPU

### Partial GPU nodes: 1-16 GPUs

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

### Full GPU nodes: 16 or more GPUs

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

### GPU slices

!!! info "Work in progress"
    This section is work in progress.
    GPU slices have not yet been configured on the system.

## Disaggregated storage / Fast disk (NVMe over Fabric)

On Roihu, it is possible to request local disk mounts from a centralised pool of fast storage resources. 
This fast storage capacity is provided over the network and will appear as local scratch from 
within a Slurm job.

Example script reserving 10G of fast NVMe disk space:

```bash
#!/bin/bash
#SBATCH --job-name=example
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4 --cpus-per-task=96
#SBATCH --bb="#BB_LUA SBF storagesize=10G path=/run/sbb/<user>" 

# Set the number of CPU threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind CPU threads to single CPU cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

# Run the program
srun myprog <options>
```

!!! warning "Disaggregated storage is currently only available on full node jobs"
    
    At present this storage can only be requested if you are the sole tenant on a compute node, i.e.
    if you are submitting to the `medium` and `large` partitions on the CPU side, or by requesting
    nodes with the `--exclusive` flag on the GPU partitions.

    Improper requests for disaggregated storage may fail with the job reported as `CANCELLED by 350`, 
    without producing standard output or error logs.
    Support for shared-node jobs is expected in Q3 2026 or when the service is ready.


See [detailed usage instructions](../roihu-disk.md#disaggregated-storage).
