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

-  Puhti-rhel8: 2.2.7.1, 3.0.0a7
-  Chipster graphical user interface

## Usage

To set up MACS2 and MACS3 commands in puhti, give command:

```text
module load macs
```

Module macs/2.2.7.1 also loads MACS 3.0.0a7.

After that you can start MACS with command:
```text
macs2 -h
macs3 -h
```

Short MACS jobs can be executed as [interactive batch jobs](../computing/running/interactive-usage.md) in Puhti-rhel8. Longer jobs should be run as [batch jobs](../computing/running/getting-started.md).


## More information

   *   [MACS2 in GitHub](https://github.com/taoliu/MACS/)
   *   [MACS3 in GitHub](https://github.com/macs3-project/MACS/)
