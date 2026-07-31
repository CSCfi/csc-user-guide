---
tags:
  - Free
catalog:
  name: Canu
  description: Single-molecule sequence assembler for genome assembly
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Canu

Canu is an assembler for long, single-molecule reads such as those from PacBio or
Oxford Nanopore sequencers. It is a fork of the Celera Assembler, handling read
correction, trimming and assembly of noisy long reads in one pipeline.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail canu` after loading `bio-apps`.

## License

Free to use and open source under
[GPL v2 License](https://github.com/marbl/canu/blob/master/README.license.GPL).

## Usage

On Roihu, Canu is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load canu
```

The basic syntax is:

```bash
canu -p <prefix> -d <output-dir> genomeSize=<size> [options] -nanopore reads.fastq.gz
```

For example:

```bash
canu -p asm -d asm-out genomeSize=4.8m useGrid=false -nanopore reads.fastq.gz
```

Canu can submit its own sub-jobs to a batch scheduler when `useGrid` is left at its
default. On Roihu, keep `useGrid=false` so Canu uses only the resources given to its
own Slurm job. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=canu
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load canu

srun canu -p asm -d asm-out genomeSize=4.8m useGrid=false \
    maxThreads=$SLURM_CPUS_PER_TASK -nanopore reads.fastq.gz
```

Submit the job with `sbatch canu_job.sh`. Larger genomes need more time and memory
than this example provides.

## More information

* [Canu home page](https://canu.readthedocs.io/)
* [Canu on GitHub](https://github.com/marbl/canu)
* [CSC Service Desk](../support/contact.md)
