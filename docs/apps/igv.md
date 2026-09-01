---
tags:
  - Free
catalog:
  name: IGV
  description: Integrative Genomics Viewer - interactive genome browser
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# IGV

The Integrative Genomics Viewer (IGV) is a high-performance, interactive tool for the
visual exploration of genomic data, including aligned sequence reads, variants and
genomic annotations.

[TOC]

## License

Free to use and open source under the [MIT License](https://github.com/igvteam/igv/blob/master/license.txt).

## Available

* Roihu: 2.19.7, via the `bio-apps` module.

## Usage

IGV is a graphical application, so it is best run through the
[Roihu web interface remote desktop](../computing/webinterface/desktop.md):

1. Open the [Desktop app](../computing/webinterface/desktop.md) in the Roihu web interface.
2. Open a terminal from `Applications` -> `Terminal Emulator`.
3. Load the modules and start the IGV GUI with the `igv.sh` launch script:

```bash
module load bio-apps/v202603
module load igv/2.19.7
igv.sh
```

### igvtools

For command-line tasks such as creating index or coverage files for large data, use
the `igvtools` utility, which can be run in a normal terminal or batch job. For example,
to index a sorted BAM file:

```bash
module load bio-apps/v202603
module load igv/2.19.7
igvtools index aligned.sorted.bam
```

`igvtools` can also be run as a batch job:

```bash
#!/bin/bash
#SBATCH --job-name=igvtools
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

module load bio-apps/v202603
module load igv/2.19.7

igvtools index aligned.sorted.bam
```

Replace `<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [IGV home page](https://igv.org/)
* [IGV user guide](https://igv.org/doc/desktop/)
