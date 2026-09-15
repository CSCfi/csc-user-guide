---
tags:
  - Academic
catalog:
  name: COSMO-RS
  description: Toolbox for the prediction of fluid phase thermodynamic properties using the COSMO-RS model
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - Roihu
---

# COSMO-RS

**COSMOsuite** is a comprehensive toolbox for the modelling and prediction of
fluid phase properties using the COSMO-RS model. The toolbox consists of the
components **COSMOtherm**, **COSMOconf**, **COSMOplex**, **COSMObase** and
**COSMOquick**.

**COSMOtherm** is a command-line/file-driven program which can be run directly
from a UNIX or DOS shell. It allows for the calculation of any solvent or solvent
mixture and solute or solute system at variable temperature and pressure.
COSMOtherm uses the chemical potentials derived from COSMO-RS theory to compute
various equilibrium thermodynamic properties or derived quantities. COSMOtherm
has a Graphical User Interface (GUI) to the command-line program, allowing for
the interactive selection of compounds, preparation of property input, program
runs and display of calculation results.

**COSMOconf** is a flexible toolbox for conformer generation. COSMOconf can be
used in combination with the [TURBOMOLE](turbomole.md) package to generate COSMO
files for relevant conformations. It enables you to use pre-defined procedures
that are optimized for the generation of the most relevant conformers for
COSMO-RS.

**COSMOplex** is a tool for simulation of self-organizing inhomogeneous systems
based on COSMO-RS.

## Available

- Roihu-CPU: 2026

## License

- You may use the Software exclusively for non-profit research purposes.
- Only users from academic (i.e. degree-granting) institutes are allowed to
  use the Software.

## Usage

Initialise the COSMO-RS environment:

```bash
module load cosmors/2026
```

On Roihu, COSMO-RS runs on the CPU nodes. Loading the module also loads
[TURBOMOLE](turbomole.md) (`turbomole/8.0`), which COSMOconf uses to generate
COSMO files. For a full list of available partitions see the
[Roihu batch job partitions](../computing/running/batch-job-partitions.md) page.

### Use the GUI via your browser

