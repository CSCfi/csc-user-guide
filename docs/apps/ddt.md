# DDT

Arm DDT is a parallel debugger with a graphical user interface (GUI).

## Available

Puhti, Mahti

## License

Usage is possible for both academic and commercial purposes.

## Usage

Set up the debugger environment
```
module load ddt
```

Compile the application to be debugged, for example a Fortran, C or C++
program, with the compiler option `-g` to enable generation of debug
information.

Here are a few examples of debug sessions (MPI debug sessions). The first
`salloc` command requests 40 processes in a single node and the second 40 processes divided
into two nodes:

```
export SLURM_OVERLAP=1

salloc --nodes=1 --ntasks-per-node=40 --time=00:30:00 --partition=small --account=<project_id> ddt srun ./debug_enabled_code
salloc --nodes=2 --ntasks-per-node=20 --time=00:30:00 --partition=large --account=<project_id> ddt srun ./debug_enabled_code
```

By default, DDT sets the initial breakpoint at `MPI_Init`. For debugging scalar or plain OpenMP programs, set the following environment variables before starting the debugger:

```
export ALLINEA_MPI_INIT=main
export ALLINEA_HOLD_MPI_INIT=1
```

## Documentation

* **On CSC supercomputers**: /appl/opt/ddt/20.1.1/doc/userguide-forge.pdf
* [On-line documentation](https://developer.arm.com/docs/101136/latest/ddt)
