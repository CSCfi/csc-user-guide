---
tags:
  - Free
catalog:
  name: PLINK
  description: Whole-genome association and population-based linkage analyses
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# PLINK

PLINK is a toolset for genome-wide association studies (GWAS) and population-based
linkage analyses. It converts and filters genotype data, computes summary statistics
and runs association tests on large datasets. Roihu has both PLINK 1.9 and PLINK 2.0.

[TOC]

## License

Free to use and open source under GNU GPLv3. See the
[PLINK 1.9 license](https://github.com/chrchang/plink-ng/blob/master/1.9/LICENSE) and the
[PLINK 2.0 license](https://github.com/chrchang/plink-ng/blob/master/2.0/COPYING).

## Available

* Roihu-CPU: 1.9.0 (module `plink`), and 2.0.0-a.6.9 and 2.0.0-b.1.3 (module
  `plink2`), via the `bio-apps` module.

## Usage

PLINK is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the PLINK version you need. PLINK 1.9 is run with the `plink`
command and PLINK 2.0 with the `plink2` command:

```bash
module load bio-apps/v202603
module load plink/1.9.0
module load plink2/2.0.0-b.1.3
```

PLINK 2.0 is faster and supports more data types, but some PLINK 1.9 features are
not yet available in it.

For example, convert a VCF file to the PLINK 1 binary format and compute allele
frequencies with PLINK 1.9:

```bash
plink --vcf data.vcf.gz --make-bed --out data
plink --bfile data --freq --out data
```

The same with PLINK 2.0, which uses its own PGEN format:

```bash
plink2 --vcf data.vcf.gz --make-pgen --out data
plink2 --pfile data --freq --out data
```

PLINK uses the cores reserved for your job by default. For memory, however, it
reserves half of the node's total memory, not half of the memory reserved for your
job, so always set `--memory` (in MiB) to fit within your job's memory.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=plink
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G

module load bio-apps/v202603
module load plink2/2.0.0-b.1.3

plink2 --pfile data --freq --memory 15000 --out data
```

`--memory 15000` leaves some of the 16 GiB reserved for the job free for PLINK's own
overhead. Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [PLINK 1.9 documentation](https://www.cog-genomics.org/plink/1.9/)
* [PLINK 2.0 documentation](https://www.cog-genomics.org/plink/2.0/)
* [PLINK GitHub repository](https://github.com/chrchang/plink-ng)
