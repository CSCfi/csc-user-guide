---
tags:
  - Free
catalog:
  name: NCBI C++ Toolkit
  description: NCBI C++ Toolkit libraries and command-line applications
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# NCBI C++ Toolkit

The NCBI C++ Toolkit is a large collection of libraries and applications from NCBI for
working with biological sequence data and the associated ASN.1 data formats. On Roihu it
is provided mainly for the command-line utilities it installs.

[TOC]

## License

The NCBI C++ Toolkit is released into the public domain by the US National Center for
Biotechnology Information. See the
[NCBI C++ Toolkit documentation](https://www.ncbi.nlm.nih.gov/toolkit) for details.

## Available

* Roihu: 28_0_12 (module `ncbi-toolkit`), via the `bio-apps` module.

## Usage

The NCBI C++ Toolkit is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the module:

```bash
module load bio-apps/v202603
module load ncbi-toolkit/28_0_12
```

The module installs a large number of programs. Most are the toolkit's own internal
**test, sample and database-driver programs** (for example `unit_test_*`, `test_*`,
`odbc100_*`, `tds100_*`), which are not intended for end users. The user-facing
command-line applications include:

* **ASN.1 and data-conversion tools:** `datatool`, `asn2asn`, `asn2fasta`, `asn2flat`,
  `asnvalidate`, `asn_cleanup`, `table2asn`, `tableval`, `idfetch`, `srcchk`,
  `agpconvert`, `agp_validate`, `multireader`.
* **Sequence-analysis tools:** `splign`, `nw_aligner`, `vecscreen`, `windowmasker`.
* **The BLAST+ programs** (`blastn`, `blastp`, `makeblastdb`, …). For standalone BLAST
  searches, the dedicated `blast-plus` module is the recommended option.

For example, to convert an ASN.1 file to FASTA with `asn2fasta`:

```bash
asn2fasta -i input.asn -o output.fasta
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=ncbi-toolkit
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load ncbi-toolkit/28_0_12

table2asn -indir submission_files -outdir asn_out
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [NCBI C++ Toolkit documentation](https://www.ncbi.nlm.nih.gov/toolkit)
* [NCBI C++ Toolkit book](https://ncbi.github.io/cxx-toolkit/)
