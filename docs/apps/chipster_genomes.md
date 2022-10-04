# chipster_genomes

## Description

Chipster_genomes is a help tool to download genome indexes used in [Chipster software](https://chipster.csc.fi/index.shtml) to Puhti.
CSC is maintaining several short read aligners (e.g. BWA, Bowtie2, STAR) in Puhti, but not the pre-calculated 
indexes for reference genomes. By default, users need to import and index themselves the reference genomes they are using.

The Chipster server however contains indexes for a set of commonly used reference organisms for several aligners.

The _chipster_genomes_ tool allows Puhti users to download the reference genome index files from the Chipster server to 
Puhti so that they can be used in Puhti too.

The genome data and indexes used in Chipster are based on the data available in Ensembl and Ensembl genomes databases. 
However, in Chipster only those sequences (chromosomes) that have been assigned to a karyotype, are included. 
Further, in GTF files negative location values are removed.

Thus the data downloaded from Chipster server may in some cases differ from the data obtained directly from Ensembl.

[TOC]

## License

Free to use and open source.
 
## Available

Available in Puhti

## Usage

chipster_genomes tool in included in _biokit module_. So to make it available, you must first run set-up command:
```text
module load biokit
```

After that you can use `chipster_genomes` command. This command needs two parameters:

*    File or index type (bed, gtf, fasta, bowtie, bowtie, bowtie2, BWA, Hisat2, TopHat2)
*    Species name

If the command is launched without any arguments, it first lists the available data types and asks to select one of them.
Then the species available for the given datatype are listed and the tool asks user to select one of them.
```text
chipster_genomes
```

The data type can alternatively be given as the first argument and the species name as the second argument.
For example the BWA indexes of Danio_rerio.GRCz11 can be retrieved with command:
```text
chipster_genomes bwa Danio_rerio.GRCz11
```
Note that as the index files may be rather large, you should normally download the data to your _scratch_ disk area.
