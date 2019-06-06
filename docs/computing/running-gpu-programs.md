# Running GPU programs

## Introduction
It is always recommended to use SLURM batch job file for running GPU specific jobs. However, for quick tests also
```batch
srun
```
command would be acceptable. When running GPU applications the batch queue (or partition) in concern need to be either *gpu*, *gputest*, *gpulong*. Which partition used is set using
```batch
-p queue_name
```
What type of GPU used is set using a generic resource (GRES) flag:
```batch
--gres=gpu:type:n
```
Where type is the type of GPU requested per compute node, currently valid values are k80 or p100 and <var>n</var> is the number of GPUs to reserve per node. On the K80 and P100 nodes one can reserve up to 4 GPUs. The *gpu* and *gpulong* partition is intended for production runs while *gputest* is intended for short (less than 15 min) test and development runs.
To request 2 K80 GPUs use
```batch
--gres=gpu:k80:2
```
or to request 4 P100 GPUs use
```batch
--gres=gpu:p100:4
```

## Running under GNU environment on one GPU
Here is a valid script for running under GNU environment that will default any GPU available:
```
#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p gpu
#SBATCH -t 00:05:00
#SBATCH -J gpu_job
#SBATCH -o gpu_job.out.%j
#SBATCH -e gpu_job.err.%j
#SBATCH --gres=gpu:k80:1
#SBATCH

module purge
module load gcc cuda
module list

srun ./your_binary
```

## Running under PGI environment on one GPU
The batch job script is very similar as in the GPU environment, the only difference is that different module needs to be loaded. And executable name is also different.
```
#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p gpu
#SBATCH -t 00:05:00
#SBATCH -J gpu_job
#SBATCH -o gpu_job.out.%j
#SBATCH -e gpu_job.err.%j
#SBATCH --gres=gpu:k80:1
#SBATCH

module purge
module load pgi cuda/7.5
module list

srun ./your_binary
```

## Running under GNU environment on multiple GPUs
Here is a valid script for running under GNU environment, on 2 GPUs on a K80 node:
```
#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p gpu
#SBATCH -t 00:05:00
#SBATCH -J gpu_job
#SBATCH -o gpu_job.out.%j
#SBATCH -e gpu_job.err.%j
#SBATCH --gres=gpu:k80:2
#SBATCH

module purge
module load gcc cuda
module list

srun ./your_binary
```
Here is a valid script for running under GNU environment, on 4 GPUs on K80 a node:
```
#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p gpu
#SBATCH -t 00:05:00
#SBATCH -J gpu_job
#SBATCH -o gpu_job.out.%j
#SBATCH -e gpu_job.err.%j
#SBATCH --gres=gpu:k80:4
#SBATCH

module purge
module load gcc cuda
module list

srun ./your_binary
```

## Using the SSD scratch space
Each P100 node is equipped with 800 GB of fast SSD storage (Sata SSDs) intended as a scratch space. While the K80 nodes have 850 GB of space consisting of a regular hard drive. This space is placed under the <var>${TMPDIR}</var> directory and in that directory there will be a folder with the name of the slurm job id, accessible from the <var>${SLURM_JOB_ID}</var> enviroment variable. It is this folder that should be used as a scratch space so to access it easily use <var>${TMPDIR}/${SLURM_JOB_ID}</var>. The space is local to each compute node meaning that it is shared among all the users of that node and in multi node jobs each node only has access to its own local scratch space and this cannot be accessed from other compute nodes.**To use this space the user needs to move data there in the beginning of the job script and any data the user wants to retain needs to be transferred from the scratch space before the job finishes, once the job ends the files on the SSD space are removed.**

If you are moving a lot of smaller files to the scratch space it the recommended work flow is:

- You first make a tar file out of them, outside of any batch job, place this tar file in the <var>${WRKDIR}</var> directory.
- Then as part if your batch job you copy the tar file to the scratch space.
- And finally still as part if your batch job you extract that tar file still to the scratch sapce.
	
For single node jobs data can be transferred to the <var>${TMPDIR}</var> location with normal file copy commands. These commands need to be run in the job script as you do not have access to the <var>${TMPDIR}</var> directory from outside the job. Below is an example for a single node script.
```
#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p gpu
#SBATCH -t 00:05:00
#SBATCH -J gpu_job
#SBATCH -o gpu_job.out.%j
#SBATCH -e gpu_job.err.%j
#SBATCH --gres=gpu:p100:1
#SBATCH

module purge
module load cuda-env/10
module list

cp ${WRKDIR}/your_file.csv ${TMPDIR}/${SLURM_JOB_ID}/your_file.csv
srun ./your_binary
```
For jobs using multiple compute nodes the copy command needs to be run on all nodes participating in the job, so we need to use srun to run the commands.
```
#!/bin/bash
#SBATCH -N 2
#SBATCH -n 2
#SBATCH -p gpu
#SBATCH -t 00:05:00
#SBATCH -J gpu_job
#SBATCH -o gpu_job.out.%j
#SBATCH -e gpu_job.err.%j
#SBATCH --gres=gpu:p100:1
#SBATCH

module purge
module load cuda-env/10
module list

srun -N ${SLURM_JOB_NUM_NODES}-${SLURM_JOB_NUM_NODES} -n ${SLURM_JOB_NUM_NODES} cp ${WRKDIR}/your_file.csv ${TMPDIR}/${SLURM_JOB_ID}/your_file.csv

srun ./your_binary
```
