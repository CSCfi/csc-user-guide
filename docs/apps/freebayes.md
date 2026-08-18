---
tags:
  - Free
catalog:
  name: Freebayes
  description: Genetic variant detector
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Freebayes

FreeBayes is a genetic variant detector designed to find small polymorphisms (SNPs, indels, MNPs and complex events).

FreeBayes is haplotype-based, in the sense that it calls variants based on the literal sequences of reads aligned to a particular target, not their precise alignment. This model is a straightforward generalization of previous ones (e.g. PolyBayes, samtools, GATK) which detect or report variants based on alignments. This method avoids one of the core problems with alignment-based variant detection, that identical sequences may have multiple possible alignments.

FreeBayes uses short-read alignments (BAM files) for any number of individuals from a population and a reference genome to determine the most-likely combination of genotypes for the population at each position in the reference. It reports positions which it finds putatively polymorphic in variant call file (VCF) format. It can also use an input set of variants (VCF) as a source of prior information, and a copy number variant map (BED) to define non-uniform ploidy variation across the samples under analysis.

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/freebayes/freebayes/master/LICENSE).

## Available

* Roihu: 1.3.6

## Usage

FreeBayes can be taken in use by first loading the bio-apps module:

```bash
module load bio-apps
module load freebayes
```

After this you can launch Freebayes. For example:

```bash
freebayes -f reference.fa input.bam > results.vcf
```

Note that FreeBayes requires a BAM file that is indexed. A BAM file can be indexed with command:

```bash
module load samtools
samtools index input.bam
```

FreeBayes analysis jobs can be computationally heavy and should be run as batch jobs on Roihu.


## More information

* [Freebayes home page](https://github.com/ekg/freebayes/blob/master/README.md)
* [Reference publication](https://arxiv.org/abs/1207.3907)
