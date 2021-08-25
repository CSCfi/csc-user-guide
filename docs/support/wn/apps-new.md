# Applications

## Turbomole 7.5.1, 25.8.2021

Turbomole 7.5.1 is now available and the default module on Puhti. The most important change with this version is that the `ricc2` module for performing 2nd order approximate coupled cluster calculations works appropriately, while older versions on Puhti have been recently reported to suffer from numerical instabilities. These issues do not apply to TM v7.5 installed on Mahti.

## CP2K 8.2, 13.8.2021

CP2K version 8.2 has been installed on Mahti and is available with `module load cp2k/8.2-omp`. This requires that `gcc/10.3.0` and `openmpi/4.1.0` are first loaded. Version `7.1-elpa` will remain the default module for now, but will be changed to `8.2-omp` in the near future (despite the name, the ELPA diagonalization library is also linked to the new 8.2 version). The `cp2k.psmp` binary of version `8.2-omp` has been tested and is roughly as efficient as `7.1-elpa`.

A list of new features and changes is found on the [CP2K website](https://www.cp2k.org/version_history). Note that some keywords, such as `MAP_CONSISTENT` in the `QS` section, have been deprecated.

## AMS 2021.102, 13.8.2021

AMS has been updated to version 2021.102 on both Mahti and Puhti and set as the default module. The [AMS documentation](../../apps/ams.md) has been updated accordingly to cover version 2021.102.

## Molpro 2021.2, 10.8.2021

Molpro 2021.2 is now available and the default version on Puhti. List of recent
changes are available on [Molpro website](https://www.molpro.net/manual/doku.php?id=recent_changes).
Our [Molpro page](../../apps/molpro.md) also contains new scalability information and an example
on how to use NVMe.

## PyTorch 1.9, 2.7.2021

PyTorch 1.9.0 is now available in the `pytorch/1.9` module on Puhti and Mahti.
The module also includes the most recent versions of TorchVision, TorchAudio and
TorchText. See the [official release
notes](https://pytorch.org/blog/pytorch-1.9-released/) for more details.

## Python Data 3.9, 22.6.2021

A new version of [Python Data](../../apps/python-data.md) is now available with
`module load python-data/3.9-1` on Puhti. It includes the most recent versions
of Scikit-learn, Pandas, JupyterLab and many other popular data analytics and
machine learning packages for Python 3.9.

This is the first version of Python Data that has been installed using
Singularity which should make loading times much faster. Thanks to wrapper
scripts this change should be mostly invisible to users. If you still encounter
any problems, don't hesitate to report them to [CSC's service
desk](../contact.md).
