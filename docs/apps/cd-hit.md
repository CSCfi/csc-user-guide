
# CD-HIT
## Description

CD-HIT can be used for clustering large sequence sets or removing identical or highly similar sequences from a sequence set. 
CD-HIT is often used as a tool to produce a non-redundant sequence set for further analysis of a large sequence set. 
CD-HIT recognizes fasta and fastq sequence formats.

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## Available
Version on CSC's Servers

Puhti: 4.8.1 

## Usage

The setup command for CD-HIT in Puhti cluster is:
```text
module load biokit
```

After the setup command, the server recognizes CD-HIT commands. The CD-HIT package has many programs. The most notable are:

| Program | Description |
|---------|-------------|
|cd-hit |Clustering and redundance removal tool for protein sequences|
|cd-hit-est |	Clustering and redundance removal tool for nucleic acid sequences (only for sequences that do not contain introns)|
|cd-hit-2d | Tool to compare two protein sequence sets |
|cd-hit-est-2d | Tool to compare two nucleic sequence sets |
|cd-hit-454 | A program to identify artificial duplicates from raw 454 sequencing reads |
|cd-hit	| Cluster peptide sequences	|
|psi-cd-hit	| Cluster proteins at less than 40% cutoff	|
|cd-hit-lap	| Identify overlapping reads |
|cd-hit-dup | Identify duplicates from single or paired Illumina reads |	
|cd-hit-454 | Identify duplicates from 454 reads |
|h-cd-hit | Hierarchical clustering |	
 

A full list of programs can be found in the CD-HIT user guide.

You can list the command line options of CD-HIT programs by using option `-help`. For example:
```text
cd-hit -help
```

A simple analysis for a protein sequence set can be done for example with command:
```text
cd-hit -i my_proteins.fasta -o reduced_set.fasta -c 0.95
```
The sample command above produces two result files:

*   _reduced_set.fasta_ contains a pruned sequence set. In this case, if two sequences are more than 95% identical, only the longer one is included to the results.
*   _reduced_set.fasta.clstr_ contains information about the clustering of the sequences that share higher similarity than the give threshold value (in this case 95%).


## Support

servicedesk@csc.fi
## Manual

*   [CD-HIT user guide](https://github.com/weizhongli/cdhit/wiki)

*   [CD-HIT home page](http://weizhongli-lab.org/cd-hit/)
