---
tags:
  - Free
catalog:
  name: ASTRAL
  description: Coalescent-based species-tree estimation from gene trees
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ASTRAL

ASTRAL is a tool for estimating an unrooted species tree given a set of unrooted gene
trees. It is statistically consistent under the multi-species coalescent model and is
suitable for species-tree estimation in the presence of incomplete lineage sorting.

[TOC]

## License

Free to use and open source under the [Apache 2.0 license](https://github.com/smirarab/ASTRAL/blob/master/README.md#license).

## Available

* Roihu: 5.7.1, via the `bio-apps` module.

## Usage

ASTRAL is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the ASTRAL module:

```bash
module load bio-apps/v202603
module load astral/5.7.1
```

ASTRAL takes a file of gene trees (one Newick tree per line) as input and writes the
estimated species tree. Run it with the `astral` command:

```bash
astral -i gene_trees.tre -o species_tree.tre
```

The module sets the `ASTRAL_HOME` environment variable, pointing to the installation
(which contains the jar file and the `lib` directory).

For larger datasets, run ASTRAL as a batch job:

```bash
#!/bin/bash
#SBATCH --job-name=astral
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load bio-apps/v202603
module load astral/5.7.1

astral -i gene_trees.tre -o species_tree.tre
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ASTRAL GitHub repository](https://github.com/smirarab/ASTRAL)
