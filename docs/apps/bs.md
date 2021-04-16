
# Illumina BaseSpace

## Description

llumina BaseSpace command line client,`bs`, can be used to retrievie data from the Illumina BaseSpace environment to Puhti.

[TOC]

## License

Software is free to use.

## Available

*    bs version 1.0.0 is available in Puhti

## Usage
First load the biokit module
```text
module load biokit
```
When biokit is loaded, the Illumina BaseSpace command line client starts with command:
```text
bs
```

To be able to use this service you must have an account in the [Illumina Base Space service](https://emea.illumina.com/products/by-type/informatics-products/basespace-sequence-hub.html).

As the first step you must set up your authentication so that you can access your data in Illumina BaseSpace. 
This is done by running command:
```text
bs auth
```
The authentication information is stored to your home directory in Puhti
($HOME/.basespace/default.cfg). Thus the authentication needs to be done only
once.

After that you can start working with your Illumina data. For example, available datasets can be listed with command:
```text
bs list datasets
```

Single dataset can be downloaded to Puhtri with command:
```text
bs download dataset -i dataset_id -o local_download_dir
```

## Manual

More detailed information about using Illumne BaseSpace client can be found form the links below :

*   [bs examples](https://developer.basespace.illumina.com/docs/content/documentation/cli/cli-examples)
*   [bs overview](https://developer.basespace.illumina.com/docs/content/documentation/cli/cli-overview)

