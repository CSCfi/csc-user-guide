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

* Roihu: 3.13.0, via the `bio-apps` module.

## Usage

Roary should be executed as a batch job. An interactive batch job for running Roary can be started with the command:

```bash
sinteractive -i 
```
 
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

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [Roary home page](https://sanger-pathogens.github.io/Roary/)
