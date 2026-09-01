---
tags:
  - Free
catalog:
  name: Dorado
  description: GPU-accelerated Oxford Nanopore basecaller
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Dorado

Dorado is a high-performance, easy-to-use, open source basecaller for Oxford Nanopore
reads. On Roihu it is provided as a GPU-accelerated build for the GH200 GPU nodes.

[TOC]

## License

Free to use and open source. See the [dorado repository](https://github.com/nanoporetech/dorado) for license terms.

## Available

* Roihu-GPU: 2.1.1, via the `bio-apps` module (GPU nodes only).

Dorado runs on the Roihu GPU (GH200) nodes. Log in to `roihu-gpu.csc.fi` and load the
modules there so you get the GPU build.

## Usage

Dorado is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Dorado module:

```bash
module load bio-apps/v202603
module load dorado/2.1.1
```

Dorado uses basecalling models that are downloaded on first use. Download them to a
writable location (for example your project's `/scratch`), or let `dorado basecaller`
fetch the model automatically when run from a writable working directory:

```bash
dorado download --model dna_r10.4.1_e8.2_400bps_sup@v5.0.0
```

### Example batch script

Dorado must run on a GPU node. Below is a sample GPU batch job:

```bash
#!/bin/bash
#SBATCH --job-name=dorado
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
module load dorado/2.1.1

dorado basecaller sup pod5_dir/ > calls.bam
```

Replace `<project>` with your CSC project (for example `project_2001234`). The `sup`
argument selects the super-accuracy model; dorado downloads it if it is not already
present.

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs, and the [GPU partitions](../computing/running/batch-job-partitions.md#roihu-gpu-partitions) for available GPU resources.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Dorado GitHub repository](https://github.com/nanoporetech/dorado)
