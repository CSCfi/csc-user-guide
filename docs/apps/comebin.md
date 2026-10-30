---
tags:
  - Free
catalog:
  name: COMEBin
  description: Metagenomic binning with contrastive multi-view representation learning
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# COMEBin

COMEBin bins metagenomic contigs into metagenome-assembled genomes (MAGs). It
learns a representation of each contig from its sequence composition and read
coverage with contrastive multi-view learning, and clusters the contigs with the
Leiden algorithm.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/ziyewang/COMEBin/blob/master/LICENSE.txt).

## Available

* Roihu-CPU: 1.1.0, via the `bio-apps` module.
* Roihu-GPU: 1.1.0 (GPU-accelerated training), via the `bio-apps` module.

## Usage

COMEBin is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the COMEBin module:

```bash
module load bio-apps/v202603
module load comebin/1.1.0
```

COMEBin needs the contigs as an uncompressed FASTA file, and a directory of
sorted BAM files from mapping the reads of each sample to the contigs. The
`gen_cov_file.sh` script included with COMEBin maps paired-end reads with BWA and
writes the BAM files to the directory given with `-b`:

```bash
gen_cov_file.sh -a contigs.fa -o cov -b bams -t 16 \
  -f _1.fastq.gz -r _2.fastq.gz reads/*.fastq.gz
```

`-f` and `-r` give the endings of the forward and reverse read files (the defaults
are `_1.fastq` and `_2.fastq`). Give all options before the read files.

`run_comebin.sh` then runs the three steps of COMEBin: data augmentation, which
computes the contig features from the contigs and BAM files, training of the
model, and clustering. Only the training step can use a GPU. Run the mapping and
all the COMEBin steps in batch jobs, not on the login node. See the
[example batch script](#example-batch-script) below.

### Running on Roihu-CPU

Run all three steps on Roihu-CPU with `-d cpu`, which trains the model on the
CPU. The default, `cuda`, fails on CPU nodes:

```bash
run_comebin.sh -a contigs.fa -p bams -o comebin_out -d cpu -t $SLURM_CPUS_PER_TASK
```

The bins are written to `comebin_out/comebin_res/comebin_res_bins`, and the bin
of each contig to `comebin_out/comebin_res/comebin_res.tsv`. If a run stops, run
the same command again: COMEBin skips the data augmentation and training steps
that have already finished.

To combine the bins of COMEBin with those of other binning tools, use
[MAGScoT](magscot.md).

### Training on a GPU

Training is faster on a GH200 GPU, but the other steps only use CPUs. Run only
the training as a GPU batch job, and the other steps as batch jobs on Roihu-CPU.
You submit the GPU job from the Roihu-GPU login node (`roihu-gpu.csc.fi`), but
note that the login node itself has no GPUs.

1. On Roihu-CPU, make the BAM files and run the data augmentation step in a batch
   job (see the [example batch script](#example-batch-script)):

    ```bash
    python $COMEBIN_INSTROOT/bin/COMEBin/main.py generate_aug_data --contig_file contigs.fa \
      --bam_file_path bams --out_augdata_path comebin_out/data_augmentation --num_threads $SLURM_CPUS_PER_TASK
    ```

2. Log in to `roihu-gpu.csc.fi`, go to the same directory as in step 1, and submit the
   [example GPU batch script](#example-gpu-batch-script), which trains the model.

3. On Roihu-CPU, run `run_comebin.sh` in a batch job with the same options as in
   [Running on Roihu-CPU](#running-on-roihu-cpu). It finds the finished data
   augmentation and training, and runs only the clustering.

### Example batch script

This runs all three steps on Roihu-CPU. For GPU training, replace the
`run_comebin.sh` line with the `generate_aug_data` command from step 1 above.

```bash
#!/bin/bash
#SBATCH --job-name=comebin
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G

module load bio-apps/v202603
module load comebin/1.1.0

gen_cov_file.sh -a contigs.fa -o cov -b bams -t $SLURM_CPUS_PER_TASK \
  -f _1.fastq.gz -r _2.fastq.gz reads/*.fastq.gz
run_comebin.sh -a contigs.fa -p bams -o comebin_out -d cpu -t $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

### Example GPU batch script

This runs only the training step, on the data augmentation results from Roihu-CPU.
Submit it from `roihu-gpu.csc.fi`:

```bash
#!/bin/bash
#SBATCH --job-name=comebin-train
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
module load comebin/1.1.0

python $COMEBIN_INSTROOT/bin/COMEBin/main.py train --data comebin_out/data_augmentation \
  --output_path comebin_out/comebin_res --earlystop --addvars --vars_sqrt \
  --num_threads $SLURM_CPUS_PER_TASK
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs, and the [GPU partitions](../computing/running/batch-job-partitions.md#roihu-gpu-partitions) for the available GPU resources.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [COMEBin GitHub repository](https://github.com/ziyewang/COMEBin)
