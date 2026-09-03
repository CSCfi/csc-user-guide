---
tags:
  - Free
catalog:
  name: FastQC
  description: Quality control tool for high throughput sequence data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# FastQC

FastQC is a quality control tool for high-throughput sequence data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

- Roihu: 0.12.1
- [Chipster](https://chipster.csc.fi) graphical user interface

## Usage

To initialize on Roihu, use:

```bash
module load bio-apps
module load fastqc
```

You can then run FastQC:

```bash
fastqc --help
```

If you run FastQC without command line arguments, it will open a GUI. The best way to run a GUI remotely on Roihu is to use the [Roihu web interface desktop](../computing/webinterface/desktop.md).

## More information

* [FastQC Homepage](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
