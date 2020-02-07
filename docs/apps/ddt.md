# DDT

Arm DDT is a parallel debugger with graphical user interface (GUI).

## Available

puhti.csc.fi

## Usage


Set up debugger environment
```
module load ddt
```
Compile the application to be debugged, for example Fortran, c or C++ program. The compiler option -g is generating the debug information.


An example debug sessions (MPI debug sessions). 40 processes in a node or 40 processes divided in two nodes:
```
salloc -n 40 -N1 -t 00:30:00 -p small --account=<project_id> ddt srun ./debug_enabled_code
salloc -n 40 -N2 --ntasks-per-node=20 -t 00:30:00 -p large --account=<project_id> ddt srun ./debug_enabled_code
```
## Documentation

<dl>
 <dt>pdf manuals:</dt>
 <dd>puhti.csc.fi /appl/opt/ddt/19.1.2/doc/userguide-forge.pdf </dd>

<dt>Web:</dt>
 <dd> https://developer.arm.com/docs/101136/latest/ddt </dd>
</dl>
