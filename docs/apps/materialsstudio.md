# Materials Studio

Materials Studio is a versatile modelling suite for building and 
quantum and classical simulation of molecules, materials and nanostructures.

!!! Note
    CSC has obtained a reduced Materials Studio license for 2021 (heavy usage is recommended
    to be done with [Maestro](maestro.md)). Decision to continue beyond 2021
    will be made by autumn 2021.

## License

Materials Studio is a commercial program by [Biovia Inc.](https://3dsbiovia.com/)
CSC has purchased a national academic license for the year 2020 that allows non-profit
usage in Finnish institutes proviging higher education (for example
universities). If you're new to Materials Studio, consider also [Maestro](maestro.md),
and [AMS](ams.md).

## Available

Puhti: Version 2020

Materials Studio version 2020 can be downloaded and installed on your local 
computer. The graphical user interface runs only on Windows, but the
back end server components can also be run on Linux.

Look here for [installation files and instructions to configure licensing](https://wiki.eduuni.fi/display/cscjemma/Materials+Studio) (requires Haka authentication)

## Usage

The way to use Materials Studio is to install it locally and:

1. Prepare jobs (build systems, set simulation parameters) locally
1. Either run them locally or write the input files on disk
1. Copy them to Puhti, prepare a batch script to run the files
1. Copy the results back for analysis

See above for instructions for download, local installation and license configuration.
Usage on Puhti does not require any installation steps.

### Detailed workflow and tips for running standalone jobs on Puhti

* Once you've set up your simulation, instead of running it, click the "Files" button
next to the "Run" button, and save the files on your local disk. You can find the
location of the files, by right clicking one of them in the "project" view.

Note, that by default Windows file manager does not show all files, so you may need
to edit the preferences.

* Use some graphical file transfer tool to copy all files in the subdirectory created
by the Materials Studio GUI to a subdirectory in Puhti in your /scratch area.

* Open an ssh-connection to Puhti, and copy/paste the template batch script from
below to that directory.

* Change the "seedname" to match yours (name of the local folder and preceded by `.param`
file names), make sure you have the right binary set (`RunCASTEP.sh, RunDMol3.sh, ...`),
the right `--account=<project>`, number of tasks, etc.

* Submit the batch job with `sbatch your-script-name`

* Once it has completed, copy back all the files to the same folder in your local
computer (you can overwrite all existing files).

* Refresh the "project" view in the Materials Studio GUI.

Different Materials Studio "modules" require a little bit different batch scripts to run
as standalone jobs on Puhti. A simple example for DMol3:

```bash
#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --ntasks=2
#SBATCH --mem-per-cpu=1G
#SBATCH --account=<project>
#SBATCH --partition=test

# select which Materials Studio server you want to run
#RunMS="/appl/soft/chem/MS/MaterialsStudio20.1/etc/CASTEP/bin/RunCASTEP.sh"
#RunMS="/appl/soft/chem/MS/MaterialsStudio20.1/etc/MesoDyn/bin/RunMesoDyn.sh"
RunMS="/appl/soft/chem/MS/MaterialsStudio20.1/etc/DMol3/bin/RunDMol3.sh"

# set the seedname for the input files
seedname=TiO2

# no need to edit below here
$RunMS -np $SLURM_NTASKS $seedname
```

And a multistep example for CASTEP, which first runs an energy calculation and then two
property calculations using the optimized wavefunction (you need to have input files for all of them).

```bash
#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --ntasks=8
#SBATCH --mem-per-cpu=1G
#SBATCH --account=<project>
#SBATCH --partition=test

# select which Materials Studio server you want to run
RunMS="/appl/soft/chem/MS/MaterialsStudio20.1/etc/CASTEP/bin/RunCASTEP.sh"
#RunMS="/appl/soft/chem/MS/MaterialsStudio20.1/etc/DMol3/bin/RunDMol3.sh"
#RunMS="/appl/soft/chem/MS/MaterialsStudio20.1/etc/MesoDyn/bin/RunMesoDyn.sh"

# set the seedname for the input files
seedname=TiO2

$RunMS -np $SLURM_NTASKS $seedname

# if you have specified property calculations
# run them after the energy or geometry optimization job
# you should have a $seedname.param file for each of these
seedname=TiO2_BandStr
$RunMS -np $SLURM_NTASKS $seedname

seedname=TiO2_DOS
$RunMS -np $SLURM_NTASKS $seedname

```

Some modules, like Forcite, require a different way (MaterialsScript) to run them on Puhti.
Instructions on using this will provided later. You can find the details
from the Materials Studio help under "Running MaterialsScript in standalone mode".

## References

Please see method descriptions and log files in Materials Studio for details.

## More information

The [Biovia website](https://3dsbiovia.com/events/webinars/materials-science/)
has useful material for self study, and the documentation which comes with the Suite has several very useful tutorials.

