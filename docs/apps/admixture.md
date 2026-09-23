---
tags:
  - Free
catalog:
  name: ADMIXTURE
  description: Maximum-likelihood estimation of individual ancestries from SNP data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ADMIXTURE

ADMIXTURE is a tool for fast maximum-likelihood estimation of individual ancestries
from multilocus SNP genotype datasets. It uses the same statistical model as
STRUCTURE but computes estimates much faster using a numerical optimization
algorithm.

[TOC]

## License

ADMIXTURE is free to use. It is distributed as a binary; see the
[ADMIXTURE home page](https://dalexander.github.io/admixture/) for the license terms.

## Available

* Roihu: 1.4.0, via the `bio-apps` module.

## Usage

ADMIXTURE is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the ADMIXTURE module:

```bash
module load bio-apps/v202603
module load admixture/1.4.0
```

ADMIXTURE takes a PLINK `.bed` (or `.ped`) genotype file and the number of assumed
ancestral populations *K*. For example, to run with *K* = 3:

```bash
admixture input.bed 3
```

This produces the ancestry fractions (`input.3.Q`) and allele frequencies
(`input.3.P`). ADMIXTURE can use multiple threads with the `-j` option.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=admixture
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load admixture/1.4.0

admixture -j$SLURM_CPUS_PER_TASK input.bed 3
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ADMIXTURE home page](https://dalexander.github.io/admixture/)
