---
tags:
  - Free
catalog:
  name: ABySS
  description: De novo, parallel, paired-end sequence assembler
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ABySS

ABySS (Assembly By Short Sequences) is a de novo, parallel, paired-end sequence assembler
that is designed for short reads. The single-processor version is useful for assembling
genomes up to 100 Mbases in size, while the parallel (MPI) version can assemble larger
genomes.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/bcgsc/abyss/blob/master/LICENSE).

## Available

* Roihu: 2.3.10, via the `bio-apps` module.

## Usage

ABySS is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the ABySS module:

```bash
module load bio-apps/v202603
module load abyss/2.3.10
```

Assemblies are run with the `abyss-pe` driver. A minimal paired-end assembly uses a
k-mer size (`k`), an output name (`name`) and the input reads (`in`):

```bash
abyss-pe k=64 name=assembly in='reads1.fq.gz reads2.fq.gz'
```

The assembly step can be parallelized with MPI by setting `np` to the number of MPI
processes; other steps use OpenMP threads set with `j`.

### Example batch script

Assembly jobs are resource demanding and should be run as batch jobs. Below is a
sample MPI batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=abyss
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load abyss/2.3.10

abyss-pe np=$SLURM_NTASKS j=$SLURM_NTASKS k=64 name=assembly in='reads1.fq.gz reads2.fq.gz'
```

Replace `<project>` with your CSC project (for example `project_2001234`).

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ABySS home page](https://www.bcgsc.ca/resources/software/abyss)
* [ABySS GitHub repository](https://github.com/bcgsc/abyss)
