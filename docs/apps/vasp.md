---
tags:
  - Other
catalog:
  name: VASP
  description: Ab initio DFT electronic structures
  license_type: Other
  disciplines:
    - Physics
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# VASP

[VASP](https://www.vasp.at/) is an ab initio DFT program for computing
electronic structures of up to few hundreds of atoms.

This page briefly describes how to use VASP on mahti.csc.fi. Usage on
puhti.csc.fi is very similar. That said, VASP is a program the usage of
which requires some experience. It is advised that new VASP users start
out with a supervisor or an experienced colleague.

## Available

See available VASP versions in with command

```console
module avail vasp
```

## License

The usage of VASP requires a license, which must be acquired directly
from the developers of the software.

VASP versions prior to 6.5.1 use unix goups 'vasp' and 'vasp6' to control access to
pre-installed executables. After acquiring the license, or after your email address has been
added to an existing license, please send an email to [CSC Service Desk](../support/contact.md),
including your _username_ at CSC, and the _email address_ you have registered for the VASP
license in the [VASP Portal](https://vasp.at).

VASP versions from 6.5.1 onwards require license file '~/.vasp/vasp_license'. The license file
is downloaded from the VASP portal with commands

```console
module load vasp/6.5.1
request_license_key.sh
```

The `request_license_key.sh` script will ask user's VASP Portal username and password.

# Usage

Precompiled VASP executables and pseudopotentials are available
through the module environment. Use the command

```console
module show vasp
```

to see more detailed information.

### An example batch job script for a small test

```bash
#!/bin/bash
#SBATCH --time=00:15:00
#SBATCH --partition=test
#SBATCH --ntasks=4
#SBATCH --mem-per-cpu=1GB
#SBATCH --account=<project>

module load vasp
srun vasp_std
```

For more options and details, see how to create batch job scripts for
[Puhti](../computing/running/creating-job-scripts-puhti.md) and
[Mahti](../computing/running/creating-job-scripts-mahti.md).

### VASP tutorials in JupyterLab

[VASP tutorials](https://www.vasp.at/tutorials/latest/) can also be
followed using JupyterLab from the
[Mahti web interface](https://www.mahti.csc.fi). Open the *Jupyter* app,
and from *Settings* -> *Python*, select *Custom module* and type in
*py4vasp*. When submitting jobs from the JupyterLab terminal window to
compute nodes, first load module `vasp`, and then use a command similar to

```console
srun -p test -A <project> -t 5 -n 2 vasp_std
```

instead of the `mpirun ...` command shown in the tutorial.

### Performance optimization

First, the performance of VASP depends crucially on the parameters in
the INCAR file that control how the different k-points, bands and FFT
coefficients are distributed among the MPI tasks, and that the correct
version (std/gam/ncl) of the executable is used.

Second, the provided prebuilt executables are built as "vanilla" as
possible and provide a reasonable baseline. The performance
optimization for large experiments should be done on a per case basis.
The commands that created the prebuilt executables are in
`$VASPDIR/README.sh`, and can be used as a starting point
for building more optimized and/or otherwise modified executables.
