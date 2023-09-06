---
tags:
  - Free
---

# CP2K

Versatile ab initio and classical molecular dynamics. CP2K is suited for large
parallel quantum chemistry calculations, in particular for AIMD.

[TOC]

## Available

* Puhti: 9.1, 2022.2, 2023.1, 2023.2
* Mahti: 8.2, 9.1, 2022.2, 2023.1, 2023.2
* LUMI: 2023.1, 2023.1-gpu, 2023.2, 2023.2-gpu

## License

CP2K is freely available under the GPL license.

## Usage

!!! info "LUMI"
    To access CSC modules on LUMI, remember to first load the CSC module tree into use with

    ```
    module use /appl/local/csc/modulefiles
    ```

Check which versions can be loaded directly:

```bash
module avail cp2k
```

You can find all installed versions with:

```bash
module spider cp2k
```

With each new project make sure that your job can efficiently utilize all the
cores you request in the batch script. The rule of thumb is that when you double
the number of cores the calculation should be at least 1.5 times faster.

### Example batch script for Puhti using MPI-only parallelization

```bash
#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=2
#SBATCH --mem-per-cpu=2GB
#SBATCH --partition=large
#SBATCH --account=<project>

module purge
module load intel-oneapi-compilers-classic/2021.6.0 intel-oneapi-mpi/2021.6.0
module load cp2k/2023.2

srun cp2k.popt H2O-64.inp > H2O-64.out
```

### Example batch script for Mahti using mixed MPI-OpenMP parallelization

```bash
#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --ntasks-per-node=32  # 2 - 128
#SBATCH --cpus-per-task=4     # 128 / ntasks-per-node
#SBATCH --nodes=2
#SBATCH --partition=test
#SBATCH --account=<project>

module purge
module load gcc/9.4.0 openmpi/4.1.2
module load cp2k/2023.2

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores

srun cp2k.psmp H2O-64.inp > H2O-64.out
```

### Example batch script for LUMI-G using a full GPU node

