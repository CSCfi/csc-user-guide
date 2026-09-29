---
tags:
  - Free
catalog:
  name: GetOrganelle
  description: Assembly of organelle genomes from whole-genome sequencing data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# GetOrganelle

GetOrganelle is a toolkit for assembling organelle genomes (chloroplast, mitochondrial
and nuclear ribosomal DNA) from whole-genome sequencing data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/Kinggerm/GetOrganelle/blob/master/LICENSE.md).

## Available

* Roihu: 1.7.7.1, via the `bio-apps` module.

## Usage

GetOrganelle is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the GetOrganelle module:

```bash
module load bio-apps/v202603
module load getorganelle/1.7.7.1
```

### Databases

GetOrganelle needs seed and label databases for the organelle types you want to
assemble. Configure them with `get_organelle_config.py`. By default these are stored
under `~/.GetOrganelle`; you can choose another location by setting the `GETORG_PATH`
environment variable (for example to a directory in your project's `/scratch`).

```bash
export GETORG_PATH=/scratch/<project>/getorganelle
get_organelle_config.py --add embplant_pt,embplant_mt
```

### Running GetOrganelle

For example, to assemble a plant plastome from paired-end reads:

```bash
#!/bin/bash
#SBATCH --job-name=getorganelle
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G

module load bio-apps/v202603
module load getorganelle/1.7.7.1

export GETORG_PATH=/scratch/<project>/getorganelle

get_organelle_from_reads.py -1 read1.fq.gz -2 read2.fq.gz \
    -o plastome_out -F embplant_pt -t $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [GetOrganelle GitHub repository](https://github.com/Kinggerm/GetOrganelle)
