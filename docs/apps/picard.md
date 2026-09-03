---
tags:
  - Free
catalog:
  name: Picard Tools
  description: Tools for working with SAM,BAM,CRAM and VCF files
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Picard Tools



Picard is a set of command line tools for manipulating high-throughput
sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.


[TOC]

## License

Free to use and open source under [MIT License](https://github.com/broadinstitute/picard/blob/master/LICENSE.txt).

## Available


- Roihu:  3.3.0

## Usage

To load Picard, load module:
```bash
module load bio-apps
module load picard
```

To get a summary of available tools:
```bash
picard
```

Please note that in the Picard manual commands start with "java -jar
picard.jar". In Roihu it is easiest to run Picard through a wrapper script,
so substitute that with just `picard`.

Example:
```bash
picard SamToFASTQ I=input.bam FASTQ=output.fastq
```

If you need to specify Java options for Picard you can use `java -jar $PICARD`.

Example:
```bash
java -Xmx128g -jar $PICARD  SamToFASTQ I=input.bam FASTQ=output.fastq
```

All Picard jobs should be run either in an [interactive session](../computing/running/interactive-usage.md) or as batch job. More information about running batch jobs can be found from the [batch job section of the Roihu user guide](../computing/running/getting-started.md).


## More information

-   [Picard home page](http://broadinstitute.github.io/picard/)
-   [Detailed tool documentation](http://broadinstitute.github.io/picard/command-line-overview.html)
