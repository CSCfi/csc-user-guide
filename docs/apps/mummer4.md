---
tags:
  - Free
catalog:
  name: MUMmer
  description: Genome alignment (MUMmer)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MUMmer

MUMmer is a versatile alignment tool for DNA and protein sequences. It is commonly used
for rapidly aligning whole genomes, comparing assemblies and detecting structural
differences. On Roihu it is provided as MUMmer 4, which includes tools such as `nucmer`,
`promer`, `mummer`, `dnadiff` and `show-coords`.

[TOC]

## License

Free to use and open source. See the [MUMmer repository](https://github.com/mummer4/mummer/blob/master/LICENSE.md).

## Available

* Roihu: 4.0.1 (module `mummer4`), via the `bio-apps` module.

## Usage

MUMmer is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MUMmer module:

```bash
module load bio-apps/v202603
module load mummer4/4.0.1
```

For example, to align a query genome against a reference with `nucmer` and summarise the
alignment coordinates:

```bash
nucmer --threads 8 -p out reference.fa query.fa
show-coords -r out.delta > out.coords
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=mummer
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load mummer4/4.0.1

nucmer --threads $SLURM_CPUS_PER_TASK -p out reference.fa query.fa
show-coords -r out.delta > out.coords
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MUMmer home page](https://mummer4.github.io/)
* [MUMmer GitHub repository](https://github.com/mummer4/mummer)
