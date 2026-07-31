---
tags:
  - Free
catalog:
  name: MUMmer4
  description: Versatile alignment tool for DNA and protein sequences
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MUMmer4

MUMmer4 aligns whole genomes and large sequence sets, using suffix- and FM-index-based
matching to find maximal unique matches before extending them into full alignments. It
is commonly used to compare assemblies, find structural variants or align related
genomes.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail mummer4` after loading `bio-apps`.

## License

Free to use and open source under
[Artistic License 2.0](https://github.com/mummer4/mummer/blob/master/LICENSE.md).

## Usage

On Roihu, MUMmer4 is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load mummer4
```

The basic syntax for aligning two genomes with `nucmer` is:

```bash
nucmer --prefix=out reference.fasta query.fasta
show-coords -rcl out.delta > out.coords
```

`show-coords` turns the binary `.delta` alignment into a readable coordinate table.
Use `promer` instead of `nucmer` for more divergent sequences aligned in amino acid
space.

Heavier jobs should be run as batch jobs. `nucmer` scales with the number of threads
given to `--threads`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=mummer4
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load mummer4

srun nucmer --threads=$SLURM_CPUS_PER_TASK --prefix=out reference.fasta query.fasta
srun show-coords -rcl out.delta > out.coords
```

Submit the job with `sbatch mummer4_job.sh`.

## More information

* [MUMmer4 home page](https://github.com/mummer4/mummer)
* [MUMmer4 manual](https://mummer4.github.io/manual/manual.html)
* [CSC Service Desk](../support/contact.md)
