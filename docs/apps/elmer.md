---
tags:
  - Free
catalog:
  name: Elmer
  description: Open source multi-physics FEM package
  license_type: Free
  disciplines:
    - Computational Engineering
  available_on:
    - LUMI
    - Roihu
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

=== "Roihu-CPU"

    | Version    | Available modules  | Notes |
    |:----------:|:-------------------|:------|
    | 26.2.1     | `elmerfem/26.2.1`  | Versioned release |
    | devel      | `elmerfem/devel`   | Development version |

=== "LUMI"

    | Version | Available modules |
    |:-------:|:------------------|
    | 9.0     | `elmer/latest`    |

## License

Elmer is licensed under GPL and (as for the `elmersolver.lib`) LGPL. It is free for everyone to use.

## Usage

=== "Roihu-CPU"

    On Roihu-CPU, Elmer is available under the module name `elmerfem`.

    To list the available versions, use:

    ```bash
    module spider elmerfem
    ```

    Load the versioned release with:

    ```bash
    module load elmerfem/26.2.1
    ```

    Alternatively, load the development version with:

    ```bash
    module load elmerfem/devel
    ```

    For detailed information about a specific version and its
    dependencies, use:

    ```bash
    module spider elmerfem/26.2.1
    ```

=== "LUMI"

    On LUMI, first enable the CSC software modules:

    ```bash
    module use /appl/local/csc/modulefiles/
    ```

    To list the available Elmer versions, use:

    ```bash
    module spider elmer
    ```

    Load the default version with:

    ```bash
    module load elmer/latest
    ```

    This version may be updated. If your simulation uses compiled
    User Functions, recompile them after an update when necessary.

### Example parallel batch script

=== "Mahti"
    The main difference on Mahti is that only full nodes can be allocated. A single node contains 128 cores.
    The following script submits a 6-hour job using 4 nodes and all 128 cores per node (hence in total 512).

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

It can be advantageous to utilize fewer cores per node than available to increase performance in certain Elmer cases. See the example on [undersubscribing](../computing/running/creating-job-scripts-roihu.md#undersubscribing-full-nodes-on-roihu-cpu).

## More information

- [Elmer home page](https://www.elmerfem.org)
