---
tags:
  - Free
catalog:
  name: Canu
  description: Long-read (PacBio/Nanopore) genome assembler
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Canu

Canu is a single-molecule sequence assembler for genomes large and small. It is
designed for high-noise long reads such as those from PacBio or Oxford Nanopore
sequencers, and performs correction, trimming and assembly.

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://github.com/marbl/canu/blob/master/README.license.GPL).

## Available

* Roihu: 2.2, via the `bio-apps` module.

## Usage

Canu is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Canu module:

```bash
module load bio-apps/v202603
module load canu/2.2
```

A basic assembly specifies a prefix (`-p`), an output directory (`-d`), the genome
size and the read type:

```bash
canu -p asm -d assembly genomeSize=5m -nanopore reads.fq.gz
```

!!! info "Grid (Slurm) submission"
    By default Canu detects the Slurm batch system and submits its own jobs to the
    queue. To instead run the whole assembly inside a single batch job allocation, set
    `useGrid=false` (recommended for small and medium genomes). For large genomes you
    can let Canu use the grid and pass account/partition settings with
    `gridOptions="--account=<project> --partition=small"`.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=canu
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load canu/2.2

canu -p asm -d assembly genomeSize=5m -nanopore reads.fq.gz \
    useGrid=false maxThreads=$SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Canu documentation](https://canu.readthedocs.io/)
* [Canu GitHub repository](https://github.com/marbl/canu)
