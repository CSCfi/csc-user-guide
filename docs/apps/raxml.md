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

* Roihu: 8.2.12, via the `bio-apps` module.

## Usage

RAxML is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the RAxML module:

```bash
module load bio-apps/v202603
module load raxml/8.2.12
```

To see the installed RAxML versions, use the command:

```bash
module spider raxml
```

### Which version to use?

RAxML comes in a serial version and three different parallel versions.

The serial version (**raxmlHPC**) is intended for small to medium datasets and for initial experiments to determine appropriate search parameters.

The PThreads version (`raxmlHPC-PTHREADS`) will work well for very long alignments. Make sure to specify the number of threads with the `-T` option. This should match the number of cores you request in the batch job script.

To choose the number of threads to use, please see section "How many Threads shall I use?" in the [RAxML manual](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf). Using too many threads can cause the program to run slower.

The MPI version (`raxmlHPC-MPI`) is for executing really large production runs (i.e. 100 or 1,000 bootstraps). You can also perform multiple inferences on larger data sets in parallel to find a best-known ML tree for your data set. Finally, the rapid BS algorithm and the associated ML search have also been parallelized with MPI.
 
The current MPI version only works properly if you specify the number of runs in the command line, since it has been designed to do multiple inferences or rapid/standard BS (bootstrap) searches in parallel. For all remaining options, the usage of this type of coarse-grained parallelism does not make much sense. Please use the `-N` option instead of the `-#` option as the latter can be mistaken for a start of a comment by the batch job system.

For versions 8.2.12 and newer there is also a hybrid MPI/threaded version (`raxmlHPC-HYBRID`)

For versions 8.2.12 and newer there are also AVX-optimized binaries available (`raxmlHPC-AVX`, `raxmlHPC-PTHREADS-AVX`, `raxmlHPC-MPI-AVX`, `raxmlHPC-HYBRID-AVX`). These can run faster that non-optimized versions, but can cause problems on some datasets. Try the non-optimized versions in case of problems.

For details, please refer to the chapter "When to use which Version?" in the [RAxML manual](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf).

### Example batch job scripts

=== "PThreads version"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --job-name=raxml_threads
    #SBATCH --partition=small
    #SBATCH --time=10:00:00
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=4
    #SBATCH --mem=8G

    module load bio-apps/v202603
    module load raxml/8.2.12

    raxmlHPC-PTHREADS -T $SLURM_CPUS_PER_TASK -s alg -m GTRGAMMA -p 12345 -n test1
    ```

=== "MPI version"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --job-name=raxml_mpi
    #SBATCH --partition=small
    #SBATCH --time=10:00:00
    #SBATCH --ntasks=100
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=2G

    module load bio-apps/v202603
    module load raxml/8.2.12

    srun raxmlHPC-MPI -N 100 -s cox1.phy -m GTRGAMMAI -p 12345 -n test2
    ```

The MPI example above runs 100 ranks within the single-node `small` partition. For
larger, multi-node runs you can use the `large` partition, which requires a
completed [scalability test](../accounts/how-to-access-roihu-large-partition.md).

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [RAxML home page](http://www.exelixis-lab.org/)
* [RAxML Manual](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf)
