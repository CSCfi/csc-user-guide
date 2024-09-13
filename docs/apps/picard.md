---
tags:
  - Free
---

# Picard Tools



Picard is a set of command line tools for manipulating high-throughput
sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.


[TOC]

## License

Free to use and open source under [MIT License](https://github.com/broadinstitute/picard/blob/master/LICENSE.txt).

## Available


- Puhti:  2.27.4, 2.27.5, 3.0.1,  3.1.1

## Usage

To load Picard, load module:
```bash
module load picard
```

Note: The `biokit` module comes with Picard version 2.27.5 due to Java version compatibility
with other software. To use newer version of Picard, load the `picard` module.

To get a summary of available tools:
```bash
picard
```

Please note that in the Picard manual commands start with "java -jar
picard.jar". In Puhti it is easiest to run Picard through a wrapper script,
so substitute that with just `picard`.

Example:
```bash
picard SamToFASTQ I=input.bam FASTQ=output.fastq
```

By default picard can use up to 8 GB  of memory. If your analysis task
requires more memory, you can launch picard with commands, `picard16`, `picard32`
and `picard64` that reserve 16, 32 or 64 GB of memory respectively.

Example:
```bash
picard16 SamToFASTQ I=input.bam FASTQ=output.fastq
```

If you need to specify Java options for Picard you can use `java -jar $PICARD`.

Example:
```bash
java -Xmx128g -jar $PICARD  SamToFASTQ I=input.bam FASTQ=output.fastq
```


## More information

-   [Picard home page](http://broadinstitute.github.io/picard/)
-   [Detailed tool documentation](http://broadinstitute.github.io/picard/command-line-overview.html)
