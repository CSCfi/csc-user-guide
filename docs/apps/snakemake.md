---
tags:
  - Free
---

# Snakemake

Snakemake is a Python-based scientific workflow management system for creating scalable, portable, and reproducible workflows. It is one of 
the popular workflow managers within the bioinformatics community, but
is not specific to bioinformatics. Like in [Nextflow](../apps/nextflow.md), Snakemake also supports running scripts (via script/run/shell directive of Snakemake rule) from other languages such as R, bash and Python.

[TOC]

## Available 

Versions available at CSC:

* Puhti: 7.15.2, 7.17.1, 8.4.6

## License

Snakemake is released under the
[MIT License](https://snakemake.readthedocs.io/en/stable/project_info/license.html).

## Usage

Snakemake is activated by loading `snakemake` module as below:

```bash
module load snakemake
```

Example of loading `snakemake` module with a specific version:

```bash
module load snakemake/8.4.6
```

For usage help, use command:

```bash
snakemake --help
```

Please refer to our tutorial on [running Snakemake workflow on Puhti](../support/tutorials/snakemake-puhti.md) for more details.

## Installation

The latest version of snakemake (v8.4.6) was installed on Puhti using virtual environment *via* pip3. See a [list of the python packages used in this module ](https://github.com/yetulaxman/containers-workflows/blob/master/snakemake_pip_hpc.yaml).


## References

If you use Snakemake in your work, please cite:

> Mölder, F., Jablonski, K.P., Letcher, B., Hall, M.B., Tomkins-Tinch, C.H., Sochat, V.,
  Forster, J., Lee, S., Twardziok, S.O., Kanitz, A., Wilm, A., Holtgrewe, M., Rahmann, S.,
  Nahnsen, S., Köster, J. Sustainable data analysis with Snakemake. F1000Research 2021,
  <https://doi.org/10.12688/f1000research.29032.1>.

## More information

* [Snakemake official documentation](https://snakemake.readthedocs.io/en/stable/index.html)
* [How to run Snakemake workflow on Puhti](../support/tutorials/snakemake-puhti.md)
* [CSC Snakemake Hackathon 2024](https://coderefinery.github.io/snakemake_hackathon/)
* [Contact CSC Service Desk for technical support](../support/contact.md)

