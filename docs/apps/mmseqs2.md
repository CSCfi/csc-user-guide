---
tags:
  - Free
catalog:
  name: MMseqs2
  description: Very fast protein search and clustering
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MMseqs2

MMseqs2 (Many-against-Many sequence searching) is a software suite for very fast and
sensitive searching and clustering of large protein and nucleotide sequence sets.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/soedinglab/MMseqs2/blob/master/LICENSE.md).

## Available

* Roihu-CPU: 18-8cc5c, via the `bio-apps` module.
* Roihu-GPU: 18-8cc5c (GPU-accelerated), via the `bio-apps` module.

On GPU nodes, the MMseqs2 build is compiled with CUDA support and can use the GH200 GPUs
to accelerate searches.

## Usage

MMseqs2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MMseqs2 module:

```bash
module load bio-apps/v202603
module load mmseqs2/18-8cc5c
```

A typical search converts the query and target FASTA files to MMseqs2 databases and
runs `mmseqs easy-search`:

```bash
mmseqs easy-search query.fasta target.fasta results.m8 tmp --threads 8
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=mmseqs2
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load mmseqs2/18-8cc5c

mmseqs easy-search query.fasta target.fasta results.m8 tmp --threads $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`). To use GPU
acceleration, run MMseqs2 in a GPU batch job on a GH200 node; see
[creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md).

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MMseqs2 GitHub repository](https://github.com/soedinglab/MMseqs2)
* [MMseqs2 user guide](https://github.com/soedinglab/mmseqs2/wiki)
