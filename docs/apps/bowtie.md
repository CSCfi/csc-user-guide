---
tags:
  - Free
catalog:
  name: Bowtie
  description: Ultrafast, memory-efficient short read aligner
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Bowtie

Bowtie is an ultrafast, memory-efficient short read aligner for short DNA sequences
(reads) from next-generation sequencers. This is the original Bowtie (Bowtie 1); for
gapped alignment of longer reads see [Bowtie2](bowtie2.md).

[TOC]

## License

Free to use and open source under the [Artistic License 2.0](https://github.com/BenLangmead/bowtie/blob/master/LICENSE).

## Available

* Roihu: 1.3.1, via the `bio-apps` module.

## Usage

Bowtie is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Bowtie module:

```bash
module load bio-apps/v202603
module load bowtie/1.3.1
```

First index the reference genome with `bowtie-build` (do this in a scratch directory):

```bash
bowtie-build genome.fa genome
```

Then align reads against the index:

```bash
bowtie -x genome reads.fq -S output.sam
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=bowtie
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
module load bowtie/1.3.1

bowtie-build genome.fa genome
bowtie -p $SLURM_CPUS_PER_TASK -x genome reads.fq -S output.sam
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Bowtie home page](https://bowtie-bio.sourceforge.net/index.shtml)
* [Bowtie GitHub repository](https://github.com/BenLangmead/bowtie)
