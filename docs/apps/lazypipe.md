# Lazypipe

## Description 

Lazypipe is a stand-alone pipeline for identifying viruses in host-associated or environmental samples. The main emphasis is on assembling, taxonomic binning and taxonomic profiling of bacterial/viral sequences.

## Usage

All componnets of Lazypipe pipeline are available in Puhti. The [Lazypipe home page](https://www.helsinki.fi/en/projects/lazypipe) provides detailed insruction how ro set up your own Lazypipe environment to Puhti, but this is not needed is you
use the Lazypipe module that is loaded with commands:

```text
module load biokit
module load lazypipe
```
The Lazypipe module includes `sbatch-lazypipe` command that automatically submits a Lazypipe task to the batch job system of Puhti. 
