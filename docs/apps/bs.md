---
tags:
  - Free
catalog:
  name: Illumina BaseSpace
  description: Command line client for retrieving data from the Illumina BaseSpace environment
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Illumina BaseSpace

Illumina BaseSpace command line client, `bs`, can be used to retrieve data from the Illumina BaseSpace environment to Roihu.

[TOC]

## License

Software is free to use.

## Available

* Roihu: 1.7.0 

## Usage

First load the basespace module:

```bash
module load basespace
```

When module is loaded, the Illumina BaseSpace command line client starts with the command:

```bash
bs
```

To be able to use this service, you must have an account in the [Illumina BaseSpace service](https://emea.illumina.com/products/by-type/informatics-products/basespace-sequence-hub.html).

As the first step, you must set up your authentication so that you can access your data in Illumina BaseSpace. 
This is done by running the command:

```bash
bs auth
```

The authentication information is stored to your home directory on Roihu
(`$HOME/.basespace/default.cfg`). Thus, the authentication needs to be done only
once.

After that you can start working with your Illumina data. For example, available datasets can be listed with the command:

```bash
bs list datasets
```

Single dataset can be downloaded to Roihu with the command:

```bash
bs download dataset -i dataset_id -o local_download_dir
```

## More information

More detailed information about using Illumina BaseSpace client can be found form the links below:

* [bs examples](https://developer.basespace.illumina.com/docs/content/documentation/cli/cli-examples)
* [bs overview](https://developer.basespace.illumina.com/docs/content/documentation/cli/cli-overview)
