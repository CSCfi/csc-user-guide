# Syntax Example

Brief introduction of what this code is about.
There is a way to use html for the top header which will hide it from TOC below.

[TOC]

Example on including a picture with the "reference style"
![Chemistry logo][logo]

Please put all images in "img" folder in root (where docs is), not in local subfolder.
And with the complete syntax including width limit.

![alt text](/img/chemistry-logo.jpg "Chemistry logo"){ width=90% }

## Available

-   Puhti: Version 42 
-   Mahti: Version 41
-   Also possible to install on your own worksation

## License

Any limitations for usage listed here.

## Usage

To use this software on Puhti, initialize it with:

```bash
$ module load gromacs-env
```

to access the default version.

This will show all available versions:
```bash
$ module avail gromacs-env
```

Some additional syntax examples.

!!! tip
    This is a tip of high importance

!!! warning
    This is a warning of high importance

!!! note
    This is a note of high importance
    With two lines


An example of a table. Note the forced line breaks in the first line.


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

**Example batch script for Taito**

```
#!/bin/bash -l
#SBATCH -t 00:30:00
#SBATCH -p parallel
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

Example for linking to files in the "files" subfolder for display or download
(think about naming them in a clever way - it's the same folder for all software):

Download an [example batch script for Sisu](files/gmx-sisu-example.job)

??? note "Sisu"
        --8<-- "docs/apps/files/gmx-sisu-example.job"

An example for embedding a video on youtube:

[![Maestro Standalone](http://img.youtube.com/vi/oQDLa6Bh-q4/0.jpg)](http://www.youtube.com/watch?v=oQDLa6Bh-q4 "Maestro Standalone")

There's another syntax for using video from the videos subfolder, see eDuuni wiki DL2021 page.

## References

Cite your work with the following references:

-   GROMACS 4: Algorithms for Highly Efficient, Load-Balanced, and
    Scalable Molecular Simulation. Hess, B., Kutzner, C., van der
    Spoel, D. and Lindahl, E. J. Chem. Theory Comput., 4, 435-447
    (2008).

## More information

-   Gromacs home page: [http://www.gromacs.org/](http://www.gromacs.org/)
-   [Tutorials on the Gromacs website]


[logo]: /img/chemistry-logo.jpg "Chemistry logo"
[Tutorials on the Gromacs website]: http://www.gromacs.org/Documentation/Tutorials
