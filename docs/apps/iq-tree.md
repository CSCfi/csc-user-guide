---
tags:
  - Free
catalog:
  name: IQ-TREE
  description: Maximum-likelihood phylogenetic inference
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# IQ-TREE

IQ-TREE is efficient software for phylogenomic inference by maximum likelihood. It
includes model selection (ModelFinder), ultrafast bootstrap approximation and a wide
range of substitution models.

[TOC]

## License

Free to use and open source under [GNU GPLv2](https://github.com/iqtree/iqtree2/blob/master/LICENSE).

## Available

* Roihu: 2.4.0, via the `bio-apps` module.

## Usage

IQ-TREE is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the IQ-TREE module:

```bash
module load bio-apps/v202603
module load iq-tree/2.4.0
```

IQ-TREE (version 2) is run with the `iqtree2` command. For example, a tree search with
model selection and ultrafast bootstrap:

```bash
iqtree2 -s alignment.phy -m MFP -B 1000 -T AUTO
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=iqtree
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
module load iq-tree/2.4.0

iqtree2 -s alignment.phy -m MFP -B 1000 -T $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [IQ-TREE home page](http://www.iqtree.org/)
* [IQ-TREE documentation](http://www.iqtree.org/doc/)
