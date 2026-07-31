---
tags:
  - Free
catalog:
  name: MAFFT
  description: Multiple sequence alignment program
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MAFFT

MAFFT is a multiple sequence alignment program for amino acid or nucleotide
sequences, offering methods that trade off between speed and accuracy.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail mafft` after loading `bio-apps`.

## License

Free to use and open source under
[BSD License](https://mafft.cbrc.jp/alignment/software/license.txt).

## Usage

On Roihu, MAFFT is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load mafft
```

The basic syntax is:

```bash
mafft [options] input.fasta > aligned.fasta
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=mafft
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load mafft

srun mafft --thread $SLURM_CPUS_PER_TASK input.fasta > aligned.fasta
```

Submit the job with `sbatch mafft_job.sh`.

## More information

* [MAFFT home page](https://mafft.cbrc.jp/alignment/software/)
* [CSC Service Desk](../support/contact.md)
