---
tags:
  - Free
---

# Nextflow

## Description

Nextflow is a scientific workflow management system for creating scalable, portable, and reproducible workflows. 

[TOC]

## License

Nextflow is released under the [Apache 2.0 license](https://github.com/nextflow-io/nextflow/blob/master/COPYING).

## Available 

Version on CSC's Servers

* Puhti: 21.10.6, 22.04.5, 22.10.1  and  23.04.3
* Mahtii: 21.10.6
  <br>


!!! info "Pay attention to usage of Nextflow version"

    Please note that nextflow version starting from 23.04.3 onwards can only be for pipelines built with DSL2. You can downgrade to lower versions for workflows that are built with DSL1
 

## Usage

In Puhti/Mahti, Nextflow is activated by loading nextflow module as below:

```text
module load nextflow
```
Usage of nextflow module with a specific version:

```text
module load nextflow/22.04.5
```

For usage help use command:
```text
nextflow -h
```
More detailed instructions can be found on [CSC documentation](https://docs.csc.fi/support/tutorials/nextflow-puhti/)

## Manual

*   [Nextflow documentation](https://www.nextflow.io/docs/latest/index.html)

## Support

servicedesk@csc.fi


