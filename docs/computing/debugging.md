# Debugging
A good tool to start is [Valgrind](https://valgrind.org/). Its most common usage is for detecting memory leaks in the code, but it includes other production-quality tools such as: thread error detectors, cache and branch-prediction profiler, a call-graph generating cache and branch-prediction profiler, and  heap profilers. 
In order to use the tool, set up the environment as needed normally by the code  and  add the flags ```-g``` (adds debugging info in the operating system's native format) to the compilation command.
The tool can be used in a [interactive session](running/interactive-usage.md) or via a [submitted job](submitting-jobs.md). The module has to be loaded first:
```bash
module load valgrind
```
Analyzing the code is simple. 
In an interactive session  use ```valgrind ./program```, while as a submitted job run with ```srun valgrind ./myprogram```.

## 
Depending on the on type of program, several other debugging tools are available on the CSC servers:

* [Arm DDT](../apps/ddt.md) Parallel C, C++ and Fortran 90 debugger. It also supports NVIDIA CUDA GPUs. 
* [GDB](gdb.md) GDB is the GNU Debugger for C, C++ and Fortran 90.
* [PDB](pdb.md) PDB is an interactive source code debugger for Python programs.
* [Cuda debugger](cgdb.md) It is an interactive source code debugger for CUDA programs.
