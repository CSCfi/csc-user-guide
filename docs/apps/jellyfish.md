---
tags:
  - Free
catalog:
  name: Jellyfish
  description: Fast k-mer counting
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Jellyfish

JELLYFISH is a tool for fast, memory-efficient counting of k-mers in DNA. It can count
k-mers using an in-memory hash table and is commonly used for genome-size estimation
and other k-mer based analyses.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/gmarcais/Jellyfish/blob/master/LICENSE).

## Available

* Roihu: 2.2.7, via the `bio-apps` module.

## Usage

Jellyfish is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Jellyfish module:

```bash
module load bio-apps/v202603
module load jellyfish/2.2.7
```

Count k-mers (here 21-mers) and generate a histogram:

```bash
jellyfish count -m 21 -s 100M -t 8 -C reads.fasta -o mer_counts.jf
jellyfish histo mer_counts.jf > mer_counts.histo
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=jellyfish
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load jellyfish/2.2.7

jellyfish count -m 21 -s 100M -t $SLURM_CPUS_PER_TASK -C reads.fasta -o mer_counts.jf
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Jellyfish home page](https://www.cbcb.umd.edu/software/jellyfish/)
* [Jellyfish GitHub repository](https://github.com/gmarcais/Jellyfish)
