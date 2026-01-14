---
tags:
  - Academic
catalog:
  name: NMRLipids
  description: NMRLipids databank containing MD simulations
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - LUMI
---

# NMRLipids

[NMRLipids Databank](https://github.com/NMRlipids/FAIRMD_lipids) is a community-driven repository 
of atomistic molecular dynamic simulations of biologically relevant lipid membranes curated within 
the NMRlipids open collaboration. The effort is designed to improve the Findability, Accessibility,
Interoperability, and Reuse (FAIR) of MD simulation data. NMRlipids databank is implemented using 
overlay databank structure as described in the [databank publication](https://www.nature.com/articles/s41467-024-45189-z)

[TOC]

## Available

=== "LUMI"
    | Version | Available modules              |
    |:-------:|:-------------------------------|
    |v1.3.0       | |

The usage of NMRLipids database requires cloning the
[NMRLipids Database](https://github.com/NMRlipids/FAIRMD_lipids) (quick) to
your scratch folder and creating symbolic links from the trajectory pointers 
to the already downloaded (large) raw data located at
`/pfs/lustrep4/appl/local/csc/datasets/NMRLipids/BilayerData/Simulations` on LUMI.
The raw data files (trajectories) require ~3 TiB of disk and downloading _them_ would take days,
but with the procedure outlined below, you can start working with them in minutes. 

The detailed instructions, including how to build a container on LUMI to use the data,
are available [here](https://github.com/NMRLipids/FAIRMD_lipids/discussions/362)

## License

The NMRLipids database is licensed under the GNU General Public License v3.0 (GPL-3.0).

## Usage

### Example batch script for LUMI

Once the NMRLipids Database is symlinked and corresponding database software image
is built as instructed above, one can use the following batch job template on LUMI as shown below: 

```
#!/bin/bash
#SBATCH --partition=small
#SBATCH --account=project_123456789
#SBATCH --time=1-0:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2 

OPTS=$@

module use /appl/local/csc/modulefiles
module load CrayEnv
module load cotainr

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
TRJPATH=/pfs/lustrep4/appl/local/csc/datasets/NMRLipids/BilayerData/Simulations

srun singularity exec \
       -B /scratch/project_123456789/:/scratch/project_123456789/ \
       -B ${TRJPATH}:${TRJPATH} \
       --env NMLDB_DATA_PATH=/scratch/project_123456789/BilayerData \
       nmdb_gmx.sif ${OPTS}
```

## References

If you use the NMRlipids databank in your publications, please always cite the NMRlipids
[Databank publication](https://www.nature.com/articles/s41467-024-45189-z),
as well as the trajectory entries and related publications whenever appropriate

## More Information

- [The NMRlipids database home page](https://www.databank.nmrlipids.fi/) has an extensive manual
and useful information
- [FAIRMD NMRLipids](https://github.com/NMRLipids/FAIRMD_lipids)
