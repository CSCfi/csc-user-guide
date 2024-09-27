# Applications

## CSC chemistry software stack on LUMI updated, 26.9.2024

The chemistry software stack maintained by CSC on LUMI
(`/appl/local/csc/soft/chem`) has been recompiled following the recent major
LUMI upgrade. Modules and instructions for the following software have been
updated:

* [Amber](../../apps/amber.md)
* [CP2K](../../apps/cp2k.md)
* [GROMACS](../../apps/gromacs.md)
* [LAMMPS](../../apps/lammps.md)
* [NAMD](../../apps/namd.md)

At the same time, some old module versions have been deprecated. In general, we
recommend using the most recent software versions as they tend to have better
performance and less bugs than older releases.

## PyTorch 2.4.1 available on LUMI, 19.9.2024

PyTorch 2.4.1 with ROCm 6.1 is now available on LUMI. The LUMI PyTorch
module now includes [vLLM version 0.5.5](https://docs.vllm.ai/en/latest/) 
in addition to FlashAttention-2, bitsandbytes and many other frequently 
requested packages already added included in earlier installations.  See our
[PyTorch module documentation for more information](../../apps/pytorch.md#available).

## GROMACS 2024.3, 12.9.2024

[GROMACS](../../apps/gromacs.md) 2024.3 is now available on Puhti and Mahti. See
[release notes](https://manual.gromacs.org/2024.3/release-notes/2024/2024.3.html)
for a list of all new features and improvements.

## JAX 0.4.30 available on Puhti and Mahti, 5.9.2024

[JAX](../../apps/jax.md) 0.4.30 has been installed on Puhti and Mahti
and set as the default version.

The `transformers` package is no longer included since it officially 
only supports JAX up to version 0.4.13.

From this version on, there will be "small" and "full" flavours of JAX,
where the "full" flavour includes JAX ML ecosystem packages as before
while the "small" flavour includes only JAX with GPU support as well as
CPU-only versions of Tensorflow and PyTorch for their data loading and
processing utilities but no additional packages. You can use the latter
if you want a cleaner base to install additional packages on.

The LUMI installation will be delayed until early autumn due to the
ongoing system update and changes to the relevant system driver versions.

## CP2K 2024.2 available on Puhti and Mahti, 27.8.2024

[CP2K](../../apps/cp2k.md) 2024.2 has been installed and set as the default
module on Puhti and Mahti. See
[release notes](https://github.com/cp2k/cp2k/releases/tag/v2024.2)
for a list of new features, fixes and breaking changes.

## ORCA 6.0.0, 22.8.2024

[ORCA](../../apps/orca.md) 6.0.0 is now available on Puhti and Mahti. This major
release brings numerous new features and enhancements. For full details, check out
the [ORCA 6 Changes](https://www.faccts.de/docs/orca/6.0/manual/contents/changes.html).

## PyTorch 2.4.0, 21.8.2024

[PyTorch](../../apps/pytorch.md) 2.4.0 added to Puhti and Mahti. The
LUMI installation will be delayed until after the current service
break. The torchtext package is no longer included as it has been
deprecated and no longer works with PyTorch 2.4. See our [PyTorch
module documentation for more information](../../apps/pytorch.md#available).

## AMS 2024 available on Puhti and Mahti, 20.8.2024

[AMS](../../apps/ams.md) has been updated to version 2024.102 on both Mahti and Puhti
and set as the default module. The [AMS2024 release notes](https://www.scm.com/downloads/release-notes-amsterdam-modeling-suite-2024/)
summarize major changes and improvements since AMS2023.

## Geoconda 3.11.9, 7.8.2024

[geoconda](../../apps/geoconda.md) version 3.11.9 has been added
and set as the default module on Puhti and Mahti. Besides package updates, it includes a few new packages: `geo2ml`, `h3pandas`, `openeo`, `pcraster` and `r5py`. From packages available in previous geoconda, `copc-lib` and `osmnx` unfortunately could not be added this time.

## Schrödinger Maestro 2024.3, 5.8.2024

[Schrödinger Maestro](../../apps/maestro.md) version 2024.3 has been installed
and set as the default module on Puhti and Mahti. As a major highlight, this
release includes the new OPLS5 polarizable force field. See
[release notes](https://www.schrodinger.com/life-science/download/release-notes/)
for the full list of new features and improvements.

## PyTorch 2.3.1, 13.6.2024

[PyTorch](../../apps/pytorch.md) 2.3.1 added to Puhti and Mahti. The
LUMI installation will be delayed until early autumn due to an
incompatible ROCm driver version. This version has also updated how
Python commands are wrapped, as this solves several problems with
using virtual environments and Jupyter Notebooks. Due to this
`apptainer` and `apptainer_wrapper` commands will no longer work, but
otherwise the change should be invisible to users. See our [PyTorch
module documentation for more
information](../../apps/pytorch.md#available).

## Python Data 3.10-24.04 now the default version

The recently installed `python-data/3.10-24.04` has been set as the
default version for [Python Data](../../apps/python-data.md).

## R 4.4.0 in r-env, 7.6.2024

R version 4.4.0 is now available in `r-env` in Puhti and is set as the default version. The new version will be available in RStudio in the Puhti web interface shortly.

## Molpro 2024.1 is available on Puhti, 5.6.2024

The new [Molpro 2024.1](../../apps/molpro.md) includes new features like
a CAS(2,2) version of icMRCCSD. Check the
[Recent changes](https://www.molpro.net/manual/doku.php?id=recent_changes)
for a detailed list of new features, bug fixes and improvements.

## GROMACS 2024.2, 22.5.2024

[GROMACS](../../apps/gromacs.md) 2024.2 is now available on Puhti, Mahti and LUMI.
New GPU versions on LUMI have been compiled to use the instant submission mode of
AdaptiveCpp, which can improve performance and scalability in some cases by more
than 10%. See [release notes](https://manual.gromacs.org/2024.2/release-notes/2024/2024.2.html)
for a list of all new features and improvements.

## Schrödinger Maestro 2024.2, 3.5.2024

[Schrödinger Maestro](../../apps/maestro.md) version 2024.2 has been installed
and set as the default module on Puhti and Mahti. See
[release notes](https://www.schrodinger.com/life-science/download/release-notes/)
for a list of new features and improvements.

## AMS 2023 available on Puhti and Mahti, 21.3.2024

[AMS](../../apps/ams.md) has been updated to version 2023.104 on both Mahti and Puhti
and set as the default module. The corresponding [AMS-GUI](../../apps/ams-gui.md)
is also updated.

## GROMACS 2024.1, 21.3.2024

[GROMACS](../../apps/gromacs.md) 2024.1 is now available on Puhti, Mahti and LUMI.
See [release notes](https://manual.gromacs.org/2024.1/release-notes/2024/2024.1.html)
for a list of new features and improvements.

## CP2K 2024.1 available on Puhti, Mahti and LUMI, 20.3.2024

[CP2K](../../apps/cp2k.md) 2024.1 has been installed and set as the default
module on Puhti, Mahti and LUMI. See
[release notes](https://github.com/cp2k/cp2k/releases/tag/v2024.1)
for a list of new features, fixes and breaking changes. As a notable change,
calculations will now abort instead of just issuing a warning if the SCF cycle
fails to converge. Add `IGNORE_CONVERGENCE_FAILURE` keyword in the `&SCF`
section to enable the old behavior.

## NAMD 3.0b6 available on LUMI, 12.3.2024

The latest AMD GPU-enabled version of NAMD is now available pre-installed
on LUMI. See our [NAMD page](../../apps/namd.md) for batch script examples
and performance notes, as well as the
[NAMD website](https://www.ks.uiuc.edu/Research/namd/3.0/features.html)
for a list of new features that improve the performance of single-node
multi-GPU simulations.

## JAX 0.4.23, 6.3.2024

[JAX](../../apps/jax.md) 0.4.23 was added to Puhti, Mahti and LUMI.
JAX modules now also include a CPU-only installation of PyTorch,
which sometimes used together with JAX for its data loading capabilities,
as well as relevant updates to all Python packages already bundled in the
previous JAX modules.

## PyTorch 2.2.1, 1.3.2024

[PyTorch](../../apps/pytorch.md) 2.2.1 added to Puhti, Mahti and
LUMI. The LUMI module includes ROCm versions of
[FlashAttention-2](https://github.com/ROCm/flash-attention) and
[bitsandbytes](https://github.com/ROCm/bitsandbytes) as these are
difficult for users to add themselves.
[xFormers](https://github.com/facebookresearch/xformers) has been
added to all three systems in addition to new versions of all
previously supported packages (e.g., DeepSpeed and Transformers).

## Snakemake, 23.2.2024

An [application page for the Snakemake workflow tool](../../apps/snakemake.md)
has been added to Docs CSC. Check it out, as well as the accompanying tutorial
on [how to use Snakemake efficiently on Puhti](../tutorials/snakemake-puhti.md).

## GROMACS 2024.0, 16.2.2024

[GROMACS](../../apps/gromacs.md) 2024.0 is now available on Puhti, Mahti and LUMI. See
[release notes](https://manual.gromacs.org/2024.0/release-notes/2024/major/highlights.html)
for a list of new features and improvements. Notably, the GPU-enabled module on LUMI
now uses a more recent version of ROCm (5.6.1) and AdaptiveCPP (23.10.0) with improved
performance.

## TmoleX 2024, 9.2.2024

[TmoleX](../../apps/tmolex.md) has been updated and is now also available via
the web interface on Puhti. 

## TURBOMOLE 7.8, 8.2.2024

[TURBOMOLE](../../apps/turbomole.md) version 7.8 has been installed
and set as the default module on Puhti and Mahti. See
[release notes](https://www.turbomole.org/turbomole/release-notes-turbomole-7-8/)
for a list of new features and improvements.

## Schrödinger Maestro 2024.1, 8.2.2024

[Schrödinger Maestro](../../apps/maestro.md) version 2024.1 has been installed
and set as the default module on Puhti and Mahti. See
[release notes](https://newsite.schrodinger.com/life-science/download/release-notes/)
for a list of new features and improvements.

## ORCA 5.0.4, 7.2.2024

[ORCA](../../apps/orca.md) 5.0.4 is now available on Puhti and Mahti. It's a bugfix release including corrections for the bug in the D4 implementation.
Please note the change in how it's launched in a batch script. 

## R 4.3.2 in r-env, 2.2.2024
	
R version 4.3.2 is now available in [r-env](../../apps/r-env.md) and is set as the default version. The new version will also be available in RStudio in the Puhti web interface shortly.

## COSMO-RS, 30.1.2024

[COSMO-RS](../../apps/cosmors.md) is a new tool for modelling fluid phase properties,
based on quantum chemistry derived properties. 
It consists of the BIOVIA COSMOsuite toolbox and can be utilized in combination with
[TURBOMOLE](../../apps/turbomole.md).

## Python Data 3.10-23.11, 28.11.2023

A new version of [Python Data](../../apps/python-data.md)
`python-data/3.10-23.11` has been installed, with the newest versions
of popular data analytics packages.

## Gromacs 2023.3, 17.11.2023

[Gromacs](../../apps/gromacs.md) 2023.3 is now available on Puhti, Mahti and
LUMI. See [release notes](https://manual.gromacs.org/current/release-notes/2023/2023.3.html)
for a list of new features and improvements. The naming of Gromacs modules on
LUMI has also been changed due to hipSYCL changing its name to
[AdaptiveCpp](https://github.com/AdaptiveCpp/AdaptiveCpp). Henceforth,
GPU-enabled modules on LUMI are simply suffixed with `-gpu` to avoid confusion.

## PyTorch 2.1 and TensorFlow 2.14, 13.11.2023

[PyTorch](../../apps/pytorch.md) 2.1 and
[TensorFlow](../../apps/tensorflow.md) 2.14 are now available on Puhti and Mahti. 
See [PyTorch 2.1 blog post](https://pytorch.org/blog/pytorch-2-1/) or the
[TensorFlow 2.14 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.14.0).

## Schrödinger Maestro 2023.4, 10.11.2023

[Schrödinger Maestro](../../apps/maestro.md) version 2023.4 has been installed
and set as the default module on Puhti and Mahti. See
[release notes](https://www.schrodinger.com/releases/new-features/) for a list
of new features and improvements.

## Molpro 2023.2 is available on Puhti, 31.10.2023

The new [Molpro 2023.2](../../apps/molpro.md) includes new features like
unrestricted coupled cluster and the PQS geometry optimizer. Check the
[Recent changes](https://www.molpro.net/manual/doku.php?id=recent_changes)
for a detailed list of new features and improvements.

## AlphaFold Genetic databases available on Puhti, 20.10.2023

Genetic databases for AlphaFold 2.3.2-1 now available on Puhti. See
[AlphaFold application page](../../apps/alphafold.md) for details.

## Schrödinger Maestro 2023.3, 8.9.2023

Schrödinger Maestro version 2023.3 has been installed and set as the default module on
Puhti and Mahti. See [release notes](https://www.schrodinger.com/releases/new-features/)
for a list of new features and improvements.

## CP2K 2023.2 available on Puhti and Mahti, 1.9.2023

[CP2K](../../apps/cp2k.md) 2023.2 has been installed and set as the default
module on Puhti and Mahti. For release notes and more details about the version,
see [the CP2K website](https://www.cp2k.org/version_history#section20232).

## CSD 2023.2 available on Puhti, 22.8.2023

Version 2023.2 of the [Cambridge Structural Database (CSD)](../../apps/csd.md) software
suite (including [GOLD](../../apps/gold.md)) has been installed and set as the default
module on Puhti. [See release notes here](https://www.ccdc.cam.ac.uk/solutions/whats-new/).

## Gromacs 2023.2 available on Puhti and Mahti, 21.8.2023

[Gromacs](../../apps/gromacs.md) 2023.2 has been installed and set as the default module on
Puhti and Mahti.
[See release notes here](https://manual.gromacs.org/2023.2/release-notes/2023/2023.2.html).

## Gromacs 2023.2 and CP2K 2023.2 available on LUMI, 4.8.2023

CPU and GPU versions of [Gromacs](../../apps/gromacs.md) 2023.2 and [CP2K](../../apps/cp2k.md)
2023.2 have been installed on LUMI. For release notes and more details about the version, see
the [GROMACS manual](https://manual.gromacs.org/2023.2/release-notes/2023/2023.2.html) and
[the CP2K website](https://www.cp2k.org/version_history#section20232).

## R 4.3.0 in r-env, 20.6.2023
	
R version 4.3.0 is now available in `r-env` and is set as the default version. The new version will also be available in RStudio in the Puhti web interface shortly.

## Gromacs 2023.1 available on LUMI, 7.6.2023

CPU and GPU versions of Gromacs 2023.1 have been installed on LUMI. Notably, the
GPU-enabled module is the official hipSYCL version, which has improved significantly
in terms of performance since the previous releases. The LUMI-G instructions on the
[Gromacs application page](../../apps/gromacs.md#lumi)
have also been updated and the
[tutorial on running multi-simulations](../tutorials/gromacs-throughput.md)
using the built-in `multidir` feature extended and adapted for LUMI-G.

## R 4.2.2 in r-env, 26.5.2023
	
R version 4.2.2 is now available in `r-env` and is set as the default version. The new version will also be available in RStudio in the Puhti web interface shortly.

## Schrödinger Maestro 2023.2, 25.5.2023

Schrödinger Maestro version 2023.2 has been installed and set as the default module on
Puhti and Mahti. See [release notes](https://www.schrodinger.com/releases/new-features/)
for a list of new features and improvements.

## NoMachine will no longer be available on CSC's supercomputers, 9.5.2023

The NoMachine remote desktop service will be discontinued on 25th May 2023, at the end of the
current licensing period. The service is superseded by web interfaces on CSC's supercomputers. The
first of them, [Puhti web interface](../../computing/webinterface/index.md), has been liked by the
researchers, the number of users is still rapidly increasing and now represents 36% of all users.
Similar web interfaces will be opened for both Mahti and LUMI, in the near future. For replacements
in specific use cases, please see
[the application page for NoMachine](../../apps/nomachine.md#replacements).

## Gromacs and CP2K now available on LUMI, 19.4.2023

CPU and GPU-enabled versions of [Gromacs](../../apps/gromacs.md) and [CP2K](../../apps/cp2k.md)
have been installed on LUMI. Before loading the modules, first take the CSC module tree into
use with `module use /appl/local/csc/modulefiles`. Note that the GPU-enabled Gromacs version
is an unofficial HIPified fork of the software by AMD and hence unsupported by the upstream
developers.

## PyTorch 2.0 and TensorFlow 2.12, 27.3.2023

[PyTorch](../../apps/pytorch.md) 2.0 and
[TensorFlow](../../apps/tensorflow.md) 2.12 are now available on Puhti and Mahti. 
See [PyTorch 2.0 blog post](https://pytorch.org/blog/pytorch-2.0-release/) or the
[TensorFlow 2.12 release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.12.0).

## Turbomole 7.7, 3.3.2023

[Turbomole](../../apps/turbomole.md) 7.7 has been installed and set as the default module on Puhti
and Mahti. [See release notes here](https://www.turbomole.org/turbomole/release-notes-turbomole-7-7/).

## Schrödinger Maestro 2023.1 and module removal policy, 10.2.2023

* The latest version of [Schrödinger Maestro](../../apps/maestro.md) (v2023.1)
  has been installed and set as the default module on CSC supercomputers.
  See [release notes](https://www.schrodinger.com/releases/new-features/)
  for a list of new features and improvements.
* Henceforth, a two-year cleaning cycle is applied on the Maestro modules on CSC
  supercomputers. Specifically, module versions older than two years will be removed
  in order to free up disk space and encourage use of the latest versions which tend
  to be more performant and have less bugs.

## CSC software collection on LUMI, 31.1.2023

Applications pre-installed by CSC on the LUMI supercomputer can now be viewed in the
[application list grouped by availability](../../apps/by_system.md). For a comprehensive
list of available EasyBuild recipes for personal or project-specific installations, see
the [LUMI Software Library](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/).

## CP2K 2023.1, 30.1.2023

[CP2K](../../apps/cp2k.md) 2023.1 has been installed and set as the default module on Puhti
and Mahti. [See release notes here](https://www.cp2k.org/version_history).

## Gromacs 2022.4, 16.1.2023

[Gromacs](../../apps/gromacs.md) 2022.4 has been installed and set as the default module on Puhti
and Mahti. [See release notes here](https://manual.gromacs.org/2022.4/release-notes/2022/2022.4.html).

## License for Materials and Discovery Studio no longer available, 3.1.2023

The national [Materials Studio](../../apps/materialsstudio.md) and
[Discovery Studio](../../apps/discovery-studio.md) licenses provided by CSC ended at the end of 2022.
Please consider using, e.g., [Maestro](../../apps/maestro.md) or [AMS](../../apps/ams.md)
instead.

## sbatch-hq, 19.12.2022

A wrapper for HyperQueue called `sbatch-hq` has been created to enable easy and efficient
task farming, *i.e.* high-throughput computing workflows where the intention is to run many
similar (non-MPI parallel, independent) commands/programs. [See the HyperQueue page for more
details](../../apps/hyperqueue.md#sbatch-hq).

## PyTorch 1.13, 9.12.2022

PyTorch 1.13.0 is now available in the `pytorch/1.13` module on Puhti
and Mahti, and has been set as the default version. See the [PyTorch
1.13 release blog
post](https://pytorch.org/blog/PyTorch-1.13-release/), and [CSC's
PyTorch module documentation](../../apps/pytorch.md).

## Amber22 installed on Puhti, 16.11.2022

[Amber](../../apps/amber.md) version 22 has been installed on Puhti and set as the default
module. [See here for a list of major new features](https://ambermd.org/AmberMD.php).

## Maestro 2022.3 and 2022.4 installed on Puhti, 15.11.2022

[Schrödinger Maestro](../../apps/maestro.md) 2022.3 and 2022.4 have been
installed on Puhti and the latter version set as the default module. [See
release notes here](https://www.schrodinger.com/releases/new-features/).

## CP2K 2022.2, 10.11.2022

[CP2K](../../apps/cp2k.md) 2022.2 has been installed and set as the default module on Puhti
and Mahti. [See release notes here](https://www.cp2k.org/version_history).

## Gromacs 2022.3, 7.11.2022

[Gromacs](../../apps/gromacs.md) 2022.3 has been installed and set as the default module on Puhti
and Mahti. [See release notes here](https://manual.gromacs.org/2022.3/release-notes/2022/2022.3.html).

## Installing software with Spack, 28.10.2022

Users can now install software on CSC supercomputers using the Spack package
manager. [See here for a short tutorial on how to use the user Spack module at
CSC](../tutorials/user-spack.md).

## Installing packages from Bioconda using Tykky, 10.10.2022

A [new tutorial](../tutorials/bioconda-tutorial.md) on how to install packages from the Bioconda
channel using the [Tykky container wrapper tool](../../computing/containers/tykky.md) has been
published. This tutorial outlines the recommended way to install software packages related to
bioinformatics and biomedical research. Note that CSC has deprecated the *direct* (non-containerized)
usage of Conda installations on our supercomputers due to file system performance issues.

## Available applications can now be viewed as grouped by license type, 7.10.2022

In addition to alphabetical ordering, grouped by discipline or by availability, applications can now be
viewed as grouped by license type. Some information about each of the license categories is
provided. See [Applications by license](../../apps/by_license.md). (The page can also be reached from
the side navigation: Applications > By license)

## Python Data 3.10-22.09, 7.10.2022

Coinciding with the Red Hat 8 update of Puhti, a new [Python Data](../../apps/python-data.md)
module has been installed (on both Puhti and Mahti). In addition, old conda-based modules have
been removed, and the naming of modules has changed. Modules are now named according to the Python
version (PV) and the year (YY) and month (MM) of the installation, as PV-YY.MM. Typically the
module will include the newest versions of libraries at installation time, to the extent software
dependencies allow. Modules can also be loaded simply with the Python version, and you will get
the most recent installation with that version of Python, for example: `module load python-data/3.9`.

## `r-env-singularity` renamed to `r-env` and update to R 4.2.1 coinciding with RHEL8 update, 14.9.2022

Following the RHEL8 update on Puhti, the `r-env-singularity` module has been renamed to
[`r-env`](../../apps/r-env.md). The R version has been updated to 4.2.1, along with several
other version updates for installations included in the module. Due to the RHEL8 update requiring
modifications to the `r-env` module setup, older R versions are currently unavailable.

## Discovery Studio and Material Studio license discontinued in 2023, 25.8.2022

CSC has been providing a national academic license for [Discovery Studio](../../apps/discovery-studio.md)
and [Materials Studio](../../apps/materialsstudio.md). Due to small usage and the availability of
overlapping tools ([Maestro](../../apps/maestro.md)), the license will not be continued after this
year. This means that in 2023 these molecular modeling tools can't be used any more at CSC nor on
users' own computers. Please contact [Service Desk](../contact.md) if you need help in moving your
molecular modeling work to other modeling environments.

## PyTorch 1.12, 8.7.2022

PyTorch 1.12.0 is now available in the `pytorch/1.12` module on Puhti
and Mahti. See the [official PyTorch 1.12 release
notes](https://pytorch.org/blog/pytorch-1.12-released/), and [CSC's
PyTorch module documentation](../../apps/pytorch.md).

## CP2K modules on Mahti recompiled, 5.7.2022

Due to an issue related to OpenBLAS, the CP2K modules on Mahti have been
recompiled and linked to another linear algebra library (AMD BLIS). The old
versions were in some cases using up to seven times as much memory as before,
while matrix diagonalizations were not benefiting from the ELPA library as
expected.

## Python Data 3.9-3 and RAPIDS 22.04, 5.5.2022

New versions of [Python Data](../../apps/python-data.md) and
[RAPIDS](../../apps/rapids.md) are now available on both Puhti and Mahti. The
default versions have been changed to these new versions.

## CP2K 9.1 linked to Gromacs 2022, 19.4.2022

[CP2K](../../apps/cp2k.md) 9.1 has been linked to [Gromacs](../../apps/gromacs.md) 2022 for QM/MM
in the module `gromacs-env/2022-cp2k` on Mahti. This option was previously available under the
CP2K module `cp2k/8.1-gmx`, which has now been deprecated. Please use `gromacs-env/2022-cp2k` for
QM/MM simulations from now on.

## PyTorch 1.11, 8.4.2022

PyTorch 1.11.0 is now available in the `pytorch/1.11` module on Puhti and Mahti,
and has been set as the default module. See the [official PyTorch 1.11 release
notes](https://pytorch.org/blog/pytorch-1.11-released/), and [CSC's PyTorch
module documentation](../../apps/pytorch.md).

## LUE released on Puhti, 5.4.2022

An approximate tool called [LUE](../tutorials/lue.md) (Lustre Usage Explorer) for reporting amount
of data in folders has been released on Puhti. LUE is significantly faster than standard tools like
`stat` or `du` while being nicer on the file system. Please use LUE to keep track of how much
data/files you have on the disk and perform clean-ups in a timely manner to ensure a more
performant filesystem for all users.

## Tykky 0.2.2, 31.3.2022

[Tykky](../../computing/containers/tykky.md), a brand new tool for wrapping Conda/pip environments
inside a Singularity container, has been released. Containerization will considerably improve
startup times and decrease IO load with less files on the shared parallel filesystem. We recommend
wrapping all existing Conda environments within containers using Tykky as the [direct usage of
Conda on CSC supercomputers has been deprecated](../tutorials/conda.md).

## TensorFlow 2.8, 17.3.2022

TensorFlow 2.8.0 is now available in the `tensorflow/2.8` module on Puhti and
Mahti, and has been set as the default module. See the [TensorFlow 2.8 release
notes on GitHub](https://github.com/tensorflow/tensorflow/releases/tag/v2.8.0/)
for more details.

## Gromacs 2022, 9.3.2022

[Gromacs 2022](../../apps/gromacs.md) has been installed on Puhti and Mahti and is available on
both systems with `module load gromacs-env/2022`. A list of new features and changes is found in the
[Gromacs manual](https://manual.gromacs.org/documentation/current/release-notes/index.html#gromacs-2022-series).
`gromacs-env/2021` is now the default.

## CP2K 9.1, 4.3.2022

[CP2K](../../apps/cp2k.md) version 9.1 has been installed on Mahti and is available with
`module load cp2k/9.1-omp`, given that `gcc/10.3.0` and `openmpi/4.1.0` are first loaded.
A list of new features and changes is found on the [CP2K website](https://www.cp2k.org/version_history#section91).

## Schrödinger Maestro 2022.1, 25.2.2022

Schrödinger Maestro 2022.1 has been installed on Puhti and set as the default module. For a list
of new features, see the [Schrödinger website](https://www.schrodinger.com/releases/new-features).

## Gromacs 2021 now default version, 7.2.2022

[Gromacs 2021.5](../../apps/gromacs.md) has been installed on Puhti and Mahti and set as the
default module (gromacs-env).

## Direct usage of Conda deprecated, 4.2.2022

CSC has [deprecated the direct usage of Conda
installations](../tutorials/conda.md) on our supercomputers' (Puhti and Mahti)
shared file systems.

## Python Data 3.9-2, 20.1.2022

A new version of [Python Data](../../apps/python-data.md) is now available with
`module load python-data/3.9-2` on both Puhti and Mahti. It includes the most
recent versions of Scikit-learn, SciPy, Pandas, JupyterLab and many other
popular data analytics and machine learning packages for Python 3.9.

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

Schrödinger Maestro 2021.3 has been installed on Puhti and set as the default module. The [extended
Maestro instructions](../tutorials/power-maestro.md#quantum-espresso) have been appended with a
section on how to speed up Quantum Espresso jobs. A bug in the script that generates the
`schrodinger.hosts` file has also been fixed by setting the `parallel` HOST entry to use the
`large` Slurm partition as intended.

## Turbomole 7.5.1, 25.8.2021

Turbomole 7.5.1 is now available and the default module on Puhti. The most important change
with this version is that the `ricc2` module for performing 2nd order approximate coupled
cluster calculations works appropriately, while older versions on Puhti have been recently
reported to suffer from numerical instabilities. These issues do not apply to TM v7.5 installed
on Mahti.

## CP2K 8.2, 13.8.2021

CP2K version 8.2 has been installed on Mahti and is available with `module load cp2k/8.2-omp`.
This requires that `gcc/10.3.0` and `openmpi/4.1.0` are first loaded. Version `7.1-elpa` will
remain the default module for now, but will be changed to `8.2-omp` in the near future (despite
the name, the ELPA diagonalization library is also linked to the new 8.2 version). The `cp2k.psmp`
binary of version `8.2-omp` has been tested and is roughly as efficient as `7.1-elpa`.

A list of new features and changes is found on the [CP2K website](https://www.cp2k.org/version_history).
Note that some keywords, such as `MAP_CONSISTENT` in the `QS` section, have been deprecated.

## AMS 2021.102, 13.8.2021

AMS has been updated to version 2021.102 on both Mahti and Puhti and set as the default module. The
[AMS documentation](../../apps/ams.md) has been updated accordingly to cover version 2021.102.

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
