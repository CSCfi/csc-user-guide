---
tags:
  - Free
catalog:
  name: ANGSD
  description: Analysis of next-generation sequencing data via genotype likelihoods
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ANGSD

ANGSD (Analysis of Next Generation Sequencing Data) is a program for analysing NGS
data. It can estimate many summary statistics and perform population-genetic analyses
directly from genotype likelihoods, which makes it well suited to low-coverage
sequencing data. It reads BAM/CRAM alignments and other common formats.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/ANGSD/angsd/blob/master/LICENSE).

## Available

* Roihu: 0.940, via the `bio-apps` module.

## Usage

ANGSD is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the ANGSD module:

```bash
module load bio-apps/v202603
module load angsd/0.940
```

ANGSD is run with the `angsd` command. For example, to calculate genotype likelihoods
for a set of BAM files listed in `bam.filelist`:

```bash
angsd -bam bam.filelist -GL 1 -doGlf 2 -doMajorMinor 1 -SNP_pval 1e-6 -out results
```

ANGSD can use multiple threads with the `-nThreads` option.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=angsd
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load angsd/0.940

angsd -bam bam.filelist -GL 1 -doGlf 2 -doMajorMinor 1 -SNP_pval 1e-6 -nThreads $SLURM_CPUS_PER_TASK -out results
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ANGSD home page](http://www.popgen.dk/angsd/)
* [ANGSD GitHub repository](https://github.com/ANGSD/angsd)
