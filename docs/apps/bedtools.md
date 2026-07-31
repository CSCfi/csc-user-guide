---
tags:
  - Free
catalog:
  name: BEDTools
  description: Toolkit for genome arithmetic on interval data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BEDTools

BEDTools is a toolkit for comparing and manipulating genomic intervals, effectively
performing set theory ("genome arithmetic") on BED, GFF, VCF and BAM files. It covers
common tasks such as intersecting, merging, subtracting and computing coverage between
sets of genomic features.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail bedtools2` after loading `bio-apps`.

## License

Free to use and open source under
[MIT License](https://github.com/arq5x/bedtools2/blob/master/LICENSE).

## Usage

On Roihu, BEDTools is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load bedtools2
```

The tool installs as `bedtools`, with subcommands for each operation:

```bash
bedtools <subcommand> [options]
```

Some commonly used subcommands:

* `intersect`   find overlaps between two sets of intervals
* `merge`       merge overlapping intervals
* `subtract`    remove intervals of one set from another
* `genomecov`   compute genome-wide coverage
* `closest`     find the nearest interval in another set

Heavier jobs should be run as batch jobs. Most BEDTools subcommands are single-threaded.
An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=bedtools
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load bedtools2

srun bedtools intersect -a fileA.bed -b fileB.bed > overlap.bed
```

Submit the job with `sbatch bedtools_job.sh`.

## More information

* [BEDTools home page](https://github.com/arq5x/bedtools2)
* [BEDTools manual](https://bedtools.readthedocs.io)
* [CSC Service Desk](../support/contact.md)
