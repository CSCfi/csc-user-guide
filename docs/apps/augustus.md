---
tags:
  - Free
catalog:
  name: AUGUSTUS
  description: Gene prediction in eukaryotic genomic sequences
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# AUGUSTUS

AUGUSTUS predicts protein-coding genes in eukaryotic genomic sequences, trained on
species-specific models built from known gene structures.

[TOC]

## Available

* Roihu-CPU: 3.5.0
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail augustus` after loading `bio-apps`.

## License

Free to use and open source under
[Artistic License](https://github.com/Gaius-Augustus/Augustus/blob/master/src/LICENSE.TXT).

## Usage

On Roihu, AUGUSTUS is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load augustus
```

The basic syntax is:

```bash
augustus --species=<species> genome.fasta > genes.gff
```

AUGUSTUS is single-threaded. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=augustus
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load augustus

srun augustus --species=human genome.fasta > genes.gff
```

Submit the job with `sbatch augustus_job.sh`.

## More information

* [AUGUSTUS home page](https://bioinf.uni-greifswald.de/augustus/)
* [AUGUSTUS on GitHub](https://github.com/Gaius-Augustus/Augustus)
* [CSC Service Desk](../support/contact.md)
