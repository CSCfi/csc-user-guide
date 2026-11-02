---
tags:
  - Free
catalog:
  name: Open Babel
  description: Program to interconvert file formats currently used in molecular modeling
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Roihu
---

# Open Babel

Open Babel is a chemical toolbox designed to speak the many languages of
chemical data. It is an open, collaborative project allowing anyone to search,
convert, analyze, or store data from molecular modeling, chemistry, solid-state
materials, biochemistry, or related areas.

## Available

- Roihu-CPU: 3.2.0

## License

Open Babel is free software available under GNU GPL.

## Usage

Initialize Open Babel on Roihu-CPU like this:

```bash
module purge
module load gcc/15.2.0 openmpi/5.0.10
module load openbabel/3.2.0
```

A simple example, converting a PDB file to a Turbomole coord file:

```bash
obabel -ipdb molecule.pdb -otmol -O coord
```

For a comprehensive list of options and supported file formats, do `obabel -H`,
or `obabel -L formats` or check the links below.

## References

Please use both of the following references to cite Open Babel:

- N M O'Boyle, M Banck, C A James, C Morley, T Vandermeersch, and G R
  Hutchison. "Open Babel: An open chemical toolbox." J. Cheminf. (2011), 3, 33.
  DOI:10.1186/1758-2946-3-33.
- The Open Babel Package, version 3.2.0, <https://openbabel.org/>.

## More information

- [Open Babel documentation](https://openbabel.org/)
- [Open Babel on GitHub](https://github.com/openbabel)
