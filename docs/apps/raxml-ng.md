---
tags:
  - Free
catalog:
  name: RAxML-NG
  description: Maximum-likelihood phylogenetic inference (RAxML-NG)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# RAxML-NG

RAxML-NG is a phylogenetic tree inference tool which uses maximum-likelihood
optimization. It is a from-scratch, faster and more user-friendly successor to
[RAxML](raxml.md).

[TOC]

## License

Free to use and open source under [GNU AGPLv3](https://github.com/amkozlov/raxml-ng/blob/master/LICENSE.txt).

## Available

* Roihu: 2.0.2, via the `bio-apps` module.

## Usage

RAxML-NG is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the RAxML-NG module:

```bash
module load bio-apps/v202603
module load raxml-ng/2.0.2
```

A typical maximum-likelihood tree search with bootstrap support:

```bash
raxml-ng --all --msa alignment.fasta --model GTR+G --bs-trees 100 --threads 8
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=raxml-ng
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
module load raxml-ng/2.0.2

raxml-ng --all --msa alignment.fasta --model GTR+G --bs-trees 100 --threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [RAxML-NG GitHub repository](https://github.com/amkozlov/raxml-ng)
* [RAxML-NG wiki](https://github.com/amkozlov/raxml-ng/wiki)
