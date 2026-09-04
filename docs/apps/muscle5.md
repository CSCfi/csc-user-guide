---
tags:
  - Free
catalog:
  name: MUSCLE5
  description: Multiple sequence alignment (v5)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MUSCLE5

MUSCLE5 is the current major version of MUSCLE, widely-used software for making multiple
alignments of protein and nucleotide sequences. It introduces new algorithms and the
ability to generate ensembles of alternative alignments. For the older version 3, see
[MUSCLE](muscle.md).

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/rcedgar/muscle/blob/main/LICENSE).

## Available

* Roihu: 5.1.0, via the `bio-apps` module.

## Usage

MUSCLE5 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MUSCLE5 module:

```bash
module load bio-apps/v202603
module load muscle5/5.1.0
```

Align sequences from a FASTA file:

```bash
muscle5 -align sequences.fasta -output aligned.fasta -threads 8
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=muscle5
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load muscle5/5.1.0

muscle5 -align sequences.fasta -output aligned.fasta -threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MUSCLE5 home page](https://drive5.com/muscle5/)
* [MUSCLE5 GitHub repository](https://github.com/rcedgar/muscle)
