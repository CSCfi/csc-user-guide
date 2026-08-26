# Submitting across architectures

## Overview

It is preferred that you submit GPU jobs from CPU (login) nodes and GPU jobs from GPU (login) nodes.
However, if you have a valid use case, it is possible to submit jobs across architectures.
We must make sure that the environment of the running job does not point to software from a different architecture.
For example, if you submit GPU job from CPU node it will default to the software stack from the CPU side.
The following instructions explain how to set the environment correctly.

By default Slurm copies the whole submitting environment to the job (`--export=ALL`), so variables such as `PATH`, `LD_LIBRARY_PATH` and the Lmod/module state arrive pointing at binaries and module trees built for the *submitting* architecture.
For running jobs on a different architecture than the shell you submit from requires the following modications to the environment:

1. **Limit what is propagated** with `--export`, so the target node builds its own environment. `HOME` and `TERM` are usually enough; Slurm's own `SLURM_*` variables are always passed. Add only what your job genuinely needs.

2. **Use a login shell with full path to the binary** (`/bin/bash --login)`, so that the user enviroment, including the module system, is fully initialized.
For batch jobs, set `CSC_ENV_INIT_NON_INTERACTIVE=yes` to force `/etc/profile.d/zz-csc-env.sh` to initialize the CSC environment in a non-interactive shell.
Interactive shells initialize it by default (because they set `PS1`).

3. For batch jobs, set `export SLURM_EXPORT_ENV=ALL` in the batch script such that commands run via `srun` will inherit all environment variables defined within the batch job.

## Interactive job

```bash
srun --account=<project> \
    --partition=gputest \
    --nodes=1 \
    --ntasks-per-node=1 \
    --cpus-per-task=72 \
    --gres=gpu:gh200:1 \
    --time=0:15:00 \
    --export=HOME,TERM \
    --pty /bin/bash --login
```

## Batch job

```bash title="batch.sh"
#!/bin/bash --login
#SBATCH --export=HOME,CSC_ENV_INIT_NON_INTERACTIVE=yes
#SBATCH --account=<project>
#SBATCH --partition=gputest
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=72
#SBATCH --nodes=1
#SBATCH --gres=gpu:gh200:1
#SBATCH --time=0:15:00
export SLURM_EXPORT_ENV=ALL

# Write your code here
```

```bash
sbatch batch.sh
```
