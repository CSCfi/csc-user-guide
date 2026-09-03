---
tags:
  - Free
catalog:
  name: medaka
  description: Nanopore consensus and variant calling
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# medaka

medaka is a tool to create consensus sequences and variant calls from Oxford Nanopore
sequencing data. It uses neural networks applied to a pileup of individual sequencing
reads against a draft assembly. On Roihu it is provided as a GPU-accelerated build for
the GH200 GPU nodes.

[TOC]

## License

Medaka is distributed under the [Oxford Nanopore Technologies PLC Public License v1.0](https://github.com/nanoporetech/medaka/blob/master/LICENSE).
The license permits use solely for research purposes, defined as internal research not intended for or directed towards commercial advantage or monetary compensation.
Sponsored or grant-funded research is permitted under the license.

## Available

* Roihu-GPU: 2.2.2 (module `py-medaka`), via the `bio-apps` module (GPU nodes only).

medaka runs on the Roihu GPU (GH200) nodes. Log in to `roihu-gpu.csc.fi` and load the
modules there so you get the GPU build.

## Usage

medaka is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the medaka module:

```bash
module load bio-apps/v202603
module load py-medaka/2.2.2
```

The main entry point for polishing a draft assembly is `medaka_consensus`. medaka
downloads the required model on first use; run it from a writable working directory (for
example in your project's `/scratch`).

### Example batch script

medaka's neural-network inference runs on a GPU, so submit it to a GPU node:

```bash
#!/bin/bash
#SBATCH --job-name=medaka
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=gpumedium
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:gh200:1

module load bio-apps/v202603
module load py-medaka/2.2.2

medaka_consensus -i reads.fq.gz -d draft_assembly.fasta -o medaka_out -t $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs, and the [GPU partitions](../computing/running/batch-job-partitions.md#roihu-gpu-partitions) for available GPU resources.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [medaka GitHub repository](https://github.com/nanoporetech/medaka)
