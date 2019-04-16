# Gromacs

Gromacs is a very efficient engine to perform molecular dynamics
simulations and energy minimization particularly for proteins. However,
it can also be used to model polymers, membranes and e.g. coarse grained
systems. It also comes with plenty of analysis scripts.

[TOC]

## Available

-   Sisu,Taito: 4.6.7, 5.1.5, 2018.6, 2019.1
-   Taito-GPU: 5.1.5, 2016.5, 2018.5
-   Check available versions with `module avail gromacs`
-   Some versions include also Plumed (see module command output)
-   Gromacs is also available on the [Finnish Grid Infrastructure] (FGI). 
    Please see below for the example on how to run Gromacs on the.

!!! note
    Gromacs versions with the hsw (Haswell) tag won't run on the login
    node, but give better performance on Haswell compute nodes. For
    preparing jobs (gmx grompp, etc.) use the snb modules on the login node,
    but the appropriate version in your batch script. The same applies also
    for GPU enabled versions. Some modules have only `mdrun_mpi` for parallel
    runs. See output of module command whether to use `gmx_mpi mdrun` or
    `mdrun_mpi`.

## License
Gromacs is free software available under LGPL, version 2.1.

## Usage

Initialise use on Taito like this:

```bash
$ module load gromacs-env
```

which will initialise the default module.

This will show all available versions:
```bash
$ module avail gromacs-env
```

**Notes about performance**

It is important to set up the simulations properly to use resources efficiently.
The most important are:

-   If you run in parallel, make a scaling test for each system - don't use more cores than is efficient. 
    Scaling depends on many aspects of your system and used algorithms, not just size.
-   Use a recent version - there has been significant speedup over the years (see table below)
-   Minimize unnecessary disk I/O - never run batch jobs with -v (the verbose flag) for mdrun

For a more complete description, consult the 
[Gromacs performance checklist] on the Gromacs page.

We recommend using the latest versions as they have most bugs fixed and
tend to be faster. If you switch the major version, check that the
results are comparable. See below for a brief performance test using the
d.dppc system (~100k atoms, PME).

||(Node archictecture / </br> Code optimization to)|cores|gmx </br> 4.5.6|gmx </br> 4.6.7|gmx </br> 5.1.5|gmx </br> 2016.5|gmx </br> 2018.1|
|--- |--- |--- |--- |--- |--- |--- |--- |
|Taito|Hsw/Hsw|48|-|-|45.505|48.407|49.369|
|Taito|Hsw/Snb|48|21.523|21.9|38.953|40.987|41.318|
|Taito|Snb/Snb|48|20.694|20.513|28.559|34.958|39.906|
|Sisu|Hsw/Hsw|48|-|30.104|39.935|48.979|49.624|
|Sisu|Hsw/Hsw|96|-|62.499|80.769|86.638|96.194|
|Taito-gpu|k80:1/Hsw|6|-|-|-|23.964|27.18|
|Taito-gpu|p100:1/Hsw|7|-|-|-|31.703|55.041|
|Taito-gpu|p100:4/Hsw|28|-|-|-|-|62.868|

From the table we can see that it does not make sense to use
but one GPU for this job and one P100 GPU is faster than two
full Haswell nodes (i.e. 48 cores), but using four full nodes
still improves speed practically linearly. Old versions are
slower and using AVX2_256 SIMD on Haswell speeds up significantly.

**Example batch script for Taito**

```
#!/bin/bash -l
#SBATCH --time=00:30:00
#SBATCH --partition=parallel
#SBATCH --constraint=snb
#SBATCH --ntasks-per-node=24
#SBATCH --nodes=4
#SBATCH --mail-type=END
##SBATCH --mail-user=your.email@your.domain  # edit the email and uncomment to get mail

# this script runs a 96 core (4 full Haswell nodes) gromacs job, requesting 30 minutes time

export OMP_NUM_THREADS=1

module load gromacs-env/2018.6 # change version as needed

srun mdrun_mpi -s topol -maxh 0.5 -dlb yes
```

Submit the script with `sbatch script_name.sh`

Download an [example batch script for Sisu](files/gmx-sisu-example.job)

