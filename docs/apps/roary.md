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
    - Puhti
    - Roihu
---

# Roary

Roary is a high-speed standalone pan genome pipeline, which takes annotated assemblies in 
GFF3 format (produced by e.g. [Prokka](./prokka.md)) and calculates the pan genome.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Puhti: 3.13.0 
* Roihu-CPU: 3.13.0

Check the installed versions on Roihu with `module avail roary` after
loading `bio-apps`.

## Usage

### Puhti

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

### Roihu

On Roihu, Roary is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load roary
```

Roary is used the same way as on Puhti, for example:

```bash
roary -p $SLURM_CPUS_PER_TASK -f ./demo -e -n -v ./gff/*.gff
```

An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=roary
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load roary

srun roary -p $SLURM_CPUS_PER_TASK -f ./demo -e -n -v ./gff/*.gff
```

Submit the job with `sbatch roary_roihu_job.sh`.

## More information

* [Roary home page](https://sanger-pathogens.github.io/Roary/)
