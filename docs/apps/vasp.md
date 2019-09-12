# VASP

[VASP](https://www.vasp.at/) is an ab initio DFT program for computing
electronic structures of up to few hundreds of atoms.

This page describes how to use VASP on puhti.csc.fi.


## Available

See available VASP versions in puhti.csc.fi with command

```console
module avail vasp
```


## License

The usage of VASP requires a license, which must be acquired directly
from the developers of the software. After acquiring the license,
please send email to [servicedesk@csc.fi](mailto:servicedesk@csc.fi),
including your license number.


## Usage

Precompiled VASP executables and pseudopotentials are available
through module environment. Use command

```console
module show vasp
```

to see more detailed information.

### An example batch job script for s small test

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

For more options and details, see [Creating a batch job
script](https://docs.csc.fi/#computing/running/creating-job-scripts/).

### Performance optimization

The provided prebuild executables are built as "vanilla" as possible,
and provide a reasonable baseline. The performance optimization for
large experiments should be done per case basis. The commands that
created the prebuilt executables are in
`VASPROOT/README-<version>.sh`, and can be used as a starting point
for building more optimized, and/or otherwise modified executables.