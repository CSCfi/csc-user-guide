---
tags:
  - Free
catalog:
  name: Prodigal
  description: Gene prediction for prokaryotic genomes
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Prodigal

Prodigal (Prokaryotic Dynamic Programming Genefinding Algorithm) predicts protein-coding
genes in bacterial and archaeal genomes and metagenomes.

[TOC]

## Available

* Roihu-CPU: 2.6.3
* Roihu-GPU: not available

Check the installed versions with `module avail prodigal` after loading `bio-apps`.

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only.

## License

Free to use and open source under
[GPL v3 License](https://github.com/hyattpd/Prodigal/blob/GoogleImport/LICENSE).

## Usage

On Roihu, Prodigal is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load prodigal
```

The basic syntax is:

```bash
prodigal -i genome.fna -o genes.gff -a proteins.faa -p single
```

Prodigal is single-threaded, so a batch job needs only one CPU core. An example batch
job script:

```bash
#!/bin/bash
#SBATCH --job-name=prodigal
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load prodigal

srun prodigal -i genome.fna -o genes.gff -a proteins.faa -p single
```

Submit the job with `sbatch prodigal_job.sh`. For a mixed metagenomic assembly, use
`-p meta` instead.

## More information

* [Prodigal home page](https://github.com/hyattpd/Prodigal)
* [Prodigal wiki](https://github.com/hyattpd/Prodigal/wiki)
* [CSC Service Desk](../support/contact.md)
