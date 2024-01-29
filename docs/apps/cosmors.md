---
tags:
  - Academic
---

# COSMOsuite

**COSMOsuite** is a Comprehensive Toolbox for the Modelling and Prediction of Fluid Phase Properties using the COSMO-RS model. 
The toolbox consists of the components **COSMOtherm, COSMOconf, COSMOplex, COSMObase** and **COSMOquick**.

**COSMOtherm** is a command line/file driven program which can be run directly from a UNIX or DOS shell. It
allows for the calculation of any solvent or solvent mixture and solute or solute system at variable
temperature and pressure. COSMOtherm uses the chemical potentials derived from COSMO-RS theory to
compute all kinds of equilibrium thermodynamic properties or derived quantities.
COSMOtherm has a Graphical User Interface to the command line program. It allows for the interactive use
of the program, i.e. selection of compounds, preparation of property input, program runs and display of
calculation results.

**COSMOconf** is a flexible tool box for conformer generation. 
COSMOconf can be used in combination with the TURBOMOLE package
to generate COSMO files for relevant conformations. 
It enables you to use pre-defined procedures that are optimized for
the generation of the most relevant conformers for COSMO-RS. COSMOconf
can be used through the GUI or from the command line.

**COSMOplex** is a tool for simulation of self-organizing inhomogeneous systems based on COSMO-RS.
COSMOconf can be used through the GUI or from the command line.
 

## Available

*   Puhti: 2024

## License

-   You may use the Software exclusively for non-profit research
    purposes.
-   Only users from academic (i.e. degree-granting) institutes are
    allowed to use the Software

## Usage

### Use the GUI via your browser

Go to [puhti.csc.fi](https://puhti.csc.fi/) using a web browser and login using your CSC user account.

1. From there [launch a Desktop](../../computing/webinterface/desktop/#launching ). 
2. Open a ```Terminal``` and move to a suitable working directory.
3. Load the COSMO-RS module ```module load cosmors/2024```.
4. Add the launcing icons to the Desktop with the command ```setup_cosmodesktop.sh```.
4. Start for instance ```COSMOtherm``` by double-clicking on its Desktop-icon .


### Run it from the command line

Initialize the COSMO-RS environment

```bash
module load cosmors/2024
```
## Documentation

The latest documentation can be found in the directory ```/appl/soft/chem/cosmors/Documentation/``` as pdf files.

Older documentation online:

-   [BIOVIA COSMOtherm](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmotherm/) 
-   [BIOVIA COSMOconf](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoconf/) 
-   [BIOVIA COSMOquick](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoquick/) 
-   [BIOVIA COSMOplex ](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoplex/) 

## More information
-   [COSMO-RS @ Dassault Systèmes](https://www.3ds.com/products/biovia/cosmo-rs) 
-   [COSMO-RS Videos on YouTube](https://www.youtube.com/playlist?list=PLRBPTxPZPfXVPSB46N-Ih1bCwMxOUY3de) 
