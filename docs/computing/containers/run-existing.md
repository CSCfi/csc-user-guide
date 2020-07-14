# Running existing containers

Puhti supports running [Singularity](https://sylabs.io/singularity/) containers. For some use cases, CSC's staff has provided ready-made Singularity containers that can be used simply by loading the right module. Please check the [application pages](../../apps/index.md) if a pre-installed container is already available, and see the specific application's page for instructions on how to use it.

If you find some image missing that you think could be generally useful, you can ask us to install it by contacting [CSC's Service Desk](https://www.csc.fi/en/contact-info).  Otherwise you can also build them yourself by converting existing Docker container images (see instructions below).


## Converting Docker images for use with Puhti

If you cannot find a suitable Singularity image among those provided by CSC's staff, you can convert it yourself from an existing Docker image.  For example, NVIDIA has a library of container images for different GPU-enabled applications in their [NVIDIA GPU cloud (NGC)](https://ngc.nvidia.com/).

Here is an example how to build a Singularity image from NVIDIA's PyTorch Docker image. We'll use `sinteractive` as heavy processing should not be done in the login nodes.

```bash
# Let's start a 1 hour interactive job
sinteractive --account <project> --time 1:00:00

# Let's use the fast local drive for temporary storage
export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH

# This is just to avoid some annoying warnings
unset XDG_RUNTIME_DIR

# Do the actual conversion
# NOTE: the Docker image is downloaded straight from NGC
singularity build pytorch_20.03-py3.sif docker://nvcr.io/nvidia/pytorch:20.03-py3
```

Note that the Singularity image `.sif` files can easily be several GB in size, so they should not be stored in your home directory, but for example in the project application directory [projappl](/computing/disk). 

To run a slurm batch job using a container you need to use the `singularity exec` command, and remember to bind all the necessary paths with the `--bind` option.  As an alternative you can also use our `singularity_wrapper` command which automatically includes all the necessary binds for CSC's environment.

For example, to a run a GPU job with the PyTorch image created above you could use the following script:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --cpus-per-task=10 
#SBATCH --partition=gputest
#SBATCH --gres=gpu:v100:1 
#SBATCH --time=15
#SBATCH --mem=16G  # Total amount of memory reserved for job

module purge

srun singularity_wrapper exec --nv /path/to/pytorch_20.03-py3.sif python3 myprog.py <options>
```

Note that the `module purge` is important as a loaded singularity-based module would override what image to use for the `singularity_wrapper` command.  The `--nv` flag is only needed for GPU jobs.
