# Krona visualization tool

## Description

Krona is a visualization tool that allows intuitive exploration of relative abundances and confidences within the 
complex hierarchies of metagenomic classifications. Krona combines a variant of radial, space-filling 
displays with parametric coloring and interactive polar-coordinate zooming. 

Krona charts can be created using an Excel template or KronaTools, which includes support for several 
bioinformatics tools and raw data formats. The interactive charts are self-contained and can be 
viewed with any modern web browser.

[TOC]

## License

Krona is free to use and open source. It is provided under it's own [license](https://raw.githubusercontent.com/marbl/Krona/master/KronaTools/LICENSE.txt).

## Version

*  Krona 2.7.1 is available in Puhti 

## Usage

To take in use KronaTools commands, load the biokit module.

```text
module load biokit
```
Many bioinformatics tools provide classifications based on the NCBI Taxonomy. 
These classifications can be imported to Krona via tab-separated files listing 
taxonomy IDs.

For example file (sample1.tsv)

```text
#queryID  #taxID  #score
query1    9606    0.9
query2    9534    0.8
```
Can be visualized with command:

```text
ktImportTaxonomy sample1.sv 
```
The three columns, by default, are _query-ID_, _taxonomy-ID_, and _score_ (optional), 
but these can be changed using options `-q`,`-t`, and `-s`. Commented lines (#) are ignored. 
For example an output file from [Kraken2](./kraken.md) can be visualized with command:

```text
ktImportTaxonomy -q 2 -t 3 KrakenOutput -o KronaReport.html
```
The Krona visualizations are based on HTML5 and thus it is not straight forward to study them in Puhti.
However if you copy these files to a publicly accessible data bucket in Allas, you can study the results with
your local web browser. You can use commands [a-flip](../../data/Allas/using_allas/a_commands/#a-flip) or [a-publish](../data/Allas/using_allas/a_commands.md#a\
-publish) to do the copying:

For example command:
```text
a-flip KronaReport.html
```
Will produce a URL that you can copy to you browser.

In addition to _ktImportTaxonomy_ there are several application specific data import tools: 
For example for BLAST (_ktImportBLAST_) and MG-RAST (_ktImportMGRAST_). There are also general purpose tools
for text (_ktImportText_) and XML data (_ktImportXML_). In Puhti you may also be interested to
use _ktImportDiskUsage_ to visualize how much different datasets use space in your directories.

## More information

*   [Krona wiki](https://github.com/marbl/Krona/wiki)



