---
tags:
  - Free
---

# CP2K

Versatile ab initio and classical molecular dynamics. CP2K is suited for large
parallel quantum chemistry calculations, in particular for AIMD.

[TOC]

## Available

=== "Puhti"
    | Version | Available modules | Notes |
    |:-------:|:------------------|:-----:|
    |9.1      |`cp2k/9.1`         |       |
    |2022.2   |`cp2k/2022.2`      |       |
    |2023.1   |`cp2k/2023.1`      |       |
    |2023.2   |`cp2k/2023.2`      |       |
    |2024.1   |`cp2k/2024.1`      |       |
    |2024.2   |`cp2k/2024.2`      |       |

=== "Mahti"
    | Version | Available modules | Notes |
    |:-------:|:------------------|:-----:|
    |8.2      |`cp2k/8.2`         |       |
    |9.1      |`cp2k/9.1`         |       |
    |2022.2   |`cp2k/2022.2`      |       |
    |2023.1   |`cp2k/2023.1`      |       |
    |2023.2   |`cp2k/2023.2`      |       |
    |2024.1   |`cp2k/2024.1`      |       |
    |2024.2   |`cp2k/2024.2`      |       |

=== "LUMI"
    | Version | Available modules                | Notes                 |
    |:-------:|:---------------------------------|:---------------------:|
    |2024.3   |`cp2k/2024.3`<br>`cp2k/2024.3-gpu`| GPU version available |

## License

CP2K is freely available under the GPL license.

## Usage

!!! info "LUMI"
    To access CSC modules on LUMI, remember to first load the CSC module tree
    into use with

    ```bash
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

Specify the version number to see how to load it:

```bash
module spider cp2k/<version>
```

With each new project, make sure that your job can efficiently utilize all the
cores you request in the batch script. The rule of thumb is that when you
double the number of cores the calculation should be at least 1.5 times faster.

### Example batch scripts

=== "Puhti (MPI only)"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:10:00
    #SBATCH --ntasks-per-node=40
    #SBATCH --nodes=2
    #SBATCH --mem-per-cpu=2GB
    #SBATCH --partition=large
    #SBATCH --account=<project>

    module purge
    module load gcc/13.2.0 openmpi/5.0.5
    module load cp2k/2024.2

    srun cp2k.popt H2O-64.inp > H2O-64.out
    ```

