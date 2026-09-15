---
tags:
  - Free
catalog:
  name: CLUMPP
  description: Alignment of replicate cluster assignments from population-structure analyses
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# CLUMPP

CLUMPP (CLUster Matching and Permutation Program) deals with label switching and
multimodality in the output of population-structure clustering programs such as
[Structure](structure.md). It permutes the cluster labels of replicate runs so that
they match up as closely as possible.

[TOC]

## License

CLUMPP is freely downloadable and free to use; no specific open-source license is
specified. See the [CLUMPP home page](https://rosenberglab.stanford.edu/clumpp.html)
for terms.

## Available

* Roihu: 1.1.2, via the `bio-apps` module.

## Usage

CLUMPP is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the CLUMPP module:

```bash
module load bio-apps/v202603
module load clumpp/1.1.2
```

CLUMPP is driven by a parameter file (`paramfile`) that specifies the input, output
and options. Run it with:

```bash
CLUMPP paramfile
```

CLUMPP is often used as part of an automated [Structure](structure.md) workflow — see
[StrAuto](strauto.md), which runs CLUMPP as part of its post-processing.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=clumpp
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

module load bio-apps/v202603
module load clumpp/1.1.2

CLUMPP paramfile
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [CLUMPP home page](https://rosenberglab.stanford.edu/clumpp.html)
