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

* Roihu-CPU: IQ-TREE 2 as `iq-tree/2.4.0` and IQ-TREE 3 as `iqtree3/3.1.4`, via the
  `bio-apps` module. The two are separate modules with distinct commands
  (`iqtree2` and `iqtree3`) and can be used side by side.

## Usage

IQ-TREE is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the IQ-TREE module you want.

IQ-TREE 2 is run with the `iqtree2` command:

```bash
module load bio-apps/v202603
module load iq-tree/2.4.0

iqtree2 -s alignment.phy -m MFP -B 1000 -T AUTO
```

IQ-TREE 3 is provided as a separate module and run with the `iqtree3` command;
the options are the same:

```bash
module load bio-apps/v202603
module load iqtree3/3.1.4

iqtree3 -s alignment.phy -m MFP -B 1000 -T AUTO
```

The examples above perform a tree search with model selection (ModelFinder) and
ultrafast bootstrap.

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
