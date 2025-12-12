# Deprecated apps

Occasionally, CSC may need to deprecate certain pre-installed software or
software versions. This may, for example, be due to discontinued licenses or
incompatibility of non-actively maintained software with updating computing
environments.

A list of deprecated software, the reasons behind the deprecation and
recommended alternatives can be found below. If you have questions, please
[contact CSC Service Desk](../contact.md).

---

## Bioconda

Bioconda is no longer available on Puhti. Native Conda installations sitting
directly on the shared file system are ineffective and not recommended in HPC
environments such as Puhti. Please use [Tykky](../../computing/containers/tykky.md)
installations instead to wrap your Conda environment within a container.
[See a tutorial on this here](../tutorials/bioconda-tutorial.md). Note that
some packages that were previously provided through Bioconda are now available
as separate modules.

---

## Discovery Studio

The national Discovery Studio license provided by CSC was discontinued in 2022.
Since the beginning of 2023, it is no longer available. Please consider using 
[Maestro](../../apps/maestro.md) instead. [Contact CSC Service Desk](../contact.md)
if you need support in migrating your workflow.

---

## Materials Studio

The national Materials Studio license provided by CSC was discontinued in 2022.
Since the beginning of 2023, it is no longer available. Please consider using, e.g., 
[Maestro](../../apps/maestro.md) or [AMS](../../apps/ams.md) instead.
[Contact CSC Service Desk](../contact.md) if you need support in migrating
your workflow.

---

## NoMachine

The NoMachine remote desktop service was discontinued at CSC on 25th May 2023,
at the end of the its licensing period.

The service is superseded by [the web interfaces for Puhti, Mahti and LUMI](../../computing/webinterface/index.md).

??? info "Replacements for NoMachine (click to reveal)"

    * For a generic graphical remote desktop, the
    [Desktop application](../../computing/webinterface/desktop.md) can be launched from the web
    interface.
    * For a shell (e.g. a persistent shell on a compute node), have a look at [the shell applications](../../computing/webinterface/index.md#shell) on the web interface.
    * Available as interactive applications.
        * [Jupyter](../../computing/webinterface/jupyter.md)
        * [Julia-Jupyter](../../computing/webinterface/julia-on-jupyter.md)
        * [MATLAB](../../computing/webinterface/matlab.md)
        * [RStudio](../../computing/webinterface/rstudio.md)
        * [TensorBoard](../../computing/webinterface/tensorboard.md)
        * [Visual Studio Code](../../computing/webinterface/vscode.md)
    * Some applications are available with GPU acceleration. See
    [Accelerated visualization](../../computing/webinterface/accelerated-visualization.md).

    **If you have difficulties in migrating to use the web interfaces, please don't hesitate to
    [contact us](../contact.md)!**

---
