---
tags:
  - Free
catalog:
  name: PLINK 2
  description: Successor to PLINK 1.9 for whole genome association analysis
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PLINK 2

PLINK 2 is the actively developed successor to [PLINK 1.9](plink.md), offering the same
kind of large-scale whole genome association analysis on a rewritten, more scalable
codebase.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail plink2` after loading `bio-apps`.

## License

Free to use and open source under
[GPLv3](https://github.com/chrchang/plink-ng/blob/master/2.0/COPYING).

## Usage

On Roihu, PLINK 2 is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load plink2
```

The basic syntax is:

```bash
plink2 --bfile mydata --glm --out results
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=plink2
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load plink2

srun plink2 --bfile mydata --glm --threads $SLURM_CPUS_PER_TASK --out results
```

Submit the job with `sbatch plink2_job.sh`.

PLINK 2 changed some file formats and defaults compared to
[PLINK 1.9](plink.md) (for example `.pgen`/`.pvar`/`.psam` instead of
`.bed`/`.bim`/`.fam`), so check which format a given workflow expects.

## More information

* [PLINK 2 home page](https://www.cog-genomics.org/plink/2.0/)
* [CSC Service Desk](../support/contact.md)
