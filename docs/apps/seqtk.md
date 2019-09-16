
# Seqtk

## Description

Seqtk is a fast and lightweight tool for processing sequences in the FASTA or FASTQ format. It seamlessly parses both FASTA and FASTQ files which can also be optionally compressed by gzip.


## Available

*    bs version 1.0.0 is available in Puhti

## Usage


Seqtk command syntax is:
```text
seqtk <command> <arguments>
```
The available seqtk commands are:

|Command | Function |
|--------|----------------------------------|
|seq     |common transformation of FASTA/Q |
|comp    |get the nucleotide composition of FASTA/Q |
|sample  |subsample sequences |
|subseq  |extract subsequences from FASTA/Q  |
|fqchk   |fastq QC (base/quality summary)  |
|mergepe |interleave two PE FASTA/Q files |
|trimfq  |trim FASTQ using the Phred algorithm |
|hety    |regional heterozygosity |
|gc      |identify high- or low-GC regions |
|mutfa   |point mutate FASTA at specified positions |
|mergefa |merge two FASTA/Q files |
|famask  |apply a X-coded FASTA to a source FASTA |
|dropse  |drop unpaired from interleaved PE FASTA/Q |
|rename  |rename sequence names |
|randbase|choose a random base from hets |
|cutN    |cut sequence at long N |
|listhet |extract the position of each het |

Examples:

Convert FASTQ to FASTA:
```text
seqtk seq -a in.fq.gz > out.fa
```
Extract sequences with names in file name.lst, one sequence name per line:
```text
seqtk subseq in.fq name.lst > out.fq
```
Extract sequences in regions contained in file reg.bed:
```text
seqtk subseq in.fa reg.bed > out.fa
```

## Manual

*   [Seqtk home page](https://github.com/lh3/seqtk)


