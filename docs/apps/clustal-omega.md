---
tags:
  - Free
catalog:
  name: Clustal Omega
  description: Multiple sequence alignment
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Clustal Omega

Clustal Omega is a fast and scalable program for multiple sequence alignment of protein
and nucleotide sequences. It can align large numbers of sequences and produce
high-quality alignments.

[TOC]

## License

Free to use and open source under [GNU GPLv2](http://www.clustal.org/omega/).

## Available

* Roihu: 1.2.4, via the `bio-apps` module.

## Usage

Clustal Omega is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Clustal Omega module:

```bash
module load bio-apps/v202603
module load clustal-omega/1.2.4
```

The program is run with the `clustalo` command. For example, to align sequences in a
FASTA file:

```bash
clustalo -i sequences.fasta -o aligned.fasta --threads 4
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=clustalo
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
module load clustal-omega/1.2.4

clustalo -i sequences.fasta -o aligned.fasta --threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Clustal Omega home page](http://www.clustal.org/omega/)
