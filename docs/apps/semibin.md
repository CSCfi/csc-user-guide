---
tags:
  - Free
catalog:
  name: SemiBin2
  description: Metagenomic binning with deep learning
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SemiBin2

SemiBin2 bins metagenomic contigs into metagenome-assembled genomes (MAGs) with
deep learning, using the sequence composition and read coverage of the contigs.
It works with assemblies from both short and long reads, and includes pretrained
models for common environments such as the human gut, soil and ocean.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/BigDataBiology/SemiBin/blob/main/COPYING.MIT).

## Available

* Roihu-CPU: 2.6.0 (module `py-semibin`), via the `bio-apps` module.

## Usage

SemiBin2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the SemiBin2 module:

```bash
module load bio-apps/v202603
module load py-semibin/2.6.0
```

SemiBin2 needs the contigs and a sorted BAM file from mapping the reads to the
contigs. Bin a single sample with a pretrained model:

```bash
SemiBin2 single_easy_bin -i contigs.fa -b sample.sorted.bam -o semibin_out \
  --environment human_gut -t 16
```

The pretrained models are `human_gut`, `dog_gut`, `ocean`, `soil`, `cat_gut`,
`human_oral`, `mouse_gut`, `pig_gut`, `built_environment`, `wastewater`,
`chicken_caecum` and `global`. Leave out `--environment` to train a new model on
your own data instead, which takes longer. For contigs assembled from long reads,
add `--sequencing-type long_read`.

Always set the number of threads with `-t`. By default, SemiBin2 uses all the
cores of the node, not only the cores reserved for your job.

The bins are written to `semibin_out/output_bins` as gzipped FASTA files
(`SemiBin_<number>.fa.gz`), and the bin of each contig to
`semibin_out/contig_bins.tsv`.

To bin several samples together, combine their contigs with
`SemiBin2 concatenate_fasta`, map the reads of each sample to the combined contigs
and run `SemiBin2 multi_easy_bin`. See the
[SemiBin2 documentation](https://semibin.readthedocs.io/en/latest/usage/) for details.

To combine the bins of SemiBin2 with those of other binning tools, use
[MAGScoT](magscot.md).

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=semibin2
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G

module load bio-apps/v202603
module load py-semibin/2.6.0

SemiBin2 single_easy_bin -i contigs.fa -b sample.sorted.bam -o semibin_out \
  --environment human_gut -t $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [SemiBin2 documentation](https://semibin.readthedocs.io/)
* [SemiBin GitHub repository](https://github.com/BigDataBiology/SemiBin)
