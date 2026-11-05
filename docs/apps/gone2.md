---
tags:
  - Free
catalog:
  name: GONE2
  description: Recent effective population size history from linkage disequilibrium
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# GONE2

GONE2 estimates the recent history of effective population size (Ne) from the linkage
disequilibrium between pairs of SNPs. It can also account for population structure,
low-coverage sequencing data and genotyping errors.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/esrud/GONE2/blob/main/LICENSE).

## Available

* Roihu-CPU: 2.0.2, via the `bio-apps` module.

## Usage

GONE2 is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the GONE2 module:

```bash
module load bio-apps/v202603
module load gone2/2.0.2
```

GONE2 reads genotype data in VCF, PED or TPED format. The file must be uncompressed
and its name must end in `.vcf`, `.ped` or `.tped`. GONE2 also needs the positions of
the SNPs on a genetic map. These are read from the `.tped` file itself, or, for `.vcf`
and `.ped` files, from a PLINK `.map` file with the same name in the same directory.
Alternatively, use `-r` to give a constant recombination rate in cM/Mb, and GONE2
converts the physical positions into a genetic map.

For example, analyse unphased diploid genotypes in `data.vcf`, assuming a
recombination rate of 1.1 cM/Mb across the genome:

```bash
gone2 -r 1.1 -t 8 -o mypop data.vcf
```

Commonly used options:

* `-g`: type of genotype data: `0` unphased diploid (default), `1` haploid, `2` phased
  diploid, `3` low-coverage
* `-x`: treat the sample as coming from a metapopulation with several subpopulations
* `-s` and `-i`: use a random subset of this many SNPs or individuals
* `-t`: number of threads
* `-o`: base name of the output files
* `-S`: seed for the random number generator. GONE2 uses a genetic algorithm, so
  results differ slightly between runs unless you fix both `-S` and `-t`.

The Ne estimates for the last 150 generations are written to `mypop_GONE2_Ne`, the
observed and predicted linkage disequilibrium to `mypop_GONE2_d2`, and a summary of
the run to `mypop_GONE2_STATS`. With `-x`, the files are named `mypop_GONE2_mix_*`.
If you leave out `-o`, the output names start with the full input file name, for
example `data.vcf_GONE2_Ne`.

The module also provides `gone2_tui`, which runs the same analysis and shows its
progress and the Ne curve live in the terminal. Use it in an
[interactive session](../computing/running/interactive-usage.md), and `gone2` in batch
jobs.

GONE2 on Roihu accepts at most 2,000,000 SNPs and 2,000 individuals (1,000 with
phased data, `-g 2`). For larger datasets, reduce your data first, for example with
[PLINK](plink.md). GONE2 always reserves about 4 GiB of memory for the genotype data,
whatever the size of your input, so reserve at least 8 GiB for the job.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=gone2
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=8G

module load bio-apps/v202603
module load gone2/2.0.2

gone2 -r 1.1 -t $SLURM_CPUS_PER_TASK -o mypop data.vcf
```

Replace `<project>` with your CSC project (for example `project_2001234`), and `1.1`
with a recombination rate suited to your species, or leave out `-r` and provide a
`data.map` file.

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [GONE2 GitHub repository](https://github.com/esrud/GONE2)
* [Santiago, E., Köpke, C. & Caballero, A. (2025). Accounting for population structure and data quality in demographic inference with linkage disequilibrium methods. Nature Communications 16, 6054](https://doi.org/10.1038/s41467-025-61378-w)
