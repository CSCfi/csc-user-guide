---
tags:
  - Free
catalog:
  name: deepTools
  description: Tools for exploring and visualizing deep-sequencing data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# deepTools

deepTools is a suite of command-line tools for processing and visualising
deep-sequencing data such as ChIP-seq, RNA-seq and MNase-seq. It covers tasks from
quality control to generating normalised coverage tracks and publication-ready plots.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed versions with `module avail py-deeptools` after loading `bio-apps`.

## License

Free to use and open source under
[MIT License](https://github.com/deeptools/deepTools/blob/master/LICENSE.txt).

## Usage

On Roihu, deepTools is part of the `bio-apps` collection, which has to be loaded
first:

```bash
module load bio-apps
module load py-deeptools
```

deepTools installs a set of separate commands rather than one unified tool. Some of
the most used ones:

| Command           | Function                                                   |
|-------------------|-------------------------------------------------------------|
| `bamCoverage`     | Convert a BAM file into a normalised coverage track        |
| `bamCompare`      | Compare two BAM files and output a ratio/difference track  |
| `computeMatrix`   | Prepare data for `plotHeatmap` or `plotProfile`             |
| `plotHeatmap`     | Draw a heatmap from a `computeMatrix` output                |
| `plotCorrelation` | Correlate read coverages between samples                    |
| `multiBamSummary` | Summarise read counts across multiple BAM files              |

For example, to build a coverage track from a BAM file:

```bash
bamCoverage --bam input.bam --outFileName coverage.bw
```

Heavier jobs should be run as batch jobs. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=deeptools
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load py-deeptools

srun bamCoverage --bam input.bam --outFileName coverage.bw \
    --numberOfProcessors $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch deeptools_job.sh`.

## More information

* [deepTools home page](https://pypi.python.org/pypi/deepTools/)
* [deepTools documentation](https://deeptools.readthedocs.io/)
* [CSC Service Desk](../support/contact.md)
