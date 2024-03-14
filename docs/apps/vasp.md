---
tags:
  - Other
---

# VASP

[VASP](https://www.vasp.at/) is an ab initio DFT program for computing
electronic structures of up to few hundreds of atoms.

This page briefly describes how to use VASP on mahti.csc.fi. Usage on puhti.csc.fi is very similar. That said,
VASP is a program which usage requires some experience. It is advised that new VASP users start out
with a supervisor or an experienced colleague.


## Available

See available VASP versions in mahti.csc.fi with command

```console
module avail vasp
```


## License

The usage of VASP requires a license, which must be acquired directly
from the developers of the software.

!!! warning ""

    After acquiring the license, please send email to [servicedesk@csc.fi](mailto:servicedesk@csc.fi),
    including the email address you have registered for the VASP license and your user name at CSC.


## Usage

Precompiled VASP executables and pseudopotentials are available
through module environment. Use command

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

For more options and details, see [Creating a batch job script](../computing/running/creating-job-scripts-puhti.md).

### VASP tutorials in Jupyter Lab

VASP tutorials can be followed also using Jupyter Lab from https://mahti.csc.fi. From
Settings -> Python, select "Custom module", and type in "py4vasp". When submitting the jobs
from the Jupyter Lab terminal window to compute nodes, first load module 'vasp', and then
use command similar to

```console
srun -p test -A <project> -t 5 -n 2 vasp_std
```

instead of the `mpirun ...` command shown in the tutorial.

### Performance optimization

First, the performance of VASP depends crucially on the parameters in
the INCAR file that control how the different k-points, bands and FFT
coefficients are distributed among the MPI tasks, and that the correct
version (std/gam/ncl) of the executable is used.

Second, the provided prebuild executables are built as "vanilla" as
possible, and provide a reasonable baseline. The performance
optimization for large experiments should be done per case basis. The
commands that created the prebuilt executables are in
`$VASPDIR/README.sh`, and can be used as a starting point
for building more optimized, and/or otherwise modified executables.
