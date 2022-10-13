# nvprof: CUDA profiler

## Available
    Puhti: 11.7.50
    Mahti: 11.5.50

## Usage

The *nvprof* profiling tool collects and views profiling data from the
command-line. It enables the collection of a timeline of CUDA-related
activities on both CPU and GPU, including kernel execution, memory transfers,
memory set and CUDA API calls and events or metrics for CUDA kernels.
Profiling results are displayed in the console after the profiling data is
collected, and may also be saved for later viewing by either *nvprof* or the
*Visual Profiler*.

To use nvprof, one needs to first load the CUDA module:

```bash
module load cuda
```

To profile a CUDA code, one then adds the command `nvprof` before the normal
command to execute the code. Running is otherwise similar to that of any other
CUDA job on [Puhti](running/example-job-scripts-puhti.md#single-gpu) or [Mahti](running/example-job-scripts-mahti.md#1-2-gpu-job-ie-gpusmall-partition).

An example of usage and output of nvprof:
```
$ nvprof dct8x8
======== Profiling result:
Time(%) Time Calls Avg Min Max Name
 49.52 9.36ms 101 92.68us 92.31us 94.31us CUDAkernel2DCT(float*, float*, int)
 37.47 7.08ms 10 708.31us 707.99us 708.50us CUDAkernel1DCT(float*,int, int,int)
 3.75 708.42us 1 708.42us 708.42us 708.42us CUDAkernel1IDCT(float*,int,int,int)
 1.84 347.99us 2 173.99us 173.59us 174.40us CUDAkernelQuantizationFloat()
 1.75 331.37us 2 165.69us 165.67us 165.70us [CUDA memcpy DtoH]
 1.41 266.70us 2 133.35us 89.70us 177.00us [CUDA memcpy HtoD]
 1.00 189.64us 1 189.64us 189.64us 189.64us CUDAkernelShortDCT(short*, int)
 0.94 176.87us 1 176.87us 176.87us 176.87us [CUDA memcpy HtoA]
 0.92 174.16us 1 174.16us 174.16us 174.16us CUDAkernelShortIDCT(short*, int)
 0.76 143.31us 1 143.31us 143.31us 143.31us CUDAkernelQuantizationShort(short*)
 0.52 97.75us 1 97.75us 97.75us 97.75us CUDAkernel2IDCT(float*, float*)
 0.12 22.59us 1 22.59us 22.59us 22.59us [CUDA memcpy DtoA]
```
nvprof supports several very useful running options:

* --export-profile: Export the profile to a file

* --analysis-metrics: Collect profiling data that can be imported to Visual
  Profiler

* --print-gpu-trace: Show trace of function calls

* --openacc-profiling on: Profile OpenACC as well (on by default)

* --cpu-profiling on: Enable some CPU profiling

* --csv --log-file FILE: Generate CSV output and save to FILE; handy for plots
  or benchmarked analysis

* --metrics M1: Measure only metric M1 which is one of the NVIDIA-provided
  metrics which can be listed via --query-metrics.

For more details please check the
[nvidia documentation](https://docs.nvidia.com/cuda/profiler-users-guide/).

!!! note "Note"
     `nvprof` does not support architectures `>SM70`. The [ `nsys`](nsys.md) tool should be used.
