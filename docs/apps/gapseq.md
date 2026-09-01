---
tags:
  - Free
catalog:
  name: gapseq
  description: Genome-scale metabolic network reconstruction and analysis
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# gapseq

gapseq performs informed prediction and analysis of bacterial metabolic pathways and
produces gap-filled genome-scale metabolic models from genome sequences.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/jotech/gapseq/blob/master/LICENSE).

## Available

* Roihu: 2.1.0, via the `bio-apps` module.

## Usage

gapseq is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the gapseq module:

```bash
module load bio-apps/v202603
module load gapseq/2.1.0
```

The full pipeline (pathway prediction, network building and gap-filling) can be run on
a genome with the `doall` subcommand:

```bash
gapseq doall genome.fna.gz
```

Individual steps (`find`, `find-transport`, `draft`, `fill`) can also be run
separately. gapseq analyses can be computationally heavy and should be run as batch
jobs:

```bash
#!/bin/bash
#SBATCH --job-name=gapseq
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load gapseq/2.1.0

gapseq doall genome.fna.gz
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [gapseq documentation](https://gapseq.readthedocs.io/)
* [gapseq GitHub repository](https://github.com/jotech/gapseq)
