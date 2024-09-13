---
tags:
  - Free
---

# BamTools

BamTools provides both a programmer's API and an end-user's toolkit for handling
BAM files.

[TOC]

## License

Free to use and open source under [MIT License](https://raw.githubusercontent.com/pezmaster31/bamtools/master/LICENSE)

## Available

-   Puhti: 2.5.2
-   Chipster graphical user interface

## Usage

On Puhti, BamTools can be taken in use as a part of biokit module collection:

```bash
module load biokit
```

The biokit module sets up a set of commonly used bioinformatics tools. Note however that there are other bioinformatics tools on Puhti,
that have a separate setup commands.

The syntax of BamTools is:

```
bamtools COMMAND ARGUMENTS
```

Available bamtools commands:

- `convert`         Converts between BAM and a number of other formats
- `count`           Prints number of alignments in BAM file(s)
- `coverage`        Prints coverage statistics from the input BAM file
- `filter`          Filters BAM file(s) by user-specified criteria
- `header`          Prints BAM header information
- `index`           Generates index for BAM file
- `merge`           Merge multiple BAM files into single file
- `random`          Select random alignments from existing BAM file(s), intended more as a testing tool.
- `resolve`         Resolves paired-end reads (marking the IsProperPair flag as needed)
- `revert`          Removes duplicate marks and restores original base qualities
- `sort`            Sorts the BAM file according to some criteria
- `split`           Splits a BAM file on user-specified property, creating a new BAM output file for each value found
- `stats`           Prints some basic statistics from input BAM file(s)

For more information on a specific command, run command:

```
bamtools help COMMAND
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

More information about BamTools can be found from the [BamTools home page](https://github.com/pezmaster31/bamtools).
