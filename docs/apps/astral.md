---
tags:
  - Free
catalog:
  name: ASTRAL
  description: Species tree estimation from a set of unrooted gene trees
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ASTRAL

ASTRAL estimates an unrooted species tree from a set of unrooted gene trees, using a
statistically consistent method that scales to large numbers of genes and species.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail astral` after loading `bio-apps`.

## License

Free to use and open source under
[Apache License 2.0](https://github.com/smirarab/ASTRAL/blob/master/LICENSE).

## Usage

On Roihu, ASTRAL is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load astral
```

The basic syntax is:

```bash
astral -i gene_trees.tre -o species_tree.tre
```

ASTRAL is single-threaded, so a single core is enough. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=astral
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=8G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load astral

srun astral -i gene_trees.tre -o species_tree.tre
```

Submit the job with `sbatch astral_job.sh`.

## More information

* [ASTRAL home page](https://github.com/smirarab/ASTRAL)
* [CSC Service Desk](../support/contact.md)
