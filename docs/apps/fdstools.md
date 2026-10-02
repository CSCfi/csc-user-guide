---
tags:
  - Free
catalog:
  name: FDSTools
  description: Noise analysis and allele calling for forensic DNA sequencing data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# FDSTools

FDSTools (Forensic DNA Sequencing Tools) is a collection of tools for analysing
massively parallel sequencing data of forensic DNA markers such as STRs and SNPs.
It characterises and filters PCR stutter and other systematic noise, and detects the
true alleles in a sample. Alleles are named with the STRNaming nomenclature.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/Jerrythafast/FDSTools/blob/main/LICENSE.txt).

## Available

* Roihu-CPU: 2.2.1 (module `py-fdstools`), via the `bio-apps` module.

## Usage

FDSTools is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the FDSTools module:

```bash
module load bio-apps/v202603
module load py-fdstools/2.2.1
```

All tools are run through the `fdstools` command. List the tools, or show the
options of a single tool, with:

```bash
fdstools --help
fdstools --help tssv
```

### Analysis pipelines

The `pipeline` tool runs complete, predefined analyses configured with an INI file.
There are three analysis types:

* `reference-sample`: runs a single reference sample through TSSV and Stuttermark.
* `reference-database`: builds a database of systematic noise from a collection of
  reference samples.
* `case-sample`: runs a single case sample through TSSV, BGPredict, BGCorrect and
  Samplestats.

The analyses need a library file that describes your markers. Create one with
`fdstools library mylibrary.txt` and fill in your markers.

If the INI file does not exist yet, `pipeline` creates it with the default settings
for the chosen analysis type:

```bash
fdstools pipeline case.ini --analysis case-sample
```

Fill in the input files and settings in `case.ini`, then run the analysis:

```bash
fdstools pipeline case.ini
```

Read counting with TSSV is the slowest step. To use several cores, set `num-threads`
in the `[tssv]` section of the INI file to the number of cores reserved for the job.

### Running individual tools

The tools can also be run one at a time. For tools that process sample data files,
such as `stuttermark`, `bgcorrect`, `samplestats` and `seqconvert`, give the input
files with `-i` and the output files with `-o`. Giving the input file as a plain
argument without `-i` does not work on Roihu.

```bash
fdstools samplestats -i sample.csv -o sample_stats.csv
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=fdstools
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2G

module load bio-apps/v202603
module load py-fdstools/2.2.1

fdstools pipeline case.ini
```

With `num-threads = 4` in the `[tssv]` section of `case.ini`, TSSV uses all four
cores reserved for the job. Replace `<project>` with your CSC project (for example
`project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [FDSTools home page](https://fdstools.nl)
* [FDSTools GitHub repository](https://github.com/Jerrythafast/FDSTools)
