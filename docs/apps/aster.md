---
tags:
  - Free
catalog:
  name: ASTER
  description: Species-tree estimation from gene trees, alignments or reads (ASTRAL-IV, ASTRAL-Pro3 and more)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ASTER

ASTER (Accurate Species Tree EstimatoR) is a package of programs for estimating
species trees. It includes ASTRAL-IV, the successor of [ASTRAL-III](astral.md), and
ASTRAL-Pro3 for gene trees with multi-copy genes. The programs are:

| Command | Program | Input |
|---|---|---|
| `astral4` | ASTRAL-IV | Unrooted gene trees |
| `astral-pro3` | ASTRAL-Pro3 | Gene family trees with multi-copy genes (paralogs) |
| `wastral` | Weighted ASTRAL | Gene trees with branch lengths and/or support values |
| `caster-site`, `caster-pair` | CASTER | Whole-genome or other aligned sequences |
| `waster` | WASTER | Raw sequencing reads |
| `dstar` | D\* statistic | Detecting hybridisation |

[TOC]

## License

Free to use and open source under [GNU AGPLv3](https://github.com/chaoszhang/ASTER/blob/master/LICENSE).

## Available

* Roihu-CPU: 1.25, via the `bio-apps` module.

## Usage

ASTER is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the ASTER module:

```bash
module load bio-apps/v202603
module load aster/1.25
```

For example, estimate a species tree from a file of gene trees (one Newick tree per
line) with ASTRAL-IV, using 4 threads:

```bash
astral4 -t 4 -o species_tree.nw gene_trees.nw 2> astral4.log
```

All the ASTER programs use one thread by default, so always set the number of threads
with `-t` to match the cores reserved for your job. If your gene trees contain several
individuals per species, give a mapping from individuals to species with `-a`.

`astral-pro3` works the same way, but takes gene family trees, which can contain
several copies of a gene from the same species:

```bash
astral-pro3 -t 4 -o species_tree.nw gene_family_trees.nw 2> astral-pro3.log
```

!!! note "ASTRAL commands"
    The `aster` module also provides ASTRAL-IV as `astral`, which is the same command
    name as ASTRAL-III in the [`astral`](astral.md) module. Use `astral4` to make sure
    you run ASTRAL-IV, and do not load both modules at the same time.

    ASTRAL-Pro3 replaces the older Java version of ASTRAL-Pro
    (`java -jar astral.1.1.6.jar`). It optimises the same objective but is faster,
    uses less memory and also estimates branch lengths. Its options differ from the
    Java version, so check them before reusing old scripts.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=astral4
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=8G

module load bio-apps/v202603
module load aster/1.25

astral4 -t $SLURM_CPUS_PER_TASK -o species_tree.nw gene_trees.nw 2> astral4.log
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ASTER GitHub repository](https://github.com/chaoszhang/ASTER), with a tutorial for each program
* [Zhang, C., Nielsen, R. & Mirarab, S. (2025). ASTER: A Package for Large-scale Phylogenomic Reconstructions. Molecular Biology and Evolution, msaf172](https://doi.org/10.1093/molbev/msaf172)
