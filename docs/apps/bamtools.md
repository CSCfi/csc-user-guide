# Bamtools

BamTools provides both a programmer's API and an end-user's toolkit for handling
BAM files.


[TOC]

## Available

-   Puhti: 2.5.1
-   Chipster graphical user interface


## Usage

In Puhti, Bamtools can be taken in use as a part of biokit module collection:

```bash
module load biokit
```
The biokit modules sets up a set of commonly used bioinformatics tools. Note however that there are bioinformatics tools in Puhti,
 that have a separate setup commands.

The syntax of bamtools is:
``` 
bamtools COMMAND  ARGUMENTS
```
Available bamtools commands:

-  **convert**        Converts between BAM and a number of other formats
-  **count**           Prints number of alignments in BAM file(s)
-  **coverage**        Prints coverage statistics from the input BAM file
-  **filter**          Filters BAM file(s) by user-specified criteria
-  **header**          Prints BAM header information
-  **index**           Generates index for BAM file
-  **merge**           Merge multiple BAM files into single file
-  **random**          Select random alignments from existing BAM file(s), intended more as a testing tool.
-  **resolve**         Resolves paired-end reads (marking the IsProperPair flag as needed)
-  **revert**          Removes duplicate marks and restores original base qualities
-  **sort**            Sorts the BAM file according to some criteria
-  **split**           Splits a BAM file on user-specified property, creating a new BAM output file for each value found
-  **stats**           Prints some basic statistics from input BAM file(s)

For more information on a specific command, run command:

```
bamtools help COMMAND
```

## Support

servicedesk@csc.fi

## Manual

More information about Bamtoos can be found from the [Bamtools home page](https://github.com/pezmaster31/bamtools).