!!! info "Note"
    Each GPU on LUMI is composed of two AMD Graphics Compute Dies (GCD). Since
    there are four GPUs per node and Slurm interprets each GCD as a separate GPU,
    you can reserve up to 8 "GPUs" per node. See more details in
    [LUMI Docs](https://docs.lumi-supercomputer.eu/hardware/lumig/).

```bash
#!/bin/bash
#SBATCH --partition=standard-g
#SBATCH --account=<project>
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --gpus-per-node=8
#SBATCH --ntasks-per-node=16  # Run two tasks per GCD, in this case more efficient

export OMP_NUM_THREADS=3

module use /appl/local/csc/modulefiles
module load cp2k/2023.2-gpu

export MPICH_GPU_SUPPORT_ENABLED=1

cat << EOF > select_gpu
#!/bin/bash

export ROCR_VISIBLE_DEVICES=\$((SLURM_LOCALID%SLURM_GPUS_PER_NODE))
exec \$*
EOF

chmod +x ./select_gpu

CPU_BIND="mask_cpu:fe000000000000,fe00000000000000"
CPU_BIND="${CPU_BIND},fe0000,fe000000"
CPU_BIND="${CPU_BIND},fe,fe00"
CPU_BIND="${CPU_BIND},fe00000000,fe0000000000"

srun --cpu-bind=$CPU_BIND ./select_gpu cp2k.psmp H2O-dft-ls.inp >> H2O-dft-ls.out
```

!!! info "CPU-GPU binding"
    To get the best performance out of multi-GPU simulations it is important to make
    sure that CPU cores are bound to GPUs in the right way. Why this matters is because
    only certain CPU cores are directly linked to a specific GPU. The example above takes
    care of this and excludes the first core from each group of 8 cores since the first
    core of the node is reserved for the operating system. In other words, there are only
    63 cores available per node, which is the reason why we run 3 threads per MPI rank, not 4.
    **Please note that CPU-GPU binding works only when reserving full nodes (`standard-g` or `--exclusive`).**

    See more details in LUMI Docs: [LUMI-G hardware](https://docs.lumi-supercomputer.eu/hardware/lumig/),
    [LUMI-G examples](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/),
    [GPU binding](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#gpu-binding)

### Performance notes

**Mahti:**

The following table shows the total execution time [s] of the [H2O-64
benchmark](https://github.com/cp2k/cp2k/blob/master/benchmarks/QS/H2O-64.inp)
in Mahti using cp2k/9.1. The column headers show how many omp-threads were used
per mpi-task.

Nodes|d1|d2|d4|d8
-|--|--|--|--
1|25.77|18.88|20.58|22.95
2|17.66|15.25|*13.34*|17.10

* For 64 water molecules, the best performance is obtained with 2 full
  nodes, 32 mpi-tasks, and 4 OMP-threads per task (like the [Mahti
  example](#example-batch-script-for-mahti-using-mixed-mpi-openmp-parallelization)).
  For this system the performance does not scale beyond 2 nodes.
* Mixed parallization is efficient: choose tasks and threads so that they add up
  to 128 (physical) cores available per node (or up to 40 on Puhti).
* Test the optimal run parameters for your model system and method.
* Selecting the ELPA diagonalization library instead of ScaLAPACK may significantly
  accelerate calculations that require large matrix diagonalizations (even up to
  50% depending on the system). A good example are metallic systems that may
  converge poorly with the orbital transformation (OT) method and thus demand a standard
  diagonalization of the Kohn-Sham matrix.

**LUMI:**

The following plot shows the total execution time of the
[linear scaling SCF benchmark](https://github.com/cp2k/cp2k/tree/master/benchmarks/QS_DM_LS)
(2048 water molecules) on Mahti (CPU), LUMI-C and LUMI-G. When CPU-GPU binding is properly
done ([see example above](#example-batch-script-for-lumi-g-using-a-full-gpu-node)), LUMI-G
is almost twice as performant as Mahti/LUMI-C when comparing GPU nodes vs. CPU nodes.
Since not all routines of CP2K have been ported to GPUs, make sure to always check the
performance and scaling of your system and method -- some simulations (e.g. standard SCF)
are better run on CPUs while others are substantially faster on GPUs (e.g. linear scaling SCF,
post HF methods). For more details, see the [CP2K website](https://www.cp2k.org/gpu).

![CP2K scaling on Mahti and LUMI](../img/cp2k-lumi.png 'CP2K scaling on Mahti and LUMI')

### High-throughput computing with CP2K

High-throughput computations can be run conveniently with CP2K using the built-in
`FARMING` program. This is an excellent option for use cases where the aim is to
run a large amount of independent computations, such as when generating data for
AI/ML pipelines. All subjobs are run in parallel within a single Slurm allocation,
thus avoiding excess calls of `srun` or `sbatch` which decreases the load on the
batch queue system.

Running `FARMING` jobs requires an additional input file in which the details of
the workflow, such as the input directories and number of parallel task groups,
are specified. Example `farming.inp` and `farming.sh` input and batch script files
are provided below. Note that `RUN_TYPE` is set to `NONE` in the `&GLOBAL` section.

```text
&GLOBAL
  PROJECT my-farming-job
  PROGRAM FARMING
  RUN_TYPE NONE
&END GLOBAL
&FARMING
  NGROUPS 8
  &JOB
    DIRECTORY run1
    INPUT_FILE_NAME nacl.inp
  &END JOB
  &JOB
    DIRECTORY run2
    INPUT_FILE_NAME nacl.inp
  &END JOB
  &JOB
    DIRECTORY run3
    INPUT_FILE_NAME nacl.inp
  &END JOB
  &JOB
    DIRECTORY run4
    INPUT_FILE_NAME nacl.inp
  &END JOB
  &JOB
    DIRECTORY run5
    INPUT_FILE_NAME nacl.inp
  &END JOB
  &JOB
    DIRECTORY run6
    INPUT_FILE_NAME nacl.inp
  &END JOB
  &JOB
    DIRECTORY run7
    INPUT_FILE_NAME nacl.inp
  &END JOB
  &JOB
    DIRECTORY run8
    INPUT_FILE_NAME nacl.inp
  &END JOB
&END FARMING
```

```bash
#!/bin/bash -l
#SBATCH --time=00:30:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=1
#SBATCH --account=<project>

module purge
module load gcc/9.4.0 openmpi/4.1.2 cp2k/2023.2

srun cp2k.psmp farming.inp >> farming.out
```

In this particular example, one full Mahti node is requested for running 8 single-point
calculations of a NaCl crystal with different lattice constants. In addition to the
`farming.inp` input, each subjob requires its own ordinary input file, which are here
organized into separate subdirectories named `run*`. Issuing `sbatch farming.sh` in
the parent directory launches all calculations in parallel, allocating 16 cores to
each subjob.

Note that dependencies can also be specified between subjobs using the
`DEPENDENCIES` and `JOB_ID` keywords under the `&JOB` section. This enables the
definition of complex workflows. For further details, see the [CP2K
manual](https://manual.cp2k.org/trunk/CP2K_INPUT/FARMING.html) and [regtest files
for example inputs](https://github.com/cp2k/cp2k/tree/master/tests/FARMING).

## References

CP2K prints out a list of relevant publications towards the end of the
log file. Choose and cite the ones relevant to the methods you've used.

## More Information

* CP2K online manual: <http://manual.cp2k.org/>
* CP2K home page: <http://www.cp2k.org/>
    * Contains [tutorials](https://www.cp2k.org/howto) and links to useful
      [tools](https://www.cp2k.org/tools)
* [Regtest inputs](https://github.com/cp2k/cp2k/tree/master/tests) can be used as
  examples on how to use the different features in CP2K. Note that the convergence  
  criteria can be quite loose and should be separately tested for production simulations.
