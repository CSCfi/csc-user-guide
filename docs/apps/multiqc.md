---
tags:
  - Free
catalog:
  name: MultiQC
  description: Aggregate bioinformatics analysis results into a single report
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MultiQC

MultiQC collects the results and logs of many bioinformatics tools, such as FastQC,
Cutadapt, STAR, Salmon and samtools, from across your samples into a single HTML
report.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://github.com/MultiQC/MultiQC/blob/main/LICENSE).

## Available

* Roihu-CPU: 1.28 and 1.35 (module `py-multiqc`), via the `bio-apps` module.

## Usage

MultiQC is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MultiQC module:

```bash
module load bio-apps/v202603
module load py-multiqc/1.35
```

Run MultiQC on the directory that contains the output of your analysis tools. MultiQC
searches the directory and its subdirectories for results it recognises:

```bash
multiqc results/
```

The report is written to `multiqc_report.html` and the parsed data to `multiqc_data`
in the current directory. Use `-o` to write them to another directory and `-n` to
change the report name.

To view the report, download it to your own computer, for example with the
[file browser of the web interface](../computing/webinterface/file-browser.md), and
open it in a web browser.

MultiQC only reads the results of other tools and usually finishes in seconds, so it
counts as light postprocessing and can be run on the login node. For very large
projects with thousands of samples, use an
[interactive session](../computing/running/interactive-usage.md) instead.

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [MultiQC documentation](https://docs.seqera.io/multiqc)
* [MultiQC GitHub repository](https://github.com/MultiQC/MultiQC)
