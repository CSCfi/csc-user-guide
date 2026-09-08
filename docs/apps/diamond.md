---
tags:
  - Free
catalog:
  name: Diamond
  description: Sequence similarity search tool for proteins and nucleotides
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Diamond

Diamond is a fast sequence similarity search tool for matching nucleotide or protein sequences against protein databases.
The key features of Diamond are:

* Pairwise alignment of proteins and translated DNA at 500x-20,000x speed of BLAST.
* Frameshift alignments for long read analysis.
* Low resource requirements and suitable for running on standard desktops or laptops.
* Various output formats, including BLAST pairwise, tabular and XML, as well as taxonomic classification.

[TOC]

## License

Free to use and open source under [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html).

## Available

* Roihu-CPU: 2.1.10 (module `diamond`), via the `bio-apps` module.

## Usage

Diamond is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Diamond module:

```bash
module load bio-apps/v202603
module load diamond/2.1.10
```

After that, you can check the Diamond help with the command:

```bash
diamond help
```

### Reference databases

CSC provides shared Diamond indexes for the NCBI non-redundant (`nr`) and
SwissProt (`swiss`) protein databases. The `diamond` module sets the environment
variable `$DIAMONDDB` to their location, and you refer to an index by basename
(Diamond appends `.dmnd`). For example, searching a set of nucleotide sequences
against SwissProt:

```bash
diamond blastx --query nuc.fasta -d $DIAMONDDB/swiss --out diamond_results.txt -p 4 --max-target-seqs 500
```

`nr` is very large, so a search against it (`-d $DIAMONDDB/nr`) needs
substantial memory and time — reserve them accordingly.

### Using your own database

You can also search against your own protein sequence database. First build a
Diamond index for your reference protein set with `diamond makedb`:

```bash
diamond makedb --in reference_proteins.fasta -d my_ref -p 4
```

The command above creates a Diamond index file (`my_ref.dmnd`) that can be used
as the query database:

```bash
diamond blastx --query nuc.fasta -d my_ref --out diamond_results2.txt -p 4 --max-target-seqs 500
```

## More information

* [Diamond Github page](https://github.com/bbuchfink/diamond)
