---
tags:
  - Free
catalog:
  name: NGS-PrimerPlex
  description: Design of multiplex PCR primer panels for targeted NGS
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# NGS-PrimerPlex

NGS-PrimerPlex designs primers for multiplex PCR panels for targeted
next-generation sequencing (NGS). It designs primer pairs for the target regions,
checks them for non-target binding in the genome and for common SNPs, and
distributes them into multiplex reactions.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/aakechin/NGS-PrimerPlex/blob/master/LICENSE).

## Available

* Roihu-CPU: 1.3.4, via the `bio-apps` module.

## Usage

NGS-PrimerPlex is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the NGS-PrimerPlex module:

```bash
module load bio-apps/v202603
module load ngs-primerplex/1.3.4
```

On Roihu, NGS-PrimerPlex is available as command-line tools only, without the
graphical user interface.

Primer design and the genome checks can take hours, so run NGS-PrimerPlex in a
batch job, not on the login node. See the
[example batch script](#example-batch-script) below.

NGS-PrimerPlex needs a reference genome FASTA file. For the non-target binding
check (`-blast`, see below), the reference must also be indexed with BWA. See
[BWA indexes](bwa.md#bwa-indexes) for how to find or make the index.

The target regions are given in a tab-separated file with one region per line:
chromosome, start position, end position and amplicon name. These can be followed
by the multiplex reactions to use, the type of primers (`L`, `R` or `B` for left,
right or both) and `W` to amplify the whole region as one amplicon. The chromosome
names must match those in the reference FASTA file:

```text
chr12	25245346	25245351	KRAS	1	B	NotW
chr7	140753335	140753337	BRAF	1	B	NotW
```

These example coordinates are based on the human GRCh38/hg38 reference genome. Ensure that the coordinates in your regions file match the assembly used for the reference FASTA. Any GenBank annotations and dbSNP files must also use the same assembly.

You can also make the regions file from a list of genes with `getGeneRegions.py`.
This needs a directory with a GenBank file for each chromosome, named after the
chromosome in the reference FASTA file (for example `chr1.gb`):

```bash
getGeneRegions.py -glf genes.txt -ref genbank/ -wgref genome.fa -rf genes.regions.csv
```

The gene list has one gene per line, optionally with the exons or codons to target.
See the
[example gene list](https://github.com/aakechin/NGS-PrimerPlex/blob/master/example_gene_list_file.txt)
in the NGS-PrimerPlex repository.

Design the primers, with `-th` giving the number of threads (the default is two):

```bash
NGS_primerplex.py -regions genes.regions.csv -ref genome.fa -blast -th 8
```

`-blast` checks the primers for non-target binding in the genome with BWA. To also
leave out primers that cover common SNPs, add `-snps -dbsnp` with a bgzipped and
indexed dbSNP VCF file for your reference genome.

The results are written next to the regions file. The primers of each multiplex
variant are in `genes.regions_primers_combination_<number>_info.xls`. If primers
cannot be designed for some regions, run `NGS_primerplex.py` again with less strict
parameters and add `-draft genes.regions_all_draft_primers.xls`. It then designs
primers only for the remaining regions.

To add adapter sequences to the designed primers, use `addSeqToPrimers.py`.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=ngs-primerplex
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G

module load bio-apps/v202603
module load ngs-primerplex/1.3.4

NGS_primerplex.py -regions genes.regions.csv -ref genome.fa -blast -th $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [NGS-PrimerPlex GitHub repository](https://github.com/aakechin/NGS-PrimerPlex)
