---
tags:
  - Free
catalog:
  name: RAxML-NG
  description: Maximum-likelihood phylogenetic tree inference
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# RAxML-NG

RAxML-NG infers maximum-likelihood phylogenetic trees from a multiple sequence
alignment, searching tree space with Subtree Pruning and Regrafting moves. It is the
successor of the original RAxML and reuses the optimized likelihood code from libpll.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail raxml-ng` after loading `bio-apps`.

## License

Free to use and open source under
[AGPL-3.0 License](https://github.com/amkozlov/raxml-ng/blob/master/LICENSE.txt).

## Usage

On Roihu, RAxML-NG is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load raxml-ng
```

The basic syntax is:

```bash
raxml-ng --all --msa alignment.fasta --model GTR+G --prefix run1
```

A full tree search with bootstrapping is CPU-intensive and benefits from multiple
threads. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=raxml-ng
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load raxml-ng

srun raxml-ng --all --msa alignment.fasta --model GTR+G \
    --threads $SLURM_CPUS_PER_TASK --prefix run1
```

Submit the job with `sbatch raxml-ng_job.sh`. Running `raxml-ng --parse` first gives a
memory estimate and a suggested thread count for the input alignment.

## More information

* [RAxML-NG home page and wiki](https://github.com/amkozlov/raxml-ng/wiki)
* [CSC Service Desk](../support/contact.md)
