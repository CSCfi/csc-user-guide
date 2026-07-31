---
tags:
  - Free
catalog:
  name: IQ-TREE
  description: Software for maximum-likelihood phylogenomic inference
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# IQ-TREE

IQ-TREE is a maximum-likelihood phylogenetics program for inferring evolutionary
trees from sequence alignments, with automatic model selection and ultrafast
bootstrap support.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail iq-tree` after loading `bio-apps`.

## License

Free to use and open source under
[GNU General Public License v2.0](https://github.com/iqtree/iqtree2/blob/master/LICENSE).

## Usage

On Roihu, IQ-TREE is part of the `bio-apps` collection, which has to be loaded first.
Note that the executable is `iqtree2`, not `iqtree`:

```bash
module load bio-apps
module load iq-tree
```

The basic syntax is:

```bash
iqtree2 -s alignment.fasta -m MFP -B 1000 -T AUTO
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=iqtree2
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load iq-tree

srun iqtree2 -s alignment.fasta -m MFP -B 1000 -T $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch iqtree2_job.sh`.

## More information

* [IQ-TREE home page](https://iqtree.github.io)
* [IQ-TREE documentation](https://iqtree.github.io/doc/)
* [CSC Service Desk](../support/contact.md)
