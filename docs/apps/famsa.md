---
tags:
  - Free
catalog:
  name: FAMSA
  description: Fast multiple sequence alignment of very large protein sets
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# FAMSA

FAMSA is a multiple sequence alignment program for large protein datasets. It can
align hundreds of thousands, or with its medoid tree heuristic even millions, of
sequences in reasonable time.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/refresh-bio/FAMSA/blob/master/LICENSE).

## Available

* Roihu-CPU: 2.5.2, via the `bio-apps` module.

## Usage

FAMSA is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the FAMSA module:

```bash
module load bio-apps/v202603
module load famsa/2.5.2
```

FAMSA takes the sequences to align in FASTA format (optionally gzipped) and writes the
alignment in FASTA format:

```bash
famsa -t 8 sequences.fasta alignment.fasta
```

Always set the number of threads with `-t` to match the cores reserved for your job.

Other useful options:

* `-gt`: guide tree method: `sl` (single linkage, default), `upgma` or `nj`
* `-medoidtree`: fast approximate guide tree for very large datasets
* `-gz`: write the alignment gzipped

Run `famsa -help` to see all options.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=famsa
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=8G

module load bio-apps/v202603
module load famsa/2.5.2

famsa -t $SLURM_CPUS_PER_TASK sequences.fasta alignment.fasta
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [FAMSA GitHub repository](https://github.com/refresh-bio/FAMSA)
