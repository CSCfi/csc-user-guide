---
tags:
  - Free
catalog:
  name: minibwa
  description: Short-read aligner, successor to BWA-MEM
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# minibwa

minibwa is a short-read aligner by Heng Li, billed as the successor of BWA-MEM. It
indexes a reference genome with an FM-index and aligns single- or paired-end reads
using a banded, SIMD-accelerated Smith-Waterman extension, adapting its parameters
to the read length. Like BWA-MEM it indexes the genome before alignment.

[TOC]

## License

The minibwa source is released under the [MIT license](https://github.com/lh3/minibwa/blob/master/LICENSE.txt).
Note that the default build (as installed here) compiles the GPL-2.0+ BWT-construction
code inherited from BWA, so the installed `minibwa` binary is effectively GPL.

## Available

* Roihu-CPU: 0.7, via the `bio-apps` module.

## Usage

minibwa is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the minibwa module:

```bash
module load bio-apps/v202603
module load minibwa/0.7
```

minibwa has two subcommands, `index` and `map`.

### Indexing a reference

Index the reference genome before aligning. Work in your project's `/scratch`
directory rather than `$HOME`, which is often too small for complete genomes:

```bash
minibwa index -t $SLURM_CPUS_PER_TASK ref.fa
```

This writes the index files `ref.fa.l2b` and `ref.fa.mbw` next to the reference.

### Aligning reads

Paired-end reads are aligned with two read files, producing SAM on standard output:

```bash
minibwa map -t $SLURM_CPUS_PER_TASK ref.fa read1.fq read2.fq > aln.sam
```

A single read file aligns single-end. Add `-f` to emit PAF instead of SAM:

```bash
minibwa map -t $SLURM_CPUS_PER_TASK ref.fa reads.fq > aln.sam
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=minibwa
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load minibwa/0.7

# Index the reference genome (once)
minibwa index -t $SLURM_CPUS_PER_TASK ref.fa

# Align paired-end reads
minibwa map -t $SLURM_CPUS_PER_TASK ref.fa read1.fq read2.fq > aln.sam
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [minibwa GitHub repository](https://github.com/lh3/minibwa)
