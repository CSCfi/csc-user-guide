---
tags:
  - Free
catalog:
  name: Exonerate
  description: A generic tool for pairwise sequence comparison
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
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

* Roihu: 2.4.0, via the `bio-apps` module.

## Usage

Exonerate is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Exonerate module:

```bash
module load bio-apps/v202603
module load exonerate/2.4.0
```

After loading, the `exonerate` commands are recognized.

For example, to align cDNA to genomic sequence, you can use the `exonerate` command with the `est2genome` model:

```bash
exonerate --model est2genome query.fasta target.fasta
```

You can see the command line options for `exonerate` with the command:

```bash
exonerate -h
```
 
Large Exonerate tasks should be executed as batch jobs. Below is a sample batch job script for running an 
Exonerate batch job on Roihu:

```bash
#!/bin/bash
#SBATCH --job-name=exonerate_job
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=08:00:00
#SBATCH --partition=small
#SBATCH --mem=8G

module load bio-apps/v202603
module load exonerate/2.4.0

exonerate --model est2genome query.fasta target.fasta
```

In the batch job example above, the maximum duration of the job is eight hours (`--time=08:00:00`) and the reserved memory is 8 GB (`--mem=8G`). Replace `<project>` with your CSC project (for example `project_2001234`).

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Exonerate home page](https://github.com/nathanweeks/exonerate)
* [Exonerate guides](https://www.animalgenome.org/bioinfo/resources/manuals/exonerate/)
