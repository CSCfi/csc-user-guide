# Debugging

## Prepare code for debugging

In order to get full debugging information, one needs to usually re-compile
the program of interest with the debug flag (`-g`) enabled. For example, with
the GNU compiler:

```
gcc -g -o example example.c
```


## Memory leaks

A good place to start is to check for memory leaks with
[Valgrind](https://valgrind.org/). It is a versatile tool that is most
commonly used to detect memory leaks in the code, but can also be used e.g. to
detect errors in threading or to investigate heap and cache usage.

In order to use Valgrind, set up the environment as needed normally by your
code and re-compile the code with the debug flag (`-g`) added.

Running an analysis with Valgrind is simple and can be done either in an
[interactive session](running/interactive-usage.md) or as a
[submitted job](running/submitting-jobs.md). In an interactive session the
command to use is `valgrind ./myprogram`, while in a submitted job the
command is `srun valgrind ./myprogram`.

For example, to check for memory leaks in an interactive session:

```bash
module load valgrind

valgrind ./example
```

To run the same analysis as a normal non-interactive job, e.g. when debugging
a parallel program, the command to use is `srun valgrind ./example`.


## Debuggers

Fully-fledged debuggers are often needed to really dig into the code execution
and to resolve runtime errors. At CSC, several debuggers are available:

* [Arm DDT](../apps/ddt.md) is a debugger for serial and parallel programs
  (MPI, OpenMP, CUDA) with both graphical and command-line interfaces
* [GDB](gdb.md) is a command-line debugger for compiled programs (C, C++,
  Fortran, etc.)
* [PDB](pdb.md) is an interactive debugger for Python programs
* [CUDA-GDB](cuda-gdb.md) is a command-line debugger for CUDA programs
* [compute-sanitizer](compute-san.md) is a command-line functional correctness checking suite
