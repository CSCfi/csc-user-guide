---
tags:
  - Free
catalog:
  name: Foldseek
  description: Fast protein structure search and clustering
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Foldseek

Foldseek enables fast and sensitive comparisons of large sets of protein structures.
It describes structures with a structural alphabet (3Di) and searches and clusters
them with MMseqs2-based algorithms. On Roihu it is provided as a GPU-accelerated
build for the GH200 GPU nodes.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/steineggerlab/foldseek/blob/master/LICENSE.md).

## Available

* Roihu-GPU: 10-941cd33, via the `bio-apps` module.

Foldseek runs on the Roihu GPU (GH200) nodes. Log in to `roihu-gpu.csc.fi` and load the
modules there so you get the GPU build.

## Usage

Foldseek is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Foldseek module:

```bash
module load bio-apps/v202603
module load foldseek/10-941cd33
```

Search a set of query structures (PDB or mmCIF files) against a set of target
structures:

```bash
foldseek easy-search queries/ targets/ results.m8 tmp
```

Cluster a set of structures:

```bash
foldseek easy-cluster structures/ clusters tmp -c 0.9
```

### Databases

`foldseek databases` downloads prebuilt databases, for example the PDB or the
AlphaFold/Swiss-Prot structures. Run it without arguments to list all available
databases. Download large databases to your project's `/scratch`:

```bash
foldseek databases PDB pdb tmp
foldseek databases Alphafold/Swiss-Prot afdb tmp
```

### GPU-accelerated search

Add `--gpu 1` to run a search on the GPU. A GPU search needs a padded target
database, which you make from a regular Foldseek database with `makepaddedseqdb`:

```bash
foldseek makepaddedseqdb afdb afdb_pad
foldseek easy-search queries/ afdb_pad results.m8 tmp --gpu 1 --prefilter-mode 1
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=foldseek
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=gpumedium
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=72
#SBATCH --gres=gpu:gh200:1

module load bio-apps/v202603
module load foldseek/10-941cd33

foldseek easy-search queries/ afdb_pad results.m8 tmp --gpu 1 --prefilter-mode 1 \
  --threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`). See
[creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md)
for more about batch jobs, and the
[GPU partitions](../computing/running/batch-job-partitions.md) for the available GPU
resources.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Foldseek GitHub repository](https://github.com/steineggerlab/foldseek)
* [Foldseek web server](https://search.foldseek.com)
