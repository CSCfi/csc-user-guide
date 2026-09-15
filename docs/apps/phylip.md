---
tags:
  - Free
catalog:
  name: PHYLIP
  description: PHYLIP phylogeny inference package
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PHYLIP

PHYLIP (the PHYLogeny Inference Package) is a package of programs for inferring
phylogenies (evolutionary trees). It includes methods such as parsimony, distance
matrix and maximum likelihood, and tools for consensus trees, bootstrapping and tree
drawing.

[TOC]

## License

Free to use. See the [PHYLIP home page](https://phylipweb.github.io/phylip/) for license terms.

## Available

* Roihu: 3.697, via the `bio-apps` module.

## Usage

PHYLIP is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the PHYLIP module:

```bash
module load bio-apps/v202603
module load phylip/3.697
```

PHYLIP consists of many individual programs (for example `dnaml`, `dnapars`,
`neighbor`, `consense`). Each program reads a file named `infile` from the working
directory (or prompts for the input file name) and is run by its name:

```bash
dnaml
```

The programs are interactive by default. For batch use, provide the responses via a
response file, for example:

```bash
dnaml < responses.txt
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=phylip
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

module load bio-apps/v202603
module load phylip/3.697

dnaml < responses.txt
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [PHYLIP home page](https://phylipweb.github.io/phylip/)
