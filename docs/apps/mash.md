---
tags:
  - Free
catalog:
  name: Mash
  description: Fast genome and metagenome distance estimation using MinHash
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Mash

Mash reduces genomes and metagenomes to small MinHash sketches, then estimates distances
between those sketches instead of aligning full sequences. This makes tasks such as
finding the closest reference genome or clustering many assemblies dramatically faster
than alignment-based approaches.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail mash` after loading `bio-apps`.

## License

Free to use and open source under
[BSD 3-Clause License](https://github.com/marbl/Mash/blob/master/LICENSE.txt).

## Usage

On Roihu, Mash is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load mash
```

The basic workflow is to sketch the inputs, then compare the sketches:

```bash
mash sketch -o reference genomes/*.fasta
mash dist reference.msh query.fasta > distances.tab
```

`mash triangle` produces an all-against-all distance matrix from a single sketch file.

Heavier jobs should be run as batch jobs. Mash scales with the number of threads given
to `-p`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=mash
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load mash

srun mash sketch -p $SLURM_CPUS_PER_TASK -o reference genomes/*.fasta
srun mash dist -p $SLURM_CPUS_PER_TASK reference.msh query.fasta > distances.tab
```

Submit the job with `sbatch mash_job.sh`.

## More information

* [Mash home page](https://mash.readthedocs.org/)
* [Mash GitHub repository](https://github.com/marbl/Mash)
* [CSC Service Desk](../support/contact.md)
