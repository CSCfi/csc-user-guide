# ncu: GPU CUDA Kernel Profiler

## Available
    Puhti: 2022.2.0.0
    Mahti: 2021.3.0.0

## Usage

NVIDIA Nsight Compute is a CUDA kernel profiler that provides detailed performance data and offers guidance for optimizing your CUDA kernels.
The *ncu* profiling and debugging tool collects and views profiling data from the
command-line. It is a low level CUDA kernel profiling tool. It enables the collection of a timeline of CUDA-related
activities on both CPU and GPU, including kernel execution, memory transfers,
memory set and CUDA API calls and events or metrics for CUDA kernels.
Profiling results are displayed in the console after the profiling data is
collected, and may also be saved for later viewing by *ncu-ui* tool.

To use `ncu`, one needs to first load the CUDA module:

```bash
module load cuda
```

To profile a CUDA code, one then adds the command `ncu` before the normal
command to execute the code. Running is otherwise similar to that of any other
CUDA job on [Puhti](running/example-job-scripts-puhti.md#single-gpu) or [Mahti](running/example-job-scripts-mahti.md#1-2-gpu-job-ie-gpusmall-partition).

An example of usage of `ncu`:
```
ncu --set full -o myreport ./a.out
```
Next the resulted report is analysed with `ncu-ui` on the CSC supercomputers or on the user's local machine. The performance of the program can be compared to the theoretical peak  (`speed-of-light`) performance or to a custom baseline (for example a previous realease to be compared to) can be used.

`ncu` supports many useful running options, it is fully customizable. Use command line arguments `--list metrics`and `--query-metrics` to check the available metrics and enquire which metrics are available for the current platform. For more details please check the [nvidia documentation](https://docs.nvidia.com/nsight-compute/index.html).
