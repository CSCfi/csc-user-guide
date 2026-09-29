---
tags:
  - Free
catalog:
  name: bwa-mem2
  description: Faster successor to bwa mem
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# bwa-mem2

bwa-mem2 is the next version of the `bwa mem` algorithm in [BWA](bwa.md). It produces
alignments identical to `bwa mem` but runs faster, at the cost of a larger index. It is
used for aligning short reads against a large reference genome.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/bwa-mem2/bwa-mem2/blob/master/LICENSE).

## Available

* Roihu: 2.3, via the `bio-apps` module.

## Usage

bwa-mem2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the bwa-mem2 module:

```bash
module load bio-apps/v202603
module load bwa-mem2/2.3
```

First index the reference genome (this needs more memory and disk than BWA):

```bash
bwa-mem2 index reference.fa
```

Then align reads:

```bash
bwa-mem2 mem -t 8 reference.fa read1.fq read2.fq > aln.sam
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=bwa-mem2
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=8G

module load bio-apps/v202603
module load bwa-mem2/2.3

bwa-mem2 mem -t $SLURM_CPUS_PER_TASK reference.fa read1.fq read2.fq > aln.sam
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [bwa-mem2 GitHub repository](https://github.com/bwa-mem2/bwa-mem2)
