---
tags:
  - Free
catalog:
  name: Structure Harvester
  description: Post-processing of STRUCTURE results (Evanno method)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Structure Harvester

Structure Harvester parses the output of Pritchard's [Structure](structure.md) program,
applies the Evanno ΔK method to help detect the number of clusters, and can optionally
emit CLUMPP-compatible indfiles and popfiles.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/dentearl/structureHarvester/blob/master/LICENSE).

## Available

* Roihu: 0.7, via the `bio-apps` module.

## Usage

Structure Harvester is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the module:

```bash
module load bio-apps/v202603
module load structureharvester/0.7
```

Run `structureHarvester.py` on a directory of Structure result files:

```bash
structureHarvester.py --dir=structure_results --out=harvester_out --evanno --clumpp
```

Structure Harvester is often used as part of an automated Structure workflow — see
[StrAuto](strauto.md), which runs it as part of its post-processing.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=structureharvester
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
module load structureharvester/0.7

structureHarvester.py --dir=structure_results --out=harvester_out --evanno --clumpp
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Structure Harvester GitHub repository](https://github.com/dentearl/structureHarvester)
