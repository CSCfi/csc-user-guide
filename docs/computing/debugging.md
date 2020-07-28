# Debugging
A good tool to start is [Valgrind](https://valgrind.org/). The  usual usage is for detecting memory leaks in the code, but it includes other production-quality tools such as: thread error detectors, cache and branch-prediction profiler, a call-graph generating cache and branch-prediction profiler, and  heap profilers. 
In order to use the tool, set up the environment as needed normally by the code  and  add the flags ```-g``` (adds debugging info in the operating system's native format) to the compilation command.
The tool can be used in a [interactive session](running/interactive-usage.md) or via a [submitted job](submitting-jobs.md). The module has to be loaded first:
```bash
module load valgrind
```
Analyzing the code is simple. 
In an interactive session  use ```valgrind ./program```, while as a submitted job run with ```srun valgrind ./myprogram```.

## Arm DDT

```bash
module load ddt
```

An example interactive debug session (for a MPI program):
```bash
salloc --nodes=2 --ntasks-per-node=20 --time=00:30:00 --partition=large \
  --account=<project> ddt srun ./debug_enabled_program
```

User's Guide (puhti.csc.fi): /appl/opt/ddt/19.1.2/doc/userguide-forge.pdf

FIXME: add links to external documentation
