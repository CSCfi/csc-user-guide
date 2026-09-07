---
tags:
  - Free
catalog:
  name: MICOM
  description: Metabolic modelling of microbial communities
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MICOM

MICOM is a Python package for the metabolic modelling of microbial communities. It
builds and simulates community-scale metabolic models from taxon abundances and
genome-scale reconstructions.

[TOC]

## License

Free to use and open source under the [Apache 2.0 license](https://github.com/micom-dev/micom/blob/main/LICENSE).

## Available

* Roihu: 0.39.0 (module `py-micom`), via the `bio-apps` module.

## Usage

MICOM is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the module:

```bash
module load bio-apps/v202603
module load py-micom/0.39.0
```

MICOM is used as a Python library. Write your analysis in a Python script and run it,
for example within a batch job:

```bash
#!/bin/bash
#SBATCH --job-name=micom
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load py-micom/0.39.0

python my_micom_analysis.py
```

Replace `<project>` with your CSC project (for example `project_2001234`). MICOM can use
multiple threads; set the number of workers in your script to match `--cpus-per-task`.

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MICOM documentation](https://micom-dev.github.io/micom/)
* [MICOM GitHub repository](https://github.com/micom-dev/micom)
