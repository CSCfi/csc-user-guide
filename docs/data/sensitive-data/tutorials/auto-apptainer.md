# Auto-apptainer

Auto-apptainer is a help tool that can be used to add software to a SD Desktop virtual machine. It utilizes a library of
of Apptainer based software contaners, pre-loaded by CSC. You can suggest a container to be added to the library.

Auto apptainer is not available by default, but you must install it first using [SD Software installer](./sd-software-installer.md).
After that you can lauch the tool with command:

```test
auto-apptainer
```
By deafault, this lists all the Apptainer packages available. From the list you can select the backage to be installed.

Alternatively you can add a fltering criteria to the command. In this case only those containers whose name or one 
of commands that the container provides, matches the search creiteria, are listed.

For example command :

```test
auto-apptainer bam
```

asks the user to choose from two contaiers: _bamtools_ and _bedtools_. Bedtools is included as it provides commands _bamToBed_ and _bamToFasta_ that match the serach criteria in this case.

Once a container is selected, one or more apptainer warpper based commands are created to drectory: _/shared-directory/sd-tools/bin_.
These commands can mostly be used like natively installed commands. For example after installing the Bamtools container, 
Bamtools can be startted with command:

```text
bamtools
```

Below you can fins a list of software that can be installed with auto-apptainer. The list can be outdated. You can get an up-to-date
list by running command _auto-apptainer_ in SD Desktop.

*  bamtools_2.5.2--hd03093a_1
*  bedtools_2.31.0
*  deepvariant_1.5.0
*  hisat2_2.2.1--h87f3376_5
*  regenie_3.0.1
*  samtools_1.17-2023-06
*  seqtk_v1.3-1-deb_cv1
*  stringtie_2.2.0--ha025227_1
*  taguette
*  vcftools_v0.1.16-1
*  vsearch_2.23.0--h6a68c12_0
*  weeder_2.0--h9f5acd7_7




