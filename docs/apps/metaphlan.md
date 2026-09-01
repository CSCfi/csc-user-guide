---
tags:
  - Free
catalog:
  name: MetaPhlAn
  description: Profiling the composition of microbial communities with metagenomic data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MetaPhlAn

MetaPhlAn is a computational tool for profiling the composition of microbial communities from metagenomic sequencing data. 

[TOC]

## License

Free to use and open source under [MIT License](https://github.com/biobakery/MetaPhlAn2/blob/master/license.txt).

## Available

* Roihu: 4.2.4 (module `py-metaphlan`), via the `bio-apps` module.

## Usage

MetaPhlAn is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MetaPhlAn module:

```bash
module load bio-apps/v202603
module load py-metaphlan/4.2.4
```

You can check basic usage with command:

```bash
metaphlan --help
```

### Database

MetaPhlAn can automatically retrieve the MetaPhlAn database and create the Bowtie2 
indexes it needs on-the-fly when the command is executed. By default MetaPhlAn 
saves these index files to the MetaPhlAn installation directory, but on Roihu
this installation is read-only, so this is not possible. Because of that, users should use the option `--bowtie2db` 
to define a directory that will be used to store the database and index files.

!!! info "Shared reference databases"
    CSC plans to provide shared reference databases at a central location on Roihu.
    This is still being set up. Until it is available, download and use your own
    copy as shown below.

For example, the user could first create a directory for the databases in their project's `/scratch`:

```bash
cd /scratch/<project>
mkdir metaphlan_databases
```

Databases can be also be pre-prepared with the `--install` option:

```bash
metaphlan --install --bowtie2db metaphlan_databases
```

The database is quite big and downloading and building it can take 
some time.

By default, the latest MetaPhlAn database is downloaded and built. You can download a specific version with the `--index` parameter.

```bash
metaphlan --install --index mpa_vJan21_CHOCOPhlAnSGB_202103 --bowtie2db metaphlan_databases
```

When running MetaPhlAn analyses you must include the `--bowtie2db` option, and also `--index`
if using a non-default database. If the database is not found in the indicated location, it will be automatically generated.

A test input dataset for testing MetaPhlAn can be downloaded from the MetaPhlAn github site:

```bash
wget https://github.com/biobakery/MetaPhlAn/releases/download/4.0.2/SRS014476-Supragingival_plaque.fasta.gz
```

In this example the job is executed as an interactive job. On the Roihu `interactive`
partition each reserved core provides 1.875 GB of memory (up to 32 cores / 60 GB /
36 hours), so request the number of cores that gives you enough memory — here 8 cores
(about 15 GB):

```bash
sinteractive --account <project> --cores 8
module load bio-apps/v202603
module load py-metaphlan/4.2.4
metaphlan --nproc 8 --bowtie2db metaphlan_databases SRS014476-Supragingival_plaque.fasta.gz --input_type fasta > SRS014476-Supragingival_plaque_profile.txt
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

*   [MetaPhlAn 4 documentation](https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4)
*   [MetaPhlAn 4 tutorial](https://github.com/biobakery/biobakery/wiki/metaphlan4)
