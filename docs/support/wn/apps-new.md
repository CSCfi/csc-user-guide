# Applications

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
