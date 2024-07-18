---
tags:
  - Free
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

* Puhti: 0.0.0.2016_01_04.cc14e52 

## Usage

To use XHMM, load the module:

```bash
module load xhmm
```

After that, XHMM starts with the command:

```bash
xhmm
```

## More information

* [XHMM home page](https://statgen.bitbucket.io/xhmm/index.html)
