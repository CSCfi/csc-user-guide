# Auto-apptainer

Auto-apptainer is a help tool that can be used to add software to a SD Desktop virtual machine. It utilizes a library
of Apptainer-based software containers, pre-loaded by CSC. You can suggest a container to be added to the library.

Auto-apptainer is not available by default, but you must install it first using [SD Software installer](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer)

After that you can launch the tool with command:

```text
auto-apptainer
```

By default, this lists all the Apptainer packages available for auto-apptainer. From the list you can select the package to be installed.

Alternatively you can add a filtering criteria to the command. In this case only those containers whose name or one 
of commands that the container provides, matches the search criteria, are listed.

For example command:

```test
auto-apptainer bam
```

asks the user to choose from two containers: _bamtools_ and _bedtools_. Bedtools is included as it provides commands `bamToBed` and `bamToFasta` that match the search criteria in this case.

Once a container is selected, one or more Apptainer wrapper-based commands are created to drectory: `/shared-directory/sd-tools/bin`.
These commands can mostly be used like natively installed commands. For example after installing the Bamtools container, 
Bamtools can be started with command:

```text
bamtools
```

Below you can find a list of software that can be installed with auto-apptainer. The list can be outdated. You can get an up-to-date
list by running command `auto-apptainer` in SD Desktop.

*  allelecount-4.2.1
*  bamtools_2.5.2--hd03093a_1
*  bcftools_1.20
*  bedtools_2.31.0
*  cnvkit-0.9.12
*  deepvariant_1.5.0
*  EIG_8.0.0
*  hisat2_2.2.1--h87f3376_5
*  htseq-2.0.3
*  image-to-text
*  kneaddata-0.12.0
*  kneaddata-0.12.1
*  mpv-0.34.1
*  p7zio
*  pdf2searchablepdf
*  picard
*  python3-for-medimaging
*  samtools_1.17-2023-06
*  seqtk_v1.3-1-deb_cv1
*  stringtie_2.2.0--ha025227_1
*  taguette.info
*  trimgalore-0.6.9
*  vcftools_v0.1.16-1
*  vsearch_2.23.0
*  weeder_2.0--h9f5acd7_7





