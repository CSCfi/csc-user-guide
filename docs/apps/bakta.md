---
tags:
  - Free
catalog:
  name: Bakta
  description: Rapid and standardized annotation of bacterial genomes, MAGs and plasmids
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Bakta

Bakta is a tool for the rapid and standardized annotation of bacterial genomes,
metagenome-assembled genomes (MAGs) and plasmids. It annotates tRNA, rRNA and other
non-coding RNA genes, CRISPR arrays and protein-coding genes, and identifies known
proteins with a fast, alignment-free sequence lookup. The results are written in
standard formats such as GFF3, GenBank, EMBL and TSV.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/oschwengers/bakta/blob/main/LICENSE).

## Available

* Roihu-CPU: 1.11.4 (module `py-bakta`), via the `bio-apps` module.

## Usage

Bakta is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Bakta module:

```bash
module load bio-apps/v202603
module load py-bakta/1.11.4
```

### Database

Bakta needs a reference database. CSC provides the full Bakta database (version 6.0),
including the AMRFinderPlus database, in `/dataset/project_2020345/bakta/db`. The
`py-bakta` module sets the `BAKTA_DB` environment variable to this directory, so you
don't need to give the `--db` option. CSC keeps the shared database up to date, so
you don't need to run `bakta_db download` or `amrfinder_update` yourself.

### Annotating a genome

Annotate a genome assembly with:

```bash
bakta --output results --prefix sample1 --threads 8 assembly.fasta
```

Useful options include:

* `--genus`, `--species` and `--strain`: organism information for the output files.
* `--locus-tag`: locus tag prefix.
* `--complete`: all sequences are complete replicons (chromosomes or plasmids).
* `--meta`: metagenome mode for gene prediction, for example for MAGs.
* `--compliant`: make the output compliant with GenBank, ENA and DDBJ.
* `--skip-plot`: skip the circular genome plot.

Run `bakta --help` for the full list of options. The results are written to the
`--output` directory: the annotations as `sample1.tsv`, `sample1.gff3`,
`sample1.gbff` and `sample1.embl`, the sequences as `sample1.fna`, `sample1.ffn` and
`sample1.faa`, and a summary in `sample1.txt`.

To annotate protein sequences instead of a genome, use `bakta_proteins`. It uses
the same database; see `bakta_proteins --help`.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=bakta
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load py-bakta/1.11.4

bakta --output results --prefix sample1 --threads $SLURM_CPUS_PER_TASK assembly.fasta
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Bakta GitHub repository](https://github.com/oschwengers/bakta)
* [Bakta documentation](https://bakta.readthedocs.io)
