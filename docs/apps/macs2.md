---
tags:
  - Free
catalog:
  name: MACS2/3
  description: ChIP-Seq analysis tool
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MACS2/3

MACS (Model-based Analysis of ChIP-Seq) is an analysis tool for NGS ChIP-Seq data.
MACS empirically models the length of the sequenced ChIP fragments and uses it to improve
the spatial resolution of predicted binding sites.

MACS also uses a dynamic Poisson distribution to effectively capture local biases in the
genome sequence, allowing for more sensitive and robust prediction. MACS can be
used for ChIP-Seq with or without control samples.

[TOC]

## License

Free to use and open source under [BSD 3-Clause License](https://raw.githubusercontent.com/macs3-project/MACS/master/LICENSE).

## Available

* Roihu-CPU: MACS2 2.2.9.1 (module `py-macs2`), and MACS3 3.0.4 and 3.1.0 (module
  `py-macs3`), via the `bio-apps` module.
* Chipster graphical user interface

## Usage

MACS is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the bio-apps
module tree and then the MACS version you need. MACS3 is run with the `macs3` command:

```bash
module load bio-apps/v202603
module load py-macs3/3.1.0
macs3 -h
```

For MACS2, load `py-macs2/2.2.9.1` instead and use the `macs2` command.

For example, call peaks from a ChIP-Seq sample against a control sample:

```bash
macs3 callpeak -t chip.bam -c control.bam -f BAM -g hs -n mysample --outdir macs_out
```

`-g` is the effective genome size. Shortcuts exist for some model organisms, such as
`hs` for human and `mm` for mouse. For other species, give the size as a number.

### Example batch script

```bash
#!/bin/bash
#SBATCH --job-name=macs
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load bio-apps/v202603
module load py-macs3/3.1.0

macs3 callpeak -t chip.bam -c control.bam -f BAM -g hs -n mysample --outdir macs_out
```

`macs3 callpeak` uses one core, so reserving more does not make it faster. Replace
`<project>` with your CSC project (for example `project_2001234`).

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MACS2 in GitHub](https://github.com/taoliu/MACS/)
* [MACS3 in GitHub](https://github.com/macs3-project/MACS/)
