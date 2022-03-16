# Open Babel

Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It is an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas. 


## Available

-   Puhti: 3.1.1
-   Mahti-rhel7:: 3.1.1

## License

Open Babel is free software available under  GNU GPL .

## Usage

Initialise Open Babel on Puhti like this:

```bash
module load openbabel/3.1.1
```

A simple example, converting a PDB file to a Turbomole coord file:

```bash
obabel -ipdb molecule.pdb -otmol -O coord
```

For a comprehensive list of options and supported file formats, do  `obabel -H`, or   `obabel -L formats` or check the links below.

## More information
-   [Open Babel wiki](http://openbabel.org/wiki/Main_Page)
-   [Open Babel on GitHub](https://github.com/openbabel )


