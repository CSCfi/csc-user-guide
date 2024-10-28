---
tags:
  - Free
---

# MetaPhlAn



MetaPhlAn is a computational tool for profiling the composition of microbial communities from metagenomic sequencing data. 

[TOC]

## License

Free to use and open source under [MIT License](https://github.com/biobakery/MetaPhlAn2/blob/master/license.txt).

## Available

*   Puhti: 4.0.2, 4.0.3, 4.0.6

## Usage

To activate MetaPhlAn Puhti, run command:

```text
module load metaphlan
```

You can check vasic usage with command;

```text
metaphlan --help
```

MetaPhlAn can automatically retrieve the MetaPhlAn database and create the Bowtie2 
indexes it needs on-the-fly when it the command is executed. By default MetaPhlAn 
saves these index files to the MetaPhlAn installation directory, but in Puhti,
this is not possible. Because of that, the users should use option `--bowtie2db` 
to define a directory that will be used to store the database and index files. 
 
For example in the case of _project_2001234_ the user could first create a directory for the databases:

```text
cd /scratch/project_2001234
mkdir metaphlan_databases
```

Databases can be also be pre-prepared with the `--install` option:

```text
metaphlan --install --bowtie2db metaphlan_databases
```

The database is quite big and downloading and building it can take 
some time.

By default, the latest MetaPhlAn database is downloaded and built. You can download a specific version with the `--index` parameter.

```text
metaphlan --install --index mpa_vJan21_CHOCOPhlAnSGB_202103 --bowtie2db metaphlan_databases
```

When running MetaPhlan analyses you must include the `--bowtie2db` option, and also `--index`
if using non-default database. If database is not found in the indicated location, it will be automatically generated.

A test input dataset for testing MataPhlAn can be downloaded from the metaphlan github site:

```text
wget https://github.com/biobakery/MetaPhlAn/releases/download/4.0.2/SRS014476-Supragingival_plaque.fasta.gz
```

In this example the job is executed as an interactive batch job.

```text
sinteractive -m 16G -c 4
module load metaphlan
metaphlan --nproc 4 --bowtie2db metaphlan_databases  SRS014476-Supragingival_plaque.fasta.gz --input_type fasta > SRS014476-Supragingival_plaque_profile.txt
```

# More information
*   [MetaPhlAn 4 documentation](https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4)
*   [MetaPhlAn 4 tutorial](https://github.com/biobakery/biobakery/wiki/metaphlan4)
