# Picard Tools

## Description

Picard is a set of command line tools for manipulating high-throughput
sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.


[TOC]

## License

Free to use and open source under [MIT License](https://github.com/broadinstitute/picard/blob/master/LICENSE.txt).

## Available

Version on CSC's Servers
- Puhti: 2.21.4

## Usage

To load Picard, laod biokit:
```text
module load biokit
```

To get a summary of available tools:
```text
picard
```

Please note that in the Picard manual commands start with "java -jar
picard.jar". In Puhti Picard needs to be run through a wrapper script,
so substitute that with just **picard**.

Example:
```
picard SamToFASTQ I=input.bam FASTQ=output.fastq
```

By default picard can use up to 8 GB  of memory. If your analysis task
requires more memory, you can launch picard with commands, **picard16**, **picard32**
and **picard64** that reserve 16, 32 or 64 GB of memory.

Example:
```text
picard16 SamToFASTQ I=input.bam FASTQ=output.fastq
```

## Manual

-   [Picard home page](http://broadinstitute.github.io/picard/)
-   [Detailed tool documentation](http://broadinstitute.github.io/picard/command-line-overview.html)
