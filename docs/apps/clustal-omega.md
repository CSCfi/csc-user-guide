---
tags:
  - Free
catalog:
  name: Clustal Omega
  description: Multiple sequence alignment tool for protein and nucleotide sequences
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Clustal Omega

Clustal Omega is a multiple sequence alignment program for proteins and nucleotide
sequences, built to scale to very large datasets of hundreds of thousands of
sequences. It is the modern replacement for ClustalW in most Clustal-based workflows.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail clustal-omega` after loading `bio-apps`.

## License

Free to use and open source under
[GPL v2 License](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## Usage

On Roihu, Clustal Omega is part of the `bio-apps` collection, which has to be loaded
first:

```bash
module load bio-apps
module load clustal-omega
```

The basic syntax is:

```bash
clustalo -i input.fasta -o aligned.fasta
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=clustalo
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load clustal-omega

srun clustalo -i input.fasta -o aligned.fasta --threads=$SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch clustalo_job.sh`.

## More information

* [Clustal Omega home page](https://www.clustal.org/omega/)
* [CSC Service Desk](../support/contact.md)
