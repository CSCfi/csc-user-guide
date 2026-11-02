---
tags:
  - Free
catalog:
  name: XHMM (eXome-Hidden Markov Model)
  description: Copy number variation calling from targeted sequencing data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# XHMM (eXome-Hidden Markov Model)

The XHMM C++ software suite was written to call copy number variation (CNV)
from next-generation sequencing projects, where exome capture was used
(or targeted sequencing, more generally).

XHMM uses principal component analysis (PCA) normalization and a hidden Markov model (HMM)
to detect and genotype copy number variation (CNV) from normalized
read-depth data from targeted sequencing experiments.

XHMM was explicitly designed to be used with targeted exome sequencing at
high coverage (at least 60x - 100x) using Illumina HiSeq (or similar) sequencing
of at least ~50 samples. However, no part of XHMM explicitly requires these
particular experimental conditions, just high coverage of genomic regions
for many samples.

[TOC]

## License

Software is free to use and open source, but no license is specified.

## Available

* Roihu-CPU: 20160104 (commit cc14e52), via the `bio-apps` module.

## Usage

XHMM is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the XHMM module:

```bash
module load bio-apps/v202603
module load xhmm/20160104
```

After that, XHMM starts with the command:

```bash
xhmm
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [XHMM home page](https://statgen.bitbucket.io/xhmm/index.html)
* [XHMM tutorial](https://statgen.bitbucket.io/xhmm/tutorial.html)
