---
tags:
  - Free
catalog:
  name: HyPhy
  description: Hypothesis testing on phylogenies (selection analysis)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# HyPhy

HyPhy (Hypothesis testing using Phylogenies) is a software package for the analysis of
genetic sequences using techniques in phylogenetics, molecular evolution and machine
learning. It is widely used for detecting signatures of natural selection (methods such
as FEL, MEME, aBSREL and BUSTED).

[TOC]

## License

Free to use and open source. See the [HyPhy repository](https://github.com/veg/hyphy/blob/master/LICENSE).

## Available

* Roihu: 2.5.51hf, via the `bio-apps` module.

## Usage

HyPhy is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the HyPhy module:

```bash
module load bio-apps/v202603
module load hyphy/2.5.51hf
```

HyPhy analyses are run with the `hyphy` command, giving the method name and the input
alignment and tree. For example, a FEL selection analysis:

```bash
hyphy fel --alignment alignment.fasta --tree tree.nwk
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=hyphy
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load hyphy/2.5.51hf

hyphy CPU=$SLURM_CPUS_PER_TASK fel --alignment alignment.fasta --tree tree.nwk
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [HyPhy home page](https://www.hyphy.org/)
* [HyPhy GitHub repository](https://github.com/veg/hyphy)
