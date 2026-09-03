---
tags:
  - Free
catalog:
  name: Cutadapt
  description: Trimming high-throughput sequencing reads
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Cutadapt

Cutadapt finds and removes adapter sequences, primers, poly-A tails and other types of 
unwanted sequence from your high-throughput sequencing reads.

[TOC]

## License

Free to use and open source under [MIT License](https://github.com/marcelm/cutadapt/blob/main/LICENSE)

## Available

- Roihu: 5.1.0

## Usage

On Roihu, Cutadapt can be taken in use by loading the module:

```bash
module load cutadapt
```

You can check the available versions with the command:

```bash
module spider cutadapt
```

You can load a specific version with the command:

```bash
module load cutadapt/5.1.0
```

The basic syntax is:

```bash
cutadapt --help
```

Cutadapt should be run either in an interactive session or as a batch job.

## Support

[CSC Service Desk](../support/contact.md)

## More information

- [Cutadapt home page](https://cutadapt.readthedocs.io/en/stable/).
