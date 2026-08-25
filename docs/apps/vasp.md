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
    - Roihu
---

# VASP

[VASP](https://www.vasp.at/) is an ab initio DFT program for computing
electronic structures of up to few hundreds of atoms.

This page briefly describes how to use VASP on Roihu. That said, using
VASP efficiently requires experience. It is advised that new VASP users start
out with a supervisor or an experienced colleague.

There are two ways to get access to VASP executables. You can build your own executables,
or you can get a personal license key and use CSC's pre-built executables.

## Build your own VASP executables

This is simple and documented in [GitHub](https://github.com/jlento/vasp-env). This
is also the way if you want to develop VASP, build modified versions of VASP, or
have acquired the license from Materials Desing Inc.

If you run into any issues building VASP, please send feedback to
[CSC's ServiceDesk](../support/contact.md).

## Use CSC's pre-built executables

You can see the available VASP versions with command

```console
module avail vasp
```

The use of the pre-built executables requires that each user gets a personal
license key, and updates it when necessary. The license key is stored
in the home directory in the file `~/.vasp/vasp_license`.

The license file is downloaded from the VASP portal with commands

```console
module load vasp
request_license_key.sh
```

The `request_license_key.sh` script will ask user's VASP Portal username and password.

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

VASP peformance depends crucially on the parameters in the INCAR file
and that the correct version (std/gam/ncl) of the executable is used.
The INCAR parameters control how the different k-points, bands and FFT
coefficients are distributed among the MPI tasks, among many other things.
