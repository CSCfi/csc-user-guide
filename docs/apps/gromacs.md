---
tags:
  - Free
---

# Gromacs

Gromacs is a very efficient engine to perform molecular dynamics
simulations and energy minimizations particularly for proteins. However,
it can also be used to model polymers, membranes and e.g. coarse grained
systems. It also comes with plenty of analysis scripts.

[TOC]

## Available

=== "Puhti"
    | Version | Available modules | Notes |
    |:-------:|:------------------|:-----:|
    |2020.5   |`gromacs/2020.5`
    |2020.7   |`gromacs/2020.7`
    |2021.4   |`gromacs/2021.4-plumed`|Module with Plumed available
    |2021.5   |`gromacs/2021.5`<br>`gromacs/2021.5-cuda`|GPU-enabled module available
    |2021.6   |`gromacs/2021.6`
    |2022.2   |`gromacs/2022.2`<br>`gromacs/2022.2-cuda`|GPU-enabled module available
    |2022.3   |`gromacs/2022.3`<br>`gromacs/2022.3-cuda`|GPU-enabled module available
    |2022.4   |`gromacs/2022.4`<br>`gromacs/2022.4-cuda`|GPU-enabled module available

=== "Mahti"
    | Version | Available modules | Notes |
    |:-------:|:------------------|:-----:|
    |2020.4   |`gromacs/2020.4-plumed`|Module with Plumed available
    |2020.5   |`gromacs/2020.5`
    |2021.3   |`gromacs/2021.3`
    |2021.4   |`gromacs/2021.4-plumed`|Module with Plumed available
    |2021.5   |`gromacs/2021.5`
    |2022     |`gromacs/2022`<br>`gromacs/2022-cp2k`|Module with CP2K available for QM/MM
    |2022.1   |`gromacs/2022.1`<br>`gromacs/2022.1-cp2k`|Module linked with CP2K available for QM/MM
    |2022.2   |`gromacs/2022.2`<br>`gromacs/2022.2-cuda`|GPU-enabled module available
    |2022.3   |`gromacs/2022.3`<br>`gromacs/2022.3-cuda`|GPU-enabled module available
    |2022.4   |`gromacs/2022.4`<br>`gromacs/2022.4-cuda`|GPU-enabled module available

=== "LUMI"
    | Version | Available modules | Notes |
    |:-------:|:------------------|:-----:|
    |2022.5   |`gromacs/2022.5`<br>`gromacs/2022.5-plumed`|Module with Plumed available
    |2023     |`gromacs/2023-dev-rocm`|Unofficial GPU-enabled fork developed by AMD[^1]
    |2023.1   |`gromacs/2023.1`<br>`gromacs/2023.1-hipsycl`<br>`gromacs/2023.1-heffte`|Official GPU-enabled modules available (hipSYCL)<br>Module linked to HeFFTe available for GPU PME decomposition

    [^1]: This module is unvalidated, unmaintained and unsupported by the Gromacs team. Proceed with caution!

- Puhti and Mahti have also `gromacs-env/<year>` modules for loading the recommended
  latest minor version from each year (replace `<year>` accordingly).
- To access modules on LUMI, first load the CSC module tree into use with
  `module use /appl/local/csc/modulefiles`
- If you want to use command-line [Plumed tools](plumed.md), load the Plumed module.

!!! info
    We only provide the parallel version `gmx_mpi`, but it can
    be used for `grompp`, `editconf` etc. similarly to the serial version.
    Instead of `gmx grompp ...`, give `gmx_mpi grompp`.

## License

Gromacs is a free software available under LGPL, version 2.1.

## Usage

Initialize recommended version of Gromacs on Puhti or Mahti like this:

```bash
module purge
module load gromacs-env
```

Use `module spider` to locate other versions. To load these modules, you
need to first load its dependencies, which are shown with
`module spider gromacs/<version>`.

### Notes about performance

It is important to set up the simulations properly to use resources efficiently.
The most important aspects to consider are:

