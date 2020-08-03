# cuda-gdb: CUDA debugger

[cuda-gdb](https://docs.nvidia.com/cuda/cuda-gdb/index.html) is an NVIDIA
extension of the GNU debugger `gdb`. It is a command-line tool for debugging
CUDA programs.

In order to use tool the CUDA code has to be compiled with the extra flags
`-g` and `-G`.

Next in an [interactive session](running/interactive-usage.md) one starts the
debugging by running:

```bash
cuda-gdb ./cuda_program
```

The tool supports all options of [gdb](gdb.md) and some extra commands
specific to CUDA debugging:

* Info commands: Commands to query information about CUDA activities
* Focus Commands: Commands to query or switch the focus of the debugger
* Configuration Commands: Commands to configure the CUDA-specific commands

Memory leaks of device code can be checked inside the debugger by activating
the memory checker with `set cuda memcheck`. Alternatively the `cuda-memcheck`
tool can be used outside of the debugger (`cuda-memcheck ./cuda_program`).
