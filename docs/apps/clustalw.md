---
tags:
  - Free
catalog:
  name: ClustalW
  description: Multiple sequence alignment
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# ClustalW

ClustalW is a classic program for the multiple alignment of nucleic acid and protein
sequences. For large-scale alignments, consider the faster
[Clustal Omega](clustal-omega.md).

[TOC]

## License

Free to use and open source under [GNU LGPLv3](https://ftp.ebi.ac.uk/pub/software/clustalw2/).

## Available

* Roihu: 2.1, via the `bio-apps` module.

## Usage

ClustalW is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the ClustalW module:

```bash
module load bio-apps/v202603
module load clustalw/2.1
```

The program is run with the `clustalw2` command. For example, to align sequences in a
file:

```bash
clustalw2 -infile=sequences.fasta -outfile=aligned.aln
```

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=clustalw
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load clustalw/2.1

clustalw2 -infile=sequences.fasta -outfile=aligned.aln
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [ClustalW at EBI](https://www.ebi.ac.uk/jdispatcher/msa/clustalw2)
