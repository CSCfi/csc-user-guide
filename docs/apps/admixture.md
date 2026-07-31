---
tags:
  - Academic
catalog:
  name: ADMIXTURE
  description: Maximum likelihood estimation of individual ancestries from SNP data
  license_type: Academic
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ADMIXTURE

ADMIXTURE estimates individual ancestry fractions from multi-locus SNP genotype data,
using a fast numerical optimization algorithm for maximum likelihood estimation.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail admixture` after loading `bio-apps`.

## License

Free for academic use. See the
[software manual](https://dalexander.github.io/admixture/admixture-manual.pdf) for the
license terms; commercial users should contact the author.

## Usage

On Roihu, ADMIXTURE is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load admixture
```

The basic syntax takes a PLINK `.bed` file and the number of ancestral populations `K`:

```bash
admixture input.bed K
```

ADMIXTURE parallelises over threads with `-j`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=admixture
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load admixture

srun admixture -j$SLURM_CPUS_PER_TASK input.bed 3
```

Submit the job with `sbatch admixture_job.sh`.

## More information

* [ADMIXTURE home page](https://dalexander.github.io/admixture/)
* [CSC Service Desk](../support/contact.md)
