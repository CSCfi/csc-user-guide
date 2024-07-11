---
tags:
  - Free
---

# Krona visualization tool

Krona is a visualization tool that allows intuitive exploration of relative abundances and confidences within the 
complex hierarchies of metagenomic classifications. Krona combines a variant of radial, space-filling 
displays with parametric coloring and interactive polar-coordinate zooming. 

Krona charts can be created using an Excel template or KronaTools, which includes support for several 
bioinformatics tools and raw data formats. The interactive charts are self-contained and can be 
viewed with any modern web browser.

[TOC]

## License

Krona is free to use and open source. It is provided under its own [license](https://raw.githubusercontent.com/marbl/Krona/master/KronaTools/LICENSE.txt).

## Available

* Puhti: 2.8.1

## Usage

To use KronaTools commands, load the biokit module:

```bash
module load biokit
```

Many bioinformatics tools provide classifications based on the NCBI Taxonomy. 
These classifications can be imported to Krona via tab-separated files listing 
taxonomy IDs.

For example, file `sample1.tsv`:

```text title="sample1.tsv"
#queryID  #taxID  #score
query1    9606    0.9
query2    9534    0.8
```

can be visualized with the command:

```bash
ktImportTaxonomy sample1.tsv
```

The three columns are by default _query-ID_, _taxonomy-ID_, and _score_ (optional),
but these can be changed using the options `-q`,`-t`, and `-s`. Commented lines (`#`) are ignored.
For example, an output file from [Kraken2](kraken.md) can be visualized with the command:

```bash
ktImportTaxonomy -q 2 -t 3 KrakenOutput -o KronaReport.html
```

The Krona visualizations are based on HTML5. To study them, you can open a virtual desktop in [Puhti web interface](../computing/webinterface/desktop.md) and open a browser there. 

Alternatively, you can copy these files to a publicly accessible data bucket in Allas, and study the results with your local web browser. You can use commands
[a-flip](../data/Allas/using_allas/a_commands.md#a-flip) or [a-publish](../data/Allas/using_allas/a_commands.md#a-publish) to do the copying:

For example the command:

```bash
a-flip KronaReport.html
```

will produce a URL that you can copy to your browser.

In addition to _ktImportTaxonomy_ there are several application-specific data import tools.
For example, for BLAST (`ktImportBLAST`) and MG-RAST (`ktImportMGRAST`). There are also general purpose tools
for text (`ktImportText`) and XML data (`ktImportXML`). On Puhti, you may also be interested to
use `ktImportDiskUsage` to visualize how many different datasets use space in your directories.

## More information

* [Krona wiki](https://github.com/marbl/Krona/wiki)
