---
tags:
  - Free
catalog:
  name: RAxML
  description: Program for inferring phylogenies with likelihood
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# RAxML

RAxML is a fast program for the inference of phylogenies with maximum likelihood method. RAxML offers several evolutionary models for both DNA and amino acid sequences.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

- Roihu: 8.2.12

## Usage

RAxML vcan be taken in use by first loading the bio-apps module:

```bash
module load bio-apps
module load raxml
```

### Which version to use?

RAxML comes in a various versions: `raxmlHPC`, `raxmlHPC-AVX`, `raxmlHPC-SSE3`, `raxmlHPC-MPI`, `raxmlHPC-MPI-AVX`, `raxmlHPC-MPI-SSE3`  

The serial version (**raxmlHPC**) is intended for small to medium datasets and for initial experiments to determine appropriate search parameters.

The MPI version (`raxmlHPC-MPI`) is for executing really large production runs (i.e. 100 or 1,000 bootstraps). You can also perform multiple inferences on larger data sets in parallel to find a best-known ML tree for your data set. Finally, the rapid BS algorithm and the associated ML search have also been parallelized with MPI.
 
The current MPI version only works properly if you specify the number of runs in the command line, since it has been designed to do multiple inferences or rapid/standard BS (bootstrap) searches in parallel. For all remaining options, the usage of this type of coarse-grained parallelism does not make much sense. Please use the `-N` option instead of the `-#` option as the latter can be mistaken for a start of a comment by the batch job system.

The are AVX-optimized binaries available (`raxmlHPC-AVX`, `raxmlHPC-MPI-AVX`). These can run faster that non-optimized versions, but can cause problems on some datasets. Try the non-optimized versions or SSE3 optimized in case of problems.

For details, please refer to the chapter "When to use which Version?" in the [RAxML manual](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf).

### Example batch job scripts

=== "Serial version for Roihu"

    ```bash
    #!/bin/bash
    #SBATCH --account=project_1234567
    #SBATCH --job-name=raxml_threads
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=8G
    #SBATCH --time=10:00:00
    #SBATCH --partition=small

    module laod bio-apps/v202603
    module load raxml/8.2.12
    raxmlHPC-HPC-AVX ­-s alg -­m GTRGAMMA ­-p 12345 ­-n test1
    ```

=== "MPI version for Roihu"

    ```bash
    #!/bin/bash
    #SBATCH --account=project_1234567
    #SBATCH --job-name=raxml_mpi
    #SBATCH --ntasks=100
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=8G
    #SBATCH --time=10:00:00
    #SBATCH --partition=small

    module laod bio-apps/v202603
    module load raxml/8.2.12
    srun raxmlHPC-MPI-AVX -N 100 -s cox1.phy -m GTRGAMMAI -p 12345 -n test2
    ```

## More information

* [RAxML home page](http://www.exelixis-lab.org/)
* [RAxML Manual](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf)
