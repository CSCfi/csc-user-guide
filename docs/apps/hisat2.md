---
tags:
  - Free
catalog:
  name: HISAT2
  description: Fast and sensitive alignment program for sequencing reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HISAT2

HISAT2 is a fast and sensitive aligner for mapping next-generation sequencing reads,
including RNA-seq and whole-genome data, against a reference genome or transcriptome.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail hisat2` after loading `bio-apps`.

## License

Free to use and open source under
[GNU General Public License v3.0](https://github.com/DaehwanKimLab/hisat2/blob/master/LICENSE).

## Usage

On Roihu, HISAT2 is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load hisat2
```

Build a genome index once, then align reads against it:

```bash
hisat2-build reference.fasta index_prefix
hisat2 -x index_prefix -U reads.fastq -S aligned.sam
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=hisat2
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load hisat2

srun hisat2 -p $SLURM_CPUS_PER_TASK -x index_prefix -U reads.fastq -S aligned.sam
```

Submit the job with `sbatch hisat2_job.sh`.

## More information

* [HISAT2 home page](https://daehwankimlab.github.io/hisat2/)
* [HISAT2 manual](https://daehwankimlab.github.io/hisat2/manual/)
* [CSC Service Desk](../support/contact.md)
