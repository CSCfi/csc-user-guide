---
tags:
  - Free
---

# Exonerate

Exonerate is a generic tool for pairwise sequence comparison. It allows you to align sequences using a many alignment models, 
using either exhaustive dynamic programming, or a variety of heuristics. You can use Exonerate for example for:

* Aligning a cDNA to a genomic sequence
* Aligning a protein to genomic sequence
* 6-frame translated alignment
* Genome to genome alignment
* Exhaustive Smith-Waterman-Gotoh alignment

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

Puhti: 2.4.0

## Usage

On Puhti, you can initialize Exonerate with the command:

```bash
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools, including Exonerate.
Note however that there are other bioinformatics tools in Puhti that have separate setup commands.

After loading the `biokit` module, the `exonerate` commands are recognized.

For example, to align cDNA to genomic sequence, you can use `exonerate` command with `est2genome` model:

```bash
exonerate --model est2genome query.fasta target.fasta
```

You can see the command line options for `exonerate` with the command:

```bash
exonerate -h
```
 
On Puhti, large Exonerate tasks should be executed as a batch jobs. Below is a sample batch job file for running an 
Exonerate batch job in Puhti:

```bash
#!/bin/bash
#SBATCH --job-name=exonerate_job
#SBATCH --account=<project>
#SBATCH --time=08:00:00
#SBATCH --mem=8G
#SBATCH --partition=small

module load biokit
exonerate --model est2genome query.fasta target.fasta
```

In the batch job example above, the maximum duration of the job is eight hours (`--time=08:00:00`) and the reserved memory is 8 GB (`--mem=8G`).

You can submit the batch job file to the batch job system with command:

```bash
sbatch batch_job_file.bash
```

## More information

* [Exonerate home page](https://github.com/nathanweeks/exonerate)
* [Exonerate guides](https://www.animalgenome.org/bioinfo/resources/manuals/exonerate/)
