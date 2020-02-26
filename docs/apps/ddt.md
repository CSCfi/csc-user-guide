# DDT

Arm DDT is a parallel debugger with a graphical user interface (GUI).

## Available

Puhti

## License

Usage is possible for both academic and commercial purposes.

## Usage

Set up debugger environment
```
module load ddt
```
Compile the application to be debugged, for example Fortran, a c or C++ program. The compiler option `-g` is generating the debug information.

Here are tiw example debug sessions (MPI debug sessions). The first requests 40 processes in a single node and the second 40 processes divided into two nodes:
```
salloc --ntasks=40 --nodes=1 --time=00:30:00 --partition=small --account=<project_id> ddt srun ./debug_enabled_code
salloc --ntasks=40 --nodes=2 --ntasks-per-node=20 --time=00:30:00 --partition=large --account=<project_id> ddt srun ./debug_enabled_code
```
## Documentation

* **pdf manuals:**
  - on puhti.csc.fi: /appl/opt/ddt/19.1.2/doc/userguide-forge.pdf
* **Web:**
 - [https://developer.arm.com/docs/101136/latest/ddt](https://developer.arm.com/docs/101136/latest/ddt)
