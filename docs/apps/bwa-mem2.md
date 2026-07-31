---
tags:
  - Free
catalog:
  name: BWA-MEM2
  description: Fast short read aligner, successor to BWA-MEM
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BWA-MEM2

BWA-MEM2 is the successor to the BWA-MEM aligner, mapping DNA sequencing reads to a
reference genome with the same seed-and-extend algorithm. It produces alignments
identical to BWA-MEM while running 1.3-3.1 times faster on modern CPUs.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail bwa-mem2` after loading `bio-apps`.

## License

Free to use and open source under
[MIT License](https://github.com/bwa-mem2/bwa-mem2/blob/master/LICENSE).

## Usage

On Roihu, BWA-MEM2 is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load bwa-mem2
```

The reference genome must first be indexed:

```bash
bwa-mem2 index reference.fasta
```

The basic alignment syntax is:

```bash
bwa-mem2 mem -t 8 reference.fasta reads_1.fastq reads_2.fastq > aln.sam
```

Heavier jobs should be run as batch jobs. Index construction needs considerably more
memory than BWA, so scale `--mem-per-cpu` up for large genomes. An example batch job
script:

```bash
#!/bin/bash
#SBATCH --job-name=bwa-mem2
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=8G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load bwa-mem2

srun bwa-mem2 index reference.fasta
srun bwa-mem2 mem -t $SLURM_CPUS_PER_TASK reference.fasta reads_1.fastq reads_2.fastq \
    > aln.sam
```

Submit the job with `sbatch bwa-mem2_job.sh`.

## More information

* [BWA-MEM2 home page](https://github.com/bwa-mem2/bwa-mem2)
* [CSC Service Desk](../support/contact.md)
