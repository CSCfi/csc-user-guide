---
tags:
  - Free
catalog:
  name: BamTools
  description: Tools for working with BAM formatted files
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# BamTools

BamTools provides both a programmer's API and an end-user's toolkit for handling
BAM files.

[TOC]

## License

Free to use and open source under the
[MIT License](https://raw.githubusercontent.com/pezmaster31/bamtools/master/LICENSE).

## Available

* Roihu: 2.5.2, via the `bio-apps` module.

## Usage

BamTools is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the BamTools module:

```bash
module load bio-apps/v202603
module load bamtools/2.5.2
```

Check the available versions with:

```bash
module spider bamtools
```

The syntax of BamTools is:

```text
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

For more information on a specific command, run:

```text
bamtools help COMMAND
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [BamTools home page](https://github.com/pezmaster31/bamtools)
