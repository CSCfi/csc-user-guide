# Applications

## Python Data default module now uses Singularity, 26.11.2021

The default version of the `python-data` module has been changed to `3.9-1`.
This means that if you have been simply doing `module load python-data` you will
now get this new version automatically. This version has been installed using
Singularity which should make loading times much faster. Thanks to wrapper
scripts this change should be mostly invisible to users. If you still encounter
any problems, don't hesitate to report them to [CSC's service
desk](../contact.md).

## Schrödinger Maestro 2021.4, 24.11.2021

Schrödinger Maestro 2021.4 has been installed on Puhti and set as the default module.

## PyTorch 1.10, 10.11.2021

PyTorch 1.10.0 is now available in the `pytorch/1.10` module on Puhti and Mahti,
and has been set as the default module. See the [official PyTorch 1.10 release
notes](https://pytorch.org/blog/pytorch-1.10-released/) for more details. CSC's
module has the following improvements:

- Jupyter Lab now works (previously only regular Jupyter Notebook UI worked)
- [DeepSpeed](https://www.deepspeed.ai/) support built in (experimental support)

## TensorFlow 2.7, 9.11.2021

TensorFlow 2.7.0 is now available in the `tensorflow/2.7` module on Puhti and
Mahti, and has been set as the default module. See the [TensorFlow 2.7 release
notes on GitHub](https://github.com/tensorflow/tensorflow/releases/tag/v2.7.0/)
for more details. CSC's module has the following improvements:

- Jupyter Lab now works (previously only regular Jupyter Notebook UI worked)

## Schrödinger Maestro 2021.3, 30.8.2021

Schrödinger Maestro 2021.3 has been installed on Puhti and set as the default module. The [extended Maestro instructions](../tutorials/power-maestro.md#quantum-espresso) have been appended with a section on how to speed up Quantum Espresso jobs. A bug in the script that generates the `schrodinger.hosts` file has also been fixed by setting the `parallel` HOST entry to use the `large` Slurm partition as intended.

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
