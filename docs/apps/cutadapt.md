---
tags:
  - Free
catalog:
  name: Cutadapt
  description: Trimming high-throughput sequencing reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
    - Roihu
---

# Cutadapt

Cutadapt finds and removes adapter sequences, primers, poly-A tails and other types of 
unwanted sequence from your high-throughput sequencing reads.

[TOC]

## License

Free to use and open source under [MIT License](https://github.com/marcelm/cutadapt/blob/main/LICENSE)

## Available

- Puhti: 3.2, 3.4, 3.5, 4.6
- Roihu: 4.7

Check the installed versions on Roihu with `module avail py-cutadapt` after loading
`bio-apps`.

## Usage

### Puhti

On Puhti, the latest version of Cutadapt can be taken in use by loading the module:

```bash
module load cutadapt
```

You can check the available versions with the command:

```bash
module spider cutadapt
```

You can load a specific version with the command:

```bash
module load cutadapt/3.2
```

The basic syntax is:

```bash
cutadapt --help
```

Cutadapt should be run either in an interactive session or as a batch job.

### Roihu

On Roihu, Cutadapt is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load py-cutadapt
```

The basic syntax is the same as on Puhti:

```bash
cutadapt --help
```

Cutadapt should be run either in an interactive session or as a batch job. An example
batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=cutadapt
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load py-cutadapt

srun cutadapt -j $SLURM_CPUS_PER_TASK -a AGATCGGAAGAGC -o trimmed.fastq.gz input.fastq.gz
```

Submit the job with `sbatch cutadapt_job.sh`.

## Support

[CSC Service Desk](../support/contact.md)

## More information

More information about Cutadapt can be found from the [Cutadapt home page](https://cutadapt.readthedocs.io/en/stable/).
