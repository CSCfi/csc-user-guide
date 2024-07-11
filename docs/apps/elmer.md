---
tags:
  - Free
---

# Elmer

Elmer is CSC's open source Finite Element multi-physics simulation package. It covers modules for fluid and solid mechanics,
acoustics, and electro-magneto dynamics.

Elmer utilizes third-party open source programs for pre- (e.g., Gmsh) and post-processing (e.g., ParaView, Visit).
The version installed includes Elmer/Ice solvers needed for glaciological simulations (ice-sheets, glaciers).
Elmer utilizes the MPI library for parallel computing with some solvers already having OpenMP parallel threading
directives implemented.

[TOC]

## Available

- Puhti: 9.0
- Mahti: 9.0
- LUMI: 9.0

## License

Elmer is licensed under GPL and (as for the `elmersolver.lib`) LGPL. It is free for everyone to use.

## Usage

On Puhti and Mahti, the Elmer versions available can be listed using the command

```bash
module avail elmer
```

On LUMI, one needs to first take into use the module files of CSC installed software:

```bash
module use /appl/local/csc/modulefiles/
module avail elmer
```

The default version of Elmer is loaded with

```bash
module load elmer/latest
```

We recommend using this version (except for special reasons) on all platforms.

Be aware that this version is frequently updated. If you have User Functions as compiled code added to your case, make sure to recompile upon such an update (the date is displayed upon loading the module).

### Example parallel batch script

=== "Puhti"
    This is a basic script for a 30-minute single node job using all 40 cores and reserving 2 GB memory for each core, where the Elmer input file is `myrun.sif`.

    ```bash
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

=== "Mahti"
    The main difference on Mahti is that only full nodes can be allocated. A single node contains 128 cores (we do _not_ recommend to use [multithreading](../computing/running/creating-job-scripts-mahti.md#hybrid-batch-jobs-with-simultaneous-multithreading-smt)). The following script submits a 6-hour job using 4 nodes and all 128 cores per node (hence in total 512).

    ```bash
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

=== "LUMI"
    Basic script for a 1-hour job using 4 nodes and 128 cores in total, where the Elmer input file is `myrun.sif`.

    ```bash
    #!/bin/bash 
    #SBATCH --time=01:00:00
    #SBATCH --job-name=jobname
    #SBATCH --output=%x.%j.out
    #SBATCH --error=%x.%j.err
    #SBATCH --partition=small
    #SBATCH --account=<project>
    #SBATCH --nodes=4
    #SBATCH --ntasks=128

    module use /appl/local/csc/modulefiles/
    module load elmer/latest
    # make sure the SIF is in the start-info
    echo myrun.sif > ELMERSOLVER_STARTINFO
    echo "starting Elmer simulation with SIF file"
    cat ELMERSOLVER_STARTINFO
    srun ElmerSolver
    echo "done"
    ```    

Instructions on how to submit and monitor jobs can be found in [CSC docs](../computing/running/submitting-jobs.md) and in [LUMI docs](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/slurm-quickstart/).

It can be advantageous to utilize fewer cores per node than available to increase performance in certain Elmer cases. See the example on [undersubscribing](../computing/running/creating-job-scripts-mahti.md#undersubscribing-nodes).

## More information

- [Elmer home page](https://www.elmerfem.org)
