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

* Roihu: 3.3.0, via the `bio-apps` module.

## Usage

Picard is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Picard module:

```bash
module load bio-apps/v202603
module load picard/3.3.0
```

To get a summary of available tools:

```bash
picard
```

Please note that in the Picard manual commands start with `java -jar
picard.jar`. On Roihu it is easiest to run Picard through the `picard`
wrapper, so substitute that with just `picard`.

Example:

```bash
picard SamToFASTQ I=input.bam FASTQ=output.fastq
```

If you need to specify Java options for Picard (for example to control the
Java heap size), you can run the jar directly with `java` — the module sets
the `$PICARD` environment variable to the Picard jar file.

Example:

```bash
java -Xmx16g -jar $PICARD SamToFASTQ I=input.bam FASTQ=output.fastq
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

-   [Picard home page](http://broadinstitute.github.io/picard/)
-   [Detailed tool documentation](http://broadinstitute.github.io/picard/command-line-overview.html)
