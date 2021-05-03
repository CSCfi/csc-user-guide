# SALMON

## Description

Salmon is a wicked-fast program to produce a highly-accurate, transcript-level quantification estimates from RNA-seq data. Salmon achieves is accuracy and speed via a number of different innovations, including the use of quasi-mapping (accurate but fast-to-compute proxies for traditional read alignments), and massively-parallel stochastic collapsed variational inference. The result is a versatile tool that fits nicely into many different pipelines. For example, you can choose to make use of our quasi-mapping algorithm by providing Salmon with raw sequencing reads, or, if it is more convenient, you can provide Salmon with regular alignments (e.g. an unsorted BAM file produced with your favorite aligner), and it will use the same wicked-fast, state-of-the-art inference algorithm to estimate transcript-level abundances for your experiment.

NOTE: Salmon works by (quasi)-mapping sequencing reads directly to the transcriptome. This means the Salmon index should be built on a set of target transcripts, not on the genome of the underlying organism. If indexing appears to be taking a very long time, or using a tremendous amount of memory (which it should not), please ensure that you are not attempting to build an index on the genome of your organism!

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

Version on CSC's Servers

-   Puhti: v0.14.1, 0.99.0b2, 1.1.0, 1.4.0

## Usage

In Puhti, the Salmon command is activated by loading the salmon module.

```text
module load salmon
```
For usage help use command:
```text
salmon --help
```
!!! Note

    Note that loading the biokit module will load an older version of Salmon that comes with Trinity.
    To use latest vesion of Salmon, load salmon module instead.


## Manual

*   [Salmon documentation](https://salmon.readthedocs.io/en/latest/)





