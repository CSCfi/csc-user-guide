---
tags:
  - Free
catalog:
  name: Nextflow
  description: Nextflow is a scientific workflow management system for creating scalable, portable, and reproducible workflows
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Nextflow

Nextflow is a scientific workflow management system for creating scalable,
portable, and reproducible workflows. It is a groovy-based language for expressing the entire workflow in a single script and also supports running scripts (via script/run/shell directive of Snakemake rule) from other languages such as R, bash and Python. 


[TOC]

## Available 

Versions available on CSC's servers

* Puhti: 21.10.6, 22.04.5, 22.10.1, 23.04.3, 24.01.0-edge.5903, 24.10.0
* Mahti: 22.05.0-edge, 24.04.4
* LUMI: 22.10.4

!!! info "Pay attention to usage of Nextflow version"
    Please note that the nextflow version starting from 23.04.3 can only be
    used for pipelines built with DSL2. You can downgrade to lower versions
    for DSL1-compliant pipelines.

## License

Nextflow is released under the
[Apache 2.0 license](https://github.com/nextflow-io/nextflow/blob/master/COPYING).

## Usage

!!! info "Nextflow on LUMI"
    To access CSC modules on LUMI, remember to first load the CSC module tree
    into use with

    ```bash
    module use /appl/local/csc/modulefiles
    ```

Nextflow is activated by loading `nextflow` module:

```bash
module load nextflow
```

The default version is usually the latest. Choose the version of the Nextflow depending on the requirements of your own pipeline. It is recommended to load Nextflow module with a version, for the reproducibility point of view.  To load `nextflow` module with a specific version:

```bash
module load nextflow/22.04.5
```

For usage help, use command:

```bash
nextflow -h
```

More detailed instructions can be found in
[CSC's Nextflow tutorial](../support/tutorials/nextflow-tutorial.md).

## References

If you use Nextflow in your work, please cite:

Di Tommaso, P., Chatzou, M., Floden, E. et al. Nextflow enables reproducible
computational workflows. Nat. Biotechnol. 35, 316–319 (2017).
<https://doi.org/10.1038/nbt.3820>

## More information

* [Nextflow official documentation](https://www.nextflow.io/docs/latest/index.html)
* [CSC Nextflow tutorial](../support/tutorials/nextflow-tutorial.md)
