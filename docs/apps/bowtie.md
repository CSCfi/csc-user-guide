---
tags:
  - Free
catalog:
  name: Bowtie
  description: Memory-efficient short read aligner
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Bowtie

Bowtie is a fast, memory-efficient aligner for short DNA sequencing reads against a
reference genome. It is the predecessor of Bowtie 2, and uses a different index format
and command-line syntax; see [Bowtie2](bowtie2.md) for the newer aligner.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail bowtie` after loading `bio-apps`.

## License

Free to use and open source under
[Artistic License 2.0](https://opensource.org/license/artistic-2-0/).

## Usage

On Roihu, Bowtie is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load bowtie
```

The reference genome must first be indexed with `bowtie-build`:

```bash
bowtie-build reference.fa genome_index
```

The basic alignment syntax is:

```bash
bowtie [options] genome_index reads.fastq > output.sam
```

Heavier jobs should be run as batch jobs. Bowtie scales well with the number of threads
given to `-p`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=bowtie
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load bowtie

bowtie-build reference.fa genome_index
srun bowtie -p $SLURM_CPUS_PER_TASK -S genome_index reads.fastq > output.sam
```

Submit the job with `sbatch bowtie_job.sh`.

## More information

* [Bowtie home page](https://sourceforge.net/projects/bowtie-bio/)
* [Bowtie manual](http://bowtie-bio.sourceforge.net/manual.shtml)
* [CSC Service Desk](../support/contact.md)
