# MACS2


## Description

MACS (Model-based Analysis of ChIP-Seq) is an analysis tool for NGS ChIP-Seq data. 
MACS empirically models the length of the sequenced ChIP fragments and uses it to improve 
the spatial resolution of predicted binding sites. 

MACS also uses a dynamic Poisson distribution to effectively capture local biases in the 
genome sequence, allowing for more sensitive and robust prediction. MACS compares can be 
used for ChIP-Seq with or without control samples.

[TOC]

## License

Free to use and open source under [BSD 3-Clause License](https://raw.githubusercontent.com/macs3-project/MACS/master/LICENSE).

## Available

Version on CSC's Servers

Puhti: 2.2.6
Chipster graphical user interface

## Usage

To set up MACS2 commands in puhti, give command:

```text
module load bioconda
```

After that you can start MACS2 with command:
```text
macs2 -h
```

Larger MACS jobs should be executed as a batch job in Puhti. Puhti User Guide for more information on running batch jobs.

## More information

   *   [MACS2 in GitHub](https://github.com/taoliu/MACS/)
