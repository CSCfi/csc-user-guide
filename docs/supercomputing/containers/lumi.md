# LUMI

LUMI uses SingularityCE instead of Apptainer.
We recommend to read the instructions for [Apptainer containers](./overview.md) which apply to SingularityCE on LUMI with certain modifications explained in this page.
We use the command `singularity` instead of `apptainer`.

## Running containers

We can run commands from a container as follows:

```bash
singularity exec container.sif mycommand
```

On LUMI, we can bind mount common disk areas to the container as follows:

```bash
singularity exec --bind="/pfs,/users,/projappl,/scratch,/project,/flash" container.sif mycommand
```

We can also enable ROCm support for AMD GPUs on LUMI as follows:

```bash
singularity exec --rocm container.sif mycommand
```

## Building containers
### Temporary directory

On LUMI, we use `/tmp` as the temporary directory.
SingularityCE bind mounts it by default to the build environment.
Therefore, manually bind mounting the temporary directory is not required.

### Cache directory

The SingularityCE cache directory can be changed if needed:

```bash
export SINGULARITY_CACHEDIR=/scratch/project_id/$USER/.singularity
```

### Build location

On the login node, we can build container images that are small enough that they do not run into memory limits.
Virtual memory in LUMI is quite large (64 GB) and preset to the hard limit, thus it is not required to adjust it.

We must build large container images on the compute node via a slurm job.
For example, we can reserve an interactive slurm job as follows, just replace `myproject` with your project:

```bash
srun --account myproject --partition small --time 0:15:00 --mem 8000 --cpus-per-task 1 --pty bash
```

On the compute node `/tmp` is a tmpfs which is limited by memory.
We must request memory that is at least twice the size of the uncompressed size of your container image (SIF file) to avoid running out of memory.

### Building an SIF image from definition file

We can write SingularityCE definition files using the `.def` file extension.
Here is a simple example of container definition:

```sh title="container.def"
Bootstrap: docker
From: docker.io/opensuse/leap:15.5

%post
    # Replace the failing commands with always succeeding dummies.
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    # Continue to install software into the container normally.
    zypper --non-interactive update
```

On LUMI, we need to use [proot](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/s/systools/#the-proot-command) to build SIF images with SingularityCE.
We can load proot as follows:

```bash
module load LUMI systools
```

Then, we can build container images in the standard way as follows:

```bash
singularity build container.sif container.def
```

Do not use the `--fakeroot` flag with SingularityCE on LUMI, as it does not behave in the same way as with Apptainer.

<!--
### Developing with interactive sandbox

We can also build sandboxes with SingularityCE and proot.
Sandboxes are useful for interactive development of containers.
We should create the sandbox to the temporary directory, not on the Lustre parallel file system.

Load proot first:

```bash
module load LUMI systools
```

We can initialize a sandbox from a base image as follows:

```bash
singularity build --sandbox --fix-perms /tmp/opensuse-leap docker://docker.io/opensuse/leap:15.5
```

Then we can run a shell in the sandbox to install software into it:

```bash
singularity shell --writable --contain --cleanenv --no-home --bind=/tmp /tmp/opensuse-leap
```

We can use the same tricks to replace the failing commands in the sandbox:

```bash
cp /usr/bin/true /usr/sbin/useradd
cp /usr/bin/true /usr/sbin/groupadd
```

Now, we can install software normally:

```bash
zypper --non-interactive update
```
-->
