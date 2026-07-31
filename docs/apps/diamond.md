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
    - Puhti
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

* Puhti: 2.0.15, 2.1.6, 2.1.10
* Roihu

Check the installed version on Roihu with `module avail diamond` after loading `bio-apps`.

## Usage

### Puhti

To use Diamond, run first the command:

```bash
module load biokit
```

or:

```bash
module load diamond
```

To load a specific version, e.g:

```bash
module load diamond/2.0.15
```

After that, you can check the Diamond help with the command:

```bash
diamond help
```

CSC provides Diamond indexes for SwissProt (swiss), Uniprot (uniprot) and NCBI non-redundant databases (nr). Location of these databases is defined with the environment variable `$DIAMONDDB`. For example, searching hits for a set of nucleotide sequences from the SwissProt database could be done with the command:

```bash
diamond blastx --query nuc.fasta -d $DIAMONDDB/swiss --out diamond_results.txt -p 4 --max-target-seqs 500
```

You can also do searches against your own protein sequence database. In this case, you must first calculate Diamond indexes for your reference protein set with command `diamond makedb`. For example:

```bash
diamond makedb --in refrerence_proteins.fasta -d my_ref -p 4
```

The command above creates a Diamond index file (`my_ref.dmnd`) that can be used as the query database:

```bash
diamond blastx --query nuc.fasta -d my_ref --out diamond_results2.txt -p 4 --max-target-seqs 500
```

### Roihu

On Roihu, Diamond is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load diamond
```

The basic syntax is:

```bash
diamond blastx --query nuc.fasta -d my_ref --out diamond_results.txt \
    -p $SLURM_CPUS_PER_TASK --max-target-seqs 500
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=diamond
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load diamond

srun diamond blastx --query nuc.fasta -d my_ref --out diamond_results.txt \
    -p $SLURM_CPUS_PER_TASK --max-target-seqs 500
```

Submit the job with `sbatch diamond_job.sh`.

## More information

* [Diamond Github page](https://github.com/bbuchfink/diamond)
