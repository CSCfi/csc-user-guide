---
tags:
  - Non-commercial
catalog:
  name: MEME Suite
  description: Motif discovery and analysis in nucleotide and protein sequences
  license_type: Non-commercial
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MEME Suite

The MEME Suite discovers novel sequence motifs shared by a set of unaligned nucleotide
or protein sequences, and offers a wide range of further motif-based analyses, such as
scanning sequences for known motifs or comparing motifs to each other.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail meme` after loading `bio-apps`.

## License

Free to use for educational, research and non-profit purposes. Commercial use requires a
licence from UC San Diego's Office of Innovation and Commercialization; see the
[MEME Suite copyright notice](https://meme-suite.org/meme/doc/copyright.html).

## Usage

On Roihu, the MEME Suite is part of the `bio-apps` collection, which has to be loaded
first:

```bash
module load bio-apps
module load meme
```

The basic syntax for motif discovery is:

```bash
meme sequences.fa -oc meme_out -dna -mod zoops -nmotifs 5
```

`-dna` (or `-protein`) sets the alphabet, and `-mod` selects the motif distribution
model: `oops` (one occurrence per sequence), `zoops` (zero or one) or `anr` (any number
of repetitions).

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=meme
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load meme

srun meme sequences.fa -oc meme_out -dna -mod zoops -nmotifs 5
```

Submit the job with `sbatch meme_job.sh`.

## More information

* [MEME Suite home page](https://meme-suite.org)
* [meme command reference](https://meme-suite.org/meme/doc/meme.html)
* [CSC Service Desk](../support/contact.md)
