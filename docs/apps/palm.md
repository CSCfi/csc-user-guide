---
tags:
  - Free
---

# PALM

PALM is an advanced and modern meteorological model system for atmospheric and oceanic
boundary-layer flows. It has been developed as a turbulence-resolving large-eddy simulation
(LES) model that is especially designed for performing on massively parallel computer
architectures.

The PALM model system has been mainly developed and is maintained by the ​PALM group at the
​[Institute of Meteorology and Climatology (IMUK)](https://www.muk.uni-hannover.de/?&L=1) of
Leibniz Universität Hannover, Germany. A number of code parts have been contributed by national
(German) and international work groups.

## License

The PALM model system is free software. It can be redistributed and/or modified under the terms
of the GNU General Public License (v3)(https://www.gnu.org/licenses/gpl-3.0.html).

## Available

PALM is available on [Puhti, Mahti and LUMI](../computing/available-systems.md) servers. Versions
available are listed when running the installation script, see below.

## Usage

After login on the server, give the command

```bash
module spider palm
```

This gives you a list of the installed versions. To load the version of your choice, give the command

```bash
module load palm/<version>
```

On LUMI, you need to first load the module environment

```bash
module use /appl/local/csc/modulefiles
module spider palm
module load palm/<version>
```

Link to read the instruction file is created,

```bash
readme_palm_csc
```

along with link to the command to run the installation script

```bash
installPalm
```

It is recommended to read first the instruction file, especially to understand on which disk
partition on the server the installation should be done (i.e., where to run the installation
script).

An example test case input file is included in the installation. In the instruction
file, run commands are given for compilation of the code, and for batch job execution
using the example case. For more information about the test case execution, see the latest
[PALM tutorials](https://palm.muk.uni-hannover.de/trac/wiki/doc/tut/palm#Exercisepresentations).

## Support

If you encounter problems using PALM, [contact CSC Service Desk](../support/contact.md).

## More information

* [The PALM model system](https://palm.muk.uni-hannover.de/trac)
* [PALM documentation](https://palm.muk.uni-hannover.de/trac/wiki/doc)
* [PALM movie gallery](https://palm.muk.uni-hannover.de/trac/wiki/gallery/movies)
* [PALM Tutorial](https://palm.muk.uni-hannover.de/trac/wiki/doc/tut/palm#Exercisepresentations)
