---
tags:
  - Free
catalog:
  name: FastQC
  description: Quality control tool for high throughput sequence data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
    - Roihu
---

# FastQC

FastQC is a quality control tool for high-throughput sequence data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

- Puhti: 0.11.9
- Roihu
- [Chipster](https://chipster.csc.fi) graphical user interface

Check the installed version on Roihu with `module avail fastqc` after loading `bio-apps`.

## Usage

### Puhti

To initialize on Puhti, use:

```bash
module load biokit
```

You can then run FastQC:

```bash
fastqc --help
```

If you run FastQC without command line arguments, it will open a GUI. The best way to run a GUI remotely on Puhti is to use the [Puhti web interface desktop](../computing/webinterface/desktop.md).

### Roihu

On Roihu, FastQC is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load fastqc
```

You can then run FastQC:

```bash
fastqc --help
```

FastQC processes one file per thread. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=fastqc
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load fastqc

srun fastqc --threads $SLURM_CPUS_PER_TASK sample_1.fastq.gz sample_2.fastq.gz
```

Submit the job with `sbatch fastqc_job.sh`.

## More information

* [FastQC Homepage](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
