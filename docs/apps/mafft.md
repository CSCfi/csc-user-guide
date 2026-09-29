---
tags:
  - Free
catalog:
  name: MAFFT
  description: Multiple sequence alignment
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MAFFT

MAFFT is a multiple sequence alignment program for unix-like operating systems. It
offers a range of alignment strategies, from fast progressive methods for large numbers
of sequences to accurate iterative-refinement methods for smaller datasets.

[TOC]

## License

Free to use and open source under the [BSD license](https://mafft.cbrc.jp/alignment/software/license.txt).

## Available

* Roihu: 7.525, via the `bio-apps` module.

## Usage

MAFFT is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MAFFT module:

```bash
module load bio-apps/v202603
module load mafft/7.525
```

A basic automatic alignment (MAFFT chooses the strategy based on the data size):

```bash
mafft --auto --thread 8 input.fasta > aligned.fasta
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=mafft
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load mafft/7.525

mafft --auto --thread $SLURM_CPUS_PER_TASK input.fasta > aligned.fasta
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MAFFT home page](https://mafft.cbrc.jp/alignment/software/)