**Example input files**

To run a Gromacs job, you will need a few inputfiles, which
can be processed into a tpr-file required by the molecular
dynamics engine mdrun or mdrun_mpi. To run your first Gromacs
simulation, download this [simple input example] and follow the instructions
in the README.txt.

**Visualizing trajectories**

In addition to ngmx program in Gromacs, trajectory files can be
visualized with the following programs:

-   [PyMOL] molecular modeling system.
-   [VMD] visualizing program for large biomolecular systems.

**Visualising XY-plots**

Gromacs tools produce output files made for the Grace program. These
data can be visualized with program Grace. To start working with Grace,
issue the command:

`module load grace`

To plot all energy components in the energy.xvg file give:

`xmgrace -nxy energy.xvg`

Alternatively, you can use the general plotting tool [gnuplot](http://www.gnuplot.info/).


## References

Cite your work with the following references:

-   GROMACS 4: Algorithms for Highly Efficient, Load-Balanced, and
    Scalable Molecular Simulation. Hess, B., Kutzner, C., van der
    Spoel, D. and Lindahl, E. J. Chem. Theory Comput., 4, 435-447
    (2008).
-   GROMACS: Fast, Flexible and Free. D. van der Spoel, E. Lindahl, B.
    Hess, G. Groenhof, A. E. Mark and H. J. C.Berendsen, J. Comp. Chem.
    26 (2005) pp. 1701-1719
-   *GROMACS: High performance molecular simulations through multi-level
    parallelism from laptops to supercomputers* 
    M. J. Abraham, T. Murtola, R. Schulz, S. Páll, J. C. Smith, B. Hess, E.
    Lindahl *SoftwareX* 1 (2015) pp. 19-25
-   *Tackling Exascale Software Challenges in Molecular Dynamics Simulations with
    GROMACS* In S. Markidis & E. Laure (Eds.), Solving Software Challenges for Exascale
    S. Páll, M. J. Abraham, C. Kutzner, B. Hess, E. Lindahl 8759 (2015) pp. 3-27
-   *GROMACS 4.5: a high-throughput and highly parallel open source molecular
    simulation toolkit* S. Pronk, S. Páll, R. Schulz, P. Larsson, P. Bjelkmar, R. Apostolov, M. R.
    Shirts, J. C. Smith, P. M. Kasson, D. van der Spoel, B. Hess, and E. Lindahl
    Bioinformatics 29 (2013) pp. 845-54

See your simulation log file for more detailed references
for methods applied in your setup.

## More information

-   Gromacs home page: [http://www.gromacs.org/](http://www.gromacs.org/)
-   [Tutorials on the Gromacs website]  
-   [More tutorials] on the Bevanlab pages
-   [Lots of material at BioExcel EU project]
-   [HOW-TO] section on the Gromacs pages
-   Gromacs [documentation]
-   A very useful Gromacs Users [Mailing list]
-   [The PRODRG Server] for online creation of small molecule topology
-   If you want to compile your own version, have a look at the options
    used in the CSC installations. The cmake -files can be found in the
    installation directories (`which gmx` ...)

  [documentation]: http://manual.gromacs.org/documentation
  [Finnish Grid Infrastructure]: https://confluence.csc.fi/display/fgi/FGI+User+Pages
  [PyMOL]: http://www.pymol.org/
  [VMD]: http://www.ks.uiuc.edu/Research/vmd/
  [Gromacs performance checklist]: http://www.gromacs.org/Documentation/Performance_checklist
  [simple input example]: files/gmx-sample.tar.gz "Sample input for Gromacs"
  [Tutorials on the Gromacs website]: http://www.gromacs.org/Documentation/Tutorials
  [The PRODRG Server]: https://www.sites.google.com/site/vanaaltenlab/prodrg
  [HOW-TO]: http://www.gromacs.org/Documentation/How-tos
  [Lots of material at BioExcel EU project]: http://bioexcel.eu/software/gromacs/
  [More tutorials]: http://www.bevanlab.biochem.vt.edu/Pages/Personal/justin/gmx-tutorials/
  [Mailing list]: http://www.gromacs.org/Support/Mailing_Lists/Search