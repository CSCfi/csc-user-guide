---
tags:
  - Free
catalog:
  name: BUSCO
  description: Assessment of genome assembly and annotation completeness
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BUSCO

BUSCO assesses the completeness of a genome assembly, gene set or transcriptome by
searching for a curated set of near-universal single-copy orthologous genes. The
results give a quick measure of how complete and well-assembled a dataset is.

[TOC]

## Available

* Roihu-CPU: 5.4.3
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail busco` after loading `bio-apps`.

## License

Free to use and open source under
[MIT License](https://gitlab.com/ezlab/busco/-/blob/master/LICENSE).

## Usage

On Roihu, BUSCO is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load busco
```

The basic syntax is:

```bash
busco -i input.fasta -l lineage_dataset -m genome -o output_name -c 8
```

`-m` selects the assessment mode (`genome`, `transcriptome` or `proteins`), and `-l`
selects the lineage dataset to compare against.

Heavier jobs should be run as batch jobs. BUSCO scales with the number of threads given
to `-c`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=busco
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load busco

srun busco -i genome.fasta -l bacteria_odb10 -m genome -o busco_output \
    -c $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch busco_job.sh`.

## More information

* [BUSCO home page](https://busco.ezlab.org/)
* [BUSCO user guide](https://busco.ezlab.org/busco_userguide.html)
* [CSC Service Desk](../support/contact.md)