Go to the [Roihu web interface](https://roihu.csc.fi/) using a web browser and
login using your CSC user account or Haka federation.

1. From there, [launch a Desktop](../computing/webinterface/desktop.md#launching).
2. Open a `Terminal` and move to a suitable working directory.
3. Load the COSMO-RS module: `module load cosmors/2026`.
4. Add the launching icons to the Desktop with the command
   `setup_cosmodesktop.sh`.
5. Start for instance `COSMOtherm` by double-clicking its Desktop icon.

### Run it from the command-line

After loading the module, COSMOtherm is available as the `cosmotherm` command. A
COSMOtherm input file refers to the shared parameter files and compound database
on its global command line via `CDIR` (parameter files) and `FDIR` (compound
COSMO/CCF files). On Roihu the parameter files are in:

```
CDIR=/appl/soft/manual/chem/x86_64/cosmors/2026/COSMOtherm/CTDATA-FILES
```

The compound-file search path (`FDIR`) points to the directory holding the COSMO
files of the compounds in your calculation. The full COSMObase compound library
is installed under
`/appl/soft/manual/chem/x86_64/cosmors/2026/COSMObase2026/<PARAMETERIZATION>`,
for example `COSMObase2026/BP-TZVP-COSMO`. Alternatively, point `FDIR` at your own
directory of COSMO files. The parameter file (e.g. `BP_TZVP_26.ctd`) and the
compound parameterization must be consistent with the level requested in the
input.

The global command line at the top of a COSMOtherm input file then looks like:

```
ctd=BP_TZVP_26.ctd CDIR=/appl/soft/manual/chem/x86_64/cosmors/2026/COSMOtherm/CTDATA-FILES
FDIR=/appl/soft/manual/chem/x86_64/cosmors/2026/COSMObase2026/BP-TZVP-COSMO
```

#### Input file structure

A COSMOtherm input file (`myjob.inp`) is line-oriented: a global command line
(parameters, paths and options), an optional title line, one line per compound,
and one or more property job blocks describing what to compute. As an example,
this input computes an isothermal binary vapour–liquid equilibrium (VLE) of
acetone and chloroform:

```
ctd=BP_TZVP_26.ctd CDIR=/appl/soft/manual/chem/x86_64/cosmors/2026/COSMOtherm/CTDATA-FILES
FDIR=/appl/soft/manual/chem/x86_64/cosmors/2026/COSMObase2026/BP-TZVP-COSMO
! Isothermal binary phase diagram (VLE) of Acetone (1) and Chloroform (2)
f = propanone_c0.cosmo VPWAG_KPA={ 4700 508.100 -7.45514 1.20200 -2.43926 -3.3559 } TPVMIN_K=259 TPVMAX_K=508
f = chcl3_c0.cosmo     VPWAG_KPA={ 5470 536.400 -6.95546 1.16625 -2.1397 -3.44421 } TPVMIN_K=215 TPVMAX_K=536
```

Here `f = <name>.cosmo` selects each compound (located via `FDIR`), a line
starting with `!` is a comment/title, and per-compound options (such as the
Wagner vapour-pressure coefficients `VPWAG_KPA` and temperature ranges) follow on
the same line. Compounds are numbered in the order listed and referred to by
index in the property job lines that follow.

Ready-to-run examples for each calculation type (VLE, LLE, solubility, solvate
screening, conformer generation, etc.) are shipped with the installation:

```bash
ls /appl/soft/manual/chem/x86_64/cosmors/2026/COSMOtherm/EXAMPLES/EXAMPLES-COMMANDLINE/
```

Copy the example closest to your task, edit the compounds and the `CDIR` and
`FDIR` paths, and run it. Most users prepare inputs interactively in the
COSMOthermX GUI and then run the resulting `.inp` file in batch. The full input
syntax is documented in the COSMOtherm user manual under
`/appl/soft/manual/chem/x86_64/cosmors/2026/documentation/`.

#### COSMO files for your own compounds

Every compound in a COSMOtherm calculation needs a COSMO file (`.cosmo`/`.ccf`),
which stores the molecular surface screening-charge information COSMO-RS is based
on. For common molecules these are provided pre-computed in the COSMObase library.
For your own molecules — or any compound not in COSMObase — the COSMO files must
be generated with a quantum-chemical calculation using
[TURBOMOLE](turbomole.md). This is what **COSMOconf** automates: it generates the
relevant conformers of a molecule, runs the TURBOMOLE COSMO calculations for
each, and prunes them to the set relevant for COSMO-RS. The resulting COSMO files
are then referenced through `FDIR` (or listed directly) in your COSMOtherm input.

The COSMO files must be generated at the same parameterization level as the
COSMOtherm parameter file used in the calculation. For example, a `BP_TZVP_26.ctd`
run requires BP-TZVP COSMO files; this is why COSMObase is organised into separate
`BP-TZVP-COSMO`, `BP-TZVPD-FINE` and other subdirectories.

A minimal batch job for a COSMOtherm input file `myjob.inp`. Run it from your
scratch directory (`/scratch/<project>/<user>/`) so the input and output files are
available on the compute nodes:

```bash
#!/bin/bash
#SBATCH --partition=small         # see batch-job-partitions for all options
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4000        # MB per CPU core
#SBATCH --account=<project>       # insert here the project to be billed
#SBATCH --time=01:00:00           # time as hh:mm:ss

module load cosmors/2026

cosmotherm myjob.inp
```

Submit it with `sbatch myjob.sh`.

## Documentation

The latest documentation can be found in the directory
`/appl/soft/manual/chem/x86_64/cosmors/2026/documentation/` as PDF files.

Older documentation online:

- [BIOVIA COSMOtherm](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmotherm/)
- [BIOVIA COSMOconf](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoconf/)
- [BIOVIA COSMOquick](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoquick/)
- [BIOVIA COSMOplex](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoplex/)

## More information

- [COSMO-RS at Dassault Systèmes](https://www.3ds.com/products/biovia/cosmo-rs)
- [COSMO-RS videos on YouTube](https://www.youtube.com/playlist?list=PLRBPTxPZPfXVPSB46N-Ih1bCwMxOUY3de)
