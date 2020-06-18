## OpenFOAM

OpenFOAM (for "Open-source Field Operation And Manipulation") is a C++ toolbox for the development of customized numerical solvers, and pre-/post-processing utilities for the solution of continuum mechanics problems, most prominently including computational fluid dynamics (CFD), ([OpenFOAM in Wikipedia](https://en.wikipedia.org/wiki/OpenFOAM)). OpenFOAM has an extensive range of features to solve anything from complex fluid flows involving chemical reactions, turbulence and heat transfer, to solid dynamics and electromagnetics ([by OpenCFD Ltd](https://www.esi-group.com/engineering-services/consulting-services/openfoam/what-openfoam)).

There are three different variants of OpenFOAM, of which at CSC - IT Center for Science computer platforms are  currently installed different versions from [OpenFOAM Foundation](https://cfd.direct/) and [OpenCFD Ltd](https://www.openfoam.com). 

## License

OpenFOAM is freely available and open source, and is licensed under the [GNU General Public Licence](https://www.gnu.org/licenses/gpl-3.0.en.html) (Gnu GPL or GPL), with GPL license typical [characteristics for exploitation](https://openfoam.org/licence/). OpenFOAM® is registered trademark of OpenCFD Ltd, licensed to the OpenFOAM Foundation. 

## Available

Different versions of OpenFOAM by OpenFOAM Foundation and OpenCFD are installed on [Taito and Puhti servers](https://research.csc.fi/csc-s-servers).

## Usage

After login on the server, give command

    module load openfoam

the command only lists available versions with some extra information.  For to launch a spesific version, follow given instructions, that is, for example, for to launch OpenFOAM Foundation's versio 7, give command

    openfoam-7

OpenCFD's versions are recognized of version sign starting with letter v, ie, for to launch version v1906, give command

    openfoam-v1906

Version specific example files for a batch job scripts are available on the servers.  The instructions how to copy those example files are printed on the terminal after module loading command. 

## Support

In problem situation, send an email to servicedesk@csc.fi.

## More information

* [OpenFOAM Foundation](https://openfoam.org/)
* [OpenFOAM by OpenCFD](https://www.openfoam.com/)


