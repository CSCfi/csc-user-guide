---
tags:
  - Free
catalog:
  name: Roary
  description: Pan genome pipeline
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Roary

Roary is a high-speed standalone pan genome pipeline, which takes annotated assemblies in 
GFF3 format (produced by e.g. [Prokka](./prokka.md)) and calculates the pan genome.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu-CPU: 3.13.0, via the `bio-apps` module.

## Usage

Roary is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Roary module:

```bash
module load bio-apps/v202603
module load roary/3.13.0
```

After that, you can launch Roary with the command `roary`. For example:

```bash
roary -f ./demo -e -n -v ./gff/*.gff
```

Run Roary in an [interactive session](../computing/running/interactive-usage.md) or as a
batch job, not on the login node. An interactive session can be started with:

```bash
sinteractive -i
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Roary home page](https://sanger-pathogens.github.io/Roary/)
