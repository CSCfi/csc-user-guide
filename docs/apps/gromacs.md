# Gromacs

Gromacs is a very efficient engine to perform molecular dynamics
simulations and energy minimizations particularly for proteins. However,
it can also be used to model polymers, membranes and e.g. coarse grained
systems. It also comes with plenty of analysis scripts.

[TOC]

## Available

-   Puhti: 2018-2021 releases with regularly updated minor versions, several with plumed or cuda
-   Mahti: 2019-2021 releases with regularly updated minor versions, several with plumed
-   Check recommended version(s) with `module avail gromacs-env`
-   If you want to use commandline [plumed tools](plumed.md), load the plumed module.

!!! note
    We only provide the parallel version `gmx_mpi`, but it can
    be used for grompp, editconf etc. similarly to the serial version.
    Instead of `gmx grompp` ... give `gmx_mpi grompp`

## License
Gromacs is free software available under LGPL, version 2.1.

## Usage

Initialise recommended version of Gromacs on Puhti like this:

```bash
module purge
module load gromacs-env
```
Use `module spider` to locate other versions. To load these modules, you
need to first load its dependencies, which are shown with
`module spider gromacs/version`.

<!-- The module will set `OMP_NUM_THREADS=1`
as otherwise mdrun will spawn threads for cores it _thinks_ are free. -->

### Notes about performance

It is important to set up the simulations properly to use resources efficiently.
The most important are:

-   If you run in parallel, make a scaling test for each system - don't use more cores than is efficient. 
    Scaling depends on many aspects of your system and used algorithms, not just size.
-   Use a recent version - there has been significant speedup over the years
-   Minimize unnecessary disk I/O - never run batch jobs with -v (the verbose flag) for mdrun
-   For large jobs, use full nodes (multiples of 40 cores, on Puhti) see example below.

For a more complete description, consult the 
[mdrun performance checklist] on the Gromacs page.

We recommend using the latest versions as they have most bugs fixed and
tend to be faster. If you switch the major version, check that the
results are comparable.

A scaling test with a very large system (1M+ particles) may take a while to 
load balance optimally. It's better to increase the number of nodes in your 
production simulation, **IF** you see better performance than in the scaling 
test at the scaling limit, rather than run very long scaling tests in advance.

### Example parallel batch script for Puhti
```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=large
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=2
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

# this script runs a 80 core (2 full nodes) gromacs job, requesting 15 minutes time

module purge
module load gromacs-env
export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
```

!!! note
    To avoid multi node parallel jobs to spread over more nodes
    than necessary, don't use the --ntasks flag, but specify --nodes and
    --ntasks-per-node=40 to get full nodes. This minimizes communication
    overhead and fragmentation of node reservations. Don't use the large
    partition for jobs with less than 40 cores.

### Example serial batch script for Puhti
```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

# this script runs a 1 core gromacs job, requesting 15 minutes time

module purge
module load gromacs-env
export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -s topol -maxh 0.2
```
    
