---
tags:
  - Free
catalog:
  name: PLINK
  description: Whole genome association analysis toolset
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PLINK

PLINK is a free, open-source toolset for whole genome association analysis, built to
handle large-scale genetic data sets efficiently. This page covers PLINK 1.9; for the
newer, actively developed toolset see [PLINK 2](plink2.md).

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail plink` after loading `bio-apps`.

## License

Free to use and open source under
[GPLv3](https://github.com/chrchang/plink-ng/blob/master/1.9/LICENSE).

## Usage

On Roihu, PLINK is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load plink
```

The basic syntax is:

```bash
plink --bfile mydata --assoc --out results
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=plink
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load plink

srun plink --bfile mydata --assoc --threads $SLURM_CPUS_PER_TASK --out results
```

Submit the job with `sbatch plink_job.sh`.

PLINK 1.9 and [PLINK 2](plink2.md) use different binary formats for some analyses, so
check which one a given workflow or collaborator expects before choosing a module.

## More information

* [PLINK 1.9 home page](https://www.cog-genomics.org/plink/1.9/)
* [CSC Service Desk](../support/contact.md)
