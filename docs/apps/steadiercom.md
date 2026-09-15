---
tags:
  - Free
catalog:
  name: SteadierCom
  description: Steady-state metabolic simulation of microbial communities
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# SteadierCom

SteadierCom is a tool for microbial community simulation using genome-scale metabolic
models. It predicts steady-state growth and cross-feeding interactions within microbial
communities and provides the `steadiercom` command-line tool.

[TOC]

## License

Free to use and open source under the [Apache 2.0 license](https://github.com/cdanielmachado/SteadierCom/blob/master/LICENSE).

## Available

* Roihu: 0.1.5 (module `py-steadiercom`), via the `bio-apps` module.

## Usage

SteadierCom is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the module:

```bash
module load bio-apps/v202603
module load py-steadiercom/0.1.5
```

Run the analysis with the `steadiercom` command, giving the community's genome-scale
models:

```bash
steadiercom models/*.xml --output community_results
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=steadiercom
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load py-steadiercom/0.1.5

steadiercom models/*.xml --output community_results
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [SteadierCom GitHub repository](https://github.com/cdanielmachado/SteadierCom)
