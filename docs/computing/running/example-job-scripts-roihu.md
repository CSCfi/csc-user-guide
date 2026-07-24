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

## Fast disk (NVMe over Fabric)

!!! info "Work in progress"
    This section is a work in progress.

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

!!! note "Aggregated storage is only available on full node partitions"
    At the present you can only request this storage for jobs that are making use of full nodes,
    i.e. that are submitted in the `medium` or `large` partitions. Presently if you try to launch in other partitions,
    your job will fail, but will be marked "CANCELLED by 350" and you will lack any stdout or stderr
    logs. This should be resolved once **support for shared node jobs arrives in Q3 2026**.

See [detailed usage instructions](../roihu-disk.md#disaggregated-storage).