=== "Mahti (mixed MPI/OpenMP)"

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
    module load cp2k/2024.2

    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    export OMP_PLACES=cores

    srun cp2k.psmp H2O-64.inp > H2O-64.out
    ```

=== "LUMI-G (full GPU node)"

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
    module load cp2k/2024.1-gpu

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

    !!! info "Note"
        Each GPU on LUMI is composed of two AMD Graphics Compute Dies (GCD).
        Since there are four GPUs per node and Slurm interprets each GCD as a
        separate GPU, you can reserve up to 8 "GPUs" per node. See more details
        in [LUMI Docs](https://docs.lumi-supercomputer.eu/hardware/lumig/).

### Performance notes

#### Mahti

The following table shows the total execution time (in seconds) of the
[H2O-256 benchmark](https://github.com/cp2k/cp2k/blob/master/benchmarks/QS/H2O-256.inp)
on Mahti using `cp2k/2024.2`. The column headers show how many OpenMP threads
were used per MPI task.

|CPU nodes|1     |2     |4         |8     |
|:-------:|:----:|:----:|:--------:|:----:|
|1        |197.35|164.80|169.66    |192.07|
|2        |111.95|107.78|**101.52**|117.60|
|4        |82.74 |72.12 |72.00     |97.97 |

* For 256 water molecules, the best efficiency is obtained with 2 full nodes,
  32 MPI tasks per node, and 4 OpenMP threads per task. For this system it is
  not efficient to scale beyond 2 nodes (256 CPU cores).
* Hybrid parallelism is often efficient – choose tasks and threads so that they
  add up to 128 (physical) cores available per node (or up to 40 on Puhti).
* Test the optimal run parameters for your model system and method.
* Using the ELPA diagonalization library instead of ScaLAPACK may significantly
  accelerate calculations that require large matrix diagonalizations (even up
  to 50% depending on the system). A good example are metallic systems that may
  converge poorly with the orbital transformation (OT) method and thus demand a
  standard diagonalization of the Kohn-Sham matrix.

#### LUMI

Only certain CPU cores are directly linked to a specific GPU on LUMI, so to
maximize multi-GPU performance, it is important to ensure that CPU cores are
bound to the GPUs accordingly. The full GPU node example above takes care of
this, and also excludes the first core of each group of 8 cores linked to a
given GCD. These are reserved for the operating system to reduce noise, meaning
that there are only 56 cores available per node.

!!! error "Note"
    Please note that CPU-GPU binding only works when reserving full nodes by
    running in the `standard-g` partition or by using the `--exclusive` flag.
    See more details in LUMI Docs:
    [LUMI-G hardware](https://docs.lumi-supercomputer.eu/hardware/lumig/),
    [LUMI-G examples](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/),
    [GPU binding](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#gpu-binding)

The following plot shows the total execution time of the
[linear-scaling SCF benchmark](https://github.com/cp2k/cp2k/tree/master/benchmarks/QS_DM_LS)
(2048 water molecules) on Mahti (CPU), LUMI-C and LUMI-G. When CPU-GPU binding
is properly done (see example above), LUMI-G is about twice as performant as
Mahti/LUMI-C when comparing GPU nodes vs. CPU nodes. Since not all routines of
CP2K have been ported to GPUs, make sure to always check the performance and
scaling of your system and method – some simulations (e.g. standard SCF) are
better run on CPUs while others are substantially faster on GPUs (e.g.
linear-scaling SCF, post-HF methods). For more details, see the
[CP2K website](https://www.cp2k.org/gpu).

![CP2K scaling on Mahti and LUMI](../img/cp2k-lumi.png 'CP2K scaling on Mahti and LUMI')

### High-throughput computing with CP2K

High-throughput computations can be run conveniently with CP2K using the
built-in `FARMING` program. This is an excellent option for use cases where the
aim is to run a large amount of independent computations, such as when
generating data for AI/ML pipelines. All subjobs are run in parallel within a
single Slurm allocation, thus avoiding excess calls of `srun` or `sbatch` which
decreases the load on the batch queue system.

Running `FARMING` jobs requires an additional input file in which the details
of the workflow, such as the input directories and number of parallel task
groups, are specified. Example input and batch script files are provided below.
Note that `RUN_TYPE` is set to `NONE` in the `&GLOBAL` section.

=== "Input file"

    ```text title="farming.inp"
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

=== "Batch script file"

    ```bash title="farming.sh"
    #!/bin/bash -l
    #SBATCH --time=00:30:00
    #SBATCH --partition=medium
    #SBATCH --ntasks-per-node=128
    #SBATCH --nodes=1
    #SBATCH --account=<project>

    module purge
    module load gcc/9.4.0 openmpi/4.1.2
    module load cp2k/2024.2

    srun cp2k.psmp farming.inp >> farming.out
    ```

In this particular example, one full Mahti node is requested for running 8
single-point calculations of a NaCl crystal with different lattice constants.
In addition to the `farming.inp` input, each subjob requires its own ordinary
input file, which are here organized into separate subdirectories named `run*`.
Issuing `sbatch farming.sh` in the parent directory launches all calculations
in parallel, allocating 16 cores to each subjob.

Note that dependencies can also be specified between subjobs using the
`DEPENDENCIES` and `JOB_ID` keywords under the `&JOB` section. This enables the
definition of complex workflows. For further details, see the
[CP2K manual](https://manual.cp2k.org/trunk/CP2K_INPUT/FARMING.html) and
[regtest files for example inputs](https://github.com/cp2k/cp2k/tree/master/tests/FARMING).

## References

CP2K prints out a list of relevant publications towards the end of the
log file. Choose and cite the ones relevant to the methods you've used.

## More information

* [CP2K online manual](https://manual.cp2k.org/)
* [CP2K home page](http://www.cp2k.org/)
    * Contains [tutorials](https://www.cp2k.org/howto) and links to useful
      [tools](https://www.cp2k.org/tools).
* [Regtest inputs](https://github.com/cp2k/cp2k/tree/master/tests) can be used
  as examples on how to use the different features in CP2K. Note that the
  convergence criteria can be quite loose and should be separately tested for
  production simulations.
