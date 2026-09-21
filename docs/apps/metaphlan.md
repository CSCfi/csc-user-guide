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

Free to use and open source under [MIT License](https://github.com/biobakery/MetaPhlAn/blob/master/license.txt).

## Available

* Roihu: 4.2.4 (module `py-metaphlan`), via the `bio-apps` module.

## Usage

MetaPhlAn is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the MetaPhlAn module:

```bash
module load bio-apps/v202603
module load py-metaphlan/4.2.4
```

You can check basic usage with the command:

```bash
metaphlan --help
```

### Database

MetaPhlAn needs a marker database (the ChocoPhlAn-SGB Bowtie2 indexes) to run.
On Roihu a shared, read-only copy is provided centrally, and the `py-metaphlan`
module points MetaPhlAn at it automatically through the `$METAPHLAN_DB_DIR`
environment variable — so for the bundled database versions you do **not** need
to pass `--db_dir`.

The following database versions are available in the shared location:

* `mpa_vJan26_CHOCOPhlAnSGB_202605` (latest)
* `mpa_vJun23_CHOCOPhlAnSGB_202403`

They sit side by side in one folder; choose which one to use with `--index` (its
value must be one of the versions listed above):

```bash
metaphlan --index mpa_vJan26_CHOCOPhlAnSGB_202605 ...
```

#### Using your own database

To use a version that is not in the shared location — or to let MetaPhlAn
download and build a fresh database — point `--db_dir` at a **writable**
directory of your own. An explicit `--db_dir` overrides `$METAPHLAN_DB_DIR`, and
because the shared copy is read-only MetaPhlAn cannot create a missing index
there.

For example, create a directory for the databases in your project's `/scratch`:

```bash
cd /scratch/<project>
mkdir metaphlan_databases
```

Databases can be pre-prepared with the `--install` option:

```bash
metaphlan --install --db_dir metaphlan_databases
```

The database is quite big and downloading and building it can take some time.

By default the latest MetaPhlAn database is downloaded and built. You can request
a specific version with the `--index` parameter:

```bash
metaphlan --install --index mpa_vJan21_CHOCOPhlAnSGB_202103 --db_dir metaphlan_databases
```

If the requested database is not found in the indicated writable location, it
will be generated automatically.

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
metaphlan --nproc 8 --index mpa_vJan26_CHOCOPhlAnSGB_202605 SRS014476-Supragingival_plaque.fasta.gz --input_type fasta > SRS014476-Supragingival_plaque_profile.txt
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

*   [MetaPhlAn 4 documentation](https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4)
*   [MetaPhlAn 4 tutorial](https://github.com/biobakery/biobakery/wiki/metaphlan4)
