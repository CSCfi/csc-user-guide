---
tags:
  - Free
catalog:
  name: MEME Suite
  description: Motif discovery and analysis (MEME Suite)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MEME Suite

The MEME Suite allows the biologist to discover novel motifs in collections of
unaligned nucleotide or protein sequences, and to perform a wide variety of other
motif-based analyses. It includes tools such as `meme`, `meme-chip`, `fimo`, `tomtom`
and `mast`.

[TOC]

## License

The MEME Suite is free for non-commercial and academic use. See the
[MEME Suite copyright and license](https://meme-suite.org/meme/doc/copyright.html).

## Available

* Roihu: 5.5.7, via the `bio-apps` module.

## Usage

MEME Suite is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MEME module:

```bash
module load bio-apps/v202603
module load meme/5.5.7
```

For example, to discover motifs with `meme`:

```bash
meme sequences.fasta -dna -oc meme_out -nmotifs 5
```

`meme` is MPI-enabled and can be parallelized across several processes. Below is an
example batch job using MPI:

```bash
#!/bin/bash
#SBATCH --job-name=meme
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load meme/5.5.7

meme sequences.fasta -dna -oc meme_out -nmotifs 5 -p $SLURM_NTASKS
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MEME Suite home page](https://meme-suite.org/)
