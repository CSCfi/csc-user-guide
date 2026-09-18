---
tags:
  - Free
catalog:
  name: BEDTools
  description: Genome arithmetic on BED/VCF/GFF intervals
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BEDTools

Collectively, the BEDTools utilities are a swiss-army knife of tools for a wide range
of genomics analysis tasks. They allow one to intersect, merge, count, complement and
shuffle genomic intervals from multiple files in widely-used formats such as BED, GFF,
GTF, VCF and BAM.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/arq5x/bedtools2/blob/master/LICENSE).

## Available

* Roihu: 2.31.1, via the `bio-apps` module.

## Usage

BEDTools is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BEDTools module:

```bash
module load bio-apps/v202603
module load bedtools2/2.31.1
```

The utilities are run through the `bedtools` command followed by a subcommand. For
example, to find overlaps between two interval files:

```bash
bedtools intersect -a features.bed -b regions.bed > overlaps.bed
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=bedtools
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load bio-apps/v202603
module load bedtools2/2.31.1

bedtools intersect -a features.bed -b regions.bed > overlaps.bed
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BEDTools documentation](https://bedtools.readthedocs.io/)
* [BEDTools GitHub repository](https://github.com/arq5x/bedtools2)
