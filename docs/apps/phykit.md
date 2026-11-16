---
tags:
  - Free
catalog:
  name: PhyKIT
  description: Toolkit for processing and analysing phylogenomic data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PhyKIT

PhyKIT is a command-line toolkit for processing and analysing multiple sequence
alignments and phylogenetic trees. It has commands for tasks such as calculating
alignment and tree statistics, concatenating alignments into a supermatrix and
assessing tree properties.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/JLSteenwyk/PhyKIT/blob/main/LICENSE.md).

## Available

* Roihu-CPU: 2.1.94 and 2.8.0 (module `py-phykit`), via the `bio-apps` module.

## Usage

PhyKIT is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the PhyKIT module:

```bash
module load bio-apps/v202603
module load py-phykit/2.8.0
```

PhyKIT is run as `phykit <command>`. For example:

```bash
# length of an alignment
phykit alignment_length alignment.fasta

# treeness of a phylogeny
phykit treeness tree.nw

# concatenate the alignments listed in alignments.txt into a supermatrix
phykit create_concatenation_matrix -a alignments.txt -p supermatrix
```

Run `phykit -h` to list all commands, and `phykit <command> -h` for the options of a
command.

Most PhyKIT commands finish in seconds. Run analyses of large datasets in an
[interactive session](../computing/running/interactive-usage.md) or as a
[batch job](../computing/running/creating-job-scripts-roihu.md).

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [PhyKIT documentation](https://jlsteenwyk.com/PhyKIT/)
* [PhyKIT GitHub repository](https://github.com/JLSteenwyk/PhyKIT)
* [Steenwyk, J.L. et al. (2021). PhyKIT: a broadly applicable UNIX shell toolkit for processing and analyzing phylogenomic data. Bioinformatics 37, 2325–2331](https://doi.org/10.1093/bioinformatics/btab096)
