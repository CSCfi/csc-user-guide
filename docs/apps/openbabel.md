---
tags:
  - Free
---

# Open Babel

Open Babel is a chemical toolbox designed to speak the many languages of chemical
data. It is an open, collaborative project allowing anyone to search, convert,
analyze, or store data from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

## Available

-   Puhti: 3.1.1
-   Mahti: 3.1.1

## License

Open Babel is free software available under GNU GPL.

## Usage

Initialize Open Babel on Puhti like this:

```bash
module load openbabel/3.1.1
```

A simple example, converting a PDB file to a Turbomole coord file:

```bash
obabel -ipdb molecule.pdb -otmol -O coord
```

For a comprehensive list of options and supported file formats, do  `obabel -H`,
or `obabel -L formats` or check the links below.

## References

Please use both of the following references to cite Open Babel:

-   N M O'Boyle, M Banck, C A James, C Morley, T Vandermeersch, and G R Hutchison.
    "Open Babel: An open chemical toolbox." J. Cheminf. (2011), 3, 33. DOI:10.1186/1758-2946-3-33
-   The Open Babel Package, version 3.1.1 http://openbabel.org

## More information

-   [Open Babel documentation](http://openbabel.org/)
-   [Open Babel on GitHub](https://github.com/openbabel )
