---
tags:
  - Free
catalog:
  name: SALMON
  description: Program to produce transcript-level quantification estimates from RNA-seq data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SALMON

Salmon is a fast program to produce highly-accurate, transcript-level quantification estimates from RNA-seq data. Salmon achieves its accuracy and speed via a number of different innovations, including the use of quasi-mapping (accurate but fast-to-compute proxies for traditional read alignments), and massively-parallel stochastic collapsed variational inference. The result is a versatile tool that fits nicely into many pipelines. For example, you can choose to make use of the quasi-mapping algorithm by providing Salmon with raw sequencing reads, or, if it is more convenient, you can provide Salmon with regular alignments (e.g. an unsorted BAM file produced with your favorite aligner), and it will use the same fast, state-of-the-art inference algorithm to estimate transcript-level abundances for your experiment.

!!! info "Note"
    Salmon works by (quasi)-mapping sequencing reads directly to the transcriptome. This means the Salmon index should be built on a set of target transcripts, not on the genome of the underlying organism. If indexing appears to be taking a very long time, or using a tremendous amount of memory (which it should not), please ensure that you are not attempting to build an index on the genome of your organism!

[TOC]

## License

Free to use and open source under [BSD 3-Clause License](https://github.com/COMBINE-lab/salmon/blob/master/LICENSE).

## Available

- Roihu-CPU: 2.8.0, via the `bio-apps` module.

## Usage

Salmon is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Salmon module:

```bash
module load bio-apps/v202603
module load salmon/2.8.0
```

For usage help, use the command:

```bash
salmon --help
```

!!! info "Rebuild indexes made with Salmon 1.x"
    Salmon 2 is a complete rewrite of Salmon, and its index format is not compatible
    with Salmon 1.x. Indexes built with older versions, for example on Puhti, must be
    rebuilt with `salmon index`.

### Example batch script

The following batch script builds an index for a set of transcripts and quantifies
paired-end reads against it:

```bash
#!/bin/bash
#SBATCH --job-name=salmon
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load salmon/2.8.0

salmon index -t transcripts.fasta -i salmon_index -p $SLURM_CPUS_PER_TASK
salmon quant -i salmon_index -l A -1 reads_1.fastq -2 reads_2.fastq \
  -p $SLURM_CPUS_PER_TASK -o sample_quant
```

The transcript-level estimates are written to `sample_quant/quant.sf`. Replace
`<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Salmon documentation](https://combine-lab.github.io/salmon)
