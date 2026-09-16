---
tags:
  - Free
catalog:
  name: StrAuto
  description: Automation and parallelization of STRUCTURE analysis
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# StrAuto

StrAuto automates and parallelizes [Structure](structure.md) analysis. From a single
input file it generates the Structure parameter and command files, runs the full
ensemble of *K* values × replicate runs, and chains the results into the Evanno ΔK
analysis with StructureHarvester and CLUMPP.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu: 1.0 (module `strauto`), via the `bio-apps` module.

Loading the `strauto` module also loads the tools it drives — `structure`,
`structureharvester` and `clumpp` — so you do not need to load them separately.

## Usage

StrAuto is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the StrAuto module:

```bash
module load bio-apps/v202603
module load strauto/1.0
```

On Roihu, StrAuto is run through the `strauto-roihu` launcher, which submits the
Structure ensemble as a native Slurm array job.

Move to the scratch directory of your project (any subdirectory inside your scratch
area will do) and create a new empty working directory:

```bash
cd /scratch/<project>/$USER
mkdir structure_job1
cd structure_job1
```

StrAuto uses two input files: a parameter file that must be named `input.py`, and a
genotype data file whose name is defined in `input.py` and ends with `.str` or
`.ustr`. Template files are provided by the module through the `$STRAUTO_TEMPLATES`
environment variable, and can be copied to your working directory:

```bash
cp $STRAUTO_TEMPLATES/input.py .
cp $STRAUTO_TEMPLATES/sim.str .
```

Edit `input.py` to match your analysis. Note that parallelization is handled by the
Slurm array job, so you should **not** set the `parallel` parameter to `True` in
`input.py`.

When the input file is ready, launch the analysis:

```bash
strauto-roihu
```

This generates the Structure parameter and command files and submits the full
*K* × replicate ensemble as a Slurm array job.

You can check on the analysis by running the same command again in the same working
directory:

```bash
strauto-roihu
```

This reports the status of the Structure jobs and, once all the Structure runs have
finished, performs the post-processing of the results (StructureHarvester Evanno ΔK
and CLUMPP).

For long-running analyses, use `strauto-roihu-longrun`, which submits the job to the
`longrun` partition:

```bash
strauto-roihu-longrun
```

## Support

[CSC Service Desk](../support/contact.md)

## More information

* [StrAuto home page](https://vc.popgen.org/software/strauto/)
* [StrAuto reference publication](http://dx.doi.org/10.1186/s12859-017-1593-0)
* [Structure home page](https://web.stanford.edu/group/pritchardlab/structure.html)
