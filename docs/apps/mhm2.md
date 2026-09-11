---
tags:
  - Free
catalog:
  name: MetaHipMer2
  description: GPU-accelerated metagenome assembly
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MetaHipMer2 (MHM2)

MetaHipMer2 is a *de novo* metagenome short-read assembler written in UPC++ and
CUDA. It runs efficiently on single servers and on multinode supercomputers,
where it can scale up to coassemble terabase-sized metagenomes. On Roihu it is
provided as a GPU-accelerated build for the GH200 GPU nodes.

[TOC]

## License

MetaHipMer2 is free and open source under a
[Berkeley Lab modified BSD 3-Clause license](https://bitbucket.org/berkeleylab/mhm2/src/master/LICENSE.txt).

## Available

* Roihu-GPU: 2.2.2.0-20260904, via the `bio-apps` module (GPU nodes only).

MHM2 runs on the Roihu GPU (GH200) nodes. Log in to `roihu-gpu.csc.fi` and load
the modules there so you get the GPU build.

## Usage

MHM2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MHM2 module:

```bash
module load bio-apps/v202603
module load mhm2/2.2.2.0-20260904
```

Assemblies are launched with the `mhm2.py` driver, which starts the parallel
(UPC++) processes for you — do **not** prefix it with `srun`. A basic run on
paired-end reads:

```bash
mhm2.py -r reads_1.fastq reads_2.fastq -o assembly_result
```

The assembled contigs are written to `assembly_result/final_assembly.fasta`. For
the full list of options use:

```bash
mhm2.py -h
```

Assembling metagenomic data is resource demanding, so run MHM2 as a batch job on
a GPU node.

!!! warning "MHM2 requires a GPU node"
    MHM2 is a GPU build and links directly against the CUDA driver library, so it
    runs only on Roihu GPU nodes. On a login node it fails at startup with
    `error while loading shared libraries: libcuda.so.1` because login nodes have
    no GPUs.

### Example batch script

MHM2 is process-parallel (UPC++): `mhm2.py` launches one process per Slurm task
and derives that count from `--ntasks-per-node`. Reserve **one task per CPU core**
you want to use, with `--cpus-per-task=1`. The example below uses one GPU with 16
processes — a reasonable starting point that you can raise (up to 72 cores per
GH200) for larger assemblies:

```bash
#!/bin/bash
#SBATCH --job-name=mhm2
#SBATCH --account=<project>
#SBATCH --output=mhm2_out_%j.txt
#SBATCH --error=mhm2_err_%j.txt
#SBATCH --partition=gpumedium
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=72 --cpus-per-task=1
#SBATCH --gres=gpu:gh200:1

module load bio-apps/v202603
module load mhm2/2.2.2.0-20260904

mhm2.py -r reads_1.fastq reads_2.fastq -o assembly_result
```

Replace `<project>` with your CSC project (for example `project_2001234`). You
can use `csc-projects` to check your CSC projects. Submit the job with `sbatch`:

```bash
sbatch mhm2_job.sh
```

If you reserve only one task (the default), MHM2 runs on a single core and warns
`Detected slurm job restricts cores to 1 because of SLURM_TASKS_PER_NODE=1` — set
`--ntasks-per-node` as shown to avoid this. To use a full GPU node, request all
four GPUs and 288 tasks (`--ntasks-per-node=288 --gres=gpu:gh200:4`); MHM2 shares
the node's GPUs among its processes. Because it communicates over InfiniBand it
can also coassemble across several nodes — increase `--nodes` accordingly.

!!! tip "Match the number of processes to the data size"
    MHM2's parallel start-up, communication and GPU-sharing overheads dominate on
    small inputs, so many processes can be **slower** than a few. For small or
    test datasets, request only a handful of cores (for example
    `--ntasks-per-node=4 --cpus-per-task=1` on the short-lived `gputest`
    partition). Use the full 72 cores per GPU, or a whole node, only for large
    metagenomes.

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md)
for more about batch jobs, and the
[GPU partitions](../computing/running/batch-job-partitions.md) for the available
GPU resources.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MetaHipMer2 repository](https://bitbucket.org/berkeleylab/mhm2)
