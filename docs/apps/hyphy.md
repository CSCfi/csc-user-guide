---
tags:
  - Free
catalog:
  name: HyPhy
  description: Toolkit for phylogenetic hypothesis testing
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HyPhy

HyPhy (Hypothesis testing using Phylogenies) is a toolkit for testing evolutionary
hypotheses on molecular sequence alignments, such as detecting selection pressure
along a phylogeny.

[TOC]

## Available

* Roihu-CPU: 2.5.51hf
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check the
installed versions with `module avail hyphy` after loading `bio-apps`.

## License

Free to use and open source under
[MIT License](https://github.com/veg/hyphy/blob/master/LICENSE).

## Usage

On Roihu, HyPhy is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load hyphy
```

HyPhy analyses are run by naming a method after the executable, together with an
alignment and a tree:

```bash
hyphy meme --alignment data.fasta --tree tree.nwk
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=hyphy
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load hyphy

srun hyphy CPU=$SLURM_CPUS_PER_TASK meme --alignment data.fasta --tree tree.nwk
```

Submit the job with `sbatch hyphy_job.sh`.

## More information

* [HyPhy home page](https://www.hyphy.org/)
* [HyPhy source code](https://github.com/veg/hyphy)
* [CSC Service Desk](../support/contact.md)
