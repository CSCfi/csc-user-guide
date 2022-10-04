# EMBOSS

## Description


EMBOSS (European Molecular Biology Open Software Suite) package contains over 200 programs for sequence analysis. 
EMBOSS is designed for classical sequence analysis were the amount of seqences are less than 100 000. Because of that, 
most of the tools are not effective for raw NGS datasets where you have milloins sequences (reads).
Examples of application areas of EMBOSS tools are given below.

*    Sequence alignment
*    Phylogeny
*    Hidden Markow models
*    Rapid database searching with sequence patterns
*    Protein motif identification, including domain analysis
*    EST analysis
*    Nucleotide sequence pattern analysis, for example to identify CpG islands.
*    Simple and species-specific repeat identification
*    Codon usage analysis for small genomes
*    Rapid identification of sequence patterns in large scale sequence sets.
*    Presentation tools for publication
*    RNA secondary structure prediction

## License

Free to use and open source under [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## Available

Version on CSC's Servers

-   Puhti: 6.5.7
-   [Chipster](https://chipster.csc.fi) provides a graphical interface to many EMBOSSS tools.
## Usage

To make EMBOSS programs available in Puhti super-cluster, give command:

```text
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools, including EMBOSS. Note however that there are bioinformatics tools in Puhti, that have a separate setup commands.

After loading biokit, you can start any of the EMBOSS programs by typing its name. For example:
```text
wossname
```
The _wossname_ command is a help tool that you can use to see what EMBOSS commands are available. You can also use it to search EMBOSS tools using key words.


## Manual

*    [Homepage of EMBOSS project](http://emboss.open-bio.org/)
*    [EMBOSS programs sorted alphabetically](https://extras.csc.fi/emboss/doc/programs/html/index.html)
*    [EMBOSS programs sorted by function](https://extras.csc.fi/emboss/doc/programs/html/groups.html)
*    [EMBOSS Quick Guide](https://extras.csc.fi/emboss/emboss_qg.pdf)
*    [Getting started with EMBOSS -tutorial](http://emboss.sourceforge.net/docs/emboss_tutorial/emboss_tutorial.html)


