
# Diamond

## Description

Diamond is a fast sequence similarity search tool for matching nucleotide or protein sequences against protein databases.
The key features of Diamond are:

*   Pairwise alignment of proteins and translated DNA at 500x-20,000x speed of BLAST.
*   Frameshift alignments for long read analysis.
*   Low resource requirements and suitable for running on standard desktops or laptops.
*   Various output formats, including BLAST pairwise, tabular and XML, as well as taxonomic classification.

[TOC]

## License

Free to use and open source under [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html).

## Available
*   Diamond 2.0.14 is available in Puhti

## Usage

To use Diamond, run first command:
```text
module load biokit
```
Afrer that, you can check the Diamond help with command:
```text
diamond help
```
CSC provides Diamond indexes for Uniprot databases (swiss, trembl) and NCBI non redundant database (nr). Location of these databases is defined with environment variable `$DIAMONDDB`.  For example searching hits for a set of nucleotide sequeces from the SwissProt database could be done with  command:
```text
diamond blastx --query nuc.fasta -d $DIAMONDDB/swiss --out diamond_results.txt -p 4 --max-target-seqs 500
```
You can also do searches against your own protein sequence database.  In this case you must first calculate Diamond indexes for your reference protein set with command diamond makedb. For example:
```text
diamond makedb --in refrerence_proteins.fasta -d my_ref -p 4
```
The command above creates a Diamond index file ( my_ref.dmnd) that can be used as the query database:
```text
diamond blastx --query nuc.fasta -d my_ref --out diamond_results2.txt -p 4 --max-target-seqs 500
```


Manual
[Diamond Github page](https://github.com/bbuchfink/diamond)
