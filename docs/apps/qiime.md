---
tags:
  - Free
---

# QIIME

QIIME (Quantitative Insights Into Microbial Ecology) is a package for comparison and analysis of microbial communities,
primarily based on high-throughput amplicon sequencing data (such as SSU rRNA) generated on a variety of platforms,
but also supporting analysis of other types of data (such as shotgun metagenomic data). QIIME takes users from their
raw sequencing output through initial analyses such as OTU picking, taxonomic assignment, and construction of
phylogenetic trees from representative sequences of OTUs, and through downstream statistical analysis, visualization,
and production of publication-quality graphics.

In 2017 a totally rewritten version QIIME2 was released. The development of the original QIIME version has stopped. QIIME2 is strongly suggested for most uses.

[TOC]

## License

Free to use and open source under [BSD 3-Clause License](https://github.com/qiime2/qiime2/blob/master/LICENSE).

## Available

- QIIME1: Puhti: 1.9.1
- QIIME2: Puhti: 2022.8, 2023.2, 2023.5, 2023.9-amplicon, 2023.9-shotgun, 2024.2-amplicon, 2024.2-shotgun

## Usage

To load QIIME1 module on Puhti:

```bash
module load qiime1
```

To use QIIME2, check available versions with:

```bash
module spider qiime2
```

Load desired version with e.g.:

```bash
module load qiime2/2023.9-amplicon
```

After that you can start QIIME2 with command:

```bash
qiime
```

## Distributions

Latest versions of QIIME2 come in different distributions: amplicon/shotgun/tiny.
These distributions vary on which plugins come with them. You can compare the
[distributions](https://docs.qiime2.org/2023.9/install/#distributions) on QIIME2
home pages.

CSC provides installations for the amplicon and shotgn distributions.

## Additional plugins

CSC only maintains the basic distributions of QIIME2. If you need plugins not included in the basic distributions, you will need to install your own QIIME2 using the [Tykky tool](../computing/containers/tykky.md).

First select the distribution (amplicon/shotgun/tiny) that best meets your needs.

Download the corresponding [environment file](https://docs.qiime2.org/2023.9/install/native/).

For example for 2023.9 amplicon distribution:

```bash
wget https://data.qiime2.org/distro/amplicon/qiime2-amplicon-2023.9-py38-linux-conda.yml
```

Check the installation instructions for the plugins you want to use.

If the additional plugins can be installed with Conda, you can simply add them to the end of the
environment file.

If the plugins need additional installation steps, you can copy them to text file and use
`conda-containerize update` command as described in the Tykky documentation.

Installation:

```bash
module purge
module load tykky
mkdir qiime
conda-containerize new --mamba --prefix qiime qiime2-amplicon-2023.9-py38-linux-conda.yml
```

If necessary, run:

```bash
conda-containerize update qiime --post-install plugins.txt
```

## Running

Note that many QIIME tasks involve heavy computing. Thus, these tasks should be executed as
batch jobs.

QIIME jobs can be very disk intensive, especially its handling of temporary files, so it is best to
reserve fast local disk for them.

For interactive batch jobs, see [sinteractive](../computing/running/interactive-usage.md) documentation.

In case of normal batch jobs, you must reserve NVMe disk area that will be used as $TMPDIR area.

For example, to reserve 100 GB of local disk space:

```text
#SBATCH --gres=nvme:100
```

For example, the batch job script below runs the denoising step of the
[QIIME moving pictures tutorial](https://docs.qiime2.org/2019.7/tutorials/moving-pictures/#option-1-dada2 )
as a batch job using eight cores.

```bash
#!/bin/bash
#SBATCH --job-name=qiime_denoise
#SBATCH --account=<project>
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --partition=small
#SBATCH --gres=nvme:100

#set up qiime
module load qiime2/2023.9-amplicon

# run task. Don't use srun in submission as it resets TMPDIR
qiime dada2 denoise-single \
  --i-demultiplexed-seqs demux.qza \
  --p-trim-left 0 \
  --p-trunc-len 120 \
  --o-representative-sequences rep-seqs-dada2.qza \
  --o-table table-dada2.qza \
  --o-denoising-stats stats-dada2.qza \
  --p-n-threads $SLURM_CPUS_PER_TASK
```

Maximum running time is set to 1 hour (`--time=01:00:00`). As QIIME2 uses thread-based
parallelization, the job is requested to use one task (`--ntasks=1`) where all cores need to be in
the same node (`--nodes=1`). This one task will use eight cores as parallel threads
`--cpus-per-task=8` that can use in total up to 16 GB of memory (`--mem=16G`). Note that the
number of cores to be used needs to be defined in actual `qiime` command, too. That is done with
Qiime option `--p-n-threads`. In this case we use `$SLURM_CPUS_PER_TASK` variable that contains the
`--cpus-pre-task` value. We could as well use `--p-n-threads 8`, but then we have to remember
to change the value if the number of reserved CPUs is changed.

The job is submitted to the batch job system with `sbatch` command. For example, if the batch job file is named `qiime_job.sh`, then the submission command is:

```bash
sbatch qiime_job.sh
```
More information about running batch jobs can be found from the [batch job section of the Puhti user guide](../computing/running/getting-started.md).

!!! warning "Note"
    The use of `tab-qiime` to enable command completion for QIIME is known to cause problems on Puhti, and should be avoided.

## More information

* [QIIME2 home page](https://qiime2.org/)
