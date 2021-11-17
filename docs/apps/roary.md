# Roary

## Description

Roary is a high speed stand alone pan genome pipeline, which takes annotated assemblies in 
GFF3 format (produced by e.g. [Prokka](./prokka.md) ) and calculates the pan genome.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

*   Roary 3.13.0 is available in Puhti

## Usage

In Puhti, Roary should be executed as a batch job. An interactive batch job for running Roary can be started
with command:

```text
sinteractive -i 
```

Roaray is installed to Puhti as a part of bioconda environment of Prokka. 
To use it, you should activate Prokka environment with commands:

```text
export PROJAPPL=/projappl/your_project_name
module load bioconda
source activate prokka
```
After that you can launch Roary with command `roary`. For example:
```
roary -f ./demo -e -n -v ./gff/*.gff
```

## More information

*   [Roary home page](https://sanger-pathogens.github.io/Roary/)

