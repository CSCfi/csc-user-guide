# Exonerate

## Description

Exonerate is a generic tool for pairwise sequence comparison. It allows you to align sequences using a many alignment models, 
using either exhaustive dynamic programming, or a variety of heuristics. You can use Exonerate for example for:

*   Aligning a cDNA to a genomic sequence
*   Aligning a protein to genomic sequence
*   6-frame translated alignment
*   Genome to genome alignment
*   Exhaustive Smith-Waterman-Gotoh alignment

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available
Version on CSC's Servers

Puhti: 2.4.0

## Usage

In Puhti you can use initialize Exonerate with command:
```text
module load biokit
```
The biokit module sets up a set of commonly used bioinformatics tools, including Exonerate 
(Note however that there are also bioinformatics tools in Puhti, that have a separate setup commands.)

After the setup command the Exonerate commands are recognized.

For example to align cDNA to genomic sequence, you can use exonerate command with _est2genome_ model.
```text
exonerate --model est2genome query.fasta target.fasta
```
You can see the command line options for exonerate with command:
```text
exonerate -h
```
 
In Puhti, large Exronerate tasks should be executed as a batch jobs. Below is a sample batch job file, for running a 
Exonerate batch job in Puhti:

```text
#!/bin/bash
#SBATCH --job-name=exonerate_job
#SBATCH --account=<project>
#SBATCH --time=08:00:00
#SBATCH --mem=8G
#SBATCH --partition=small

module load biokit
exonerate --model est2genome query.fasta target.fasta
```

In the batch job example above, the maximum duration of the job is eight hours (-t 08:00:00 ) and the reserved memory size is 8 GB (--mem=8G).

You can submit the batch job file to the batch job system with command:
```text
sbatch batch_job_file.bash
```

## Manual

*   [Exonerate home page](https://github.com/nathanweeks/exonerate)
*   [Exonerate guides](https://www.animalgenome.org/bioinfo/resources/manuals/exonerate/)

