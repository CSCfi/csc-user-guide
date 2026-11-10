---
tags:
  - Free
catalog:
  name: PhyloNet
  description: Inference and analysis of phylogenetic networks
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PhyloNet

PhyloNet analyses, reconstructs and evaluates reticulate (non-treelike) evolutionary
relationships, such as those caused by hybridisation, as phylogenetic networks. It also
infers species trees in the presence of incomplete lineage sorting.

[TOC]

## License

Free to download and use from the [PhyloNet website](https://phylogenomics.rice.edu/html/phylonet.html).
The distribution does not state a specific license.

## Available

* Roihu-CPU: 3.8.5, via the `bio-apps` module.

## Usage

PhyloNet is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the PhyloNet module:

```bash
module load bio-apps/v202603
module load phylonet/3.8.5
```

PhyloNet reads a NEXUS file that contains the input data, for example gene trees,
and a `PHYLONET` block with the commands to run. For example, `network.nex` below infers
a phylogenetic network with at most one reticulation from three gene trees, using
8 threads:

```text
#NEXUS

BEGIN TREES;
Tree gt1 = ((A,B),(C,D));
Tree gt2 = ((A,C),(B,D));
Tree gt3 = ((A,B),(C,D));
END;

BEGIN PHYLONET;
InferNetwork_MPL (gt1,gt2,gt3) 1 -pl 8;
END;
```

Run it with:

```bash
phylonet network.nex
```

Commands that can run in parallel, such as `InferNetwork_MPL`, take the number of
threads with `-pl`. Set it to match the cores reserved for your job. See the
[PhyloNet documentation](https://phylogenomics.rice.edu/html/phylonet.html) for the
commands and their options.

PhyloNet is a Java program, and Java may limit it to a fraction of the memory reserved
for your job. Set the maximum memory with the `JAVA_OPTS` environment variable, as in
the batch script below.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=phylonet
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G

module load bio-apps/v202603
module load phylonet/3.8.5

export JAVA_OPTS="-Xmx14g"
phylonet network.nex
```

`-Xmx14g` leaves some of the 16 GiB reserved for the job free for Java's own
overhead. Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [PhyloNet website](https://phylogenomics.rice.edu/html/phylonet.html)
* [Wen, D., Yu, Y., Zhu, J. & Nakhleh, L. (2018). Inferring phylogenetic networks using PhyloNet. Systematic Biology 67, 735–740](https://doi.org/10.1093/sysbio/syy015)
