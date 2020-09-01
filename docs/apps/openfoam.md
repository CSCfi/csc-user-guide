## OpenFOAM

OpenFOAM (for "Open-source Field Operation And Manipulation") is a C++ toolbox for the development of customized numerical solvers, and pre-/post-processing utilities for the solution of continuum mechanics problems, most prominently including computational fluid dynamics (CFD), ([OpenFOAM in Wikipedia](https://en.wikipedia.org/wiki/OpenFOAM)). OpenFOAM has an extensive range of features to solve anything from complex fluid flows involving chemical reactions, turbulence and heat transfer, to solid dynamics and electromagnetics ([by OpenCFD Ltd](https://www.esi-group.com/engineering-services/consulting-services/openfoam/what-openfoam)).

There are three different variants of OpenFOAM, of which at CSC - IT Center for Science computer platforms are  currently installed different versions from [OpenFOAM Foundation](https://cfd.direct/) and [OpenCFD Ltd](https://www.openfoam.com). 

## License

OpenFOAM is freely available and open source, and is licensed under the [GNU General Public Licence](https://www.gnu.org/licenses/gpl-3.0.en.html) (Gnu GPL or GPL), with GPL license typical [characteristics for exploitation](https://openfoam.org/licence/). OpenFOAM® is registered trademark of OpenCFD Ltd, licensed to the OpenFOAM Foundation. 

## Available

Different versions of OpenFOAM by OpenFOAM Foundation and OpenCFD are installed on [Puhti and Mahti servers](https://research.csc.fi/csc-s-servers).

## Usage

After login on the server, give command

    module load openfoam

the command only lists available versions with some extra information.  For to launch a spesific version, follow given instructions, that is, for example, for to launch OpenFOAM Foundation's versio 7, give command

    openfoam-7

OpenCFD's versions are recognized of version sign starting with letter v, ie, for to launch version v1906, give command

    openfoam-v1906

Version specific example files for a batch job scripts are available on the servers.  The instructions how to copy those example files are printed on the terminal after module loading command. 

### Use collated parallel IO method on CSC's servers

-   on CSC's computing servers, use OpenFOAM's [collated IO method](https://openfoam.org/news/parallel-io/) when ever possible
-   use of collated method absolutely necessary when the model size is large and lot of disk IO is necessary

The file system used in CSC's computing platforms Puhti and Mahti is [Lustre](http://lustre.org/), which is optimized for reading and writing small number of files.  The number of output files written by OpenFOAM can easily become very large, even up to millions, if the mesh size is large, and of field variables all are written on the disk, even on every time step. Using this sort IO operation simultaneously by only a few OpenFOAM heavy users, the file system become hevily overloaded, and the whole computing platform can get jammed.

Above described, OpenFOAM's traditional parallel IO method can in the latest versions of OpenFOAM be replaced with collated parallel IO method, where the output data is written only in few files.  Considering HPC platforms using parallel files systems, this has been a significant improvement to OpenFOAM.

In test runs on CSC's servers with the collated IO method, significant difference in throughput time has not been recognized compared to non-collated method.  In some tests, collated method has shown to be even slightly faster. Our recommendation is to use collated method whenever it is practicable.

#### An example 

Mahti server one node contains 128  cores.  If the total subdomain number in the model is 256, user may allocate two full nodes for the solver run.  Decomposition batch job will then done using command

    decomposePar -fileHandler collated -ioRanks '(0 128 256)'

and two directories `processors256_0-127` and `processors256_128-255` are created.  For the solver run command will then be

    pimpleFoam -parallel -fileHandler collated -ioRanks '(0 128 256)'

In that way,  128 processes are running on both nodes, and on each node one process is a master process.  Reconstruction of the data is done in the batch job with command

    reconstructPar

In this example, the pressure results of domains 0 to 127 per time step are written into a single file.  In a non-collated method, the same results would have been written into 128 separate files. This tremendous decrease of number of output files happens naturally with all the rest of the field variables also.  

IO operations in the collated method are based on threaded sub-processes, and therefore do not cause any time overhead for the simulation compared to non-collated method.

#### Example batch job scipts for collated method usage on Mahti

The example scripts for separate batch runs for decomposition, solver and reconstruction are in folder

    /appl/soft/eng/OpenFOAM/batch_script_examples

Notice that on Mahti decomposition and reconstruction must be done in `interactive` queue,
[more info on using the interactive queue](../../computing/running/creating-job-scripts-mahti/#using-interactive-partition-for-non-parallel-pre-or-post-processing).

## Support

In a problem situation, send an email to servicedesk@csc.fi.

## More information

* [OpenFOAM Foundation](https://openfoam.org/)
* [OpenFOAM by OpenCFD](https://www.openfoam.com/)


