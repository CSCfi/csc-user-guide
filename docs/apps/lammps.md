# LAMMPS

LAMMPS is a "Molecular Dynamics Simulator" which supports
a wide variety of [different force fields](https://lammps.sandia.gov/doc/Intro_features.html#interatomic-potentials-force-fields).
CSC does not have a
general purpose installation of LAMMPS, as each user typically
needs a little bit customised version. Please read below
how to create yours.

[TOC]

## Available

-   Puhti: Instructions available for building
-   Mahti: Instructions available for building

## License

LAMMPS is an open-source code, distributed freely under the terms of the GNU Public License (GPL).

## Usage

First [download](https://lammps.sandia.gov/download.html) the software. Please don't use the
prebuilt binaries, but take a look at the instructions for configuring and compiling LAMMPS 
on Puhti or Mahti for optimal performance (and to include the packages you need) in here:

```
/appl/soft/chem/lammps/
```

Please compile in `$TMPDIR` and install in `/projappl/<project code>`. 
Consult these pages on how to create batch jobs 
[on Puhti](../computing/running/creating-job-scripts-puhti.md) and 
[on Mahti](../computing/running/creating-job-scripts-mahti.md).

If you have problems in compiling LAMMPS, please contact servicedesk@csc.fi.

## References

The following JCP paper is the canonical reference to use for citing LAMMPS.
It describes the parallel spatial-decomposition, neighbor-finding, and communcation 
algorithms used in the code. Please also give the URL of the LAMMPS website in your paper, namely http://lammps.sandia.gov.

* S. Plimpton, Fast Parallel Algorithms for Short-Range Molecular Dynamics, J Comp Phys, 117, 1-19 (1995)

References to other methods used in LAMMPS can be found [here](https://lammps.sandia.gov/cite.html)

## More information

-   LAMMPS home page: [https://lammps.sandia.gov/](https://lammps.sandia.gov/)


