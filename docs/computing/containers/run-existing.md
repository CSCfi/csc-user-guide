# Running existing containers

Puhti supports running [Singularity](https://sylabs.io/singularity/) containers.  The easiest option is to build containers from existing Docker images.


## Building containers from existing Docker images

Singularity containers are typically built from Docker images, and the easiest way to get started is to use a pre-built Docker image.  For example Nvidia has a library of container images for different GPU-enabled applications in their [Nvidia GPU cloud (NGC)](https://ngc.nvidia.com/).

Here is an example how to build a Singularity image from Nvidia's PyTorch Docker image on a Puhti compute node:

```bash
# We'll reserve 100GB NVME for fast temporary disk space
srun -A <project> --gres=nvme:100 -t 1:00:00 --mem=16G --pty $SHELL

# Let's use the NVME space for temporary storage
export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH

# This is just to avoid some annoying warnings
unset XDG_RUNTIME_DIR PROMPT_COMMAND

# Do the actual conversion
# NOTE: the Docker image is downloaded straight from NGC
singularity build pytorch_19.10-py3.sif docker://nvcr.io/nvidia/pytorch:19.10-py3
```

Note that the Singularity image `.sif` files can easily be several GB in size, so they should not be stored in your home directory, but for example in the project appliction directory [projappl](/computing/disk). 

## Run batch job using a container

To run a slurm batch job using a container you just need to add `singularity exec` to the place in your slurm script where you are executing the command.

For example, to a run a GPU job with the PyTorch image created above you could use the following script:

```bash
#!/bin/bash
#SBATCH --account=<project> 
#SBATCH --cpus-per-task=10 
#SBATCH --partition=gpu 
#SBATCH --gres=gpu:v100:1 
#SBATCH --time=10
#SBATCH --mem=16G  # Total amount of memory reserved for job

srun singularity exec --nv --bind /projappl:/projappl --bind /scratch:/scratch \
    /path/to/pytorch_19.10-py3.sif \
    python3 myprog <options>
```

Note that we use `--bind` to map `/projappl` and `/scratch` so that they are visible in the Singularity environment.  The `--nv` flag is only needed for GPU jobs.
