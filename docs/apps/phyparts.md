---
tags:
  - Free
catalog:
  name: PhyParts
  description: Gene tree concordance and conflict mapped onto a species tree
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PhyParts

PhyParts maps the clades of a set of gene trees onto a species tree and counts how
many gene trees support or conflict with each clade. The gene trees may contain gene
duplications and missing taxa, which is common in transcriptome and genome data.

[TOC]

## License

Free to download and use from the
[PhyParts repository](https://bitbucket.org/blackrim/phyparts). The repository does
not state a specific license.

## Available

* Roihu-CPU: 0.0.1, via the `bio-apps` module.

## Usage

PhyParts is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the PhyParts module:

```bash
module load bio-apps/v202603
module load phyparts/0.0.1
```

For example, run a full concordance and conflict analysis of the gene trees in the
directory `genetrees/` against the species tree `species.tre`:

```bash
phyparts -a 1 -v -d genetrees/ -m species.tre -o out
```

PhyParts assumes rooted trees, so root the gene trees and the species tree before the
analysis. The main options are:

* `-a`: type of analysis: `0` concordance and conflict, `1` full concordance and
  conflict (also counts the alternative topologies), `2` gene duplications
* `-d`: directory or file of gene trees
* `-m`: species tree to map the gene trees onto
* `-s`: ignore gene tree clades with support lower than this value, for example `70`
  for bootstrap support
* `-o`: prefix of the output files
* `-v`: verbose output, also lists the concordant and conflicting gene trees for each
  node

The output files include `out.concon.tre`, which contains the species tree three
times: annotated with the number of concordant gene trees, the number of conflicting
gene trees and the ICA score of each clade. `out.node.key` gives the clade of each
node number used in the other output files.

PhyParts is a Java program, and Java may limit it to a fraction of the memory reserved
for your job. For large datasets, set the maximum memory with the `JAVA_OPTS`
environment variable, for example `export JAVA_OPTS="-Xmx7g"` in a job that reserves
8 GiB.

Small analyses finish quickly in an
[interactive session](../computing/running/interactive-usage.md). Run large datasets
as a [batch job](../computing/running/creating-job-scripts-roihu.md).

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [PhyParts repository](https://bitbucket.org/blackrim/phyparts)
* [Smith, S.A. et al. (2015). Analysis of phylogenomic datasets reveals conflict, concordance, and gene duplications with examples from animals and plants. BMC Evolutionary Biology 15, 150](https://doi.org/10.1186/s12862-015-0423-0)
