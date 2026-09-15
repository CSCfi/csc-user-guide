---
tags:
  - Free
catalog:
  name: inStrain
  description: Strain-level population genomics from metagenomic mappings
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# inStrain

inStrain is a Python program for the analysis of co-occurring genome populations from
metagenomes. It performs strain-level comparisons, microdiversity analysis and
non-synonymous variant identification from read mappings.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/MrOlm/inStrain/blob/master/LICENSE).

## Available

* Roihu: 1.6.3 (module `py-instrain`), via the `bio-apps` module.

## Usage

inStrain is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the module:

```bash
module load bio-apps/v202603
module load py-instrain/1.6.3
```

Profile a metagenomic mapping (a sorted BAM against a genome or set of genomes):

```bash
inStrain profile aligned.sorted.bam genomes.fasta -o instrain_out -p 8
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=instrain
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load py-instrain/1.6.3

inStrain profile aligned.sorted.bam genomes.fasta -o instrain_out -p $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [inStrain documentation](https://instrain.readthedocs.io/)
* [inStrain GitHub repository](https://github.com/MrOlm/inStrain)
