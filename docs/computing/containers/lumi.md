# LUMI

LUMI uses SingularityCE instead of Apptainer.
The instructions from [Apptainer containers](./overview.md) apply with certain modifications.

## Temporary directory

On LUMI, we use `/tmp` as the temporary directory.
SingularityCE bind mounts it by default to the build environment.
Therefore, manually bind mounting the temporary directory is not required.

## Cache directory

The SingularityCE cache directory can be changed if needed:

```bash
export SINGULARITY_CACHEDIR=/scratch/project_id/$USER/.singularity
```

## Build location

On the login node, we can build container images that are small enough that they do not run into memory limits.
Virtual memory in LUMI is quite large (64 GB) and preset to the hard limit, thus it is not required to adjust it.

We must build large container images on the compute node via a slurm job.
For example, we can reserve an interactive slurm job as follows, just replace `myproject` with your project:

```bash
srun --account myproject --partition small --time 0:15:00 --mem 8000 --cpus-per-task 1 --pty bash
```

On the compute node `/tmp` is a tmpfs which is limited by memory.
We must request memory that is at least twice the size of the uncompressed size of your container image (SIF file) to avoid running out of memory.

## Building an SIF image

In LUMI, we need to use [proot](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/s/systools/#the-proot-command) to build SIF images with SingularityCE.
We can load proot as follows:

```bash
module load LUMI systools
```

Then, we can build container images in the standard way as follows:

```bash
singularity build container.sif container.def
```

Do not use the `--fakeroot` flag with SingularityCE in LUMI, as it does not behave in the same way as with Apptainer.
