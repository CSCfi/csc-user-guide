## NVIDIA profiler (nvprof)
The nvprof profiling tool collects and views profiling data from the command-line. It enables the collection of a timeline of CUDA-related activities on both CPU and GPU, including kernel execution, memory transfers, memory set and CUDA API calls and events or metrics for CUDA kernels. Profiling results are displayed in the console after the profiling data is collected, and may also be saved for later viewing by either nvprof or the Visual Profiler. The nvprof is ran the same way as a usual [CUDA](https://docs.csc.fi/computing/running/example-job-scripts/#single-gpu) program.

```bash
module load gcc/8.3.0
module load cuda
```

An example of usage and output of nvprof:
```
$ nvprof  ./a.out
==27694== Profiling application: matrixMul
==27694== Profiling result:
Time(%)      Time     Calls       Avg       Min       Max  Name
 99.94%  1.11524s       301  3.7051ms  3.6928ms  3.7174ms  void matrixMulCUDA<int=32>(float*, float*, float*, int, int)
  0.04%  406.30us         2  203.15us  136.13us  270.18us  [CUDA memcpy HtoD]
  0.02%  248.29us         1  248.29us  248.29us  248.29us  [CUDA memcpy DtoH]
```
nvprof supports several very useful running options:
* --print-gpu-trace: Show trace of function calls
* --openacc-profiling on: Profile OpenACC as well (on by default)
* --cpu-profiling on: Enable some CPU profiling
* --csv --log-file FILE: Generate CSV output and save to FILE; handy for plots or benchmarked analysis
* --metrics M1: Measure only metric M1 which is one of the NVIDIA-provided metrics which can be listed via --query-metrics.


For more details please check the [nvidia documentation](https://docs.nvidia.com/cuda/profiler-users-guide/).
