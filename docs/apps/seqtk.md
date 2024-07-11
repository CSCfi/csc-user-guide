---
tags:
  - Free
---

# Seqtk

Seqtk is a fast and lightweight tool for processing sequences in the FASTA or FASTQ format. It seamlessly parses both FASTA and FASTQ files which can also be optionally compressed by gzip.

[TOC]

## License

Free to use and open source under [MIT License](https://github.com/lh3/seqtk/blob/master/LICENSE).

## Available

* Puhti: 1.3-r106, 1.4

## Usage

Seqtk is included in the biokit module:

```bash
module load biokit
```

Alternatively, Seqtk can be loaded as an independent module:

```bash
module load seqtk/<version>
```

`seqtk` command syntax is:

```bash
seqtk <command> <arguments>
```

The available Seqtk commands are:

|Command | Function |
|--------|----------------------------------|
|`seq`     |common transformation of FASTA/Q |
|`comp`    |get the nucleotide composition of FASTA/Q |
|`sample`  |sub-sample sequences |
|`subseq`  |extract subsequences from FASTA/Q  |
|`fqchk`   |fastq QC (base/quality summary)  |
|`mergepe` |interleave two PE FASTA/Q files |
|`trimfq`  |trim FASTQ using the Phred algorithm |
|`hety`    |regional heterozygosity |
|`gc`      |identify high- or low-GC regions |
|`mutfa`   |point mutate FASTA at specified positions |
|`mergefa` |merge two FASTA/Q files |
|`famask`  |apply an X-coded FASTA to a source FASTA |
|`dropse`  |drop unpaired from interleaved PE FASTA/Q |
|`rename`  |rename sequence names |
|`randbase`|choose a random base from hets |
|`cutN`    |cut sequence at long N |
|`listhet` |extract the position of each het |

### Examples

Convert FASTQ to FASTA:

```bash
seqtk seq -a in.fq.gz > out.fa
```

Extract sequences with names in file `name.lst`, one sequence name per line:

```bash
seqtk subseq in.fq name.lst > out.fq
```

Extract sequences in regions contained in file `reg.bed`:

```bash
seqtk subseq in.fa reg.bed > out.fa
```

## More information

* [Seqtk home page](https://github.com/lh3/seqtk)
