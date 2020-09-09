# Elmer

Elmer is CSC's open source Finite Element multi-physics simulation package.  It covers modules for fluid and solid mechanics,
acoustics, electro-magneto dynamics 

Elmer utilizes third-party open source programs for pre- (e.g., Gmsh) and post-processing (e.g., ParaView, Visit).
The version installed includes Elmer/Ice solvers needed for glaciological simulations (ice-sheets, glaciers).
Elmer utilizes the MPI library for parallel computing with some solvers already having OpenMP parallel threading
directives implemented.

[TOC]

## Available

-  Puhti: 8.4
-  Mahti: 8.4

## License
Elmer is licensed under GPL and (as for the elmersolver.lib) LGPL, hence free to use for everyone.

## Usage

Elmer version available can be listed using the command
```
$ module avail elmer
````
The default version of Elmer is taken into use by 
```bash
$ module load elmer/latest
```

We recommend to use this version (except for special reasons) on both platforms. 

Be aware that this version is frequently updated. If you have User Functions as compiled code added to your case, make sure to recompile upon such an update (the date is displayed upon loading the module).

**Example parallel batch script for Puhti**

This is a basic script for a 30 minute single full node job using all 40 cores and reserving 2 GB memory for each core. 

```
#!/bin/bash 
#SBATCH --time=00:30:00
#SBATCH --job-name=jobname
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
#SBATCH --partition=small
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=2G
#SBATCH --account=<project>

module load elmer/latest
# make sure the SIF is in the start-info
echo myrun.sif > ELMERSOLVER_STARTINFO
echo "starting Elmer simulation with SIF file"
cat ELMERSOLVER_STARTINFO
srun ElmerSolver
echo "done"
```

Instructions on how to submit and monitor jobs can be found [here](../computing/running/submitting-jobs.md).

**Example parallel batch script for Mahti**

The main difference on mahti is, that only complete nodes can be allocated. A single node contains 128 cores (we do _not_ recommend to use [multithreading](../computing/running/creating-job-scripts-mahti.md#hybrid-batch-jobs-with-simultaneous-multithreading-smt)). The following script submits a 6 hour job using 4 nodes and all 128 cores per node (hence in total 512).

```
#!/bin/bash 
#SBATCH --time=06:00:00
#SBATCH --job-name=jobname
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
#SBATCH --partition=medium
#SBATCH --account=<project>
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=128

export OMP_NUM_THREADS=1
module load elmer/latest
# make sure the SIF is in the start-info
echo myrun.sif > ELMERSOLVER_STARTINFO
echo "starting Elmer simulation with SIF file"
cat ELMERSOLVER_STARTINFO
srun ElmerSolver
echo "done"
```

It can be advantageous to utilize fewer cores per node as available, which can increase performance in certain Elmer cases. See the example on [undersubscribing](../computing/running/creating-job-scripts-mahti.md#undersubscribing-nodes).

## More information

-   [Elmer home page](https://www.elmerfem.org)
