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

**Example parallel batch script for Puhti**

```
#!/bin/bash 
#SBATCH --time=00:30:00
#SBATCH --partition=small
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=2G
#SBATCH --account=<project>

# this script runs a 40 core (1 full node) Elmer job, requesting 30 minutes time
# and 2 GB of memory for each core

module load elmer/latest
# make sure the SIF is in the start-info
echo myrun.sif > ELMERSOLVER_STARTINFO
echo "starting Elmer simulation with SIF file"
cat ELMERSOLVER_STARTINFO
srun ElmerSolver
echo "done"
```


## More information

-   [Elmer home page](https://www.elmerfem.org)
