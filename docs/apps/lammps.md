# LAMMPS

LAMMPS is a "Molecular Dynamics Simulator" which supports
a wide variety of [different force fields](https://lammps.sandia.gov/doc/Intro_features.html#interatomic-potentials-force-fields).
CSC does not have a
general purpose installation of LAMMPS, as each user typically
needs a little bit customised version. Please read below
how to create yours.

[TOC]

## Available

-   Puhti: Instructions available for building
-   Mahti: Instructions available for building

## License

LAMMPS is an open-source code, distributed freely under the terms of the GNU Public License (GPL).

## Usage

First [download](https://lammps.sandia.gov/download.html) the software. Please don't use the
prebuilt binaries, but take a look at the instructions for configuring and compiling LAMMPS 
on Puhti or Mahti for optimal performance (and to include the packages you need) in here:

```
/appl/soft/chem/lammps/
```

Please compile in `$TMPDIR` and install in `/projappl/<project code>`. 
Consult these pages on how to create batch jobs 
[on Puhti](../computing/running/creating-job-scripts-puhti.md) and 
[on Mahti](../computing/running/creating-job-scripts-mahti.md).

If you have problems in compiling LAMMPS, please contact servicedesk@csc.fi.

### High-throughput computing with LAMMPS

LAMMPS offers comprehensive support for executing loops and multiple independent simulations. The `-partition` command-line switch enables running these concurrently within a single Slurm job step, thus accelerating the computations while keeping the load on the batch queue system minimal as excessive calls of `srun` or `sbatch` are avoided. An example LAMMPS batch script using the `-partition` option is provided below.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=00:15:00
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=40
#SBATCH --mem-per-cpu=100

export PATH=$PATH:/path/to/lmp_puhti

srun lmp_puhti -in loop.lammps -partition 24x5
```

The above example runs an umbrella sampling simulation of ethanol adsorption on a NaCl surface in accordance with [this LAMMPS tutorial](https://lammpstutorials.github.io/tutorials/tutorial06.html). The simulation consists of 24 iterations where the ethanol molecule is gradually pulled closer to the surface. These 24 iterations are all run concurrently using 5 MPI tasks each, which is specified in the batch script as `-partition 24x5`. The number of processors must add up to the amount requested, in this case 3 full Puhti nodes (120 cores). In general, the partitions do not have to be of equal size, but one could for example specify `-partition 3x30 20 10` for 3 partitions of 30 cores, one of 20 cores and one of 10 cores (3 Puhti nodes). This does of course not make sense for jobs where the subtasks are virtually identical such as here.

If the `-partition` switch is used one needs to replace the usual `index` and `loop` variable styles used in the input of sequential simulations. The corresponding styles compatible with multi-partition jobs are `world`, `universe` and `uloop`. For further details, see the LAMMPS documentation on [running multiple simulations from one input script](https://docs.lammps.org/Howto_multiple.html), the [partition switch](https://docs.lammps.org/Run_options.html#partition) and [variable styles compatible with multi-partition jobs](https://docs.lammps.org/variable.html).

## References

The following JCP paper is the canonical reference to use for citing LAMMPS.
It describes the parallel spatial-decomposition, neighbor-finding, and communcation 
algorithms used in the code. Please also give the URL of the LAMMPS website in your paper, namely http://lammps.sandia.gov.

* S. Plimpton, Fast Parallel Algorithms for Short-Range Molecular Dynamics, J Comp Phys, 117, 1-19 (1995)

References to other methods used in LAMMPS can be found [here](https://lammps.sandia.gov/cite.html)

## More information

-   LAMMPS home page: [https://lammps.sandia.gov/](https://lammps.sandia.gov/)


