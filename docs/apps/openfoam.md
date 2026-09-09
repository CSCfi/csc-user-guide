---
tags:
  - Free
catalog:
  name: OpenFOAM
  description: OpenFOAM® is the leading free, open source software for computational fluid dynamics (CFD)
  license_type: Free
  disciplines:
    - Computational Engineering
  available_on:
    - Roihu
    - Mahti
    - LUMI
---

# OpenFOAM
[OpenFOAM](https://www.openfoam.com/) (for "Open-source Field Operation And Manipulation") is a C++ toolbox for the development of customized numerical solvers, and pre-/post-processing utilities for the solution of continuum mechanics problems, most prominently including computational fluid dynamics (CFD). OpenFOAM has an extensive range of features to solve anything from complex fluid flows involving chemical reactions, turbulence and heat transfer, to solid dynamics and electromagnetics ([by OpenCFD Ltd](https://www.openfoam.com/)).

There are different variants of OpenFOAM, of which at CSC - IT Center for Science computer platforms, are currently installed different versions from [OpenFOAM Foundation](https://cfd.direct/) and [OpenCFD Ltd](https://www.openfoam.com).

## License
OpenFOAM is freely available and open source, and is licensed under the [GNU General Public Licence](https://www.gnu.org/licenses/gpl-3.0.en.html) (Gnu GPL or GPL), with GPL license typical [characteristics for exploitation](https://openfoam.org/licence/).

## Available
Different versions of OpenFOAM, provided by OpenFOAM Foundation and OpenCFD, are installed on [Roihu, Mahti and LUMI servers](../computing/available-systems.md).

## Usage
After logging in to the server, give the command
```bash
module -r spider '.*openfoam.*'
```

On LUMI, you need to first load the module environment
```bash
module use /appl/local/csc/modulefiles
module spider openfoam
```

The command lists available OpenFOAM versions on the server. To get more information about a specific version, for example, about OpenFOAM Foundation's version 12, use the command
```bash
module spider openfoam-org/12
```

To launch a specific version (say, version 12), give the command
```bash
module load openfoam-org/12
```

OpenCFD's versions are recognized by a version string starting with letter _v_, i.e., to launch version openfoam/v2412, give the command
```bash
module load openfoam/v2412
```

### Use collated parallel I/O method on CSC's servers
- on CSC's computing servers, use OpenFOAM's [collated I/O method](https://openfoam.org/news/parallel-io/) whenever possible
- using the collated method is absolutely necessary when the model size is large and a lot of disk I/O is necessary

The file system used on CSC's computing platforms, Roihu, Mahti and LUMI, is [Lustre](http://lustre.org/), which is optimized for reading and writing small number of files. The number of output files written by OpenFOAM can easily become very large, even up to millions, if the mesh size is large, and if field variables are written to the disk every time step. Such I/O operations will cause the file system to become heavily overloaded, and the whole computing platform can get jammed even by a few simultaneous OpenFOAM users.

The above described traditional parallel I/O method of OpenFOAM can be replaced in the latest versions of OpenFOAM with the collated parallel I/O method, where the output data is written only in few files. Considering HPC platforms using parallel files systems, this has been a significant improvement to OpenFOAM.

In test runs on CSC's servers with the collated I/O method, significant difference in throughput time has not been recognized compared to non-collated method. In some tests, collated method has shown to be slightly faster. Our recommendation is to use collated method whenever it is practicable.

#### An example
Mahti server contains 128 cores per node. If the total subdomain number in the model is 256, a user may allocate two full nodes for the solver run. Decomposition batch job can then be done using the command
```bash
decomposePar -fileHandler collated -ioRanks '(0 128 256)'
```

and two directories `processors256_0-127` and `processors256_128-255` are created. For the solver run, the command will then be
```bash
pimpleFoam -parallel -fileHandler collated -ioRanks '(0 128 256)'
```

In that way, 128 processes are launched on both nodes, and on each node one process is a master process. Reconstruction of the data is done in the batch job with the command
```bash
reconstructPar
```

In this example, the pressure results of domains 0 to 127 per time step are written into a single file. In a non-collated method, the same results would have been written into 128 separate files. This tremendous decrease in the number of output files happens naturally with all the rest of the field variables also.

I/O operations in the collated method are based on threaded sub-processes, and therefore do not cause any time overhead for the simulation compared to non-collated method.

## Support
If you encounter any issue while using OpenFOAM on CSC's servers, please send an email to [CSC Service Desk](../support/contact.md).

## More information
- [OpenFOAM Foundation](https://openfoam.org/)
- [OpenFOAM by OpenCFD](https://www.openfoam.com/)
