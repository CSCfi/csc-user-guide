---
tags:
  - Free
catalog:
  name: InterProScan
  description: Protein signature/motif search tool
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# InterProScan

InterProScan is a tool that compares protein or nucleotide sequence against a set of protein signature databases.
The results obtained from different databases are given in uniform format. The InterProScan 5 installation on Roihu can
be used to search protein signatures from the following databases:

   * AntiFam
   * CDD
   * FunFam
   * Gene3D
   * HAMAP
   * NCBIfam
   * PANTHER
   * Pfam
   * PIRSF
   * PIRSR
   * PRINTS
   * PROSITE (patterns and profiles)
   * SFLD
   * SMART
   * SUPERFAMILY

The analyses that require a separate license (Phobius, SignalP and TMHMM) are not
available. To see the available analyses and their database versions, run
`interproscan.sh -h`.

[TOC]

## License

Free to use and open source under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Available

* Roihu-CPU: 5.76-107.0, via the `bio-apps` module.

## Usage

InterProScan is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the InterProScan module:

```bash
module load bio-apps/v202603
module load interproscan/5.76-107.0
```

The InterProScan data is installed in a shared location on Roihu. The module sets the
`INTERPROSCAN_CONF` environment variable to a configuration file that points
InterProScan to this data, so you don't need to download or configure anything
yourself.

InterProScan is run with the `interproscan.sh` command. To check the available
options, give the command:

```bash
interproscan.sh -h
```

Below are two sample InterProScan commands:

1. Running InterProScan search for a nucleotide sequence set against all InterProScan databases.
Results are reported in XML format.

```bash
interproscan.sh -i nucleotides.fasta -o results.xml -f XML -t n
```

2. Running InterProScan search for a protein sequence set against Pfam. Results are reported in GFF3 format.

```bash
interproscan.sh -i proteins.fasta -o results.gff3 -f GFF3 -appl Pfam
```

The `interproscan.sh` launcher reserves up to 14 GB of memory for Java alone, so don't
run InterProScan on the login nodes. Use an
[interactive session](../computing/running/interactive-usage.md) with enough cores to
get the memory, for example `sinteractive --account <project> --cores 12 --time 04:00:00`
(about 22 GB), or a batch job.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=interproscan
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G

module load bio-apps/v202603
module load interproscan/5.76-107.0

interproscan.sh -i proteins.fasta -o results.tsv -f TSV -cpu $SLURM_CPUS_PER_TASK
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

*   [InterPro home page](https://www.ebi.ac.uk/interpro/)
*   [InterProScan documentation](https://interproscan-docs.readthedocs.io/en/v5/)
