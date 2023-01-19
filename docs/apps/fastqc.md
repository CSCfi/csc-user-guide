---
tags:
  - Free
---

# FastQC

## Description

FastQC is a  quality control tool for high throughput sequence data.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

###Version on CSC's Servers

-   Puhti: 0.11.8 
-   [Chipster](https://chipster.csc.fi) graphical user interface

##Usage


To initialize in Puhti use:
```text
module load biokit
```

You can then run FastQC:
```text
fastqc --help
```

If you run FastQC without command line arguments, it will open a GUI. The best way to run a GUI remotely on Puhti is to use the [Puhti web interface desktop](../computing/webinterface/desktop.md).

## Manual

*   [FastQC Homepage](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
