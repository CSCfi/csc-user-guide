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

* Roihu: 3.13.0 

## Usage

Roary can be taken in use by first loading the bio-apps module:


```bash
module load bio-apps
module load roary
```

After that, you can launch Roary with the command `roary`. For example:

```bash
roary -f ./demo -e -n -v ./gff/*.gff
```

All Roary jobs jobs should be run either in an [interactive session](../computing/running/interactive-usage.md) or as batch job. More information about running batch jobs can be found from the [batch job section of the Roihu user guide](../computing/running/getting-started.md).


## More information

* [Roary home page](https://sanger-pathogens.github.io/Roary/)
