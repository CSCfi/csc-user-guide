# MetaPhlAn

## Description

MetaPhlAn is a computational tool for profiling the composition of microbial communities from metagenomic sequencing data. 
MetaPhlAn relies on unique clade-specific marker genes identified from ~17,000 reference genomes.

[TOC]

## License

Free to use and open source under [MIT License](https://github.com/biobakery/MetaPhlAn2/blob/master/license.txt).

## Availability

*   MetaPhlAn 3.0 is available in Puhti

## Usage

In Puhti, MetaPhlAn is installed as part of gcc 9.1.0 compatible _biopythontools_ module.
To activate it, run commands:

```text
module load biokit
module load biopythontools
metaphlan
```
MetaPhlAn can automatically retrieve the MetaPhlAn database and create the Bowtie2 indexes it needs on-the-fly 
when it the command is executed. By default MetaPhlAn saves these index files to the MetaPhlAn installation directory, but in Puhti,
this is not possible. Because of that, the users should use option `--bowtie2db` 
to define a directory that will be used to store the database and index files. 
 
For example in the case of _project_2001234_ the user could first create a directory for the databases:
```text
cd /scratch/project_2001234
mkdir metaphlan_databases
```
A test input dataset for testing MataPhlAn can be downloaded from the metaphlan gothub site:
```text
wget https://github.com/biobakery/biobakery/raw/master/demos/biobakery_demos/data/metaphlan3/input/SRS014476-Supragingival_plaque.fasta.gz
```
In the MetaPhlAn command `--bowtie2db` is used to define the database directory. In this example the job is executed as an interactive batch job.

```text
sinteractive -m 4G -c 4
module load biokit
module load biopythontools
metaphlan --bowtie2db metaphlan_databases  SRS014476-Supragingival_plaque.fasta.gz --input_type fasta > SRS014476-Supragingival_plaque_profile.txt
```

# More information
*   [MetaPhlAn 3.0 home page](https://github.com/biobakery/MetaPhlAn/tree/3.0)
*   [MetaPhlAn 3.0 tutorial](https://github.com/biobakery/biobakery/wiki/metaphlan3)