- If you run in parallel, make a scaling test for each system - don't use more cores/GPUs
  than is efficient. Scaling depends on many aspects of your system and used algorithms,
  not just size.
- Use a recent version – there has been significant speedup and bug fixes over the years.
  If you switch the major version, remember to check that the results are comparable.
- Minimize unnecessary disk I/O – never run batch jobs with `-v` (the verbose flag)
  for `mdrun`.
- For large jobs, use full nodes (multiples of 40 cores on Puhti or multiples
  of 128 cores on Mahti), see example below.
- Performance on GPUs depends on what you offload and the optimium depends on many factors.
  Please consult the [excellent ENCCS online materials](https://enccs.github.io/gromacs-gpu-performance/)
  for a general overview.
- On LUMI-G it is important to make sure CPUs are bound to the correct GPUs to minimize
  communication overhead. See example below and
  [LUMI Docs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#gpu-binding)
  for more information.

For a more complete description, consult the [mdrun performance checklist] on the
Gromacs page.

A scaling test with a very large system (1M+ particles) may take a while to
load balance optimally. Rather than running very long scaling tests in advance,
it is better to increase the number of nodes in your production simulation **IF**
you see better performance than in the scaling test at the scaling limit.

### Example parallel batch script for Puhti

```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=large
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=2
#SBATCH --account=<project>
##SBATCH --mail-type=END # uncomment to get mail

# this script runs a 80 core (2 full nodes) gromacs job, requesting 15 minutes time

module purge
module load gromacs-env
export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
```

!!! info "Note"
    To avoid multinode parallel jobs spreading over more nodes
    than necessary, don't use the `--ntasks` flag, but specify `--nodes` and
    `--ntasks-per-node=40` to get full nodes. This minimizes communication
    overhead and fragmentation of node reservations.

### Example serial batch script for Puhti

```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
##SBATCH --mail-type=END # uncomment to get mail

# this script runs a 1 core gromacs job, requesting 15 minutes time

module purge
module load gromacs-env
export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -s topol -maxh 0.2
```

### Example GPU batch script for Puhti

```bash
#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:v100:1
#SBATCH --time=00:10:00
#SBATCH --partition=gpu
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

module purge
module load gromacs-env/2022-gpu

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun gmx_mpi mdrun -s topol -dlb yes

# additional flags, like these, may be useful - test!
# srun gmx_mpi mdrun -pin on -pme gpu -pmefft gpu -nb gpu -bonded gpu -update gpu -nstlist 200 -s topol -dlb yes
```

!!! info "Note"
    Please make sure that using one GPU (and up to 10 CPU cores) is
    faster than using one full node of CPU cores according to our
    [usage policy](../../computing/usage-policy). Otherwise, don't
    use GPUs on Puhti.

### Example MPI-only parallel batch script for Mahti

```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=2
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

# this script runs a 256 core (2 full nodes, no hyperthreading) gromacs job,
# requesting 15 minutes time

module purge
module load gromacs-env

export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
```

### Example mixed parallel batch script for Mahti

```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=2
#SBATCH --nodes=2
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

# this script runs a 256 core (2 full nodes, no hyperthreading) gromacs job,
# requesting 15 minutes time and 64 tasks per node, each with 2 OpenMP threads

module purge
module load gromacs-env

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
```

### Example batch script for LUMI – single GCD <a name="lumi"></a>

```bash
#!/bin/bash
#SBATCH --partition=small-g
#SBATCH --account=<project>
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=7

module use /appl/local/csc/modulefiles
module load gromacs/2023.1-hipsycl

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun gmx_mpi mdrun -s topol -nb gpu -bonded gpu -pme gpu -update gpu
```

### Example batch script for LUMI – full GPU node

!!! info "Note"
    Each GPU on LUMI is composed of two AMD Graphics Compute Dies (GCD). Since
    there are four GPUs per node and Slurm interprets each GCD as a separate GPU,
    you can reserve up to 8 "GPUs" per node. See more details in
    [LUMI Docs](https://docs.lumi-supercomputer.eu/hardware/lumig/).

```bash
#!/bin/bash
#SBATCH --partition=standard-g
#SBATCH --account=<project>
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --gpus-per-node=8
#SBATCH --ntasks-per-node=8

module use /appl/local/csc/modulefiles
module load gromacs/2023.1-hipsycl

export OMP_NUM_THREADS=7

export MPICH_GPU_SUPPORT_ENABLED=1
export GMX_ENABLE_DIRECT_GPU_COMM=1
export GMX_FORCE_GPU_AWARE_MPI=1

cat << EOF > select_gpu
#!/bin/bash

export ROCR_VISIBLE_DEVICES=\$SLURM_LOCALID
exec \$*
EOF

chmod +x ./select_gpu

CPU_BIND="mask_cpu:fe000000000000,fe00000000000000"
CPU_BIND="${CPU_BIND},fe0000,fe000000"
CPU_BIND="${CPU_BIND},fe,fe00"
CPU_BIND="${CPU_BIND},fe00000000,fe0000000000"

srun --cpu-bind=$CPU_BIND ./select_gpu gmx_mpi mdrun -s topol -nb gpu -bonded gpu -pme gpu -update gpu -npme 1
```

!!! info "Direct GPU communication and GPU-aware MPI"
    Instead of communicating between GPUs through the CPU, direct GPU communication
    will bring significant performance benefits when running on multiple GPUs. Enabling
    this requires exporting the following environment variables:

    ```
    export MPICH_GPU_SUPPORT_ENABLED=1
    export GMX_ENABLE_DIRECT_GPU_COMM=1
    export GMX_FORCE_GPU_AWARE_MPI=1
    ```

!!! info "CPU-GPU binding"
    To get the best performance out of multi-GPU simulations it is important to make
    sure that CPU cores are bound to GPUs in the right way. Why this matters is because
    only certain CPU cores are directly linked to a specific GPU. The example above takes
    care of this and excludes the first core from each group of 8 cores since the first
    core of the node is reserved for the operating system. In other words, there are only
    63 cores available per node, which is the reason why we run 7 threads per MPI rank, not 8.
    **Please note that CPU-GPU binding works only when reserving full nodes (`standard-g` or `--exclusive`).**

    See more details in LUMI Docs: [LUMI-G hardware](https://docs.lumi-supercomputer.eu/hardware/lumig/),
    [LUMI-G examples](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/),
    [GPU binding](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#gpu-binding)

Below is a comparison of the performance of Gromacs 2023.1 on Mahti (CPUs and GPUs)
and LUMI-G using the STMV benchmark (1067k atoms). This is a large system which scales
very well also on GPUs. The performance on a single LUMI GCD (half a GPU) is almost as
good as on a full Nvidia A100 GPU on Mahti, and much better than on a single 128-core CPU
node. Importantly, the amount of GPU nodes on LUMI is massively larger than on Mahti
(2560 vs. 24).

![Gromacs scaling on GPUs on Mahti and LUMI](../img/stmv.png 'Gromacs scaling on GPUs on Mahti and LUMI')

!!! info "Small systems on LUMI-G and high-throughput simulations"
    While medium-sized and large systems (100k–1M+ atoms) such as the STMV benchmark
    above are likely to be able to utilize multiple GPUs very well, small systems
    (less than 100k atoms) are typically best run on just a single GCD. A good way
    to increase the GPU utilization and efficiency of small simulations is to run
    many trajectories per GCD. This can be accomplished using the built-in multidir
    feature of Gromacs. For more details about GPU-sharing and aggregate sampling, see our
    [tutorial on high-throughput simulations with Gromacs](../support/tutorials/gromacs-throughput.md).

#### PME decomposition

Scaling of huge systems with several millions atoms may be limited by single GPU PME. To
significantly improve the scaling, decomposition of PME to multiple GPUs is possible in the
`gromacs/2023.1-heffte` module with the [HeFFTe library](https://icl-utk-edu.github.io/heffte/)
linked. Add the following exports to the batch script above:

```bash
export GMX_GPU_PME_DECOMPOSITION=1
export GMX_PMEONEDD=1
```

The number of PME ranks to use depends on the specific case, but 1 or 2 per GPU *node* should
be a reasonable starting point. So for 16 LUMI-G nodes, use `-npme 16` or `-npme 32`.

### Visualizing trajectories and graphs

In addition to the `view` tool of Gromacs (not available at CSC),
trajectory files can be visualized with the following programs:

- [VMD](vmd.md) visualization program for large biomolecular systems
- [Grace](grace.md) plotting data produced with Gromacs tools
- [PyMOL] molecular modeling system (not available at CSC)

!!! warning "Note"
    Please don't run visualization or heavy Gromacs tool scripts on
    the login node (see [usage policy for details](../../computing/usage-policy)).
    You can run the tools in the [interactive partition](../computing/running/interactive-usage.md)
    by prepending your `gmx_mpi` command with `orterun -n 1`, e.g.:
    
    ```
    orterun -n 1 gmx_mpi msd -n index -s topol -f traj
    ```

## References

Cite your work with the following references:

- GROMACS 4: Algorithms for Highly Efficient, Load-Balanced, and
    Scalable Molecular Simulation. Hess, B., Kutzner, C., van der
    Spoel, D. and Lindahl, E. J. Chem. Theory Comput., 4, 435-447
    (2008).
- GROMACS: Fast, Flexible and Free. D. van der Spoel, E. Lindahl, B.
    Hess, G. Groenhof, A. E. Mark and H. J. C.Berendsen, J. Comp. Chem.
    26 (2005) pp. 1701-1719
- *GROMACS: High performance molecular simulations through multi-level
    parallelism from laptops to supercomputers*
    M. J. Abraham, T. Murtola, R. Schulz, S. Páll, J. C. Smith, B. Hess, E.
    Lindahl *SoftwareX* 1 (2015) pp. 19-25
- *Tackling Exascale Software Challenges in Molecular Dynamics Simulations with
    GROMACS* In S. Markidis & E. Laure (Eds.), Solving Software Challenges for Exascale
    S. Páll, M. J. Abraham, C. Kutzner, B. Hess, E. Lindahl 8759 (2015) pp. 3-27
- *GROMACS 4.5: a high-throughput and highly parallel open source molecular
    simulation toolkit* S. Pronk, S. Páll, R. Schulz, P. Larsson, P. Bjelkmar, R. Apostolov, M. R.
    Shirts, J. C. Smith, P. M. Kasson, D. van der Spoel, B. Hess, and E. Lindahl
    Bioinformatics 29 (2013) pp. 845-54

See your simulation log file for more detailed references
for methods applied in your setup.

## More information

- Gromacs home page: [http://www.gromacs.org/](http://www.gromacs.org/)
- [Hands-on tutorials] by Justin A. Lemkul, on [GROMACS tutorial home](https://tutorials.gromacs.org/)
  and by [Bert de Groot group](https://www3.mpibpc.mpg.de/groups/de_groot/compbio/index.html)
- [Lots of material at BioExcel EU project]
- [How-To](https://manual.gromacs.org/documentation/current/how-to/index.html) section in the
  Gromacs manual
- Gromacs [documentation] and [mdrun performance checklist]
- [The PRODRG Server] for online creation of small molecule topologies
- [Advanced Gromacs Workshop materials](https://enccs.github.io/gromacs-gpu-performance/)
- [High-throughput computing with Gromacs](../support/tutorials/gromacs-throughput.md)

  [mdrun performance checklist]: https://manual.gromacs.org/current/user-guide/mdrun-performance.html
  [documentation]: http://manual.gromacs.org/documentation
  [PyMOL]: http://www.pymol.org/
  [The PRODRG Server]: https://www.sites.google.com/site/vanaaltenlab/prodrg
  [Lots of material at BioExcel EU project]: http://bioexcel.eu/software/gromacs/
  [Hands-on tutorials]: http://www.mdtutorials.com/gmx/
  [official Gromacs documentation]: https://manual.gromacs.org/documentation/current/user-guide/mdrun-features.html#running-multi-simulations
