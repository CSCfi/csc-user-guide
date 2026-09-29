---
tags:
  - Free
catalog:
  name: HISAT2
  description: Spliced aligner for RNA-seq and DNA reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HISAT2

HISAT2 is a fast and sensitive alignment program for mapping next-generation sequencing
reads (both DNA and RNA) to a reference genome. It is widely used for spliced alignment
of RNA-seq reads.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/DaehwanKimLab/hisat2/blob/master/LICENSE).

## Available

* Roihu: 2.2.1, via the `bio-apps` module.

## Usage

HISAT2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the HISAT2 module:

```bash
module load bio-apps/v202603
module load hisat2/2.2.1
```

First build an index of the reference genome:

```bash
hisat2-build genome.fa genome_index
```

Then align reads (here paired-end):

```bash
hisat2 -p 8 -x genome_index -1 read1.fq -2 read2.fq -S output.sam
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=hisat2
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load hisat2/2.2.1

hisat2 -p $SLURM_CPUS_PER_TASK -x genome_index -1 read1.fq -2 read2.fq -S output.sam
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [HISAT2 home page](https://daehwankimlab.github.io/hisat2/)
