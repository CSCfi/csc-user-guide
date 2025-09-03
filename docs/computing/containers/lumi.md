# LUMI
LUMI uses SingularityCE instead of Apptainer.

On LUMI, Singulairity will use `/tmp` as the temporary directory is `/tmp`.
On login node, `/tmp` is a local disk.
On compute node `/tmp` is a tmpfs and limited by memory.
Reserve enough memory, the job is killed if the requsted limit is exceeded.

Interactive job

```bash
srun --account project_id --partition small --time 0:15:00 --mem 8000 --cpus-per-task 1 --pty bash
```

Cache directory can be changed if needed:

```bash
export SINGULARITY_CACHEDIR=/scratch/project_id/$USER/.singularity
```

We can use [proot](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/s/systools/#the-proot-command) to build containers instead of fakeroot.
Do not use the `--fakeroot` flag with Singularity, it does not behave in the same way as with Apptainer.
We can load proot as follows:

```bash
module load LUMI systools
```

Then, we can build container images:

```bash
singularity build container.sif container.def
```
