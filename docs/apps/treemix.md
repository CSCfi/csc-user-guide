---
tags:
  - Free
catalog:
  name: TreeMix
  description: Population splits and admixture from genome-wide allele frequencies
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# TreeMix

TreeMix infers the splits and mixtures (admixture or migration events) of populations
from genome-wide allele frequency data. It models the history of the populations as a
graph: a tree with added migration edges.

[TOC]

## License

Free to use and open source under GNU GPLv3.

## Available

* Roihu-CPU: 1.13, via the `bio-apps` module.

## Usage

TreeMix is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the TreeMix module:

```bash
module load bio-apps/v202603
module load treemix/1.13
```

The input is a gzipped file of allele counts. Its first line lists the population
names, and each following line gives the counts of the two alleles of one SNP in each
population, for example `5,1 1,1 4,0`.

For example, fit a tree with two migration edges, estimating the covariance matrix in
blocks of 500 SNPs and rooting the tree with population `outgroup`:

```bash
treemix -i allele_counts.gz -m 2 -k 500 -root outgroup -o out_m2
```

The results are written to files starting with `out_m2`. The module also provides the
`threepop`, `fourpop` and `f4ratio` commands for f3 and f4 statistics.

To plot the results, start R in the same session and use the functions from
`plotting_funcs.R`, which comes with TreeMix:

```r
source(Sys.which("plotting_funcs.R"))
plot_tree("out_m2")
```

### Example batch script

TreeMix uses one core. The batch script below fits models with 0 to 5 migration edges:

```bash
#!/bin/bash
#SBATCH --job-name=treemix
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load treemix/1.13

for m in 0 1 2 3 4 5; do
    treemix -i allele_counts.gz -m $m -k 500 -root outgroup -o out_m$m
done
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [TreeMix repository](https://bitbucket.org/nygcresearch/treemix)
* [Pickrell, J.K. & Pritchard, J.K. (2012). Inference of population splits and mixtures from genome-wide allele frequency data. PLOS Genetics 8, e1002967](https://doi.org/10.1371/journal.pgen.1002967)
