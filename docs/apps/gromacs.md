# Gromacs

Gromacs is a very efficient engine to perform molecular dynamics
simulations and energy minimizations particularly for proteins. However,
it can also be used to model polymers, membranes and e.g. coarse grained
systems. It also comes with plenty of analysis scripts.

[TOC]

## Available

-   Puhti: 2018-2020 releases with regularly updated minor versions, several with plumed or cuda
-   Mahti: 2019-2020 releases with regularly updated minor versions, several with plumed
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

<!-- The module will set `$OMP_NUM_THREADS=1`
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
[Gromacs performance checklist] on the Gromacs page.

We recommend using the latest versions as they have most bugs fixed and
tend to be faster. If you switch the major version, check that the
results are comparable.

A scaling test with a very large system (1M+ particles) may take a while to 
load balance optimally. It's better to increase the number of nodes in your 
production simulation, **IF** you see better performance than in the scaling 
test at the scaling limit, rather than run very long scaling tests in advance.

### Example parallel batch script for Puhti
```bash
#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH --partition=large
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=2
#SBATCH --account=<project>
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

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
    overhead and fragmentation of node reservations.

### Example serial batch script for Puhti
```bash
#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 1 core gromacs job, requesting 15 minutes time

module purge
module load gromacs-env
export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
```
    
### Example GPU script for Puhti
```bash
#!/bin/bash -l
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:v100:1
#SBATCH --time=00:10:00
#SBATCH --partition=gpu
#SBATCH --account=<project>
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

module load gromacs-env/2020-gpu

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export SLURM_CPU_BIND=none

srun gmx_mpi mdrun -s verlet -pin on -dlb yes
# additional flags, like these, may be useful - test!
# srun gmx_mpi mdrun -pme gpu -pmefft gpu -nb gpu -bonded gpu -update gpu \
    -nstlist 200 -s verlet -pin on -dlb yes

```
!!! note
    Please make sure that using one GPU (and upto 10 cores) is at least twice as fast
    as using one full node of CPU cores. Otherwise, don't use GPUs.
    You can compare the "cost" of using
    CPU vs. GPU in the [billing calculator](https://research.csc.fi/billing-and-monitoring)


Submit the script with `sbatch script_name.sh`

### Example mpi-only parallel batch script for Mahti

```bash
#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=2
#SBATCH --account=<project>
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 256 core (2 full nodes, no hyperthreading) gromacs job, requesting 15 minutes time

module purge
module load gcc/9.3.0 openmpi/4.0.3 gromacs/2020.2

export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
```

### Example mixed parallel batch script for Mahti

```bash
#!/bin/bash -l
#SBATCH --time=00:15:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=2
#SBATCH --nodes=2
#SBATCH --account=<project>
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 256 core (2 full nodes, no hyperthreading) gromacs job, requesting 15 minutes time
# 64 tasks per node, each with 2 OpenMP threads

module purge
module load gcc/9.3.0 openmpi/4.0.3 gromacs/2020.2

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
```

### Visualizing trajectories and graphs

In addition to ngmx program in Gromacs, trajectory files can be
visualized with the following programs:

-   [PyMOL] molecular modeling system.
-   [VMD] visualizing program for large biomolecular systems.
-   [Grace](grace.md) plotting graphs produced with Gromacs tools

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
-   [Tutorials on the Gromacs website]  
-   [More tutorials] by Justin A. Lemkul
-   [Lots of material at BioExcel EU project]
-   [HOW-TO] section on the Gromacs pages
-   Gromacs [documentation]
-   [The PRODRG Server] for online creation of small molecule topology
-   [2019 Advanced Gromacs Workshop materials](https://research.csc.fi/web/training/-/advanced-gromacs-workshop)

  [documentation]: http://manual.gromacs.org/documentation
  [PyMOL]: http://www.pymol.org/
  [VMD]: http://www.ks.uiuc.edu/Research/vmd/
  [Gromacs performance checklist]: http://www.gromacs.org/Documentation/Performance_checklist
  [Tutorials on the Gromacs website]: http://www.gromacs.org/Documentation/Tutorials
  [The PRODRG Server]: https://www.sites.google.com/site/vanaaltenlab/prodrg
  [HOW-TO]: http://www.gromacs.org/Documentation/How-tos
  [Lots of material at BioExcel EU project]: http://bioexcel.eu/software/gromacs/
  [More tutorials]: http://www.mdtutorials.com/gmx/
