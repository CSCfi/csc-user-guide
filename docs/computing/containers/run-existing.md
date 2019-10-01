# Running existing containers

Puhti supports running [Singularity](https://sylabs.io/singularity/) containers.  The easiest option is to build containers from existing Docker images.


## Building containers from existing Docker images

Singularity containers are typically built from Docker images, and the easiest way to get started is to use a pre-build Docker image.  For example Nvidia has a library of container images for different GPU-enabled applications in their [Nvidia GPU cloud (NGC)](https://ngc.nvidia.com/).

Here is an example how to build a Singluarity image from Nvidia's PyTorch Docker image on a Puhti compute node:

```bash
# We'll reserve 100GB NVME for fast temporary disk space
srun -A <project> --gres=nvme:100 -t 30:00 --mem=16G --pty $SHELL

# Let's use the NVME space as $TMPDIR
export TMPDIR=$LOCAL_SCRATCH

# This is just to avoid some annoying warnings
unset XDG_RUNTIME_DIR PROMPT_COMMAND

# Do the actual conversion
# NOTE: the Docker image is downloaded straight from NGC
singularity build pytorch_19.09-py3.sif docker://nvcr.io/nvidia/pytorch:19.09-py3
```

Note that the Singularity image `.sif` files can easily be several GB in size, so they should not be stored in your home directory, but in a [project scratch](/computing/disk/#scratch-directory) or [projappl](/computing/disk/#projappl-directory) folder.

## Run batch job using a container

To run a slurm batch job using a container you just need to add `singularity exec` to the place in your slurm script where you are executing the command.

For example, to a run a GPU job with the PyTorch image created above you could use the following script:

```bash
#!/bin/bash
#SBATCH -A <project> -c 10 -p gpu --gres=gpu:v100:1 -t 1:00:00 --mem=16G

srun singularity exec --nv --bind /projappl:/projappl --bind /scratch:/scratch \
    /path/to/pytorch_19.09-py3.sif \
    myprog <options>
```

Note that we use `--bind` to map `/projappl` and `/scratch` so that they are visible in the Singularity environment.  The `--nv` flag is only needed for GPU jobs.
