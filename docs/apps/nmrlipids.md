---
tags:
  - Academic
catalog:
  name: NMRLipids
  description: TBA
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - LUMI
---

# NMRLipids

[NMRlipids Databank](https://github.com/NMRLipids/BilayerData), recently referred to as FAIRMD BilayerData, is a community-driven repository of atomistic molecular dynamic simulations of biologically relevant lipid membranes curated within the NMRlipids open collaboration. The effiort is designed to improve the Findability, Accessibility, Interoperability, and Reuse (FAIR) of MD simulation data. NMRlipids databank is implemented using overlay databank structure as described in the [databank publication](https://www.nature.com/articles/s41467-024-45189-z)

[TOC]

## Available

=== "LUMI"
    | Version | Available modules              |
    |:-------:|:-------------------------------|
    |v1.3.0       | |

The usage of NMRLipids database requires cloning [NMRLipids Database](https://github.com/NMRlipids/FAIRMD_lipids) and creating a symbolic link from the cloned data to the actaul raw data located at
/pfs/lustrep4/appl/local/csc/datasets/NMRLipids/BilayerData/Simulations on LUMI.
Detailed installation instructions are available [here](https://github.com/NMRLipids/FAIRMD_lipids/discussions/362)

## License

NMRLipids database is licensed under the GNU General Public License v3.0 (GPL-3.0).

## Usage

### Example batch scripts for LUMI

Once the NMRLipids Database ymlinked and NMRlipid singularity is built,  one can use batch job template on LUMI as shown below: 

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

If you use the NMRlipids databank in your publications, ease always cite the NMRlipids [Databank publication](https://www.nature.com/articles/s41467-024-45189-z), as well as the trajectory entries and related publications whenever appropriate

## More Information

- [The NMRlipids database home page](https://www.databank.nmrlipids.fi/) has an extensive manual
and useful information.
- [FAIRMD NMRLipids](https://github.com/NMRLipids/FAIRMD_lipids)
