---
tags:
  - Free
catalog:
  name: BEDOPS
  description: Set operations and other tools for genomic interval data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BEDOPS

BEDOPS is a command-line toolkit for fast set and statistical operations on genomic
interval data such as BED, GFF and VCF files. It scales to whole-genome datasets and
covers common tasks such as intersections, merges, closest-feature searches and format
conversion.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail bedops` after loading `bio-apps`.

## License

Free to use and open source under the
[GPL v2 License](https://github.com/bedops/bedops/blob/master/LICENSE), with bundled
components under the bzip2, MIT and zlib licenses.

## Usage

On Roihu, BEDOPS is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load bedops
```

BEDOPS installs several separate tools. The most commonly used one is `bedops`, which
performs set operations on two or more sorted BED files:

```bash
bedops --operation input1.bed input2.bed > result.bed
```

Input files must be sorted first, which the bundled `sort-bed` tool does:

```bash
sort-bed unsorted.bed > sorted.bed
```

Other tools in the collection include `bedmap` (map and aggregate one set of intervals
onto another), `closest-features` and format converters such as `gff2bed` and `vcf2bed`.

Heavier jobs should be run as batch jobs. BEDOPS tools are single-threaded. An example
batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=bedops
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load bedops

srun bedops --intersect fileA.bed fileB.bed > overlap.bed
```

Submit the job with `sbatch bedops_job.sh`.

## More information

* [BEDOPS home page](https://bedops.readthedocs.io)
* [CSC Service Desk](../support/contact.md)
