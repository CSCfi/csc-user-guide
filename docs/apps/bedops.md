---
tags:
  - Free
catalog:
  name: BEDOPS
  description: Set operations on genomic intervals (BED)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BEDOPS

BEDOPS is an open-source command-line toolkit that performs highly efficient and
scalable set, statistical and multi-processing operations on genomic intervals in BED
format. It includes tools such as `bedops` (set operations), `bedmap` (mapping and
statistics), `sort-bed` (sorting) and `closest-features`.

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://github.com/bedops/bedops/blob/master/LICENSE).

## Available

* Roihu: 2.4.42, via the `bio-apps` module.

## Usage

BEDOPS is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BEDOPS module:

```bash
module load bio-apps/v202603
module load bedops/2.4.42
```

Most BEDOPS operations require sorted BED input, which you can produce with `sort-bed`:

```bash
sort-bed unsorted.bed > sorted.bed
```

You can then perform set operations, for example finding the intersection of two BED
files:

```bash
bedops --intersect a.sorted.bed b.sorted.bed > intersection.bed
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=bedops
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load bedops/2.4.42

bedops --intersect a.sorted.bed b.sorted.bed > intersection.bed
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BEDOPS documentation](https://bedops.readthedocs.io/)
* [BEDOPS GitHub repository](https://github.com/bedops/bedops)
