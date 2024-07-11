---
tags:
  - Free
---

# Roary

Roary is a high-speed standalone pan genome pipeline, which takes annotated assemblies in 
GFF3 format (produced by e.g. [Prokka](./prokka.md)) and calculates the pan genome.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Puhti: 3.13.0 

## Usage

On Puhti, Roary should be executed as a batch job. An interactive batch job for running Roary can be started with the command:

```bash
sinteractive -i 
```
 
To use Roary, load the module using the command:

```bash
module load roary
```

After that, you can launch Roary with the command `roary`. For example:

```bash
roary -f ./demo -e -n -v ./gff/*.gff
```

## More information

* [Roary home page](https://sanger-pathogens.github.io/Roary/)
