## CUDA debugger
[```cuda-gdb```](https://docs.nvidia.com/cuda/cuda-gdb/index.html) is an extension from NVIDIA of  gnu debugger ```gdb```. NVIDIA command line tool for debugging CUDA programs.   

In order to use tool the CUDA code has to be compiled with the extra flags ```-g``` and ```-G```. Next in an [interactive session](running/interactive-usage.md) one start the debugging by running ```cuda-gdb ./cuda_program```.

The tool supports all options of the [```gdb```](gdb.md) and the extra commands specific to CUDA debugging.

* Info commands: Commands to query information about CUDA activities
* Focus Commands: Commands to query or switch the focus of the debugger
* Configuration Commands: Commands to configure the CUDA-specific commands

The memory leaks of the device code can be check inside the debugger by activating the memory checker with ```set cuda memcheck```. Alternatively the ```cuda-memcheck``` tool can be outside of the debugger ```cuda-memcheck ./cuda_program```. 