### Example GPU script for Puhti
```bash
#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:v100:1
#SBATCH --time=00:10:00
#SBATCH --partition=gpu
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

module load gromacs-env/2020-gpu

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun gmx_mpi mdrun -s verlet -dlb yes
# additional flags, like these, may be useful - test!
# srun gmx_mpi mdrun -pin on -pme gpu -pmefft gpu -nb gpu -bonded gpu -update gpu \
    -nstlist 200 -s verlet -pin on -dlb yes

```
!!! note
    Please make sure that using one GPU (and upto 10 cores) is at least twice as fast
    as using one full node of CPU cores according to the [usage policy](../../computing/overview/#gpu-nodes).
    Otherwise, don't use GPUs.

Submit the script with `sbatch script_name.sh`

### Example mpi-only parallel batch script for Mahti

```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=2
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

# this script runs a 256 core (2 full nodes, no hyperthreading) gromacs job, requesting 15 minutes time

module purge
module load gcc/10.3.0 openmpi/4.1.0 gromacs/2021.5

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

# this script runs a 256 core (2 full nodes, no hyperthreading) gromacs job, requesting 15 minutes time
# 64 tasks per node, each with 2 OpenMP threads

module purge
module load gcc/10.3.0 openmpi/4.1.0 gromacs/2021.5

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
```

### High-throughput computing with Gromacs

Gromacs comes with a built-in `multidir` functionality, which allows users to run multiple concurrent simulations within one SLURM allocation. This is an excellent option for high-throughput use cases, where the aim is to run several similar, but independent, jobs. Notably, multiple calls of `sbatch` or `srun` are not needed, which decreases the load on the batch queue system. Please consider this option if you're running high-throughput workflows or jobs such as replica exchange, umbrella sampling or adaptive weight histogram (AWH) free energy simulations using Gromacs.

An example `multidir.sh` batch script for running a `multidir` Gromacs job is provided below. This example adapts the production part of the [lysozyme tutorial](http://www.mdtutorials.com/gmx/lysozyme/) by considering 8 similar copies of the system that have been equilibrated with different velocity initializations. Inputs corresponding to each copy are named identically `md_0_1.tpr` and placed in subdirectories `run*` as illustrated below by the output of the `tree` command.

```console
$ tree
.
├── multidir.sh
├── run1
│   └── md_0_1.tpr
├── run2
│   └── md_0_1.tpr
├── run3
│   └── md_0_1.tpr
├── run4
│   └── md_0_1.tpr
├── run5
│   └── md_0_1.tpr
├── run6
│   └── md_0_1.tpr
├── run7
│   └── md_0_1.tpr
└── run8
    └── md_0_1.tpr
```

```bash
#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=1
#SBATCH --account=<project>

# this script runs a 128 core gromacs multidir job (8 simulations, 16 cores per simulation)

module purge
module load gcc/10.3.0 openmpi/4.1.0 gromacs/2021.5

export OMP_NUM_THREADS=1

# Create a list for the directories, convenient if there are many
list=()
for i in `seq 8`
do
    list+=(run${i})
done

srun gmx_mpi mdrun -multidir ${list[@]} -deffnm md_0_1 -dlb yes
```

By issuing `sbatch multidir.sh` in the parent directory, all simulations are run concurrently using one full Mahti node without hyperthreading so that each system is allocated 16 cores. As the systems were initialized with different velocities, we obtain 8 distinct trajectories and an improved sampling of the phase space (see RMSD analysis below). This is a great option for enhanced sampling when your system does not scale beyond a certain core count.

For further details on running Gromacs multi-simulations, see the [official Gromacs documentation](https://manual.gromacs.org/documentation/current/user-guide/mdrun-features.html#running-multi-simulations).

### Visualizing trajectories and graphs

In addition to `view` (not available at CSC, though) tool of Gromacs,
trajectory files can be visualized with the following programs:

-   [PyMOL] molecular modeling system.
-   [VMD](vmd.md) visualizing program for large biomolecular systems.
-   [Grace](grace.md) plotting graphs produced with Gromacs tools

!!! note
    Please don't run visualization or heavy Gromacs tool scripts in
    the login node (see [usage policy for details](../../computing/overview/#usage-policy)).
    You can run the tools in the [interactive partition](../computing/running/interactive-usage.md)
    by prepending your `gmx_mpi` command with `orterun -n 1`, e.g. `orterun -n 1 gmx_mpi msd -n index -s topol -f traj`).

## References

Cite your work with the following references:

-   GROMACS 4: Algorithms for Highly Efficient, Load-Balanced, and
    Scalable Molecular Simulation. Hess, B., Kutzner, C., van der
    Spoel, D. and Lindahl, E. J. Chem. Theory Comput., 4, 435-447
    (2008).
-   GROMACS: Fast, Flexible and Free. D. van der Spoel, E. Lindahl, B.
    Hess, G. Groenhof, A. E. Mark and H. J. C.Berendsen, J. Comp. Chem.
    26 (2005) pp. 1701-1719
-   *GROMACS: High performance molecular simulations through multi-level
    parallelism from laptops to supercomputers* 
    M. J. Abraham, T. Murtola, R. Schulz, S. Páll, J. C. Smith, B. Hess, E.
    Lindahl *SoftwareX* 1 (2015) pp. 19-25
-   *Tackling Exascale Software Challenges in Molecular Dynamics Simulations with
    GROMACS* In S. Markidis & E. Laure (Eds.), Solving Software Challenges for Exascale
    S. Páll, M. J. Abraham, C. Kutzner, B. Hess, E. Lindahl 8759 (2015) pp. 3-27
-   *GROMACS 4.5: a high-throughput and highly parallel open source molecular
    simulation toolkit* S. Pronk, S. Páll, R. Schulz, P. Larsson, P. Bjelkmar, R. Apostolov, M. R.
    Shirts, J. C. Smith, P. M. Kasson, D. van der Spoel, B. Hess, and E. Lindahl
    Bioinformatics 29 (2013) pp. 845-54

See your simulation log file for more detailed references
for methods applied in your setup.

## More information

-   Gromacs home page: [http://www.gromacs.org/](http://www.gromacs.org/)
-   [Hands-on tutorials] by Justin A. Lemkul, on [GROMACS tutorial home](https://tutorials.gromacs.org/) and by [Bert de Groot group](https://www3.mpibpc.mpg.de/groups/de_groot/compbio/index.html)
-   [Lots of material at BioExcel EU project]
-   [HOW-TO](https://manual.gromacs.org/documentation/current/how-to/index.html) section on the Gromacs pages
-   Gromacs [documentation] and [mdrun performance checklist]
-   [The PRODRG Server] for online creation of small molecule topology
-   [2021 Advanced Gromacs Workshop materials](https://enccs.github.io/gromacs-gpu-performance/)

  [mdrun performance checklist]: https://manual.gromacs.org/current/user-guide/mdrun-performance.html
  [documentation]: http://manual.gromacs.org/documentation
  [PyMOL]: http://www.pymol.org/
  [The PRODRG Server]: https://www.sites.google.com/site/vanaaltenlab/prodrg
  [Lots of material at BioExcel EU project]: http://bioexcel.eu/software/gromacs/
  [Hands-on tutorials]: http://www.mdtutorials.com/gmx/
