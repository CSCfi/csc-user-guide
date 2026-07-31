---
tags:
  - Free
catalog:
  name: HybPiper
  description: Toolkit for recovering target genes from sequence capture data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HybPiper

HybPiper is a suite of Python scripts for recovering target gene sequences from
targeted sequence capture reads, most often for phylogenetic studies.

[TOC]

## Available

* Roihu-CPU: 2.3.4
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail hybpiper` after loading `bio-apps`.

## License

Free to use and open source under
[GNU General Public License v3.0](https://github.com/mossmatters/HybPiper/blob/master/LICENSE.txt).

## Usage

On Roihu, HybPiper is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load hybpiper
```

The main entry point is `hybpiper`, with subcommands such as `assemble`,
`retrieve_sequences` and `stats`. Assemble sequences for one sample from paired-end
reads and a nucleotide target file:

```bash
hybpiper assemble --targetfile_dna targets.fasta \
    --readfiles sample_R1.fastq sample_R2.fastq --bwa --prefix sample_name
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=hybpiper
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load hybpiper

srun hybpiper assemble --targetfile_dna targets.fasta \
    --readfiles sample_R1.fastq sample_R2.fastq --bwa --prefix sample_name \
    --cpu $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch hybpiper_job.sh`.

## More information

* [HybPiper home page](https://github.com/mossmatters/HybPiper)
* [HybPiper wiki](https://github.com/mossmatters/HybPiper/wiki)
* [CSC Service Desk](../support/contact.md)
