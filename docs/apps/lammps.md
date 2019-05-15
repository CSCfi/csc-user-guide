# LAMMPS

LAMMPS is a classical molecular dynamics code, and an acronym for
Large-scale Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for solid-state materials (metals, semiconductors)
and soft matter (biomolecules, polymers) and coarse-grained or
mesoscopic systems. It can be used to model atoms or, more generically,
as a parallel particle simulator at the atomic, meso, or continuum
scale.

## Available

* Will be available on Puhti version XXX

## License

LAMMPS is distributed as an [open source] code under the terms of the [GPL].

## Usage

To get the LAMMPS binary in path, give:

    module load lammps

Have a look at the example submit script for Sisu in the installation
directory (/appl/chem/lammps/example.job).

## References

Citing LAMMPS in your papers

The following JCP paper is the canoncial reference to use for citing
LAMMPS. It describes the parallel spatial-decomposition,
neighbor-finding, and communcation algorithms used in the code. Please
also give the URL of the [LAMMPS WWW Site] in your paper, namely
http://lammps.sandia.gov.

S. Plimpton, **Fast Parallel Algorithms for Short-Range Molecular
Dynamics**, J Comp Phys, 117, 1-19 (1995). ([abstract]) ([pdf]) ([tar
file] of figures if they don't display correctly in the PDF file)

## More information

* [LAMMPS WWW Site], including the manual


  [LAMMPS WWW Site]: http://lammps.sandia.gov/index.html
  [abstract]: http://www.sandia.gov/%7Esjplimp/abstracts/jcompphys95.html
  [pdf]: http://www.sandia.gov/%7Esjplimp/papers/jcompphys95.pdf
  [tar file]: http://www.sandia.gov/%7Esjplimp/papers/jcompphys95_figs.tar.gz
  [open source]: https://lammps.sandia.gov/open_source.html
  [GPL]: http://www.gnu.org/copyleft/gpl.html