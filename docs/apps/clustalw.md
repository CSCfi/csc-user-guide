---
tags:
  - Free
catalog:
  name: ClustalW
  description: Multiple alignment tool for nucleic acid and protein sequences
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ClustalW

ClustalW is a classic multiple sequence alignment program for DNA, RNA and protein
sequences, run through its `clustalw2` command-line tool. For large datasets, the
newer Clustal Omega is usually a better choice.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail clustalw` after loading `bio-apps`.

## License

Free to use and open source under
[LGPL v3 License](https://ftp.ebi.ac.uk/pub/software/clustalw2/2.1/COPYING.LESSER).

## Usage

On Roihu, ClustalW is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load clustalw
```

The basic syntax is:

```bash
clustalw2 -INFILE=input.fasta -OUTFILE=aligned.aln
```

Heavier jobs should be run as batch jobs. ClustalW is single-threaded, so a job only
needs one CPU core. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=clustalw
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load clustalw

srun clustalw2 -INFILE=input.fasta -OUTFILE=aligned.aln
```

Submit the job with `sbatch clustalw_job.sh`.

## More information

* [ClustalW2 files at EBI](https://ftp.ebi.ac.uk/pub/software/clustalw2)
* [CSC Service Desk](../support/contact.md)
