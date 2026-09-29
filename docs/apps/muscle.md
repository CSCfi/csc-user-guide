---
tags:
  - Free
catalog:
  name: MUSCLE
  description: Multiple sequence alignment (v3)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MUSCLE

MUSCLE is a widely-used program for creating multiple sequence alignments of protein and
nucleotide sequences. This is MUSCLE version 3; for the current major version see
[MUSCLE5](muscle5.md).

[TOC]

## License

MUSCLE is free to use and in the public domain. See the [MUSCLE home page](https://drive5.com/muscle/).

## Available

* Roihu: 3.8.31, via the `bio-apps` module.

## Usage

MUSCLE is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MUSCLE module:

```bash
module load bio-apps/v202603
module load muscle/3.8.31
```

Align sequences from a FASTA file:

```bash
muscle -in sequences.fasta -out aligned.fasta
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=muscle
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load muscle/3.8.31

muscle -in sequences.fasta -out aligned.fasta
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MUSCLE home page](https://drive5.com/muscle/)
