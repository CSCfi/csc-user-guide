---
tags:
  - Free
catalog:
  name: Cufflinks
  description: Transcript assembly and differential expression analysis for RNA-seq
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Cufflinks

Cufflinks assembles aligned RNA-seq reads into transcripts, estimates their
abundances, and tests for differential expression and regulation between samples. It
takes spliced-read alignments, for example from HISAT2, as input.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail cufflinks` after loading `bio-apps`.

## License

Free to use and open source under
[Boost Software License 1.0](https://github.com/cole-trapnell-lab/cufflinks/blob/master/LICENSE).

## Usage

On Roihu, Cufflinks is part of the `bio-apps` collection, which has to be loaded
first:

```bash
module load bio-apps
module load cufflinks
```

The basic syntax is:

```bash
cufflinks [options] aligned_reads.bam
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=cufflinks
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load cufflinks

srun cufflinks -p $SLURM_CPUS_PER_TASK -o cufflinks_out aligned_reads.bam
```

Submit the job with `sbatch cufflinks_job.sh`.

## More information

* [Cufflinks home page](https://cole-trapnell-lab.github.io/cufflinks)
* [CSC Service Desk](../support/contact.md)
