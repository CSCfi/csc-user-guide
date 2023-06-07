# High-throughput computing with Gromacs

Gromacs comes with a built-in `multidir` functionality, which allows users to run
multiple concurrent simulations within one Slurm allocation. This is an excellent
option for high-throughput use cases, where the aim is to run several similar, but
independent, jobs. Notably, multiple calls of `sbatch` or `srun` are not needed,
which decreases the load on the batch queue system. Please consider this option if
you're running high-throughput workflows or enhanced sampling jobs such as replica
exchange or free energy simulations using ensemble-based distance or orientation
restraints.

Another utility of `multidir` is that it can be used to increase the GPU efficiency
of small systems. By launching multiple trajectories per GPU, the combined throughput
of each independent simulation will increase due to better GPU utilization. This is
especially useful to maximize the performance for small systems on LUMI-G, as well on
Mahti where only full CPU nodes can be reserved.

## Example batch script for Mahti

This example adapts the production part of the [lysozyme tutorial](http://www.mdtutorials.com/gmx/lysozyme/)
by considering 8 similar copies of the system that have been equilibrated with different velocity
initializations. Inputs corresponding to each copy are named identically `md_0_1.tpr`
and placed in subdirectories `run*` as illustrated below by the output of the `tree`
command.

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
module load gromacs-env

export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -multidir run* -s md_0_1.tpr -dlb yes
```

By issuing `sbatch multidir.sh` in the parent directory, all simulations are run concurrently
using one full Mahti node without hyperthreading so that each system is allocated 16 cores.
As the systems were initialized with different velocities, we obtain 8 distinct trajectories
and an improved sampling of the phase space (see RMSD analysis below). This is a great way
to accelerate sampling if your system does not scale to a full Mahti node.

![Root-mean-squared-deviations of the simulated replicas](../../img/multidir-rmsd.svg 'Root-mean-squared-deviations of the simulated replicas')

## Example batch script for LUMI



## More information

* [Gromacs manual: Running multi-simulations](https://manual.gromacs.org/current/user-guide/mdrun-features.html#running-multi-simulations)